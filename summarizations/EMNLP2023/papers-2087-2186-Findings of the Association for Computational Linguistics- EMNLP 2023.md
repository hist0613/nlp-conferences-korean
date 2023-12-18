# Korean Three-Line Summarizations of Papers 2087-2186 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Leveraging Contrastive Learning and Knowledge Distillation for Incomplete Modality Rumor Detection (https://aclanthology.org/2023.findings-emnlp.900/)
- Anthology ID: 2023.findings-emnlp.900 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 온라인 소셜 미크로블로그를 통해 루머는 상대적으로 적은 비용으로 빠르게 퍼지며 우리 일상생활에서 상당한 경제적 손실과 부정적인 결과를 초래한다. 
    2. 기존의 루머 탐지 모델은 다중모달 게시물의 텍스트와 이미지 간의 의미적 일관성과 단일 모달 게시물에서 불완전한 모달에 의한 도전과제를 간과하는 경우가 많다.
    3. 이 논문에서는 Incomplete Modality Rumor Detection을 위한 새로운 CLKD-IMRD 프레임워크를 제안한다. CLKD-IMRD는 텍스트와 이미지 간의 의미적 일관성을 파악하는 데 Contrastive Learning과 Knowledge Distillation을 사용하면서 개별 게시물 내의 불완전한 모달에 대한 모델 일반화를 강화한다. 실험 결과, CLKD-IMRD가 소셜 미디어에서의 루머 탐지를 위한 두 개의 영어 및 중국어 벤치마크 데이터셋에서 최첨단 기법보다 우수한 성능을 보였다.

###### Beyond Testers’ Biases: Guiding Model Testing with Knowledge Bases using LLMs (https://aclanthology.org/2023.findings-emnlp.901/)
- Anthology ID: 2023.findings-emnlp.901 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 모델 테스팅 연구는 주로 테스트 케이스를 생성하는 데 초점을 맞추고 있으며, 테스트할 내용을 식별하는 단계는 주로 무시되고 지원도 부족하다.
    2. 우리는 모델 테스팅을 안내하기 위해 요구 사항을 도출하는 데 도움을 주는 인터랙티브 도구인 Weaver를 제안한다.
    3. Weaver는 대화 형식으로 큰 언어 모델을 활용하여 지식 베이스를 생성하고 그 중에서 컨셉을 추천함으로써 테스터가 추가 테스트 요구 사항을 도출할 수 있게 한다.

###### CAR: Conceptualization-Augmented Reasoner for Zero-Shot Commonsense Question Answering (https://aclanthology.org/2023.findings-emnlp.902/)
- Anthology ID: 2023.findings-emnlp.902 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Zero-shot commonsense question answering"을 위한 기존 접근 방식은 CommonSense 지식 베이스에서 합성 QA 쌍으로 모델을 사전 학습시키는 것이지만, 이는 CSKB의 내재적 불완전성으로 인해 semantic coverage를 제한하고, 샘플된 negative examples이 불충분하고 모순되는 경우가 있다는 문제가 있다.
    2. 따라서 CAR라는 zero-shot commonsense question-answering 프레임워크를 제안한다. 이 프레임워크는 CAR이름 때문에 알려져 있다. CAR은 CSKB의 커버리지를 높이고 false negative distractors를 선택할 확률을 줄이기 위해 common sense 지식 쌍을 다양한 고수준 인스턴스로 추상화한다.
    3. 다양한 실험을 통해 CAR은 GPT3.5, ChatGPT 같은 큰 언어 모델을 포함한 기존 방법들보다 zero-shot commonsense 시나리오에 대해 더 강력하게 일반화할 수 있음을 입증하였다.

###### kNN-CM: A Non-parametric Inference-Phase Adaptation of Parametric Text Classifiers (https://aclanthology.org/2023.findings-emnlp.903/)
- Anthology ID: 2023.findings-emnlp.903 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 반모수 모델은 매개변수화 모델과 비매개변수화 모델의 속성을 가지며, 다음 단어 예측 언어 모델링에서 효과적임이 입증되어왔다.
    2. 그러나 이러한 모델의 텍스트 구별 능력에 대한 연구가 부족하다. 우리는 학습된 매개변수 텍스트 분류기의 능력을 향상시키기 위해 간단한 근접 이웃 탐색을 통해 k-최근접 이웃 분류 모델(kNN-CM)이라는 추론 단계 접근 방식을 제안한다.
    3. 실험 결과는 SuperGLUE 과제 8개, ANLI 데이터셋 3개, QA 데이터셋 11개, 그리고 감성 분류 데이터셋 2개에서 일관된 성능 향상을 보여준다.

###### Cross-modality Data Augmentation for End-to-End Sign Language Translation (https://aclanthology.org/2023.findings-emnlp.904/)
- Anthology ID: 2023.findings-emnlp.904 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "End-to-end sign language translation" (SLT)은 중간 표현 없이 수화 동영상을 말로 된 텍스트로 직접 변환하는 것을 목표로 한다. 그러나 레이블된 데이터 부족과 수화 동영상과 텍스트 간의 모달리티 간격으로 인해 어려움이 있었다. 이 문제를 해결하기 위해, 우리는 Cross-modality Data Augmentation (XmDA) 프레임워크를 제안하여 수어 번역 능력을 전달하는 것을 목표로 한다.
    2. XmDA는 크로스 모달리티 믹스업과 크로스 모달리티 지식 증류라는 두 가지 주요 구성 요소로 이루어져 있다. 전자는 수어 동영상 특징과 수어 표현 간의 일치를 증진하여 모달리티 간격을 줄인다. 후자는 수어에서 텍스트로의 번역 지식을 활용하여 말로 된 텍스트 생성을 안내한다.
    3. PHOENIX-2014T 및 CSL-Daily와 같은 두 가지 널리 사용되는 SLT 데이터셋에서의 실험 결과는 XmDA 프레임워크가 베이스라인 모델보다 유의하게 성능이 향상됨을 보여준다. 또한 광범위한 분석 결과는 XmDA가 수화 동영상과 수어 표현 간의 표현 거리를 줄이고, 저빈도 단어 및 긴 문장의 번역을 개선함으로써 엔드 투 엔드 수어 번역을 향상시킨다는 것을 확인한다.

###### Consistency is Key: On Data-Efficient Modality Transfer in Speech Translation (https://aclanthology.org/2023.findings-emnlp.905/)
- Anthology ID: 2023.findings-emnlp.905 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 ST에서는 data scarcity를 극복하기 위해 MT 데이터를 사용하는 progressive training이 흔한 연구 사례가 되었으나, 실제로 효과가 없다는 것을 실험 결과로 확인하였다.
    2. 우리는 학습-잊어버림 trade-off를 critical obstacle로 확인하고, consistency learning (CL)이 이 trade-off를 극복할 수 있다는 가설을 세웠고 검증하였다.
    3. 우리의 CL과 knowledge distillation (KD)을 결합한 방법은 추가 데이터 없이도 이전 연구 방법들보다 MuST-C dataset에서 우수한 성능을 보여주며, consistency-informed KD가 KD+CL보다 더 나은 결과를 달성했다.

###### Relation-Aware Question Answering for Heterogeneous Knowledge Graphs (https://aclanthology.org/2023.findings-emnlp.906/)
- Anthology ID: 2023.findings-emnlp.906 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 멀티합 특정 지식 베이스 질문 응답(KBQA)은 다중 단계 추론이 필요한 지식 그래프(KG)에서 답변 entity를 찾는 것을 목표로 한다. 기존의 검색 기반 접근 방식은 각 단계별로 특정 관계에 집중하고 추론 경로 내의 중간 entity를 예측하여 이 작업을 해결한다. 그러나 이러한 모델들은 head-tail entity의 정보와 관계 사이의 의미적 연결을 활용하여 현재 관계 표현을 강화하는 것을 실패하며, 이는 지식 그래프 내의 관계 정보를 제대로 캡처하지 못하게 한다.
    
    2. 이 문제를 해결하기 위해, 우리는 두개의 관계 그래프가 있는 이중 관계 그래프를 구성한다. 각 노드는 원래 KG의 관계를 나타내고, 동일한 head 또는 tail entities를 공유하는 관계 사이에 에지를 생성한다. 그런 다음, 우리는 원래 entity 그래프 추론, 이중 관계 그래프 정보 전파 및 이 두 그래프 사이의 상호 작용을 반복적으로 수행한다. 이렇게 하면 entity와 관계 간의 상호 작용이 강화되고, 더 좋은 entity와 관계 표현을 얻게 된다.
    
    3. WebQSP와 CWQ라는 두 개의 공개 데이터셋을 대상으로 한 실험 결과, 우리의 접근 방식이 이전 최상위 수준보다 상당한 성능 향상을 이뤘다.

###### InstOptima: Evolutionary Multi-objective Instruction Optimization via Large Language Model-based Instruction Operators (https://aclanthology.org/2023.findings-emnlp.907/)
- Anthology ID: 2023.findings-emnlp.907 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델에서는 instruction 기반 언어 모델링이 주목받고 있다. 하지만 instruction engineering의 효율성은 여전히 낮으며 instruction의 품질에 영향을 미치는 길이나 complexity와 같은 중요한 목표를 고려하지 못하고 있다.
    2. 본 논문에서는 instruction 생성을 다목적 최적화 문제로 취급하고, instruction 연산자(돌연변이, 교배 등)들을 모사하는 대형 언어 모델(LLM)을 활용하는 새로운 접근 방법을 제안한다.
    3. 실험 결과는 세부 조정 성능의 향상과 다양한 고품질 instruction 셋의 생성을 보여준다.

###### Less than One-shot: Named Entity Recognition via Extremely Weak Supervision (https://aclanthology.org/2023.findings-emnlp.908/)
- Anthology ID: 2023.findings-emnlp.908 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 극도로 약한 지도 하에서 XWS(X-NER) 방식의 명명체 인식 문제를 연구한 결과, 단 한개의 예제 개체가 컨텍스트-프리 방식으로 주어지는 상황에서도 X-NER 방법이 최신 1-shot NER 방법보다 우수한 성능을 보이는 것을 알 수 있었다.
    2. 우리는 우선 미탐지 훈련 데이터로부터 예제 개체와 유사한 entity span들을 추출하였고, entity span을 대체하기 전과 후의 컨텍스트 분포를 비교하는 것이 좋은 성능을 보였다.
    3. X-NER은 1-shot 지도와 ChatGPT 어노테이션 보다 우수한 성능을 보이며, 다국어 능력을 향후 연구에 상속시켜 갖고 있다는 장점을 가지고 있다.

###### Focus on the Core: Efficient Attention via Pruned Token Compression for Document Classification (https://aclanthology.org/2023.findings-emnlp.909/)
- Anthology ID: 2023.findings-emnlp.909 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP 태스크에서 트랜스포머 기반 모델들은 우수한 성능을 보여주지만, BERT와 같은 사전 훈련된 모델은 계산 비용이 많이 드는 자기 어텐션 메커니즘을 갖고 있어서, 분류 성능에 부정적인 영향을 미치는 토큰을 포함하여 모든 토큰과 상호 작용한다.
    2. 이 논문에서는 두 가지 전략, 토큰 가지치기와 토큰 결합, 을 통합하여 이러한 문제를 해결하는 방법을 제안한다.
    3. 이 두 가지 접근 방식을 통합함으로써, 모델의 성능을 향상시키고 계산 요구 사항을 줄일 수 있다. 다양한 데이터셋과의 실험에서 기존 모델과 비교하여 우수한 성능을 보여주며, 메모리 비용을 0.61배로 줄이고 1.64배 가속화된다.

###### Semantic Decomposition of Question and SQL for Text-to-SQL Parsing (https://aclanthology.org/2023.findings-emnlp.910/)
- Anthology ID: 2023.findings-emnlp.910 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Text-to-SQL의 semantic parsing은 cross-domain과 complex한 쿼리에 일반화하는 데 어려움을 겪고 있다. 이 논문에서는 Question Decomposition 전략을 사용하여 복잡한 SQL 쿼리의 파싱을 향상시키는 방법을 제안한다.
    2. QPL(Query Plan Language)은 모듈식으로 SQL 쿼리를 분해하여 간단하고 정규적인 서브 쿼리로 분할하는 새로운 방법을 제안한다. QPL은 기존의 semantic-parsing 아키텍처에 이점을 제공하며, 기존의 semantic-parsing보다 semantically equivalent한 쿼리에 대해서 QPL을 사용하여 학습하는 것이 더 효과적이다.
    3. QPL은 database schema에 민감한 data retrieval을 위한 Question Decomposer를 만드는 데 도움이 되며, 복잡한 쿼리에 대해서 비전문가도 쉽게 접근할 수 있어 semantic parser의 해석 가능한 출력을 도출할 수 있다.

