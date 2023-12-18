# Korean Three-Line Summarizations of Papers 1-100 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (https://aclanthology.org/2023.emnlp-main.0/)
- Anthology ID: 2023.emnlp-main.0 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    요약문을 생성할 수 없습니다.

###### IAG: Induction-Augmented Generation Framework for Answering Reasoning Questions (https://aclanthology.org/2023.emnlp-main.1/)
- Anthology ID: 2023.emnlp-main.1 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 외부 지식과 파라미터 기반 언어 모델의 메모리를 결합한 RAG 모델은 오픈 도메인 QA 태스크에서 최고의 아키텍처가 되었습니다. 그러나 일반적인 지식 베이스는 한정된 커버리지와 노이즈가 있는 정보로 제한되어 있어 암묵적 추론 질문에 대한 검색 기반 접근법은 부적절합니다.
    2. 이 논문에서는 검색 문서와 함께 유추적인 지식을 활용하는 Induction-Augmented Generation (IAG) 프레임워크를 제안합니다. 이를 위해 유추적 추론 패턴을 기반으로하는 독특한 프롬프팅 방법을 사용하여 대규모 언어 모델을 활용하여 이러한 지식을 도출합니다.
    3. 실험 결과, IAG는 RAG 기준선 및 ChatGPT보다 두 개의 오픈 도메인 QA 태스크에서 우수한 성능을 보였습니다. 특히, 우리의 최고 모델은 CSQA2.0 (2022년 11월 1일부터) 및 StrategyQA (2023년 1월 8일부터)의 공식 리더보드에서 1위를 차지했습니다.

###### Absolute Position Embedding Learns Sinusoid-like Waves for Attention Based on Relative Position (https://aclanthology.org/2023.emnlp-main.2/)
- Anthology ID: 2023.emnlp-main.2 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 어텐션 가중치는 Transformer 기반 모델의 추론 과정을 해석하는 데 도움이 되는 신호입니다.
    2. 일부 어텐션 헤드에서는 각 토큰의 이웃에 집중하여, 주변 토큰에 따라 각 토큰의 출력 벡터가 의존성을 가짐으로써 추론이 문맥에 따라 다를 수 있습니다.
    3. 연구 결과는 학습된 위치 임베딩이 사인 함수 형태의 구성 요소를 가지고 있으며, 이러한 구성 요소가 셀프-어텐션에서 query와 key에 전달되고, 어텐션 헤드가 관련 상대적 위치의 인근 토큰에 집중하도록 사인 함수 구성 요소의 위상을 조정한다는 것을 보여줍니다.

###### Chinese Lexical Substitution: Dataset and Method (https://aclanthology.org/2023.emnlp-main.3/)
- Anthology ID: 2023.emnlp-main.3 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 lexical substitution (LS) 벤치마크는 인간 주석자에게 기억에서 대체어를 생각하도록 한 것으로, 카버리지가 제한되고 규모도 상대적으로 작은 문제가 있다. 따라서 우리는 사람과 기계의 협업을 바탕으로 한 LS 데이터셋을 구성하기 위한 새로운 주석 방법을 제안한다.
    2. 우리의 주석 방법을 기반으로, 우리는 중국어 LS 데이터셋 CHNLS를 구축했으며, 뉴스, 소설 및 위키피디아 등 세 가지 텍스트 장르를 커버하는 33,695개의 인스턴스와 144,708개의 대체어로 구성되어 있다.
    3. 실험 결과로 앙상블 방법이 다른 LS 방법보다 우수하게 나타났으며, 중국어 LS 작업에서 최초로 연구되었다.

###### Decoding the Silent Majority: Inducing Belief Augmented Social Graph with Large Language Model for Response Forecasting (https://aclanthology.org/2023.emnlp-main.4/)
- Anthology ID: 2023.emnlp-main.4 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 뉴스 미디어를 위한 자동 응답 예측은 소셜 및 컨텍스트 정보를 활용하여 뉴스 릴리스의 영향력을 예측하고 사회적 충돌 및 도덕적 상해와 같은 예기치 않은 부정적 결과를 방지하는 데 핵심적인 역할을 한다.
    2. 기존의 방법들은 사용자의 명시적 프로필이나 과거 활동이 제한된 경우 (lurker라고 함)에도 인간-인간 상호작용 및 문맥 정보를 활용하여 효과적으로 응답을 예측해야 한다는 요건을 충족시키기 위해 최적의 처리와 활용 방법에 대해 제한적으로 다루었다.
    3. 이 논문에서는 대규모 언어 모델을 활용하여 기존 소셜 네트워크 위에 믿음-중심 그래프를 형성하고 그래프 기반 전파를 통해 사회적 역학을 캡처하는 프레임워크인 SocialSense를 제안한다. 이 방법론은 먼 거리에 위치한 유사한 신념을 가진 사용자들을 연결하는 인공 그래프를 형성하여 응답 패턴을 효과적으로 파악할 수 있다는 가설을 세우고 있다.

###### Fine-grained Conversational Decoding via Isotropic and Proximal Search (https://aclanthology.org/2023.emnlp-main.5/)
- Anthology ID: 2023.emnlp-main.5 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 응답 생성에는 보통 범용 텍스트 디코딩 접근 방식이 사용되는데, 이 논문에서는 대화 특정 인코딩 방법을 활용하여 응답의 품질을 개선하지만, 대화 디코딩 방법에는 여전히 자세히 연구되지 않았다.
    2. 이 논문에서는 지역성(locality)과 동질성(isotropy)의 규칙을 따르는 좋은 대화 특징 공간이어야 한다는 SimDRC의 영감을 받아, 세밀한 대화 디코딩 방법인 IPS (isotropic and proximal search)를 제안한다.
    3. 실험 결과, IPS는 자동 및 인간 평가 메트릭 모두에서 대화 분야에서 기존 디코딩 전략보다 유의미하게 우수한 성과를 보여주며, 더 심층적인 분석을 통해 우리의 방법의 효과를 확인하였다.

###### Holistic Inter-Annotator Agreement and Corpus Coherence Estimation in a Large-scale Multilingual Annotation Campaign (https://aclanthology.org/2023.emnlp-main.6/)
- Anthology ID: 2023.emnlp-main.6 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문에서는 6개의 언어와 약 40 명의 주석가들이 참여한 대규모 다국어 주석 캠페인의 난이도를 보고한다. 사람들이 주석을 달기 어려워하는 기술을 강조하고, 이 현상의 원인에 대해 설명한다.
    2. 우리는 단어 임베딩을 기반으로 한 새로운 Annotator 확인(metric)인 Holistic IAA를 소개하고, 이 metric을 사용한 다양한 실험과 전통적인 Inter Annotator Agreement(IAA) metric과의 상관관계에 대해 보고한다.
    3. 그러나 주석가들 간의 상호 작용이 다소 제한되어 있고, 즉, 몇 명의 주석가들만 동일한 문서 하위 집합에 주석을 달으며, 우리는 데이터 세트 전체의 일관성을 평가하고, 서로 다른 문서와 언어에 대해 주석을 달은 주석가 간의 IAA에 대한 좋은 대리자를 찾기 위한 방법을 모색한다.

###### PHD: Pixel-Based Language Modeling of Historical Documents (https://aclanthology.org/2023.emnlp-main.7/)
- Anthology ID: 2023.emnlp-main.7 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 고전문서의 디지털화는 역사학자에게 이전에 없던 연구 기회를 제공하지만, 전통적인 방식은 OCR을 사용하여 이미지를 텍스트로 변환하는 것으로, 이미지로 처리하는 잠재적 이점을 간과하고 많은 노이즈를 도입하고 있다.
    2. 이 논문에서는 픽셀 기반 언어 모델을 사용하여 마스킹된 픽셀 패치를 재구성하는 방법을 제안한다.
    3. 역사적 스캔을 생성하기 위한 새로운 방법과 실제 역사적 신문을 결합하여 모델을 사전 훈련시키고, 이 모델을 역사적 QA 작업에 성공적으로 적용하여 유용성을 입증하였다.

###### Primacy Effect of ChatGPT (https://aclanthology.org/2023.emnlp-main.8/)
- Anthology ID: 2023.emnlp-main.8 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT와 같은 대형 언어 모델은 zero-shot 성능에서 탁월한 성과를 보여주고 있지만, 레이블의 순서에 따라 선택되는 기울기가 있다는 연구 결과를 발견하였다. 
    2. ChatGPT의 의사 결정은 레이블의 순서에 영향을 받고, 순서상 먼저 등장하는 레이블을 선호한다는 것을 확인하였다. 
    3. 이러한 결과는 더 신뢰할 수 있는 ChatGPT 기반 솔루션을 개발하기 위한 추가적인 통찰력을 제공할 수 있으며, 관련 코드를 공개하였다.

###### Evaluating the Rationale Understanding of Critical Reasoning in Logical Reading Comprehension (https://aclanthology.org/2023.emnlp-main.9/)
- Anthology ID: 2023.emnlp-main.9 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "논리적 읽기 이해 능력을 정확하게 평가하기 위해, 우리는 주요 추론의 이유를 이해하기 위한 데이터셋을 제공한다. 기존 다중 선택 논리적 읽기 이해 데이터셋의 질문을 사용하여 선택 또는 제거해야 하는 대답 옵션에 대한 이유에 대한 논리적 설명을 크라우드소싱하였다. 우리의 데이터셋 실험 결과, 최근의 대형 언어 모델들은 주요 질문에 올바른 답을 줄 수는 있지만, 서브 질문에 대답하는 데 어려움을 겪는다는 것을 보여준다."
    2. "모델들은 특히 주요 질문의 잘못된 답변 옵션을 위한 서브 질문에 대한 답변을 제공하기 어렵다는 것을 알 수 있었으며, 이는 모델들이 잘못된 대안이 왜 제거되어야 하는지에 대한 한정된 능력을 가지고 있다는 것을 시사한다."
    3. "이러한 결과들은 우리의 데이터셋이 언어 모델들의 중요한 추론 능력에 대한 추가적인 연구를 유도하면서 관련 대안의 제거 과정에 초점을 맞추고 있다는 것을 시사한다."

###### Evaluating and Modeling Attribution for Cross-Lingual Question Answering (https://aclanthology.org/2023.emnlp-main.10/)
- Anthology ID: 2023.emnlp-main.10 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 높은 리소스를 가진 언어에서는 신뢰할 수 있는 답변 콘텐츠가 풍부하게 제공되고 질문에 대한 답을 얻기가 쉬우나, 해당 언어를 알지 못하는 사람들은 이러한 콘텐츠에 접근하기 힘들다.
    2. 이 논문에서는 Cross-lingual 질문 응답(QA)을 위한 attribution (특정 출처 적용)에 대해 연구한다. 그리고 상위 cross-lingual QA 시스템의 attribution 수준을 평가한 결과, 답변의 상당 부분이 어떤 출처에 속하는지 알 수 없음이 발견되었다.
    3. 이러한 부족한 attribution 문제를 해결하기 위해 Natural Language Inference 모델과 PaLM 2 모델을 이용하여 attribution 감지를 시도하였고, 이를 통해 cross-lingual QA 시스템의 attribution 수준을 개선할 수 있었다.

###### Better Quality Pre-training Data and T5 Models for African Languages (https://aclanthology.org/2023.emnlp-main.11/)
- Anthology ID: 2023.emnlp-main.11 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구에서는 다국어 언어 모델의 사전 훈련 데이터의 품질 향상의 중요성을 강조한다. 특히 저자원 언어에 대한 기존 웹 크롤은 품질 문제를 가지고 있는데, 이러한 문제점을 이해하고 수정하기 위해 기존 사전 훈련 말뭉치를 정밀히 조사하여 16개 아프리카 언어용 새로운 다국어 사전 훈련 말뭉치를 소개한다.
    2. 이 데이터셋을 구축하기 위해 가장 포괄적인 다국어 웹 크롤 중 하나인 mC4에서 13개 언어에 대한 현재 데이터 소스를 철저히 조사하고, 세심한 조사와 개선된 웹 크롤링 전략을 통해 더 깨끗한 데이터를 추출한다.
    3. 이후 이 데이터셋을 사용하여 T5 기반 모델을 사전 훈련하고 여러 하위 작업에서의 성능을 평가한다. 새로운 모델은 네 가지 NLP 작업에서 기존 사전 훈련 모델보다 더 나은 효과를 보여주며, 저자원 시나리오에서 언어 모델의 사전 훈련에 데이터 품질이 중요한 역할을 한다는 것을 강조한다.

###### Sparse Universal Transformer (https://aclanthology.org/2023.emnlp-main.12/)
- Anthology ID: 2023.emnlp-main.12 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 유니버셜 트랜스포머(UT)는 레이어 간에 파라미터를 공유하며, 일정 가정하에서 Turing-complete한 트랜스포머 변종이다. 이 논문에서는 Sparse Mixture of Experts (SMoE)를 이용하여 이 UT의 계산 복잡성을 줄이고, 파라미터 효율성과 일반화 능력을 유지하는 Sparse Universal Transformer (SUT)을 제안한다.
    2. SUT는 견고한 일반화 결과와 WMT'14와 같은 표준적인 자연어 벤치마크에서의 파라미터 및 계산 효율을 달성하여, 유니버셜 트랜스포머와 베니라 트랜스포머의 장점을 모두 결합한다.
    3. 현재까지의 최첨단 자연어처리 시스템들은 대부분 베니라 트랜스포머를 기반 모델로 사용하고 있으며, 이는 UT의 파라미터 스케일링이 VT와 비교해 컴퓨팅과 메모리 비용이 더 많이 들기 때문이다.

