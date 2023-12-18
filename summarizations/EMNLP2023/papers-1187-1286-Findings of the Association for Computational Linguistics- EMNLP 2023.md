# Korean Three-Line Summarizations of Papers 1187-1286 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Findings of the Association for Computational Linguistics: EMNLP 2023 (https://aclanthology.org/2023.findings-emnlp.0/)
- Anthology ID: 2023.findings-emnlp.0 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors:  
- Summary: 
    요약문을 생성할 수 없습니다.

###### Multi Document Summarization Evaluation in the Presence of Damaging Content (https://aclanthology.org/2023.findings-emnlp.1/)
- Anthology ID: 2023.findings-emnlp.1 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Multi-document summarization (MDS) task에서는 여러 개의 문서에 대한 요약을 생성한다. 그런데 일부 문서에는 various reasons로 인해 독자에게 노출되어서는 안 되는 damaging documents가 있다. 
    2. 기존 메트릭들은 요약의 관련성과 일관성을 평가하지만, 우리는 damaging documents를 올바르게 처리하는 MDS 시스템의 능력을 측정하는 두 가지 새로운 평가 메트릭을 제안한다.  
    3. 실험을 통해 우리의 메트릭이 MDS 시스템에서 damaging content를 제거하면서 문서의 요약을 제대로 처리하는 능력을 효과적으로 측정할 수 있음을 보였다.

###### Guiding AMR Parsing with Reverse Graph Linearization (https://aclanthology.org/2023.findings-emnlp.2/)
- Anthology ID: 2023.findings-emnlp.2 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Abstract Meaning Representation (AMR) 파싱은 주어진 문장으로부터 추상적 의미 그래프를 추출하는 것을 목표로 한다. 기존의 시퀀스-투-시퀀스 접근법은 의미 그래프를 노드와 엣지의 시퀀스로 선형화하고 직접 선형화된 그래프를 생성하는 방식으로 좋은 성능을 달성하였다. 
    2. 그러나 이러한 접근법에서는 디코딩 과정에서 구조 손실이 누적되는 현상이 발생하고, 그로 인해 이후에 디코딩된 노드와 엣지의 F1-점수가 이전에 디코딩된 것보다 훨씬 낮게 나타난다.
    3. 이 문제를 해결하기 위해 우리는 새로운 Reverse Graph Linearization (RGL) 향상 프레임워크를 제안한다. RGL은 AMR 그래프의 기본 및 역 선형화 순서를 정의하며, 기본 순서의 뒷부분에 나타나는 대부분의 구조가 역순서의 앞부분에 나타나고 그 반대도 성립한다. RGL은 역순서 선형화를 기존의 AMR 파서에 두 번의 셀프 디스틸레이션 메커니즘을 통해 통합시키고, 모델이 기본 선형화를 생성하는 동안 모델을 가이드한다.

###### Translate the Beauty in Songs: Jointly Learning to Align Melody and Translate Lyrics (https://aclanthology.org/2023.findings-emnlp.3/)
- Anthology ID: 2023.findings-emnlp.3 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 'Song translation'은 가사 번역과 음악적 알맞은 맞춤을 모두 다루어야 하는데,  이는 번역 과정의 어려운 문제로 관심을 받고 있다.
    2. 본 논문에서는 lyric 번역과 가사-멜로디 맞춤을 동시에 모델링하는 Lyrics-Melody Translation with Adaptive Grouping (LTAG)를 제안한다.
    3. 훈련 데이터 부족 문제를 해결하기 위해 back-translation 방법을 사용하였고, 영어-중국어 가사 번역 데이터셋에서 실험한 결과, 모델의 효과성을 확립했다.

###### Aksharantar: Open Indic-language Transliteration datasets and models for the Next Billion Users (https://aclanthology.org/2023.findings-emnlp.4/)
- Anthology ID: 2023.findings-emnlp.4 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 스크립트 사용과 로마자 표기법의 인도어 문맥에서 Transliteration은 매우 중요하지만, 훈련 및 평가 세트가 공개적으로 제공되는 경우가 드물다.
    2. 본 논문에서는 모노링글 및 병렬 코퍼스에서 마이닝하고, 의사결정자들로부터 데이터를 수집하여 인도어 언어에 대한 가장 큰 공개적인 Transliteration 데이터셋인 Aksharantar를 소개한다.
    3. Aksharantar는 21개의 인도어 언어로 총 26백만 개의 Transliteration 쌍을 가지고 있으며, 기존 데이터셋의 21배 크기이며 7개 언어와 1개 언어 가족에 대한 최초의 공개 데이터셋이다.

###### Pretraining Without Attention (https://aclanthology.org/2023.findings-emnlp.5/)
- Anthology ID: 2023.findings-emnlp.5 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP에서 pretraining 성공에 Transformers는 필수적인 역할을 한다. 
    2. 하지만 다른 아키텍처를 사용하면 downstream 정확성은 현저히 나빠지거나 GLUE와 같은 표준 벤치마크에는 attention layer가 필요하다. 
    3. 이 연구는 최근 state-space 모델 기반의 순서 라우팅의 진보를 이용하여 attention 없이 pretraining을 탐구한다.

###### Time-Aware Representation Learning for Time-Sensitive Question Answering (https://aclanthology.org/2023.findings-emnlp.6/)
- Anthology ID: 2023.findings-emnlp.6 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 문제 해결에서 시간은 중요한 요소 중 하나이지만, 기존 QA 데이터셋에는 충분한 시간 표현이 없어 언어 모델은 'after'와 'before'와 같은 시간 표시자와 숫자 사이의 관계를 이해하는 데 어려움을 겪는다.
    2. 이 문제를 해결하기 위해, 우리는 시간-문맥 정보를 고려한 질문 응답 (TCQA) 프레임워크를 제안한다.
    3. TCQA로 훈련된 모델이 TimeQA 데이터셋에서 8.5의 F1-점수를 넘어서는 등 베이스라인 모델보다 성능이 우수함을 실험적으로 보여준다.
    
    (Note: It seems like the term "TimeQA" refers to a specific dataset.)

###### EffEval: A Comprehensive Evaluation of Efficiency for MT Evaluation Metrics (https://aclanthology.org/2023.findings-emnlp.7/)
- Anthology ID: 2023.findings-emnlp.7 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 효율성은 LLMs 시대에 인클루저브성을 증진시키고 환경적 비용을 줄이기 위한 중요한 속성이다. 본 연구에서는 MT 평가 메트릭의 효율성에 대한 철저한 평가를 제공한다.
    2. 우리의 접근은 계산 집약적인 transformers를 가벼운 대안으로 대체하고, LLM 표현 위에 정렬 알고리즘에 대한 선형 및 이차 근사를 사용하는 것이다.
    3. 결과적으로 TinyBERT가 품질과 효율성 사이의 최적의 균형을 제공하며, CPU 속도 향상은 GPU보다 훨씬 크다는 것을 보였다.

###### Unsupervised Opinion Summarization Using Approximate Geodesics (https://aclanthology.org/2023.findings-emnlp.8/)
- Anthology ID: 2023.findings-emnlp.8 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의견 요약은 사용자 리뷰로부터 유명한 의견을 잡아내는 작업이다. 이 논문에서는 데이터에 대한 사전 지식이 필요하지 않는 비지도 추출적 의견 요약 시스템인 GeoSumm을 소개한다. GeoSumm은 인코더-디코더 기반 표현 학습 모델로 구성되어 텍스트의 토픽별 표현을 생성한다.
    2. 이러한 토픽별 표현은 학습 가능한 잠재 단위의 분포로써 텍스트의 맥락을 포착한다. GeoSumm은 디코더의 여러 레이어에서 사전 학습한 텍스트 표현을 기반으로 사전 학습을 수행하여 이러한 토픽별 표현을 생성한다.
    3. 우리는 이러한 토픽별 표현을 사용하여 새로운 근사 Geodesic 거리 기반의 스코어링 메커니즘을 이용하여 리뷰 문장의 중요성을 정량화한다. 이 중요성 점수를 사용하여 일반적인 의견 및 측면별 요약을 작성한다. GeoSumm은 세 가지 의견 요약 데이터셋에서 강력한 성능을 달성하고 있으며, 모델의 작동 방식을 분석하고 다양한 도메인에서 GeoSumm의 일반화 능력을 보여주기 위해 추가 실험을 수행한다.

###### Investigating the Frequency Distortion of Word Embeddings and Its Impact on Bias Metrics (https://aclanthology.org/2023.findings-emnlp.9/)
- Anthology ID: 2023.findings-emnlp.9 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 연구들은 정적인 단어 임베딩이 단어의 빈도를 인코딩할 수 있다고 보여주었으나, 이러한 동작에 대해서는 덜 연구되어 왔다. 
    2. 이 연구에서 우리는 정적인 단어 임베딩에서 빈도와 의미 유사성 사이의 관계가 어떻게 관련되어 있는지 연구하고, 이러한 관계가 임베딩 기반 편향 메트릭에 미치는 영향을 평가한다. 
    3. 우리는 Skip-gram, GloVe, FastText 임베딩이 높은 빈도 단어 사이의 유사성이 다른 빈도 조합 사이의 것보다 높은 경향을 가지도록 한다는 것을 발견하였다.

###### Improving Classifier Robustness through Active Generative Counterfactual Data Augmentation (https://aclanthology.org/2023.findings-emnlp.10/)
- Anthology ID: 2023.findings-emnlp.10 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Counterfactual 데이터 증강(CDA)은 자연어 분류기의 robustness를 향상시키기 위해 일반적으로 사용되는 기술이다. 하지만 meaningful한 counterfactual을 발견하고 효율적으로 라벨링하는 것은 인간의 비용을 최소화하는 문제점이 있는데, 이 논문에서는 counterfactual 생성 모델을 이용하여 더 많은 다양한 counterfactual을 생성하고 학습된 보조 분류기로 자동으로 라벨을 달 수 있는 framework를 제안한다.
    2. 생성된 counterfactual들에 대해 원래의 예시와의 관계를 보간하는 pairwise 분류기를 훈련시킴으로써 보다 정확하게 라벨을 달 수 있다는 통찰력을 제공한다.
    3. 작은 양의 인간-라벨링된 counterfactual 데이터(10%)로 학습된 라벨을 가진 counterfactual 증강 데이터셋을 생성할 수 있으며, 이를 통해 sentiment classification과 question paraphrase 태스크에서 robustness를 18-20% 향상시키고 6개의 도메인 외 데이터셋에서 에러를 14-21% 감소시킬 수 있다는 것을 실험적으로 보여준다.

###### Data Augmentation Techniques for Machine Translation of Code-Switched Texts: A Comparative Study (https://aclanthology.org/2023.findings-emnlp.11/)
- Anthology ID: 2023.findings-emnlp.11 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 데이터 부족 문제를 해결하기 위한 코드 스위칭(CSW) 텍스트 생성이 점점 주목받고 있다. 이 연구에서는 세 가지 인기있는 augmentation 접근 방식인 용어 대체, 언어학 이론, 배후 번역(back-translation)을 이집트 아라비아어-영어 코드 스위칭 문맥에서 비교하였다.
    2. CSW 평행 데이터로 학습된 배후 번역과 CSW 예측 기반 용어 대체가 두 가지 작업에 대해 가장 좋은 성능을 보였다.
    3. 언어학적 이론과 임의의 용어 대체는 CSW 평행 데이터가 없는 경우에 효과적이었으며, 두 가지 접근 방식 모두 유사한 결과를 달성했다.

###### On the Relation between Sensitivity and Accuracy in In-Context Learning (https://aclanthology.org/2023.findings-emnlp.12/)
- Anthology ID: 2023.findings-emnlp.12 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "In-context learning(ICL)은 prompt에 대해 너무 민감해서 실제 상황에서 신뢰성이 떨어진다. 이 연구에서는 ICL의 다양한 변형에 대한 민감도를 조사했다."
    2. "실험 결과, ICL의 민감도와 정확도 사이에 강한 음의 상관관계를 발견했다. 민감한 예측은 정확하지 않을 가능성이 높다."
    3. "이러한 결과를 바탕으로, 우리는 SenSel이라는 few-shot selective prediction 방법을 제안한다. 실험 결과, SenSel은 abstention 결정에서 두 가지 기존 기법을 일관되게 능가한다."

###### Self-distilled Transitive Instance Weighting for Denoised Distantly Supervised Relation Extraction (https://aclanthology.org/2023.findings-emnlp.13/)
- Anthology ID: 2023.findings-emnlp.13 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. distant supervision을 이용한 관계 추출에서 잘못된 레이블이 존재하는 것은 큰 문제로 인식되고 있으며, 기존 연구는 이러한 잡음을 완화하기 위해 bag-level 학습을 하는 경우가 많았다. 
    2. 이 논문에서는 중간 출력의 정보를 활용하여 동적인 인스턴스 가중치를 생성하는 새로운 Transitive Instance Weighting 메커니즘을 제안하여 잘못된 레이블이 있는 경우에도 효과적으로 대응하는 것을 목표로 한다. 
    3. 실험 결과는 우리의 방법이 state-of-the-art 성과를 달성하며, 기준 모델 대비 일관된 성능 향상을 보여준다.

