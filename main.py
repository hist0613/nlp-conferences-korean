import os
import re
import time
import json
from tqdm import tqdm

from bs4 import BeautifulSoup
import requests

from gpt import get_openai_summarization
from settings import MAX_NB_GPT3_ATTEMPT, MAX_NB_SHOW


CACHE_FILE = "papers_cache.json"


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)


def update_cache(cache, paper_url):
    # 논문 정보가 캐시에 없는 경우 스크래핑하여 추가
    if paper_url not in cache:
        time.sleep(0.5)  # 요청 사이 지연
        paper_page = get_paper_page(paper_url)
        paper_soup = BeautifulSoup(paper_page.text, "html.parser")
        paper_info = extract_info_aclanthology(paper_soup)
        cache[paper_url] = paper_info

    # 한국어 초록이 캐시에 없는 경우 번역하여 추가
    if "paper_summary_kr" not in cache[paper_url]:
        if not paper_info["paper_authors"] or paper_info["paper_abstract"] is None:
            cache[paper_url]["paper_summary_kr"] = "요약문을 생성할 수 없습니다."
        else:
            cache[paper_url]["paper_summary_kr"] = get_openai_summarization(
                cache[paper_url]["paper_abstract"]
            )

    save_cache(cache)


def get_paper_page(paper_url):
    for trial in range(MAX_NB_GPT3_ATTEMPT):
        try:
            paper_page = requests.get(paper_url)
            if paper_page.status_code == 200:
                break
        except requests.exceptions.ConnectionError as e:
            print(e)
            time.sleep(trial * 30 + 15)
    return paper_page


def extract_info_aclanthology(paper_soup):
    # 논문 제목 추출
    title_section = paper_soup.find("h2", id="title")
    paper_title = title_section.text.strip() if title_section else None

    # Anthology ID 추출
    anthology_id_section = paper_soup.find("dt", string="Anthology ID:")
    paper_comment = (
        anthology_id_section.find_next_sibling("dd").text.strip()
        if anthology_id_section
        else None
    )

    # 논문 권호 추출
    volume_section = paper_soup.find("dt", string="Volume:")
    paper_volume = (
        volume_section.find_next_sibling("dd").a.text.strip()
        if volume_section and volume_section.find_next_sibling("dd").a
        else None
    )

    # 편집자 추출
    editors_section = paper_soup.find("dt", string="Editors:")
    editors_links = (
        editors_section.find_next_sibling("dd").find_all("a") if editors_section else []
    )
    paper_authors = [editor.text.strip() for editor in editors_links]

    # 초록 추출
    abstract_section = paper_soup.find("div", class_="acl-abstract")
    paper_abstract = (
        abstract_section.span.text.strip()
        if abstract_section and abstract_section.span
        else None
    )

    return {
        "paper_title": paper_title,
        "paper_comment": paper_comment,
        "paper_volume": paper_volume,
        "paper_authors": paper_authors,
        "paper_abstract": paper_abstract,
    }


def get_paper_info(paper_url, cache):
    if paper_url in cache and "paper_summary_kr" in cache[paper_url]:
        return cache[paper_url]
    else:
        update_cache(cache, paper_url)
        return cache[paper_url]


def get_paper_list(page_url):
    list_page = requests.get(page_url)
    list_soup = BeautifulSoup(list_page.text, "html.parser")

    papers = []
    for paper_block in list_soup.select("p.d-sm-flex.align-items-stretch"):
        title_tag = paper_block.find("strong").find("a")
        if title_tag:
            title = title_tag.get_text(strip=True)
            paper_url = "https://aclanthology.org" + title_tag["href"]
            papers.append(
                {
                    "title": title,
                    "url": paper_url,
                }
            )

    return papers


def save_papers_to_file(
    papers, volume, start_idx, end_idx, base_dir="summarizations/EMNLP2023"
):
    os.makedirs(base_dir, exist_ok=True)
    file_name = f"papers-{start_idx:04d}-{end_idx:04d}-{volume}.md"
    file_path = os.path.join(base_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as fp:
        fp.write(
            f"# Korean Three-Line Summarizations of Papers {start_idx}-{end_idx} in {volume}\n"
        )
        for paper_info in papers:
            response_text = (
                f"###### {paper_info['paper_title']} ({paper_info['url']})\n"
            )
            response_text += f"- Anthology ID: {paper_info['paper_comment']} \n"
            response_text += f"- Volume: {paper_info['paper_volume']} \n"
            response_text += f"- Summary: \n" + "\n".join(
                ["    " + line for line in paper_info["paper_summary_kr"].split("\n")]
            )
            response_text += "\n\n"
            fp.write(response_text)


if __name__ == "__main__":
    cache = load_cache()
    papers = get_paper_list("https://aclanthology.org/events/emnlp-2023/")

    temp_papers = []
    prev_volume = ""
    start_idx = 1

    for paper_idx, paper_info in tqdm(enumerate(papers, 1)):
        full_paper_info = get_paper_info(paper_info["url"], cache)
        paper_info.update(full_paper_info)

        if prev_volume != paper_info["paper_volume"]:
            if prev_volume:
                end_idx = paper_idx - 1
                save_papers_to_file(temp_papers, prev_volume, start_idx, end_idx)
                temp_papers = []
                start_idx = paper_idx
            prev_volume = paper_info["paper_volume"]

        temp_papers.append(paper_info)
        if len(temp_papers) >= MAX_NB_SHOW:
            end_idx = paper_idx
            save_papers_to_file(temp_papers, prev_volume, start_idx, end_idx)
            temp_papers = []
            start_idx = paper_idx + 1

    if temp_papers:
        end_idx = paper_idx
        save_papers_to_file(temp_papers, prev_volume, start_idx, end_idx)