###### Theory of Mind for Multi-Agent Collaboration via Large Language Models (https://aclanthology.org/2023.emnlp-main.13/)
- Anthology ID: 2023.emnlp-main.13 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델 (LLM)은 추론 및 계획에 뛰어난 성과를 보여주었지만, 다중 에이전트 협업에 대한 능력은 아직 탐구되지 않았다. 이 연구는 LLM 기반 에이전트를 Theory of Mind (ToM) 추론 과제를 가진 다중 에이전트 협력 텍스트 게임에서 평가하여, Multi-Agent Reinforcement Learning (MARL) 및 계획 기반 베이스라인과의 성능을 비교한다.
    2. LLM 기반 에이전트들은 긴 시야 범위에 대한 문맥 관리의 체계적인 실패 및 과제 상태에 대한 환각으로 인해 계획 최적화에 제한이 있음을 관찰했다.
    3. 명시적 신념 상태 표현의 사용은 이러한 문제를 완화하는 데 도움이 되며, LLM 기반 에이전트의 과제 성능 및 ToM 추론의 정확성을 향상시킨다는 것을 발견했다.

###### Establishing Trustworthiness: Rethinking Tasks and Model Evaluation (https://aclanthology.org/2023.emnlp-main.14/)
- Anthology ID: 2023.emnlp-main.14 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 이해는 다면적인 인지 능력이며, NLP (자연어 처리) 커뮤니티는 수십 년 동안 컴퓨터 모델을 통해 이를 모델링하기 위해 노력해왔다. 
    2. 큰 언어 모델 (LLM)의 등장으로 인해 과거에는 특정 모델 구조와 평가 방법이 있다는 개념이 무너지고, 다목적, Task-agnostic 접근 방식이 대세가 되었다.
    3. 따라서 우리는 NLP에서 Task와 모델 평가의 개념을 재고하고, 더 ganzholistischen 언어 이해를 위한 평가 프로토콜을 추구해야 한다고 주장한다.

###### Let’s Think Frame by Frame with VIP: A Video Infilling and Prediction Dataset for Evaluating Video Chain-of-Thought (https://aclanthology.org/2023.emnlp-main.15/)
- Anthology ID: 2023.emnlp-main.15 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 결과들은 이미지를 자연어를 사용해 추론하는 vision-language system의 능력을 보여주었으나 비디오 추론 능력은 아직 충분히 연구되지 않았다. 
    2. 우리는 비디오 추론을 작은 수의 핵심 프레임에 대한 순차적 이해로 구성하고, 비디오 처리의 복잡성을 완화시키면서 vision-language의 강력함과 로버스트함을 활용하는 것을 제안한다. 
    3. 새로운 응용 프로그램을 평가하기 위해, 우리는 VIP라는 도전적인 데이터셋을 소개하는데 이는 비디오의 chain-of-thought를 통해 모델의 추론 능력을 탐구하기 위해 설계되었다. 비디오 인구 및 비디오 예측과 같은 두 가지 작업을 제안하여 그 능력을 평가한다.

###### GPTAraEval: A Comprehensive Evaluation of ChatGPT on Arabic NLP (https://aclanthology.org/2023.emnlp-main.16/)
- Anthology ID: 2023.emnlp-main.16 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT는 영어 벤치마크에서 뛰어난 성능을 보이지만, 다양한 언어 환경에서의 효능은 크게 알려져 있지 않다. 이 논문에서는 ChatGPT를 아랍어와 방언에 대해 평가하고자 한다.
    2. 대규모 자동 및 인간 평가를 통해 ChatGPT의 성능을 조사하고, 영어에서 뛰어난 성능을 보이는 ChatGPT보다 아랍어에 맞춰 finetuning된 작은 모델들이 일관적으로 우위에 서 있다는 결론에 도달하였다.
    3. ChatGPT와 GPT-4의 모던 스탠다드 아랍어와 아랍어 방언에 대한 성능을 세심하게 비교, 분석한 결과 두 모델 모두 MSA에 비하여 아랍어 방언을 다루는 데 상대적인 약점을 가지고 있다는 것을 밝혀냈다.

###### Dual-Channel Span for Aspect Sentiment Triplet Extraction (https://aclanthology.org/2023.emnlp-main.17/)
- Anthology ID: 2023.emnlp-main.17 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Aspect Sentiment Triplet Extraction (ASTE)"는 세세한 측면 기반 감성 분석(ABSA)의 합성 작업 중 하나로, 측면 용어, 해당 의견 용어 및 연관된 감성 방향의 세트를 추출하는 것을 목표로 한다. 
    2. 기존의 스팬 기반 접근 방법들은 모든 가능한 스팬을 열거해야 하는 문제점이 있었으나, 이 연구에서는 품사와 관련된 통사 관계를 이용하여 스팬 후보를 생성함으로써 이 부담을 줄이고, 스팬 표현에 풍부한 언어적 정보를 제공한다.
    3. 두 개의 공개 데이터셋에서의 실험 결과, 우리의 설계의 효과성과 ASTE/ATE/OTE 작업에서의 우수성을 입증하였다.

###### Cultural Concept Adaptation on Multimodal Reasoning (https://aclanthology.org/2023.emnlp-main.18/)
- Anthology ID: 2023.emnlp-main.18 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 저희는 다문화적인 역량을 향상시키기 위한 문화적 적응 방법의 개발이 중요하다고 생각하며, 낮은 자원 데이터에 대한 성능을 개선하고 모두가 공정한 기회를 누릴 수 있는 최첨단 기술을 제공합니다.
    2. 이 논문에서는 부족한 데이터와 비싼 어노테이션의 어려움을 극복하기 위해 높은 자원 문화를 활용하여 낮은 자원 문화를 이해시키는 방법을 소개합니다.
    3. 실험 결과, 우리의 방법은 다섯 가지 언어에 대해 제로샷과 퓨샷 설정에서 기존 다문화 및 다모달 모델의 성능을 일관되게 향상시킵니다.

###### Understanding Compositional Data Augmentation in Typologically Diverse Morphological Inflection (https://aclanthology.org/2023.emnlp-main.19/)
- Anthology ID: 2023.emnlp-main.19 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 데이터 부족 문제를 해결하기 위해 낮은 자원의 자동 형태 변형에서는 데이터 확장 기법이 널리 사용되지만, 이러한 기법의 전체적인 의미는 여전히 분명하지 않은 상태이다.
    2. 본 연구에서는 데이터 확장 전략 중 하나인 StemCorrupt의 이론적 측면에 대해 조명하고, 기존의 훈련 데이터 예제에서 어간 문자를 무작위로 치환하여 가상의 예제를 생성하는 방법을 분석한다.
    3. StemCorrupt는 근본적인 데이터 분포의 변화를 가져오며, 내재적인 구성합성 구조를 보여준다는 것을 발견하고, 일정 수준의 다양성과 예측적 불확실성을 가지는 데이터 포인트의 하위 집합을 선택하는 것이 경쟁하는 기준에 비해 데이터 효율성을 크게 향상시킨다는 것을 보여준다.

###### Evaluating Object Hallucination in Large Vision-Language Models (https://aclanthology.org/2023.emnlp-main.20/)
- Anthology ID: 2023.emnlp-main.20 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에 제안된 대형 언어 모델 (LLM)의 뛰어난 언어 능력에서 영감을 받아, 복잡한 다중 모달 태스크의 성능을 향상시키기 위해 강력한 LLM을 통합한 대형 시각-언어 모델 (LVLM)이 제안되었습니다.
    2. 그러나 LVLM은 객체 환시(object hallucination)라는 문제점을 가지고 있으며, 이는 설명과 대상 이미지와 일치하지 않은 객체를 생성하는 경향이 있습니다.
    3. 본 논문은 LVLM의 객체 환시에 대한 체계적인 연구를 제시하며, 대표적인 LVLM에 대한 평가 실험을 수행하여 심각한 객체 환시 문제가 있는 것을 보여줍니다.

###### Event Ontology Completion with Hierarchical Structure Evolution Networks (https://aclanthology.org/2023.emnlp-main.21/)
- Anthology ID: 2023.emnlp-main.21 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 event detection 방법은 사전에 정의된 event schemas에 의존하지만, 이는 비용이 많이 들고 schemas의 커버리지가 제한되는 문제점이 있다.
    2. 본 논문에서는 Event Ontology Completion (EOC)이라는 새로운 연구 과제를 제안하고, 이를 위해 Hierarchical Structure Evolution Network (HalTon)을 개발하였다.
    3. 실험 결과, HalTon은 기존방법보다 ARI score에서 8.23%, 8.79%, 8.10% 더 높은 성능을 보여준다.

###### Parameter-efficient Tuning for Large Language Model without Calculating Its Gradients (https://aclanthology.org/2023.emnlp-main.22/)
- Anthology ID: 2023.emnlp-main.22 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델의 모든 매개변수를 fine-tuning 하는 것은 계산 및 시간적 리소스가 크게 요구되는데, 본 논문에서는 gradient를 계산하지 않고도 매개변수 효율 조정이 가능한 새로운 방법을 제안한다.
    2. 작은 언어 모델로부터 얻은 parameter-efficient 모듈들을 대규모 언어 모델로 전송하여 smooth하고 효과적인 적응 프로세스를 보장하는데, 이를 위해 Bridge 모델을 도입한다.
    3. 본 방법은 T5와 GPT-2 언어 모델을 사용하여 SuperGLUE 벤치마크에서 fine-tuning 및 parameter-efficient tuning과 비교 가능한 성능을 달성하며, gradient 기반 최적화 없이도 parameter-efficient tuning에 비해 최대 5.7배의 메모리 절감을 달성한다.

###### Discourse Structures Guided Fine-grained Propaganda Identification (https://aclanthology.org/2023.emnlp-main.23/)
- Anthology ID: 2023.emnlp-main.23 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Propaganda는 주로 정치적 목적으로 대중을 선동하거나 오도하는 형태의 기만적인 이야기이다. 이 논문에서는 정치 뉴스에서 propaganda를 문장 수준과 토큰 수준에서 식별하는 것을 목표로 한다.
    2. Propaganda 콘텐츠는 인과관계를 나타내거나 주변 문장과 대조적인 어조로 작성된 문장에 더 자주 포함되어 있다는 것을 관찰했다.
    3. 따라서 우리는 propaganda 탐지를 위해 지역적 및 전역적 담화 구조를 결합하고, 주변 문장 사이의 PDTB-style 담화 관계 및 뉴스 기사의 일반적인 담화 역할을 식별하기 위해 두 가지 교사 모델을 구성한다.

###### CompoundPiece: Evaluating and Improving Decompounding Performance of Language Models (https://aclanthology.org/2023.emnlp-main.24/)
- Anthology ID: 2023.emnlp-main.24 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 복합어 분해 작업 연구는 한국어, 동양어 등 복합어 형성이 매우 생산적인 언어에만 집중되어 왔고, 많은 언어들의 복합어 및 비복합어가 포함된 공개 데이터셋이 없었다. 본 논문에서는 56개의 다양한 언어로 이루어진 255,000개의 복합어 및 비복합어 단어를 포함하는 데이터셋을 소개하고, 이를 사용하여 대용량 언어 모델의 복합어 분해 작업을 평가한다.
    2. 실험 결과, 대용량 언어 모델의 복합어 분해 작업 성능이 낮다는 것을 확인하였고, 이는 subword tokenization에 의해 불리하게 토큰화된 단어들에 대한 영향이 컸다. 따라서, 이러한 문제를 해결하기 위해 두 단계의 접근 방식을 제안한다. 
    3. 첫 번째 단계에서는 fully self-supervised objective를 사용하여 모델을 학습시키고, 두 번째 단계에서는 Wiktionary의 주석 달린 데이터를 사용하여 모델을 fine-tuning한다. 이를 통해 unsupervised 모델은 이전에 보고된 모델보다 13.9%의 정확도를, fine-tuned 모델은 이전에 보고된 모든 복합어 분해 도구들보다 우수한 성능을 보였다.

###### Improving Image Captioning via Predicting Structured Concepts (https://aclanthology.org/2023.emnlp-main.25/)
- Anthology ID: 2023.emnlp-main.25 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이미지 캡션 작업에서 이미지와 텍스트 간의 의미적 간극을 해결하는 것이 어려운데, 이 분야의 기존 연구들은 의미 개념을 두 모드 간의 다리 역할로 취급하고 캡션 성능을 향상시키는 데 일부 주목했다.
    2. 그러나 이와 관련된 개념들의 관계를 무시하는 경우가 많으며, 이는 이미지의 객체 뿐만 아니라 텍스트의 단어 종속성에도 의존하기 때문에 좋은 설명을 만들어내는 과정 개선의 상당한 잠재력을 제공한다.
    3. 이 논문에서는 개념과 개념 구조를 예측하기 위해 구조화된 개념 예측자 (SCP)를 제안하고, 이를 캡션 작업에 통합하여 개념을 통해 시각 신호의 기여도를 향상시키고, 더 나은 설명 생성을 위해 이들의 관계를 구별하는 데 활용한다.

