# Korean Three-Line Summarizations of Papers 1787-1886 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Connecting the Dots: What Graph-Based Text Representations Work Best for Text Classification using Graph Neural Networks? (https://aclanthology.org/2023.findings-emnlp.600/)
- Anthology ID: 2023.findings-emnlp.600 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 구조 정보를 고려한 기계 학습인 GNN의 성공에도 불구하고, 많은 연구들은 특정 도메인에 대해서만 텍스트 분류에 GNN을 사용하였으며, 데이터의 특성에 제한이 있다. 
    2. 이 연구는 다양한 GNN 아키텍처와 설정을 사용하여 다섯 가지 데이터셋에서 다양한 그래프 구성 방법을 비교하고, 각각의 장단점과 개방적인 도전 과제를 밝힌다. 
    3. 실험 결과, 텍스트 입력 특징과 도메인에 따라 그래프의 효과가 다르며, 간단한 그래프 구성 방법이 문서가 길수록 더 좋은 성능을 보여주고, 긴 문서에 대해서는 Transformer-based 모델보다 그래프 표현 방법이 효과적이며, 텍스트 분류 작업에 그래프 기법이 특히 효율적이다.

###### Natural Language Annotations for Reasoning about Program Semantics (https://aclanthology.org/2023.findings-emnlp.601/)
- Anthology ID: 2023.findings-emnlp.601 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 연구자들은 프로그래밍 조수를 만들기 위해 자연어 추론을 코드와 결합하고, 코드에서 추론을 도출하여 그들의 작업을 설명하고, 교육 가능한 프로그래밍 조수를 만들고, 그들의 추론에 있는 틈새를 찾으려고 한다.
    2. 우리는 정적 분석 없이 구문과 일반적인 주석만으로 프로그램의 흥미로운 속성을 자동으로 추론할 수 있을까? 프로그램의 논리와 행동은 얼마나 많이 자연어로 표현될 수 있을까?
    3. 이 논문에서는 이러한 질문에 대답하기 위해 HTL 데이터셋과 프로토콜을 제안한다. 이 데이터셋은 코드 주석에 의존하지 않고, 내부 컴파일러 표현을 사용하지 않고, 코드에 자연어 술어를 더 세분화된 수준으로 주석으로 추가하는 것이 가능하도록 구성되어 있다.

###### Pre-trained Speech Processing Models Contain Human-Like Biases that Propagate to Speech Emotion Recognition (https://aclanthology.org/2023.findings-emnlp.602/)
- Anthology ID: 2023.findings-emnlp.602 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 성별, 인종 등과 같은 인간의 편견에 모델이 영향을 받는 것은 알려져 왔으나, 어떻게 이러한 편견이 생기는지는 아직 파악되지 않았다. 
    2. 이 논문에서는 사전 훈련된 모델에서 편견을 감지하기 위한 메소드인 SpEAT를 제안하고, 이를 사용하여 다양한 영어 음성 모델에서 여섯 가지 유형의 편견을 확인하였다.
    3. 사전 훈련된 음성 모델에서 발견된 편견은 실제 세계에서도 영향을 미칠 수 있으며, SER 작업에 적용된 모델에서도 이러한 편견이 전파될 수 있다는 것을 보여주었다.

###### Text Classification via Large Language Models (https://aclanthology.org/2023.findings-emnlp.603/)
- Anthology ID: 2023.findings-emnlp.603 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. GPT-3와 같은 대규모 언어 모델은 텍스트 분류 작업에서 성능이 좋지 않은데, 이는 복잡한 언어 현상에 대한 추론 능력의 부족과 in-context learning에서 허용되는 토큰 수의 제한 때문이다.
    2. 이 논문에서는 Clue And Reasoning Prompting(CARP)을 소개하는데, 이는 텍스트 분류에서 복잡한 언어 현상에 대응하기 위해 고안된 점진적 추론 전략을 사용한다. CARP은 LLM에게 표면적인 단서를 찾도록 유도하고, 이를 기반으로 최종 결정을 위한 진단 추론 과정을 수행한다. 또한, 제한된 토큰 문제를 해결하기 위해 CARP은 in-context learning에서 kNN demonstration search를 사용한다.
    3. CARP은 4개의 텍스트 분류 벤치마크에서 새로운 SOTA 성능을 보여주며, 저자들은 CARP가 낮은 자원과 도메인 적응에서 인상적인 능력을 발휘한다고 밝혔다. 또한, CARP는 클래스당 16개의 예제를 사용하여 1,024개의 예제를 사용한 지도 학습 모델과 비슷한 성능을 달성한다.

###### On Task-personalized Multimodal Few-shot Learning for Visually-rich Document Entity Retrieval (https://aclanthology.org/2023.findings-emnlp.604/)
- Anthology ID: 2023.findings-emnlp.604 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 비주얼리 리치한 문서 엔티티 검색(VDER)은 송장과 영수증과 같은 문서 이미지에서 주요 정보(예: 날짜, 주소)를 추출하는 것이 중요한 산업용 NLP 응용 프로그램이 되었다. 그러나 새로운 문서 유형이 지속적으로 등장하면서 각각 고유한 엔티티 유형을 포함하기 때문에 다양한 도전 과제가 발생한다. 
    2. 이 연구에서는 새로운 개체 수준의 퓨 샷 VDER 작업을 연구하는데, 이는 각 작업별로 고유한 레이블 공간과 OOD 콘텐츠의 복잡성이 증가하는 독특한 시나리오에서 이루어진다. 
    3. 실험 결과, 우리의 접근 방식은 인기있는 메타 학습 베이스 라인의 견고성을 크게 향상시킴을 보여준다.

###### Semi-Structured Object Sequence Encoders (https://aclanthology.org/2023.findings-emnlp.605/)
- Anthology ID: 2023.findings-emnlp.605 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 반정형 객체 시퀀스 모델링에 대한 과제를 탐구하며, 특히 이러한 시퀀스에 대한 구조를 고려한 입력 표현 개발에 초점을 맞춘다.
    2. 기존 방법들과 비교하여 우리의 접근법은 hierarchical encoding과 record-centric 표현, flattened 표현을 포함한 다른 방법들을 능가하며, 실제 데이터를 사용한 여러 예측 과제에서 우수한 성능을 보여준다.
    3. 특히, two-part 접근법과 shared-attention-head 아키텍처 및 독특한 훈련 스케줄을 제안하여 기존 방법보다 더 긴 객체 시퀀스에 대해 처리할 수 있다.

###### DeTiME: Diffusion-Enhanced Topic Modeling using Encoder-decoder based LLM (https://aclanthology.org/2023.findings-emnlp.606/)
- Anthology ID: 2023.findings-emnlp.606 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 처리 분야에서 Neural Topic Models (NTMs)와 Large Language Models (LLMs)는 중요한 연구 관심을 받는 분야로 등장하였다. 그러나 NTMs는 주로 LLMs에서 가져온 문맥 임베딩을 사용하는데, 이는 클러스터링에 최적화되지 않거나 토픽 생성에 용이하지 않다.
    2. 본 연구는 Diffusion-Enhanced Topic Modeling using Encoder-Decoder-based LLMs (DeTiME)라는 새로운 프레임워크를 도입하여 이러한 공백을 해결한다. DeTiME은 Encoder-Decoder 기반 LLMs를 활용하여 클러스터링 가능한 임베딩을 생성하고, 기존 방법과 비교하여 우수한 클러스터링 능력과 향상된 의미적 일관성을 가지는 토픽을 생성할 수 있다.
    3. 또한, 확산의 힘을 이용함으로써 DeTiME은 식별된 토픽과 관련 콘텐츠를 생성할 수 있는 능력을 제공한다. 이 중복 기능을 통해 사용자는 효율적으로 고도로 군집화된 토픽과 관련 콘텐츠를 동시에 생성할 수 있다. DeTiME은 임베딩을 생성하는 데에도 적합하며, 학습이 효율적이고 높은 적응성을 가지며 다양한 응용 분야에 잠재력을 보여준다.

###### Energy and Carbon Considerations of Fine-Tuning BERT (https://aclanthology.org/2023.findings-emnlp.607/)
- Anthology ID: 2023.findings-emnlp.607 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 연구에서 널리 사용되는 미세 조정 (fine-tuning) 접근 방식의 에너지 비용과 탄소 배출량을 정량화하는 작업이 선행되어왔으나, 이 작업은 주로 언어 모델에 집중되어 왔다.
    2. 하나의 사전 훈련 (pre-training) 단계가 낮은 훈련 단계보다 훨씬 더 많은 에너지를 소모하지만, 미세 조정은 더 자주 수행되며 많은 수의 개별 작업자에 의해 수행되므로 NLP의 에너지와 탄소 발자국을 고려할 때 반드시 고려해야 한다.
    3. 본 논문에서는 작업, 데이터셋, 하드웨어 인프라 및 측정 모드에서 미세 조정의 계산 비용에 대한 신중한 실험적 연구를 수행하고, 사전 훈련 및 추론과 비교하여 미세 조정의 에너지 및 탄소 비용을 이해하고 미세 조정의 에너지 효율성을 향상시키기를 원하는 NLP 연구자와 실무자들에게 가이드라인을 제공한다.

###### Democratizing LLMs: An Exploration of Cost-Performance Trade-offs in Self-Refined Open-Source Models (https://aclanthology.org/2023.findings-emnlp.608/)
- Anthology ID: 2023.findings-emnlp.608 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소위 비공개 LLM의 지배로 인해 접근이 제한되고 정보 개인정보 보안에 대한 우려가 제기되고 있다. 
    2. SoTA(open-source) 대안은 정보 민감한 고용량의 어플리케이션에 중요하지만 성능에서는 부족한 경우가 많다. 
    3. 이 논문에서는 어떤 고려 사항에 따라 태스크에 최적인 모델을 찾기 위해 PeRFICS라는 새로운 랭킹 메트릭과 외부 영향이 없는 반복적인 자가 비판과 자가 재정립 메커니즘을 제안한다.

###### Chinese Metaphorical Relation Extraction: Dataset and Models (https://aclanthology.org/2023.findings-emnlp.609/)
- Anthology ID: 2023.findings-emnlp.609 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 메타포 식별은 일반적으로 sequence labeling이나 구문적으로 관련된 단어 쌍의 분류 문제로 구성된다. 이 논문에서 우리는 메타포 식별을 관계 추출 문제로 새롭게 정의한다. 우리는 타겟 범위와 소스 관련 범위라는 두 가지 범위 사이의 링크인 메타포 관계를 도입한다.
    2. 우리는 타겟과 소스의 특성을 파악하기 위해 단어 이상의 유연하고 정확한 텍스트 단위를 사용할 수 있는데, 이는 단어 단위로는 어려운 메타포의 특성을 잡아낼 수 있다.
    3. 우리는 중국어 메타포 관계 추출을 위한 데이터셋을 만들고, 타겟/소스 관련 범위와 세부적인 범위 유형과 함께 4,200개 이상의 문장을 메타포 관계로 주석을 달았다. 우리는 메타포 관계 추출을 위한 범위 기반의 end-to-end 모델을 개발하고 이의 효과성을 입증했다.

###### Example-based Hypernetworks for Multi-source Adaptation to Unseen Domains (https://aclanthology.org/2023.findings-emnlp.610/)
- Anthology ID: 2023.findings-emnlp.610 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 알고리즘의 발전에도 불구하고, 도메인 외 일반화는 여전히 큰 도전이다. 이 논문에서는 다양한 소스 도메인으로부터 레이블된 데이터를 활용하여 훈련 중에 알려지지 않은 대상 도메인에 일반화하는 문제를 다룬다. 
    2. 우리는 하이퍼네트워크 적응으로 예시 기반 메타-러닝을 사용하여 새로운 시그니처를 생성하고, 이를 하이퍼네트워크를 통해 과제 분류기의 가중치를 생성하는 혁신적인 프레임워크를 제안한다.
    3. 이 방법을 감성 분류와 자연어 추론 두 가지 작업에서 29개의 적응 시나리오에서 평가하였고, 기존 알고리즘보다 성능이 우수한 것을 확인하였다. 또한 세부 적인 사례에 대한 효과성을 입증하기 위해 few-shot GPT-3와 우리의 학습 모델을 비교하였다. 이 논문은 알려지지 않은 도메인에 대한 하이퍼네트워크 적응의 첫 번째 적용 사례로 전해진다.

###### Beneath the Surface: Unveiling Harmful Memes with Multimodal Reasoning Distilled from Large Language Models (https://aclanthology.org/2023.findings-emnlp.611/)
- Anthology ID: 2023.findings-emnlp.611 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사회적 미디어 시대에는 진부한 "밈"이 넘쳐나고 있는데, 이 밈들의 의미를 탐지하고 파악하는 것은 텍스트나 이미지로는 명시적으로 전달되지 않는 때문에 중요한 도전 과제이다.
    2. 기존의 해로운 밈 탐지 방법들은 표면적으로 해로울 특징을 분류하는 방식만을 사용하고 있지만, 밈의 텍스트와 이미지에 대한 깊은 인식을 무시하고 있다.
    3. 본 논문에서는 밈의 다중 모달 정보를 교차작용을 통해 뛰어난 추론을 기반으로 해로운 밈을 탐지하려고 한다. 많은 양의 텍스트를 다루는 대형 언어 모델에 영감을 받아, 본 연구에서는 추론 연산을 수행하고 그 결과를 이용하여 다중 모달 융합과 가볍게 튜닝하는 새로운 생성적 프레임워크를 제안한다. 이러한 아이디어를 바탕으로 한 실험 결과는 기존 방법과 비교하여 우수한 성능을 보여준다.