###### Time-Aware Language Modeling for Historical Text Dating (https://aclanthology.org/2023.findings-emnlp.911/)
- Anthology ID: 2023.findings-emnlp.911 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 텍스트 데이터화는 텍스트에 명시적인 시간적 언급이 일반적으로 나타나지 않기 때문에 어려운 작업이다. 
    2. 기존의 최첨단 접근법은 언어 모델을 통해 단어 표현을 학습하지만, 대부분의 접근법은 단어의 시간 변화를 무시하고 텍스트 모델링의 노력에 영향을 미칠 수 있다.
    3. 이 논문에서는 TALM이라는 시간감각 언어 모델을 제안하여, 특정 시기에 맞는 언어 모델을 일반 도메인 언어 모델에서 전이학습하여 시간적 단어 표현을 학습한다. 이러한 방법은 시간 경과에 따른 문서 표현을 위해 계층적 모델링 접근법을 구축한다. 실험 결과는 우리의 모델이 단어의 암묵적인 시간적 정보를 효과적으로 포착하며, 역사적 텍스트 데이터화 작업에서 최첨단 접근법을 능가한다는 것을 보여준다.

###### A Read-and-Select Framework for Zero-shot Entity Linking (https://aclanthology.org/2023.findings-emnlp.912/)
- Anthology ID: 2023.findings-emnlp.912 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Zero-shot entity linking (EL)"는 보편화 능력을 도전하기 위해 보이지 않는 엔티티에 엔티티 멘션을 정렬하는 것을 목표로 한다. 
    2. 기존 방법들은 후보 추출 단계에 주로 초점을 맞추고, 후보 순위 결정 단계를 무시한다. 반면 이 논문에서는 "read-and-select (ReS)" 프레임워크를 제안하여 후보 선정 문제를 순차적 라벨링 문제로 설명하고, 모든 후보 표현을 통합하여 엔티티 간 비교를 가능하게 한다.
    3. 이 방법은 대부분의 이전 연구에 사용된 노동 집약적 다상(pre-training) 없이도 "ZESHEL" 데이터셋에서 최고 성능을 달성하며, 멘션-엔티티 상호작용과 엔티티 간 상호작용의 효과를 보여준다.

###### Multi-Task Learning of Query Generation and Classification for Generative Conversational Question Rewriting (https://aclanthology.org/2023.findings-emnlp.913/)
- Anthology ID: 2023.findings-emnlp.913 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 검색 환경에서 질문을하고 대화의 일부로 답변을 받는 상황에서 질문의 모호성은 주요한 도전 과제이며, 대화 기록에서 문맥 정보를 활용하여 효과적으로 다룰 수 있다. 
    2. 기존 접근 방식들은 주제의 연속성을 분류 작업으로 다루거나, 재구성된 질문을 생성하는 텍스트 생성 작업으로 다루고 있다. 하지만 이 논문에서는 두 작업을 모두 포함하여 대화 중 모호한 질문을 효과적으로 식별하는 Multi-Task Learning (MTL) 접근 방식을 제안하고 있다. 
    3. BART와 T5를 기반으로 한 모델을 사용하여 대화식 질문 재작성과 추론 질문 식별 작업을 동시에 수행하는 모델을 학습하였으며, 다양한 테스트 세트에서 평가하여 단일 작업 학습 기준을 능가하는 결과를 보였다.

###### DepNeCTI: Dependency-based Nested Compound Type Identification for Sanskrit (https://aclanthology.org/2023.findings-emnlp.914/)
- Anthology ID: 2023.findings-emnlp.914 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 구성 복합어는 산스크리트어에서 흔한 현상이며, 복합어의 구성 요소의 내재적 구조를 이해하는 것은 의미를 해독하는 데 중요하다. 본 논문에서는 다중 구성 복합어 유형 식별 문제를 제안하고, 이를 위해 새로운 주석이 달린 데이터셋과 DepNeCTI라는 새로운 프레임워크를 제안한다.
    2. 기존 기법들은 이진 복합어에 초점을 맞추고 다중 구성 복합어를 무시해왔지만, 본 논문에서는 다중 구성 복합어의 내재적 의미 관계를 해석하기 위해 이와 같은 문제를 처음으로 제안한다.
    3. 실험 결과, DepNeCTI는 기존 기준선 기법과 비교하여 라벨링된 구간 점수(LSS)에서 평균 절댓값 13.1점의 F1-score 향상과 추론 효율성의 5배 향상을 달성한다.

###### HeQ: a Large and Diverse Hebrew Reading Comprehension Benchmark (https://aclanthology.org/2023.findings-emnlp.915/)
- Anthology ID: 2023.findings-emnlp.915 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 히브리어 자연어 처리 (NLP)에 대한 벤치마크는 주로 형태-문법적인 작업에 초점을 맞추고, 언어 이해의 의미적인 차원을 무시하고 있다.
    2. 우리는 이 간극을 좁히기 위해 히브리어 기계 독해 (MRC) 데이터셋을 제공하기로 결정했다. 
    3. 우리는 새로운 가이드라인, 통제된 크라우드소싱 프로토콜 및 수정된 평가 메트릭을 개발하여 히브리어 특유의 풍부한 형태학적 특성에 적합하도록 한다.

###### HANSEN: Human and AI Spoken Text Benchmark for Authorship Analysis (https://aclanthology.org/2023.findings-emnlp.916/)
- Anthology ID: 2023.findings-emnlp.916 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 작문 분석(Stylometry)은 자연어처리(NLP)에서 오랫동안 중요한 요소로 다뤄져 왔으나 최근 대형 언어 모델(LLMs)의 발전에 따라 작문 분석은 사람이 쓴 텍스트와 AI가 생성한 텍스트를 구분하는 데 더욱 중요해졌다.
    2. 그러나 이 작문 분석 작업은 주로 작성된 텍스트에 초점을 맞추어 왔고, 구어 텍스트는 고려하지 않았다. 
    3. 따라서 우리는 구어 텍스트를 위한 가장 큰 벤치마크인 HANSEN(Human And ai Spoken tExt beNchmark)를 소개하며 인식된 인간 데이터셋과 AI생성 구어 텍스트 데이터셋을 활용하여 Authorship Attribution (AA) 및 Author Verification (AV)를 수행하고 최첨단 모델을 사용하여 인간 대 AI 텍스트 감지 작업을 수행한다.

###### Data Augmentation for Code Translation with Comparable Corpora and Multiple References (https://aclanthology.org/2023.findings-emnlp.917/)
- Anthology ID: 2023.findings-emnlp.917 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 프로그래밍 언어 간의 코드 번역은 병렬 훈련 데이터가 부족한 문제 때문에 주요한 어려움을 가지고 있다. 본 논문에서는 기능이 유사한 코드 쌍을 갖는 비교 가능한 문서나 기존의 병렬 데이터에 다중 참조 번역을 추가하는 데이터 증강 기법 두 가지를 제안한다. 
    2. 자연어 문서에서 코드 생성 모델을 사용하여 생성된 프로그램을 포함한 여러 유형의 비교 가능한 문서를 분석한다. 게다가, 다중 참조 번역을 자동으로 생성하고 유닛 테스트로 번역을 필터링하여 단일 참조 번역에 대한 과적합을 줄인다. 이렇게 함으로써 목표 번역에 다양성을 추가할 수 있다. 
    3. 실험 결과, 우리의 데이터 증강 기법은 Java, Python 및 C++ 간의 번역에서 CodeT5의 계산 정확도 (CA@1)를 평균 7.5% 향상시킨다. 이는 실행을 통해 번역의 정확성을 확인하는 것이다.

###### Multilingual Generation and Answering of Questions from Texts and Knowledge Graphs (https://aclanthology.org/2023.findings-emnlp.918/)
- Anthology ID: 2023.findings-emnlp.918 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. QG와 QA를 다양한 NLP 응용 분야에 도움이 되는 다중 모달리티(KG와 NL)를 가진 자동 평가를 위한 QA 기반 방법들을 연결할 수 있는 능력이 있다.
    2. 이 논문에서는 QG-QA에 대한 멀티링귤러(Multilingual)와 멀티모달 (Multimodal) (KG와 NL) 기능을 초록어와 러시아어로 확장시켰다.
    3. 이 연구에서는 그래프와 텍스트 간에 맞춤된 QG-QA 데이터를 만들기 위해 합성 데이터 생성과 기계 번역을 활용하여 멀티모달, 멀티태스크 모델을 훈련시켜 멀티모달 QG와 QA를 포르투갈어와 러시아어로 수행할 수 있음을 보였다.

###### InfoDiffusion: Information Entropy Aware Diffusion Process for Non-Autoregressive Text Generation (https://aclanthology.org/2023.findings-emnlp.919/)
- Anthology ID: 2023.findings-emnlp.919 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 생성 모델에서 "쉬운 것부터" 생성하는 기존 방식과 인간의 "키워드부터" 생성하는 방식 사이에는 큰 차이가 있는데, 이 논문에서는 이 차이를 줄이기 위해 자동회귀적이지 않은 InfoDiffusion 모델을 제안한다. 
    2. 제안한 모델은 "키워드-정보부터" 생성 전략을 도입하고 텍스트 정보량을 기반으로한 잡음 스케줄을 사용한다.
    3. 실험 결과, InfoDiffusion은 텍스트 생성 품질과 다양성에서 기준 모델을 능가하며 샘플링 효율성이 더 높음을 보여준다.

###### Enhancing Scalability of Pre-trained Language Models via Efficient Parameter Sharing (https://aclanthology.org/2023.findings-emnlp.920/)
- Anthology ID: 2023.findings-emnlp.920 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 사전 훈련된 언어 모델(PLMs)의 깊이를 확장하기 위한 매우 parameter-efficient한 방법을 제안한다. 
    2. 다른 이전의 연구들은 모든 parameter를 공유하거나 추가 블록을 사용하는 반면, 이 연구에서는 효율적인 텐서 분해 방법인 MPO를 기반으로 더 강력한 parameter-sharing 아키텍처를 설계한다. 
    3. 실험 결과, 우리가 제안한 모델은 확장성을 개선하고 더 적은 parameter로 BERT-large와 비슷한 성능을 달성하는 것을 보여주었다.

###### Boosting Prompt-Based Self-Training With Mapping-Free Automatic Verbalizer for Multi-Class Classification (https://aclanthology.org/2023.findings-emnlp.921/)
- Anthology ID: 2023.findings-emnlp.921 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 prompt-based fine-tuning은 몇 개의 예시만 가지고도 텍스트 분류 작업을 수행할 수 있는 중요한 기술로 주목받고 있으나, 다중 클래스 분류에 대한 prompt-based self-training 연구가 충분히 이루어지지 않았다.
    2. 이 연구에서는 Mapping-free Automatic Verbalizer (MAV)라는 효율적인 Verbalizer 구조를 소개하고, MLM 예측에서 모든 정보를 활용하여 자동으로 필요한 단어 특징을 추출하여 분류하는 기능을 한다.
    3. 다섯 개의 다중 클래스 분류 데이터셋에 대한 실험결과 MAV의 superior self-training 효과가 입증되었다.

###### On the Impact of Cross-Domain Data on German Language Models (https://aclanthology.org/2023.findings-emnlp.922/)
- Anthology ID: 2023.findings-emnlp.922 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 대형 언어 모델은 일반적인 웹 데이터나 특정 도메인 데이터에서 훈련되었으나, 최근 대규모 언어 모델의 성공은 도메인 간 데이터 다양성의 이점을 보여준다.
    2. 우리는 5개 도메인의 텍스트를 포함하는 독일어 데이터셋과 고품질 데이터를 포함하는 다른 데이터셋을 제시하고, 두 데이터셋에서 122M에서 750M 파라미터까지의 모델을 훈련함으로써 다양한 후속 작업에 대한 포괄적인 벤치마크를 수행한다.
    3. 우리의 결과는 도메인 간 데이터셋에서 훈련된 모델이 단독으로 훈련된 고품질 데이터보다 우수한 성능을 보이며, 이로 인해 이전 최고 성능 대비 최대 4.45%의 성능 향상을 나타낸다.

###### Dialect-to-Standard Normalization: A Large-Scale Multilingual Evaluation (https://aclanthology.org/2023.findings-emnlp.923/)
- Anthology ID: 2023.findings-emnlp.923 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 정규화 방법은 주로 역사적 언어나 사용자 생성 콘텐츠에 적용되었지만, 방언적 표기에는 덜 사용되었다. 이 논문에서는 방언에서 표준어로의 정규화를 독립된 문장 수준의 문자 변환 문제로 소개하고, 방언에서 표준어로의 정규화 방법에 대한 대규모 분석을 제공한다.
    2. 네 가지 언어 (핀란드어, 노르웨이어, 스위스 독일어, 슬로베니아어)를 커버하는 다국어 데이터셋을 구축하고, 자동 정규화에 대한 다양한 use case에 해당하는 세 가지 다른 데이터 분할을 제공한다.
    3. 토큰화 접근 방식과 문맥 크기에 따라 텍스트 정규화 작업에 제안된 가장 성공적인 시퀀스-투-시퀀스 모델 아키텍처를 평가하고, 핀란드어, 스위스 독일어, 슬로베니아어의 경우 3개 단어의 슬라이딩 윈도우로 훈련된 문자 수준 Transformer가 가장 잘 작동한다는 것을 발견했다.