###### GATITOS: Using a New Multilingual Lexicon for Low-resource Machine Translation (https://aclanthology.org/2023.emnlp-main.26/)
- Anthology ID: 2023.emnlp-main.26 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최신 기계 번역 모델과 언어 모델은 병렬 데이터에 기반하지 않고도 번역할 수 있지만, 여전히 예측 가능한 방식으로 많은 문제를 겪고 있다. 이 연구에서는 양방향 어휘 정리자를 활용하여 이러한 문제를 해결하는 방법을 제안한다.
    2. 연구에서는 어휘 데이터 증강을 통해 비지도 번역에서 상당한 성능 향상을 보여준다.
    3. 여러 가지 데이터 증강 방법을 비교하여 유사한 개선 효과를 나타내고, 이를 결합함으로써 더 큰 향상을 얻을 수 있다는 것을 보여준다.

###### Continually Improving Extractive QA via Human Feedback (https://aclanthology.org/2023.emnlp-main.27/)
- Anthology ID: 2023.emnlp-main.27 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사용자의 피드백을 통해 추출형 질문 응답 시스템을 지속적으로 개선하는 연구를 수행했습니다.
    2. 정보를 얻고자 하는 사용자들이 질문을 하고, 모델이 예측한 답변을 받고, 피드백을 제공하는 반복적인 접근법을 설계하고 적용했습니다.
    3. 우리의 실험 결과는 다양한 데이터 조건에서 추출형 QA 모델의 사용자 피드백을 통한 시스템 개선이 효과적이며, 도메인 적응에 큰 잠재력을 보여줌을 보여줍니다.

###### Using Interpretation Methods for Model Enhancement (https://aclanthology.org/2023.emnlp-main.28/)
- Anthology ID: 2023.emnlp-main.28 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. neural 자연어 처리 시대에서 neural 모델의 해석을 유도하려는 연구들이 존재하는데, 기계 번역 및 기타 태스크에 대해 모델이 gold rationale과 일치할 수 있도록 추가적으로 학습시키는 방법이 제안되었다.
    2. 이 논문에서는 인터프리테이션 방법과 gold rationale을 이용하여 모델을 향상시키기 위한 프레임워크를 제안한다. 이 방법은 다양한 인터프리테이션 방법을 포함할 수 있다.
    3. 실험 결과, 저자들이 제안한 프레임워크는 특히 저자들이 제안한 새로운 두 가지 방법이 대부분의 설정에서 gradient-based 방법보다 우수한 성능을 보인다는 것을 확인하였다.

###### An Expression Tree Decoding Strategy for Mathematical Equation Generation (https://aclanthology.org/2023.emnlp-main.29/)
- Anthology ID: 2023.emnlp-main.29 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어로부터 수학식을 생성하기 위해서는 수학 표현 간의 관계를 정확하게 이해해야 한다. 기존 접근법은 토큰 수준과 표현 수준으로 크게 분류된다. 전자는 수학식을 수학 언어로 취급하여 순차적으로 수학 토큰을 생성한다. 후자는 각 표현을 한 번에 하나씩 생성한다. 하지만 각 표현은 문제 해결 단계를 나타내며, 이러한 단계 사이에는 병렬 또는 종속 관계가 자연스럽게 존재하는데, 현재의 순차적인 방법에서는 이를 무시한다.
    2. 따라서 우리는 표현 수준 생성에 트리 구조를 통합하고, 표현 트리 디코딩 전략을 제안한다. 표현을 노드로 하는 트리를 생성하기 위해 우리는 레이어별 병렬 디코딩 전략을 사용한다. 각 레이어에서는 독립적인 표현 (리프 노드)을 병렬로 디코딩하고, 다른 표현에 의존하는 부모 노드 표현을 순차적으로 생성하기 위해 레이어별로 병렬 디코딩을 반복한다. 또한, 각 레이어에서 여러 예측과 주석을 매칭시키기 위해 이분 매칭 알고리즘을 사용한다.
    3. 실험 결과, 우리의 방법이 다른 기준선에 비해 향상된 성능을 보이며, 특히 복잡한 구조를 가진 수학식에 대해서 더 좋은 성과를 얻는다.

###### Bootstrapping Small & High Performance Language Models with Unmasking-Removal Training Policy (https://aclanthology.org/2023.emnlp-main.30/)
- Anthology ID: 2023.emnlp-main.30 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "BabyBERTa는 작은 양의 아동 언어 모델로, 훈련 과정에서 단어들이 완전히 노출되지 않았음에도 불구하고 RoBERTa-base와 비교할만한 수준의 문법성을 보여준다."
    2. 이 논문은 BabyBERTa 기반 모델의 성능을 연구하며, Semantic Role Labeling (SRL) 및 두 개의 추출형 질의응답 과제에 초점을 맞추어 데이터 양과 모델 크기를 줄여 효율적인 시스템 구축을 목표로 한다.
    3. 실험 결과, BabyBERTa는 10M 단어로 훈련할 때 RoBERTa의 마스킹 정책보다 어느 정도 강력한 시작점이며, 이 경향은 훈련 데이터를 더 추가할 때에도 유지되는 것으로 나타났다.

###### Diversity Enhanced Narrative Question Generation for Storybooks (https://aclanthology.org/2023.emnlp-main.31/)
- Anthology ID: 2023.emnlp-main.31 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이미 많은 발전이 있었지만, 질문 생성(QG)에서 생성된 질문의 다양성을 향상하거나 측정하는 것에는 아직도 도전이 남아있다.
    2. 본 논문에서는 맥락과 질문에 초점을 맞춘 mQG 모델을 소개하며, 다양하고 답변 가능한 여러 개의 질문을 생성할 수 있다. 
    3. mQG는 SQuAD 2.0으로 세분화된 질문을 분류하여 생성된 질문의 답변 가능성을 검증하며, FairytaleQA 데이터셋에서 훈련 및 평가되고 TellMeWhy 및 SQuAD1.1 데이터셋에도 제로샷 적용을 수행한다.

###### Debiasing Made State-of-the-art: Revisiting the Simple Seed-based Weak Supervision for Text Classification (https://aclanthology.org/2023.emnlp-main.32/)
- Anthology ID: 2023.emnlp-main.32 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 약한 지도학습 텍스트 분류의 발전은 대부분 인간의 경험을 바탕으로 한 휴리스틱(근거)를 품질 좋은 가짜 라벨로 변환하기 위해 정교한 방법을 고안하는 것에 초점을 맞추고 있다.
    2. 이 논문에서는 유명한 가상 라벨 생성 방법인 seed matching 기반 방법을 재검토하여, 그 파워가 크게 과소평가되었다는 것을 보여준다.
    3. seed matching의 한계 성능은 단순한 seed-match 규칙에 의해 주입되는 라벨 편향으로 인해 발생하며, seed words를 삭제하면 이 편향을 완화시키고 더 나은 신뢰성을 학습할 수 있어 seed matching의 성능을 크게 향상시킬 수 있다는 것을 보여준다.

###### How to Enhance Causal Discrimination of Utterances: A Case on Affective Reasoning (https://aclanthology.org/2023.emnlp-main.33/)
- Anthology ID: 2023.emnlp-main.33 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대부분의 모델이 시맨틱 상관관계는 잘 파악하지만 특정한 인과관계를 결정하는 것에 어려움을 겪고 있다. 
    2. 이 논문에서는 대화 과정에 i.i.d. 잡음 요소를 통합하여 구조적 인과 모델(SCM)을 구축하는 방법을 제안한다. 
    3. 우리의 실험에서는 우리의 접근법의 효과성과 해석 가능성을 검증하였다.

###### Compressing and Debiasing Vision-Language Pre-Trained Models for Visual Question Answering (https://aclanthology.org/2023.emnlp-main.34/)
- Anthology ID: 2023.emnlp-main.34 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 Vision-Language Pre-trained Models(VLPs)은 언어 데이터셋의 편향에 의존하여 일반화하지 못하고, 메모리와 연산의 효율성도 낮은 문제가 있다.
    2. 본 논문에서는 VLP의 압축과 편향 보정을 동시에 고려하여 효과적으로 탐색한다.
    3. Sparse하고 robust한 subnetworks를 찾아 OOD 데이터셋에서 더 적은 파라미터로 좋은 성능을 보이는 것을 실험적으로 입증하였다.

###### Selectively Answering Ambiguous Questions (https://aclanthology.org/2023.emnlp-main.35/)
- Anthology ID: 2023.emnlp-main.35 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 신뢰할 수 있는 언어 모델은 답을 모르는 경우에 답을 하지 않아야 한다. 그러나 질문의 답이 알려지지 않은 경우는 다양한 이유로 인해 발생할 수 있다.
    2. 이 논문에서는 질문의 목적이나 맥락의 불명확성으로 인해 답이 애매한 경우에 대해 연구하였다.
    3. 이 실험에서는 샘플된 모델 출력별 반복 빈도수를 측정하는 것이 이전 연구에서 사용된 모델의 우도나 자체 검증보다 신뢰성 있는 캘리브레이션 방법임을 발견했으며, 이는 명확하지 않은 질문에 대한 답변에서 더욱 좋은 결과를 나타내었다.

###### Temporal Knowledge Graph Forecasting Without Knowledge Using In-Context Learning (https://aclanthology.org/2023.emnlp-main.36/)
- Anthology ID: 2023.emnlp-main.36 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 자연어 처리 기술을 사용하여 시간적 지식 그래프(TKG) 예측을 수행하는 방법을 제안하고, 사전 학습된 큰 언어 모델(LLM)이 최첨단 모델(SOTA)과 비슷한 성능을 보인다는 것을 관찰하였다.
    2. LLM은 사전 학습된 모델로, 예측 작업을 위해 정교한 아키텍처와 감독 학습을 사용하는 SOTA 모델과 비슷한 성능을 보여준다. 이러한 강력한 성능을 보이기 위해 LLM은 문맥의 상징적 패턴을 활용할 수 있으며, 사전 의미 지식은 필요하지 않다는 것을 실험에서 확인하였다.
    3. 더 나아가, 자연어 모델을 통해 TKG 예측을 수행할 때, 역사적 사실 선택, 프롬프트 구성, 정보 전파 제어, 출력의 확률 분포 구성에 대한 다양한 접근 방식을 탐구하였고, 이를 통해 더 강력한 성능을 얻었다.

###### Knowledge Graph Compression Enhances Diverse Commonsense Generation (https://aclanthology.org/2023.emnlp-main.37/)
- Anthology ID: 2023.emnlp-main.37 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 일반상식 설명을 생성하기 위해서는 문맥에 명시적으로 언급되지 않은 일반상식 지식에 대한 추론이 필요하다. 기존의 모델들은 ConceptNet과 같은 일반상식 지식 그래프를 사용하여 입력된 개념과 관련된 지식의 하위 그래프를 추출한다.
    2. 그러나 ConceptNet은 커버리지가 크고, 결국 광범위한 규모를 갖기 때문에 추출된 하위 그래프는 느슨하게 관련되거나 중복되는 정보를 포함할 수 있고, 이는 모델에 노이즈를 도입할 수 있다.
    3. 우리는 이를 해결하기 위해 과제에 관련된 지식에 초점을 맞춘 차별화 가능한 그래프 압축 알고리즘을 적용하여 이 문제를 해결하는 방법을 제안한다. 압축된 하위 그래프는 일반상식과 추론 설명을 생성하는 모델에 통합될 때 훨씬 다양한 출력을 제공한다.

###### Pragmatic Reasoning Unlocks Quantifier Semantics for Foundation Models (https://aclanthology.org/2023.emnlp-main.38/)
- Anthology ID: 2023.emnlp-main.38 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Generalized quantifiers (예: few, most)는 술어(predicate)가 얼마나 만족하는지 비율을 나타내는 데 사용됩니다. 최근 foundation models은 직접적인 훈련 신호가 없어 이 능력을 갖고 있는지 여전히 불확실합니다."
    2. 이 논문에서는 QuRe라는 크라우드 소싱된 인간 주석을 포함한 Wikipedia 문장의 일반화된 양화자를 도입하여 양자 이해를 탐구합니다.
    3. Natural language inference와 Rational Speech Acts 프레임워크를 결합한 PRESQUE를 사용하여 실험 결과, 추가적인 훈련 없이 특정 비율 범위를 예측하는 데 있어 PRESQUE가 literal listener 기준보다 20% 상대적인 개선을 나타내었습니다.