###### MWE as WSD: Solving Multiword Expression Identification with Word Sense Disambiguation (https://aclanthology.org/2023.findings-emnlp.14/)
- Anthology ID: 2023.findings-emnlp.14 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 단어 의미 구분 (WSD) 접근법은 인풋 콘텍스트 외에 의미 설명서의 인코딩을 활용하여 성능을 향상시키고 있다. 본 연구에서는 이러한 접근법을 사용하여 다중단어 표현 (MWE) 식별에 적용할 수 있음을 보여주었다.
    2. 우리의 방법은 규칙 기반 추출 파이프라인에서 생성되는 MWE 후보들을 필터링하는 데에 의미 설명서와 콘텍스트 정보를 사용하는 모델을 훈련시켰다.
    3. 우리의 접근법은 DiMSUM 데이터셋에서 최대 1.9 F1 포인트의 성능 향상을 이끌어내어 MWE 식별에서 최고 성능을 보여주고, PARSEME 1.1 영어 데이터셋에서도 경쟁력 있는 결과를 달성하였다. 또한, 우리의 모델은 WSD 성능의 대부분을 유지하며, 두 가지 작업에 하나의 모델을 사용할 수 있다는 것을 보여준다.

###### Dual Contrastive Learning Framework for Incremental Text Classification (https://aclanthology.org/2023.findings-emnlp.15/)
- Anthology ID: 2023.findings-emnlp.15 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 증분 학습은 온라인 지식 발견의 맥락에서 중요한 역할을 한다. 바다 모델 (Language Model)이 지속적으로 지식을 학습하고 갱신할 수 있도록 도와준다.
    2. 우리는 이 논문에서 다운스트림 시퀀스 태스크로 잘 전달될 수 있는 더욱 일반화된 임베딩 공간을 학습하는 데 초점을 맞추고 있다.
    3. 우리는 Dual Contrastive Learning (DCL) 기반 프레임워크를 제안하여 다른 태스크간에 임베딩의 전이성을 향상시키고, 과적합 현상을 감소시키며, 다양한 텍스트 데이터셋에서 우수한 성능을 달성하고 있다.

###### Reference Free Domain Adaptation for Translation of Noisy Questions with Question Specific Rewards (https://aclanthology.org/2023.findings-emnlp.16/)
- Anthology ID: 2023.findings-emnlp.16 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기술 분야 내의 질문-답변(CQA) 포털은 조직 내 사용자들에게 도움이 되는 가치있는 도구로 작용하지만, 영어를 구사하지 못하는 사용자들에게 접근 가능하게 만드는 것은 여전히 도전과제이다. 
    2. 이 논문에서는 Neural Machine Translation (NMT)을 사용하여 질문을 번역하는 것이 어려운 noisy한 환경에 대응하기 위한 훈련 방법론을 제안한다. 
    3. 기존의 synthetic target data에 의존하는 방법들 보다 더 나은 성능을 보이며, 잡음이 있는 데이터에 대해서도 robust하게 동작하는 것을 입증하였다.

###### Filtered Semi-Markov CRF (https://aclanthology.org/2023.findings-emnlp.17/)
- Anthology ID: 2023.findings-emnlp.17 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 전통적인 Linear Chain CRF 대신, Semi-Markov CRF가 Named Entity Recognition (NER)과 같은 텍스트 분할 작업에 대안으로 제안되었다. 단어 수준 예측이 아닌 Segment를 기본 단위로 취급하기 때문에 더 표현력이 우수하다.
    2. 하지만 Semi-CRF는 두 가지 주요 문제가 있다: (1) 입력 시퀀스의 모든 Span에 대해 동작하기 때문에 시퀀스 길이에 대해 이차 복잡성이 발생한다는 것와 (2) NER과 같은 시퀀스 레이블링 작업에서 CRF보다 성능이 떨어진다는 것.
    3. 본 논문에서는 필터링 단계를 통해 관련 없는 Segment를 제거하여 복잡성과 탐색 공간을 줄이는, Semi-CRF의 변형인 Filtered Semi-Markov CRF를 소개한다. 우리의 접근법은 여러 NER 벤치마크에서 CRF와 Semi-CRF보다 우수한 성능을 발휘함과 동시에 훨씬 빠르다.

###### Data Pruning for Efficient Model Pruning in Neural Machine Translation (https://aclanthology.org/2023.findings-emnlp.18/)
- Anthology ID: 2023.findings-emnlp.18 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 큰 규모의 사전 훈련된 언어 모델의 메모리 요구량과 추론 시간을 줄이기 위해 모델 가지치기 방법을 사용할 수 있는데,이 논문에서는 데이터 가지치기와 이동 가지치기를 결합하여 효율적인 fine-pruning을 가능하게 했다.
    2. 개별 훈련 인스턴스의 Cross-entropy 점수들을 활용하여 데이터셋 가지치기 전략을 설계하였고, 루마니아어-영어 및 터키어-영어 번역 과업에서 데이터셋 가지치기 방법이 다른 방법에 비해 우수한 성능을 보였다.
    3. 데이터 가지치기는 수렴에 필요한 전체 단계와 이동 가지치기의 훈련 시간을 줄이는 것을 실험적으로 보여주었으며, NMT의 상황에서 데이터와 모델 가지치기의 상호작용을 이해하기 위해 새로운 통찰력을 얻었다.

###### Long-Form Speech Translation through Segmentation with Finite-State Decoding Constraints on Large Language Models (https://aclanthology.org/2023.findings-emnlp.19/)
- Anthology ID: 2023.findings-emnlp.19 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 음성 번역에서의 한 가지 어려움은 말하는 내용이 긴 형태일 때, 고품질의 번역을 위해 짧은 단위가 필요하지만 이 불일치를 해결하기 위해 큰 언어 모델 (LLM)을 사용하여 긴 ASR 트랜스크립트를 독립적으로 번역 가능한 세그먼트로 분할한다.
    2. 우리는 디코딩 중 유효하지 않은 출력을 제거하기 위해 유한 상태 제약 조건을 포함하여 LLM의 환각되는 경향을 극복한다.
    3. 우리는 prompt-tuning이나 fine-tuning을 통해 ASR 오류가 포함된 트랜스크립트에 대해서도 LLM이 적응 가능함을 발견하였고, 최고의 LLM은 분할을 향상시킴으로써 9개의 테스트 세트에서 영어-독일어, 영어-스페인어, 영어-아라비아어 TED 강연 번역에서 평균 BLEU를 2.9 포인트 향상시켰다.

###### Re-Temp: Relation-Aware Temporal Representation Learning for Temporal Knowledge Graph Completion (https://aclanthology.org/2023.findings-emnlp.20/)
- Anthology ID: 2023.findings-emnlp.20 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Temporal Knowledge Graph Completion (TKGC)는 미래의 사실을 기반으로 누락된 엔티티를 예측하는데 실제 예측 문제와 더 가까워 실제적인 도전 과제를 제시한다. 
    2. 기존 연구들은 주로 최근 스냅샷에 적용하는 sequential graph neural networks를 사용하여 entity와 relation을 인코딩하지만, 이러한 방식은 쿼리에 나타난 entity와의 관련 관계를 고려하여 관련 없는 스냅샷을 건너뛰는 능력과 명시적인 시간 정보의 중요성을 간과하기 쉽다.
    3. 이를 해결하기 위해 우리는 명시적인 시간 임베딩을 입력으로 사용하고 각 타임스탬프 이후에 스킵 정보 흐름을 통합하여 예측에 불필요한 정보를 건너뛰는 모델인 Re-Temp (Relation-Aware Temporal Representation Learning)을 제안한다. 또한 정보 누출을 막기 위해 두 단계의 전방 전파 방법을 도입한다. 6개의 TKGC (extrapolation) 데이터셋에서 실시한 평가를 통해 우리의 모델이 최근 8개의 state-of-the-art 모델보다 큰 폭으로 우수한 성능을 보여주었다."

###### RethinkingTMSC: An Empirical Study for Target-Oriented Multimodal Sentiment Classification (https://aclanthology.org/2023.findings-emnlp.21/)
- Anthology ID: 2023.findings-emnlp.21 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근, 타겟 지향적 다중 모달 감성 분류(TMSC)가 학계에서 큰 관심을 받고 있으나, 현재의 다중 모달 모델은 성능 한계에 도달했다. 
    2. 이 논문에서는 어떤 모달이 TMSC에 있어서 더 중요한지, 어떤 다중 모달 퓨전 모듈이 더 효과적인지, 기존 데이터셋이 연구를 충분히 지원하는지 등을 연구하고 있다. 
    3. 실험과 분석 결과, 현재의 TMSC 시스템은 최대한 많은 타겟의 감성을 텍스트로만 결정할 수 있기 때문에 텍스트 모달에 주로 의존하고 있다는 것을 보여주었다. 따라서 모델 디자인과 데이터셋 구축을 위해 여러 가지 방향을 제안하고 있다.

###### Lexical Entrainment for Conversational Systems (https://aclanthology.org/2023.findings-emnlp.22/)
- Anthology ID: 2023.findings-emnlp.22 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템은 인간과 같은 특징을 갖추기를 기대되고 있다. 이 논문은 lexical entrainment (LE)이라는 현상을 다룬다. LE는 대화 상대방의 어휘 선택에 맞게 어휘를 조정하는 현상으로, 대화의 명확성과 모호성 감소를 위해 LE를 대화 시스템에 명시적으로 통합하는 방법을 제안한다.
    2. LE 현상을 대화 시스템에 통합하기 위해, MultiWOZ-ENTR이라는 새 데이터셋과 대화 시스템을 위한 LE 측정 방법을 제안한다.
    3. 또한, LE 추출 작업과 LE 생성 작업을 위한 두 가지 기준선 접근법을 제시한다. LE 추출 작업은 대화 맥락에서 LE 표현을 감지하는 것을 목표로 한다.

###### AutoReply: Detecting Nonsense in Dialogue with Discriminative Replies (https://aclanthology.org/2023.findings-emnlp.23/)
- Anthology ID: 2023.findings-emnlp.23 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 대화 모델이 자신의 메시지에 오류를 감지할 수 있다고 보여준다. "이해하지 못했다" 라는 대답의 가능성을 계산하여 부적절한 메시지를 감지할 수 있다. 
    2. 미리 정의된 대답들로 이루어진 AutoReply를 사용하여 복잡한 어플리케이션인 Diplomacy에서도 효과적으로 말이 안되는 대화를 감지할 수 있음을 보여준다. 
    3. AutoReply는 소수의 주석이 달린 대화 예시를 기반으로 자동으로 최적의 대답을 탐색하며, 이는 수동으로 만든 대답과 성능이 비슷하다.

###### Follow-on Question Suggestion via Voice Hints for Voice Assistants (https://aclanthology.org/2023.findings-emnlp.24/)
- Anthology ID: 2023.findings-emnlp.24 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Alexa나 Siri와 같은 음성 비서의 사용이 급속히 증가함에 따라 사용자는 음성 검색을 통해 즉시 정보에 접근할 수 있다. 그러나 음성 기반의 상황에서 질의 제안은 단순한 일이 아니다.
    2. 이 논문에서는 사용자가 계속 질문할 수 있도록 간결하고 자연스러운 음성 힌트를 제공하는 새로운 작업인 "질문 제안"에 도전한다.
    3. 우리는 기존의 모델과 sequence-to-sequence Transformer를 사용하여 질문 목록에서 음성 힌트를 생성하기 위한 방법을 제안하고, 새로운 데이터셋을 사용하여 이를 평가한다. 평가 결과, 단순히 질문을 연결하는 것보다 언어학적으로 기반된 사전 훈련 과정을 적용한 접근법이 가장 자연스러운 힌트를 생성하는 데 사람들이 더 선호함을 보였다.

###### Bidirectional Masked Self-attention and N-gram Span Attention for Constituency Parsing (https://aclanthology.org/2023.findings-emnlp.25/)
- Anthology ID: 2023.findings-emnlp.25 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 어텐션 메커니즘은 특히 자연어 처리(NLP) 태스크에서 심층 학습의 중요한 요소가 되었다. 그러나, 어텐션 메커니즘은 문장 범위를 형성하는 데 필요한 방향성 정보를 부족하게 할 수 있다. 
    2. 이 문제를 해결하기 위해, 우리는 Bidirectional masked and N-gram span Attention (BNA) 모델을 제안한다. 이 모델은 어텐션 메커니즘을 수정하여 각 단어 사이의 명확한 종속성을 포착하고 출력 범위 벡터의 표현을 강화한다. 
    3. 제안된 모델은 Penn Treebank와 Chinese Penn Treebank 데이터셋에서 최고의 성능을 달성하며, 각각 96.47과 94.15의 F1 스코어를 기록한다. 축소 연구와 분석은 BNA 모델이 양방향 종속성을 통해 각 단어를 문장에 맥락화하고 범위 표현을 향상시키는 데 효과적임을 보여준다.