###### Domain Adaptation for Conversational Query Production with the RAG Model Feedback (https://aclanthology.org/2023.findings-emnlp.612/)
- Anthology ID: 2023.findings-emnlp.612 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "대화형 쿼리 생성은 대화 시스템을 위한 신흥 기본 작업으로, 검색 엔진에서 방대하고 지속적으로 업데이트되는 지식을 탐색하기 위해 검색 쿼리를 생성한다. "
    2. "이 연구 분야를 가속화하기 위해 이전 연구에서는 여러 가지 도메인의 대화를 커버하지 못하는 제한적인 주석이 달린 데이터셋을 공개해왔으나, 이 과제를 해결하기 위해 우리는 신규 도메인 적응 프레임워크를 제안한다. "
    3. "이 프레임워크는 이전 작업에서 개선된 약간 지도 학습 알고리즘을 바탕으로 하고, RAG 모델 피드백에 따라 방향을 제시하여 더욱 견고하고 강력한 결과를 보여준다."

###### LEGO: A Multi-agent Collaborative Framework with Role-playing and Iterative Feedback for Causality Explanation Generation (https://aclanthology.org/2023.findings-emnlp.613/)
- Anthology ID: 2023.findings-emnlp.613 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인과성 설명 생성은 초기 원인-결과 쌍이 주어지면 자연어로 설명을 생성하는 것을 말한다. 이 과제는 명시적이고 철저한 근거를 요구하며, 일반 상식 지식을 습득하기 위해 메모리에 쉽게 기억되지 않는 것으로 알려져 있기 때문에 대형 언어 모델에 대한 도전과제이다. 
    2. 이 논문은 LEGO라는 다중 에이전트 협업 프레임워크를 소개하는데, 이는 역할 할당 및 반복적 피드백을 통해 LLM을 자유롭게 변형 가능한 레고 블록으로 취급한다. 먼저 세밀한 세계 지식 통합 모듈을 사용하여 표준 인과 관련성 현상을 완화하기 위해 과제에 대한 정보를 보완한다. 그런 다음 다면적 피드백과 개선 모듈을 이용하여 생성된 설명을 개선한다. 
    3. WIKIWHY와 e-CARE 데이터셋에서의 실험 결과, 우리의 다중 에이전트 프레임워크가 원인과 결과 사이의 인과관계를 추론하는 면에서 우수성을 보였다.

###### Ranking LLM-Generated Loop Invariants for Program Verification (https://aclanthology.org/2023.findings-emnlp.614/)
- Anthology ID: 2023.findings-emnlp.614 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 공리화된 루프 불변수의 합성은 프로그램 검증을 자동화하는 데에 기본적이다. 이 연구에서는 GPT-3.5 또는 GPT-4와 같은 대형 언어 모델은 0-shot 설정에서 특정 프로그램의 루프 불변수를 합성하는 능력을 갖추고 있지만, 올바른 불변수를 생성하기 위해 여러 개의 샘플이 필요하다. 이는 불변수를 확립하기 위해 프로그램 검증기에 대규모 호출을 유발할 수 있다. 이 문제를 해결하기 위해 우리는 LLMs의 생성 결과에 대한 재랭킹 접근법을 제안한다. 우리는 문제 정의를 기반으로 올바른 불변수와 잘못된 시도를 구별할 수 있는 랭커를 설계했다. 이 랭커는 대조 랭커로 최적화되었다. 실험 결과는 이 재랭킹 메커니즘이 생성된 후보들 중 올바른 불변수의 순위를 크게 향상시키며, 검증기에 대한 호출 수를 현저히 줄일 수 있음을 보여준다.
    
    2. 대형 언어 모델인 GPT-3.5나 GPT-4는 특정 프로그램의 루프 불변수를 0-shot 설정에서 합성하는 능력을 갖추고 있지만, 올바른 불변수를 생성하기 위해서는 여러 개의 샘플이 필요하다. 이로 인해 불변수를 검증기에 확립하기 위한 호출 수가 많아질 수 있다.
    3. 이를 해결하기 위해 우리는 생성된 결과에 대한 재랭킹 접근법을 제안하며, 문제 정의를 기반으로 올바른 불변수와 잘못된 시도를 구별하는 랭커를 설계했다. 실험 결과는 이러한 재랭킹 메커니즘이 올바른 불변수의 순위를 크게 향상시키고 검증기에 대한 호출 수를 현저히 줄일 수 있음을 보여준다.

###### WordNet Is All You Need: A Surprisingly Effective Unsupervised Method for Graded Lexical Entailment (https://aclanthology.org/2023.findings-emnlp.615/)
- Anthology ID: 2023.findings-emnlp.615 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 WordNet을 사용하여 영어에서 등급화된 어휘 의미 연관성 (GLE)을 예측하는 간단한 비지도 학습 방법을 제안한다.
    2. 우리의 방법은 WordNet의 계층적인 synset 구조를 활용하여 대칭적 의미 유사도 점수와 비대칭적 특수성 손실 점수의 합으로 GLE를 모델링한다.
    3. 우리의 방법은 HyperLex (Vulic et al., 2017)라는 가장 큰 GLE 데이터셋에서 상태-of-the-art 성능을 달성하며, WordNet을 약한 지도로 사용하는 전문화된 단어 임베딩 방법을 포함한 모든 이전 방법을 능가한다.

###### Knowledge Corpus Error in Question Answering (https://aclanthology.org/2023.findings-emnlp.616/)
- Anthology ID: 2023.findings-emnlp.616 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 오픈 도메인 질의 응답(QA) 작업에서는 기존의 검색 단계 대신에 큰 언어 모델(LLM)에서 context passages를 생성하는 방식을 적용해왔다. 하지만 생성된 passages가 검색된 것보다 효과적일 수 있는 이유는 잘 알려져 있지 않다.
    2. 이 연구에서는 QA의 전통적인 접근 방식을 재검토하고, knowledge corpus error라는 개념을 도입한다. 이 오류는 검색에 사용된 지식 corpus가 전체 string space의 하위 집합일 때 발생하며, corpus 밖에 있는 더 도움이 되는 passages를 제외할 수 있다.
    3. LLM들은 더 큰 공간에서 passages를 생성함으로써 이러한 한계를 완화할 수 있으며, LLM을 사용하여 인간 주석이 달린 gold context를 다른 방식으로 해석하는 실험을 제안하고, 세 가지 QA 벤치마크에서의 결과는 paraphrased passage를 사용할 때 성능이 향상되었으며, 이는 knowledge corpus error의 존재를 나타낸다.

###### Epsilon Sampling Rocks: Investigating Sampling Strategies for Minimum Bayes Risk Decoding for Machine Translation (https://aclanthology.org/2023.findings-emnlp.617/)
- Anthology ID: 2023.findings-emnlp.617 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 기계 번역에서는 최소 베이즈 위험(MBR) 디코딩이 beam search 디코딩 대안으로 효과적일 수 있다는 것이 밝혀진 바 있다. 그러나 MBR 디코딩은 어떻게 및 얼마나 많은 후보를 모델에서 샘플링하는지에 크게 의존하며, 이 논문에서는 MBR 디코딩을 위한 후보 목록 생성 방법이 성능에 어떤 영향을 미치는지 탐구한다.
    2. 우리는 선조 법칙, nucleus 샘플링, 상위 k 샘플링과 같은 인기있는 샘플링 방법을 평가한다.
    3. 인간 평가를 통해 우리는 epsilon-sampling 기반 MBR 디코딩이 beam search 디코딩뿐만 아니라 다른 모든 샘플링 방법과 비교하여 네 개의 언어 쌍에서 유의미한 성능 향상을 보인다는 것을 입증하였다.

###### The language of prompting: What linguistic properties make a prompt successful? (https://aclanthology.org/2023.findings-emnlp.618/)
- Anthology ID: 2023.findings-emnlp.618 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최신 LLMs(Large Language Models)는 zero-shot이나 few-shot에서 놀라운 성능을 보이는데, 이때 prompt의 선택에 따라 성능이 크게 달라지므로 prompt 최적화에 대한 연구들이 많이 진행되고 있다. 그러나 prompt의 언어적 특성이 작업 성능과 어떻게 관련되는지에 대한 체계적인 이해가 부족하다. 
    2. 이 연구에서는 LLM의 크기, 사전훈련된 정도에 따라 다른 LLM들이 의미적으로 동일하지만 언어 구조가 다른 prompt에서의 성능을 비교한다. 저자들의 발견은 사전훈련이나 지시 튜닝 데이터에서의 언어 사용을 반영하는 prompt에서 최적 성능을 얻을 수 있다는 일반적인 가정과는 다르게, prompts은 데이터셋이나 모델 간에 잘 전이되지 않고, 성능은 보통 perplexity, 단어 빈도, 단어 의미 모호성 또는 prompt의 길이로 설명할 수 없다는 것이다. 
    3. 이 결과를 바탕으로 저자들은 prompting 연구에 대한 더 견고하고 포괄적인 평가 기준의 제안을 제시한다.

###### When and Why Does Bias Mitigation Work? (https://aclanthology.org/2023.findings-emnlp.619/)
- Anthology ID: 2023.findings-emnlp.619 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신경망 모델은 얕은 표면적인 특징을 활용하여 언어 이해 작업을 수행하는 것으로 나타났으며, 이는 실무자가 원하는 보다 깊은 언어 이해 및 추론 기술을 배우는 것과는 다릅니다. 
    2. 이전 연구에서는 모델을 편견 있는 특징이나 데이터셋의 결함에서 멀리하도록 하는 Debiasing 기술을 개발했지만, 이러한 Debiasing으로 인해 모델은 숨겨진 편견에 더 의존함으로써 테스크를 해결하는 데 도움이 되는 견고한 특징을 학습하지 못할 수 있다는 것을 보여주고 있습니다. 
    3. 그 결과로 우리는 기존의 모델을 Debiasing 하는 것만으로는 많은 언어 이해 작업에는 충분하지 않을 수 있으며, 상식적 추론과 추론과 같은 복잡한 과제를 해결하기 위해 새로운 학습 패러다임을 고려해야 할 것을 제안합니다.

###### Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation Synergy (https://aclanthology.org/2023.findings-emnlp.620/)
- Anthology ID: 2023.findings-emnlp.620 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "검색 보강 생성은 오래되어 고정된 지식과 환각과 같은 거대한 언어 모델의 한계를 극복할 수 있는 아주 유망한 분야로써 많은 관심을 받아왔다. 그러나 특히 복잡한 정보 요구를 가진 쿼리의 경우, 검색 시 관련성을 파악하기 어렵다. 최근 연구에서는 대형 언어 모델을 검색에 적극적으로 참여시켜 관련성 모델링을 개선하는 방안을 제안해왔다."
    2. "우리는 이 논문에서 Iter-RetGen이라고 부르는 방법으로 검색과 생성을 반복적으로 통합함으로써 강력한 성능을 얻을 수 있다는 것을 보여준다. 모델의 작업 입력에 대한 응답은 작업을 완료하기 위한 필요한 내용을 보여주며, 따라서 다른 반복에서 더 관련 있는 지식을 검색하고 이를 통해 더 나은 응답을 생성하는 데 도움이 된다."
    3. "우리는 다중 홉 질문응답, 사실 검증, 상식적 추론 등에서 Iter-RetGen을 평가하고, 파라미터 기반 지식과 비파라미터 기반 지식을 유연하게 활용할 수 있으며, 검색과 생성의 추가적인 부담이 적으면서 최첨단 검색 보강 기베스랑 경쟁력이나 우위를 갖는다. 생성 보강 검색 적응을 통해 성능을 더욱 향상시킬 수 있다."

###### Dynamic Low-rank Estimation for Transformer-based Language Models (https://aclanthology.org/2023.findings-emnlp.621/)
- Anthology ID: 2023.findings-emnlp.621 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 행렬 분해 방법 (SVD와 그의 variant들)은 Transformer 기반 언어 모델의 압축에 널리 사용되지만, 기존 방법들은 결국 변화하는 중요도 분포 가정을 하고 파인튜닝 후에 추가적인 조정을 요구하는 문제가 있다.
    2. 이 논문에서는 트레이닝 과정에서 다른 레이어의 행렬에 동적 rank 자원을 할당하는 RankDyna라는 행렬 분해 방법을 제안한다.
    3. 다양한 파라미터 예산 수준에서 RankDyna가 다른 SOTA 방법들보다 우수한 성능을 보이며, 더 높은 압축률에서 RankDyna의 이점이 더욱 부각되는 것을 확인할 수 있다.

###### Non-parallel Accent Transfer based on Fine-grained Controllable Accent Modelling (https://aclanthology.org/2023.findings-emnlp.622/)
- Anthology ID: 2023.findings-emnlp.622 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 강세 전이 연구는 병렬 데이터나 음성인식 모델에 의존하였으나, 이 논문은 비병렬 데이터를 사용하여 강세 전이의 실제 응용을 위해 연구하였다.
    2. 이 연구에서는 강세 전이 모델링의 어려움과 음성 표현의 분리에 집중하였다.
    3. 연구에서 제안한 방법들은 음조와 리듬을 고려하여 강세를 세밀하게 모델링하고, 상호 정보 학습을 이용하여 생성된 음성의 강세를 제어하는 방법으로 이러한 문제들을 해결하였다. 실험 결과는 제안된 프레임워크가 기준 모델과 비교하여 강인함과 오디오 품질 측면에서 우수한 성능을 보였다.