###### Re-Examining Summarization Evaluation across Multiple Quality Criteria (https://aclanthology.org/2023.findings-emnlp.924/)
- Anthology ID: 2023.findings-emnlp.924 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 평가 메트릭의 평가는 zuverlässige 인간 평가에서 얻은 시스템 순위와의 상관관계를 측정하여 더 높은 상관관계가 더 좋은 평가 메트릭을 의미한다.
    2. 그러나 여러 Quality Criteria (QCs)가 있는 NLP 태스크의 경우 이 방법론의 타당성에 관한 의문을 제기한다.
    3. 결론적으로 여러 QCs가 있는 경우에는 metric 평가 방법론을 더 조사해야 함을 강조한다.

###### A Parallel Corpus for Vietnamese Central-Northern Dialect Text Transfer (https://aclanthology.org/2023.findings-emnlp.925/)
- Anthology ID: 2023.findings-emnlp.925 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 베트남어는 3개의 주요 지역, 북부, 중부 및 남부에 밀접하게 결합된 방언 변형을 포함하고 있습니다. 현재 NLP 모델은 베트남어 중앙 방언 텍스트를 이해하지 못하는 것으로 관측되었으며, 이는 리소스의 부족으로 인한 것입니다.
    2. 베트남어 중앙북 방언 텍스트 전송 작업에서 단일 언어 모델이 다중 언어 모델보다 우위를 보이는 것을 발견했습니다.
    3. 풍부한 번역 및 텍스트-이미지 검색 작업 결과를 통해 세부적으로 베트남어 중앙 방언 도메인에서 기존 NLP 시스템의 성능을 향상시킬 수 있는 것을 보였습니다.

###### A Comprehensive Evaluation of Tool-Assisted Generation Strategies (https://aclanthology.org/2023.findings-emnlp.926/)
- Anthology ID: 2023.findings-emnlp.926 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구는 언어 모델에 툴 (예: 검색 엔진, 계산기)을 추가하여 누락된 지식이나 잘못된 논리적 추론과 같은 단점을 극복하는 방법을 조사하고 있다. 
    2. 이 논문에서는 다양한 few-shot tool-usage 전략들을 체계적으로 비교하고, 툴을 활용하지 않는 강력한 베이스라인과의 비교를 수행한다. 
    3. 연구 결과, 툴을 효과적으로 사용하는 것은 여전히 어려운 문제이며, 지식 검색 작업에서는 잘못된 출력을 툴을 사용하여 수정하는 전략이 성능 면에서 더 우수하다는 것을 보여준다. 그러나 툴을 사용한 전략은 토큰 수에 비례하여 많은 비용이 들지만 성능 향상에는 큰 기여를 하지 않는다고 다는 것을 발견하였다.

###### InheritSumm: A General, Versatile and Compact Summarizer by Distilling from GPT (https://aclanthology.org/2023.findings-emnlp.927/)
- Anthology ID: 2023.findings-emnlp.927 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. GPT-3와 같은 큰 모델들은 zero-shot 및 few-shot 요약 작업에서 뛰어난 성능을 보이지만, 그들의 많은 서빙 및 fine-tuning 비용은 다양한 응용 분야에서의 활용을 어렵게 한다.
    2. 그러나 이전 연구에서는 자동 메트릭은 작은 fine-tuned 모델들을 선호하지만, 인간 평가자들에 따르면 그들이 생성하는 요약의 품질은 GPT-3와 같은 큰 모델들보다 열악하다고 발견되었다.
    3. 이 문제를 해결하기 위해 우리는 GPT-3.5에서 축소(distillation)를 통해 도출된 다재다능하고 간결한 요약 모델인 InheritSumm을 제안한다. InheritSumm은 GPT-3.5와 비교할만한 zero-shot 및 few-shot 요약 능력을 가지며 fine-tuning 목적으로 충분히 간결하다. 실험 결과 InheritSumm은 zero-shot 및 few-shot 설정에서 GPT-3.5와 유사하거나 우수한 성능을 보여준다. 또한, prefix-tuning 및 전체 데이터 fine-tuning 시나리오에서 이전에 확립된 최상의 작은 모델들보다 우수한 성능을 발휘한다.

###### Learning to love diligent trolls: Accounting for rater effects in the dialogue safety task (https://aclanthology.org/2023.findings-emnlp.928/)
- Anthology ID: 2023.findings-emnlp.928 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 챗봇은 모욕적인 발언을 생성할 위험이 있으며, 이를 피해야 한다. 이 논문은 사용자의 피드백으로부터 얻은 대화/레이블 쌍을 이용하여 챗봇을 지속적으로 개선하는 방법을 제안한다. 
    2. 이전 연구들에서는 고객 간 교차 검증 에러를 기준으로 오인된 훈련 데이터를 제거해왔으나, 이는 비용이 많이 든다. 본 연구에서는 여러 사용자가 각 발언을 평가하고 이를 통해 올바른 레이블을 추론하기 위해 잠재적 클래스 분석(LCA)을 사용하는 AES와 비슷한 해결책을 제안한다.
    3. 실험 결과, 적대적인 사용자들 사이에서 일관성이 있을 때 AES와 비슷한 해결책은 높은 정확도로 훈련 레이블을 추론할 수 있다는 것을 보였다.

###### Can ChatGPT Perform Reasoning Using the IRAC Method in Analyzing Legal Scenarios Like a Lawyer? (https://aclanthology.org/2023.findings-emnlp.929/)
- Anthology ID: 2023.findings-emnlp.929 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 ChatGPT와 같은 대형 언어 모델들이 다양한 법률 작업을 수행할 수 있는 능력으로 인해 법률 분야에서 많은 관심을 받고 있다. 그러나 여전히 LLMs가 변호사들과 동일한 방식으로 법률 케이스를 분석하고 추론할 수 있는지는 알려져 있지 않다. 
    2. 이 연구에서는 법률 전문가들이 법률 분석을 위해 널리 사용하는 IRAC 방법론을 활용하여 ChatGPT를 적용하여 케이스 분석을 수행하기 위한 독특한 말뭉치를 구축하였다. 
    3. 실험 결과는 LLMs와 법률 전문가들의 분석 간의 일치를 개선하기 위한 가능한 미래 연구 방향을 알려주고 있다.

###### Coverage-based Example Selection for In-Context Learning (https://aclanthology.org/2023.findings-emnlp.930/)
- Anthology ID: 2023.findings-emnlp.930 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "In-context learning (ICL)은 큰 언어 모델이 몇 가지 태스크 예제로 조건부로 작업을 수행하는 능력인데, 이때 예제들은 테스트 인스턴스에 대해 정보를 제공해야한다."
    2. 기존 방식은 각각 독립적으로 순위를 매기고 가장 유사한 예제를 선택하는데, 이 방식은 중복되는 예제들을 선택하면서 중요한 정보를 빠뜨리는 문제가 있다.
    3. 이 논문에서는 BERTScore-Recall (BSR)이 테스트 입력의 중요한 측면인 추론 패턴 등을 더 잘 보여주는 더 좋은 예제를 선택한다는 것을 보였으며, Set-BSR을 사용하여 셋 수준에서 최적화 가능한 메트릭을 확장시켜 새로운 방식의 선택 방법을 제안한다.

###### Are Structural Concepts Universal in Transformer Language Models? Towards Interpretable Cross-Lingual Generalization (https://aclanthology.org/2023.findings-emnlp.931/)
- Anthology ID: 2023.findings-emnlp.931 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(LLM)은 다양한 언어 간의 암묵적인 지식 전달을 통해 상당한 교차 언어 일반화 능력을 보여주었지만, 저자원 언어에 대해서는 특히 도전적인 문제가 있습니다. 
    2. 본 논문에서는 언어 간 개념적 관련성을 명시적으로 정렬하여 교차 언어 일반화를 향상시키는 가능성을 조사합니다. 
    3. 실험 결과, 우리의 방법은 최첨단 방법과 경쟁력 있는 결과를 보여주며, 특히 자원이 제한된 언어에 큰 이점을 제공합니다.

###### Thorny Roses: Investigating the Dual Use Dilemma in Natural Language Processing (https://aclanthology.org/2023.findings-emnlp.932/)
- Anthology ID: 2023.findings-emnlp.932 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대용도 언어 모델(LLM)들이 점점 발전하고 접근성이 높아지면서, 그들의 의도적 오용 위험이 더욱 두드러지는 자연어 처리(NLP)에서의 이중 사용은 불명확한 문제이다. 
    2. 이 논문에서는 NLP 연구자와 실무자들의 의견을 반영하여 이중 사용에 대한 NLP 특정 정의를 제시한다. 
    3. 더 나아가, NLP에서 이중 사용에 초점을 맞춘 체크리스트를 제안하며, 이는 기존의 학회 윤리 프레임워크에 통합할 수 있다.

###### BYOC: Personalized Few-Shot Classification with Co-Authored Class Descriptions (https://aclanthology.org/2023.findings-emnlp.933/)
- Anthology ID: 2023.findings-emnlp.933 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 분류는 다양한 NLP 응용 분야를 위한 잘 연구된 기술이다. 그러나 기존 방법들은 모델을 학습시키기 위해 큰 어노테이션된 말뭉치를 필요로 하거나, 큰 언어 모델을 사용할 때는 prompt를 조심스럽게 작성하고 많은 예제를 수용할 수 있는 긴 문맥이 필요하다.
    2. 우리는 이 문제를 해결하기 위해 LLM을 사용하여 페워샷(few-shot) 텍스트 분류에 새로운 접근 방법을 제안한다. LLM은 페워샷 예제 대신 각 클래스의 중요한 특징을 설명하는 프롬프트를 받는다. 이후 사용자와 LLM은 상호작용하면서 프롬프트를 작성한다.
    3. 실험 결과 우리의 접근 방법은 큰 데이터셋으로 학습한 모델의 성능 기준 79%를 달성하면서, 학습 데이터셋의 1%만을 사용하여 높은 정확도의 분류기를 얻을 수 있음을 보여주고, 30명의 참가자와 진행한 연구에 따르면 엔드 유저들은 특정한 요구에 맞는 분류기를 만들 수 있다는 것을 보여주었다.

###### Approximating CKY with Transformers (https://aclanthology.org/2023.findings-emnlp.934/)
- Anthology ID: 2023.findings-emnlp.934 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 transformer 모델이 CKY 알고리즘을 근사화하는 능력을 조사하고, 이를 통해 CKY 알고리즘의 문장 길이에 대한 세제곱 의존성을 피하는 방법을 제안한다.
    2. 일반적인 구문 구문 분석 벤치마크에서, 이 접근 방식은 CKY를 사용하는 유사한 파서보다 경쟁력있는 성능 또는 더 뛰어난 성능을 달성하는 동시에 속도도 빠르다.
    3. 또한, 무작위 PCFG(확률적 구문 구조) 하에서의 파싱 가능성을 평가한 결과, 문법이 더 모호해질수록 성능이 저하되는 것을 발견하였고, 추가적인 귀납적 편향을 포함하는 것이 도움이 된다는 것을 확인하였다.

###### DialGuide: Aligning Dialogue Model Behavior with Developer Guidelines (https://aclanthology.org/2023.findings-emnlp.935/)
- Anthology ID: 2023.findings-emnlp.935 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 모델은 일관되고 유창한 응답을 생성할 수 있지만, 제어하기 어렵고 매력이 없는, 안전하지 않은 결과물을 생성할 수도 있다. 이러한 예측할 수 없는 특성은 사용자의 신뢰를 약화시키고 모델의 실세계에서의 사용을 어렵게 할 수 있다. 
    2. 이를 해결하기 위해, 우리는 DialGuide라는 새로운 프레임워크를 소개한다. DialGuide는 자연어 규칙 또는 가이드라인을 사용하여 대화 모델의 행동을 제어할 수 있다. 
    3. 우리는 DialGuide를 오픈 도메인 대화 응답 생성의 세 가지 작업에 대해평가하였다. 우리의 데이터셋은 두 도메인 (잡담과 안전)에서 10,737개의 양성 및 15,467개의 음성 대화 문맥-응답-지침 세트를 포함하고 있다.

###### RWKV: Reinventing RNNs for the Transformer Era (https://aclanthology.org/2023.findings-emnlp.936/)
- Anthology ID: 2023.findings-emnlp.936 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 트랜스포머는 NLP 태스크에서 차세대 기술로 평가받지만, 시퀀스 길이에 대해 제곱에 비례하는 메모리와 연산 복잡성을 가지고 있다.
    2. 이와는 달리 재귀 신경망(RNN)은 선형 스케일링을 갖고 있지만, 병렬화와 확장성 등의 한계로 트랜스포머와 비교하여 성능을 내기 어렵다.
    3. 따라서 저자들은 효율적인 트레이닝 기법과 결합한 새로운 모델 아키텍처인 Receptance Weighted Key Value (RWKV)를 제안하고, 이를 통해 트랜스포머나 RNN 중 어느 방식으로 모델을 적용할지 선택할 수 있도록 하여 트레이닝은 병렬화하고 추론은 일정한 계산 및 메모리 복잡성을 유지할 수 있다는 것을 보여주었다.