###### CR-COPEC: Causal Rationale of Corporate Performance Changes to learn from Financial Reports (https://aclanthology.org/2023.findings-emnlp.26/)
- Anthology ID: 2023.findings-emnlp.26 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "이 논문에서는 CR-COPEC라고 불리는 자율 상업 성능 변화의 인과관계를 갖는(rationale) 기업들의 재무 보고서를 소개한다."
    2. 이 데이터셋은 전문가의 인과분석을 포현하는 방식으로 U.S. 기업들의 10-K 연간보고서로부터 인과관계를 탐지한다. 
    3. CR-COPEC는 기업의 재무 성과에 영향을 미치는 다양한 특성들을 고려하여 다양한 산업에서도 유일한 내러티브를 고려하여 인과 문장을 식별할 수 있다.

###### Plausibility Processing in Transformer Language Models: Focusing on the Role of Attention Heads in GPT (https://aclanthology.org/2023.findings-emnlp.27/)
- Anthology ID: 2023.findings-emnlp.27 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 Transformer 언어 모델이 명사-동사 관계의 타당성 처리를 어떻게 수행하는지, 특히 심층적인 지식에 대해서 탐구하는 것이다. 
    2. 실험 결과, GPT2는 다른 Transformer 언어 모델들과 비교했을 때 명사-동사 관계의 타당성 처리에서 사람과 더 비슷한 특성을 보였다. 
    3. 또한, GPT2의 attention heads가 타당성에 대한 지식을 갖고 있으며 이러한 heads가 GPT2의 타당성 처리 능력에 인과적으로 기여한다는 것을 실험 결과를 통해 확인하였다.

###### Automatic Unit Test Data Generation and Actor-Critic Reinforcement Learning for Code Synthesis (https://aclanthology.org/2023.findings-emnlp.28/)
- Anthology ID: 2023.findings-emnlp.28 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 큰 사전 훈련 언어 모델의 등장으로 코드 합성 (Code Synthesis) 분야에서 놀라운 성능을 보이고, Language Modelling (LM) 목적으로 훈련된 자연어 생성(Natural Language Generation)과 유사한 방식으로 Code Generation 문제를 다룬다.
    2. RL 기반 방법은 기존에 정의된 Unit Tests에 기반한 보상 신호에 의존하는데, 이러한 Unit Tests를 정의하는 것은 사전 훈련 데이터셋과 비교해 어렵다. 따라서 이 논문에서는 Code Synthesis 모델의 RL 훈련을 위해 자동으로 함수 시그니처와 관련된 Unit Tests 데이터를 얻는 것을 제안한다.
    3. 또한, 단순하지만 효과적인 Actor-Critic 기반 RL 훈련 방법을 도입하고, 자동 생성 된 훈련 데이터와 함께 사용하면 기존의 code synthesis LM에 비해 최대 9.9%의 성능 향상을 가져오며, 표준 PPO 또는 CodeRL로 훈련된 RL 기반 모델에 비해 최대 4.3%의 성능 향상을 얻을 수 있다.

###### Unlocking the Heterogeneous Landscape of Big Data NLP with DUUI (https://aclanthology.org/2023.findings-emnlp.29/)
- Anthology ID: 2023.findings-emnlp.29 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대용량 코퍼스의 자동 분석은 시간 효율성 관점에서 복잡한 작업이다. 이에 NLP 분야에서 유연하고 확장가능한 텍스트 분석을 위한 적합한 프레임워크가 없다는 문제가 있다. 이 논문은 이러한 문제를 해결하기 위해 Docker Unified UIMA Interface(DUUI)를 제안한다.
    2. DUUI는 대용량 텍스트 코퍼스의 자동 분석을 위한 확장 가능하고 유연하며 가벼운 웹 프레임워크로, Docker를 통해 빅데이터 경험과 가상화 기술을 활용한다. 
    3. DUUI의 통신 접근 방식은 최신 기술과 비교하여 우수한 시간 효율성을 보여주며, 대용량 텍스트 데이터의 분석이 가능하게 한다.

###### Towards Agile Text Classifiers for Everyone (https://aclanthology.org/2023.findings-emnlp.30/)
- Anthology ID: 2023.findings-emnlp.30 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 기반 안전 분류기는 콘텐츠 관리에 널리 사용되며 점점 더 디지털 어시스턴트와 챗봇의 안전 기능 조정에 사용되고 있다.
    2. 이 논문에서는 특정 정책을 빠르게 개발할 수 있는 작은 목표 데이터셋을 사용하여 분류기를 훈련시키는 "민첩한 텍스트 분류" 방법을 소개하고 평가한다.
    3. 작은 데이터셋으로도 최첨단 성능을 달성할 수 있으며, 이를 통해 대규모 안전 분류기를 개발하는데 필요한 시간과 자원을 대폭 줄일 수 있다.

###### Beyond Good Intentions: Reporting the Research Landscape of NLP for Social Good (https://aclanthology.org/2023.findings-emnlp.31/)
- Anthology ID: 2023.findings-emnlp.31 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP의 발전과 함께 다양한 분야에서 다양한 NLP 응용 프로그램이 나타나고 있지만, 이러한 연구들이 오늘날의 사회적 문제를 다루고 있는지는 연구자들에게 항상 분명하지 않다. 
    2. 따라서 이 논문에서는 NLP4SGPapers라는 과학적 데이터셋과 관련된 세 가지 작업을 소개하고, NLP4SG 논문을 식별하고 NLP4SG의 경험을 파악할 수 있게 한다. 
    3. 이 논문은 최신 NLP 모델을 사용하여 이러한 작업을 수행하고, ACL Anthology 전체에 적용하여 NLP4SG 분야의 포괄적인 개요를 제공한다.

###### PAXQA: Generating Cross-lingual Question Answering Examples at Training Scale (https://aclanthology.org/2023.findings-emnlp.32/)
- Anthology ID: 2023.findings-emnlp.32 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 질의응답(QA) 시스템들의 성공은 대량의 고품질 훈련 데이터에 기인하고 있다. 하지만 이러한 주석 작업은 비용이 많이 들며, 크로스-언어 환경에서는 어려움이 더욱 증가한다. 이 논문에서는 기존 병렬 말뭉치로부터 간접 감독을 활용한 재원화된 크로스-언어 QA 데이터 생성 방법을 제안한다.
    2. "PAXQA"라고 명명한 이 방법은 크로스-언어 QA를 두 단계로 분해한다. 첫 번째 단계에서는 질문 생성(QG) 모델을 영어 쪽에 적용한다. 두 번째 단계에서는 질문과 답변을 번역하기 위해 주석 투사(annotation projection)를 적용한다.
    3. PAXQA를 적용하여 4개 언어(총 662,000개의 예제)에 대한 크로스-언어 QA 예제를 생성하고 인간 평가를 수행한 결과, 이 데이터셋으로 미세 조정된 모델이 기존의 재원화된 데이터 생성 모델들보다 추출 기반 QA 데이터셋에서 우수한 성능을 보였다. 특히, 영어 이외의 언어로 된 질문과 영어로 된 맥락의 경우 가장 큰 성능 향상이 있었다.

###### Sharing, Teaching and Aligning: Knowledgeable Transfer Learning for Cross-Lingual Machine Reading Comprehension (https://aclanthology.org/2023.findings-emnlp.33/)
- Anthology ID: 2023.findings-emnlp.33 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Cross-lingual machine reading comprehension (MRC)에서는 다른 언어에서의 답 위치의 변동 때문에 크로스-언어적 전송을 향상시키기 위한 깊은 수준의 지원을 제공하기 어렵다."
    2. X-STA는 크로스-언어적 MRC를 위한 새로운 접근법으로, attenive한 '선생님'을 활용하여 소스 언어의 답 위치를 목표 출력 공간으로 subtle하게 전달한다. Gradient-Disentangled Knowledge Sharing 기법을 제안하여 교차 어텐션 블록을 더 개선시켰다.
    3. 실험 결과는 우리의 방법이 최신의 접근법들보다 효과적이며, 3가지의 다국어 MRC 데이터셋에서 우수한 결과를 보여준다.

###### BERT Goes Off-Topic: Investigating the Domain Transfer Challenge using Genre Classification (https://aclanthology.org/2023.findings-emnlp.34/)
- Anthology ID: 2023.findings-emnlp.34 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 사전 훈련 언어 모델(Pretrained Language Model, PLM)의 성능으로 많은 텍스트 분류 작업의 성능이 향상되었지만, 토픽의 분포가 변하는 경우 성능 차이가 여전히 발생한다.
    2. 우리는 대량의 말뭉치와 다양한 주제를 사용하여 이 현상을 실험적으로 확인하고, 도메인 전이가 전혀 계속 어렵다는 것을 확인했다.
    3. 우리는 훈련 코퍼스에 특정 장르와 주제로 동시에 있는 문서가 없어도 원하는 장르와 주제의 텍스트를 생성하는 데이터 증강 방법을 개발했다. 이를 사용하여 훈련 데이터셋을 증강하면 일부 주제에서 F1 점수가 50%까지 향상되며, 다른 주제에서는 거의 향상되지 않는다.

###### Toward Stronger Textual Attack Detectors (https://aclanthology.org/2023.findings-emnlp.35/)
- Anthology ID: 2023.findings-emnlp.35 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 적대적 공격의 다양성이 급증함에 따라 딥 NLP 시스템의 무결성에 대한 우려와 심각한 위협이 제기되고 있지만, 이를 방어하기 위한 연구는 아직 많이 이루어지지 않았다.
    2. 이 논문은 텍스트 적대적 공격을 탐지하기 위한 LAROUSSE 프레임워크를 소개하고, STAKEOUT이라는 새로운 벤치마크를 제안한다. 
    3. LAROUSSE는 비지도 학습 기반이며 하이퍼파라미터 없고 미분 가능하지 않기 때문에 기울기 기반 방법에 대해 보호되며, STAKEOUT은 다양한 실험을 통해 LAROUSSE가 이전에 제안된 방법들보다 우수하게 작동하며, 탐지율의 변동에 대한 흥미로운 요인을 확인하는 데 사용될 수 있는 강력한 평가 프레임워크를 제공한다.

###### MEAL: Stable and Active Learning for Few-Shot Prompting (https://aclanthology.org/2023.findings-emnlp.36/)
- Anthology ID: 2023.findings-emnlp.36 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 고정된 데이터셋에서의 few-shot classification은 run to run variability가 높아 비교가 어렵고, 많은 실제 어플리케이션에 대해서 신뢰할 수 없게 만든다. 
    2. 이 논문에서는 run variability를 줄이기 위해 새로운 앙상블 기법을 제안하고, 데이터셋을 선택하기 위한 새로운 active learning 기준을 소개한다.
    3. 실험을 통해 제안된 MEAL (Multiprompt finetuning and prediction Ensembling with Active Learning) 방법이 prompt-based finetuning의 성능을 2.3개 향상시킨다는 것을 보여준다.

###### Structure and Label Constrained Data Augmentation for Cross-domain Few-shot NER (https://aclanthology.org/2023.findings-emnlp.37/)
- Anthology ID: 2023.findings-emnlp.37 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Cross-domain few-shot named entity recognition (NER)은 소스 도메인의 관련 지식을 활용하여 제한된 레이블 데이터로 대상 도메인의 개체를 인식하는 어려운 작업이다. 
    2. 이 논문에서는 entity annotations과 entity structures 두 가지 새로운 관점에서 도메인 차이를 분석하고, 각각 word-to-tag 및 word-to-word 관계를 활용하여 이를 모델링하는 방법을 제안한다.  
    3. 또한, SLC-DA라 불리는 Structure and Label Constrained Data Augmentation에서는 소스 도메인에서 대상 도메인으로의 원활한 전이를 도와주기 위해 레이블 제한된 사전 훈련 작업과 구조 제한된 최적화 목적을 도입하여 도메인 특정 증강 데이터를 생성한다. 여러 표준 데이터셋을 평가한 결과, 우리의 방법은 최고의 기록이나 경쟁력 있는 결과를 달성하여 cross-domain few-shot NER에서의 효과를 입증한다.