###### LLM-FP4: 4-Bit Floating-Point Quantized Transformers (https://aclanthology.org/2023.emnlp-main.39/)
- Anthology ID: 2023.emnlp-main.39 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 LLM-FP4라는 방법을 제안하여 용량이 큰 언어 모델에서 가중치와 활성화 함수를 후처리 방식으로 4비트 부동 소수점 값으로 양자화하는 것을 제안한다.
    2. 기존 post-training quantization (PTQ) 솔루션은 주로 정수 기반이며 8비트 미만의 비트 폭에 대해 어려움이 있다.
    3. 우리는 최적의 양자화 매개변수를 탐색함으로써 강력한 FP-PTQ 기준을 구축하고, 활성화 양자화 난이도를 해결하기 위해 채널별 활성화 양자화를 제안한다.

###### Improving Biomedical Abstractive Summarisation with Knowledge Aggregation from Citation Papers (https://aclanthology.org/2023.emnlp-main.40/)
- Anthology ID: 2023.emnlp-main.40 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 생물의료 문헌에서 파생된 초록은 전문적인 글쓰기 스타일과 생물의료 용어와 같은 독특한 도메인 특성을 가지고 있어 관련 문헌에 대한 깊은 이해가 필요하다. 그 결과, 존재하는 언어 모델은 도메인 특정 배경 지식의 부재로 생물의료 전문가가 작성한 요약문과 견줄만한 정확한 기술적 요약문을 생성하기 어렵다.
    2. 이 연구는 소스 기사 내에서 인용된 외부 논문으로부터 지식을 집계하여 생물의료 분야에서 언어 모델의 성능을 향상시키고자 한다. 우리는 도메인 특정 지식을 인용 논문으로부터 통합하는 새로운 어텐션 기반의 인용 집계 모델을 제안한다. 이 모델은 논문 내용과 인용 논문으로부터의 관련 지식을 모두 활용하여 신경망이 요약문을 생성할 수 있게 한다.
    3. 실험 결과, 우리의 모델은 최신 기법을 능가하며 생물의료 텍스트의 요약에서 상당한 개선을 달성한다. 이를 위해 우리는 대규모 생물의료 요약 데이터셋을 구축하고 이를 연구의 기반으로 공개한다.

###### Explanation Selection Using Unlabeled Data for Chain-of-Thought Prompting (https://aclanthology.org/2023.emnlp-main.41/)
- Anthology ID: 2023.emnlp-main.41 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 연구들은 대규모 언어 모델에 설명을 포함하여 구성하면 텍스트 추론 작업에서 뛰어난 성능을 얻을 수 있다는 것을 보여준다. 그러나 조금 다른 설명은 결과적인 작업 정확도에 큰 영향을 미칠 수 있다. 
    2. 이 논문에서는 어떻게 설명을 포함한 프롬프트를 블랙박스로 최적화할지 다루고 있다. 먼저 각 예제에 대해 후보 설명 집합을 생성하고, 이러한 설명들의 효과적인 조합을 찾기 위해 두 단계의 프레임워크를 사용한다.
    3. 실험 결과, 우리의 프록시 메트릭은 실제 정확도와 상관관계를 가지고 있으며, 우리의 방법은 크라우드워커 주석 및 단순한 탐색 전략보다 높은 성능의 프롬프트를 효과적으로 개선할 수 있다는 것을 보여준다.

###### HalOmi: A Manually Annotated Benchmark for Multilingual Hallucination and Omission Detection in Machine Translation (https://aclanthology.org/2023.emnlp-main.42/)
- Anthology ID: 2023.emnlp-main.42 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기계 번역에서의 환각은 입력과 관련없는 정보가 포함된 번역을 의미하며, 생략은 일부 입력 정보가 누락된 번역을 의미한다. 두 경우 모두 사용자 신뢰를 약화시키는 치명적인 오류인데, 이러한 병과가 포함된 주석이 달린 데이터는 극히 부족하며 고수준 언어에서만 제한적으로 존재한다.
    2. 본 논문에서는 다양한 자원 수준과 스크립트를 다루는 18개의 번역 방향에 대한 환각과 생략 현상에 대한 주석이 달린 데이터셋을 공개한다.
    3. 또한, 이전의 환각과 생략 탐지 방법들을 재방문하고, 단일 언어 쌍을 기반으로 한 결론들이 대규모 평가에는 거의 적용되지 않음을 보이며, 새로운 견고한 기준을 수립한다.

###### Gradient-based Gradual Pruning for Language-Specific Multilingual Neural Machine Translation (https://aclanthology.org/2023.emnlp-main.43/)
- Anthology ID: 2023.emnlp-main.43 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 멀티링구얼 뉴럴 기계 번역(MNMT)은 단일 모델로 여러 언어 간 번역을 편리하게 제공하지만, 고자원 언어에서 MNMT는 양쪽 번역 대조군에 비해 성능 저하가 발생할 수 있다.
    2. 이 논문에서는 이러한 문제를 해결하기 위해 MNMT를 위한 점진적 그래디언트 기반 가지치기 기법을 제안한다.
    3. 실험 결과, 저자들의 방법은 IWSLT와 WMT 데이터셋에서 현저한 성능 향상을 보여주었다.

###### LLM-powered Data Augmentation for Enhanced Cross-lingual Performance (https://aclanthology.org/2023.emnlp-main.44/)
- Anthology ID: 2023.emnlp-main.44 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 매우 제한된 데이터셋에서 다국어 상식 추론 데이터셋의 데이터 증강을 위해 대용량 언어 모델(Large Language Models, LLMs)을 활용하는 잠재력을 탐구한다.
    2. LLMs로 생성된 데이터를 활용하여 작은 다국어 모델(mBERT, XLMR)의 성능을 평가하고, 영어와 대상 언어로 생성된 데이터와 번역된 영어로 생성된 데이터의 성능을 비교한다.
    3. LLMs인 ChatGPT와 GPT-4는 대부분의 언어에서 자연스러운 텍스트와 논리적일관성을 잘 생성하지만, Tamil 같은 특정 언어에서 의미 있는 텍스트를 생성하는 데 어려움이 있으며, ChatGPT는 원본 데이터에 비해 타당한 대안을 생성하는 데 실패하는 반면, GPT-4의 예제는 경쟁력 있는 논리적 일관성을 보인다.

###### Prompt-based Logical Semantics Enhancement for Implicit Discourse Relation Recognition (https://aclanthology.org/2023.emnlp-main.45/)
- Anthology ID: 2023.emnlp-main.45 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 명시적 연결어 없이 담화 관계를 추론하는 IDRR은 여전히 중요하고 어려운 작업이다. 최근의 연구들은 주석된 의미로부터 계층 구조 정보를 활용하여 담화 관계를 향상시킬 수 있다는 것을 보여주고 있다.
    2. 그러나 IDRR의 성능과 견고성은 주석된 데이터의 가용성에 크게 제약을 받는다. 다행히도 명시적 연결어가 있는 주석되지 않은 발화의 풍부한 자료를 활용하여 담화 관계 특성을 향상시킬 수 있다.
    3. 연구에서는 IDRR을 위해 특정 주제 단어 예측 기법을 사용하여 사전 훈련된 언어 모델에 담화 관계에 관련된 지식을 주입하는 PLSE 방법을 제안한다. 실험 결과, 우리의 방법은 PDTB 2.0 및 CoNLL16 데이터셋에서 현재 최첨단 모델과 일관된 탁월한 성능을 보여준다.

###### VLIS: Unimodal Language Models Guide Multimodal Language Generation (https://aclanthology.org/2023.emnlp-main.46/)
- Anthology ID: 2023.emnlp-main.46 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어와 시각의 시너지를 활용하는 다중모달 언어 생성은 급격히 확장되는 분야이며, 그러나 복잡한 언어 이해를 필요로 하는 작업에서 기존 시각-언어 모델은 어려움을 겪고 있다.
    2. 이 논문에서는 비전-언어 모델의 시각 적응 능력과 텍스트만 있는 단일 모달 언어 모델의 언어 이해를 조합하여 별도의 학습 없이 복잡한 작업을 수행하는 VLIS(Vision-Language models as Importance Sampling weights)라는 새로운 프레임워크를 소개한다.
    3. VLIS는 시각-언어 모델로부터 각 이미지와 텍스트의 점별 상호정보를 추출하고, 이 값을 텍스트 모델의 토큰 likelihood를 조정하는 중요 표본추출 가중치로 사용함으로써 다양한 작업에서 vision-language 모델의 성능을 향상시킨다.

###### Conceptual structure coheres in human cognition but not in large language models (https://aclanthology.org/2023.emnlp-main.47/)
- Anthology ID: 2023.emnlp-main.47 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어의 신경망 모델은 오랫동안 마인드와 뇌의 개념적 표현에 대한 가설 개발 도구로 사용되어 왔다. 최근 언어 모델에서는 인지심리학에서 일반적으로 사용되는 방법과 거의 동일한 방법을 사용하여 개념적 표현의 잠재적 구조를 조사하는 것이 가능하다. 
    2. 이 연구에서는 인간과 GPT-3의 DaVinci 변형이라는 잘 알려진 대형 언어 모델에서 어깨너머 대화방법으로도 작동하는 세 가지 기법을 사용하여 양쪽의 어휘-의미 구조를 추정하고 비교한다. 
    3. 결과적으로, LLM 행동에서 추정된 구조는 개별적으로 인간 행동에서 추정된 구조와 일치하지만, 특정 작업에 의존하므로 서로 일관되지 않은 추정 값이 나온다. 이 결과는 최신 LLM의 지식과 인간 인지와의 차이점중 한가지를 보여준다.

###### Towards LLM-driven Dialogue State Tracking (https://aclanthology.org/2023.emnlp-main.48/)
- Anthology ID: 2023.emnlp-main.48 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 상태 추적(DST)은 과업 지향형 대화 시스템에서 사용자 목표와 시스템 동작을 정확하게 추적하는 데 매우 중요하다. 이 연구에서는 ChatGPT의 DST 능력을 초기로 조사한 결과를 보고한다.
    2. ChatGPT는 DST 작업에서 뛰어난 성능을 발휘하여 연구자들에게 가치 있는 통찰력을 제공하고 대화 시스템의 설계와 향상에 유용한 방향을 제시한다.
    3. 그러나 ChatGPT는 소스가 공개되지 않아 요청 제한과 데이터 프라이버시 우려 등의 중요한 한계가 있다. 이를 해결하기 위해 작은 오픈 소스 기반 모델을 기반으로 하는 LDST 라는 LLM 기반 DST 프레임워크를 제안한다.

###### Learning Language-guided Adaptive Hyper-modality Representation for Multimodal Sentiment Analysis (https://aclanthology.org/2023.emnlp-main.49/)
- Anthology ID: 2023.emnlp-main.49 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다중 모달 감성 분석(MSA)은 다양한 소스(언어, 비디오, 오디오 등)로부터 풍부한 정보를 활용하여 효과적이지만, 모달 간 감성과 무관한 정보 또는 충돌하는 정보들은 성능 향상을 방해할 수 있다.
    2. 따라서 저희는 Adaptive Hyper-modality Learning (AHL) 모듈을 사용하여 서로 다른 스케일의 언어 기능을 가이드로 하여 시각 및 오디오 기능에서 무관성/충돌 억제 표현을 학습하는 Adaptive Language-guided Multimodal Transformer (ALMT)를 제안한다.
    3. ALMT는 다중 모달 융합을 통해 보완적이고 통합된 표현을 얻어 효과적인 MSA를 수행하며, MOSI, MOSEI, CH-SIMS와 같은 인기 있는 데이터셋에서 최고의 성능을 달성하고, 무관성/충돌 억제 매커니즘의 타당성과 필요성을 보여주는 다양한 실험 결과를 보여준다.

###### Multitask Multimodal Prompted Training for Interactive Embodied Task Completion (https://aclanthology.org/2023.emnlp-main.50/)
- Anthology ID: 2023.emnlp-main.50 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인터랙티브하고 신체적인 작업은 기존의 Vision & Language (VL) 모델들에게 적어도 두 가지 기본적인 어려움을 제시하는데, 하나는 언어를 행동과 관측들의 경로에 기반하여 정립하는 것이고, 또 하나는 지시를 명확히 하는 것이다.
    2. 이 문제를 해결하기 위해, 우리는 Embodied MultiModal Agent (EMMA)라는 통합된 인코더-디코더 모델을 제안한다. EMMA는 이미지와 경로를 근거로 하여 행동 예측을 멀티모달 텍스트 생성으로 바꾼다. EMMA는 모든 작업을 텍스트 생성으로 통합함으로써, 작업 간의 전이를 용이하게 하는 행동 언어를 학습한다.
    3. 독립적으로 훈련되는 모듈러 접근법과는 달리, EMMA는 각 작업이 목표 달성에 기여하는 하나의 멀티태스크 모델을 사용한다. EMMA는 몇 가지 VL 벤치마크에서 유사한 모델과 비슷한 성능을 보이며, Dialog-guided Task Completion (DTC)에서는 새로운 최고 성능(36.81% 성공률)을 보여준다. (DTC는 Alexa Arena에서 독립 가이드가 있는 에이전트를 평가하는 벤치마크입니다.)