###### Who Wrote it and Why? Prompting Large-Language Models for Authorship Verification (https://aclanthology.org/2023.findings-emnlp.937/)
- Anthology ID: 2023.findings-emnlp.937 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 저자 검증(AV)은 법의학 분석, 표절 탐지, 속임수 있는 콘텐츠 식별 등에서 활용되는 자연어 처리(NLP)와 계산 언어학의 기본 작업이다. 기존 AV 기술은 데이터 요구 사항과 설명 가능성의 한계를 갖고 있다.
    2. 이 논문에서는 PromptAV라는 새로운 기술을 제안하여 대규모 언어 모델을 활용하여 AV를 수행한다. PromptAV는 단계별 기술적 설명 프롬프트를 제공하여 사람들이 해석하기 쉬운 설명을 통해 성능을 크게 향상시킨다.
    3. PromptAV는 최첨단 기준선에 비해 우수한 성능을 발휘하며, 제한된 학습 데이터로도 효과적으로 작동하고 해석 가능성을 향상시킴으로써 AV 작업에 효과적이고 해석 가능한 솔루션으로의 잠재력을 보여준다.

###### Transitioning Representations between Languages for Cross-lingual Event Detection via Langevin Dynamics (https://aclanthology.org/2023.findings-emnlp.938/)
- Anthology ID: 2023.findings-emnlp.938 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전 연구는 representation matching 기법에 초점을 맞춰 고-저 자원 언어 간의 cross-lingual transfer learning (CLTL)을 가능하게 해왔다. 그러나 representation을 변경하게 되므로, 실제 예측을 위해 source-language의 교육 데이터로부터 학습한 ED에 대한 구분력 있는 특징들을 상실할 수 있다.
    2. 우리는 Langevin Dynamics와 semantic preservation 프레임워크를 소개하여 cross-lingual ED에 대한 새로운 접근법을 제시한다. 이를 통해 target-language 예제의 representation만 source-language의 공간으로 전환하여 source language의 표현과 구분력 있는 정보를 보존할 수 있다.
    3. 세 가지 언어에 대한 실험 결과, 우리의 방법은 CLTL에서 ED에 대한 최고 수준의 성능을 보여준다.

###### VISIT: Visualizing and Interpreting the Semantic Information Flow of Transformers (https://aclanthology.org/2023.findings-emnlp.939/)
- Anthology ID: 2023.findings-emnlp.939 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 인터프리터빌리티(해석가능성)의 진보들은 transformer 기반 언어 모델의 가중치와 hidden states를 vocabulary로 변환하여 인간이 해석하기 더 쉽도록 할 수 있다는 것을 제안한다. 
    2. 본 논문에서는 LM attention heads와 memory values를 분석하여 어텐션 메커니즘 내의 정보 흐름 패턴을 파악한다.
    3. 우리의 시각화 도구는 GPT의 forward pass를 인터랙티브한 플로우 그래프로 시각화하여 모델 내부 작업을 간단히 파악할 수 있게 한다.

###### Is Robustness Transferable across Languages in Multilingual Neural Machine Translation? (https://aclanthology.org/2023.findings-emnlp.940/)
- Anthology ID: 2023.findings-emnlp.940 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신뢰성 있는 NLP 시스템 개발을 위해, 모델의 robustness는 성능을 지속하는 능력이 강조되고 있다. 특히 기계 번역에서는, 최근의 연구들이 adversarial training과 data augmentation을 통해 모델의 robustness를 개선하는데 성공하였으나, 이러한 연구들은 단일 번역 방향에 대한 이중 언어 기계 번역에 중점을 두고 있다.
    2. 본 논문에서는 다국어 신경 기계 번역에서 다양한 언어들 간의 robustness 전이 가능성을 조사한다. 특히, 다국어 신경 기계 번역 모델의 특정 번역 방향을 character, word, multi-level noises로 공격하여 다른 번역 방향의 robustness를 평가한다.
    3. 연구 결과, 한 번역 방향에서 얻은 robustness가 다른 번역 방향으로 전이될 수 있음을 실험적으로 확인하였으며, 특히 character-level noise와 word-level noise에 대한 robustness 전이가 더 가능한 경우를 확인하였다.

###### Arabic Mini-ClimateGPT : A Climate Change and Sustainability Tailored Arabic LLM (https://aclanthology.org/2023.findings-emnlp.941/)
- Anthology ID: 2023.findings-emnlp.941 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기후 변화는 사회적으로 맞닥뜨리는 가장 중요한 도전 중 하나이다. 이 논문에서는 기후변화와 지속가능성에 대한 500,000개 이상의 지시문을 보유한 아랍어 데이터셋으로 특별히 조정된 경량 아랍어 Mini-ClimateGPT 모델을 제안한다.
    2. 이 모델은 대화형 스타일의 지시조정(curated instruction tuning)에 특히 초점을 맞춘 오픈소스 LLM(대용량 언어 모델)을 기반으로 구축되었다. ChatGPT 기반 평가에서 기준 모델을 88.3%의 경우에서 능가했으며, 인간 전문가 평가에서는 81.6%의 선호도를 얻었다.
    3. 이를테면, 이 논문에서 제안된 기타 오픈소스 모델보다 우리 모델의 응답을 더 선호하는 사람들이 81.6%를 차지한다.

###### Interpreting Answers to Yes-No Questions in User-Generated Content (https://aclanthology.org/2023.findings-emnlp.942/)
- Anthology ID: 2023.findings-emnlp.942 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어에서 예/아니오 질문에 대한 답변을 해석하는 것은 어렵다. 예와 아니오 키워드는 흔하지 않고, 이러한 키워드를 포함한 답변들도 키워드가 제안하는 바와는 다르게 해석되는 경우가 많다.
    2. 본 논문에서는 트위터로부터 얻은 4,442개의 예/아니오 질문-답변 쌍의 새로운 말뭉치를 제시한다. 예나 아니오로 해석되는 답변의 언어적 특성과 알려지지 않은 해석을 가진 답변에 대해 논의한다.
    3. 해당 문제에 대해 사회적 미디어 외부에서의 말뭉치를 세밀하게 조정하고 결합한 후에도, 대형 언어 모델이 이 문제를 해결하는 데는 여전히 멀었다는 것을 보여준다.

###### Task-Aware Self-Supervised Framework for Dialogue Discourse Parsing (https://aclanthology.org/2023.findings-emnlp.943/)
- Anthology ID: 2023.findings-emnlp.943 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 문맥 파싱은 다중 선택 문제 생성, 대화 요약 및 대화에서의 감정 인식 등 다양한 대화 관련 태스크에 유용한 자연 언어 처리 태스크이다. 
    2. 기존 파싱 접근법들은 사전에 정의된 관계 유형에 제한되어 있어 파서의 태스크에 대한 적응성이 제한될 수 있다. 
    3. 이 논문에서는 태스크에 대한 인식 패러다임을 도입하여 파서의 다양성을 향상시킨다.

###### Selective Demonstrations for Cross-domain Text-to-SQL (https://aclanthology.org/2023.findings-emnlp.944/)
- Anthology ID: 2023.findings-emnlp.944 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대규모 언어 모델(Large language models, LLMs)은 in-context learning을 통해 도메인 내 주석을 사용하지 않고도 교차 도메인 텍스트-투-SQL 작업에서 탁월한 일반화 능력을 보였다. 그러나 도메인 내 사례를 통합하면 LLMs의 성능이 크게 향상되는 것으로 나타났다. 
    2. 본 논문에서는 도메인 내 사례 내에서 성능 향상에 기여하는 주요 요소를 탐구하고, 도메인 주석에 의존하지 않고도 이러한 이점을 활용할 수 있는지 연구한다. 
    3. 그 결과, ODIS라는 사례 선택 프레임워크를 제안하고, 도메인 외 사례와 합성된 도메인 내 사례를 모두 활용하여 사례를 구성한다. ODIS는 하이브리드 소스에서 사례를 검색함으로써 양쪽의 장점을 활용하며, 단일 데이터 소스에 의존하는 기준 모델에 비해 효과적이다. 또한, ODIS는 두 개의 교차 도메인 텍스트-투-SQL 데이터셋에서 최신 접근 방법을 능가하며, 실행 정확도에서 각각 1.1 및 11.8 포인트의 개선을 나타낸다.

###### DocSplit: Simple Contrastive Pretraining for Large Document Embeddings (https://aclanthology.org/2023.findings-emnlp.945/)
- Anthology ID: 2023.findings-emnlp.945 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 모델 사전학습 방법은 로컬 정보만 고려하는데, 그 결과로 토큰 마스킹 전략을 사용하면 가까운 단어가 먼 단어보다 더 중요하게 여겨지기 때문에 문장 임베딩의 품질은 높지만 큰 문서에 대한 임베딩은 품질이 낮아진다.
    2. 우리는 전체적인 글로벌 문맥을 고려하도록 모델을 강제하는 DocSplit이라는 새로운 사전학습 방법을 제안한다.
    3. 우리의 실험 결과, DocSplit은 문서 분류, 퓨-샷 학습 및 정보 검색 작업에서 다른 사전학습 방법을 능가한다.

###### TELeR: A General Taxonomy of LLM Prompts for Benchmarking Complex Tasks (https://aclanthology.org/2023.findings-emnlp.946/)
- Anthology ID: 2023.findings-emnlp.946 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLMs가 전통적인 대화 상황에서 텍스트를 이해하고 생성하는 데 큰 성공을 보였지만, 복잡한 task를 수행하는 능력은 아직 연구되지 않았고 벤치마크되지 않았다.
    2. 이 논문에서는 다양한 task에 대한 프롬프트의 다양성과 성능에 대한 taxonomy를 제안한다. 이를 통해 향후 연구들에서 특정 task를 비교할 수 있게 되며, 연구자들은 LLMs의 성능에 대해 더 정확한 결론을 내릴 수 있다.
    3. 이 taxonomy는 다양한 연구를 통해 공통된 기준을 세워 LLMs의 복잡한 task 수행 능력을 평가하는데 도움을 줄 것이다.

###### IntenDD: A Unified Contrastive Learning Approach for Intent Detection and Discovery (https://aclanthology.org/2023.findings-emnlp.947/)
- Anthology ID: 2023.findings-emnlp.947 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 발화로부터 의도를 식별하는 것은 과제 지향 대화 시스템의 중요한 구성 요소입니다. 의도 관련 작업은 일반적으로 분류 작업으로 정의되며, 발화를 사전에 정의된 카테고리로 분류하거나 새로운 의도 카테고리를 발화에서 발견해야 하는 클러스터링 작업으로 모델링됩니다.
    2. 기존 방법들은 일반적으로 이러한 작업들을 별도의 작업으로 모델링하지만, 우리는 IntenDD라는 통합적인 접근 방법을 제안하여 공유 발화 인코딩 백본을 활용합니다. IntenDD는 표현 학습을 위해 완전히 비지도 대조학습 전략을 사용하며, 렉시컬 특징을 기반으로 레이블이 없는 발화에 가상 레이블을 생성합니다.
    3. 다양한 벤치마크 데이터셋에서의 광범위한 평가를 통해 IntenDD가 모든 세 가지 작업에서 경쟁력 있는 기준 모델보다 일관적으로 우수한 성능을 보였습니다. 평균적으로, IntenDD는 다중 분류(few-shot MC), 다중 레이블 (few-shot ML), 의도 발견 작업에서 각각 해당 지표에 대해 2.32% , 1.26%, 1.52%의 향상률을 보고하였습니다.

###### INarIG: Iterative Non-autoregressive Instruct Generation Model For Word-Level Auto Completion (https://aclanthology.org/2023.findings-emnlp.948/)
- Anthology ID: 2023.findings-emnlp.948 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 컴퓨터 보조 번역(CAT)은 인간 번역 효율을 향상시키는데 중요한데, 이 중에서도 Word-Level Auto Completion (WLAC)은 기존 방법들을 개선하여 가장 정확한 결과를 도출해냈다.
    2. 기존의 방법들은 타겟 단어의 양쪽 문맥을 고려하기 위해 단어 분류 모델을 사용하거나, 오른쪽 문맥의 의존성을 무시하는 문제가 있다.
    3. 이 논문에서는 INarIG(Iterative Non-autoregressive Instruct Generation) 모델을 제안하여 입력된 정보를 완전히 활용하기 위해 인간이 작성한 시퀀스를 Instruction Unit으로 구성하고 하위 단어를 사용한 반복적 디코딩 기법을 도입하여 낮은 빈도 단어에 대해서도 높은 예측 정확도를 달성하였다.

###### Is the Answer in the Text? Challenging ChatGPT with Evidence Retrieval from Instructive Text (https://aclanthology.org/2023.findings-emnlp.949/)
- Anthology ID: 2023.findings-emnlp.949 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 생성형 언어 모델이 텍스트 상황에서의 질문에 대한 정답을 생성하는 데 놀라운 성과를 보이고 있다. 그러나 이러한 답변은 환영에 걸려있거나, 잘못된 증거를 인용하거나, 오도적인 정보를 퍼뜨릴 수 있다.
    2. 이 연구에서는 ChatGPT라는 최신 생성 모델을 기계 독해 시스템으로 사용하여 이 문제를 다루고자 한다.
    3. 제안된 방법으로 ChatGPT는 신뢰할 수 있는 교육적 텍스트에서 다양하고 개방적인 질문에 대한 답을 검색하도록 요청하며, WHERE라는 평가 벤치마크가 도입된다. 이 데이터셋은 WikiHow 기사들을 대상으로 하며, 질문에 대한 증거 문장이 철저하게 주석 달려 있으며, 모든 질문이 기사의 주제에 관한 것인데도 불구하고 제공된 문맥을 사용하여 대답할 수 있는 것은 아니다.