###### Weakly-supervised Deep Cognate Detection Framework for Low-Resourced Languages Using Morphological Knowledge of Closely-Related Languages (https://aclanthology.org/2023.findings-emnlp.38/)
- Anthology ID: 2023.findings-emnlp.38 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 적은 데이터를 가진 언어에 대한 transfer learning에서 cognate을 활용하는 것은 자동기계번역, 개체명인식, 정보 검색과 같은 언어이해 태스크에 대한 흥미로운 기회이다.
    2. 기존의 방법은 orthographic, phonetic, 혹은 state-of-the-art contextual language model을 활용한 지도형 cognate 탐지 태스크에 초점을 맞추었으며, 대부분의 적은 데이터를 가진 언어에서 성능이 좋지 않다.
    3. 본 논문에서는 적은 데이터를 가진 언어를 위한 언어견지는 weakly-supervised 기반의 deep cognate 탐지 프레임워크를 제안한다. 더불어, 관련 언어로부터 유래된 형태적 지식을 활용하여 탐지 작업을 수행하며, 사전 정의된 cognate annotation이 필요없으며 다른 언어 가족에 속하는 다양한 언어에 적용될 수 있다.

###### SQLPrompt: In-Context Text-to-SQL with Minimal Labeled Data (https://aclanthology.org/2023.findings-emnlp.39/)
- Anthology ID: 2023.findings-emnlp.39 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트-투-SQL은 자연어 텍스트로부터 데이터베이스에 대한 SQL 쿼리를 자동으로 생성하기 위한 작업이다. 이 연구에서는 Text-to-SQL의 소수의 데이터셋에 대한 프롬프팅 능력을 향상시키기 위해 "SQLPrompt"라는 방법을 제안한다.
    2. SQLPrompt는 혁신적인 프롬프트 디자인, 일관성을 기반으로 한 실행 디코딩 전략, 그리고 일관성 선택 도중 다양한 프롬프트 디자인과 기초 모델을 사용하여 SQL 제안을 다양화하는 방법("MixPrompt" 및 "MixLLMs")을 포함한다.
    3. 우리는 SQLPrompt가 레이블이 없는 소수 데이터에 대한 인-컨텍스트 학습에서 기존 접근법들보다 훨씬 우수한 성능을 보이며, 수천 개의 레이블 데이터를 사용한 최첨단 fine-tuning과의 격차를 줄였음을 보여준다.

###### Toward Building General Foundation Models for Language, Vision, and Vision-Language Understanding Tasks (https://aclanthology.org/2023.findings-emnlp.40/)
- Anthology ID: 2023.findings-emnlp.40 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 foundation models는 언어, 시각 또는 시각-언어 태스크 중 하나에서만 가장 우수한 성능을 보여주지만, 모든 이해 태스크에 대해 가장 우수한 성능을 보이는 일반 foundation model을 구성할 수 있는지 여전히 미정이다.
    2. 이 논문에서는 일반 foundation model인 X-Foundation Model (X-FM)을 훈련하기 위한 새로운 방법을 제안한다. X-FM은 언어 인코더, 시각 인코더, 퓨전 인코더로 구성되어 있으며, 훈련 방법에는 텍스트, 이미지, 이미지-텍스트 쌍 데이터로부터 X-FM을 학습하기 위한 두 가지 새로운 기술이 포함되어 있다.
    3. 벤치마크 데이터셋에서의 실험 결과, X-FM은 기존의 일반 foundation 모델보다 우수한 성능을 보이고, 언어, 시각 또는 시각-언어 이해를 위해 특정한 foundation 모델들과 비교할 때 더 나은 성능을 보여준다는 것을 보여준다.

###### Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction (https://aclanthology.org/2023.findings-emnlp.41/)
- Anthology ID: 2023.findings-emnlp.41 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 새로운 task인 트리거 경고 할당에 관한 첫 번째 데이터셋과 평가 결과를 제시한다.
    2. Archive of Our Own (AO3)라는 인기있는 팬픽 사이트에서 추출한 서술적 픽션(corpus)의 라벨링된 말뭉치를 도입하고 영어 이야기에 트리거 경고를 할당할 것인지 여부를 결정하는 문서 수준의 분류 작업을 정의한다.
    3. 우리는 "violence"라는 가장 일반적으로 할당되는 트리거 유형에 초점을 맞추고, AO3 작가들에 의해 제공되는 경고 라벨을 사용하여 SVM, BERT 및 Longformer 모델을 훈련시키고 F1 점수가 0.8에서 0.9 사이라는 결과를 얻어 violence에 대한 트리거 경고 할당이 실현 가능함을 보여준다.

###### Pass-Tuning: Towards Structure-Aware Parameter-Efficient Tuning for Code Representation Learning (https://aclanthology.org/2023.findings-emnlp.42/)
- Anthology ID: 2023.findings-emnlp.42 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 코드 인텔리전스 분야에서 Code Pre-trained Models(CodePTMs)가 다양한 작업에 대해 표준 범주가 되었으나, 많은 작업에 대해 파인튜닝하는 전략이 적용되면 모델 크기가 증가하고 이는 과도한 비용을 초래한다.
    2. 기존의 Parameter-Efficient Learning (PEL) 방법론은 이와 유사한 문제를 완화하기 위해 자연어 처리 모델에 적용되었지만, 이를 코드에 적용하는 것은 코드의 내재 구조적 특성을 포착하지 못한다.
    3. 이 논문에서는 코드의 내재 구조적 특성을 캡처하기 위해 Pass-Tuning이라는 구조 인식적 파라미터 효율적 코드 표현 학습 방법을 제안한다. 이 방법은 튜닝 가능한 Prefix로서 Abstract Syntax Tree (AST)로부터 학습하는 그래프 신경망 모듈을 이용한다. 우리는 총 8개의 프로그래밍 언어를 대상으로 다양한 작업을 평가하였고, 이를 통해 우리의 방법의 효과성, 강건성, 그리고 일반성을 입증하였다.

###### Counterfactual Augmentation for Multimodal Learning Under Presentation Bias (https://aclanthology.org/2023.findings-emnlp.43/)
- Anthology ID: 2023.findings-emnlp.43 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 기계 학습 시스템에서 라벨은 시스템이 원하는 사용자 행동에서 파생되는 경우가 많다. 하지만 사용자와 모델 사이의 피드백 루프로 인해 향후 사용자 행동에 영향을 주는 presentation bias가 발생하며, 이는 새로운 모델을 학습시키는 능력을 저해한다.
    2. 이 논문에서는 counterfactual augmentation이라는 새로운 인과적 방법을 제안하여 생성된 counterfactual 라벨을 사용하여 presentation bias를 보정하는 것을 목표로 한다.
    3. 실험 결과는 counterfactual augmentation이 보정되지 않은 모델 및 기존의 편향 보정 방법보다 더 나은 성능을 보여준다고 보여주며, 모델 분석 결과는 생성된 counterfactual이 오라클 설정에서 실제 counterfactual과 일치한다는 것을 나타낸다.

###### A Table-to-Text Framework with Heterogeneous Multidominance Attention and Self-Evaluated Multi-Pass Deliberation (https://aclanthology.org/2023.findings-emnlp.44/)
- Anthology ID: 2023.findings-emnlp.44 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 행렬-텍스트 변환의 성능은 크게 발전했으나, 계층적 구조와 같은 행렬 구조 신호의 효과적인 활용은 여전히 어려운 문제입니다.
    2. 또한, 생성된 설명을 신중히 검토하는 것이 행렬-텍스트 문제에서 효과적임이 입증되었으나, 여러 번의 후보 중 어떤 결과를 채택해야 할지 결정하는 것은 다른 어려움을 제공합니다.
    3. 이 논문에서는 자체 평가된 다중 패스 생성(Self-evaluated multi-pass Generation) 및 이질성 다중 우세성 어텐션(Heterogenous Multidominance Attention)을 기반으로 한 새로운 행렬-텍스트 접근법인 SG-HMA를 제안합니다. 이로 인해 효율적인 계층 구조의 상호 작용을 포함한 텍스트 생성에 대한 풍부한 신호를 제공합니다.

###### Crossing the Aisle: Unveiling Partisan and Counter-Partisan Events in News Reporting (https://aclanthology.org/2023.findings-emnlp.45/)
- Anthology ID: 2023.findings-emnlp.45 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언론은 비편향적인 보도를 유지하는 것이 기대되지만, 그들은 여전히 이념적 입장을 지지하거나 반대하는 사건들을 선택적으로 포함하거나 제외함으로써 대중 의견에 영향을 미칠 수 있다. 
    2. 이 논문에서는 언론의 중립성과 사건의 포함 또는 제외를 통해 대중에게 어떤 영향을 미치는지 연구한다. 
    3. 이를 위해, 우리는 언론사에 따라 다른 304개의 뉴스 기사에서 8,511개의 (반대-)이념적 이벤트 주석이 있는 고품질 데이터셋 PAC을 도입한다.

###### Video-Text Retrieval by Supervised Sparse Multi-Grained Learning (https://aclanthology.org/2023.findings-emnlp.46/)
- Anthology ID: 2023.findings-emnlp.46 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 비디오-텍스트 검색에서의 진전은 더 나은 표현 학습에 의해 이루어졌으나, 이 논문에서는 비디오-텍스트 검색을 위한 새로운 다수정보 변형 학습 프레임워크인 S3MA를 제안한다. 
    2. S3MA는 비디오와 텍스트 간에 공유되는 희소 공간을 학습하기 위해 유한 수의 sparse 개념을 초기화하고 제안된 유사성 및 정렬 손실을 사용하여 공유 희소 공간을 지도 방식으로 학습하고 업데이트한다. 
    3. S3MA의 학습된 공유 희소 공간과 다양한 정보 변형 학습 결과, 여러 비디오-텍스트 검색 벤치마크에서 S3MA가 기존 방법들보다 우수한 성능을 보여준다는 것을 확인할 수 있다.

###### Zero-Shot-BERT-Adapters: a Zero-Shot Pipeline for Unknown Intent Detection (https://aclanthology.org/2023.findings-emnlp.47/)
- Anthology ID: 2023.findings-emnlp.47 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 처리에서 의도 발견은 중요한 작업이며 산업 응용 분야에서 점점 더 중요해지고 있다. 사용자 입력에서 새로운, 이전에 보지 못한 의도를 식별하는 것은 이 분야에서 가장 큰 도전 중 하나이다.
    2. 이 연구에서는 Transformer 아키텍처를 기반으로 한 다국어 의도 발견을 위한 Two-stage 방법을 제안한다. 알려진 클래스에 대한 학습 후, 알려지지 않은 의도를 분류하는 Zero-shot setting에서 성능을 평가한다.
    3. 실험 결과, Zero-Shot-BERT-Adapters가 알려진 의도 분류 및 보이지 않는 의도 발견과 같은 Zero-shot setting에서 다양한 기준선을 앞서는 것을 보여준다. 이 접근 방식은 고객 관리에 널리 응용될 수 있는 잠재력을 갖고 있으며, 대형 언어 모델과는 달리 쉽게 배포 및 확장할 수 있는 경량 모델을 통해 자동화된 동적 트리아지를 가능하게 한다.

###### ReFSQL: A Retrieval-Augmentation Framework for Text-to-SQL Generation (https://aclanthology.org/2023.findings-emnlp.48/)
- Anthology ID: 2023.findings-emnlp.48 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Text-to-SQL"은 자연어 질문을 SQL 쿼리로 번역하는 작업이다. 기존 방법들은 자연어와 SQL 언어를 직접 매칭시키고 모든 질문에 대해 하나의 인코더-디코더 기반 모델을 학습시키지만, 이는 SQL의 내재적인 구조적 특성과 구체적인 구조 지식과 일반적인 지식 사이의 간격을 과소평가하여 생성된 SQL에 구조적 에러가 발생한다. 
    2. 저자들은 이러한 문제를 해결하기 위해 ReFSQL이라는 검색-인수(argument) 프레임워크를 제안한다. 이 프레임워크는 구조 강화 검색기와 생성기 두 부분으로 구성되어 있다. 
    3. 실험 결과는 우리의 접근 방식이 Text-to-SQL 생성의 정확성과 견고성을 향상시키는 데 효과적임을 검증하며, 다양한 다른 기저 모델과 결합할 때 (11B flan-T5를 포함한) 개선된 성능을 보이며, fine-tuning 접근 방식을 사용하는 기존 방법과 비교했을 때 최고의 성능을 달성하였다.

###### Approximating Two-Layer Feedforward Networks for Efficient Transformers (https://aclanthology.org/2023.findings-emnlp.49/)
- Anthology ID: 2023.findings-emnlp.49 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 성능을 희생하지 않고 신경망의 계산 및 메모리 요구량을 줄이는 방법은 무엇인가요? 최근의 연구들은 희소한 MoEs를 사용하여 자원 효율적인 대형 언어 모델을 구축한다. 
    2. 이 논문에서는 MoEs에 대한 여러 가지 새로운 관점을 제시하고, *두개 층의 신경망* (예: Transformer의 feedforward block)을 근사화하는 다양한 방법을 *통합*하는 일반적인 프레임워크를 소개한다. 
    3. 계산-동일한 조건이 아닌 매개변수-동일한 조건에서 MoEs를 밀집한 기준모델과 비교하는 이전의 연구와는 달리, 우리의 평가 조건은 매개 변수-동일한 조건으로 설정되며, 이는 LM을 적절하게 평가하는 데 중요하다.