###### Compositional Generalization for Data-to-Text Generation (https://aclanthology.org/2023.findings-emnlp.623/)
- Anthology ID: 2023.findings-emnlp.623 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 데이터-텍스트 생성은 구조화된 데이터를 일관된 텍스트로 변환하는 과정인데, 새로운 형태의 구조화된 데이터를 처리할 때 여전히 문제가 발생하여 (위조나 생략과 같은) 텍스트의 충실성에 영향을 준다. 
    2. 이 문제를 "composition generalisation"이라 칭하며, 이를 해결하기 위해 다른 접근 방식의 성능을 평가하는 벤치마크를 만들기로 하였다. 
    3. 또한, 우리는 군집화를 통해 이러한 문제를 해결하는 새로운 모델을 제안한다. 이 모델은 문장 단위로 텍스트를 생성하며, 한 번에 하나의 군집된 Predicate를 사용한다. 이러한 접근 방식은 모든 평가 메트릭에서 T5에 비해 큰 개선을 보인다. 특히, 입력과의 충실성을 유지하는 메트릭에서 T5보다 31%의 향상을 이루었다.

###### In-Context Learning Creates Task Vectors (https://aclanthology.org/2023.findings-emnlp.624/)
- Anthology ID: 2023.findings-emnlp.624 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최신 언어 모델의 이기능 (ICL)은 강력한 학습 패러다임이지만 여전히 그 밑단 메커니즘을 잘 이해하지 못하고 있다.
    2. 이 논문에서는 ICL에서 학습된 함수가 매우 간단한 구조를 가지고 있다는 것을 보여줌으로써 기존의 기계 학습 프레임워크와의 관계를 설명한다.
    3. 실험을 통해 위의 주장을 지원하며 다양한 모델과 태스크에 걸친 결과를 보여준다.

###### TalkUp: Paving the Way for Understanding Empowering Language (https://aclanthology.org/2023.findings-emnlp.625/)
- Anthology ID: 2023.findings-emnlp.625 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 기술은 교육, 직장 업무, 의료 등 여러 실제 상황에서 중요하며, 하지만 NLP에서 강조되는 "empowering language"은 연구와 구체화하기 어렵다.
    2. 이 논문에서는 언어학과 사회심리학 문헌에 기반하여 empowering language을 탐색하며, 이를 위해 Reddit 게시물 데이터셋을 구축하였다.
    3. 이 데이터셋은 TalkUp이라고 불리며, empowering 및 disempowering language를 포착하는 언어 모델을 훈련시키는 데 사용될 수 있다. 또한 상황에 따른 함의, 전제, 사회적 맥락이 언어의 의미에 어떻게 영향을 미치는지 조사할 수 있는 방향성을 제공한다.

###### Unifying Text, Tables, and Images for Multimodal Question Answering (https://aclanthology.org/2023.findings-emnlp.626/)
- Anthology ID: 2023.findings-emnlp.626 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 멀티모달 질문 답변 (MMQA)은 여러 지식 모달리티 (예: 텍스트, 테이블, 이미지)에서 답을 도출하는 것을 목표로 하는데, 이는 다양한 응용 분야에 대한 주목을 받고 있다. 
    2. 현재의 MMQA 접근 방식은 단일 모달이나 이중 모달 QA 모델에 의존하는 경우가 많은데, 이는 모든 모달리티 간의 정보를 효과적으로 통합하고 사전 훈련된 언어 모델의 능력을 활용하는 데 제한이 있다. 
    3. 이 논문에서는 테이블 선형화와 이미지 캡셔닝 기술을 활용하여 세 가지 다른 입력 모달리티를 텍스트-텍스트 형식으로 통합하는 UniMMQA라는 새로운 프레임워크를 제안하고, 텍스트-텍스트 생성 과정에 다중모달 합리성 생성기를 도입하여 크로스모달 추론을 향상시켰다. 실험 결과는 UniMMQA의 지도 및 비지도 설정에서의 우수성을 보여준다.

###### Unsupervised Lexical Simplification with Context Augmentation (https://aclanthology.org/2023.findings-emnlp.627/)
- Anthology ID: 2023.findings-emnlp.627 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 논문은 감독되지 않은 데이터와 사전 훈련된 언어 모델만을 사용하는 새로운 자동 단어 간소화 방법을 제안한다. 
    2. 주어진 대상 단어와 그 문맥에 기반하여, 우리의 방법은 대상 문맥과 동일한 문맥뿐만 아니라 단어력 데이터에서 샘플링한 추가 문맥을 사용하여 대체어를 생성한다.
    3. 영어, 포르투갈어, 스페인어로 TSAR-2022 공유 과제에서 실험을 진행한 결과, 우리의 모델이 모든 언어에서 다른 감독 없는 시스템보다 큰 성능향상을 보여주며, GPT-3.5와 앙상블하면 새로운 최고 성능을 달성함을 보여주었다.

###### mLongT5: A Multilingual and Efficient Text-To-Text Transformer for Longer Sequences (https://aclanthology.org/2023.findings-emnlp.628/)
- Anthology ID: 2023.findings-emnlp.628 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 긴 입력을 처리하는데 적합한 multilingual한 텍스트를 텍스트로 변환하는 transformer 모델인 mLongT5를 개발했다.
    2. mLongT5 모델은 LongT5의 아키텍처를 기반으로하며, mT5의 multilingual 데이터셋과 UL2의 pretrained task를 활용한다.
    3. 다양한 multilingual summarization 및 question-answering 태스크에서 평가를 진행한 결과, mLongT5는 mBART나 M-BERT와 비교했을 때 더 강력한 성능을 보였다.

###### Multilingual Lottery Tickets to Pretrain Language Models (https://aclanthology.org/2023.findings-emnlp.629/)
- Anthology ID: 2023.findings-emnlp.629 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 사전학습 언어 모델(mPLMs)을 훈련할 때 발생하는 다국어로 인한 제약은 용량이 제한되었을 때 특히 심하게 나타난다. 이 논문은 이러한 문제를 해결하기 위해 개별 언어의 용량을 유지하면서 부정적인 간섭을 줄이는 방식을 제안한다.
    2. 먼저 모델의 규모를 줄여 간섭을 감소시키고, 그런 다음 전체 모델과 비슷한 성능을 가진 개별 언어의 하위 네트워크나 "복권티켓"을 찾는다.
    3. 이를 통해 추론 비용을 줄이고 성능을 향상시키는데 성공하며, 탐색 비용 또한 무시할 수 있으며 언어적 유사성을 qualitatively 보존한다.

###### Target-Aware Spatio-Temporal Reasoning via Answering Questions in Dynamic Audio-Visual Scenarios (https://aclanthology.org/2023.findings-emnlp.630/)
- Anthology ID: 2023.findings-emnlp.630 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오디오-시각적 문의-답변 (AVQA)은 다중 단계 시공간 추론을 포함하여 다중 모달 맥락에서 복잡한 작업이다. 
    2. 이 논문에서는 AVQA를 위한 새로운 목표지향적 시공간 고정 네트워크를 제안하였다. 
    3. 실험 결과는 우리의 방법이 기존 기법들보다 효과적이라는 것을 확인하였다.

###### KG-GPT: A General Framework for Reasoning on Knowledge Graphs Using Large Language Models (https://aclanthology.org/2023.findings-emnlp.631/)
- Anthology ID: 2023.findings-emnlp.631 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)은 비구조적인 텍스트 이해와 생성에 큰 발전을 이루고 있지만, 정형 데이터에 대한 응용은 아직 충분히 탐구되지 않았다. 특히, LLM을 지식 그래프(KG)의 복잡한 추론 작업에 사용하는 것은 거의 이루어지지 않았다. 
    2. 이 논문에서는 KG를 활용하는 작업에 LLM을 활용하기 위해 KG-GPT라는 LLM의 다목적 프레임워크를 제안한다. 
    3. KG 기반 사실 검증 및 KGQA 벤치마크를 사용하여 KG-GPT를 평가하였고, 해당 모델은 경쟁력있고 견고한 성능을 보여주었으며, 몇몇 fully-supervised 모델보다 우수한 성능을 보였다.

###### Breaking the Language Barrier: Improving Cross-Lingual Reasoning with Structured Self-Attention (https://aclanthology.org/2023.findings-emnlp.632/)
- Anthology ID: 2023.findings-emnlp.632 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 다국어 언어 모델(MultiLM)이 다른 언어에 대한 논리 추론 능력을 전이할 수 있는지 조사한다. 
    2. 새로운 언어에서 추론이 여전히 동일한 언어로 이루어지지만 모델은 학습한 추론 능력을 다국어로 전이시켜야하는 단일 언어 추론, 그리고 맥락과 질문의 언어가 다른 코드 스위치 추론 두 가지 방식에서 MultiLM의 다국어 추론 능력을 평가한다. 
    3. RuleTaker 및 LeapOfThought 두 가지 논리 추론 데이터셋에서 우리는 MultiLM이 단일 언어 설정에서는 추론 능력을 다국어로 전이시킬 수 있지만 코드 스위치 설정에서는 추론 능력을 전이하기 어려움을 보여준다. 이 관찰을 바탕으로, 우리는 코드 스위치 시퀀스에서 전문적인 효율성을 향상시키기 위해 특별한 매개 변수 세트를 사용하는 새로운 어텐션 메커니즘을 제안한다. 이는 RuleTaker 및 LeapOfThought 데이터셋에서 각각 14% 및 4%까지 추론 성능을 향상시킨다.

###### CITB: A Benchmark for Continual Instruction Tuning (https://aclanthology.org/2023.findings-emnlp.633/)
- Anthology ID: 2023.findings-emnlp.633 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Continual Learning (CL)은 지속적으로 새로운 지식을 학습하고 그것을 새로운 과제에 전달하는 사람의 학습 능력을 재현하기 위한 패러다임이다. 이 논문에서는 Continual Instruction Tuning (CIT)이라는 새로운 문제를 제안하고, 지식을 이전하는 데 도움이 되는 Instruction Tuning (IT)과 CL의 관계를 연구한다.
    2. 실험 결과, 기존의 CL 방법들이 자연어 지침을 효과적으로 활용하지 못하며, 순차적으로 Instruction Tuned 모델을 fine-tuning 하는 것이 비슷하거나 더 좋은 결과를 낼 수 있다고 보여주었다.
    3. 이 논문에서는 CIT에 영향을 미칠 수 있는 다양한 측면을 탐구하며, 이를 통해 이 분야에서의 더 많은 연구를 촉진할 수 있는 CIT 벤치마크를 제시한다.

###### Mixture-of-Linguistic-Experts Adapters for Improving and Interpreting Pre-trained Language Models (https://aclanthology.org/2023.findings-emnlp.634/)
- Anthology ID: 2023.findings-emnlp.634 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 언어 모델에 언어 구조를 주입하는 방식을 제안하여 경제적인 파라미터 조정 (PEFT) 설정에서 성능을 향상시킨다.
    2. 우리의 접근 방식에서는 다양한 언어 구조를 인코딩하는 병렬 어댑터 모듈을 사용하여, Gumbel-Softmax 게이트를 사용하여 각 레이어에서 이러한 모듈의 중요성을 결정한다.
    3. 실험 결과는 우리의 방법이 최첨단 PEFT 방법보다 많은 파라미터를 사용하지 않고 우수한 성능을 발휘할 수 있음을 보여준다. 또한, 각 레이어에서 각 모델이 선택한 전문가들을 분석하여 향후 연구에 대한 통찰력을 제시한다.

###### Towards Better Representations for Multi-Label Text Classification with Multi-granularity Information (https://aclanthology.org/2023.findings-emnlp.635/)
- Anthology ID: 2023.findings-emnlp.635 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 Pre-trained Language Model (PLM)을 사용하여 다중 라벨 텍스트 분류 (MLTC)를 위한 텍스트 표현 학습과 라벨 상관관계 모델링에 초점을 맞추었으나, PLM이 단어 빈도 중심의 텍스트 표현을 생성하여 서로 다른 라벨을 가진 텍스트가 가깝게 분포되는 문제가 있다.
    2. 이를 해결하기 위해, CL-MIL(Contrastive Learning-Multi-granularity Information Learning)이라는 새로운 프레임워크를 제안하여 텍스트 표현을 개선한다. 첫째로, 대조적 학습을 사용하여 균일한 초기 텍스트 표현을 생성하고 라벨 빈도를 암묵적으로 통합한다. 둘째로, 다양한 텍스트-라벨 상관관계, 라벨-라벨 관계 및 라벨 빈도와 같은 다중 그래뉴러티 정보를 텍스트 표현에 통합하고 구별력을 향상시킨다.
    3. 실험 결과에서는 CL-MIL의 모듈들이 보완적인 성능을 발휘하며, 텍스트 표현의 품질을 개선하고 MLTC에서 안정적이고 경쟁력 있는 성능 향상을 이끌어냄을 보여준다.

###### PCMID: Multi-Intent Detection through Supervised Prototypical Contrastive Learning (https://aclanthology.org/2023.findings-emnlp.636/)
- Anthology ID: 2023.findings-emnlp.636 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의도 감지는 자연어 이해(NLU)에서 주요한 작업으로, 사용자의 발화를 기반으로 사용자의 의도를 해석하는 대화 시스템의 구성 요소이다. 이 논문에서는 PCMID라는 새로운 Multi-Intent Detection 프레임워크를 제안한다. PCMID 모델은 최적화된 의미 공간에서 주어진 사용자 발화의 여러 의도 레이블에 대한 다중 의미 표현을 학습할 수 있다.
    2. 기존의 단일 의도 가정에 의한 의도 감지 시스템에 비해 PCMID는 실제 상황에서 각 사용자 발화가 매우 복잡하고 여러 의도를 표현할 수 있는 경우에 더 도전적인 작업이다.
    3. 실험 결과, PCMID는 다중 공개 벤치마크 데이터셋과 실제 세계 데이터셋에서 현재 최고의 성능을 달성한다.