###### PaRaDe: Passage Ranking using Demonstrations with LLMs (https://aclanthology.org/2023.findings-emnlp.950/)
- Anthology ID: 2023.findings-emnlp.950 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구결과에서는, 대형 언어 모델이(first stage retrieval method인 BM25를 포함하여) 효과적으로 zero-shot passage re-ranking을 수행할 수 있다는 것을 보여준다.
    2. 이 연구에서 우리는 프롬프트에 포함시킬 few-shot demonstrations를 알고리즘적으로 선택함으로써 LLM 기반의 re-ranking을 개선한다.
    3. 우리 연구는 어려움에 기반한 새로운 demonstrations 선택 전략을 제안하고, 랭킹에 도움이 되는 demonstrations은 질문 생성에서도 효과적임을 밝힌다.

###### Learning Dynamic Representations for Discourse Dependency Parsing (https://aclanthology.org/2023.findings-emnlp.951/)
- Anthology ID: 2023.findings-emnlp.951 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. discourse dependency parsing 문제에서는 기존 작업들이 transition history로부터 얻은 arcs를 무시하고 transition 상태를 일부 EDUs로만 특징화한다. 
    2. 이 논문에서는 이전 transition 단계에서 구성된 sub-trees에 대해 GAT 기반 인코더를 사용하여 동적 표현을 학습하는 것을 제안한다. 
    3. 실험 결과, 우리의 모델은 RST-DT, SciDTB, CDTB를 포함한 다양한 데이터셋에서 최고 성능을 달성할 수 있다는 것을 보여준다.

###### K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings (https://aclanthology.org/2023.findings-emnlp.952/)
- Anthology ID: 2023.findings-emnlp.952 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수많은 online hate 확산 방지를 위한 데이터셋이 제안되었지만, 이들의 대부분은 영어 위주이고, 주로 혐오 표현의 명시적인 형태에 초점을 맞추었다. 
    2. 이 연구의 목표는 미묘한 혐오 표현을 포함한 다양한 언어로 고품질의 코퍼스를 개발하는 것이다. 
    3. K-HATERS 데이터셋은 대상 특정적인 혐오 표현을 포함한 약 192,000개의 한국어 뉴스 댓글로 구성되어 있으며, 3점 Likert 척도로 대상별 불쾌감 정도를 평가하였다. 이 데이터셋은 한국어에서 다양한 정도의 혐오 표현을 감지할 수 있도록 구성되었다고 한다.

###### Mitigating Data Imbalance and Representation Degeneration in Multilingual Machine Translation (https://aclanthology.org/2023.findings-emnlp.953/)
- Anthology ID: 2023.findings-emnlp.953 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 언어 신경기계번역(MNMT)에서 데이터의 불균형과 표현의 역행에 대한 두 가지 주요 도전 과제가 여전히 존재한다고 주장한다.
    2. Bi-ACL을 제안하여 MNMT 모델의 성능을 향상시키기 위해 목표측 단일언어 데이터와 양방향 자동인코더, 양방향 대조학습 등의 모듈을 활용한다.
    3. 다양한 실험에서 제안된 방법이 나흘 언어와 고자원 언어에서 강력한 기준 모델보다 더 효과적임을 보여주며, 영역 및 언어 간의 지식 이전도 가능함을 입증한다.

###### BotPercent: Estimating Bot Populations in Twitter Communities (https://aclanthology.org/2023.findings-emnlp.954/)
- Anthology ID: 2023.findings-emnlp.954 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 트위터 봇 탐지는 가짜 정보와 소셜 미디어 대화의 정품성을 보호하기 위해 중요하다. 그러나 악성 봇은 점점 더 정교하고 개인화되고 있으며, 기존의 봇 탐지 방법은 이러한 봇들이 작동하는 소셜 환경(커뮤니티)을 고려하지 않으며 정확도가 떨어진다.
    2. 본 연구에서는 커뮤니티별 봇 탐지를 소개하며, 커뮤니티의 문맥을 고려하여 봇의 비율을 추정한다. BotPercent라는 방법은 트위터 봇 탐지 데이터셋과 특징, 텍스트, 그래프 기반 모델의 결합으로 이루어져 있다.
    3. 실험 결과, BotPercent는 균형 잡힌 클래스 분포와 불균형한 클래스 분포 설정에서 커뮤니티 수준 트위터 봇 탐지에서 state-of-the-art 성능을 보여주며, 트위터 커뮤니티 내 봇 인구의 편향이 적은 추정치를 제공한다. 봇이 존재하는 트위터 그룹(언론매체, 정치 커뮤니티 등)에서 봇 비율을 분석한 결과, 봇의 존재는 일정하지 않고 지리적-시간적 분포에서 상당한 이질성을 보여줌을 발견했다.

###### The Locality and Symmetry of Positional Encodings (https://aclanthology.org/2023.findings-emnlp.955/)
- Anthology ID: 2023.findings-emnlp.955 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. positional encodings (PEs)은 transformer 기반 언어 모델에 단어 순서 정보를 주입하는 데 사용되지만, 최근의 연구에서 여러 positional encodings가 단어 순서에 무감각하다는 사실에 대한 설명은 제대로 이루어지지 않았다. 
    2. 우리는 Bidirectional Masked Language Models (BERT-style)에서 positional encodings에 대한 체계적인 연구를 진행하여 (1) 두 가지 공통 속성, Locality와 Symmetry을 확인함으로써 PEs의 핵심 기능을 밝혀냈다. (2) 두 속성이 downstream tasks의 성능과 밀접한 상관관계를 가지고 있는 것을 보였다. (3) 우리는 현재의 PEs가 결과적으로 성능이 낮게 나오는 두 가지 새로운 probing tasks를 도입하여 현재 PEs의 약점을 양적 평가하였다. 
    3. 우리는 이러한 결과가 transformer 기반 언어 모델의 좀 더 나은 PEs 개발의 기초가 될 것이라고 믿고 있다.

###### Towards a Deep Understanding of Multilingual End-to-End Speech Translation (https://aclanthology.org/2023.findings-emnlp.956/)
- Anthology ID: 2023.findings-emnlp.956 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 22개 언어로 학습된 다중 언어 음성 번역 모델에서 학습된 표현을 평가하기 위해 Singular Value Canonical Correlation Analysis (SVCCA)를 사용한다. 이를 통해 다국어 음성 번역의 기능성과 다국어 신경망 기계 번역과의 관련성을 이해할 수 있다.
    2. 특정 언어의 학습 데이터가 제한적인 경우 다국어 음성 번역에서 언어적 유사성의 효과가 떨어진다.
    3. 제한된 데이터를 가진 저자원 언어와 언어적으로 연관된 고자원 언어를 결합하여 다국어 음성 번역의 효율적인 접근 방식을 제안한다.

###### An Empirical Investigation of Implicit and Explicit Knowledge-Enhanced Methods for Ad Hoc Dataset Retrieval (https://aclanthology.org/2023.findings-emnlp.957/)
- Anthology ID: 2023.findings-emnlp.957 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Ad hoc 데이터셋 검색은 웹에서 데이터를 찾는 중요한 방법이 되었으며, 해당 문제의 핵심은 데이터셋의 쿼리에 대한 관련성을 어떻게 측정할 것인가이다."
    2. 이 논문에서는 해당 특화된 작업에서 시용 가능한 지식 향상 검색 방법을 구현하고 평가하며, 명시적 및 암시적 지식 향상 검색 방법에 대해 다양한 설정에서 연구해 결과를 제시한다.
    3. 결과적으로 이 작업의 독특한 특성을 밝히며, 다양한 방법의 보간(interpolation)이 최상의 실천 방법이라는 것을 제안한다.

###### A Multi-Modal Multilingual Benchmark for Document Image Classification (https://aclanthology.org/2023.findings-emnlp.958/)
- Anthology ID: 2023.findings-emnlp.958 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문서 이미지 분류는 양식, 이메일 등과 같은 문서의 내용과 구조를 이해하여 문서를 분류하는 것으로, 일반 텍스트 문서 분류와는 다르다고 한다.
    2. 기존 데이터셋의 한계를 극복하기 위해 새롭게 만들어진 WIKI-DOC와 MULTIEURLEX-DOC라는 다국어 데이터셋을 제시하고, 다양한 시각적인 문서 이해 혹은 Document AI 모델이 이 데이터셋 위에서 잘 동작하지 않는 한계를 밝힌다.
    3. 시험적인 실험 결과는 다국어 Document AI 모델의 특성상 매우 다른 언어 간의 cross-lingual transfer에 한계가 있음을 보여주고, 이러한 데이터셋과 결과는 Document AI 모델의 개선에 대해 미래 연구의 문을 열 수 있다.

###### Unnatural language processing: How do language models handle machine-generated prompts? (https://aclanthology.org/2023.findings-emnlp.959/)
- Anthology ID: 2023.findings-emnlp.959 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수동으로 만든 의미론적이고 문법적으로 잘 구성된 프롬프트는 주로 단어 시퀀스에 기반한 자동 생성 프롬프트에 의해 능가된다.
    2. 기계가 생성한 프롬프트를 사용하여 모델이 자연어가 아닌 입력에 대해 어떻게 응답하는지 조사했다. 
    3. 기계 생성 프롬프트와 사람이 생성한 자연어 프롬프트에 대한 모델의 동작을 비교해 보여줬으며, 비슷한 출력을 만들더라도 각각 다른 응답 패턴을 가진다.

###### Investigating the Effectiveness of Multiple Expert Models Collaboration (https://aclanthology.org/2023.findings-emnlp.960/)
- Anthology ID: 2023.findings-emnlp.960 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구는 다양한 도메인에서 공정한 조건에서 여러 기계 번역(MT) 모델과 집계 방법의 효과를 조사하고, 다중 도메인 MT를 처리하는 방향을 탐구한다.
    2. 모든 도메인을 공동으로 훈련시키는 단일 모델 접근법과, 특정 집계 전략을 사용하는 다중 전문가 모델 접근법의 성능을 비교한다.
    3. 여러 도메인 전문가 모델을 조합하는 것이 모든 도메인 데이터를 훈련시킨 큰 모델보다 우수한 성능을 낼 수 있다는 것을 실험을 통해 입증한다.

###### Gradually Excavating External Knowledge for Implicit Complex Question Answering (https://aclanthology.org/2023.findings-emnlp.961/)
- Anthology ID: 2023.findings-emnlp.961 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델 (LLM)은 인간 수준의 능력과 막대한 잠재력으로 인해 큰 관심을 받고 있다. 그러나 오픈 도메인의 묵시적 질의응답 문제에 대해서는 LLM이 최적의 해결책이 아닐 수 있다. 
    2. 이 논문에서는 오픈 도메인 복잡한 질문 응답을 위한 점진적 지식 발굴 프레임워크를 제안한다. 
    3. LLM은 점진적으로 외부 정보를 습득하고 그에 따라 추론을 수행하여 최종 답을 찾아가는 방식으로 복잡한 질문에 대한 해결을 진행한다.

###### Evaluating Subjective Cognitive Appraisals of Emotions from Large Language Models (https://aclanthology.org/2023.findings-emnlp.962/)
- Anthology ID: 2023.findings-emnlp.962 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구는 CovidET-Appraisals라는 가장 포괄적인 데이터셋을 제시함으로써, 대화형 랭귀지 모델이 인지적 평가를 자동으로 평가하고 설명하는 능력을 평가하는 이상적인 테스트 베드를 제공한다.
    2. 최고의 모델이 성능이 좋음에도 불구하고 오픈소스 LLMs는 이 작업에서 부족한 것으로 나타났다.
    3. 많은 NLP 태스크에서 뛰어난 능력을 가진 랭귀지 모델의 미래 발전을 위한 새로운 도전 과제로 이어지는 결과를 보임.

###### Exploring Linguistic Properties of Monolingual BERTs with Typological Classification among Languages (https://aclanthology.org/2023.findings-emnlp.963/)
- Anthology ID: 2023.findings-emnlp.963 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. transformer 모델의 인상적인 성과로 인해 NLP 연구자들은 이 모델이 자연어의 기저 구조를 어떻게 표현하는지 조사하기 위해 깊이 파고들게 되었다. 
    2. 본 논문에서는 언어 간 유형론적 유사성을 사용하여 모노링구얼(transformer) 모델이 구조적 정보를 어떻게 인코딩하는지 관찰하는 새로운 접근법을 제안한다.
    3. 중앙 커널 얼라인먼트를 사용하여 weight matrices(가중치 행렬) 간 유사성을 측정하는 연구를 수행한 결과, 구문적 유형론적 유사성이 일반적으로 구문 인코딩을 담당하는 사전 학습된 BERT 레이어에 대한 가중치의 유사성과 일치한다는 것을 발견하였다.