###### Adapter-TST: A Parameter Efficient Method for Multiple-Attribute Text Style Transfer (https://aclanthology.org/2023.findings-emnlp.50/)
- Anthology ID: 2023.findings-emnlp.50 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 속성 텍스트 스타일 전환을 위해 대형 언어 모델을 세밀 조정으로 적용하는 것은 특정 다운스트림 작업을 위해 많은 계산 자원과 레이블된 데이터가 필요하여 어려울 수 있다.
    2. 이 논문에서는 Adapter-TST라는 프레임워크를 제안하여 사전 학습 모델의 원래 파라미터를 고정시키고 여러 속성 정보를 모델링하기 위해 다른 신경 어댑터를 사용하는 다중 속성 텍스트 스타일 전환 모델을 개발한다.
    3. 실험 결과, Adapter-TST는 모든 최신 기베으로부터 더 적은 자원을 사용하여 탁월한 성능을 보여주며, 각 어댑터는 특정 스타일 속성을 효과적으로 특징화하고 구성 편집을 수행하기 위해 설정될 수 있다는 것을 실험적으로 입증했다.

###### Solving the Right Problem is Key for Translational NLP: A Case Study in UMLS Vocabulary Insertion (https://aclanthology.org/2023.findings-emnlp.51/)
- Anthology ID: 2023.findings-emnlp.51 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델의 발전으로 인해 NLP 시스템은 실제 세팅에서 우수한 성능을 보여야 하는 요구가 증가하고 있다. 하지만, 실제 문제와 잘 부합하지 않은 경우에는 강력한 모델 만으로는 좋은 결과를 얻기 어렵다. 이 논문에서는 실제 세계의 작업과 일치하는 UMLS 어휘 삽입 작업을 연구하고 이를 반영한 새로운 task와 dataset, 강력한 기준 모델을 제안한다.
    2. UMLS 어휘 삽입 작업을 위해 기존 솔루션을 재활용하여 개발한 강력한 베이스라인을 사용하며, 실제 편집자에게도 질적 개선을 제공하는 효과적인 바이오메디컬 언어 모델을 제안한다.
    3. 문제 수정의 중요성을 강조하기 위해 이 사례 연구가 실제 NLP 솔루션의 성공에 어떤 중요성을 가지는지를 제시한다.

###### Improving Cross-lingual Transfer through Subtree-aware Word Reordering (https://aclanthology.org/2023.findings-emnlp.52/)
- Anthology ID: 2023.findings-emnlp.52 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 다국어 언어 모델(XLM-R 및 mT5 같은)의 능력이 인상적으로 성장했음에도 불구하고, 특히 low-resource 환경에서는 멀리 떨어진 언어를 처리하는 데 여전히 어려움이 있음이 보여져왔다.
    2. 효과적인 교차언어 전이를 위한 장벽 중 하나는 단어 순서 패턴의 변동성이다. 이는 원천 언어나 목표 언어 측면에서의 단어 재배치를 통해 완화될 수 있으며, 다양한 방법이 제안되었다. 
    3. 이 논문에서는 Universal Dependencies를 기반으로 한 새로운 강력한 재배치 방법을 제안하며, 이는 소량의 주석 데이터에 대해 구문적 문맥에 따른 세밀한 단어 순서 패턴을 학습할 수 있으며, 구문 트리의 모든 수준에 적용할 수 있다는 것을 보여주었다.

###### Novel Slot Detection With an Incremental Setting (https://aclanthology.org/2023.findings-emnlp.53/)
- Anthology ID: 2023.findings-emnlp.53 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 대화 시스템은 다양한 사용자 요청과 빠르게 변화하는 도메인에 직면하여, 이전에 보지 못한 슬롯 유형에 빠르게 적응하는 것은 주요 도전과제이다.
    2. 이 논문에서는 새로운 슬롯 탐지 (NSD)를 도입하여 잠재적인 새로운 유형을 발견하는 것을 소개하고, 이를 이후 상호 작용에서 처리할 수 없는 상태로 남겨지기 때문에 NSD를 이용한 대화 시스템은 실용적인 개선을 이끌어내지 못한다.
    3. 그래서 우리는 이 논문에서 NSD를 이용한 대화 시스템을 1) 알려지지 않은 슬롯을 검색하고 2) 새로운 유형을 처리할 수 있는 능력을 갖는 모델을 훈련시키기 위한 두 단계로 분리하는 접근 방법을 제안한다.

###### Self-supervised Post-processing Method to Enrich Pretrained Word Vectors (https://aclanthology.org/2023.findings-emnlp.54/)
- Anthology ID: 2023.findings-emnlp.54 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Retrofitting 기법은 단어 표상 간 의미적 및 관계적 지식의 약점을 보완하기 위해 외부 리소스를 주입하는 방법이었다. 하지만, 이전의 방법은 추가적인 외부 리소스를 필요로하며 Lexicon에 강하게 의존한다. 따라서 우리는 이러한 문제에 대처하기 위해 self-supervised extrofitting이라는 기존 extrofitting의 간단한 확장을 제안한다."
    2. "우리의 방법은 외부 리소스 없이도 모든 단어 유사도 태스크에서 기본 임베딩을 개선시킨다. 게다가 이 방법은 Lexicon이 희소한 언어에도 효과적이다. 우리는 대화 상태 추적 및 텍스트 분류 과제에서 우리의 방법의 장점을 보여주며, 다른 단어 벡터 특수화 방법과 비교하여 더 나은 결과와 일반화된 결과를 보고한다."
    3. (띄어쓰기 체크) "retrofitting 방법인 extrofitting은 외부 리소스를 단어 표상에 주입하여 단어들간의 의미적 및 관계적 지식의 한계를 보완하는 기법이다. 그러나, 이전 방법들은 외부 리소스에 의존하고 Lexicon에 강한 제약이 있다. 이 문제를 해결하기 위해 우리는 extrofitting의 간단한 확장인 self-supervised extrofitting을 제안한다."

###### Automatic Model Selection with Large Language Models for Reasoning (https://aclanthology.org/2023.findings-emnlp.55/)
- Anthology ID: 2023.findings-emnlp.55 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Chain-of-Thought (CoT)와 Program-Aided Language Models (PAL)은 서로 다른 추론 방법으로 각각의 장점을 가지고 있는데, CoT는 자연 언어를 사용하여 유연성과 해석 가능성을 제공하고, PAL은 프로그래밍 언어를 사용하여 구조화되고 엄격한 논리를 제공한다.
    2. 이 논문에서는 큰 언어 모델 (LLM)을 사용하여 동적으로 두 방법을 선택하는 모델 선택 방법을 제안한다. 이 방법의 실현 가능성은 이론적 분석에 의해 강조되었으며, 실험 결과로도 확인되었다.
    3. 우리의 제안된 방법은 Codex, ChatGPT, GPT-4와 함께 여덟 가지 추론 데이터셋에서 상당한 성능 향상을 보여주었으며, self-consistency와 결합하면 성능을 더 향상시키면서 계산 비용을 크게 줄일 수 있다. 또한, GSM8K와 SVAMP에서는 96.8%와 93.7%의 정확도로 새로운 최고 성과를 달성하였다.

###### ARKitSceneRefer: Text-based Localization of Small Objects in Diverse Real-World 3D Indoor Scenes (https://aclanthology.org/2023.findings-emnlp.56/)
- Anthology ID: 2023.findings-emnlp.56 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 3D Refering Expression Comprehension은 3D 장면 내에서 텍스트 표현을 객체로 지정하는 작업으로, 가정용 로봇이나 확장현실 기기에서 사용자 지시에 언급된 객체를 로컬라이즈(localize)하는 데 중요한 작업이다. 
    2. 기존 indoor 3D referring expression comprehension 데이터셋들은 일반적으로 로컬라이즈하기 쉬운 대형 객체 클래스(예: 의자, 테이블, 문)를 다루고 소형 객체(예: 조리 도구나 사무용품)를 자주 무시한다. 
    3. 이 논문은 ARKitScenes의 다양하고 고해상도 3D scene 데이터셋을 기반으로 실제 실내 장면에서 자주 등장하는 소형 일상용품에 초점을 맞춘 ARKitSceneRefer 데이터셋을 구축한다.

###### Improving Question Generation with Multi-level Content Planning (https://aclanthology.org/2023.findings-emnlp.57/)
- Anthology ID: 2023.findings-emnlp.57 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 주어진 맥락과 답변으로부터 질문을 생성하는 문제를 해결하기 위해, 특히 맥락 간 다중 점프 추론을 필요로 하는 질문에 초점을 맞추었다.
    2. Key phrase의 선택이 QG에 필수적이라는 이전 연구들의 제안에도 불구하고, 특히 긴 맥락에 대해 이러한 이분 표현된 구문들을 의미있는 질문으로 연결하는 것은 여전히 어렵다.
    3. 이를 해결하기 위해 MultiFactor라는 새로운 QG 프레임워크를 제안하였는데, MultiFactor에는 key phrase 선택과 텍스트 생성을 위한 복합성 적용을 위한 두 개의 구성요소인 FA-Model 및 Q-Model이 포함되어 있다.

###### Is ChatGPT a Financial Expert? Evaluating Language Models on Financial Natural Language Processing (https://aclanthology.org/2023.findings-emnlp.58/)
- Anthology ID: 2023.findings-emnlp.58 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT와 같은 대형 언어 모델 (LLM)의 등장으로 일반적인 자연어 전처리 (NLP) 작업은 혁신되었지만, 금융 도메인에서의 전문성은 포괄적인 평가가 부족하였다.
    2. 금융 NLP 작업에서 LLM의 능력을 평가하기 위해 FinLMEval이라는 Financial Language Model Evaluation 프레임워크를 제시하고, 언어 모델의 성능을 평가하기 위해 설계된 아홉 개의 데이터셋을 제공한다. 
    3. 연구 결과, ChatGPT는 대부분의 금융 작업에서 뛰어난 성능을 보여주지만, 특히 독점 데이터셋을 처리할 때에는 전문가 모델에 비해 성능이 떨어지는 것으로 나타났다. 이 연구는 금융 도메인에서 더 세련된 LLM을 구축하기 위한 지속적인 노력을 위한 평가 기준을 마련하기를 바란다.

###### DelucionQA: Detecting Hallucinations in Domain-specific Question Answering (https://aclanthology.org/2023.findings-emnlp.59/)
- Anthology ID: 2023.findings-emnlp.59 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대량 언어 모델(LLM)로 생성된 텍스트에서 환각 현상은 요약, 질의응답 등 거의 모든 응용 분야에서 발견된다. 신뢰성이 요구되는 응용 분야에서 LLM 생성 텍스트에 환각이 존재할 수 있다면 심각한 문제이지만, 정보 검색을 활용하여 LLM에 관련 배경 정보를 제공함으로써 환각의 양을 줄일 수 있다.
    2. 그러나 여전히 LLM은 맥락의 관련 정보를 포착하지 못하거나 파라메트릭 지식을 우선시함으로써 다양한 이유로 환각을 생성할 수 있다. 자동 방법을 통해 환각을 감지하는 것이 매우 중요하다.
    3. 따라서 이 논문에서는 특정 도메인의 QA 작업을 위해 LLM에서 검색을 보강하여 생성된 환각을 포착하는 정교한 데이터셋 DelucionQA를 도입하고, 환각 감지 방법의 기준을 제안한다. 또한 대상 시나리오에서의 환각 현상에 대한 유용한 통찰력을 공유하기 위해 분석 및 사례 연구를 제공한다.

###### InvGC: Robust Cross-Modal Retrieval by Inverse Graph Convolution (https://aclanthology.org/2023.findings-emnlp.60/)
- Anthology ID: 2023.findings-emnlp.60 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 획기적인 시각 및 언어 모델링으로 인해 크로스 모달 검색의 중요한 진전이 이뤄졌지만, 멀티모달 데이터 표현은 제한적인 볼록 모양에 군집화되어 검색 성능을 저해하는 것으로 조사되었다.
    2. 이 논문에서는 다양한 크로스 모달 벤치마크와 방법들에서 표현의 변질 문제가 존재함을 실험적으로 검증하였다.
    3. InvGC라는 그래프 컨벌루션과 평균 풀링에 영감을 받은 후처리 기술을 소개하여 데이터 포인트들 간의 거리를 늘려 효과적으로 표현들을 분리하는 것을 제안하였다.