###### Is GPT-4 a Good Data Analyst? (https://aclanthology.org/2023.findings-emnlp.637/)
- Anthology ID: 2023.findings-emnlp.637 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)은 맥락 이해, 코드 생성, 언어 생성, 데이터 스토리텔링 등 다양한 도메인과 작업에서 강력한 성능을 보여주면서 많은 데이터 분석가들이 인공지능에 의해 대체될까 우려하고 있다. 우리는 이 논란의 소재를 다루며 "GPT-4가 좋은 데이터 분석가인가?"라는 연구 질문을 제기하고 대조 연구를 통해 답하려고 한다.
    2. 우리는 GPT-4를 데이터 분석가로 간주하여 다양한 도메인의 데이터베이스를 사용하여 end-to-end 데이터 분석을 수행하도록 하였다. 우리는 GPT-4에 대한 prompt를 신중히 설계하여 실험을 진행하기 위한 프레임워크를 제안하였다.
    3. 실험 결과, GPT-4는 인간과 비교 가능한 성능을 달성할 수 있음을 보였다. 또한 GPT-4가 데이터 분석가를 대체할 수 있는 결론을 내리기 전에 추가 연구에 대한 조명을 제공한다.

###### DiffusionRet: Diffusion-Enhanced Generative Retriever using Constrained Decoding (https://aclanthology.org/2023.findings-emnlp.638/)
- Anthology ID: 2023.findings-emnlp.638 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Generative retrieval"은 쿼리를 관련 문서 ID로 매핑하는 새로운 정보 검색(IR) 패러다임으로 최근에 등장하였지만, 중간 추론 단계의 부족과 인공적인 문서 ID 기호 사용으로 인한 선훈단계와의 불일치 문제로 고통받고 있다.
    2. 이러한 한계를 극복하기 위해 우리는 검색 전에 쿼리로부터 문서 생성을 사용하는 중간 단계로서의 접근 방식을 제안한다.
    3. 실험 결과, 우리가 제안한 DiffusionRet은 기존의 generative retrieval 방법보다 우수한 성능을 보이며, 매우 작은 매개 변수 개수로 최신의 성능을 달성한다.

###### Estimating Large Language Model Capabilities without Labeled Test Data (https://aclanthology.org/2023.findings-emnlp.639/)
- Anthology ID: 2023.findings-emnlp.639 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (Large Language Models, LLMs)은 몇 가지 예시만으로도 문맥 학습 (In-Context Learning, ICL)을 효과적으로 수행할 수 있는 능력을 갖추었습니다. 그러나 ICL의 성공은 과제에 따라 다양하게 달라집니다. 따라서 새로운 과제에 대해 ICL을 적용할 수 있는지를 빠르게 판단하는 것은 중요합니다. 그러나 ICL 정확도를 직접 평가하는 것은 주로 비용이 많이 드는 상황에서는 비효율적입니다.
    
    2. 이 논문에서는 ICL 정확도 추정이라는 작업을 제안합니다. 이 작업에서는 새로운 과제에 대해 레이블이 없는 테스트 데이터만으로 LLM의 정확도를 예측합니다. ICL 정확도 추정을 수행하기 위해, LLM의 확신 점수를 특성으로 사용하여 메타모델을 훈련하는 방법을 제안합니다.
    
    3. 우리의 방법을 4개의 LLM과 3개의 과제 컬렉션을 포함한 새로운 벤치마크에서 여러 강력한 정확도 추정 기준과 비교하였고, 12개의 설정 중 7개에서 기존 기준에 비해 성능을 향상시켰습니다. 또한, 40개의 레이블이 있는 테스트 예제 당 직접 평가하는 것과 동일한 추정 성능을 달성하였습니다. 동시에 기존의 접근 방식은 모든 설정에서 정확하고 신뢰할 수 있는 ICL 정확도 추정을 제공하지 않아 LLM 예측의 불확실성을 측정하는 더 좋은 방법에 대한 필요성을 강조하고 있습니다.

###### A Novel Contrastive Learning Method for Clickbait Detection on RoCliCo: A Romanian Clickbait Corpus of News Articles (https://aclanthology.org/2023.findings-emnlp.640/)
- Anthology ID: 2023.findings-emnlp.640 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수익 증대를 위해 뉴스 웹사이트는 종종 유혹적인 뉴스 제목을 사용하여 사용자들이 제목을 클릭하고 전문을 읽도록 한다. 이 연구에서는 이러한 클릭베이트를 자동으로 탐지하는 작업을 Romanian 언어로 수행하는 새로운 Romanian Clickbait Corpus (RoCliCo)를 소개한다. 
    2. RoCliCo는 8,313개의 뉴스 샘플로 구성되어 있으며, 클릭베이트와 클릭베이트가 아닌 레이블로 수동으로 주석이 달려있다. 
    3. 기계학습 방법과 함께 가중 투표 앙상블을 사용하여 여러 베이스라인을 구축하고, BERT 기반 대조 학습 모델을 제안하여 클릭베이트 및 클릭베이트가 아닌 뉴스의 제목과 내용을 깊은 표현 공간에 인코딩하는 방법을 제시한다.

###### Large Language Models as Source Planner for Personalized Knowledge-grounded Dialogues (https://aclanthology.org/2023.findings-emnlp.641/)
- Anthology ID: 2023.findings-emnlp.641 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오픈 도메인 대화 시스템은 보다 정보성과 근거 있는 응답을 생성하기 위해 다양한 지식 원천을 필요로 한다. 
    2. 그러나 기존 지식-중심 대화 시스템은 단일 지식 원천에 초점을 맞추거나 여러 지식 원천 간의 의존성을 간과하여 일관성 없는 또는 패러독스적인 응답을 생성할 수 있다.
    3. 본 논문에서는 SAFARI라는 새로운 프레임워크를 제안하여 다중 지식 원천과 그 사이의 의존성을 효과적으로 결합하는 방법을 소개하고 실험 결과를 통해 SAFARI 프레임워크가 페르소나 일관성과 지식 강화된 응답을 효과적으로 생성할 수 있다는 것을 보여준다.

###### Toxicity in Multilingual Machine Translation at Scale (https://aclanthology.org/2023.findings-emnlp.642/)
- Anthology ID: 2023.findings-emnlp.642 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기계 번역 시스템은 중요한나 일부 오류, 특히 악성 표현 추가와 같은 치명적인 오류가 있다. 
    2. 저자들은 약 164개 언어로 만들어진 큰 평가 데이터셋을 사용하여 다양한 언어에서 추가된 독성을 평가하고 분석하였으며, 가장 많은 추가 독성을 보이는 언어는 저자들이 분석한 13가지 인구통계 축 중 제일 낮은 리소스를 가진 언어들이었다.
    3. 소스 기여에 대한 측정을 사용하여 독성의 원인을 해석하였고, 소스 기여와 독성 사이에는 유의한 상관관계가 있음을 보였다. 추가 독성을 줄이기 위해 훈련 데이터를 적절히 관리하고, 환각을 완화하고, 불안정한 변역을 확인하는 것을 권장한다.

###### Conversational Recommender System and Large Language Model Are Made for Each Other in E-commerce Pre-sales Dialogue (https://aclanthology.org/2023.findings-emnlp.643/)
- Anthology ID: 2023.findings-emnlp.643 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 E-commerce 사전 판매 대화에서 LLM과 CRS의 협력이 효과적일 수 있다는 것을 조사하고, 두 가지 협력 방법을 제안한다. 
    2. 협력 접근법에 대한 실험을 수행하고, E-commerce 사전 판매 대화의 네 가지 작업에 대한 두 가지 CRS와 두 가지 LLM의 협력 접근법의 영향을 분석한다. 
    3. 결과적으로 LLM과 CRS 간의 협력이 일부 경우에 매우 효과적일 수 있다는 것을 발견하였다.

###### VIP5: Towards Multimodal Foundation Models for Recommendation (https://aclanthology.org/2023.findings-emnlp.644/)
- Anthology ID: 2023.findings-emnlp.644 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 컴퓨터 비전, 자연어 처리, 추천 시스템은 독립적으로 발전하여 서로의 발전을 직접적으로 이용하기 어려운 상황이다. 
    2. 그러나 최근 foundation models의 개발로 인해, 다양한 모달리티와 추천 과제를 통합하기 위한 다중모달 foundation model(MFM)을 제안한다.
    3. 이를 위해 다중모달 개인화 프롬프트를 도입하고, 경량 어뎁터를 수행하는 매개변수 효율적인 훈련 방법을 제안하여 추천 성능을 향상시킨다.

###### A Spectral Viewpoint on Continual Relation Extraction (https://aclanthology.org/2023.findings-emnlp.645/)
- Anthology ID: 2023.findings-emnlp.645 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자립 관계 추출(CRE)은 새로운 관계 학습하면서 이전에 학습한 관계의 능력을 유지하기 위해 모델을 지속적으로 훈련시킨다. 연속적인 학습 문제에서와 마찬가지로, CRE에서는 학습된 공간이 변화하면서 표현이 변하고 이로 인해 이전 작업의 성능이 저하된다.
    2. 이 논문에서는 이러한 현상을 스펙트럼 관점에서 조명한다. 각 클래스의 형태에 대해, 그것의 고유 벡터(또는 스펙트럼 요소)가 크게 바뀌지 않는다면, 형태는 잘 유지된다는 주요 주장이다.
    3. 이분석을 기반으로, 우리는 단순하면서도 효과적인 클래스별 정규화를 제안하고, 표현 학습에서 고유값을 향상시킨다는 것을 관찰하였다. 실험 결과는 우리의 방법이 상당한 성능 향상을 보였으며, 더 큰 고유값이 더 좋은 성능을 보인다는 가설을 검증한다.

###### Learning to Follow Object-Centric Image Editing Instructions Faithfully (https://aclanthology.org/2023.findings-emnlp.646/)
- Anthology ID: 2023.findings-emnlp.646 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 명령은 텍스트-이미지 확산 모델의 출력을 편집하기 위한 강력한 인터페이스이지만, 암시적 의미를 모델링해야 하는 불명확성, 편집을 수행해야 하는 위치를 찾아야 하는 배정, 편집 명령에 영향을 받지 않는 이미지 요소를 보존해야 하는 충실성과 같은 여러 가지 도전 과제가 있다.
    2. 기존 접근 방식은 자연어 명령을 사용한 이미지 편집에 자동으로 생성된 페어 데이터를 의존하고 있다. 하지만 우리의 조사에서 다루었듯이 이러한 데이터는 노이즈가 많고 때로는 무의미하여 위의 문제를 악화시킨다.
    3. 이 논문에서는 세그멘테이션, Chain-of-Thought prompting, 시각적 질문응답 등 최근의 발전을 활용하여 페어 데이터의 품질을 크게 향상시켰다. 또한, 명령에 의해 변경되어야 하는 이미지 부분을 강조하여 지도신호를 향상시킨다. 개선된 데이터로 fine-tuning된 모델은 최첨단 기준선보다 미세한 객체 중심의 편집을 더 잘 수행하며, 자동 및 인간 평가에서도 위에서 언급한 문제들을 완화시키는 것을 보여준다. 더욱이, 우리의 모델은 시각적 은유와 같은 훈련 중 보지 못한 도메인으로의 일반화도 가능하다.

###### Zero-shot Topical Text Classification with LLMs - an Experimental Study (https://aclanthology.org/2023.findings-emnlp.647/)
- Anthology ID: 2023.findings-emnlp.647 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 large language models의 zero-shot 성능을 비교한 TTC23 데이터셋을 공유한다.
    2. TTC-specialized LMs(fine-tuning)이 벤치마크에서 최고의 성능을 보이며, 해당 코드와 모델은 커뮤니티에서 이용 가능하다.
    3. 본 논문의 결과는 topical text classification에 관심있는 실무자들에게 유용한 가이드가 될 것이다.

###### Are Personalized Stochastic Parrots More Dangerous? Evaluating Persona Biases in Dialogue Systems (https://aclanthology.org/2023.findings-emnlp.648/)
- Anthology ID: 2023.findings-emnlp.648 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델은 일반적이거나 특정 인구 집단과 대화에서 역할을 따라 할 수 있게 되었다. 
    2. 이 논문에서는 다음과 같은 persona의 사회적 편향성(“persona biases”)을 연구하며, 이는 대화 모델의 해로운 행동에 대한 민감도로 정의한다.
    3. 우리는 RNA/DNA, harmful expression, harmful agreement, 등 다섯 가지 측면에서 persona 편향을 평가하는 포괄적인 평가 체계를 세우면서, blender, ChatGPT, Alpaca, Vicuna와 같은 네 가지 다른 모델에서 얻은 연구 결과에서 대화 시스템의 중요한 사회적 편향성을 보이며 등장인물(persona)의 사용을 다시 검토할 필요성을 강조한다.

###### A Black-Box Attack on Code Models via Representation Nearest Neighbor Search (https://aclanthology.org/2023.findings-emnlp.649/)
- Anthology ID: 2023.findings-emnlp.649 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 적대적 코드 예시 생성 방법은 대체 변수의 제한된 가용성, 이 대체 변수의 높은 검증 비용, 그리고 주목할 만한 왜곡이 있는 적대적 샘플의 생성과 같은 여러 가지 도전 과제를 가지고 있다. 
    2. 이 논문에서는 RNNS라는 방법론을 제안하며, 과거의 공격을 기반으로 잠재적인 적대적 대체 변수를 찾기 위한 검색 시드를 사용한다. 또한, 이산적인 대체 변수 대신에 미리 훈련된 변수 이름 인코더를 사용하여 연속적인 벡터 공간으로 대체 변수를 매핑한다. 
    3. 실험 결과, RNNS는 ASR과 QT 측면에서 기준모델보다 우수한 성능을 보이며, 대체 변수의 수와 변수 길이 변화 측면에서도 기준모델에 비해 작은 왜곡을 도입한다. 또한, RNNS는 방어된 모델을 공격하는 데 효율적이며 적대적 훈련에 사용될 수 있다는 것을 실험적으로 보여준다.