###### Discourse Sense Flows: Modelling the Rhetorical Style of Documents across Various Domains (https://aclanthology.org/2023.findings-emnlp.964/)
- Anthology ID: 2023.findings-emnlp.964 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 얕은 담화파싱 연구에서는 특히 명시적 연결어와 대안적 어휘화 등 담화 관계 신호의 역할에 대해 새롭게 주목받고 있다.
    2. 우리는 먼저 Penn Discourse Treebank v3 말뭉치를 기반으로 명시적 연결어와 대안적 어휘화의 신호를 추출하고 의미를 분류하는 새로운 모델을 개발한다.
    3. 그 후 이 모델을 다양한 원시 말뭉치에 적용하고, PDTB의 의미에 의한 담론 스타일을 문서의 연결관계의 선형 순서로 모델링하는 'discourse sense flows'를 소개한다.

###### HierarchicalContrast: A Coarse-to-Fine Contrastive Learning Framework for Cross-Domain Zero-Shot Slot Filling (https://aclanthology.org/2023.findings-emnlp.965/)
- Anthology ID: 2023.findings-emnlp.965 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. task-oriented 대화 시나리오에서, 교차 도메인 제로샷 슬롯 채우기는 주요한 역할을 한다. 기존의 zero-shot slot filling 방법들은 타겟 도메인에서의 일반화 능력이 제한되어 있다. 
    2. 이 논문에서는 HiCL이라는 새로운 위계적 대조학습 프레임워크를 제안하여, 훈련 단계에서 보지 못한 슬롯 타입에도 일반화할 수 있도록 한다. 
    3. 강건한 성능을 갖는 이 방법을 사용하여 제로샷 슬롯 채우기를 수행하면 기존의 방법을 능가하는 성능을 보여줄 수 있다.

###### A Confederacy of Models: a Comprehensive Evaluation of LLMs on Creative Writing (https://aclanthology.org/2023.findings-emnlp.966/)
- Anthology ID: 2023.findings-emnlp.966 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구에서는 상상력, 일관성, 스타일을 요구하는 어려운 상황에서 최신 언어 모델 (LLM)들을 평가하였다. 결과적으로, 일부 상용 LLM은 대다수의 측면에서 우리 작가들과 비슷한 성능을 나타내었다. 
    2. 그러나 오픈소스 LLM은 이와 비교하여 뒤처지는 경향을 보였다. 
    3. 우리는 창의성에서 인간이 앞세워지고, 유머 측면에서는 일부 LLM만 인간과 비슷한 성능을 나타내는 바이너리(이분적) 구분을 볼 수 있다고 발견하였다.

###### 1-PAGER: One Pass Answer Generation and Evidence Retrieval (https://aclanthology.org/2023.findings-emnlp.967/)
- Anthology ID: 2023.findings-emnlp.967 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 1-Pager는 Transformer 기반 모델과 decoding 과정을 사용하여 질문에 답변하고 증거를 검색하는 첫 번째 시스템으로, 'retrieve-and-read' 대안과 비교해 검색 및 답변 정확성 측면에서 경쟁력을 보인다.
    2. 1-Pager는 증거 코퍼스에 기반하여 예측을 내리는 것으로, '닫힌 책' 형태의 질문 응답 모델보다 성능이 우수하다.
    3. 1-Pager는 더 많은 문서를 읽은 후에 답변을 생성하는 더 비용이 많이 드는 시스템과는 아직 동등한 성능은 아니지만, 이는 NLP에서 우월한 sequence-to-sequence 패러다임에 검색을 접목하여 발전시키는 중요한 단계를 제공한다는 주장이다. 또한, 코퍼스를 파티션하기 위해 사용된 검색 경로들은 읽고 이해하기 쉬우며, 해석 가능한 신경 검색에 대한 발전 방향을 제시한다.

###### Context-faithful Prompting for Large Language Models (https://aclanthology.org/2023.findings-emnlp.968/)
- Anthology ID: 2023.findings-emnlp.968 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large Language Models, LLMs)은 세계적 사실에 대한 지식을 효율적으로 인코딩할 수 있으나, 맥락에 민감한 NLP 태스크에서는 맥락에 관련된 단서를 간과하여 잘못된 예측을 할 수 있다. 
    2. 이 논문에서는 LLMs의 맥락적 충실성을 평가하고 향상시키기 위해 주어진 조건에 맞는 질문 방식을 사용하여 최대한 효과적인 방법을 찾아냈다. 
    3. 실험 결과, 해당 방식을 적용하면 기존 모델에 비해 더 맥락에 충실한 예측이 가능하다는 것을 확인할 수 있었다.

###### InfoCL: Alleviating Catastrophic Forgetting in Continual Text Classification from An Information Theoretic Perspective (https://aclanthology.org/2023.findings-emnlp.969/)
- Anthology ID: 2023.findings-emnlp.969 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지속적 학습(Continual learning)은 기존의 과제를 잊어버리지 않는 동안 새로운 지식을 지속적으로 배우는 것을 목표로 한다. 
    2. 이 논문에서는 텍스트 분류 과제에서 감소하는 성능 문제를 해결하기 위해 정보 병목 현상의 압축 효과를 다루고, 플레이백 기반의 새로운 지속적 텍스트 분류 방법을 제안한다. 
    3. 실험 결과, InfoCL은 잊음 문제를 효과적으로 완화하고 세 가지 텍스트 분류 과제에서 최고의 성능을 달성한다.

###### Sparse Frame Grouping Network with Action Centered for Untrimmed Video Paragraph Captioning (https://aclanthology.org/2023.findings-emnlp.970/)
- Anthology ID: 2023.findings-emnlp.970 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 이벤트 주석 없는 비트림된 동영상에 대한 문단 캡션을 생성하는 것이 동시에 정확성을 높이고 반복을 최소화하는 것은 어렵다는 도전에 대해 다루고 있다. 
    2. 이를 해결하기 위해, 이 논문은 Sparse Frame Grouping (SFG)이란 모듈을 제안하였다. 이 모듈은 전체 비디오에 대한 행동 정보로부터 이벤트 정보를 동적으로 그룹화하고 사전 정의된 클립 내에서 중복된 프레임을 제외한다.
    3. 실험 결과, SFG는 ActivityNet Captions와 YouCook2 데이터셋에서 모든 지표에서 최고 수준의 성능을 보여주고 있다.

###### Unsupervised Binary Code Translation with Application to Code Clone Detection and Vulnerability Discovery (https://aclanthology.org/2023.findings-emnlp.971/)
- Anthology ID: 2023.findings-emnlp.971 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 바이너리 코드 분석은 소프트웨어 보안 연구 분야에서 엄청난 중요성을 가지고 있다. 그러나 다양한 Instruction Set Architecture (ISA)에서 소프트웨어가 빈번하게 컴파일되는 경우, ISA를 건너뛴 바이너리 코드 분석은 신생 문제가 되었다. 본 논문에서는 NMT (Neural Machine Translation)의 개념과 기법을 바이너리 코드 분석에 적용하여 데이터 부족 문제를 해결하고 교차 아키텍처 바이너리 코드 분석을 용이하게 한다.
    2. 우리는 저 자원 ISA에서 효과적으로 교차 아키텍처 바이너리 코드 분석을 할 수 있도록, 저 자원 ISA의 바이너리를 고 자원 ISA (예: x86)로 번역하여 테스트한다. 이를 위해 고 자원 ISA에서 훈련된 모델을 사용하는데, 우리의 모델인 UNSUPERBINTRANS를 구현하고 그 성능을 평가하였다.
    3. 우리는 코드 유사성 감지와 취약점 탐지 두 가지 하위 태스크에서 실험을 진행하였고, 양쪽 모두에서 높은 정확도를 달성하였다.

###### Drilling Down into the Discourse Structure with LLMs for Long Document Question Answering (https://aclanthology.org/2023.findings-emnlp.972/)
- Anthology ID: 2023.findings-emnlp.972 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 zero-shot long document evidence retrieval 작업에 큰 언어 모델(Large Language Models, LLMs)이 얼마나 적용 가능한지를 평가하는 것을 목표로 한다. 그러나 현재 LLMs는 제한된 문맥 길이만을 입력으로 받기 때문에 문서 청크를 입력으로 제공하는 것은 글로벌 문맥을 간과하고 세그먼트 간 의존성을 제대로 캡처하지 못할 수도 있다.
    2. 따라서 우리는 독특한 문서 구조를 활용하는 기술들을 제안하여 이러한 도전을 해결한다. 이 구조를 활용하여 문서를 간결하게 표현하고 서로 다른 부분 간의 관계를 더 포괄적으로 이해하고 분석할 수 있다. 
    3. 전체 토큰의 26%만을 처리하면서 최고의 방법과 비교하여 99.6%의 성능을 유지할 수 있음을 보여주고, gold evidence 사용을 통한 zero-shot 성능에 근접한 복잡한 multi-hop 질문 응답에서도 우리의 접근 방식이 어떻게 최상의 zero-shot 성능을 달성할 수 있는지 설명한다.

###### Emergent Inabilities? Inverse Scaling Over the Course of Pretraining (https://aclanthology.org/2023.findings-emnlp.973/)
- Anthology ID: 2023.findings-emnlp.973 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구는 언어 모델의 성능이 학습 과정 동안 감소할 수 있다는 것을 조사하여 태스크별로 성능이 감소하는 경우가 있는지 알아보았다.
    2. Pythia 12B 모델의 경우, 학습 과정에서 성능이 감소하는 태스크 8개를 발견했다. 그 중 5개 태스크의 경우, 더 큰 언어 모델일수록 성능 감소가 더 크게 나타났으며, 전반적으로는 성능이 향상되더라도 성능 감소가 지속되는 것을 보였다.
    3. 이는 모델이 추가 데이터로 학습될 때 모든 관련 벤치마크에서 성능을 테스트하는 것의 중요성을 강조하며, 전반적인 성능이 향상되더라도 주의가 필요하다.

###### Alignment Precedes Fusion: Open-Vocabulary Named Entity Recognition as Context-Type Semantic Matching (https://aclanthology.org/2023.findings-emnlp.974/)
- Anthology ID: 2023.findings-emnlp.974 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이름 있는 entity 인식 모델들의 개발에서 이루어진 큰 성과에도 불구하고, 새로운 유형으로의 확장은 여전히 현실 세계에서 어렵다. 
    2. 지속적인 학습 및 zero-shot 학습 방법들은 새로운 유형을 처리하기 위해 인간 지도보다 적은 자동 지도를 사용하여 시도되었으나, 지도 학습 방법에 비해 성공적으로 적용되지 못했다.
    3. 이 논문에서는 인간 수준의 능력을 모방하기 위해 open-vocabulary named entity recognition(OVNER)이라는 더 현실적이고 도전적인 상황을 고려한다.
    
    (논문 초록을 토대로 한 번더 요약하자면) 
    산업 현장에서 개발된 이름 entity 인식 모델로도 새로운 유형의 entity에 대한 대응이 어려워 여러가지 학습 방법론을 실험하였으나, 지도 학습 방식에 비해 성과가 좋지 않았다. 이 논문은 그와 같은 개선을 위해 실제 사람의 능력을 모방하기 위한 상황을 가정하였으며 이를 위한 메커니즘을 제안한다.

###### Representation Projection Invariance Mitigates Representation Collapse (https://aclanthology.org/2023.findings-emnlp.975/)
- Anthology ID: 2023.findings-emnlp.975 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습된 언어 모델에서 학습된 문맥화된 표현을 미세 조정하는 것은 NLP에서 흔히 사용되는 방법이지만, 이 과정에서 representation degradation 문제가 발생할 수 있다. 본 논문에서는 Representation Projection Invariance (REPINA)라는 새로운 정규화 방법을 제안하여 미세 조정하는 동안 표현의 정보 내용을 유지하고 representation collapse를 감소시킨다.
    2. 실험 결과, REPINA는 다른 기준선과 비교했을 때 대부분의 과제에서 (13개 중 10개) 가장 우수한 성능을 보였으며, 분야 내 성능 뿐만 아니라 분야 외 성능도 향상시켰다. 
    3. 또한, REPINA는 소량 데이터 및 레이블 변동에 대해 강건하며, representation collapse를 측정하기 위한 여러 메트릭을 제안하였으며, 이를 통해 본 논문의 방법이 representation collapse를 완화하는 데 효과적임을 입증하였다.