###### Dissecting In-Context Learning of Translations in GPT-3 (https://aclanthology.org/2023.findings-emnlp.61/)
- Anthology ID: 2023.findings-emnlp.61 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 언어 모델을 기반으로한 기계 번역에서의 연구는 대부분 few-shot 샘플을 선택하는 데 중점을 두고 있다. 
    2. 이 논문에서는 high-quality, in-domain demonstrations을 변형하여 인접한 문맥에서 번역을 학습하는 데 데모 이력의 역할을 더 잘 이해하려고 한다. 
    3. 본 연구에서는 asymmetric perturbation(비대칭 유사 지배)의 결과가 매우 다른 것을 보이며, 번역의 문맥적 학습에서 가장 중요한 학습 신호는 출력 텍스트 분포이다는 것을 밝혔다.

###### Social Commonsense-Guided Search Query Generation for Open-Domain Knowledge-Powered Conversations (https://aclanthology.org/2023.findings-emnlp.62/)
- Anthology ID: 2023.findings-emnlp.62 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오픈 도메인 대화에서는 유용한 대화를 위해 관련 지식을 얻을 수 있는 검색 쿼리를 생성하는 것이 도전적일 수 있다. 하지만 사용자가 명확한 요청을 표현하지 않을 때 정보를 검색해야 할지 결정하는 것은 어려울 수 있다. 
    2. 이 논문에서는 사회적 상식에 기반한 검색 쿼리 생성에 초점을 맞춘 새로운 접근 방식을 제시한다. 대화 주제와 관련된 연결을 생성함으로써 검색 쿼리 생성을 지원하는데, 이를 위해 상식 대화 시스템을 활용한다.
    3. 제안된 프레임워크는 주제 추적, 상식적인 응답 생성 및 매개 변수로서의 검색 쿼리 생성을 통해 수동 사용자 상호 작용을 다룬다. 평가 결과, 명시적인 대화 정보에만 의존하는 기존의 쿼리 생성 기법의 한계를 극복하고, 더 관련성이 높고 특정하며 매력적인 검색 쿼리를 생성하여 더욱 흥미로운 응답을 얻을 수 있다.

###### MixTEA: Semi-supervised Entity Alignment with Mixture Teaching (https://aclanthology.org/2023.findings-emnlp.63/)
- Anthology ID: 2023.findings-emnlp.63 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 반지도 학습 entity alignment (EA)은 충분한 라벨링된 매핑 데이터의 부재로 인해 실질적이고 어려운 작업이다.
    2. 이 논문은 MixTEA라는 새로운 반지도 EA 방법을 제안한다. 이 방법은 표준으로 몇 개의 라벨 매핑을 사용하여 학생 모델을 훈련시킨다. 잡음이 있는 가짜 매핑의 부정확성을 평가하기 위해 BDV 기법을 제안하고, MDR 모듈을 통해 잡음이 있는 매핑의 부정적인 영향을 줄인다.
    3. 벤치마크 데이터셋을 통한 결과와 추가적인 분석에서 우리 제안 방법의 우수성과 효과성을 입증하였다.

###### EZ-STANCE: A Large Dataset for Zero-Shot Stance Detection (https://aclanthology.org/2023.findings-emnlp.64/)
- Anthology ID: 2023.findings-emnlp.64 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Zero-shot stance detection (ZSSD)는 훈련 과정에서 보지 못한 대상에 대해 작성자가 찬성, 반대 또는 중립적인지 여부를 결정하는 것을 목표로 한다.
    2. 이 논문에서는 다른 ZSSD 데이터셋인 VAST와는 대조적으로, 다양한 도메인을 커버하는 명사구 대상과 주장 대상을 함께 포함한 대규모 영어 ZSSD 데이터셋인 EZ-STANCE를 제공한다. 
    3. 또한, 명사구 대상에 대해 두 가지 간단하고 효과적인 prompt를 적용하여 ZSSD를 NLI 태스크로 변환하는 방법을 제안하고, 실험적 결과에서 EZ-STANCE가 새로운 도전 과제로서 의미있는 연구 기회를 제공한다는 것을 보여준다.

###### Boot and Switch: Alternating Distillation for Zero-Shot Dense Retrieval (https://aclanthology.org/2023.findings-emnlp.65/)
- Anthology ID: 2023.findings-emnlp.65 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Neural 'dense' retrieval 모델은 많은 데이터셋에서 state-of-the-art 성능을 보이지만, 종종 제한된 도메인 이전 능력을 가진다." 
    2. 기존의 적응 방법들은 명시적인 지도, 복잡한 모델 구조 또는 거대한 외부 모델을 요구하는 등 불편하다. 
    3. 본 논문에서는 간단하지만 효과적인 비지도 학습 방법인 ABEL을 제안하고, 이러한 방법은 unsupervised dense retriever 모델을 향상시키는 reranker의 피드백을 통해 상호 증진을 달성한다.

###### TESTA: Temporal-Spatial Token Aggregation for Long-form Video-Language Understanding (https://aclanthology.org/2023.findings-emnlp.66/)
- Anthology ID: 2023.findings-emnlp.66 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 비디오-언어 사전 훈련은 비디오-언어 이해 태스크를 발전시키는 데 있어 중요한 역할을 하고 있으나, 비디오 인코딩의 엄청난 계산 부담은 특히 장편 비디오의 경우 효율성 저해요소로 작용한다.
    2. 이 논문에서는 비디오의 시공간 관련성을 효율적으로 포착하기 위해 TEmporal-Spatial Token Aggregation (TESTA)라는 방법을 제안한다. TESTA는 비디오 성질에 기인한 대규모 시각 토큰을 적게하여 비디오 인코딩을 가속화한다.
    3. TESTA를 기반으로 한 사전 훈련된 비디오-언어 모델을 소개하며, 이 모델은 각 비디오 인코더 블록에서 분리된 공간-시간 토큰 집계 모듈을 갖추고 있다. TESTA는 이 모델의 계산 효율성을 1.7배 향상시키고, 더 긴 입력 프레임 처리에서 유연성을 통해 중요한 성능 향상을 이룬다.

###### Fusing Temporal Graphs into Transformers for Time-Sensitive Question Answering (https://aclanthology.org/2023.findings-emnlp.67/)
- Anthology ID: 2023.findings-emnlp.67 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 긴 문서로부터 시간에 민감한 질문에 답변하는 것은 문서와 질문에서 시간적 추론이 필요하다. 
    2. 본 연구에서는 기존의 시간 정보 추출 시스템을 활용하여 시간에 대한 그래프를 구성하고, Transformer 모델에 이러한 그래프를 통합하는 다양한 접근 방식을 조사한다.
    3. 실험 결과, 우리가 제안한 시간 그래프를 입력 텍스트에 통합하는 방식은 Transformer 모델의 시간적 추론 능력을 크게 향상시키며, 그래프 컨볼루션 기반 접근 방식보다 우수한 성능을 보여 새로운 최고 성능을 수립한다.

###### The Internal State of an LLM Knows When It’s Lying (https://aclanthology.org/2023.findings-emnlp.68/)
- Anthology ID: 2023.findings-emnlp.68 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLM)은 다양한 작업에서 뛰어난 성능을 보여주지만, 가장 큰 단점은 확신있는 톤으로 부정확하거나 거짓 정보를 생성한다는 것이다.
    2. 이 논문에서는 LLM의 내부 상태를 사용하여 명제의 진실성을 확인하는 것이 가능하다는 증거를 제공한다.
    3. LLM의 은닉 레이어 활성화를 기반으로 명제가 참인지 거짓인지를 예측하는 분류기를 학습하여, LLM이 명제를 읽거나 생성할 때 이를 판별할 수 있다는 것을 실험을 통해 보여주었다.

###### Factual Relation Discrimination for Factuality-oriented Abstractive Summarization (https://aclanthology.org/2023.findings-emnlp.69/)
- Anthology ID: 2023.findings-emnlp.69 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대부분의 신경망 추상적 요약 모델은 고품질 요약을 생성할 수 있으나, 여전히 사실적 오류가 자주 포함되어 있다. 
    2. 기존 사실성 지향적 추상적 요약 모델은 사실적 정보의 통합만을 고려하고 사실적 오류의 원인을 간과한다. 
    3. 이 논문에서는 사실성지향적 추상적 요약 모델 DASum을 제안하며, 사실성 오류의 원인을 식별할 수 있는 새로운 작업인 factual relation discrimination을 기반으로 한다.

###### Multi-Modal Knowledge Graph Transformer Framework for Multi-Modal Entity Alignment (https://aclanthology.org/2023.findings-emnlp.70/)
- Anthology ID: 2023.findings-emnlp.70 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 모달 지식 그래프에서 동등한 entity 쌍을 찾는 MMEA(Multi-Modal Entity Alignment)는 여러 종류의 정보로 인해 어려움을 겪는 중요한 작업이다.
    2. 이 논문에서는 Meaformer라는 새로운 MMEA transformer를 제안하여 neighbor features, multi-modal attributes, entity types를 계층적으로 도입하여 alignment 작업을 강화한다.
    3. Transformer의 hierarchical modifiable self-attention block과 entity-type prefix injection을 이용하여 전역 정보를 제한하고 다양한 정보의 독특한 의미를 보전한다.

###### Is a Prestigious Job the same as a Prestigious Country? A Case Study on Multilingual Sentence Embeddings and European Countries (https://aclanthology.org/2023.findings-emnlp.71/)
- Anthology ID: 2023.findings-emnlp.71 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 다국어 문장의 표현이 유럽 국가와 직업을 어떻게 파악하고 이것이 유럽 언어별로 다른지를 연구한다.
    2. 우리는 기계 번역을 통해 12개 유럽 언어로 템플릿 문장을 제시하고 임베딩에서 가장 두드러진 차원을 분석한다.
    3. 분석 결과, 전체적으로 가장 큰 차이는 동유럽과 서유럽의 정치적 차이와 GDP에 따른 국가의 경제적 강도로 나타났으며, 직업 차원은 대부분의 모델에서 국가 차원과는 관련이 없었다.

###### Towards A Holistic Landscape of Situated Theory of Mind in Large Language Models (https://aclanthology.org/2023.findings-emnlp.72/)
- Anthology ID: 2023.findings-emnlp.72 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 연구는 대형 언어 모델들이 Theory of Mind (ToM)에 대한 부족한 성능을 보이고 있으며, 기존의 평가 지표들이 ToM의 여러 측면에 초점을 맞추고 있어 경로 단축이나 데이터 누수에 취약하다는 문제가 있다.
    2. 이 논문에서는 기계의 ToM을 7가지 정신 상태 범주로 지표화하고, 기존의 평가 기준을 분석하여 ToM의 미개척된 측면을 확인한다. 또한 기계를 환경에 물리적으로 위치하고 인간과 상호작용하는 개체로 취급하여 ganzs 다른 평가 방법론을 제안한다.
    3. 맥락을 고려한 평가는 정신 상태를 더 포괄적으로 평가할 수 있으며, 단축 경로와 데이터 누출의 위험을 줄일 수 있다. 그 외에도 그리드 월드(experimental setup)에서의 연구 결과를 제시하여 미래의 ToM과 LLMs(Intuitive means)를 융합하는 연구를 촉진하기를 희망한다.

###### Text Augmented Spatial Aware Zero-shot Referring Image Segmentation (https://aclanthology.org/2023.findings-emnlp.73/)
- Anthology ID: 2023.findings-emnlp.73 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 픽셀 수준의 어노테이션을 사용하지 않고 언급된 사진 세그멘테이션을 하기 위한 zero-shot referring image segmentation 문제를 다룬다.
    2. 기존 연구들은 CLIP와 같은 사전 훈련된 cross-modal 모델을 활용하여 언급된 식별 마스크와 관련성을 맞추는 것으로, 이미지-텍스트 간의 전역적인 매칭만을 고려한다.
    3. 이 논문에서는 Training-free하고 다양한 비주얼 인코더에 강건한 Text Augmented Spatial-aware (TAS) zero-shot referring image segmentation 프레임워크를 제안하며, 확장된 실험을 통해 다른 방법들보다 탁월한 성능을 보였다.

###### IRFL: Image Recognition of Figurative Language (https://aclanthology.org/2023.findings-emnlp.74/)
- Anthology ID: 2023.findings-emnlp.74 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 글과 이미지와 같은 다중 모달에서 유사유형(예: 은유, 유사유, 관용구) 같은 말의 의미를 이해하는 것은 AI의 중요한 도전 과제이다.
    2. 이 연구에서는 Image Recognition of Figurative Language (IRFL) 데이터셋을 개발하였고 이에서 두 가지의 새로운 태스크를 제안하였다.
    3. 최신 비전과 언어 모델로 실험한 결과, 최고의 모델 성능은 인간(97%)보다 현저히 낮았고, 이러한 문제를 개선하기 위해 데이터셋과 코드를 공개하였다.