###### We’re Afraid Language Models Aren’t Modeling Ambiguity (https://aclanthology.org/2023.emnlp-main.51/)
- Anthology ID: 2023.emnlp-main.51 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 어디선가 모호함은 자연어의 본질적인 특징이다. 모호한 언어를 처리하는 것은 대화상대로서 오해를 예상하고 청취자로서 해석을 수정하는데 핵심적인 부분이다. 이 논문에서는 AmbiEnt라는 언어학자 주석이 달린 1,645개의 다양한 모호한 어구 예제를 활용하여 사전 훈련된 언어 모델이 모호함을 인식하고 가능한 의미를 분리하는 첫 번째 평가를 제시한다.
    2. 사전 훈련된 언어 모델은 모호함을 인식하고 의미를 분리하기 위한 작업에서 여전히 매우 어렵다는 것을 발견한다. Crowdworker 평가에서 GPT-4의 생성된 모호 해소는 데이터셋의 모호 해소에 비해 올바른 경우에만 32%의 정확도를 보였다. 
    3. 마지막으로, 모호함에 민감한 도구의 가치를 보여주기 위해, 다중 레이블 NLI 모델이 모호함으로 인해 잘못된 정치적 주장을 찾아내는 데 사용될 수 있음을 보여준다. NLP에서 모호함의 중요성을 되새기도록 연구 분야에 독려한다.

###### Linear-Time Modeling of Linguistic Structure: An Order-Theoretic Perspective (https://aclanthology.org/2023.emnlp-main.52/)
- Anthology ID: 2023.emnlp-main.52 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트 간의 관계를 모델링하는 것은 자연어를 이해하는 데 필수적이다. 하지만 이와 같은 작업은 토큰들 간의 조합에 대한 비교가 필요하므로 문자열의 길이에 대한 이차 시간 복잡도를 가진다. 
    2. 우리는 토큰 간의 관계를 문자열에 대한 부분 순서로 변환하여 이러한 비교를 피할 수 있으며, 또한 작업의 복잡도를 선형으로 감소시킬 수 있다고 보여준다. 
    3. 실험 결과, 우리의 방법은 의존성 구문 및 핵심 분석 작업에서 최첨단 또는 비슷한 성능을 달성한다는 것을 보여준다. 또한, 우리의 방법의 선형 복잡성과 병렬성은 그래프 기반 공유 지침 해결 모델의 속도를 두 배로 높이고, 그래프 기반 의존성 파서의 속도를 10배 높인다.

###### GEMINI: Controlling The Sentence-Level Summary Style in Abstractive Text Summarization (https://aclanthology.org/2023.emnlp-main.53/)
- Anthology ID: 2023.emnlp-main.53 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인간 전문가들은 문서에서 문장을 추출하거나 다양한 정보를 퓨전하여 요약을 작성하는 등 다양한 기술을 활용한다. GEMINI 모델은 이러한 다양성을 따라하기 위해 문장 다시 작성과 요약 기술을 흉내내는 리라이터와 생성기를 통합하는 방식으로 구성되어 있다.
    2. GEMINI는 특정 문서 문장을 다시 작성할지 아니면 요약 문장을 처음부터 생성할지 선택하는 적응형 모델이다.
    3. 실험 결과, GEMINI는 순수하게 인용적 요약 기법이나 다시 작성 기법보다 성능이 뛰어나며, WikiHow 데이터셋에서 최상의 결과를 달성한다. 또한, 문맥에 따라 요약 문장의 인간적 스타일이 일관되게 예측 가능하다는 것을 실험 결과로 보여주고 있다.

###### Fidelity-Enriched Contrastive Search: Reconciling the Faithfulness-Diversity Trade-Off in Text Generation (https://aclanthology.org/2023.emnlp-main.54/)
- Anthology ID: 2023.emnlp-main.54 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 생성 작업에서 자주 발생하는 환영(hallucination) 문제에 대해 다루고 있다. 언어 모델은 종종 유창하고 설득력 있는 내용을 생성하지만 제공된 소스와 일관성이 부족하여 잠재적인 부정확성을 초래한다. 
    2. 제안된 새로운 디코딩 방법인 FECS는 문맥에 민감한 규제항을 사용하여 대조 탐색 프레임워크를 확장한다. FECS는 제공된 소스와 의미적으로 유사한 토큰을 촉진하면서 생성된 텍스트의 반복성을 벌점화한다. 
    3. FECS는 환영에 취약한 두 작업인 요약 생성과 대화 생성에서 효과적임을 보여준다. 결과는 FECS가 다양한 언어 모델 크기에서 충실성을 지속적으로 향상시키면서 잘 수행되는 디코딩 알고리즘과 비슷한 출력 다양성을 유지한다는 것을 보여준다.

###### Analyzing Norm Violations in Live-Stream Chat (https://aclanthology.org/2023.emnlp-main.55/)
- Anthology ID: 2023.emnlp-main.55 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 유해한 언어, 예를 들어 혐오 발언은 사용자가 온라인 커뮤니티에서 참여하는 것을 방해하고 인기있는 플랫폼에서 즐기는 것을 어렵게 만들 수 있다. 하지만 이러한 유해한 언어를 탐지하기 위한 이전 접근 방식은 Reddit와 Twitter와 같은 온라인 포럼과 소셜 미디어의 대화에 주로 관심을 두었으며, 라이브 스트리밍 플랫폼인 Twitch와 YouTube Live에서의 대화에 적용할 때 효과적이지 않다는 것이다.
    2. 따라서 이 논문에서는 라이브 스트리밍 플랫폼에서의 대화에서의 규범 위반을 탐지하기 위한 최초의 NLP 연구를 제시한다. 우리는 Twitch에서 4,583개의 중재된 댓글을 주석으로 달고 라이브 스트림 채팅에서 규범 위반 범주를 정의한다.
    3. 우리는 이 연구를 통해 사람들이 라이브 스트림 모더레이션에서 사용하는 정보적 문맥을 파악하고, 문맥을 활용하여 규범 위반을 식별하는 모델을 훈련시킨다는 것을 밝혔으며, 결과적으로 적절한 문맥 정보가 모더레이션 성능을 35% 향상시킬 수 있다는 것을 보여준다.

###### Coarse-to-Fine Contrastive Learning in Image-Text-Graph Space for Improved Vision-Language Compositionality (https://aclanthology.org/2023.emnlp-main.56/)
- Anthology ID: 2023.emnlp-main.56 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 비교적 괜찮은 성과를 보였던 Contrastively trained vision-language 모델들이 객체, 속성, 관계에 대한 구성적 추론 능력이 제한되어 있다는 한계점이 최근에 드러나고 있다.
    2. 우리는 이미지에서 파싱된 scene graph를 이미지 scene graph의 프록시로 간주하고, 이미지와 텍스트 간의 거친-정교한 contrastive 학습 목적함수와 함께 다양한 복잡도의 문장을 동일한 이미지에 맞추는 그래프 분해 및 augmentation 프레임워크를 제안한다.
    3. 우리는 어트리뷰트 바인딩과 관계 이해를 향상시키기 위해 scene graph 공간에서의 새로운 negative mining 기법을 도입하였고, 다양한 벤치마크에서 속성 바인딩, 관계 이해, 체계적 일반화, 생산성을 크게 향상시키는 효과적인 접근법을 실험을 통해 입증하였다.

###### Reading Books is Great, But Not if You Are Driving! Visually Grounded Reasoning about Defeasible Commonsense Norms (https://aclanthology.org/2023.emnlp-main.57/)
- Anthology ID: 2023.emnlp-main.57 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 상식적 규범은 맥락에 의해 유연하게 결정된다: 책을 읽는 것은 대부분 좋지만, 운전할 때는 그렇지 않다. 그러나 시각적으로 제공되는 상황에서 이러한 맥락을 해결하는 것은 기계에게는 도전이다.
    2. 이 논문에서는 시각적 이해와 상식적 규범에 대한 추론이 필요하며, 이를 연구하기 위한 NormLens라는 다중 모달 벤치마크를 구축한다.
    3. 특히 우리는 대형 언어 모델로부터 상식적 지식을 추출하여 모델과 인간의 일치도를 높이는 간단하면서도 효과적인 방법을 제시한다.

###### Enhancing Uncertainty-Based Hallucination Detection with Stronger Focus (https://aclanthology.org/2023.emnlp-main.58/)
- Anthology ID: 2023.emnlp-main.58 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델은 다양한 분야에서 놀라운 성능을 보여주어 인기를 끌었지만, 높은 확률로 유사하지 않거나 무의미한 출력을 생성하는 경우가 많다. 
    2. 기존에는 외부 지식을 필요로 하거나 다양한 응답을 샘플링하여 일관성을 검증하는 방법을 사용했지만 비용과 효율성이 문제였다.
    3. 이 논문에서는 언어 모델의 허상 여부를 탐지하기 위해 참조 자료없이 불확실성 기반의 새로운 방법을 제안한다. 실험 결과는 우리의 방법이 모든 평가 메트릭에서 최고 수준의 성능을 달성하고 추가 정보가 필요하지 않도록 한다.

###### FactKB: Generalizable Factuality Evaluation using Language Models Enhanced with Factual Knowledge (https://aclanthology.org/2023.emnlp-main.59/)
- Anthology ID: 2023.emnlp-main.59 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 신뢰할 수 있는 요약 시스템의 진보와 채택을 위해 자동 생성된 요약의 사실적 일치성을 평가하는 것은 필수적이다.
    2. 기존의 사실성 평가 모델은 새로운 도메인에서 entity와 relation 오류에 특히 취약하여 robust하지 않다.
    3. 우리는 외부 지식 베이스에서 추출한 사실을 사용하여 사실성 평가 모델을 사전 훈련시키는 간단하고 일반화 가능한 FactKB 방법을 제안한다.

###### Mitigating Backdoor Poisoning Attacks through the Lens of Spurious Correlation (https://aclanthology.org/2023.emnlp-main.60/)
- Anthology ID: 2023.emnlp-main.60 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 NLP 모델들은 신뢰할 수 없는 대규모 데이터셋으로 훈련되는 경우가 많아 악의적인 공격자가 모델 동작을 손상시킬 수 있는 위험이 존재한다.
    2. 이 논문은 악의적인 공격에 대한 방어 수단으로 spurious correlation을 완화하는 방법을 제안한다.
    3. 실험 결과, 해당 방어 방법은 backdoor 공격의 성공율을 크게 감소시키며 insertion-based 공격의 경우 거의 완벽한 방어를 제공한다.

###### Symbol tuning improves in-context learning in language models (https://aclanthology.org/2023.emnlp-main.61/)
- Anthology ID: 2023.emnlp-main.61 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 심볼 튜닝(symbol tuning)을 소개하는데, 이는 언어 모델을 실제 문장 대신 임의의 심볼로 된 입력-라벨 쌍으로 학습시키는 것이다. 심볼 튜닝은 모델이 지시사항이나 자연어 라벨을 사용하여 작업을 이해할 수 없을 때, 입력-라벨 매핑을 학습하여 작업을 수행하게끔 유도하는 개념을 기반으로 한다. 실험 결과, 심볼 튜닝은 보다 다양한 설정에서 성능을 향상시키며, 알고리즘적 추론 작업에서 뛰어난 결과를 보인다.
    2. 심볼 튜닝은 이전 지식을 무시하고 현재 문맥 정보를 사용하여 라벨을 덮어씌우는 기능이 더욱 강화되어, 입출력간의 관계 매핑에 더 효과적인 방법이다. 
    3. 심볼 튜닝은 보다 다양한 작업에서 성능이 향상되며, 특히 알고리즘적 추론 작업과 더 체계적인 문맥 정확성을 필요로 하는 작업에서 더 높은 성능을 보인다.

###### The neural dynamics of word recognition and integration (https://aclanthology.org/2023.emnlp-main.62/)
- Anthology ID: 2023.emnlp-main.62 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 청중은 다가오는 내용에 대한 기대와 감각적인 증거를 함께 결합하여 빠르고 소음이 있는 일상적인 언어에 있는 단어를 인식한다. 이 연구에서는 Bayesian decision theory로 통계적 가설을 제안하며, scalp EEG 신호를 분석하여 인식과 통합하는 과정과 관련된 뇌 활동의 근본적인 특성을 밝힌다. 
    2. 이 모델은 빠르게 인식되는 단어와 그렇지 않은 단어에 대해 서로 다른 뇌 처리를 보여준다. 
    3. 우리의 결과는 단어 인식과 함께 빠른 과정의 단어 통합을 결합한 말해 듣기 두 가지 모델을 지원하며, 이를 분리하는 데 도움이 될 수 있는 잠재적인 모델링 단계를 토의한다.