###### Tunable Soft Prompts are Messengers in Federated Learning (https://aclanthology.org/2023.findings-emnlp.976/)
- Anthology ID: 2023.findings-emnlp.976 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Federated Learning(FL)은 분산된 데이터 소스를 사용하여 협업적으로 기계 학습 모델을 교육하는 것을 가능하게 한다. 하지만 FL에서 모델 개인 정보 보호가 부족해지는 문제가 발생하며, 특허 상표의 대형 언어 모델을 기반으로 모델을 연방 수정하고 싶을 때 특히 도전이 된다.
    2. 이 연구에서는 튜닝 가능한 소프트 프롬프트를 통해 참가자들 간의 정보 교환을 수행하는 새로운 FL 훈련 접근법을 제안한다. 이러한 소프트 프롬프트는 서버와 클라이언트 간에 업데이트되고 전달되는데, 글로벌 모델 파라미터의 역할을 가지며 로컬 데이터와 글로벌 모델에서 유용한 지식을 전달하는 메신저 역할을 한다.
    3. 제안된 접근 방식은 글로벌 모델이 공유되지 않으며 로컬 훈련이 글로벌 모델보다 적은 파라미터를 가진 보조 모델을 기반으로 진행되므로, FL에서 통신 및 계산 비용을 줄이면서 글로벌 모델을 보호한다. 실험적 결과는 제안된 접근 방식의 효과를 여러 기준과 비교하여 보여준다.

###### Style-Aware Radiology Report Generation with RadGraph and Few-Shot Prompting (https://aclanthology.org/2023.findings-emnlp.977/)
- Anthology ID: 2023.findings-emnlp.977 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의료 이미지로부터 자동으로 생성된 보고서는 영상의과학자들의 업무 효율성을 향상시킬 수 있으나, 보고서의 내용 (영상 속 사항 등)을 포맷과 단어의 선택과 함께 생성하는 기존 방식은 잘못된 보고서를 생성할 수 있다.
    2. 본 연구에서는 라디오로지 보고서 생성을 위해 두 단계의 접근법을 제안한다. 먼저 이미지로부터 내용을 추출한 다음 추출된 내용을 특정 영상의과학자의 스타일에 맞춰 보고서로 변환한다.
    3. 실험결과, 우리의 방법은 유용한 성능 향상을 이끌어냄을 보여주었으며, 임상평가자들에게서 얻은 결과는 AI가 생성한 보고서가 몇 가지 예시를 사용하여 개별 영상의과학자의 스타일에 맞는 맞춤형 보고서로 전환이 가능하다는 것을 보여준다.

###### Incorporating Probing Signals into Multimodal Machine Translation via Visual Question-Answering Pairs (https://aclanthology.org/2023.findings-emnlp.978/)
- Anthology ID: 2023.findings-emnlp.978 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 문장이 완전한 경우에 MMT 시스템이 이미지 정보에 대한 감성이 감소한다는 일반적인 이해를 자세히 연구하였다. 이 현상은 이미지 정보의 중복이 아닌 교차 모달 상호작용 부족에 기인한다고 주장한다.
    2. 소스 텍스트에서 VQA 스타일의 병렬 한영 쌍을 생성하여 더 강력한 교차 모달 상호작용을 유발하기 위한 새로운 접근 방식을 제안한다.
    3. Multi30K-VQA 데이터셋을 만들기 위해 MMT에서 VQA 스타일 데이터로 프로빙(probing) 신호를 명시적으로 모델링하고, 이를 MMT 훈련 과정에 통합하는 MMT-VQA 다중 작업 학습 프레임워크를 도입한다.

###### GenKIE: Robust Generative Multimodal Document Key Information Extraction (https://aclanthology.org/2023.findings-emnlp.979/)
- Anthology ID: 2023.findings-emnlp.979 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 스캔된 문서로부터 중요한 정보를 추출하는 Key information extraction(KIE)은 다양한 분야에서 응용 가능성으로 인해 점점 더 주목을 받고 있다. 
    2. 이 논문에서는 OCR 오류를 다루거나 번거롭게 토큰 수준의 레이블링을 필요로 하지 않는 새로운 생성 모델인 GenKIE를 제안한다. 
    3. GenKIE는 시각, 레이아웃 및 텍스트 기능을 포함하여 여러 가지 입력 기능을 임베딩하는 다중모달 인코더와 원하는 결과를 생성하는 디코더를 사용하는 시퀀스-시퀀스 다중모달 생성 모델이다.

###### Improving Multimodal Sentiment Analysis: Supervised Angular margin-based Contrastive Learning for Enhanced Fusion Representation (https://aclanthology.org/2023.findings-emnlp.980/)
- Anthology ID: 2023.findings-emnlp.980 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 복합감성분석에서 다중 형상(fusion representation) 품질이 모델의 효과에 크게 의존하며, 이는 여러 modal의 표현이 예측 벡터에 편향을 줌으로써 발생한다. 
    2. 이러한 한계를 극복하기 위해 우리는 "Supervised Angular-based Contrastive Learning for Multimodal Sentiment Analysis"라는 프레임워크를 소개한다. 
    3. 이 프레임워크는 복합감성분석에서 다중 모달 표현의 식별력과 일반성을 향상시키고, 퓨전 벡터의 편향을 극복하는데 효과적임을 실험적으로 입증하였다.

###### Efficient Multilingual Language Model Compression through Vocabulary Trimming (https://aclanthology.org/2023.findings-emnlp.981/)
- Anthology ID: 2023.findings-emnlp.981 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 언어 모델에서 모델 파라미터가 크기 때문에 이 논문에서는 대상 언어에 대한 언어별 어휘만을 사용하여 여전히 좋은 성능을 유지하는 어휘 트리밍 (VT) 방법을 제안한다.
    2. VT는 기존 다국어 언어 모델의 어휘를 축소시켜 원래 모델로부터 어떤 언어에 대해서도 작동할 수 있다.
    3. 실험 결과, VT는 원래의 다국어 언어 모델과 비교해 크기가 상당히 작으면서도 성능을 유지할 수 있었으며, 특히 특정 언어에 대해 모델을 재학습할 필요 없이 작업과 관련된 언어의 특징을 유지하는 데 도움이 될 수 있다.

###### ICU: Conquering Language Barriers in Vision-and-Language Modeling by Dividing the Tasks into Image Captioning and Language Understanding (https://aclanthology.org/2023.findings-emnlp.982/)
- Anthology ID: 2023.findings-emnlp.982 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 이미지 캡션 생성을 위한 ICU (Image Caption Understanding)은 V&L 모델이 영어로 이미지에 대한 캡션을 생성하고, 이를 다국어 언어 모델(mLM)에 입력하여 다국어 언어 이해를 수행하는 두 단계로 V&L 작업을 분할하여 언어 장벽을 극복한다. 
    2. ICU는 다국어 텍스트 데이터가 풍부하고 품질이 높은 특징을 활용하여 V&L 모델에서 다국어 처리의 부담을 줄인다. 
    3. IGLUE 벤치마크에서 9개 언어로 진행한 실험 결과, ICU는 5개 언어에서 새로운 최고 성능을 달성하고, 나머지 언어에서는 비교 가능한 결과를 나타냈다.

###### GTA: Gated Toxicity Avoidance for LM Performance Preservation (https://aclanthology.org/2023.findings-emnlp.983/)
- Anthology ID: 2023.findings-emnlp.983 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. GPT-4와 같은 언어 생성 모델의 발전은 다양한 NLP 생성 태스크에서 놀라운 결과를 보여주었지만, 인종이나 성에 관련된 모욕적인 단어를 생성할 수 있기 때문에 피해 단어의 발생을 완화하기 위해 다양한 Controllable Text Generation (CTG) 방법들이 제안되었다.
    2. 그러나 기존의 CTG 방법들은 독성을 줄일뿐만 아니라 주제 일관성, 문법, 난해도 등 언어 모델의 생성 성능에도 부정적인 영향을 미친다.
    3. 이 논문은 이전 방법들의 한계를 탐구하고, 어떤 CTG 방법에도 적용할 수 있는 간단한 Gated Toxicity Avoidance (GTA)로 해결책을 제시한다. 제안된 GTA의 효과를 다양한 데이터셋과 최신 CTG 방법과 비교함으로써 검증하였으며, 결과는 독성 감소 수준은 유지하면서 언어 모델의 생성 성능을 보존하는 것을 보여준다.

###### LMGQS: A Large-scale Dataset for Query-focused Summarization (https://aclanthology.org/2023.findings-emnlp.984/)
- Anthology ID: 2023.findings-emnlp.984 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Query-focused summarization (QFS)은 주어진 질문에 직접 답변하거나 관련이 있는 요약문을 입력 문서에서 추출하거나 생성하는 작업이다. 그러나 문서, 질문, 요약으로 이루어진 대규모 데이터셋의 부족으로 모델 개발이 어려웠다고 한다."
    2. 저자들은 "일반적인 summarization 어노테이션에는 각각의 요약 문장마다 숨겨진 질문이 존재하며, 이를 복원하기 위해 대규모 사전 훈련된 언어 모델을 활용한다"라고 가설을 세우고, 이를 통해 네 가지 일반적인 요약 벤치마크를 QFS 벤치마크 데이터셋인 LMGQS로 변환한다.
    3. LMGQS에서 언어 모델을 파인튜닝함으로써 기존 QFS 벤치마크에서 zero-shot과 지도 학습 기반의 최고 성능을 달성하며, LMGQS의 고품질과 다양성을 입증한다.

###### ChatCoT: Tool-Augmented Chain-of-Thought Reasoning on Chat-based Large Language Models (https://aclanthology.org/2023.findings-emnlp.985/)
- Anthology ID: 2023.findings-emnlp.985 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLM)은 다양한 평가 벤치마크에서 우수한 성능을 보여주었지만, 특정 지식과 다중 점프 추론을 필요로 하는 복잡한 추론 작업에서 여전히 어려움을 겪는다.
    2. ChatCoT는 대화 기반 LLM (예 : ChatGPT)을 위한 도구보강된 chain-of-thought 추론 프레임워크로서, 여러 번의 대화로 구성된 추론을 모델링하여 도구를 보다 자연스러운 방식으로 활용한다.
    3. ChatCoT는 대화 기반 LLM의 다중 턴 대화 능력을 효과적으로 활용하며, 연속적인 단계적 도구보강 추론을 수행하기 위해 도구 사용과 추론 과정을 통합하는 방법을 제안한다. 최근 연구와 비교해 7.9% 상대적 개선을 이루어 복잡한 추론 작업에서의 효과를 입증하였다.

###### Non-Autoregressive Document-Level Machine Translation (https://aclanthology.org/2023.findings-emnlp.986/)
- Anthology ID: 2023.findings-emnlp.986 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에 제안된 non-autoregressive translation (NAT) 모델들은 문장 수준의 기계 번역에서 auto-regressive translation (AT) 모델들에 비해 비슷한 성능과 높은 속도를 보이지만, 문서 수준의 기계 번역에서의 능력은 아직 알려지지 않아서 실제 상황에서의 활용이 어렵다.
    2. 본 논문에서는 문서 수준의 기계 번역에서 일반적인 NAT 모델들을 철저히 조사하고, 소스와 타겟 사이의 문장 정렬에 대해 간단하지만 효과적인 설계를 제안한다.
    3. 실험 결과, NAT 모델들은 문서에서 높은 가속화를 달성하며, 문장 정렬은 그들의 성능을 크게 향상시킨다. 그러나 현재 NAT 모델들은 여전히 AT 모델들에 비해 상당한 성능 차이가 있다.

###### Exploring the Effectiveness of Multi-Lingual Commonsense Knowledge-Aware Open-Domain Dialogue Response Generation (https://aclanthology.org/2023.findings-emnlp.987/)
- Anthology ID: 2023.findings-emnlp.987 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구들은 대화 생성 시 일상적 상식 지식을 활용하여 정보성을 높이고 환상적인 내용을 줄이는 것에 대한 유망한 결과를 보여주었으나, 대화 맥락과 언어가 일관된 단일 언어의 상식 지식만 사용할 수 있다는 제한점이 있다.
    2. 이 논문에서는 다른 언어의 상식 지식을 활용하여 현재의 대화 생성을 향상시키기 위해 Multi-Lingual Commonsense Knowledge-Aware Response Generation (MCKRG)라는 새로운 과제를 제안한다.
    3. MCK-Dialog라는 7개 언어로 구성된 데이터셋을 생성하고, 제안된 MCK-T5 모델을 사용하여 다국적 상식 지식의 효과를 검증하였다. 풍부한 실험 결과는 다국적 상식 지식을 효과적으로 활용할 수 있는 높은 자원과 낮은 자원 언어에서의 큰 잠재력을 보여준다. 이 연구는 다국적 상식 지식을 활용한 대화 생성에 대한 첫 번째 시도이다.

###### Mixture of Soft Prompts for Controllable Data Generation (https://aclanthology.org/2023.findings-emnlp.988/)
- Anthology ID: 2023.findings-emnlp.988 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large language models, LLMs)은 자연어 패턴을 따를 때 유창한 텍스트를 효과적으로 생성하지만, 구조화된 예측 작업에서는 출력 형식이 제한되어 있어 이러한 제한을 고려하지 않고 훈련된 모델들도 고민하는 문제가 발생한다.
    2. 이 논문에서는 LLM을 직접 예측하는 대신 데이터 augmentation을 위한 도구로 활용하여 문제의 접근 방식을 바꿨다. 제안된 Mixture of Soft Prompts(MSP)은 제어된 방식으로 다중 속성 데이터를 생성하기 위한 매개변수 효율적인 절차로서 작동한다.
    3. 실험을 통해 MSP가 다양하고 자연스러운 텍스트를 생성하면서도 레이블 의미를 보존한다는 것을 확인할 수 있었고, 강력한 베이스라인과 비교했을 때 세 가지 벤치마크에서 최고 성능을 달성한다. 이러한 방법은 복잡한 예측 작업에 LLM을 적용하기 위한 대체적인 데이터 중심 접근 방식을 제공한다.