###### Self-supervised Meta-Prompt Learning with Meta-Gradient Regularization for Few-shot Generalization (https://aclanthology.org/2023.findings-emnlp.75/)
- Anthology ID: 2023.findings-emnlp.75 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Prompt tuning"은 parameter-efficient한 방법으로, soft prompts을 학습하고 언어 모델을 특정 downstream task에 맞게 조건을 걸 수 있다. 그러나 few-shot 설정에서는 좋은 초기화에 크게 의존하며, 적은 데이터로는 일반화하기 어렵다. 
    2. 이 논문에서는 Self-supervised meta-learning을 이용하여 적은 수의 unlabeled data만으로 효율적인 적응을 위한 universal prompt 초기화를 학습하고, 과적합 문제를 완화하기 위해 gradient regularization 기법을 함께 사용한다. 
    3. 실험 결과, SUPMER은 다양한 few-shot downstream task에서 더 좋은 성능을 보이며, 도메인 일반화 능력도 우수하다. SUPMER 코드는 https://github.com/beepkh/SUPMER에서 확인할 수 있다.

###### An Adaptive Prompt Generation Framework for Task-oriented Dialogue System (https://aclanthology.org/2023.findings-emnlp.76/)
- Anthology ID: 2023.findings-emnlp.76 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대부분의 대형 언어 모델 (LLM)은 프롬프트를 사용하여 여러 다운스트림 작업을 수행하는 데 있어서 사실상의 방법이지만, 특정 작업에 적합한 프롬프트를 찾는 것은 여전히 어려운 문제입니다.
    2. 이 논문에서는 훈련 가능한 슬롯 생성자(TSG)와 적응형 프롬프트 생성자(APG)를 제안하여, LLM을 통해 실태완비된 TOD 시스템을 위한 잠재력을 최대로 발휘합니다.
    3. MultiWOZ 2.0 데이터셋에서의 실험 결과, 제안한 방법은 기존 방법보다 성능이 우수함을 입증하였으며, 코드와 데이터가 공개될 예정입니다.

###### Temporal Knowledge Graph Reasoning Based on N-tuple Modeling (https://aclanthology.org/2023.findings-emnlp.77/)
- Anthology ID: 2023.findings-emnlp.77 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "시간적 지식 그래프(TKG)를 통한 추론은 다양한 응용 분야에서 미래의 시간적 사실(예: 이벤트)을 예측하기 위해 중요하다. 기존 TKG에 있는 시간적 사실은 본질적 개체(즉, 주요 역할을 하는 개체)만 포함하고 (주체 개체, 술어, 목적 개체, 타임스탬프)라는 네 개의 요소로 구성되어 있다. 이러한 표현은 시간적 사실을 과도하게 단순화하고 불가피하게 정보 손실을 초래한다. 따라서 우리는 temporal fact를 보다 정확하게 n-튜플로 설명하여 TKG를 N-튜플 Temporal Knowledge Graphs (N-TKGs)로 보완하는 것을 제안한다." 
    2. "N-TKG를 통해 추론을 수행하기 위해, 우리는 더 나아가 N-tuple Evolutional Network (NE-Net)을 제안한다. NE-Net은 시간적 사실의 다른 타임스탬프에서 엔티티와 술어의 진화적인 표현을 반복적으로 학습하며, 이러한 엔티티와 술어 간의 관계를 모델링한다. 학습된 표현을 기반으로 미래 타임스탬프에서의 추론 작업을 과업별 디코더를 통해 실현할 수 있다." 
    3. "새로운 두 개의 데이터셋에서의 실험 결과는 N-TKG의 우수성과 NE-Net의 효과를 입증한다."

###### Make Your Decision Convincing! A Unified Two-Stage Framework: Self-Attribution and Decision-Making (https://aclanthology.org/2023.findings-emnlp.78/)
- Anthology ID: 2023.findings-emnlp.78 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 블랙박스 모델 해석 방법은 높은 NLP 성능을 보이며 고품질의 근거를 생성하기는 하지만, 생성된 근거와 모델의 결정 사이에 신뢰성이 부족하다는 문제가 있다.
    2. 따라서 이 논문에서는 Self-Attribution and Decision-Making (SADM)라는 통일된 두 단계 프레임워크를 제안하여 생성된 근거와 모델의 결정 사이의 신뢰성을 높인다.
    3. ERASER 벤치마크에서 수행한 실험으로 우리의 프레임워크가 신뢰성 높은 근거-모델 결정 링크를 확립하면서 NLP 성능과 근거 품질에서 경쟁력 있는 결과를 얻었음을 보였다.

###### Adaptive Structure Induction for Aspect-based Sentiment Analysis with Spectral Perspective (https://aclanthology.org/2023.findings-emnlp.79/)
- Anthology ID: 2023.findings-emnlp.79 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 구조 정보 (예 : 의존 구문 트리)를 포함하는 것이 측면 기반 감성 분석 (ABSA)의 성능을 향상시킬 수 있다고 알려져 있다. 그러나 이 구조 정보는 대개 최적화되지 않고 번거롭게 구해진다. 따라서 자동으로 적응적인 구조를 학습하는 것이 이 문제를 해결하는 데 도움이 된다.
    2. 본 논문에서는 사전 훈련된 언어 모델 (PLM)에서 구조 유도에 집중하며, 언어 표현의 규모 정보가 구조 유도 능력에 미치는 영향을 탐구하기 위해 스펙트럼 관점에서 구조 유도를 시도한다. 우리의 모델은 일반적으로 사용되는 PLM (예 : RoBERTa 등)과 간단하면서 효과적인 그래프 구조 학습 (GSL) 모듈로 구성된다.
    3. ABSA에 대한 세 가지 공개 벤치마크에서 광범위한 실험을 수행하였고, 결과와 추가적인 분석에서 스펙트럼 접근법을 도입함으로써 AsD (Aspects-sentiment Distance)를 줄일 수 있으며 구조 유도에 도움이 됨을 보여주었다. 심지어 이러한 간단한 프레임워크를 기반으로한 결과가 세 데이터셋에서 최고 성능 또는 거의 최고 성능에 달할 수 있다는 것을 발견하였다. 게다가, 우리의 연구는 다른 작업에 일반화되거나 다른 유사한 도메인에 영감을 줄 수 있는 잠재력을 가지고 있다.

###### NovaCOMET: Open Commonsense Foundation Models with Symbolic Knowledge Distillation (https://aclanthology.org/2023.findings-emnlp.80/)
- Anthology ID: 2023.findings-emnlp.80 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NovaCOMET은 지식 모델과 일반적인 task 모델의 최상의 측면을 결합한 오픈 커먼센스 지식 모델이다.
    2. NovATOMIC에서 기호적으로 정리된 지식 그래프를 만들고, 이를 통해 NovaCOMET을 학습시킨다.
    3. NovaCOMET은 임의의 구조를 입력이나 출력으로 사용할 수 있도록 한 오픈 포맷 훈련 목적으로 구성되어 있다. 그 결과, NovaCOMET은 커먼센스 생성 태스크에서 Flan-T5와 유사한 오픈 태스크 모델을 능가한다.

###### In-Context Demonstration Selection with Cross Entropy Difference (https://aclanthology.org/2023.findings-emnlp.81/)
- Anthology ID: 2023.findings-emnlp.81 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large language model, LLM)은 문맥 내 시연을 활용하여 제로샷(task-agnostic) 태스크 성능을 향상시킬 수 있으나, 가장 적합한 문맥 예제를 선택하는 것은 어렵다. 
    2. 우리는 테스트 예제에 대해 finetuning된 언어 모델의 perplexity와 문맥 시연의 효과가 음의 상관관계를 가진다는 관찰을 기반으로 크로스 엔트로피 차이(CED) 메소드를 제안한다. 
    3. CED를 사용하여 각 테스트 입력마다 문맥 시연을 순위화하고 선택함으로써, CED를 사용한 문맥 시연 선택은 다양한 LLM에 대해 베이스라인 선택 방법보다 성능을 향상시킬 수 있다.

###### The Past, Present, and Future of Typological Databases in NLP (https://aclanthology.org/2023.findings-emnlp.82/)
- Anthology ID: 2023.findings-emnlp.82 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 타입론 database들은 서로와 언어문법과 같은 다른 근원들 사이에서 일관성이 없다. 일부 불일치는 에러나 언어적 변형 때문이지만, 많은 불일치는 database의 이산적인 범주적 특성 때문이다.
    2. 우리는 타입론 database와 자연어처리의 활용과 불일치에 대해 체계적인 조사를 통해 이 문제에 빛을 냈다.
    3. 우리는 이산적인 타입론 database 대신 연속적인 타입론 특성을 사용하는 것이 유익하며, 이는 언어학의 권장사항과도 일치한다고 주장한다. 특히, 저자원 언어 모델링에 큰 잠재력을 가진다고 제안한다.

###### SoulChat: Improving LLMs’ Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations (https://aclanthology.org/2023.findings-emnlp.83/)
- Anthology ID: 2023.findings-emnlp.83 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 기억력과 사고 흐름의 능력 때문에 다양한 분야에서 널리 적용되고 있다. 그러나 심리상담 분야에서 이 모델들은 종종 일반적인 조언을 제공하려고 성급하게 움직인다. 
    2. 우리는 심리 지원을 받는 사용자들이 이성적인 조언보다는 공감, 신뢰, 이해, 위안을 필요로 한다는 점을 감안하여 대화 맥락과 감정적인 응답을 대상으로 한 다면 대화 데이터셋을 구축하였다. 
    3. 실험 결과, 심리 상담사의 표현에 가까운 대화 기록과 응답을 사용하여 대형 언어 모델의 공감 능력을 유의미하게 향상시킬 수 있다는 것을 보였다.

###### Can ChatGPT Assess Human Personalities? A General Evaluation Framework (https://aclanthology.org/2023.findings-emnlp.84/)
- Anthology ID: 2023.findings-emnlp.84 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델들 (LLM)은 다양한 영역에서 탁월한 결과를 내지만, 그들의 인간과 유사한 심리학적 특성은 아직 크게 연구되어지지 않았다.
    2. 본 논문에서는 LLM을 사용하여 인간의 성격을 분석하는 가능성을 탐구한 일반적인 평가 프레임워크를 제시한다.
    3. 실험 결과, ChatGPT는 인간의 성격을 평가할 수 있으며, 평균 결과는 InstructGPT보다 낮은 견고성에도 불구하고 더 일관되고 공정한 평가를 달성할 수 있음을 보여준다.

###### MoqaGPT : Zero-Shot Multi-modal Open-domain Question Answering with Large Language Model (https://aclanthology.org/2023.findings-emnlp.85/)
- Anthology ID: 2023.findings-emnlp.85 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 멀티모달 오픈 도메인 질문 답변은 이미지, 테이블, 파손 등과 같은 다양한 모달리티 데이터베이스에서 증거 검색을 필요로 하는데, GPT-4와 같은 대형 언어 모델조차 이 작업에 부족함을 보인다. 
    2. 우리는 LLMs가 이 작업을 제로샷 방식으로 수행할 수 있게하기 위해 MoqaGPT라는 간단하고 유연한 프레임워크를 제안한다.
    3. MoqaGPT는 복잡한 멀티모달 순위매기기를 우회하는 divide-and-conquer 전략을 사용하며, 새로운 모달리티를 수용하고 새로운 모델로 순조롭게 전환할 수 있다.

###### Large Language Models Know Your Contextual Search Intent: A Prompting Framework for Conversational Search (https://aclanthology.org/2023.findings-emnlp.86/)
- Anthology ID: 2023.findings-emnlp.86 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화형 검색에서 사용자의 상황에 맞는 검색 의도를 정확히 이해하는 것은 중요한 도전 과제이다. 기존 방법들은 제한된 데이터로 학습되었기 때문에 실제 대화형 검색 시나리오를 처리하는 데에 효과적이고 견고한 성능을 보여주지 못한다.
    2. 이 논문에서는 큰 언어 모델(Large Language Models)을 사용하여 대화형 검색에 도움이 되는 텍스트 기반 검색 의도 해석기로 활용하는 간단하면서도 효과적인 프롬프팅 프레임워크인 LLM4CS를 제안한다.
    3. 실험 결과, 우리의 LLM4CS 프레임워크는 기존 방법 및 심지어 사람에 의한 재작성을 사용한 경우와 비교하여 널리 사용되는 대화형 검색 벤치마크에서 뛰어난 성능을 보여준다. 이는 LLM을 대화형 검색에 더 잘 활용하기 위한 중요한 증거를 제공한다.