###### Tree of Clarifications: Answering Ambiguous Questions with Retrieval-Augmented Large Language Models (https://aclanthology.org/2023.emnlp-main.63/)
- Anthology ID: 2023.emnlp-main.63 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 오픈 도메인 질문 응답에서의 질문은 종종 다의성을 가지며, 여러 가지 해석이 가능하다. 이 논문에서는 Tree of Clarifications (ToC)라는 새로운 프레임워크를 제안하여 다의성을 다루고, 외부 지식을 활용하여 AQ에 대한 트리로 구성된 명료화를 생성하고 이를 통해 긴 형식의 대답을 생성한다.
    2. ToC는 ASQA에서 몇 가지 예상 밖의 상황(few-shot setup)에서 기존 기준선을 앞질러서 Disambig-F1 및 Disambig-ROUGE 측면에서 훈련 세트 전체에 훈련된 완전 지도학습과 비교했을 때 우수한 결과를 보여준다.
    3. 코드는 https://github.com/gankim/tree-of-clarifications에서 제공된다.

###### Incorporating Worker Perspectives into MTurk Annotation Practices for NLP (https://aclanthology.org/2023.emnlp-main.64/)
- Anthology ID: 2023.emnlp-main.64 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 아마존 메카니컬 터크(MTurk)에서의 자연어 처리를 위한 데이터 수집은 데이터 품질에 대한 연구와 NLP 연구자들 사이에서 공유되는 휴리스틱에 의존하는 경우가 많으나, MTurk 작업자들의 시각을 고려하지 않으면 작업자의 권리와 응답 품질과 관련된 문제가 발생할 수 있다. 
    2. MTurk 작업자들에 대한 조사 결과, NLP 연구자들의 지식과 작업자들의 선호 사항이 상충되는 경우가 많았다. 그들은 믿을 수 있고 합리적인 보수에 불확실하고 매우 높은 보수를 선호하는 추세이며, 인구 통계 질문에 흔히 거짓으로 대답하고 작업이 거부되는 것에 분노를 표했다. 
    3. 이러한 결과를 바탕으로 우리는 향후 NLP 연구에서 MTurk 작업자들의 경험을 고려하여 작업자의 권리를 존중하고 데이터 품질을 개선할 수 있는 방안을 제시한다.

###### Predict the Future from the Past? On the Temporal Data Distribution Shift in Financial Sentiment Classifications (https://aclanthology.org/2023.emnlp-main.65/)
- Anthology ID: 2023.emnlp-main.65 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 금융 텍스트의 시간적 데이터 분포 변동은 일반적으로 흐름 (prevalent) 하다. 금융 감성 분석 시스템은 어떻게 변화하는 데이터 분포에 강건하면서도 정확한 감성을 추론할 수 있는 변동성 있는 시장 환경에서 훈련되어야 하는가?
    2. 이 논문에서는 세년간의 실제 금융 소셜 미디어 데이터셋을 사용하여 시간적 데이터 분포 변동에서의 금융 감성 분석 시스템에 대한 실험을 수행한다. 그 결과, fine-tuned 모델은 시간적 분포 변동이 발생할 때 일반적인 성능 저하를 겪는다.
    3. 이러한 문제에 대응하기 위해 본 논문에서는 금융 텍스트의 독특한 시간적 특성에 영감을 받아 분포 탐지와 시계열 모델링을 결합한 새로운 방법을 제안한다. 실험 결과는 제안된 방법이 변동성 있는 금융 시장에서 진화하는 시간적 변화에 적응하는 모델의 능력을 향상시킨다는 것을 보여준다.

###### Look-back Decoding for Open-Ended Text Generation (https://aclanthology.org/2023.emnlp-main.66/)
- Anthology ID: 2023.emnlp-main.66 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 단순히 문맥을 따라가는 것이 아닌, 일관성 있는 언어 생성을 위해 확장된 디코딩 알고리즘인 Look-back을 제안한다.
    2. Look-back은 현재와 이전 디코딩 단계의 분포 차이를 추적하여 중복된 구문과 주제의 변화를 예측하고 제거함으로써 더 유창하고 일관성 있는 텍스트를 생성할 수 있다.
    3. 문서 연속성과 이야기 생성에서의 디코딩 실험을 수행하여, Look-back이 다른 강력한 디코딩 방법들을 능가하는 결과를 얻었다.

###### Large Language Models Can Self-Improve (https://aclanthology.org/2023.emnlp-main.67/)
- Anthology ID: 2023.emnlp-main.67 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델 (LLMs)은 다양한 작업에서 우수한 성능을 달성했지만, LLM의 fine-tuning은 광범위한 지도를 필요로 한다. 
    2. 하지만 사람들은 외부 입력 없이 자체적 thinking 으로 추론 능력을 향상시킬 수 있다. 
    3. 본 논문에서는 미리 학습된 LLM을 사용하여 라벨이 없는 질문에 대한 "높은 확신"이 있는 rationale-augmented 답변을 생성하고, 이를 대상 출력 값으로 사용하여 LLM을 fine-tuning하는 방법을 제안한다.

###### CodeT5+: Open Code Large Language Models for Code Understanding and Generation (https://aclanthology.org/2023.emnlp-main.68/)
- Anthology ID: 2023.emnlp-main.68 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large language models, LLMs)은 코드 지능(Code intelligence) 분야에서 두 가지 주요 한계를 가지고 있다. 첫째, 특정 아키텍처(encoder-only 또는 decoder-only)를 채택하거나 다양한 downstream 작업에 효율적인 아키텍처에 적용할 수 있는 융통성이 부족하다. 둘째, 몇몇 작업에 관련이 없을 수 있는 제한된 사전학습 목적을 사용하고 있어 성능 저하를 유발한다.
    2. 이 논문에서는 다양한 코드 작업에 적합하도록 유연하게 조합할 수 있는, encoder-decoder 구조의 LLM인 "CodeT5+"를 제안한다. 이 작업들을 위한 사전 학습 목표의 혼합을 제안하며, 이는 span denoising, contrastive learning, text-code matching, causal LM pretraining 작업을 다양한 단일 및 다중 언어 코드 코퍼스에서 수행한다.
    3. 우리는 CodeT5+를 처음부터 학습시키지 않고 사전에 학습된 LLM으로 초기화하고, 자연어 지시사항과 조화를 이루기 위해 instruction-tuning을 탐구한다. 우리는 zero-shot, finetuning, instruction-tuning을 포함한 다양한 설정에서 CodeT5+를 20개 이상의 코드 관련 벤치마크에서 평가하였고, 다양한 코드 관련 작업에서 최첨단 성능을 보였다. 특히 instruction-tuned CodeT5+ 16B는 다른 오픈 소스 코드 LLMs와 비교하여 HumanEval 코드 생성 작업에서 35.0% pass@1 및 54.5% pass@10의 최첨단 결과를 달성하여 OpenAI code-cushman-001 모델을 능가하였다.

###### Structural generalization in COGS: Supertagging is (almost) all you need (https://aclanthology.org/2023.emnlp-main.69/)
- Anthology ID: 2023.emnlp-main.69 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어처리(Natural Language Processing) 응용 프로그램에서 신경망(neural network)은 OOD(out-of-distribution) 예제에 대한 일반화에 실패한다고 알려져 있다. 특히 최근의 의미 분석 데이터셋에서는 신경망의 구성적 적용이 필요한 경우에 대한 제한 사항을 제기하고 있다. 
    2. 본 논문에서는 본래 그래프 기반 파싱 프레임워크(neural graph-based parsing framework)를 여러 가지 방법으로 확장하여 이 문제를 완화한다. 
    3. 실험적으로, 우리의 접근 방식은 구성적 적용에 대한 알려진 어려운 COGS 데이터셋에서 구조적 합성에 필요한 예제의 결과를 크게 향상시킨다.

###### BioT5: Enriching Cross-modal Integration in Biology with Chemical Knowledge and Natural Language Associations (https://aclanthology.org/2023.emnlp-main.70/)
- Anthology ID: 2023.emnlp-main.70 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 생물학 연구에서는 분자, 단백질, 자연어의 통합을 통해 약물 개발을 향상시키고 있는데, 문제는 유효하지 않은 SMILES 표현을 생성하고, 문맥 정보를 제대로 활용하지 않으며, 구조화되지 않은 지식과 구조화된 지식을 동일하게 처리한다는 것이다. 
    2. 따라서 이 논문에서는 BioT5라는 종합적인 사전학습 프레임워크를 제안하여, 화학 지식과 자연어 연관성을 통한 생물학의 교차 모달 통합을 강화한다. 
    3. BioT5는 SELFIES를 사용하여 100% 강력한 분자 표현을 만들고, 구조화되지 않은 생물학적 문헌의 문맥에서 생물 개체의 지식을 추출한다. 또한, BioT5는 구조화된 지식과 구조화되지 않은 지식을 구분하여 정보를 더 효과적으로 활용한다. 이후 fine-tuning을 통해 BioT5는 다양한 작업에서 우수한 성능을 보이며, 생물 개체의 내재된 관계와 속성을 잘 포착한다는 것을 보여준다.

###### Hyperpolyglot LLMs: Cross-Lingual Interpretability in Token Embeddings (https://aclanthology.org/2023.emnlp-main.71/)
- Anthology ID: 2023.emnlp-main.71 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 대형 언어 모델 (LLM)의 교양적 전달 학습은 매우 중요한 성질이다. 하지만 LLM은 언어 간의 관계를 어떻게 표현하는가? 입력 임베딩 간의 유사성은 해석 가능하며, 이 임베딩의 기하학은 모델 패밀리에 따라 다르다.
    2. 한 모델 (XLM-RoBERTa)은 임베딩에서 언어를 인코딩하고, 서로 다른 문자체계의 토큰을 99.2%의 정확도로 선형 분리할 수 있다.
    3. 다른 모델 패밀리 (mT5)는 교차 언어 의미 유사성을 나타내며, 어떤 토큰에 대해 50개의 가장 근접한 이웃은 평균적으로 7.61개의 문자체계로 나타나며, 자주 번역어들이다. 이 결과들은 명확한 평행 교차 언어 학습 및 사전 훈련 목적에 동기부여가 없음에도 불구하고 놀라운 결과이다.

###### Target-oriented Proactive Dialogue Systems with Personalization: Problem Formulation and Dataset Curation (https://aclanthology.org/2023.emnlp-main.72/)
- Anthology ID: 2023.emnlp-main.72 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "대화 목표를 사전에 정의하거나 특정 시스템 목표를 달성하기 위해 대화를 미리 조정하는 대상 지향적 대화 시스템은 대화형 AI 분야에서 흥미로운 영역이다."
    2. "본 논문은 <대화 행위, 주제> 쌍을 대화 목표로 고려하여 개인 맞춤형 대상 지향적 대화의 새로운 문제를 탐구한다. "
    3. "이를 위해, 우리는 역할 모델링 접근법을 사용하여 자동 데이터셋 조립 프레임워크를 제안하고, 이 프레임워크를 기반으로 대규모 개인맞춤형 대상 지향 대화 데이터셋인 TopDial을 구축했다."

###### SeqXGPT: Sentence-Level AI-Generated Text Detection (https://aclanthology.org/2023.emnlp-main.73/)
- Anthology ID: 2023.emnlp-main.73 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large Language Models, LLMs)은 인간과 유사한 내용을 생성할 수 있기 때문에 LLM의 남용에 대한 우려가 제기되고 있다. 그러므로 강력한 AI 생성 텍스트(AIGT) 감지기를 구축하는 것이 중요하다.
    2. 이 논문에서는 현재의 연구들이 문서 수준의 AIGT 감지만을 고려하고 있으며, 그래서 문장 수준의 감지 도전을 소개한다.
    3. Sequence X (Check) GPT라는 새로운 방법을 제안하며, 이 방법은 백박스 LLMs로부터의 로그 확률 목록을 sentence-level AIGT 감지의 특성으로 활용한다. 이 특성은 음성 처리에서 파동과 같이 구성되며, LLMs로 연구하기 어렵다. 따라서 저자들은 SeqXGPT를 컨볼루션과 self-attention 네트워크를 기반으로 구축하였다. 실험 결과는 이전의 방법들이 문장 수준의 AIGT 감지를 해결하는데 어려움이 있음을 보여주고, 저자들의 방법은 문장 및 문서 수준의 감지 도전에서 기준선 방법을 크게 능가할 뿐만 아니라 강한 일반화 능력을 보여준다.

###### QTSumm: Query-Focused Summarization over Tabular Data (https://aclanthology.org/2023.emnlp-main.74/)
- Anthology ID: 2023.emnlp-main.74 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사람들은 데이터 분석이나 특정 질문에 답하기 위해 주로 테이블을 참고한다. 사용자의 정보 요구에 맞는 정확한 테이블 요약을 제공할 수 있는 텍스트 생성 시스템은 관련 데이터 인사이트에 대한 효율적인 접근을 용이하게 할 수 있다. 이를 바탕으로 우리는 쿼리 중심 테이블 요약 작업을 정의하고, 주어진 테이블을 기반으로 인간과 유사한 추론과 분석을 수행하여 맞춤형 요약을 생성하는 텍스트 생성 모델을 개발하였다.
    2. 우리는 이 작업을 위해 QTSumm이라는 새로운 벤치마크를 소개한다. 이 데이터셋은 다양한 주제를 다루는 2,934개의 테이블에 대한 7,111개의 인간 주석된 쿼리-요약 쌍으로 구성되어 있다. 우리는 텍스트 생성, 테이블-텍스트 생성 및 대규모 언어 모델 등의 강력한 기준선 모델들을 QTSumm에서 실험하였다.
    3. 실험 결과와 수동 분석은 이 새로운 작업이 향후 연구에서 테이블-텍스트 생성에서 상당한 도전을 제시한다는 것을 보여주었다. 또한, 우리는 ReFactor라는 새로운 접근법을 제안하여 쿼리와 관련된 정보를 테이블 데이터에서 검색하고 추론하여 여러 자연어 사실을 생성한다. 실험 결과는 ReFactor가 모델 입력에 생성된 사실을 연결함으로써 기준선을 효과적으로 개선할 수 있음을 보여준다.