###### How Well Do Text Embedding Models Understand Syntax? (https://aclanthology.org/2023.findings-emnlp.650/)
- Anthology ID: 2023.findings-emnlp.650 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 임베딩 모델은 텍스트 데이터의 의미적 특성을 잘 포착하는 데 기여하였지만, 이러한 모델이 다양한 문법적 문맥에서 일반화를 얼마나 잘하는지는 미처 연구되지 않았다.
    2. 이 논문에서는 구조적 휴리스틱과 개념 간의 관계 이해와 같은 두 가지 중요한 문법적 측면에서 텍스트 임베딩 모델의 문법 이해 능력을 검토하는 평가 세트인 SR을 개발한다.
    3. 기존 텍스트 임베딩 모델은 이러한 문법적 이해 과제를 충분히 해결하지 못했으며, 기존의 벤치마크 데이터셋을 기준으로 평가할 때 이러한 무능력이 더욱 두드러진다는 연구 결과를 밝힌다.

###### CASSI: Contextual and Semantic Structure-based Interpolation Augmentation for Low-Resource NER (https://aclanthology.org/2023.findings-emnlp.651/)
- Anthology ID: 2023.findings-emnlp.651 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 augmentation 기법은 NER과 같은 토큰 수준의 작업에서 주석 오염(annotation corruption) 문제로 성능 향상에 어려움을 겪고 있다.
    2. 또한, 기존 방법은 데이터셋에 다양한 문맥의 다양성을 신뢰성 있게 추가할 수 없어서 low-resource NER에 중요한 역할을 하는 것으로 알려진다.
    3. 이 논문에서는 semantic하게 유사한 두 문장을 strucutral하게 결합하여 의미적으로 올바르고 유창한 새로운 문장을 생성함으로써 주석 오염을 피하면서 고품질의 문맥적으로 다양한 augmentation을 생성하는 CASSI (Contextual and Semantic Structure-based Interpolation) 방법을 제안한다.

###### NEWTON: Are Large Language Models Capable of Physical Reasoning? (https://aclanthology.org/2023.findings-emnlp.652/)
- Anthology ID: 2023.findings-emnlp.652 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)이 구문, 의미, 단어 의미, 상식적 지식을 포함한 것이 실험적으로 입증되었으나, 일상 객체를 이해하는 데 중요한 속성에 대한 물리적 추론 능력에 대해서는 제한적으로 연구되었다.
    2. 우리는 LLM의 물리적 추론 능력을 평가하기 위한 NEWTON이라는 새로운 저장소와 벤치마크를 소개한다. 또한, 연구자가 해당 응용 분야에 적합한 객체와 속성에 맞게 커스터마이징된 이 벤치마크의 변형을 생성할 수 있도록 파이프라인을 제공한다.
    3. 우리의 결과는 GPT-4와 같은 LLM들이 시나리오 기반 작업에서 강한 추론 능력을 보이지만, 사람과 비교했을 때 객체-속성 추론에서 일관성이 부족함을 보여준다. 또한 NEWTON 플랫폼은 언어 모델의 평가와 향상을 위한 잠재력을 나타내며, 로봇 조작과 같은 물리적으로 기반된 환경에 통합하는 길을 열어준다. Project site: https://newtonreasoning.github.io

###### Beyond Denouncing Hate: Strategies for Countering Implied Biases and Stereotypes in Language (https://aclanthology.org/2023.findings-emnlp.653/)
- Anthology ID: 2023.findings-emnlp.653 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인터넷 상의 혐오 표현에 대처하기 위한 counterspeech는 인식 조절 (censorship) 없이 문제를 해결하는 인기 있는 방법이 되었으나, 이 격언적인 언어의 동작을 제대로 대처하기 위해서는 잘못된 고정 관념을 전도하고 이를 반박할 수 있는 능력이 필요하다. 
    2. 이 논문에서는 심리학과 철학 문헌에서 영감을 받아, 혐오 언어의 고정관념적 함축을 반박하는 여섯 가지 심리학적인 전략을 제안한다. 
    3. 실험결과에서는, 인간이 직접 작성한 counterspeech가 함축된 고정관념에 맞추어 구체적으로 반박하는 전략을 사용하는 반면, 기계 생성 counterspeech는 일반적으로 혐오 언어의 비인간성을 부인하는 전략을 사용한다.

###### On the Calibration of Large Language Models and Alignment (https://aclanthology.org/2023.findings-emnlp.654/)
- Anthology ID: 2023.findings-emnlp.654 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델은 많은 관심을 받고 널리 적용되고 있지만 신뢰성과 관련된 동시에 문제점들이 발생하고 있다.
    2. 우리는 신뢰성 평가를 위한 confidence calibration을 사용하여 deep model의 신뢰성을 측정하고 개선하는 중요한 도구로서의 역할을 연구하였다.
    3. 우리의 연구는 popular LLMs가 잘 캘리브레이션되어 있는지, 그리고 훈련 과정이 모델의 캘리브레이션에 어떤 영향을 미치는지에 대해 조명한다.

###### TCRA-LLM: Token Compression Retrieval Augmented Large Language Model for Inference Cost Reduction (https://aclanthology.org/2023.findings-emnlp.655/)
- Anthology ID: 2023.findings-emnlp.655 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT와 같은 큰 언어 모델의 인기가 증가함에 따라 기업들은 이 모델을 사용한 다양한 응용프로그램을 개발하고 있다. 이 논문에서는 사용자 쿼리에 대한 맥락 기반 학습 능력을 활용하여 지식 검색으로 얻은 정보를 활용해 응답을 생성하는데, 이때 발생하는 입력 토큰 크기 증가 문제를 해결하기 위해 압축 방법을 제안한다.
    2. 제안된 방법은 요약 압축과 의미 압축으로 구성된다. 요약 압축은 T5 기반 모델을 사용하여 다양한 길이의 샘플을 포함하는 데이터셋을 이용해 미세조정하고 요약을 통해 토큰 크기를 줄이는 방법이다. 의미 압축은 의미에 덜 영향을 미치는 단어를 제거하여 토큰 크기를 더욱 줄이는 방법이다.
    3. 제안된 방법들의 효과를 적절히 평가하기 위해, 임신 기간이나 영유아를 위한 음식 추천에 초점을 맞춘 FRDB라는 데이터셋을 제안하고 활용한다. 요약 압축은 토큰 크기를 65% 감소시키면서 정확성을 0.3% 향상시킬 수 있으며, 의미 압축은 토큰 크기를 20% 줄일 수 있는데 정확성은 1.6% 감소한다.

###### Identifying Conspiracy Theories News based on Event Relation Graph (https://aclanthology.org/2023.findings-emnlp.656/)
- Anthology ID: 2023.findings-emnlp.656 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사회적 미디어 짧은 텍스트에서는 여론이론이 다루어졌으나, 긴 뉴스 문서에서의 이러한 잘못된 정보에는 제한적인 관심이 있었다. 
    2. 이 논문에서는 뉴스 기사가 여론 이론을 포함하고 있는지 여부를 파악하는 것을 목표로 한다. 
    3. 이를 위해 각 기사에 이벤트 관계 그래프를 도입하여 여론 이론 식별에 필수적인 이야기의 문맥적 이해를 달성하고, 이벤트 관계 그래프를 이용하여 여론 이론 식별의 정확도와 재현율을 향상시키는 방법을 제안한다.

###### Salespeople vs SalesBot: Exploring the Role of Educational Value in Conversational Recommender Systems (https://aclanthology.org/2023.findings-emnlp.657/)
- Anthology ID: 2023.findings-emnlp.657 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 구매를 하려면 소비자는 도메인 지식을 습득하기 위해 연구하거나 판매원에게 상담을 해야하지만, 기존의 대화형 추천 시스템은 사용자의 배경 지식 부족을 간과하고 선호도만을 중점으로 한다.
    2. 이 논문에서는 제품 추천과 교육적 가치를 혼합한 대화형 에이전트를 위한 새로운 문제 공간을 정의한다.
    3. SalesOps라는 프레임워크를 소개하고, SalesBot과 ShopperBot을 소개하여 이러한 시스템을 시뮬레이션하고 평가할 수 있도록 한다.

###### Dynamic Open-book Prompt for Conversational Recommender System (https://aclanthology.org/2023.findings-emnlp.658/)
- Anthology ID: 2023.findings-emnlp.658 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Conversational Recommender System (CRS)은 대화형 대화를 통해 맞춤형 추천을 제공하고 있으나, 기존 방법들은 진행 중인 대화의 제한된 문맥에 의해 성능이 제한된다. 
    2. 이 논문에서는 Dynamic Open-book Prompt 접근법을 제안하여 학습 데이터를 추론 중에 참고할 수 있는 도구를 만들어 문맥의 한계를 해결한다.
    3. 실험 결과, 제안된 모델이 기존의 최신 방법보다 향상된 성능을 보여주었다.

###### Auto-Instruct: Automatic Instruction Generation and Ranking for Black-Box Language Models (https://aclanthology.org/2023.findings-emnlp.659/)
- Anthology ID: 2023.findings-emnlp.659 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLMs)은 과제별 세부 조정이 필요하지 않고 자연어 명령에 따라 다양한 작업을 수행할 수 있지만, LLM의 성능은 명령어의 품질에 크게 영향을 받으며, 각 작업용 효과적인 명령어를 수동으로 작성하는 것은 번거롭고 주관적인 과정이다.
    2. 본 논문에서는 LLM에 제공되는 명령어의 품질을 자동으로 향상시키는 새로운 방법인 Auto-Instruct를 소개한다. 이 방법은 LLM의 생성 능력을 활용하여 주어진 작업에 대해 다양한 후보 명령어를 생성하고, 575개의 기존 NLP 작업을 사용하여 훈련된 점수 모델을 사용하여 순위를 매긴다.
    3. 118개의 비 관련 작업에 대한 실험에서, Auto-Instruct가 사람이 작성한 명령어와 기존 LLM 생성 명령어에 비해 뛰어나며, 훈련 과정에 통합되지 않은 다른 LLM에 대해서도 주목할만한 일반화 능력을 보인다.

###### DiffuSeq-v2: Bridging Discrete and Continuous Text Spaces for Accelerated Seq2Seq Diffusion Models (https://aclanthology.org/2023.findings-emnlp.660/)
- Anthology ID: 2023.findings-emnlp.660 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Diffusion 모델은 고품질의 텍스트 시퀀스를 생성하는 데 중요한 역할을 한다. 그러나 현재의 방법은 주로 연속적인 diffusion 공간에서 이산적인 텍스트를 나타내는데, 이로 인해 훈련 중에 상당한 계산 오버헤드가 발생하고 샘플링 속도가 느려진다. 이 논문에서는 이산적인 변이를 재구성하는 데 도움이 되는 소프트 흡수 상태를 도입하여 diffusion 모델이 기반이 되는 가우시안 공간을 기반으로 학습을 강화하고 조건부 신호를 복원하는 능력을 향상시킨다."
    2. "샘플링 단계에서는 최신 ODE 솔버를 사용하여 연속적인 공간에서 샘플링 과정을 가속화한다. 포괄적인 실험 평가 결과, 우리의 제안된 방법은 훈련 수렴 속도를 4배 빠르게하며, 같은 품질의 샘플을 800배 더 빠르게 생성하여 실제 적용에 크게 다가갈 수 있도록 한다."

###### M2C: Towards Automatic Multimodal Manga Complement (https://aclanthology.org/2023.findings-emnlp.661/)
- Anthology ID: 2023.findings-emnlp.661 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 멀티모달 만화 분석은 시각적 특징과 텍스트 특징을 통해 만화 이해를 개선하는데 초점을 맞추고 있으며, 이는 자연어 처리와 컴퓨터 비전 커뮤니티 모두에서 큰 주목을 받고 있다.
    2. 현재 대부분의 만화는 손으로 그리고, 누락된 페이지, 텍스트 오염, 텍스트 나이 등의 문제가 발생하여 만화 텍스트 내용이 누락되고 인간의 이해를 심각하게 방해하는 문제가 있다.
    3. 이 논문에서는 비전과 언어 이해를 위한 공유 의미 공간을 제공함으로써 이러한 문제를 해결하는 멀티모달 만화 보완(M2C) 과제를 제안하고, MCoT라는 만화 인식 방법과 FVP-M2라는 효과적인 베이스라인 방법을 설계한 후, 대규모 다국어 데이터셋을 이용한 실험을 통해 FVP-M2의 효과를 입증하였다.

###### Learn Your Tokens: Word-Pooled Tokenization for Language Modeling (https://aclanthology.org/2023.findings-emnlp.662/)
- Anthology ID: 2023.findings-emnlp.662 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 모델은 일반적으로 문자들을 결합하여 'ing'과 같은 긴 표면 문자열 또는 완전한 단어로 구성하는 결정론적이고 수동형 휴리스틱 방식으로 텍스트를 서브워드로 토큰화한다. 기존 토큰화 전략의 한계점이 특히 영어 이외의 언어로 작성된 문서와 숫자 표현에 대해 반복적으로 확인되었다.
    2. 본 논문에서는 '자신만의 토큰 학습' 방법을 고려하여 단어 경계를 활용하여 바이트/문자를 단어 표현으로 결합하고, 이 표현을 넣고 기본 언어 모델에 다시 개별 문자/바이트를 병렬적으로 디코딩하는 방식을 제안한다.
    3. 실험 결과, 우리의 중간 표현의 토크나이저는 인쇄된 언어 모델링 메트릭인 다음 단어 예측에서 서브워드 및 바이트/문자 모델보다 300% 이상의 성능을 보이며, 특히 희귀한 단어에서는 30배 이상의 성능을 보인다고 밝혀졌다.