###### A Boundary Offset Prediction Network for Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.989/)
- Anthology ID: 2023.findings-emnlp.989 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 명명된 entity recognition (NER)은 텍스트에서 명명된 entity를 식별하고 분류하는 자연 언어 처리의 기본적인 작업이다. 하지만 NER에 대한 span 기반 방법은 일반적으로 텍스트 span에 entity 타입을 할당하며, 결과적으로 불균형한 샘플 공간을 가지며 non-entity와 entity span 간의 연결을 무시한다.
    2. 이 문제를 해결하기 위해, 우리는 경계 간격에 대한 예측 네트워크인 BOPN(Boundary Offset Prediction Network)라는 NER를 위한 새로운 접근 방식을 제안한다. BOPN은 non-entity와 entity span 간의 연결을 설정하기 위해 경계 간격의 안내 semantics를 활용하여, non-entity span이 entity 탐지에 추가적인 양성 샘플로 작동할 수 있게 한다.
    3. 게다가, 우리의 방법은 entity 타입과 span 표현을 통합하여 entity 타입을 검출 대상으로 사용하는 대신 타입 인식 경계 간격을 생성한다. 우리는 여덟 가지의 널리 사용되는 NER 데이터셋에서 실험을 수행하고, 결과는 우리의 제안된 BOPN이 이전 최첨단 방법보다 뛰어난 성능을 보여준다.

###### Prefix-Tuning Based Unsupervised Text Style Transfer (https://aclanthology.org/2023.findings-emnlp.990/)
- Anthology ID: 2023.findings-emnlp.990 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 비지도 텍스트 스타일 변환은 병렬 데이터를 사용하지 않고 입력 문장의 스타일을 변경하면서 내용을 보존하는 생성 모델을 훈련하는 것을 목표로 한다. 이 논문에서는 능력있는 사전 훈련된 대형 언어 모델을 활용하여 비지도 텍스트 스타일 변환에 대한 새로운 prefix-tuning 기반 방법을 제안한다.
    2. 우리는 공유 프리픽스(shared prefix), 스타일 프리픽스(style prefix), 내용 프리픽스(content prefix)의 세 가지 다른 종류의 프리픽스를 구성하여 각각 과제 특정 정보, 대상 스타일 및 입력 문장의 내용 정보를 인코딩한다.
    3. 이 논문에서 제안하는 방법은 이전 작업에서 사용된 임베딩보다 더 풍부한 정보를 제공할 수 있는 프리픽스를 사용하며, 재귀적인 방식으로 언어 모델을 사용하여 스타일 변환 과정에서 입력 문장과 GPT-2간의 상호작용을 더욱 효과적으로 처리한다. 이를 통해 우리의 방법은 유명한 데이터셋에서 상태-of-the-art 기준을 능가하는 결과를 보여주었다.

###### Evaluating and Enhancing the Robustness of Code Pre-trained Models through Structure-Aware Adversarial Samples Generation (https://aclanthology.org/2023.findings-emnlp.991/)
- Anthology ID: 2023.findings-emnlp.991 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CodePTMs (Code Pre-Trained Models)의 robustness를 평가하기 위해 이전의 방법들은 텍스트적인 측면을 중점으로하지만, 코드의 구조를 고려하지 않았다. 
    2. 이 논문에서는 코드의 내재적인 구조를 기반으로 한 새로운 robustness 평가 방법을 제안한다. 
    3. 코드의 식별자 토큰 및 서브트리 구조에 대한 적대적 공격을 수행하고, 동등한 정보를 가진 입력 샘플에 대한 모델의 민감도도 탐색하여 평가한다.

###### Annotation Sensitivity: Training Data Collection Methods Affect Model Performance (https://aclanthology.org/2023.findings-emnlp.992/)
- Anthology ID: 2023.findings-emnlp.992 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 학습 데이터가 인간 주석가로부터 수집되는 경우 주석기 계약의 디자인, 주석기에 제공되는 명령, 주석기의 특성 및 상호작용이 학습 데이터에 영향을 미칠 수 있다. 
    2. 본 연구는 주석 도구를 작성할 때 디자인 선택이 결과 주석에 훈련된 모델에도 영향을 미친다는 것을 보여준다.
    3. 우리는 주석 데이터 수집 방법이 주석 자체와 하류 모델 성능 및 예측에 미치는 영향을 가리키는 "annotation sensitivity"라는 용어를 소개한다.

###### Qualitative Code Suggestion: A Human-Centric Approach to Qualitative Coding (https://aclanthology.org/2023.findings-emnlp.993/)
- Anthology ID: 2023.findings-emnlp.993 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Qualitative coding"은 연구자가 어떤 텍스트 말뭉치를 읽고 구절에 서술적 레이블 또는 질적 코드를 할당하는 콘텐츠 분석 방법이다. 이 연구는 기존의 NLP 기술을 사용하여 질적 코드 작성자를 돕는 데 큰 도움이 될 수 있다고 본다.
    2. 기존 시도들은 질적 코딩을 완전히 자동화 가능한 분류 문제로 설정하지만, 이 논문에서는 질적 코드 제안(QCS) 작업을 협력적인 방식으로 정의한다.
    3. QCS는 이전에 할당된 질적 코드의 순위가 지정된 구절로부터 추천된다. 또한 QCS는 사용자 중심이며, 구절의 주석 순서, 희귀 코드의 중요성 및 코드 작성자 간 주석 스타일의 차이와 같은 질적 코딩의 이전에 무시된 특성을 통합한다.

###### D2TV: Dual Knowledge Distillation and Target-oriented Vision Modeling for Many-to-Many Multimodal Summarization (https://aclanthology.org/2023.findings-emnlp.994/)
- Anthology ID: 2023.findings-emnlp.994 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. M3S (Many-to-many multimodal summarization) 작업은 어떤 언어로든 문서 입력과 해당 이미지 시퀀스로 요약을 생성하는 작업이다. 기존의 MMS (multimodal monolingual summarization)나 MXLS (multimodal cross-lingual summarization) 작업과 다르게 M3S 작업에 대한 연구는 적은 편이다.
    2. 이 논문에서는 M3S 작업에 대한 일반적이고 실용적인 프레임워크를 제안한다. 빼려지지 않은 시각적 정보를 버리기 위해 target-oriented contrastive objective를 사용하고, dual knowledge distillation 방법을 사용하여 MMS와 MXLS 간의 지식을 상호 전달하고 서로 상호 작용할 수 있도록 보장한다.
    3. 많은 실험을 통해 제안된 접근 방식의 효과를 보여주며, 또한 44개 언어의 많은-많은 multimodal summarization 데이터셋인 lmttM3Sum을 제공하여 향후 연구에 도움을 준다.

###### Improving Input-label Mapping with Demonstration Replay for In-context Learning (https://aclanthology.org/2023.findings-emnlp.995/)
- Anthology ID: 2023.findings-emnlp.995 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "In-context learning (ICL)은 다운스트림 NLP 태스크의 모델 이해력을 향상시키기 위해 모델 파라미터를 직접 조정하지 않고 입력-라벨 증명을 입력에 추가하는 방식으로, 대규모 언어 모델의 적용 능력 중 하나이다."
    2. "ICL은 대규모 언어 모델의 강력한 언어 모델링 능력으로 인해 효과적이며, 입력과 라벨 사이의 매핑을 학습할 수 있다. 그러나 ICL의 인과성 특성으로 인해 언어 모델링은 역방향만 고려하며, 전체 입력-라벨 정보를 포착하지 못하고 모델의 성능을 제한한다."
    3. "이 논문에서는 Repeated Demonstration with Sliding Causal Attention(RdSca)라는 독특한 ICL 방법을 제안한다. RdSca는 나중에 나오는 증명을 중복시켜 앞쪽에 연결함으로써 모델이 인과적 제약에도 불구하고 나중 정보를 '관찰'할 수 있게 한다. 또한 정보 노출을 피하기 위해 인과적 어텐션을 맞춤화하는 슬라이딩 인과주의도 소개한다. 실험 결과는 우리의 방법이 ICL 증명에서 입력-라벨 매핑을 크게 개선한다는 것을 보여주었다. 또한 학습 없이 인과주의 어텐션을 사용자 맞춤화하는 방법에 대한 깊이있는 분석도 수행하였다."

###### Enhancing Text-to-SQL Capabilities of Large Language Models: A Study on Prompt Design Strategies (https://aclanthology.org/2023.findings-emnlp.996/)
- Anthology ID: 2023.findings-emnlp.996 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 인공지능 (AI) 모델들은 대규모 언어 모델을 활용하여 일부 예시나 과제별 지시사항으로 보완된 문맥을 기반으로 예측하는 "In-context learning (ICL)"이라는 새로운 접근 방법이 자연어처리 태스크에 등장하였다.
    2. 이 연구에서는 이 방법을 구조화된 지식 소스를 활용하는 질의응답 (Question Answering) 태스크로 확장하고, LLM을 활용한 Text-to-SQL 시스템을 향상시키기 위한 다양한 프롬프트 디자인 전략을 탐구한다.
    3. 연구 결과, 다양성과 유사성을 모두 고려하는 예시 선택 방법은 성능을 향상시키며, 또한 데이터베이스 관련 지식의 보강이 LLM에 이익을 준다는 것을 보여준다. 따라서 이 방법은 Text-to-SQL 태스크에 LLM을 적용하는데 효과적이며, 성공적인 전략의 요인을 분석한다.

###### Cross-lingual Open-Retrieval Question Answering for African Languages (https://aclanthology.org/2023.findings-emnlp.997/)
- Anthology ID: 2023.findings-emnlp.997 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 아프리카 언어들은 디지털로 이용 가능한 내용이 매우 적어, 질문 답변 시스템이 사용자의 정보 요구를 충족시키는 것이 어렵다. 그래서 우리는 크로스-언어 개방형 검색 기반 질문 답변 (Cross-lingual open-retrieval question answering, XOR QA) 시스템을 통해 이 공백을 채울 수 있는 방법을 제공한다.
    2. 우리는 아프리카 언어에 초점을 맞춘 최초의 크로스-언어 QA 데이터셋인 Our Dataset을 만들었다. Our Dataset은 10개의 아프리카 언어를 대상으로 12,000개 이상의 XOR QA 예시를 포함하고 있다.
    3. 이전 데이터셋들은 대상 언어의 정보 커버리지를 보완하는 방식으로 주로 사용되었다. 하지만 Our Dataset은 크로스-언어 답변이 높은 커버리지의 유일한 소스인 언어에 초점을 맞춘다. 이를 통해 우리는 아프리카 언어가 XOR QA의 가장 중요하고 현실적인 사용 사례 중 하나라고 주장한다.

###### Viewing Knowledge Transfer in Multilingual Machine Translation Through a Representational Lens (https://aclanthology.org/2023.findings-emnlp.998/)
- Anthology ID: 2023.findings-emnlp.998 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 신경 기계 번역에서는 번역 품질만으로는 지식 전달을 측정하는 데 충분한 지표가 되지 않는다는 주장이 있다. 
    2. 우리는 표현적 전달 잠재력(RTP)을 도입하여 언어 간의 표현적 유사성을 측정한다. RTP는 긍정적 전달과 부정적 전달(간섭) 모두를 측정할 수 있으며, 번역 품질의 변화와 강한 상관관계가 있으며, 이는 전달이 발생한다는 것을 보여준다. 
    3. 또한, 전달에 관련된 데이터 및 언어 특성을 조사하였고, 다중 병렬 중복(multi-parallel overlap)이 중요한 특징임을 발견하였다. 이를 바탕으로, 우리는 다중 병렬 데이터를 활용하여 언어 간 불변성을 장려하는 보조 유사도 손실(auxiliary similarity loss)을 사용하는 새로운 훈련 방법을 개발하였다. 이 방법은 다양한 데이터 및 모델 설정에서 저자원 언어의 번역 품질을 향상시킨다.

###### Aligning Predictive Uncertainty with Clarification Questions in Grounded Dialog (https://aclanthology.org/2023.findings-emnlp.999/)
- Anthology ID: 2023.findings-emnlp.999 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 효과적인 협업을 위해서는 명확하지 않은 부분을 물어볼 필요가 있다. 이 논문에서는 예측 불확실성을 기반으로 질문의 필요성을 근거화하는 방법을 제안한다. 
    2. T5 인코더-디코더 아키텍처를 사용하여 Minecraft 협업 건축 과제를 해결하는 인공 에이전트를 학습한다. 명확하고 모호한 지시 사이의 분포적 차이를 더 잘 달성하는 불확실성 metric을 식별한다.
    3. 또한, 잘 보정된 예측 확률이 모호한 지시사항을 탐지하는 데 도움이 됨을 보여주고, 불확실성과 대화 기록 길이간의 관계에 대한 신규한 분석을 제시하여 감지에 어려움을 가지는 중요한 특성을 강조한다.