###### From Wrong To Right: A Recursive Approach Towards Vision-Language Explanation (https://aclanthology.org/2023.emnlp-main.75/)
- Anthology ID: 2023.emnlp-main.75 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 제한적으로 주어진 주석으로 시각-언어 모델을 적응시키기 위해 Insightful Explanation 생성에 대한 Recursive Visual Explanation 알고리즘인 ReVisE를 제안한다.
    2. 이 알고리즘은 다중 단계 접근법으로, 답변이 수렴할 때까지 차례로 시각적 특징, 답변 및 설명을 계산하여 설명 품질을 단계적으로 향상시킨다.
    3. ReVisE에 의해 생성된 설명은 몇 가지 셀프-트레이닝에 유용한 주석으로 활용되며, 이 방법은 사람 주석의 5%만을 사용하면서 이전 방법보다 뛰어난 성능을 발휘한다.

###### ‘Don’t Get Too Technical with Me’: A Discourse Structure-Based Framework for Automatic Science Journalism (https://aclanthology.org/2023.emnlp-main.76/)
- Anthology ID: 2023.emnlp-main.76 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 과학 저널리즘(automatic science journalism)을 지원하기 위해, 실제 세계의 과학 논문을 일반 대중에게 보다 적절한 뉴스 기사로 리포팅하는 자동 시스템을 설계하는 것이 목표이다.
    2. 새롭게 구축된 실제 데이터셋 (SciTechNews)을 소개하며, 해당 데이터셋의 논문, 해당 뉴스 기사, 전문가가 작성한 간단한 요약 스니펫의 튜플을 제공한다.
    3. 우리의 모델이 대상 독자를 위한 의미 있는 콘텐츠 계획을 상세히 설명하고, 선택한 정보를 단순화하며, 일관된 최종 보고서를 일반인 스타일로 생성하는 데 있어서 기존 baseline 방법 (예: Alpaca와 ChatGPT)보다 더 뛰어난 성능을 보인다는 폭넓은 자동 및 인간 실험을 통해 이를 증명한다.

###### LACMA: Language-Aligning Contrastive Learning with Meta-Actions for Embodied Instruction Following (https://aclanthology.org/2023.emnlp-main.77/)
- Anthology ID: 2023.emnlp-main.77 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "End-to-end Transformers는 훈련 데이터에서는 목표 환경을 본 바 있는 경우에는 근거 있는 지시 따르기에서 높은 성공률을 보여주었으나," 미처 보지 못한 환경에서는 어려움을 겪는다.
    2. 이러한 일반화의 부족은 에이전트가 자연어 지시에서의 미묘한 변화에 둔감하기 때문이다.
    3. 우리는 대조 학습을 통해 에이전트의 숨겨진 상태와 지시문을 명시적으로 맞추는 것을 제안하고, 고위 수준의 메타 액션을 도입하여 관련성을 강화함으로써, 에이전트가 미처 보지 못한 환경에서 일반화하는 것을 돕는다.

###### Penalty Decoding: Well Suppress the Self-Reinforcement Effect in Open-Ended Text Generation (https://aclanthology.org/2023.emnlp-main.78/)
- Anthology ID: 2023.emnlp-main.78 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 본 논문은 텍스트 생성에서 latent representations을 의미 있는 문장으로 변환하는 디코딩 알고리즘의 효과에 대해 연구한다.
    2. 또한, 디코딩 중 반복 페널티(repetition penalty)의 효과를 알기 위해 연구하였다.
    3. 실제사례를 통한 실험결과는 세 가지 전략을 적용한 이 방안이 인간의 출력과 유사한 고품질의 문장 생성을 돕는다는 것을 입증한다.

###### Towards Robust Pruning: An Adaptive Knowledge-Retention Pruning Strategy for Language Models (https://aclanthology.org/2023.emnlp-main.79/)
- Anthology ID: 2023.emnlp-main.79 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 잘 훈련된 모델들은 정확성과 희소성 뿐만 아니라 강인성에 대한 가지는 목표를 가지고 있다. 하지만 기존 방법들은 모델의 희소성을 지속적으로 증가시키면서 적대적 공격에 대한 강인성을 향상시키는 것에 어려움을 겪으며 재훈련 과정이 필요하다.
    2. 이 논문에서는 언어 모델의 강건성은 사전에 학습된 지식의 범위에 비례한다고 주장한다. 따라서 저자들은 밀집 언어 모델의 임베딩 공간과 피처 공간을 충실히 복제하는 사후 훈련 가지치기 전략을 제안하여 가지치기 과정에서 더 많은 사전 학습 지식을 보존하도록 한다.
    3. 실험 결과, 저자들의 방법은 BERT 모델에 대해 SST2, IMDB, AGNews 데이터셋에서 정확성, 희소성, 강인성, 가지치기 비용의 균형을 더 잘 잡아내는 것으로 나타났다. 이는 언어 모델에서 강인 가지치기에 대한 중요한 발전을 의미한다.

###### Clinical Contradiction Detection (https://aclanthology.org/2023.emnlp-main.80/)
- Anthology ID: 2023.emnlp-main.80 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문장의 모순을 탐지하는 것은 문헌의 타당성과 소비하는 정보의 중요한 요소이다. 의료 문헌은 모순된 진술로 가득 차 있다. 
    2. 의료 도메인에서 모순을 탐지하는 것은 임상 전문 지식이 필요하기 때문에 어렵다고 알려져 있다. 
    3. 본 논문에서는 의료 온톨로지를 활용하여 잠재적 의료 모순의 시드를 구축하는 '원격 지도' 방법을 제안한다.

###### Vera: A General-Purpose Plausibility Estimation Model for Commonsense Statements (https://aclanthology.org/2023.emnlp-main.81/)
- Anthology ID: 2023.emnlp-main.81 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 언어 모델은 지적인 면에서 뛰어날 수 있지만 일상적인 상식 오류를 포함한 텍스트를 생성하기도 한다. 이를 위해 본 논문에서는 기계 텍스트의 상식적 타당성을 평가할 수 있는 후방 검증(retrospective verification) 접근 방법을 제안한다.
    2. Vera라는 일반적인 모델을 소개하며, 이 모델은 진술문의 상식적 타당성을 추정하는 것을 학습한다. Vera는 19개의 QA 데이터셋과 두 개의 상식 지식 베이스에서 자동으로 변환된 약 7백만 개의 상식적 진술문을 사용하여 다양한 상식 도메인을 지원한다.
    3. Vera는 검증 형식의 상식 문제 해결에 적용되면, GPT-3.5/ChatGPT/GPT-4를 비롯한 기존 모델들보다 훨씬 우수한 성능을 보이며, 보다 효과적인 일반화 능력과 잘 조정된 결과를 제공한다. Vera는 기계가 생성한 상식적 지식을 걸러내는 데 능숙하며, ChatGPT와 같은 모델에서 생성된 잘못된 상식적 진술문을 실제 환경에서 탐지하는 데 유용하다.

###### Text-Transport: Toward Learning Causal Effects of Natural Language (https://aclanthology.org/2023.emnlp-main.82/)
- Anthology ID: 2023.emnlp-main.82 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 기술이 실제 환경에서 중요해짐에 따라, 언어의 변화가 독자의 인식에 어떤 영향을 주는지 이해하는 것이 중요하다.
    2. 이 논문에서는 텍스트 분포 하의 자연어로부터 인과효과를 추정하기 위한 Text-Transport 방법을 제안한다.
    3. Text-Transport를 사용하여 혐오 발언과 같은 현실적인 상황에서 인과 추론을 수행할 때 텍스트 도메인 간 인과효과가 크게 변하는 것을 보여주며 강력한 방법임을 입증한다.

###### How Does Generative Retrieval Scale to Millions of Passages? (https://aclanthology.org/2023.emnlp-main.83/)
- Anthology ID: 2023.emnlp-main.83 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기 존의 정보 검색 문제를 sequence-to-sequence 모델링 작업으로 바꾸어 전체 문서 코퍼스를 하나의 Transformer로 인코딩하는 generative retrieval의 신기한 패러다임이 등장하였다.
    2. 이 논문은 100K 정도의 규모의 문서 코퍼스에서 generative retrieval 기술을 개선하기 위한 다양한 접근 방식을 평가한 첫 번째 연구이다.
    3. 연구 결과로는 검색 성능과 관련하여 synthetic query를 문서 표현으로 사용하는 것의 중요성, 연산 비용을 고려할 때 기존의 구조 수정 제안의 비효율성, 그리고 모델 파라미터 스케일링의 한계 등을 발견하였다.

###### Unveiling the Implicit Toxicity in Large Language Models (https://aclanthology.org/2023.emnlp-main.84/)
- Anthology ID: 2023.emnlp-main.84 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(LLM)의 개방성과 놀라운 기능들은 악용될 경우 새로운 안전 문제를 일으킬 수 있다. 
    2. 기존 연구들은 주로 기존 독성 분류기로 감지하기 쉬운 독성 결과를 조사하는데 초점을 맞추었지만, 우리는 LLM이 간단한 zero-shot prompting으로 감지하기 어려운 다양한 암시적인 독성 결과를 생성할 수 있다고 보여준다.
    3. 또한, 우리는 강화학습(Reinforcement Learning, RL) 기반의 공격 방법을 제안하여 LLM에서 암시적인 독성을 유발한다. 실험 결과, RL fine-tuning을 통해 공격 성공률을 크게 향상시킬 수 있다는 것을 보여준다.

###### Is ChatGPT a General-Purpose Natural Language Processing Task Solver? (https://aclanthology.org/2023.emnlp-main.85/)
- Anthology ID: 2023.emnlp-main.85 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델 (LLM)의 발전으로 인해, LLM은 downstream 데이터에 대한 적응 없이도 다양한 자연어 처리 (NLP) 작업을 zero-shot으로 수행할 수 있는 능력을 보였다. 
    2. 이 논문에서는 ChatGPT의 zero-shot 학습 능력을 20개의 인기 있는 NLP 데이터셋에서 평가함으로써 현재 버전의 ChatGPT의 효과성과 한계를 실험적으로 분석한다.
    3. ChatGPT는 추론 능력을 필요로 하는 많은 작업에서 잘 수행되지만, 시퀀스 태깅과 같은 특정 작업에서는 여전히 도전을 겪는다는 결론을 찾아냈다.

###### Length is a Curse and a Blessing for Document-level Semantics (https://aclanthology.org/2023.emnlp-main.86/)
- Anthology ID: 2023.emnlp-main.86 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 contrastive learning (CL)이 이전의 언어 모델을 기반으로 문장과 문서 수준의 인코딩 능력을 복구하는 데에 널리 사용되고 있습니다. 그러나 이 논문에서는 CL을 기반으로 하는 모델의 길이 일반화 능력에 대해 의문을 제기하며, 텍스트의 길이에 의한 의미 변화에 취약하다는 것을 확인하였습니다.
    2. 저희는 길이 공격에 대한 이론적 기반을 유도하였고, 문서의 길이를 늘리는 것이 이미 CL에서 가져온 높은 문서 내 유사성을 강화시킬 것이라는 것을 보였습니다. 또한, CL이 제공하는 등방성(isotropy)도 훈련 중 노출된 텍스트의 길이 범위에 크게 의존한다는 것을 발견했습니다.
    3. 이러한 연구 결과에 영감을 받아, 저희는 간단하면서도 범용적인 문서 표현 학습 프레임워크인 LA(SER)3를 소개하였습니다. 이 모델은 세마틱으로 강건한 문장 표현 학습을 위한 길이에 무관한 자기 참조(length-agnostic self-reference) 방법을 사용하며, 표준 정보 검색 벤치마크에서 최고 성능을 달성했습니다.

###### ALCUNA: Large Language Models Meet New Knowledge (https://aclanthology.org/2023.emnlp-main.87/)
- Anthology ID: 2023.emnlp-main.87 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. NLP의 발달로 대규모 언어 모델 (LLM)들이 다양한 도메인에서 여러 가지 작업을 뛰어넘는 성능을 보이고 있는데, 기존 벤치마크들은 특히 새로운 지식을 다룰 때 이러한 모델의 역량을 충분히 측정하지 못할 수 있다.
    2. 이 논문에서는 빠르게 진화하는 세계에서 중요하면서도 어려운 새로운 지식을 처리하는 LLM의 능력을 평가하기 위한 벤치마크의 부재를 다룬다.
    3. 우리는 기존의 개체 속성과 관계를 조작하여 새로운 지식을 생성하는 KnowGen이라는 접근법을 제안하고, 이를 통해 LLM의 지식 이해, 구별, 연관성을 평가하기 위한 ALCUNA라는 벤치마크를 도입한다.