###### Towards Detecting Contextual Real-Time Toxicity for In-Game Chat (https://aclanthology.org/2023.findings-emnlp.663/)
- Anthology ID: 2023.findings-emnlp.663 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실시간 독성 감지는 소셜 미디어와 게임 플랫폼의 증가로 인해 큰 도전이다. 우리는 ToxBuster라는 간단하고 확장 가능한 모델을 제시하며, 이 모델은 대화 내용과 메타데이터를 포함하여 실시간으로 독성 콘텐츠를 신뢰할 수 있게 감지한다. 
    2. ToxBuster는 Rainbow Six Siege, For Honor, DOTA 2를 포괄하는 인기 멀티플레이어 게임에서 기존 독성 모델보다 일관되게 우수한 결과를 보여준다. 
    3. 우리는 각 모델 구성 요소의 중요성을 평가하고 데이터셋 간의 ToxBuster의 전이성을 탐색하기 위해 연구를 수행했다. 또한, 우리는 ToxBuster가 게임 후 모더레이션에서 효과적이며, 90.0% 수준의 정확도로 82.1%의 채팅 신고된 플레이어를 탐지하는 것을 보여준다. 추가로, 신고되지 않은 독성 플레이어의 6%를 사전적으로 제한할 수 있는 방법도 제시한다.

###### JWSign: A Highly Multilingual Corpus of Bible Translations for more Diversity in Sign Language Processing (https://aclanthology.org/2023.findings-emnlp.664/)
- Anthology ID: 2023.findings-emnlp.664 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수화 처리의 진보는 충분한 데이터의 부족으로 막혀, 인식, 번역 및 제작 작업의 발전이 방지되고 있다. 
    2. 우리는 수화 번역을 위한 새로운 대규모 다국어 데이터셋인 JWSign을 소개한다. 이 데이터셋은 98개의 수화 언어로 된 2,530 시간의 성경 번역을 포함하며, 1,500명 이상의 개별 수화사가 참여했다.
    3. 우리의 실험은 다국어 시스템이 양언 언어 기준 모델보다 뛰어나며, 고자원 시나리오에서 관련된 언어로 언어 쌍을 클러스터링하면 번역 품질이 향상됨을 보여준다.

###### Do Stochastic Parrots have Feelings Too? Improving Neural Detection of Synthetic Text via Emotion Recognition (https://aclanthology.org/2023.findings-emnlp.665/)
- Anthology ID: 2023.findings-emnlp.665 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "최근 발전된 생성 AI 기술은 고성능의 합성 텍스트 생성 기술에 초점을 맞추고 있다. 이제 이러한 모델이 광범위하게 이용 가능하고 사용이 용이해졌으므로 합성 텍스트를 인식할 수 있는 동등한 강력한 기술을 제공하는 것이 긴요하다."
    2. "우리는 심리학적 연구에서 영감을 받아 사람들이 감정에 영향을 받고 글을 쓸 때 감정을 담을 수 있다는 것을 제안하였다."
    3. "우리의 연구 결과는 우리의 감정인식 기반의 합성 텍스트 감지기가 다양한 합성 텍스트 생성기, 모델 크기, 데이터셋 및 도메인에서 시사하는 개선을 달성하였으며, ChatGPT와 비교했을 때도 상당한 성과를 나타내어 감정이 합성 텍스트를 식별하는 신호로 높은 잠재력을 보여주었다."

###### Variator: Accelerating Pre-trained Models with Plug-and-Play Compression Modules (https://aclanthology.org/2023.findings-emnlp.666/)
- Anthology ID: 2023.findings-emnlp.666 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large language model, LLM)는 NLP 태스크에서 놀라운 결과를 보여주었지만, 매우 큰 파라미터 크기와 이로 인한 계산 비용이 문제가 되었다. 
    2. 이 논문에서는 Variator라는 파라미터 효율적인 가속 방법을 제안하는데, compressible 플러그인을 사용하여 계산 효율성을 향상시킨다. 
    3. Variator는 53%의 계산 비용을 절약할 수 있으며, 성능 저하는 2% 미만이며, 수십억 개의 파라미터로 확장될 때 압축되지 않은 LLM의 강력한 성능을 보인다.

###### PivotFEC: Enhancing Few-shot Factual Error Correction with a Pivot Task Approach using Large Language Models (https://aclanthology.org/2023.findings-emnlp.667/)
- Anthology ID: 2023.findings-emnlp.667 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Factual Error Correction (FEC)은 성의 없는 주장을 수정하여 지원하는 증거와 더 정확하게 일치시키는 것을 목표로한다. 그러나 거짓 주장과 그에 대한 수정 내용을 포함하는 데이터셋 부족으로 인해 이 분야의 발전이 지연되고 있다.
    2. 기존의 method들은 오류를 식별하는게 어렵기 때문에, 잘못된 에러 마스킹 문제 등 문제점이 발생한다. 이러한 도전을 극복하기 위해, 우리는 PivotFEC이라는 새로운 방법을 제안한다.
    3. PivotFEC은 대형 언어 모델을 활용하여 몇 가지 표본과 함께 FEC를 향상시키는 pivot task 접근 방식을 적용한다. PivotFEC은 널리 사용되는 SARI 메트릭을 개선하고, FEC에 직접적으로 LLM을 사용한 few-shot 대안보다 7.9 점 높은 SARI로 성능을 향상시키는 것을 실험을 통해 입증한다.

###### Semantic Similarity Covariance Matrix Shrinkage (https://aclanthology.org/2023.findings-emnlp.668/)
- Anthology ID: 2023.findings-emnlp.668 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 금융 응용프로그램, 특히 포트폴리오 최적화에는 공분산 행렬의 정확한 추정이 필수적이다. 그러나 변수의 수와 관측치의 수가 비슷하거나 적을 때 샘플 공분산은 차원의 저주 문제(dimensionality curse)를 겪는다.
    2. 이 문제를 해결하기 위해 이전 작업에서는 추정된 행렬을 정규화하기 위해 선형 공분산 shrinkage를 제안했다. 하지만 제안된 방법들은 오로지 과거 가격 데이터만을 사용하여 기업의 기본 데이터를 무시한다.
    3. 본 논문에서는 텍스트 설명이나 지식 그래프에서 파생된 의미적 유사성을 활용하여 공분산 추정을 개선하기를 제안한다. 의미적 유사성을 정확한 추정자(biased estimator)로 사용하는 대신 수축(shrinkage) 대상으로 활용한다. 결과적으로 얻어지는 공분산 추정기는 의미적 유사성과 최근 가격 이력을 모두 활용하며, 다양한 금융 자산에 적용할 수 있다. 이 접근 방식의 효과는 다양한 시장 조건을 포함하는 기간에 대해 증명되었으며, 기존의 공분산 shrinkage 기법과 비교되었다.

###### LLM-in-the-loop: Leveraging Large Language Model for Thematic Analysis (https://aclanthology.org/2023.findings-emnlp.669/)
- Anthology ID: 2023.findings-emnlp.669 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 주제 분석(Thematic analysis, TA)은 많은 학문 분야에서 질적 데이터를 분석하는 데 널리 활용되고 있다. 그러나 신뢰할 수 있는 분석을 위해 동일한 데이터를 최소 두 명의 인간 코더에게 할당하는 것은 일반적이다. 
    2. 이 논문은 큰 언어 모델(Large Language Model, LLM)을 활용하여 TA를 수행하는 인간-LLM 협업 프레임워크를 제안하였다. 이 프레임워크는 LLM과의 상호작용을 통해 논의를 구성하고 TA를 위한 최종 코드북을 생성한다.
    3. 이 프레임워크는 음악 청취 경험과 비밀번호 관리자 사용과 같은 설문 데이터를 사용하여 유용성을 입증하였으며, 결과적으로 인간 코더의 분석 품질을 유지한 채 TA의 노동량과 시간을 줄일 수 있다.

###### LLM aided semi-supervision for efficient Extractive Dialog Summarization (https://aclanthology.org/2023.findings-emnlp.670/)
- Anthology ID: 2023.findings-emnlp.670 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 형식에서 요약을 생성하는 경우, 대규모 라벨이 부여된 데이터셋이 필요하다. 이 논문에서는 라벨이 없는 데이터를 효율적으로 사용하여 고객-에이전트 대화의 추출 요약을 수행하는 방법을 제안한다.
    2. 먼저 요약을 질문-답변 문제로 정의하고, 대화에 대한 가짜 라벨을 대량의 언어 모델을 사용하여 생성한다. 그런 다음 이러한 가짜 라벨을 사용하여 대화 요약 모델을 미세 조정하여 대량의 언어 모델의 지식을 작은 전문 모델로 전달한다.
    3. 실험 결과로 TWEETSUMM 데이터셋에 대해 10%의 라벨이 달린 원본 데이터를 사용하여 ROUGE-1/-2/-L 값이 각각 65.9/57.0/61.0을 달성할 수 있었다. 전체 훈련 데이터셋에 대해 훈련된 최첨단 모델은 ROUGE-1/-2/-L에 각각 65.16/55.81/64.37를 달성하는데, 즉 최악의 경우(ROUGE-L)에도 10%의 데이터만 사용하여 성능을 94.7% 효과적으로 유지하는 것을 확인했다.

###### Investigating Multilingual Coreference Resolution by Universal Annotations (https://aclanthology.org/2023.findings-emnlp.671/)
- Anthology ID: 2023.findings-emnlp.671 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 핵심 지시어 해결(MCR)은 오랜 기간 동안 도전적인 작업이었다. 이 논문에서는 새로운 다국어 핵심 지시어 데이터 셋인 CorefUD를 사용하여 핵심 지시어 작업에 대해 조사한다.
    2. 우선, 언어 수준에서 다양한 말, 개체 및 문서 수준의 데이터를 조사하여 여러 언어에서 핵심 지시어의 특성을 파악한다.
    3. 또한, CRAC 2022 공유 작업에서 고도의 힘들다고 평가된 문제들을 유니버설 어노테이션을 사용하여 오류 분석하고, 이 분석을 기반으로 유니버설 형태-통사론 어노테이션에서 특징을 추출하여 MCR 작업에 대한 잠재적 이점을 평가한다.

###### FactSpotter: Evaluating the Factual Faithfulness of Graph-to-Text Generation (https://aclanthology.org/2023.findings-emnlp.672/)
- Anthology ID: 2023.findings-emnlp.672 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 그래프를 입력받아 그래프 안의 정보에 대한 자연스럽고 충실한 텍스트로 변환하는 Graph-to-Text(G2T) 생성은 대화 생성, 질문응답 등 다양한 응용 분야가 있다. 
    2. 기존 데이터셋에 대해서 G2T 생성 문제가 어느 정도 해결되었는지와 제안된 메트릭이 생성된 텍스트를 비교할 때 어떻게 작동하는지를 조사한다. 
    3. 이 논문에서는 사실적 충실성(factual faithfulness)을 올바르게 인식하는 새로운 메트릭 FactSpotter를 제안하여 데이터 정확성, 데이터 커버리지, 일치성 등에 대한 인간 주석과 가장 높은 상관관계를 보여준다.

###### LayoutDIT: Layout-Aware End-to-End Document Image Translation with Multi-Step Conductive Decoder (https://aclanthology.org/2023.findings-emnlp.673/)
- Anthology ID: 2023.findings-emnlp.673 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이미지 안의 텍스트를 한 언어에서 다른 언어로 번역하는 Document Image Translation (DIT)은 시각적 레이아웃과 텍스트 의미를 동시에 이해해야 하는 어려운 과제이다. 그러나 기존 방법들은 실제 복잡한 문서 이미지에서 중요한 시각적 레이아웃을 포착하기 어려워한다.
    2. 논문에서는 DIT에 시각적 레이아웃 지식을 최초로 end-to-end 방식으로 통합하는 시도를 한다. 레이아웃을 고려한 인코더와 다단계의 conductive 디코더를 사용하여 문서 번역을 순차적으로 단계별로 수행한다.
    3. 실험 결과, LayoutDIT는 기존 방법들보다 더 나은 parameter efficiency와 함께 우수한 일반화 성능을 보여준다. 또한 다양하고 복잡한 레이아웃 환경에서도 좋은 일반화 능력을 갖고 있다는 것을 검증하기 위해 새로운 다중 도메인 문서 이미지 번역 데이터셋을 제작하였다.

###### Balaur: Language Model Pretraining with Lexical Semantic Relations (https://aclanthology.org/2023.findings-emnlp.674/)
- Anthology ID: 2023.findings-emnlp.674 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의미적 관계 (LSR)는 단어들 간의 의미적인 관계를 특징짓고 어휘 추론 태스크에서 체계적인 일반화에 중요한 역할을 한다. 
    2. 기존의 사전 훈련 언어 모델 (LMs)은 hypernymy의 지식이 필요한 여러 태스크에서 여전히 어려움을 겪고 있으며, LSR의 언어적 행동과의 일치를 더 잘하기 위해 개선이 필요하다. 
    3. 이 논문에서는 모델이 사전 훈련 과정에서 LSR을 직접적으로 모델링하여 이 도전에 대처하는 Balaur 모델을 제안한다.