###### DocAsRef: An Empirical Study on Repurposing Reference-based Summary Quality Metrics as Reference-free Metrics (https://aclanthology.org/2023.findings-emnlp.87/)
- Anthology ID: 2023.findings-emnlp.87 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 요약 품질 평가는 reference-based와 reference-free 두 가지 범주로 나뉜다. 자동 요약을 평가할 때 reference-based 메트릭은 인간이 작성한 참조 정보에 의존하지만, 이 논문에서는 이러한 메트릭을 참조 문서 대신 원본 문서에 대해 평가하는 것으로 적용하여 reference-free 메트릭으로 변환할 수 있다는 가설을 제시한다.
    2. 실험 결과가 이 가설을 지원한다. pretrained DeBERTa-large-MNLI 모델을 사용한 zero-shot BERTScore는 다양한 측면에서 SummEval과 Newsroom 데이터셋에서 원래의 reference-based 버전보다 일관되게 성능이 우수하다. 또한 대부분의 기존 reference-free 메트릭 보다 우수한 결과를 보이며, GPT-3.5를 기반으로 한 zero-shot 요약 평가기와도 견줄만한 성능을 보인다.

###### Toxicity in chatgpt: Analyzing persona-assigned language models (https://aclanthology.org/2023.findings-emnlp.88/)
- Anthology ID: 2023.findings-emnlp.88 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 기반의 LLM인 ChatGPT에서 특정 인물을 설정하는 것이 생성물의 독성을 크게 증가시키는 것을 발견했다. ChatGPT에 지정된 페르소나, 예를 들어 체급추기꾼 무함마드 알리와 같은,에 따라서 독성이 최대 6배까지 증가할 수 있는데, 이 때 생성물은 잘못된 편견, 유해한 대화, 상처를 주는 의견을 가지게 된다. 
    2. 또한 특정 개체(예: 특정 인종)가 다른 개체에 비해 표적으로 지정되어 논리 페르소나와 상관없이 차별적인 편견을 반영하는 문제가 있다. 
    3. 본 연구 결과는 법규안에서 여러 조항을 위반하고 있음을 보여주며, 폭넓은 AI 커뮤니티가 현재의 안전 매커니즘의 효과를 재고하고 견고하며 안전하며 신뢰성 있는 AI를 개발하기 위한 더 나은 기술을 개발하기를 바란다.

###### Execution-Based Evaluation for Open-Domain Code Generation (https://aclanthology.org/2023.findings-emnlp.89/)
- Anthology ID: 2023.findings-emnlp.89 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제적인 설정에서 코딩 쿼리 범위를 확장하기 위해, 우리는 ODEX라는 첫 번째 Open-Domain Execution 기반 Python 코드 생성 데이터셋을 제안한다. 
    2. ODEX에는 79개의 다양한 라이브러리를 포함한 945개의 자연어-코드 쌍과 실행을 위한 1,707개의 사람이 작성한 테스트 케이스가 있다. 
    3. ODEX는 CODEX보다 더 나은 결과를 보이는 반면, CODEGEN은 규모를 확장함에 따라 효과적으로 개선되며 CODEX과 동등한 성능을 보여준다.

###### Syntax-Aware Retrieval Augmented Code Generation (https://aclanthology.org/2023.findings-emnlp.90/)
- Anthology ID: 2023.findings-emnlp.90 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 설명을 바탕으로 코드를 자동으로 생성하는 신경망 코드 생성 모델이 널리 채택되고 있으나, 현재의 방식은 색인 기반 메커니즘이 코드 생성과정에서 추가적인 잡음을 도입해 문법적으로도 잘못된 코드를 생성하는 문제가 있다.
    2. kNN-TRANX는 코드 생성 작업에 대한 맞춤형 작은 데이터 저장소에서의 검색을 가능하게 하여 이러한 문제를 해결한다. 또한 검색노이즈의 영향을 줄이기 위해 구문 제약을 활용한다.
    3. 두 개의 공개 데이터셋에서 kNN-TRANX를 평가한 결과, 우리의 접근 방식의 효과가 입증되었다.

###### Selecting Key Views for Zero-Shot Entity Linking (https://aclanthology.org/2023.findings-emnlp.91/)
- Anthology ID: 2023.findings-emnlp.91 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 엔티티 링킹은 텍스트의 멘션과 지식 베이스의 엔티티를 매칭시키는 것인데, 최근 연구에서는 zero-shot 환경에 초점을 맞추고 있다. 이 논문은 엔티티 설명에서 주요 정보를 선택하여 zero-shot 엔티티 링킹을 위한 KVZEL 프레임워크를 제안한다.
    2. KVZEL은 주석 관련 정보를 강조하고 멘션과 관련된 정보를 캡처하기 위해 unsupervised clustering과 키 뷰 선택 모듈을 사용한다.
    3. 실험 결과 KVZEL은 zero-shot 엔티티 링킹 데이터셋에서 새로운 최고 성능을 달성한다.

###### Is Explanation the Cure? Misinformation Mitigation in the Short Term and Long Term (https://aclanthology.org/2023.findings-emnlp.92/)
- Anthology ID: 2023.findings-emnlp.92 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP 모델의 발전으로 자동 설명 생성이 제안되어 사회적 미디어 플랫폼에서의 잘못된 정보에 대항하는 대안으로 제시되고 있으나, 이러한 설명이 실제로 어떻게 사람들이 가짜 뉴스와 싸울 수 있는 데 도움이 되는지는 더 연구되어야 한다.
    2. 본 연구에서는 경고 레이블과 GPT-4로 생성된 최신 대조적 설명의 효과를 비교하여 가짜 뉴스의 잘못된 정보를 해체하는 데 어떤 것이 더 유용한지를 비교하는 것이다.
    3. 결과적으로, 경고 그룹과 설명 그룹 모두 단기 및 장기적으로 가짜 주장에 대한 참여자의 자체적인 믿음을 유의미하게 감소시키는 것으로 나타났다.

###### Improving the Robustness of Summarization Models by Detecting and Removing Input Noise (https://aclanthology.org/2023.findings-emnlp.93/)
- Anthology ID: 2023.findings-emnlp.93 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 요약 모델의 평가는 일반적으로 학습 데이터와 동일한 분포의 테스트 데이터를 사용한다. 그러나 실제 환경에서는 요약 대상 문서에 텍스트 추출 오류나 데이터 파이프라인 버그로 인해 노이즈가 포함될 수 있다.
    2. 우리는 다양한 유형의 입력 노이즈로 인한 모델 성능의 심각한 저하를 12 개의 ROUGE-1 점까지 측정하는 대규모 실험을 제시한다.
    3. 또한, 우리는 추가적인 학습, 보조 모델 또는 노이즈 유형의 사전 지식을 필요로하지 않고 모델 추론 중에 입력에서 노이즈를 감지하고 제거하는 가벼운 방법을 제안한다. 이를 통해 성능 저하의 상당 부분을 효과적으로 완화할 수 있으며, 때로는 11 개의 ROUGE-1 점 정도 큰 성능 향상을 나타낸다.

###### How Reliable Are AI-Generated-Text Detectors? An Assessment Framework Using Evasive Soft Prompts (https://aclanthology.org/2023.findings-emnlp.94/)
- Anthology ID: 2023.findings-emnlp.94 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 강력한 사전 학습 언어 모델(PLM)의 출시를 주된 원동력으로하여 AI가 생성한 텍스트의 급속한 확산이 있었지만, 이러한 텍스트의 남용 문제를 해결하기 위해 OpenAI detector와 Stanford DetectGPT 등 다양한 성능 우수한 탐지기가 개발되었다.
    2. 본 연구에서는 이러한 탐지기의 신뢰성을 어떻게 평가할 수 있는지를 묻고, 이에 대한 대답으로 PLM이 이러한 우수한 탐지기를 피하기 위해 텍스트를 생성할 수 있는 철저한 접근 방식을 설계한다.
    3. 제안된 접근 방식은 PLM이 탐지기를 속일 수 있는 "인간과 비슷한" 텍스트를 생산하기 위한 새로운 유형의 소프트 프롬프트인 "universal evasive prompt"를 제안하며, 다양한 작성 업무에서 여러 PLM을 활용하여 extensive한 실험을 진행하여 evasive soft prompt의 효과를 평가하였다.

###### Knowledge is a Region in Weight Space for Fine-tuned Language Models (https://aclanthology.org/2023.findings-emnlp.95/)
- Anthology ID: 2023.findings-emnlp.95 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단일 모델과 단일 데이터셋에 대한 연구가 널리 집중되어 왔으나, 서로 다른 모델들 간의 관계에 대해서는 상대적으로 많이 알려져 있지 않다. 
    2. 본 논문에서는 서로 다른 모델들이 가중치 공간과 손실 함수 landscape에서 어떻게 상호 연결되는지를 연구하고 있다. 
    3. 실험 결과, 비슷한 데이터셋에서 finetuning된 모델들은 가중치 공간에서 군집을 이루며, 이들 모델들 사이를 탐색하면 새로운 모델이 태스크 성능을 유지하거나 개선할 수 있다는 것을 보여준다.

###### Unveiling the Multi-Annotation Process: Examining the Influence of Annotation Quantity and Instance Difficulty on Model Performance (https://aclanthology.org/2023.findings-emnlp.96/)
- Anthology ID: 2023.findings-emnlp.96 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 커뮤니티에서는 언어 해석, 주관성, 모호함의 뉘앙스를 더 잘 잡기 위해 다중 주석 데이터셋 구축을 주장해왔다. 
    2. 본 논문에서는 단일 주석과 다중 주석으로 데이터셋이 확장될 때 성능 평가 점수가 어떻게 다를 수 있는지 선행 연구를 진행한다. 
    3. 우리는 주석 예산이 동일한 유사한 데이터셋이 성능 향상에도 불구하고 다양한 결과를 야기할 수 있다는 것을 보여준다.

###### On the Risk of Misinformation Pollution with Large Language Models (https://aclanthology.org/2023.findings-emnlp.97/)
- Anthology ID: 2023.findings-emnlp.97 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 Large Language Models (LLMs)의 잠재적 오용이 신뢰할 만한 가짜 정보를 생성하고 이에 따른 정보 중심 애플리케이션, 특히 Open-Domain Question Answering (ODQA) 시스템에 미치는 영향을 조사했습니다.
    2. LLMs가 효과적인 가짜 정보 생성기로 작용할 수 있으며, 이는 ODQA 시스템의 성능에 중대한 저하 (최대 87%)를 일으킵니다.
    3. LLM이 생성한 가짜 정보로 인한 피해를 완화하기 위해, 가짜 정보 탐지, 주의 권유, 독자 앙상블이라는 세 가지 방어 전략을 제안하고 있습니다.

###### Dolphin: A Challenging and Diverse Benchmark for Arabic NLG (https://aclanthology.org/2023.findings-emnlp.98/)
- Anthology ID: 2023.findings-emnlp.98 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Dolphin"은 다양한 아랍어 언어와 다양성에 특화된 자연어 생성(NLG) 평가 프레임워크를 제공한다고 한다. 이 벤치마크는 다이얼로그 생성, 질문 응답, 기계 번역, 요약 등 13개의 다양한 NLG 태스크를 포함하고 있으며, 40개의 다양하고 대표적인 공개 데이터셋으로 구성되어 있다.
    2. Dolphin은 실제 상황과 아랍어의 언어적 풍부함을 반영하기 위해 신중하게 선정된 50개의 테스트 세트를 가지고 있으며, 아랍어 및 다국어 모델의 성능과 일반화 능력을 평가하는 새로운 기준을 제시하고 있다.
    3. Dolphin은 다양성을 강조하고 현재의 아랍어 NLG 연구의 빈곤한 부분을 파악하는 광범위한 분석을 제공하며, 이 벤치마크에서 여러 아랍어 및 다국어 모델을 평가하고 강력한 기준을 제시하여 연구자들이 비교할 수 있도록 한다.

###### Hierarchical Enhancement Framework for Aspect-based Argument Mining (https://aclanthology.org/2023.findings-emnlp.99/)
- Anthology ID: 2023.findings-emnlp.99 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Aspect-Based Argument Mining (ABAM)는 계산적 논증에서 중요한 작업이다. 기존의 방법들은 ABAM을 nested named entity recognition 문제로 다루어 ABAM 작업의 독특한 도전과제를 효과적으로 해결하기 위한 전략의 필요성을 간과하고 있다."
    2. 우리는 Hierarchical Enhancement Framework (HEF)에서 세 개의 새로운 구성 요소를 소개하여 ABAM을 위한 층별 개선 프레임워크를 제안한다. 
    3. 이 프레임워크는 Semantic and Syntactic Fusion (SSF) 구성 요소, Batch-level Heterogeneous Graph Attention Network (BHGAT) 구성 요소, Span Mask Interactive Attention (SMIA) 구성 요소를 통해 동작하여, argument unit과 aspect term 인식에서 도전 과제를 더 잘 다루고 성능과 정확도를 향상시킨다.