###### Location-Aware Visual Question Generation with Lightweight Models (https://aclanthology.org/2023.emnlp-main.88/)
- Anthology ID: 2023.emnlp-main.88 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "이 연구는 특정 지리적 위치와 관련된 데이터로부터 매력적인 질문을 생성하는 새로운 작업인 위치 인식 시각적 질문 생성(LocaVQG)을 소개한다. 구체적으로, 우리는 주변 이미지와 GPS 좌표로 이러한 위치 인식 정보를 표현한다. 이 작업에 대처하기 위해, 우리는 GPT-4를 활용하여 다양하고 복잡한 질문을 생성하기 위한 데이터셋 생성 파이프라인을 제시한다."
    2. "그런 다음, 휴대 전화와 같은 엣지 장치에 맞는 경량 모델을 학습할 수 있는 방법을 제안한다. 이를 위해, 위치 인식 정보로부터 매력적인 질문을 신뢰성 있게 생성할 수 있는 방법을 제안한다. 우리의 제안된 방법은 인간 평가(참여도, 연결성, 일관성) 및 자동 평가 메트릭(BERTScore, ROUGE-2)에서 기준 모델보다 우수한 성능을 보여준다."
    3. "또한, 데이터셋 생성과 작업 해결을 위한 우리의 제안된 기술을 정당화하기 위해 포괄적인 태색 연구를 수행한다."

###### MemeCap: A Dataset for Captioning and Interpreting Memes (https://aclanthology.org/2023.emnlp-main.89/)
- Anthology ID: 2023.emnlp-main.89 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "MemesCap" 데이터셋은 웹 사용자가 시각적 인쇄표현을 사용하여 자신의 생각을 표현하는 데에 폭넓게 사용되는 도구이다.
    2. 최근의 비젼-언어(VL) 모델들은 이미지 캡셔닝, 시각적 질문 답변 과제에서도 성공을 거두었지만, MemeCap 데이터셋에서 시각적 인쇄표현에 여전히 어려움을 겪고 있으며, 사람보다 훨씬 성능이 떨어진다.
    3. 우리는 시각적 인쇄표현을 이해하기 위해 면밀한 실험을 진행하였고, 최신 VL 모델을 사용하여 모델이 visual metaphors을 해석하는 데에 어려움을 겪는 점을 확인하였다.

###### Where to start? Analyzing the potential value of intermediate models (https://aclanthology.org/2023.emnlp-main.90/)
- Anthology ID: 2023.emnlp-main.90 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 연구에서 성급하게 훈련된 모델(finetuned models)이 vanillar pretrained model보다 더 좋은 기반 모델(base model)일 수 있다는 것을 관찰했다.
    2. 우리는 이러한 intertraining 방식을 다양한 영어 분류 작업에 대해 체계적으로 분석했고, 결과적으로 대상 데이터셋과 시작점으로 삼을 기반 모델에 대해 독립적으로 평가할 수 있는 잠재적인 이득이 있다는 것을 알았다.
    3. 또한, 우리의 분석을 기반으로 실제 환경에서 어떤 기반 모델을 선택할지 결정하는 것에 대한 실용적이고 효율적인 접근 방식을 제안한다.

###### Transcending Scaling Laws with 0.1% Extra Compute (https://aclanthology.org/2023.emnlp-main.91/)
- Anthology ID: 2023.emnlp-main.91 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델의 성능을 향상시키는 것은 컴퓨팅 비용이 많이 들지만, 이 논문에서 제안되는 UL2R은 상대적으로 작은 양의 추가 연산으로 기존 언어 모델과 스케일링 곡선을 크게 개선한다.
    2. 우리는 UL2의 mixture-of-denoiser 목적을 사용하여 최신 대형 언어 모델을 몇 단계 더 학습하는 방식인 UL2R을 제안하였고, 거의 소량의 추가 연산 비용과 새로운 데이터 소스 없이 큰 언어 모델의 스케일링 특성을 향상시킬 수 있음을 보여준다.
    3. U-PaLM이라고 불리는 8B, 62B, 540B의 규모의 새로운 모델들을 도입하여, UL2R로 기준이 되는 언어 모델인 PaLM을 계속 학습시켰으며, 540B의 스케일에서 타겟 모델의 성능과 비슷한 성능을 달성하면서 약간의 연산 비용을 절약하는 것을 보였다.

###### CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation (https://aclanthology.org/2023.emnlp-main.92/)
- Anthology ID: 2023.emnlp-main.92 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에 큰 언어 모델들이 발전함에 따라, ChatGPT와 같은 모델들은 많은 텍스트 주석 작업에서 유사했거나 심지어 인간 주석자를 능가하는 zero-shot 능력을 보여주고 있다.
    2. 이 논문은 인간과 언어 모델 사이에 주석 작업을 어떻게 분배하여 품질과 비용 목표를 동시에 달성할 수 있는지에 대해 연구한다.
    3. CoAnnotating이라는 새로운 패러다임을 제안하여 uncertainty를 활용하여 LLM의 주석 능력을 추정한다.

###### Optimizing Retrieval-augmented Reader Models via Token Elimination (https://aclanthology.org/2023.emnlp-main.93/)
- Anthology ID: 2023.emnlp-main.93 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Fusion-in-Decoder(FiD)는 질문 답변, 사실 확인과 같은 여러 open-domain 태스크에 효과적으로 사용되는 retrieval-augmented 언어 모델이다. 그러나 FiD에서는 먼저 검색된 passage들을 generative 모델(Reader)을 통해 처리하는데, 특히 긴 출력일 경우 디코딩 시간이 매우 지연될 수 있다. 
    2. 본 논문에서는 모든 검색된 passage들이 Reader 모델의 성능에 어떤 기여를 하는지 분석하고, 답변 생성 과정에 있어서 필수적인 정보를 제공하지 않을 수 있는 토큰 레벨에서 일부 검색 정보를 제거하는 방법을 제안한다.
    3. 실험 결과로, 우리의 방법은 성능 저하가 2%로 제한되며, 실행 시간을 최대 62.2%까지 줄일 수 있으며, 경우에 따라서는 성능을 향상시킬 수 있다는 것을 보여준다.

###### WSDMS: Debunk Fake News via Weakly Supervised Detection of Misinforming Sentences with Contextualized Social Wisdom (https://aclanthology.org/2023.emnlp-main.94/)
- Anthology ID: 2023.emnlp-main.94 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 가짜 뉴스 검출 방법들은 뉴스 기사의 진실성을 판단하는 데 초점을 맞추고 있어서 가짜 뉴스가 진실과 거짓의 요소를 혼합한 경우에 대해서는 과소 간주된다.
    2. 따라서 이 연구에서는 가짜 뉴스에 포함된 문장 수준의 오진에 대한 탐지를 다루는 새로운 과제를 조사한다. 
    3. "Weakly Supervised Detection of Misinforming Sentences (WSDMS)"라는 모델을 제안하여 문장 수준의 오진과 기사 수준의 진실성을 추론하는 데에 유용한 모델을 개발한다.

###### Robust Prompt Optimization for Large Language Models Against Distribution Shifts (https://aclanthology.org/2023.emnlp-main.95/)
- Anthology ID: 2023.emnlp-main.95 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large Language Model, LLM)은 다양한 자연어 처리 작업에서 높은 성능을 보여주지만, 작업 프롬프트의 구문에 따라서 성능이 크게 달라질 수 있어서 레이블된 작업 데이터를 사용한 자동 프롬프트 최적화에 대한 연구가 진행되고 있다.
    2. 그러나 이러한 프롬프트 최적화 기술은 실제 상황에서 발생하는 하위집단 분포 변화와 같은 분포 변화에 취약하다는 것을 알 수 있다. 이러한 문제에 대응하기 위해 우리는 LLM에 대한 강건한 프롬프트 최적화 문제를 제안하였는데, 이는 레이블된 소스 그룹으로 최적화된 프롬프트가 동시에 레이블되지 않은 타겟 그룹에도 적용될 수 있는 능력을 요구한다.
    3. 이를 해결하기 위해 우리는 타겟 그룹의 레이블되지 않은 데이터를 프롬프트 최적화에 통합하는 Generalized Prompt Optimization (GPO) 프레임워크를 제안한다. 실험 결과, 이러한 프레임워크가 타겟 그룹에서 상당한 성능 향상을 보여주고 소스 그룹에서도 비슷한 성능을 보인다.

###### Exploiting Asymmetry for Synthetic Training Data Generation: SynthIE and the Case of Information Extraction (https://aclanthology.org/2023.emnlp-main.96/)
- Anthology ID: 2023.emnlp-main.96 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large language models, LLMs)은 구조화된 출력 문제에 대해서도 역방향으로 작동하도록 유도하여, 복잡한 작업을 위한 대규모이고 고품질의 데이터를 생성할 수 있다는 것을 보여줍니다.
    2. 이 논문은 정보 추출을 위한 데이터셋 생성의 어려움을 극복하기 위해 LLM을 사용하여 합성 데이터를 생성하는 방법을 설명합니다.
    3. 합성된 데이터는 사람들에 의해 평가되어 기존 데이터셋보다 우수한 품질을 가지며, 다른 작은 모델들을 세밀하게 조정하여 기존 최고 성과와 큰 차이로 이길 수 있음을 보여줍니다.

###### Condensing Multilingual Knowledge with Lightweight Language-Specific Modules (https://aclanthology.org/2023.emnlp-main.97/)
- Anthology ID: 2023.emnlp-main.97 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어별 모듈이나 Mixture-of-Experts (MoE)를 사용하는 것은 멀티링귀스 모델 성능을 향상시키는 입증된 방법이나, 수백 개의 언어나 전문가를 다루는 것은 관리하기 어렵다.
    2. 우리는 이러한 문제를 해결하기 위해 Language-specific Matrix Synthesis (LMS)라는 새로운 방법을 제안한다. 
    3. LMS는 매개변수를 효율적으로 사용하고 가벼운 모듈을 사용하여 기존 방법보다 우수한 성능을 보이며, 멀티링귀지 번역에서 Switch Transformer보다 +1.73 BLEU를 달성한다. 또한, 우리는 Fuse Distillation (FD)를 도입하여 여러 언어별 모듈에서 멀티링귀지 지식을 한 개의 공유 모듈로 압축하여 모델 추론 및 저장 효율성을 향상시킨다.

###### The Framework Tax: Disparities Between Inference Efficiency in NLP Research and Deployment (https://aclanthology.org/2023.emnlp-main.98/)
- Anthology ID: 2023.emnlp-main.98 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 처리 시스템의 계산 효율성에 대한 관심이 증가함에 따라 효율적인 모델 아키텍처와 하드웨어 가속기 개선이 이뤄졌으나, 이로 인해 계산 처리량이 증가하고 부동 소수점 연산이 감소한 결과가 실제로 벽시계 추론 지연 시간에 직접적인 향상으로 이어지지 않는다는 것을 보여준다.
    2. 이 불일치는 딥러닝 프레임워크에 의해 도입된 병목 현상으로 설명될 수 있으며, 하드웨어의 속도가 시간이 흐름에 따라 증가함에 따라 불일치가 더 커지는 것을 관찰할 수 있다.
    3. 이 논문에서는 모델 디자인 결정, 프레임워크 패러다임, 하드웨어 플랫폼이 총 모델 지연 시간에 미치는 영향을 분석하는 일련의 사례 연구를 통해 이 현상을 검토한다. 그리고 이러한 연구 결과를 바탕으로 효율적인 NLP 모델 연구와 실제 적용 사이의 격차를 좁히기 위한 조치 가능한 권고사항을 제공한다.

###### Evaluating Cross-Domain Text-to-SQL Models and Benchmarks (https://aclanthology.org/2023.emnlp-main.99/)
- Anthology ID: 2023.emnlp-main.99 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Text-to-SQL 벤치마크에서 모델이 생성한 SQL 쿼리와 벤치마크의 참조 SQL 쿼리를 정확하게 일치시키는 것은 여러 이유로 실패할 수 있다. 이 논문에서는 여러 프로미넌트한 텍스트-투-SQL 벤치마크를 연구하고, 수동으로 SQL 쿼리를 평가하고 동등한 표현으로 재작성하여 성능을 재평가한다.
    2. 이 연구에서는 벤치마크에서 제공되는 샘플에서 파생될 수 있는 여러 해석 때문에 이 벤치마크에 대한 완벽한 성능 달성은 어렵다는 사실을 발견하였다. 
    3. 가장 놀라운 발견으로 GPT4 기반 모델이 Spider 벤치마크에서 골드 스탠더드 참조 쿼리를 능가했다는 사실을 발견하였다. 이 결과는 벤치마크 평가를 조심스럽게 해석하고 동시에 독립된 추가 평가의 중요성을 인정하는 것의 중요성을 강조한다.