###### Exploring In-Context Learning for Knowledge Grounded Dialog Generation (https://aclanthology.org/2023.findings-emnlp.675/)
- Anthology ID: 2023.findings-emnlp.675 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 생성 모델은 현실적인 시나리오에서 널리 쓰이지만, 환각과 사실적으로 부정확한 출력을 생성하는 경향이 있어 큰 우려를 불러일으킨다. 이를 해결하기 위해 우리는 IKA라는 플러그 앤 플레이 검색 기반 프레임워크를 제안하며, 이는 인과 관계를 기반으로한 지식 대화 생성을 위해 인콘텍스트 학습과 검색 기술을 활용한다.
    2. 우리는 1백만 가지 이상의 사실을 포함하는 대규모 지식 그래프를 사용하여 우리의 프레임워크의 효과와 일반화 능력을 조사하기 위해 철저한 실험을 설계했다.
    3. 실험 결과, 우리의 방법은 이전의 훈련 기반 최고 성능을 큰 폭으로 개선하였으며, 특히 BLEU4에서 46.67%, ROUGE-L에서 26.01%, BARTScore에서 122.90%, 그리고 엔터티 커버리지 F1에서 30.50%의 성능 향상을 보였다. 추가적인 분석은 LLM이 지식탄력적인 작업을 수행하는 능력을 보여주었고, 이는 이전에 약하고 잘 연구되지 않았던 부분이다.

###### Towards Enhancing Relational Rules for Knowledge Graph Link Prediction (https://aclanthology.org/2023.findings-emnlp.676/)
- Anthology ID: 2023.findings-emnlp.676 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프 추론에 대한 GNN 모델인 PRGNN은 관계 규칙을 이용해 관계형 다이그래프에서 누락된 지식을 추론하고, 상당한 성능을 보였다. 그러나 PRGNN의 추론 과정에서 순차적 관계 조합과 정보 전파 속도의 차이 등 두 가지 중요한 특성이 간과되어 관계 규칙 학습의 정확도가 저하된다.
    2. 따라서 이 문제를 해결하기 위해, 우리는 새로운 지식 그래프 추론 방법인 RUN-GNN을 제안한다. RUN-GNN은 순차적 관계 조합을 모델링하기 위한 쿼리 관련 퓨전 게이트 유닛과 정보 전파 지연의 부정적인 영향을 완화하기 위한 버퍼링 업데이트 메커니즘을 사용하여 관계 규칙 학습의 품질을 향상시킨다.
    3. 다양한 데이터셋에서의 실험 결과, RUN-GNN이 전이적 및 귀납적 링크 예측 작업에서 우수한 성능을 보였음을 확인할 수 있다.

###### Are NLP Models Good at Tracing Thoughts: An Overview of Narrative Understanding (https://aclanthology.org/2023.findings-emnlp.677/)
- Anthology ID: 2023.findings-emnlp.677 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. narrative understanding은 작가의 인지 과정을 이해하는 것으로, 글의 문법적 일관성을 유지하는 것 이외에 작가의 사고를 이해하는 능력이 매우 제한적이다.
    2. 본 논문에서는 narrative understanding 태스크에 대한 종합적인 조사를 진행하고, 그들의 특징, 정의, 분류, 관련 데이터셋, 훈련 목표, 평가 지표 및 제한 사항에 대해 상세히 조사한다.
    3. 또한, 우리는 모듈화된 큰 언어 모델이 새로운 narrative understanding 태스크를 해결하기 위한 잠재력을 탐구하며, narrative 이해를 향상시키기 위한 새로운 관점을 제시한다.

###### Who is Speaking? Speaker-Aware Multiparty Dialogue Act Classification (https://aclanthology.org/2023.findings-emnlp.678/)
- Anthology ID: 2023.findings-emnlp.678 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화에서 발화는 독립적으로 발생하지 않으며 발화자가 누구인지에 대한 정보를 가져야 주변 문맥을 통해 발화자의 의도를 파악할 수 있다. 이 논문에서는 발화자의 인식을 각 발화 표현에 명시적으로 추가하고, 발화자가 대화 내에서 어떻게 상호작용하는지를 모델링하는 그래프 신경망을 사용하여 발화자 표현을 학습한다. 
    2. 이를 통해 발화자 표현을 사용하여 대화 표현을 업데이트하고, MRDA와 SwDA 데이터셋에서 여러 인터락터가 참여하는 대화와 이중 대화에 대해 실험을 진행하고, 우리의 접근법의 효과를 보여준다.
    3. 다중 참여자 대화에서 대화 흐름을 이해하는 데 발화자 인식이 중요한 역할을 하며, 그래프 신경망을 사용한 발화자 모델링은 이를 성공적으로 해결할 수 있는 효과적인 방법이다.

###### Demystifying Prompts in Language Models via Perplexity Estimation (https://aclanthology.org/2023.findings-emnlp.679/)
- Anthology ID: 2023.findings-emnlp.679 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "언어 모델은 zero-shot과 few-shot in-context learning으로 다양한 작업을 수행할 수 있다. 그러나 성능은 프롬프트의 선택에 따라 크게 달라지고, 그 이유를 아직 이해하지 못하고 있다."
    2. "우리는 이 논문에서 이러한 변동성에 기여하는 요소들에 대해 분석하고, 새로운 경험적 가설을 수립한다: 프롬프트의 성능은 모델이 그 언어에 익숙한 정도에 따라 예측된다."
    3. "우리는 다양한 작업들을 통해, 합리적인 프롬프트에 대해 관련이 있는 경우, 프롬프트의 퍼플렉서티가 낮을수록 작업을 더 잘 수행할 수 있다는 것을 보여준다."

###### C2D2 Dataset: A Resource for the Cognitive Distortion Analysis and Its Impact on Mental Health (https://aclanthology.org/2023.findings-emnlp.680/)
- Anthology ID: 2023.findings-emnlp.680 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인식 왜곡(Cognitive distortions)은 비이성적인 사고의 패턴으로, 현실의 왜곡된 인식과 정신 건강 문제로 이어질 수 있다. 
    2. 이 논문에서는 첫 번째 전문가 지도 중국어 "Cognitive Distortion Dataset"을 소개하며, 일상생활에서 7,500개의 인식 왜곡에 대한 감상을 담고 있다. 
    3. 또한, 정신장애 진단을 받은 개인들이 공유한 소셜 미디어 텍스트에서도 인식 왜곡의 존재를 검토하여, 인식 왜곡과 정신건강 상태의 연관성을 제시한다.

###### MixEdit: Revisiting Data Augmentation and Beyond for Grammatical Error Correction (https://aclanthology.org/2023.findings-emnlp.681/)
- Anthology ID: 2023.findings-emnlp.681 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "데이터 부족 문제 해결을 위해 데이터 증강은 문법 오류 교정(GEC) 분야에서 효과적으로 입증되었다. 그러나 이러한 전략들이 효과적인 이유는 여전히 잘 이해되지 않았다."
    2. "따라서 이 연구에서는 데이터 증강이 GEC 모델을 어떻게 개선하는지 명확히 설명하고자 한다."
    3. "Affinity와 Diversity 두 개의 계산적으로 효율적인 척도를 도입하여 좋은 GEC 데이터 증강 전략이 모델 성능을 향상시킬 수 있음을 밝혀냈다."

###### CCEval: A Representative Evaluation Benchmark for the Chinese-centric Multilingual Machine Translation (https://aclanthology.org/2023.findings-emnlp.682/)
- Anthology ID: 2023.findings-emnlp.682 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 국제 비즈니스 개발과 문화 교류의 증가로 인해 중국 중심의 다국어 기계 번역의 중요성이 커졌으나, 이 분야의 발전을 제한하는 중요한 요소는 대표성과 품질이 높은 평가 벤치마크의 부족이다. 
    2. CCEval은 중립적이고 대표적인 중국 중심 다국어 기계 번역 평가 데이터셋으로 이 사각지대를 채우기 위해 소개되었다. 
    3. 이 데이터셋은 2500개의 중국어 문장으로 구성되어 있으며, 다른 다국어 기계 번역 평가 벤치마크보다 다양한 언어적 특징을 포함하고 있다고 주장한다.

###### ROME: Evaluating Pre-trained Vision-Language Models on Reasoning beyond Visual Common Sense (https://aclanthology.org/2023.findings-emnlp.683/)
- Anthology ID: 2023.findings-emnlp.683 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인류는 일반적인 상식을 넘어서는 추론 능력을 가지고 있다. 그러나 진행중인 비전-언어 모델은 비직관적인 시나리오에 대해서도 일반적인 상황을 선호하기 때문에 이런 능력을 가지지 못한다.
    2. 본 논문에서는 최신 사전 훈련된 비전-언어 모델이 비직관적인 콘텐츠를 올바르게 해석하는 추론 능력을 가지고 있는지 평가하기 위해 ROME라는 새로운 프로빙 데이터셋을 소개한다.
    3. 최신 사전 훈련된 비전-언어 모델 실험은 대부분 이러한 모델이 여전히 비직관적인 시나리오를 해석하는 능력이 크게 부족하다는 것을 보여준다. 이를 통해 ROME은 비전-언어 연구에서 일반적인 상식 지식을 넘어서는 추론 능력에 대한 추가적인 연구를 촉진할 것을 기대한다.

###### Automatic Analysis of Substantiation in Scientific Peer Reviews (https://aclanthology.org/2023.findings-emnlp.684/)
- Anthology ID: 2023.findings-emnlp.684 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 인공지능 학회에서 문제가 되는 동료 리뷰 문제가 증가함에 따라, 자동 품질 관리 방법이 긴요하게 필요합니다. 
    2. 이 논문에서는 품질 측면 중 하나인 '전증' 을 알고리즘으로 평가하기 위한 방법을 제안합니다. 
    3. 이를 위해 claim-evidence 쌍을 추출하기 위한 문제로 정의하고, 이 작업을 위한 첫 번째 주석이 달린 데이터 세트인 SubstanReview를 수집하고, 이 데이터를 기반으로 인수 광산 시스템을 훈련시킵니다.

###### Hierarchical Prompting Assists Large Language Model on Web Navigation (https://aclanthology.org/2023.findings-emnlp.685/)
- Anthology ID: 2023.findings-emnlp.685 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)은 상호작용적 의사 결정에서 복잡한 관측을 처리하는 데 어려움을 겪는다. 이 문제를 완화하기 위해, 우리는 간단한 계층적 프롬프팅 접근법을 제안한다.
    2. 우리의 방법은 이전의 프롬프팅 접근법과 다르게 항상 전체 관측 자료(웹 페이지)를 프롬프트에 넣는 대신 별도의 Summarizer 프롬프트와 관련성이 높은 액션-다방향 관측을 먼저 구축하는 것을 제안한다.
    3. 우리의 방법은 웹 탐색과 같이 전체 관찰에는 중복되고 관련 없는 정보가 많은 복잡한 도메인에서 뛰어난 성과를 보여준다. 우리의 접근법은 동일한 LLM을 기반으로 한 이전의 최첨단 프롬프팅 메커니즘보다 작업 성공률에서 6.2%의 향상을 보여주며, 긴 관측 트레이스를 가진 상호작용적 의사 결정 과제에서의 잠재력을 보여준다.

###### Can Large Language Models Fix Data Annotation Errors? An Empirical Study Using Debatepedia for Query-Focused Text Summarization (https://aclanthology.org/2023.findings-emnlp.686/)
- Anthology ID: 2023.findings-emnlp.686 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Debatepedia는 논란이 있는 주제에 대한 주장과 반대 주장으로 이루어진 공개 데이터셋으로, 최근 단일 문서 질의 중심의 의미 요약 작업에 널리 사용되고 있다. 그러나 최근 이 데이터셋은 noise에 의해 제한되고 있으며, 대부분의 질의는 해당 문서와 관련이 없다는 것이 밝혀졌다.
    2. 본 연구에서는 대규모 언어 모델 (large language models, LLMs)이 Debatepedia 데이터셋을 정제하는 데 사용될 수 있는지 조사한다. ChatGPT와 PaLM이라는 두 개의 LLM의 언어 생성 능력을 활용하여 쿼리를 재생성한다.
    3. 실험 결과, 쿼리 교정에 있어서 대규모 언어 모델에만 의존하는 것은 데이터 정제에 그다지 유용하지 않을 수 있다는 것을 발견했다. 그러나 룰 기반 접근법을 활용하여 데이터 샘플링을 한 다음 LLMs (특히 ChatGPT)를 사용하여 재생성할 경우, 보다 일반적인 쿼리 중심 텍스트 요약 모델의 개발에 적합한 더 우수한 품질의 데이터셋을 얻을 수 있다는 것을 관찰했다.

###### TSTR: Target Similarity Tuning Meets the Real World (https://aclanthology.org/2023.findings-emnlp.687/)
- Anthology ID: 2023.findings-emnlp.687 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Target similarity tuning (TST)은 대형 언어 모델을 통해 자연어에서 코드 생성으로 관련 예제를 선택하여 성능을 향상시키는 방법이다. 이 논문에서는 실제 세계에서 TST를 적용하고 개선하기 위한 다양한 방법을 제안한다.
    2. 우리는 문장 변형기 (sentence transformer)를 더 큰 모델의 임베딩으로 대체하여 언어 분포에 대한 민감도를 줄이고, 합성적 예제 생성에 더 많은 유연성을 제공한다. 또한, 이러한 임베딩을 코드 유사성과 일치하도록 변환하는 작은 모델을 훈련시켜, 모델이 블랙 박스로 남아 있고 추론 시간에서 몇 가지 행렬 곱셈만 필요하도록 한다.
    3. 마지막으로, TST 모델을 훈련시키기 위해 효율적으로 작은 수의 훈련 예제를 선택하는 방법과 코드 생성 실험 없이도 TST를 평가하는 랭킹 기반 평가 방법을 도입한다.

###### RealBehavior: A Framework for Faithfully Characterizing Foundation Models’ Human-like Behavior Mechanisms (https://aclanthology.org/2023.findings-emnlp.688/)
- Anthology ID: 2023.findings-emnlp.688 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간과 유사한 행동을 파악하기 위해 심리학적 이론을 사용하는 연구가 증가하고 있으나, 이러한 이론의 결과의 충실성을 검증하지 않고 직접적으로 적용하는 경향이 있다. 
    2. 이 논문에서는 RealBehavior라는 프레임워크를 소개하여 모델의 인간형 행동을 충실하게 특성화하는 방법을 제안한다. 
    3. 우리의 연구 결과는 심리학적 도구의 단순한 적용이 모든 인간형 행동을 충실하게 특성화할 수 없음을 시사하며, 모델을 인간과 사회적 가치와 조화되게 정렬하는 영향과 제한된 특성을 갖는 모델의 생성을 방지하기 위해 다양한 정렬 목표의 필요성을 논의한다.

###### Unraveling Downstream Gender Bias from Large Language Models: A Study on AI Educational Writing Assistance (https://aclanthology.org/2023.findings-emnlp.689/)
- Anthology ID: 2023.findings-emnlp.689 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(LLM)은 학생들에게 작문 제안을 제공하는 등 교육적인 과제에 점점 더 활용되고 있다. 하지만, LLM에는 학습자에게 부정적인 영향을 줄 수 있는 내재적인 편향이 존재한다. 이 논문에서는 LLM의 편향이 인간의 작문에 어떻게 영향을 미치는지 조사하였다.
    2. 231명의 학생들이 회사 사례 피어 리뷰를 작성하도록 한 대규모 사용자 연구를 수행하였고, 작문 지원의 다양한 단계에서 성향 편향을 평가하였다. 결과적으로, LLM 제안이 있는 그룹과 없는 그룹 간에 성향 편향에는 유의미한 차이가 없는 것으로 나타났다.
    3. 이 연구는 LLM의 편향이 학생들의 작문에 영향을 미치지 않는 환경에서 AI 작문 지원의 사용에 대해 낙관적인 결과를 제시하고 있다.

###### VERVE: Template-based ReflectiVE Rewriting for MotiVational IntErviewing (https://aclanthology.org/2023.findings-emnlp.690/)
- Anthology ID: 2023.findings-emnlp.690 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 교단의 학습 평가 시간을 줄일 수 있는 자동 MCQ 생성 기능 있으나, 현재의 평가 방법은 교육적 가치를 고려하지 않고 다만 단어의 유사성만 고려한다.
    2. 우리는 지식 종속 가능성(KDA)를 활용한 새로운 자동 평가 메트릭을 제안하고 MCQ의 대답 가능성(answerability) 및 대상 사실에 대한 학생의 지식을 평가한다.
    3. 인간 평가 결과를 통해 우리의 방법이 실제 교실 환경에서 효과적이며, KDA_disc와 KDA_cont가 높은 상관관계를 가지고 있음을 보여주었다.
    
    
    1. 최근까지 NLP 작업에서 모델의 정확성이 인간을 뛰어넘는 수준이지만, spurious pattern에 의존하는 한계로 robustness가 제한된다고 알려져 있다.
    2. 이 논문은 contrastive learning과 counterfactual augmentation을 이용하여 강건성을 높이기 위한 연구를 진행한다.
    3. 다양한 실험 결과를 통해 우리의 접근 방식이 기존에 단어 기반 합성에 영향을 받는 bias에 덜 민감하며, 많은 개선을 이루었다고 보여진다. (1. counterfactual robustness, 2. cross-domain generalization, 3. generalization from scarce data)
    
    
    1. 상담사는 motivational interviewing (MI)에서 전문성을 갖기 위해 reflective listening이라는 기본 기술을 습득해야 한다.
    2. 이 논문은 상담 응답 재작성을 소개하며, 비반사적인 발언을 반사적인 응답으로 변환한다.
    3. VERVE라는 템플릿 기반의 재작성 시스템을 소개하며, 매개 훈련 및 적응형 템플릿 업데이트를 활용하여 비반사적인 문장을 반사적인 응답으로 변환하는 방법을 제안한다.

###### Self-Knowledge Guided Retrieval Augmentation for Large Language Models (https://aclanthology.org/2023.findings-emnlp.691/)
- Anthology ID: 2023.findings-emnlp.691 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 과제별 세부 조정 없이 뛰어난 성능을 보였으나, 그 모델 매개 변수에 저장된 지식은 여전히 완전하지 않고 계산 비용이 큰 관계로 업데이트하기 어렵다.
    2. 해당 논문은 내부 지식과 외부 세계 지식을 모두 적절하게 활용하기 위해 모델이 스스로 알고 있는 것과 모르는 것을 인식하도록 하는 "self-knowledge"를 탐구하고, 새로운 질문을 다룰 때 이전에 겪었던 질문을 참조하고 적응적으로 외부 자원을 호출할 수 있는 간단하면서도 효과적인 방법인 Self-Knowledge guided Retrieval augmentation (SKR)을 제안한다.
    3. SKR은 InstructGPT 또는 ChatGPT를 사용하여 다양한 데이터셋에 대해 평가되었으며, 이를 통해 기존의 chain-of-thought 및 완전 검색 기반 방법보다 우수한 성능을 보여준다.

###### Pretraining Language Models with Text-Attributed Heterogeneous Graphs (https://aclanthology.org/2023.findings-emnlp.692/)
- Anthology ID: 2023.findings-emnlp.692 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 여러 현실 세계 시나리오에서 (예 : 학술 네트워크, 소셜 플랫폼) 다른 유형의 개체는 텍스트와 연결 관계로 연결되어 있는데, 해당될 수 있는 것은 텍스트 속성이 있는 이질적인 그래프로 추상화될 수 있다. 이 논문에서는 이러한 이질적인 그래프의 네트워크 연결 관계를 명시적으로 고려하는 언어 모델을 위한 새로운 사전학습 프레임워크를 제안한다.
    2. 우리는 첫째로, 특정한 순서 내에서 대상 노드의 이웃을 컨텍스트 그래프로 정의하고, 언어 모델과 보조 이질적 그래프 신경망을 동시에 최적화하여 컨텍스트 그래프에 관련된 노드를 예측하기 위한 topology-aware 사전학습 작업을 제안한다.
    3. 둘째로, 텍스트-순한 노드는 다른 노드보다 텍스트가 적을 수 있으므로, 불균형 문제를 처리하기 위해 이웃의 텍스트 정보로 텍스트가 부족한 노드를 보완하는 텍스트 보강 전략을 개발하였다.

###### CReTIHC: Designing Causal Reasoning Tasks about Temporal Interventions and Hallucinated Confoundings (https://aclanthology.org/2023.findings-emnlp.693/)
- Anthology ID: 2023.findings-emnlp.693 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large language models, LLMs)은 자연어 처리에서 인상적인 역량을 보여주었으나, 시간적 개입과 언어 환시에 대한 인과관계 수립 능력은 여전히 어렵다.
    2. 이 논문은 LLM의 인과 추론 능력을 테스트하고 향상시키기 위해 고안된 CReTIHC 데이터셋을 제시한다.
    3. CReTIHC 데이터셋은 기존 인과 추론 데이터셋을 재공학하여 말의 환시와 시간적 개입 요소를 포함한 복잡한 시나리오를 생성하여 LLM이 정보를 비판적으로 평가하고 인과관계를 식별할 수 있도록 한다.

###### On the Dimensionality of Sentence Embeddings (https://aclanthology.org/2023.findings-emnlp.694/)
- Anthology ID: 2023.findings-emnlp.694 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문장 embedding의 차원에 대한 이해는 한정되어 있으나, 이 논문은 optimal한 차원이 기본 값보다 작을 수 있다는 것을 보여준다.
    2. 성능 저하 없이 문장 embedding의 차원을 압축하기 위해, encoder와 pooler의 성능 저하를 식별하고, 이 성능 저하를 완화하기 위해 두 단계의 학습 방법을 제안한다.
    3. 7개의 STS 태스크와 7개의 문장 분류 태스크에서 실험 결과, 우리의 방법은 저차원 문장 embedding의 성능을 크게 향상시킨다.

###### Pit One Against Many: Leveraging Attention-head Embeddings for Parameter-efficient Multi-head Attention (https://aclanthology.org/2023.findings-emnlp.695/)
- Anthology ID: 2023.findings-emnlp.695 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델의 스케일링은 자연 언어 처리 작업에서 큰 성능 향상을 가져왔지만, 메모리 요구량이 매우 크다. 이 논문에서는 트랜스포머의 위치 임베딩에서 영감을 받아, 멀티 헤드 어텐션 (MHA) 메커니즘의 메모리 풋프린트를 단순화하고 줄이기 위한 대안 모듈을 제안한다.
    2. 제안된 MHE 어텐션은 다른 어텐션 메커니즘에 비해 훨씬 더 메모리 효율적이며, 다양한 하위 작업에서 기존의 MHA에 비해 높은 예측 성능 보존 비율을 달성한다.
    3. MHE 어텐션은 단일 헤드 어텐션에 비해 추가 매개변수의 무시할 만한 분수만 필요로 하며, MHA는 추가적인 매개변수를 (3n2-3n)d2-3nd만큼 필요로 한다.

###### Entity-Based Evaluation of Political Bias in Automatic Summarization (https://aclanthology.org/2023.findings-emnlp.696/)
- Anthology ID: 2023.findings-emnlp.696 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 시스템은 사회적 편견을 인코딩할 수 있다는 연구가 많이 있으나, 대표적인 정치적 편견에 대한 요약 모델의 지식은 여전히 부족하다.
    2. 우리는 entity replacement 방법을 사용하여 자동 생성된 뉴스 기사 요약에서 정치인들의 표현을 조사했다.
    3. 우리는 몇 가지 추출적 및 추상적 요약 모델의 Donald Trump과 Joe Biden에 대한 민감도를 평가하는 entity-based computational framework을 개발했고, 특히 사용된 요약에서 entity가 중요한 역할을 할 때 이러한 편견을 발견했다.

###### StyleBART: Decorate Pretrained Model with Style Adapters for Unsupervised Stylistic Headline Generation (https://aclanthology.org/2023.findings-emnlp.697/)
- Anthology ID: 2023.findings-emnlp.697 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 스타일리스트 헤드라인 생성은 기사의 내용을 요약하면서 사용자를 끌어들일 원하는 스타일을 반영하는 헤드라인을 생성하는 과제이다. 
    2. 이 연구에서는 스타일리스트 헤드라인 생성을 위한 비지도 학습 방법을 제안한다. 
    3. StyleBART는 사전 학습된 BART 모델에 어댑터를 사용하여 다양한 스타일로 헤드라인을 생성할 수 있도록 하고, 인버스 패러프레이징 작업을 통해 스타일 어댑터를 향상시킨다.

###### RSVP: Customer Intent Detection via Agent Response Contrastive and Generative Pre-Training (https://aclanthology.org/2023.findings-emnlp.698/)
- Anthology ID: 2023.findings-emnlp.698 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 고객 서비스의 대화 시스템은 사용자에게 정확한 답변과 상담원의 의도를 감지하여 상담원이 사용자의 의도에 맞게 응답하는 과업 지향 대화에서 동일환 데이터를 기반으로 사용자에게 24시간 동안 지원하는 역할을 수행하기 위해 신경망 모델을 통해 개발되었다. 
    2. 기존의 의도 감지 방법은 대규모 데이터셋을 사용하여 언어 모델을 사전학습하는 것에 과도한 의존성이 있는데, 이는 주요한 데이터 수집 비용으로 인해 우월함에 제약을 줄 수 있다. 또한, 고객의 의도에 중요한 응답에 대한 정보를 무시하는데, 이는 상담원이 응답을 고객의 의도에 맞게 조정해야 하는 역할을 수행하기 때문에 중요하다. 
    3. 본 논문에서는 의도 지향 대화를 위해 상담원의 응답을 사전학습하는 RSVP라는 자기 학습 프레임워크를 제안하였다. RSVP는 발화-응답 쌍의 관계를 포함하기 위해 두 단계로 사전학습을 수행하는 두 가지 사전학습 과제를 소개한다.

###### Improving Low-resource Question Answering by Augmenting Question Information (https://aclanthology.org/2023.findings-emnlp.699/)
- Anthology ID: 2023.findings-emnlp.699 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 모델 시대에서는 리소스가 제한된 질의응답 태스크의 성능이 떨어져 자연어처리에서 데이터 증강의 중요성이 강조된다.
    2. 우리는 Prompt Answer, Question Generation, Question Filter로 구성된 PQQ라는 혁신적인 질문 데이터 증강 방법을 소개하여 대형 모델의 내부 지식을 활용하고 질문, 문단, 답변 중 어떤 데이터 요소가 가장 많은 증강 이점을 얻을 수 있는지 결정하며 과도한 noise를 유발하지 않으면서 증강 내용의 일관성을 유지한다.
    3. 실험 결과, ChatGPT는 실험 데이터에서 성능이 저조하지만, 우리의 PQQ 방법은 기존 증강 전략을 뛰어넘는 성과를 보여주며, SQUAD1.1 및 TriviaQA와 같은 고리소스 QA 태스크에서 검증되었다.

