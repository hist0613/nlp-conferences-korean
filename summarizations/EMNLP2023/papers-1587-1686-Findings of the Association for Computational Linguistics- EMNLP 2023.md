# Korean Three-Line Summarizations of Papers 1587-1686 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Grammatical Error Correction via Mixed-Grained Weighted Training (https://aclanthology.org/2023.findings-emnlp.400/)
- Anthology ID: 2023.findings-emnlp.400 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문법 오류 수정(GEC)의 작업은 자연 텍스트에서 문법적인 오류를 자동으로 수정하는 것을 목표로 한다. 이전 연구들은 주석이 달린 훈련 데이터를 동등하게 처리하지만, 데이터의 내재적인 불일치를 무시한다.
    2. 따라서 우리는 MainGEC를 제안하는데, 이는 내재적인 불일치를 고려하여 토큰 수준과 문장 수준의 훈련 가중치를 설계하고, 혼합된 정도의 가중치 훈련을 수행하여 GEC의 훈련 효과를 향상시킨다.
    3. 실험 결과, Seq2Seq 또는 Seq2Edit 방식에서도 MainGEC는 두 가지 벤치마크 데이터셋에서 일관된 성능 향상을 이끌어 내며, 설계된 가중치의 효과를 검증하기 위한 추가 실험도 효과적임을 보여준다.

###### A Unified Framework for Synaesthesia Analysis (https://aclanthology.org/2023.findings-emnlp.401/)
- Anthology ID: 2023.findings-emnlp.401 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Synaesthesia"은 감각 운동을 다른 감각으로 표현하는 현상으로, 이는 언어적 현상 뿐만 아니라 인간의 사고와 행동을 구성하는 인지 현상으로 이해하기 어렵다. 
    2. 이 논문은 모든 종류의 Synaesthesia 요소를 주석으로 달고 그들 사이의 관계를 완전히 탐구하기 위한 통합 프레임워크를 제안한다. 
    3. 특히, 우리는 감각 운동뿐만 아니라 그들의 힌트와 자극을 포함한 새로운 주석 체계를 도입하여 Synaesthetic 정보를 효과적으로 이해할 수 있도록 한다.

###### Domain Private Transformers for Multi-Domain Dialog Systems (https://aclanthology.org/2023.findings-emnlp.402/)
- Anthology ID: 2023.findings-emnlp.402 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 일반적인 큰 규모의 언어 모델은 다양한 대화 도메인에서 인상적인 성능을 보이고 있다. 그러나 다양한 도메인에 대한 출력을 보장할 수 없으므로 도메인 따른 개인 정보 보호 방법인 "도메인 프라이버시"를 제안한다.
    2. 토큰 수준의 도메인 분류를 기반으로 정책 함수를 개발하고 훈련된 모델의 도메인 프라이버시를 개선하기 위한 효율적인 미세 조정 방법을 제안한다.
    3. 멤버쉽 추론 공격에 대한 실험에서 우리의 제안된 방법이 최근에 다루었던 동적 사생활 언어 모델에서 적용된 방법과 유사한 저항력을 가짐을 보여준다.

###### Visual Elements Mining as Prompts for Instruction Learning for Target-Oriented Multimodal Sentiment Classification (https://aclanthology.org/2023.findings-emnlp.403/)
- Anthology ID: 2023.findings-emnlp.403 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Target-oriented Multimodal Sentiment Classification (TMSC)는 문장 내 특정 대상에 대한 감성 극성을 식별하기 위해 시각적 모달리티와 텍스트 모달리티를 결합하는 것을 목표로 한다."
    2. "VEMP(VIsual Elements Mining as Prompts) 방법을 제안하여 시각적 요소의 의미 정보를 텍스트 심볼로 내장된 이미지(TSEI), 대상을 고려한 형용사-명사 쌍(TANPs) 및 이미지 장면 설명으로 기술하고 이를 모델 Tk-Instruct의 인스트럭션 학습을 위한 프롬프트로 변환한다."
    3. "실험 결과, 우리의 방법이 두 개의 벤치마크 데이터셋에서 최고의 성능을 달성하며, 추가적인 분석에서 우리의 방법의 각 구성 요소의 효과를 입증한다."

###### NASH: A Simple Unified Framework of Structured Pruning for Accelerating Encoder-Decoder Language Models (https://aclanthology.org/2023.findings-emnlp.404/)
- Anthology ID: 2023.findings-emnlp.404 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Structured pruning 방법은 Transformer와 같은 다양한 네트워크 구조에서 모델 크기를 줄이고 추론 속도를 빠르게 하는 데 효과적으로 사용된다.
    2. 하지만 encoder-decoder 모델에서 structured pruning 방법은 encoder-only 모델에 비해 상대적으로 조금 연구되었다.
    3. 이 연구에서는 encoder와 decoder 구성 요소를 분리된 방식으로 structured pruning하는 encoder-decoder 모델의 동작을 조사하였고, 그 결과를 통해 encoder 레이어의 수가 추론 속도에 지배적인 요소이며, pruned encoder 네트워크의 낮은 희소도가 생성 품질을 향상시킨다는 두 가지 인사이트를 제시하였다.

###### GBT: Generative Boosting Training Approach for Paraphrase Identification (https://aclanthology.org/2023.findings-emnlp.405/)
- Anthology ID: 2023.findings-emnlp.405 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문장의 쌍이 동일한 의미를 나타내는지 판별하는 Paraphrase Identification (PI) 작업은 정보 검색과 질문 응답에서 널리 사용되는데, 데이터 확장 (DA)은 PI 작업에 효과적이라 증명되었습니다. 그러나 대부분의 DA 방법은 비효율성과 낮은 품질의 한계를 가지고 있습니다.
    2. 이 연구에서는 PI를 위해 Generative Boosting Training (GBT) 접근 방식을 제안합니다. GBT는 인간 학습 과정을 기반으로 단일 모델에 대한 부스팅 학습 방법을 설계하며, 주기적으로 misclassified 인스턴스에 대한 seq2seq 모델을 사용하여 DA를 수행합니다.
    3. 실험 결과, GBT의 부스팅을 통해 단일 BERT 모델은 효율적이고 효과적인 성능을 보여주며, Pre-trained Language Model (PLM) 기반 기준 모델보다 우수한 성능을 보입니다.

###### DeCrisisMB: Debiased Semi-Supervised Learning for Crisis Tweet Classification via Memory Bank (https://aclanthology.org/2023.findings-emnlp.406/)
- Anthology ID: 2023.findings-emnlp.406 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 위기 상황에서 사람들은 주로 Twitter와 같은 소셜 미디어 플랫폼을 사용하여 상황에 대한 정보, 경고, 조언 및 지원을 전파한다. 이 논문에서는 위기 사태 분석을 위해 사회적 미디어에서 얻은 정보를 활용하는데, 최신 디바이어싱 방법을 연구하고 새로운 디바이어싱 방법을 제안한다.
    2. 완전 감독 학습은 방대한 양의 데이터를 주석으로 달아야 하므로 제한된 응답 시간 때문에 실용적이지 않다. 반면, 반감독 모델은 일부 클래스에는 중간 결과를 얻지만 다른 클래스에는 극히 부정확하게 수행되어 재난 모니터링과 구조에 심각한 영향을 줄 수 있다.
    3. 이 논문에서는 반감독 위기 트윗 분류에서 최근의 두 디바이어싱 방법을 연구하고, 각 훈련 반복마다 각 클래스의 생성된 가짜 레이블로부터 동일한 샘플링을 수행하는 메모리백(Memory Bank)을 활용한 간단하면서도 효과적인 디바이어싱 방법인 DeCrisisMB를 제안한다.

###### Probing LLMs for hate speech detection: strengths and vulnerabilities (https://aclanthology.org/2023.findings-emnlp.407/)
- Anthology ID: 2023.findings-emnlp.407 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어 플랫폼과 연구자들은 최근 대형 언어 모델을 사용하여 혐오 또는 유해한 언어를 탐지하려는 노력을 기울이고 있다. 그러나 이러한 연구들에서는 설명, 추가적인 맥락, 피해자 정보를 탐지과정에 활용하지 않는다.
    2. 본 연구에서는 다양한 prompt 변형, 입력 정보를 활용하고, 인과관계를 추가하지 않은 상황에서 대형 언어 모델의 성능을 평가한다. 이를 통해 모델 성능을 개선하기 위해 목표 정보를 파이프라인에 포함시키는 것이 효과적임을 확인한다.
    3. 또한, 모델이 올바르게 분류하거나 그 이유를 설명하지 못하는 오류 사례들의 유형을 제시하고, 이러한 취약점들은 모델에 대한 'jailbreak' prompt로 작용할 수 있으며, 이를 대비하기 위한 산업용 안전장치 기술의 개발이 필요하다.

###### From Simple to Complex: A Progressive Framework for Document-level Informative Argument Extraction (https://aclanthology.org/2023.findings-emnlp.408/)
- Anthology ID: 2023.findings-emnlp.408 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Document-level Event Argument Extraction (EAE)는 단일 문서에서 여러 이벤트의 인자(argument)를 추출하는 모델에 더 의존하기 때문에 이러한 이벤트들 사이의 종속성(dependencies)을 고려해야 한다. 
    2. 기존 방법들은 문서에서 이벤트들이 나타나는 순서에 따라 추출하지만, 첫 번째 문장에 나타나는 이벤트가 가장 추출하기 쉬운 것은 아니다. 
    3. 이 논문에서 제안하는 simple-to-complex 접근법은 이벤트의 난이도를 계산한 다음, 추출을 단순한 것부터 복잡한 순서로 수행하여 더 확실한 결과를 메모리에 저장하고, 모델은 이 신뢰할 수 있는 정보를 사용하여 더 어려운 이벤트를 예측한다.

###### MultiCMET: A Novel Chinese Benchmark for Understanding Multimodal Metaphor (https://aclanthology.org/2023.findings-emnlp.409/)
- Anthology ID: 2023.findings-emnlp.409 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 메타포는 인간의 의사소통에서 보편적인 측면이며, 대중 매체의 발전과 함께 다중 모드 형태로의 존재가 더욱 두드러지게 되었다. 그러나 다중 언어적 메타포 자원에 대한 연구는 제한적이며, 기존의 자연어 처리 작업은 메타포의 소스와 타겟 도메인을 분류하는 탐색을 다루지 않고 있다. 
    2. 이 연구에서는 다중 모달 중국 메타포 데이터셋인 MultiCMET을 소개하고, 광고의 텍스트-이미지 쌍 13,820개에 대한 메타포, 도메인 카테고리, 그리고 메타포가 전달하는 감성에 대해 수동으로 주석을 달았다.
    3. 또한, 도메인 특정 어휘 기능을 소개함으로써 메타포를 감지하기 위한 Cascading Domain Knowledge Integration (CDKI) 벤치마크를 구축했으며, 실험 결과 CDKI의 효과를 입증하였다. 데이터셋과 코드는 공개되어 있다.

###### GlotLID: Language Identification for Low-Resource Languages (https://aclanthology.org/2023.findings-emnlp.410/)
- Anthology ID: 2023.findings-emnlp.410 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 많은 논문들이 300개 정도의 고자원 및 중간자원 언어에 대한 언어 식별(LID)에 대한 좋은 솔루션을 발표했지만, 저자원 언어, 신뢰성, 효율성, 사용 용이성에 대한 특징( desiderata)을 만족하는 LID 모델이 없다.
    2. 이 논문에서는 GlotLID-M이라는 LID 모델을 발표하며 저자원 언어에 대해 넓은 범위의 커버리지, 신뢰성 및 효율성 조건을 만족시키는 것을 보여준다.
    3. GlotLID-M은 1665개 언어를 식별하며, 이전 작업에 비해 커버리지가 크게 증가한다. 실험 결과, F1과 false positive rate (FPR)를 가중치로 잡을 때 GlotLID-M은 네 개의 베이스라인(CL, FT176, OpenLID, NLLB)을 능가한다.

###### Finding Support Examples for In-Context Learning (https://aclanthology.org/2023.findings-emnlp.411/)
- Anthology ID: 2023.findings-emnlp.411 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "In-context learning"은 언어 모델이 몇 가지 예시를 관찰하고 테스트 입력에 대한 예측을 직접 출력하는 새로운 학습 패러다임이다. 그러나 기존 방법들은 제공된 예시에 민감하며 무작위로 샘플링된 예시는 성능이 낮을 수 있다. 
    2. 이 논문에서는 in-context learning에 최적인 "support examples"를 찾기 위한 방법을 제안한다. 이를 위해 언어 모델의 피드백을 기반으로 예시의 in-context 정보성을 평가하는 새로운 메트릭을 제안하고, 이를 이용하여 예시를 선별하는 과정을 진행한다. 
    3. 실험 결과, 이 알고리즘은 다양한 기준모델보다 우월한 성능을 보이며, 각 구성요소가 성능 향상에 중요한 역할을 하는 것으로 나타났다. 이를 통해 supporting examples와 in-context learning의 원리에 대한 통찰을 얻을 수 있다.

###### Uncovering the Root of Hate Speech: A Dataset for Identifying Hate Instigating Speech (https://aclanthology.org/2023.findings-emnlp.412/)
- Anthology ID: 2023.findings-emnlp.412 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 hate speech 탐지와 중재 방법에는 주로 기계학습 등의 컴퓨터적 접근이 사용되어왔지만, hate speech의 근본 원인을 찾는 작업은 미비한 상태였다. 
    2. 이 연구에서는 hate instigating speech라는 개념을 소개하며, 이는 다른 사람들이 hate speech에 동참하도록 유도하거나 자극하는 특정 유형의 온라인 텍스트 게시물을 말한다. 
    3. hate instigating speech의 식별은 효과적인 hate speech 중재에 상당한 영향력을 가지며, hate speech의 뿌리인 hate instigating speech에 초점을 맞추면 중재 검토가 필요한 콘텐츠의 양을 크게 줄일 수 있다.
    
    abstract: A difficulty of creating high-quality Multiple Choice Questions (MCQs) for educational purposes lies in the lack of good metrics for evaluating their quality. We propose using Knowledge Dependent Answerability (KDA) as a novel evaluation metric to measure the MCQ's ability to assess the student's knowledge of the corresponding target fact. This metric takes into account the answerability of the MCQ given knowledge of the target fact, unlike existing metrics that only evaluate the similarity of the generated MCQ to a gold sample in the dataset. Through human studies, we demonstrate the strong correlation of KDA_disc and KDA_cont with the usability and effectiveness of MCQs in an actual classroom setting, as labeled by experts.
    
    1. MCQ의 품질을 평가하는 좋은 메트릭스의 부재로 인해 교육 목적으로 높은 품질의 MCQ를 만드는 데 어려움이 있다. 
    2. 이 논문에서는 MCQ가 대응하는 학생의 지식을 평가하는 능력을 측정하기 위해 Knowledge Dependent Answerability (KDA)를 새로운 평가 메트릭으로 제안한다. 
    3. 기존 메트릭과 달리 KDA는 MCQ의 대상 사실에 대한 지식을 고려하여 평가하며, 인간 연구를 통해 KDA_disc와 KDA_cont가 실제 강의실에서의 사용성과 효과에 강한 상관관계를 가짐을 보였다.

###### Responsible AI Considerations in Text Summarization Research: A Review of Current Practices (https://aclanthology.org/2023.findings-emnlp.413/)
- Anthology ID: 2023.findings-emnlp.413 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. AI 및 NLP 연구에는 주로 윤리적 고려 사항, 부정적 영향 및 다른 책임 있는 AI 문제에 대해 생각하도록 요구한다. 하지만, 텍스트 요약과 같은 특정 NLP 작업에서 이러한 문제가 얼마나 흔한지 또는 언제, 그리고 왜 이러한 문제가 발생할 가능성이 있는지에 대한 이해는 여전히 제한적이다.
    2. 이 논문에서는 화자인 AI 커뮤니티에서 주로 간과되는 텍스트 요약과 같은 주요 NLP 작업에서 연구 및 보고 관행을 조사한다.
    3. 연구 방법을 기반으로 매우 제한적인 논문에서 잠재적인 부정적 영향이나 다른 책임 있는 AI 문제를 고려하는 것이 제한되고 있음을 발견하였다. 이를 바탕으로 구체적인 연구 방향과 실천 사례에 대한 권고사항을 제시한다.

###### Improving Speech Translation by Fusing Speech and Text (https://aclanthology.org/2023.findings-emnlp.414/)
- Anthology ID: 2023.findings-emnlp.414 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 언어 번역을 개선하기 위해 음성과 텍스트의 상호 보완적인 특성을 활용한다.
    2. 하지만 음성과 텍스트는 다른 특성을 가지고 있어 통합이 어려운데, 이러한 특성 차이를 해결하기 위해 FuseST라는 모델을 제안한다.
    3. FuseST는 음성, 텍스트, 그리고 통합된 음성-텍스트 세 가지 입력 형태를 지원하며, MuST-C, GigaST, newstest benchmark에서 우수한 성능을 보인다.

###### Narrative Order Aware Story Generation via Bidirectional Pretraining Model with Optimal Transport Reward (https://aclanthology.org/2023.findings-emnlp.415/)
- Anthology ID: 2023.findings-emnlp.415 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 매력적인 이야기를 만들기 위해 작가는 종종 논리적으로 일관된 사건의 연속을 계획하고 서사적 순서를 요령 있게 조작하여 플래시백을 생성한다. 그러나 기존의 이야기 생성 시스템은 사건 간 상관관계를 충분히 이해하지 못하고 사건의 시간적 순서에 대한 인식도 부족하여, 이야기의 논리와 서사적 순서를 균형있게 잡는 고품질 사건을 생성하는 것이 어렵다.
    2. 본 논문에서는 이야기 생성을 위한 narrative order 인식 프레임워크 BPOT를 제안한다. 이 프레임워크는 이벤트 간 상관관계와 이벤트 간 순서를 양방향으로 사전 훈련(pretraining)하는 모델을 제시한다. 또한, 심층 강화학습 알고리즘과 새로운 optimal transport reward를 설계하여 세부 튜닝 단계에서 생성된 사건의 품질을 더욱 개선한다.
    3. 자동 및 수동 평가 결과 모두, 우리의 프레임워크가 논리적으로 일관된 플래시백을 가진 이야기를 생성하는 데 우수함을 보여주고 있다.

###### Explainable Claim Verification via Knowledge-Grounded Reasoning with Large Language Models (https://aclanthology.org/2023.findings-emnlp.416/)
- Anthology ID: 2023.findings-emnlp.416 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Claim verification의 문제에서는 인간이 주석을 단 데이터의 사용 없이 claim을 검증하는 방법을 이해하는 것이 중요하다."
    2. 시험 데이터가 없이도 Comprehensive한 설명을 제공할 수 있는 모델을 제안한다.
    3. FOLK는 claim을 FOL (First-Order-Logic)로 번역하여 검증해주며, 이 프로세스는 사람이 읽을 수 있는 형태로 이해 과정을 설명한다.

###### Strong and Efficient Baselines for Open Domain Conversational Question Answering (https://aclanthology.org/2023.findings-emnlp.417/)
- Anthology ID: 2023.findings-emnlp.417 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구들은 대화형 (ODConvQA) 도메인에 대한 baseline 성능 평가에 제한적인 관심을 보이고 있다. 
    2. 이 논문에서는 SotA(DPR retriever 및 FiD reader pipeline)가 ODConvQA 태스크에 적용될 때 여러 제한으로 인해 성능이 크게 저하됨을 보여준다. 
    3. 우리는 retriever와 reader 사이에 빠른 reranking 구성 요소를 도입하고, 대상 finetuning 단계를 수행함으로써 강력하면서도 단순하고 효율적인 baseline을 제안하고 평가한다. 이를 통해 SotA 결과를 향상시키고 reader의 지연 시간을 60% 감소시키는 것을 실험을 통해 보여준다.

###### Efficient Continue Training of Temporal Language Model with Structural Information (https://aclanthology.org/2023.findings-emnlp.418/)
- Anthology ID: 2023.findings-emnlp.418 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 언어 모델은 특정 시점에서 수집된 데이터로 주로 훈련되며, 시간에 따라 일반화하고 언어 변화를 모델링하기 어려워진다. 
    2. 기존의 temporal language model(TempoBERT)은 훈련 과정에 타임스탬프를 직접 포함시켜 시간 변수를 모델링했다. 
    3. 이 논문에서는 토큰들과 함께 중요한 구문적 변화를 가지는 단어들과 시간 접두어 간의 내재적 관계를 기반으로 언어 변화를 학습하는 Syntax-Guided Temporal Language Model(SG-TLM)을 제안한다.

###### Retrieval-Augmented Parsing for Complex Graphs by Exploiting Structure and Uncertainty (https://aclanthology.org/2023.findings-emnlp.419/)
- Anthology ID: 2023.findings-emnlp.419 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 retrieval 방법은 복잡한 그래프 파싱 문제에서 정확한 예시를 식별하지 못해 부적절한 검색을 하고 제한된 검색 예산 하에서 유추된 결과를 얻기 때문에, 복잡한 그래프 문제에서 retrieval augmented 모델을 개선하기 위해 structural similarity와 model uncertainty 두 가지 독특한 정보를 활용하였다.
    2. 모델의 불확실성을 그래프 예측의 양자화하기 위해 SUGAR를 제안하였다. 가장 불확실한 서브그래프를 식별하고 이를 기준으로 예시를 검색한다.
    3. 복잡한 그래프 구조를 가진 실제 파싱 벤치마크에서, SUGAR는 구조나 모델의 불확실성을 고려하지 않는 전통적인 방법에 비해 강력한 성능을 보였다.

###### When it Rains, it Pours: Modeling Media Storms and the News Ecosystem (https://aclanthology.org/2023.findings-emnlp.420/)
- Anthology ID: 2023.findings-emnlp.420 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대부분의 사건들은 뉴스 매체에서 짧은 보도만 받지만, 가끔은 하나의 사건이 뉴스를 뒤집어 놓고 몇 주 동안 지속되는 대량의 보도가 나온다. 
    2. 이 연구에서는 두 개의 기사 유사도 모델을 개발함으로써 지역 및 국가 온라인 뉴스를 커버하고 대략 2년 동안의 매체 폭풍을 포함하는 포괄적인 말뭉치를 만들었다. 
    3. 이를 통해 우리는 매체 폭풍의 진화와 주제 분포에 대한 확인하고 이를 통해 매체 보도와 매체 간의 어제타설 순서에 대한 이전 가설에 대한 증거를 제공할 수 있었다.

###### Intra-Event and Inter-Event Dependency-Aware Graph Network for Event Argument Extraction (https://aclanthology.org/2023.findings-emnlp.421/)
- Anthology ID: 2023.findings-emnlp.421 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "이벤트 인자 추출은 구조화된 정보를 제공하기 위해 다양한 자연어 처리 작업에 있어서 중요하다. 기존의 방식은 일일히 이벤트 인자를 추출하고 이벤트 구조의 관점에서 인자 역할 간의 의존성 정보를 구축하는 것을 주로 소홀히 한다."
    2. "이 논문에서는 다른 역할 간의 의존성을 적절하게 모델링하여 성능을 높이는 방법에 대해 연구한다."
    3. "우리는 이벤트 구조를 기반으로 하는 intra-event와 inter-event 의존성을 고려한 그래프 네트워크를 제안하고, 의존성 정보와 이벤트 표현을 최적화하기 위해 의존성 상호작용 모듈과 보조 과업을 소개한다. 실험 결과는 우리가 제안한 방법의 큰 장점을 보여준다."

###### From Relevance to Utility: Evidence Retrieval with Feedback for Fact Verification (https://aclanthology.org/2023.findings-emnlp.422/)
- Anthology ID: 2023.findings-emnlp.422 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 검증 증명 (FV)에서 검색 강화 방법은 주요 접근법이 되었으며, 명제의 정당성을 검증하기 위해 여러 검색된 증거에 대한 추론이 필요하다. 
    2. 기존의 작업은 자주 사용되는 검색 모델을 사용하여 증거를 검색하며, 확률 순위 원칙에 기반한 모델을 사용한다. 하지만, FV에서는 관련성 대신 검증기가 전달된 증거에서 어떤 유틸리티를 얻는지에 집중해야 한다. 
    3. 우리는 claim verifier의 피드백을 통합하여 증거 검색 프로세스를 최적화하는 feedback-based evidence retriever (FER)를 소개한다. 실험 결과, FER가 기존의 기준에 비해 우월함을 입증하였다.

###### How to Train Your Dragon: Diverse Augmentation Towards Generalizable Dense Retrieval (https://aclanthology.org/2023.findings-emnlp.423/)
- Anthology ID: 2023.findings-emnlp.423 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 들어 DR(dense retrieval)를 개선하기 위해 비감독 대조 학습과 pseudo-query 생성과 같은 다양한 기술들이 개발되었지만, 기존 DR들은 supervises와 zero-shot retrieval 간의 효율성 절충을 겪는 경우가 많다.
    2. 본 논문에서는 DR의 contrastive learning에 대해 DA(data augmentation) 프레임워크 아래에서 체계적으로 연구하였다. 또한, 기존 DA의 일부 문제를 지적하고, 새로운 DA 접근법을 제안하여 일반화 가능한 DR을 훈련시켰다.
    3. DRAGON이라는 BERT-base 사이즈의 DR은 supervised와 zero-shot 평가에서 최고의 효과성을 달성하여, 더 복잡한 late interaction을 사용하는 모델들과도 경쟁할 수 있게 되었다.

###### Discovering Highly Influential Shortcut Reasoning: An Automated Template-Free Approach (https://aclanthology.org/2023.findings-emnlp.424/)
- Anthology ID: 2023.findings-emnlp.424 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Shortcut reasoning"은 NLP 모델의 robustness를 손상시키는 비합리적인 추론 과정이다. 이전 연구들은 shortcut reasoning을 식별하는 것에 대한 많은 노력이 있었지만, 발견된 shortcut reasoning의 심각성을 정량화하는 방법은 제시되지 않았고, 특정 유형의 shortcut reasoning이 누락될 수 있다는 두 가지 주요한 한계가 있다.
    2. 이러한 문제를 해결하기 위해, 우리는 shortcut reasoning을 식별하기 위한 새로운 방법을 제안한다. 제안된 방법은 out-of-distribution 데이터를 활용하여 shortcut reasoning의 심각성을 정량화하고, shortcut reasoning을 유발하는 토큰 유형에 대한 가정을 하지 않는다.
    3. Natural Language Inference와 Sentiment Analysis에서의 실험 결과는 우리의 프레임워크가 이전 연구에서 알려진 shortcut reasoning 뿐만 아니라 알려지지 않은 shortcut reasoning도 성공적으로 발견한다는 것을 보여준다.

###### Schema-adaptable Knowledge Graph Construction (https://aclanthology.org/2023.findings-emnlp.425/)
- Anthology ID: 2023.findings-emnlp.425 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 지식 그래프 구축 방식은 정적인 정보 추출 방식으로, 사전에 정의된 스키마로 제한되어 있다. 이는 동적인 상황이나 도메인에서 새로운 지식이 등장할 때 제대로 작동하지 못한다.
    2. 이에 따라 우리는 스키마 자동적으로 변화시키는 KGC를 위한 새로운 태스크를 제안한다. 이 태스크는 재학습 없이 동적으로 변화하는 스키마 그래프에 기반하여 entity, relation, event를 추출하는 것을 목표로 한다.
    3. 우리는 여러 가지 유명한 접근 방식들의 스키마 변화 대응 능력을 조사하고, AdaKGC라고 불리는 간단하지만 효과적인 베이스라인을 제안한다. 실험 결과, AdaKGC가 다른 방법들보다 우수한 성능을 보이지만, 아직 개선의 여지가 있다는 것을 보여준다.

###### Evaluating the Knowledge Base Completion Potential of GPT (https://aclanthology.org/2023.findings-emnlp.426/)
- Anthology ID: 2023.findings-emnlp.426 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 구조화된 지식 베이스(KB)는 검색 엔진 및 기타 응용 프로그램에 필수적이지만, 그들은 불완전할 수 있다. 
    2. 최근의 연구들은 대중적인 주제들에 대해 평가하거나 이미 존재하는 사실들을 샘플링하는 한계가 있다. 
    3. 본 연구에서는 GPT-3, ChatGPT 및 GPT-4와 같은 모델이 Wikidata와 같은 대형 KB를 완성하는 데 있어 완전히 설득력 있는 결과를 달성하지 못한다는 것을 발견했지만, 보다 작은 LMs에 비해 실질적인 개선을 보여준다.

###### Conic10K: A Challenging Math Problem Understanding and Reasoning Dataset (https://aclanthology.org/2023.findings-emnlp.427/)
- Anthology ID: 2023.findings-emnlp.427 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인공지능의 능력을 평가하는 데 수학적 이해와 추론은 중요한 작업이다. 그러나 기존 벤치마크는 추론의 몇 단계만 요구하거나 특정 주제의 적은 양의 데이터만 포함하므로 다양한 문제를 세부적으로 분석하기 어렵다.
    2. 본 논문에서는 중국의 고교 교육에서의 Conic10K라는 도전적인 수학 문제 데이터셋을 제안한다. 이 데이터셋은 다양한 수리적 추론을 포함하고 있으며, 콘익 섹션에 대한 지식만 요구한다.
    3. 실험 결과, 기존의 대형 언어 모델 (GPT-4 포함)은 복잡한 추론에서 성능이 떨어진다. 이 연구는 더 정확한 자연어 이해와 추론 기술에 대한 발전을 위한 영감을 줄 것으로 기대된다.

###### DepWiGNN: A Depth-wise Graph Neural Network for Multi-hop Spatial Reasoning in Text (https://aclanthology.org/2023.findings-emnlp.428/)
- Anthology ID: 2023.findings-emnlp.428 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 공간적 추론은 다양한 실생활 응용에서 중요한 역할을 한다. 기존의 공간적 추론 접근법은 순수한 텍스트에서 공간적 관계를 추론하지만, 자연어와 심볼 구조 간의 차이를 간과한다.
    2. 이 논문에서는 그래프 신경망(GNN)을 활용하여 심볼 구조를 합성하고 집계하는 능력을 갖춘 새로운 방법을 제안한다. 
    3. 실험 결과로는 DepWiGNN이 기존의 공간적 추론 방법들보다 우수한 성능으로 장기 의존성을 포착하는 능력을 갖추고 있음을 보여준다.

###### TK-KNN: A Balanced Distance-Based Pseudo Labeling Approach for Semi-Supervised Intent Classification (https://aclanthology.org/2023.findings-emnlp.429/)
- Anthology ID: 2023.findings-emnlp.429 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템에서 의도 감지의 능력은 현대 기술에서 점점 더 중요해지고 있다. 그러나 이러한 시스템은 보통 레이블이 없는 많은 데이터를 생성하며, 이 데이터에 수작업으로 레이블을 붙이는 것은 상당한 인력이 필요하다. 
    2. 반지도 학습 방법은 일부 레이블이 달린 레이블을 훈련한 모델을 사용하고 모델 예측 확신이 특정 임계값보다 높은 일부 레이블이 달려있지 않은 레이블에 가짜 레이블(pseudo-label)을 지정하여 이 비용을 해결하려고 시도한다. 
    3. 본 논문에서는 임베딩 공간에서의 거리를 기반으로 한 더 견고한 가짜 레이블링 접근 방식을 사용하는 Top-K 최근접 이웃(TK-KNN)을 소개한다. 이는 랭킹 기반 접근 방식을 통해 클래스 간에 균형 잡힌 가짜 레이블이 달린 예제 세트를 유지하는 것을 목표로 한다.

###### Late Fusion of Transformers for Sentiment Analysis of Code-Switched Data (https://aclanthology.org/2023.findings-emnlp.430/)
- Anthology ID: 2023.findings-emnlp.430 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 코드 스위칭은 다중 언어를 사용하는 지역 사회에서 흔한 현상이지만, 코드 스위칭 데이터의 감성 분석은 도전적이면서도 소중한 연구 분야입니다.
    2. 논문에서는 두 개의 트랜스포머를 결합하여 (logits, 추정치) 생성한 후 신경망으로 입력하여 코드 스위칭 데이터에 대한 감성 분석 시스템을 개발합니다.
    3. 실험 결과, 우리의 접근 방식은 GLUECoS 벤치마크 데이터셋에서 최고 성능을 보여줌으로써 En-Es에서 73.66%, En-Hi에서는 61.24%의 F1 점수를 달성했습니다.

###### Inductive Relation Inference of Knowledge Graph Enhanced by Ontology Information (https://aclanthology.org/2023.findings-emnlp.431/)
- Anthology ID: 2023.findings-emnlp.431 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프의 추론은 그래프 내의 새로운 미지의 개체들 간의 잠재적인 관계를 완성하는 것을 목표로 한다. 기존 방법들은 그래프 구조 정보나 관계 정보와 같은 entity-independent feature들을 기반으로 추론을 한다.
    2. 하지만 새로운 개체들의 이웃은 종종 충분한 정보를 제공하지 못하여 이 feature들을 효과적으로 구성하는 데 어려움을 겪는다.
    3. 본 논문에서는 온톨로지 정보를 융합하는 지식 그래프 추론 방법을 제안한다. 초점이 되는 서브그래프를 기반으로 개념에 해당하는 feature embeddings를 가져와 온톨로지 내에 내재된 시맨틱 정보를 학습하며, 개체들과 개념들 사이의 시맨틱 관계를 명시적으로 모델링하기 위해 타입 제약 regular loss를 구축하여 개체의 누락된 개념들을 포착한다.

###### Dynamic Stance: Modeling Discussions by Labeling the Interactions (https://aclanthology.org/2023.findings-emnlp.432/)
- Anthology ID: 2023.findings-emnlp.432 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Stance detection은 주어진 주제에 대한 텍스트의 표현된 태도를 할당하여 일반화 능력이 떨어지고 주제에 강하게 의존하는 정적인 작업으로 주로 모델링되었다. 
    2. 이 논문에서는 메시지와 그에 대한 응답 간의 상호작용에 초점을 맞춘 동적인 작업으로 stance를 모델링하는 것을 제안한다.
    3. DySC라는 새로운 데이터셋을 만들고, 여러 언어에서 토픽과 언어 간의 이식성을 보여주기 위해 일련의 단일 언어 및 다국어 모델을 DySC에 대해 세밀하게 조정하였다.

###### Harnessing the Power of Large Language Models for Empathetic Response Generation: Empirical Investigations and Improvements (https://aclanthology.org/2023.findings-emnlp.433/)
- Anthology ID: 2023.findings-emnlp.433 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 공감 대화는 조화로운 사회적 관계 구축에 필수적인 부분이며, 도움이 되는 AI 개발에 기여한다. 이전 접근 방식은 주로 작은 규모의 언어 모델을 사용하였으나, ChatGPT의 등장으로 대형 언어 모델의 응용 효과가 큰 관심을 받고 있다.
    2. 본 연구는 대규모 언어 모델(Large Language Models)을 사용한 공감적인 대답 생성의 성능을 실험적으로 조사하고, 의미론적으로 비슷한 문맥 학습, 두 단계의 상호작용 생성과 지식 베이스와의 결합과 같은 세 가지 개선 방법을 제안한다.
    3. 광범위한 실험 결과, 대형 언어 모델은 우리가 제안한 방법을 통해 상당한 성과 향상을 이룰 수 있으며, 자동 및 인간 평가에서 최고의 성능을 달성할 수 있는 것으로 나타났다. 또한, GPT-4가 인간 평가자를 시뮬레이션하는 가능성도 탐색하였다.

###### GPT Deciphering Fedspeak: Quantifying Dissent Among Hawks and Doves (https://aclanthology.org/2023.findings-emnlp.434/)
- Anthology ID: 2023.findings-emnlp.434 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 세계의 시장과 정책 결정자들은 Federal Open Market Committee (FOMC)의 중대한 통화정책 결정에 많은 관심을 갖고 있다. 회의 기록에는 위원들의 경제에 대한 태도가 담겨있으며, 이들로부터 인플레이션에 대한 연구와 차별을 분석한다.
    2. 작은 차이점들이 공개적인 발언에서는 누락되기 때문에, 회의 기록과 소식통은 위원들의 다양한 의견을 보다 잘 반영하고 있다.
    3. 따라서, FOMC의 의견을 예측할 때는 진영 간의 의견 충돌을 충분히 반영하지 않는다면 정확하지 않을 수 있음을 주장한다.

###### DialogQAE: N-to-N Question Answer Pair Extraction from Customer Service Chatlog (https://aclanthology.org/2023.findings-emnlp.435/)
- Anthology ID: 2023.findings-emnlp.435 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 고객 서비스의 대화 기록에서 질문-답변 (QA) 쌍을 추출하여 차가운 시작 또는 지속적 통합 시나리오에서 고객 서비스 챗봇의 지식 베이스를 풍부하게 하는 것은 효율적인 방법이다.
    2. 기존 연구들은 성장하는 고객 서비스 챗봇의 대화 기록에서 1대1 QA 쌍을 얻으려고 시도하였으나, 대화 문맥에서 불완전한 발화를 통합하는 데 실패하였다.
    3. 이 논문에서는 N-to-N QA 추출 작업을 제안하며, 파생된 질문과 해당하는 답변이 서로 다른 발화에서 나뉠 수 있는 작업을 다룬다.

###### Inverse Reinforcement Learning for Text Summarization (https://aclanthology.org/2023.findings-emnlp.436/)
- Anthology ID: 2023.findings-emnlp.436 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 역 강화 학습(IRL)을 요약 모델 훈련에 적용하여 사람의 요약 행동을 모방하는 효과적인 패러다임으로 소개한다.
    2. 우리의 IRL 모델은 요약을 위한 여러 중요한 부 서브 리워드 (sub-reward)를 이용하여 보상 함수를 추정하고, 동시에 정책 네트워크를 최적화한다.
    3. CNN/DailyMail와 WikiHow와 같은 다양한 도메인의 데이터셋과 BART-base 및 BART-large와 같은 다양한 모델 크기에서의 실험 결과는 MLE 및 RL 베이스라인 대비 우리의 제안된 IRL 모델의 우위성을 보여준다.

###### MM-Reasoner: A Multi-Modal Knowledge-Aware Framework for Knowledge-Based Visual Question Answering (https://aclanthology.org/2023.findings-emnlp.437/)
- Anthology ID: 2023.findings-emnlp.437 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델의 강력한 추론 능력을 활용한 최근 지식 기반 시각 질의 응답 (KVQA) 접근 방식은 입력 이미지의 전역 캡션을 사용하여 질문에 답을 제공한다. 그러나 이러한 방식은 캡션에 포착되지 않은 중요한 시각적 정보를 놓칠 수 있다. 또한 질문에 답하기 위해 필요한 시각적 정보를 완전히 활용할 수 없다.
    2. 우리는 이러한 문제를 해결하기 위해 KVQA를 위한 새로운 프레임워크인 MM-Reasoner를 소개한다. MM-Reasoner는 먼저 밀집 캡셔너, 객체 탐지기, OCR과 같은 비전 API 세트를 사용하여 텍스트 형식으로 이미지에서 상세한 정보를 추출한다. 그런 다음, 추출된 텍스트 정보에서 LLM에게 질문에 특정된 지식을 추출하도록 요청하여 추론에 필요한 외부 지식, 상식, 명시적인 지지 사실 및 근거가 포함된 풍부한 표현을 제공한다.
    3. 마지막으로, 지식, 질문 및 시각적 입력을 사용하여 비전-언어 모델 (VLM)을 세밀하게 조정하는 데 사용된다. 테스트 시에 MM-Reasoner는 VLM이 예측한 잠재적인 답변을 사용하여 프롬프트를 반복적으로 갱신 및 최적화하여 답변을 미세조정한다. 실험적 연구는 MM-Reasoner가 여러 KVQA 데이터셋에서 최고 성능을 달성함을 보여준다.

###### Toward Joint Language Modeling for Speech Units and Text (https://aclanthology.org/2023.findings-emnlp.438/)
- Anthology ID: 2023.findings-emnlp.438 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 음성과 텍스트는 인간 언어의 두 가지 주요 형태이다. 하지만 언어 모델링 분야에서는 이들을 공동으로 모델링하는 데 거의 노력이 기울여지지 않았다.
    2. 본 논문에서는 연속된 음성 신호를 이산 단위로 변환하기 위해 다양한 음성 토크나이저를 비교하며 혼합된 음성-텍스트 데이터를 구성하는 다양한 방법을 사용한다. 그리고 음성과 텍스트를 얼마나 잘 혼합하는지를 평가하기 위해 자동화된 메트릭을 소개한다.
    3. 또한, 공동 언어 모델을 다양한 형태(음성 또는 텍스트)의 하위 의미 이해(SLU) 작업에 Fine-tuning하고, 공유 표현 학습을 평가하기 위해 성능을 테스트한다. 결과적으로 제안된 혼합 기술로 음성 단위와 텍스트를 섞는 것은 SLU 작업에서 음성만을 고려한 기준 모델에 비해 향상되며, 제로샷 크로스모달 전이성을 보인다.

###### From Chaos to Clarity: Claim Normalization to Empower Fact-Checking (https://aclanthology.org/2023.findings-emnlp.439/)
- Anthology ID: 2023.findings-emnlp.439 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어 플랫폼의 확산과 함께 소셜 미디어 포스트를 통해 사실과 다른 주장이 포함 된 게시물에 노출되게 된다. 하지만 이러한 포스트의 잡음은 검증이 필요한 정확하고 중요한 주장을 식별하는 것에 어려움을 제공한다. 이 논문에서는 ClaimNorm이라고 불리는 새로운 작업을 소개하며, 복잡하고 잡음이 많은 소셜 미디어 포스트를 더 직관적이고 이해하기 쉬운 정규화된 주장으로 분해하고자 한다. 
    2. 우리는 CACN이라는 전처리 방법을 제안하며, chain-of-thought와 claim check-worthiness estimation을 활용하여 인간의 추론과정을 모방하여 복잡한 주장을 이해한다. 
    3. 우리는 CLAN이라는 6,000개 이상의 실제 소셜 미디어 포스트와 해당 정규화된 주장으로 구성된 포괄적인 데이터셋을 만들어 실험을 진행하였고, 이를 통해 CACN이 다양한 평가 척도에서 여러 베이스라인 알고리즘을 능가함을 보였다.

###### Mitigating Biases in Hate Speech Detection from A Causal Perspective (https://aclanthology.org/2023.findings-emnlp.440/)
- Anthology ID: 2023.findings-emnlp.440 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 많은 혐오 발언 탐지기들이 자동으로 혐오 문구를 감지하는 데 사용되고 있지만, 그들의 훈련 데이터셋은 때때로 특정 고정 관념 (예: 인종 또는 종교와 관련된)으로 치우쳐있어서 예측을 위한 편법에 의존하기 쉽다.
    2. 이 논문에서는 grammar induction을 사용하여 혐오 발언의 문법 패턴을 찾아 원인 관점에서 이 현상을 분석한다. spuriousness와 모델 예측에 미치는 영향을 기반으로 다양한 편견을 분류하고 검증한다.
    3. 그런 다음, 이러한 confounder를 기반으로 Multi-Task Intervention 및 Data-Specific Intervention과 같은 두 가지 완화 접근 방식을 제안한다. 9개의 혐오 문구 데이터셋에서 수행한 실험은 우리의 접근법의 효과를 입증한다.

###### Unmasking the Hidden Meaning: Bridging Implicit and Explicit Hate Speech Embedding Representations (https://aclanthology.org/2023.findings-emnlp.441/)
- Anthology ID: 2023.findings-emnlp.441 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 혐오 발언(HS) 감지에 대한 연구는 주로 사용자 생성 콘텐츠에서 명백한 혐오 표현을 식별하는 데 초점을 맞추었다. 하지만 최근에는 보다 묵시적이고 미묘한 학대적 콘텐츠를 다룰 수 있는 방법에 대한 연구도 진행되고 있다.
    2. 그러나 이러한 노력에도 불구하고, 자동화된 시스템은 여전히 묵시적이고 더 은폐된 혐오 발언을 정확하게 인식하는 데 어려움을 겪고 있다.
    3. 이 연구에서는 트랜스포머 모델에 기반한 다양한 모델들을 비교 분석하며, 묵시적인 HS 메시지를 포함한 다섯 가지 데이터셋에서의 성능을 평가하였다.

###### PerturbScore: Connecting Discrete and Continuous Perturbations in NLP (https://aclanthology.org/2023.findings-emnlp.442/)
- Anthology ID: 2023.findings-emnlp.442 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP에서의 신경망 응용의 빠른 발전으로 인해 모델의 robustness 문제에 대한 관심이 증가하고 있다. 
    2. 컴퓨터 비전과 달리 텍스트의 이산적인 특성은 NLP에서의 robustness를 탐구하는 것이 더 도전적이다. 
    3. 본 연구에서는 이산성(specificity)와 연속성(continuity) 사이의 상관관계를 연결하고 측정하는 방법을 제안하여 NLP 모델에서 이산적인 변동을 이해하는 데 도움을 주려고한다.

###### InstructoR: Instructing Unsupervised Conversational Dense Retrieval with Large Language Models (https://aclanthology.org/2023.findings-emnlp.443/)
- Anthology ID: 2023.findings-emnlp.443 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 방법들은 제한된 지도학습 데이터로 사전 훈련된 ad-hoc 재검색기를 단순히 세밀 조정하는 것에 그치기 때문에, 다중 턴 대화를 처리하고 사용자의 실제 질의 의도를 이해하는 것이 어렵다. 
    2. 이 논문에서는 대화형 재검색 과제에 대해, 큰 언어 모델 (LLM)이 복잡한 대화 맥락에서 사용자의 질의 의도를 정확하게 파악하고, 지도 신호를 통해 무지도 방식으로 재검색기를 가르칠 수 있다는 것을 발견했다.
    3. 우리는 InstructoR라는 독창적인 방법을 제안하여, LLM을 사용하여 세션-패시지 일치도 점수를 추정하고, 이를 소프트 라벨로 사용하여 재검색기의 훈련을 안내하는 무지도 훈련 프레임워크를 설계했다. 우리의 방법은 낮은 자원 및 제로샷 설정에서도 효과적임을 실험적으로 검증하였다.

###### The Iron(ic) Melting Pot: Reviewing Human Evaluation in Humour, Irony and Sarcasm Generation (https://aclanthology.org/2023.findings-emnlp.444/)
- Anthology ID: 2023.findings-emnlp.444 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "자연어 생성 시스템을 평가하기 위해 인간 평가가 가장 효과적인 방법이라고 알려져 있지만, 그 실행의 질은 자주 의심 받는다."
    2. "특히 유머, 반어적 표현 등과 같은 특이한 언어 형태의 생성은 선택된 평가자들의 특성이 매우 중요한 하위 도메인으로, 투명성과 재현성을 위해 가능한 한 평가자들의 인구 특성을 보고하는 노력이 필요하다고 주장한다."
    3. "이 논문에서는 각 언어 형태의 개요와 다른 참가자 변수에 의해 어떻게 해석이 영향을 받는지에 대한 예시를 분석하여 이러한 주장을 뒷받침하였고, NLG에서 평가 절차가 어떻게 보고되는지에 대한 비판적인 조사를 수행하여 평가자 인구 특성의 공개적인 보고 부족과 크라우드소싱 플랫폼에 대한 의존성이 심각하다는 점을 확인하였다."

###### INGENIOUS: Using Informative Data Subsets for Efficient Pre-Training of Language Models (https://aclanthology.org/2023.findings-emnlp.445/)
- Anthology ID: 2023.findings-emnlp.445 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습 언어 모델(PTLM)은 모델 용량과 학습 데이터셋 크기가 증가함에 따라 일반화 및 새로운 기능에서 높은 성능을 보이는데, 이로 인해 대단한 모델의 개발이 진행되고 있다. 
    2. 그러나 훈련 시간이 길어지고 컴퓨팅 비용이 많이 들며, 환경에도 해로울 수 있으므로, 훈련 데이터의 유효성을 최적화하는 것이 중요하다.
    3. 우리는 정보를 많이 담은 하위 집합을 선택하는 서브모듈러 최적화를 활용하여 효율적으로 PTLM(BERT, BioBERT, GPT-2)을 훈련시킬 수 있으며, 완전히 훈련된 모델의 성능의 약 99%를 달성할 수 있다는 것을 검증하였다.

###### Towards General Error Diagnosis via Behavioral Testing in Machine Translation (https://aclanthology.org/2023.findings-emnlp.446/)
- Anthology ID: 2023.findings-emnlp.446 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기계 번역(MT) 시스템에 대한 행동 테스트는 언어 오류를 진단하고 NLP 모델의 능력을 평가하는 중요한 수단이다. 하지만 MT 시스템의 행동 테스트는 일반적으로 새로운 테스트 케이스에 대한 번역 품질을 평가하기 위해 사람의 노력이 필요하다. 이 논문은 MT 시스템의 행동 테스트를 수행하기 위해 새로운 BTPGBT (Bilingual Translation Pair Generation based Behavior Testing) 프레임워크를 제안한다. 
    2. BTPGBT의 핵심 아이디어는 고품질의 테스트 케이스와 유사 기준을 자동화하는 새로운 이중 번역 쌍 생성(BTPG) 접근 방식을 사용하는 것이다.
    3. 다양한 MT 시스템에 대한 실험 결과는 BTPGBT가 일반적인 오류 진단을 위한 포괄적이고 정확한 행동 테스트 결과를 제공할 수 있으며, 이로부터 몇 가지 유익한 결과를 얻을 수 있다는 것을 보여준다.

###### Retrieval-Augmented Few-shot Text Classification (https://aclanthology.org/2023.findings-emnlp.447/)
- Anthology ID: 2023.findings-emnlp.447 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 retrieval-augmented 방법은 retrieval 공간이 충분한 표준 시나리오에서 잘 작동하지만, 제한된 retrieval 공간을 가진 피실험자 시나리오에서는 실제로 실현하기 어렵다는 것을 이 논문은 보여준다. 
    2. 기본적인 metric을 사용하여 의미론적으로 유사한 예시를 검색하는 것은 불가능하며, task-specific retrieval metric을 학습하는 것이 중요하다. 
    3. 앵커에 기반한 loss를 최소화하여 학습하는 것은 약한 감독 신호와 경사 소실 문제 때문에 어렵다는 것을 심층적인 분석을 통해 보여주었고, 이를 해결하기 위해 EM 알고리즘과 랭크 기반 loss를 활용하는 두 가지 훈련 목표를 도입하였다.

###### Temporal Extrapolation and Knowledge Transfer for Lifelong Temporal Knowledge Graph Reasoning (https://aclanthology.org/2023.findings-emnlp.448/)
- Anthology ID: 2023.findings-emnlp.448 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 시간적인 지식 그래프(TKG)는 시간이 흐름에 따라 계속해서 새로운 개체와 사실이 나타나므로 미래 타임스탬프에 대해 예측하고 새로운 구성 요소에 대한 지식을 전송할 수 있는 모델이 필요하다.
    2. 우리는 '평생 TKG 추론'이라는 실제 문제를 수행하기 위해 시간 경로 기반 강화 학습(RL) 프레임워크를 제안한다.
    3. 실험 결과는 우리의 모델이 모든 기준 모델들보다 더 나은 성능을 보여준다.

###### Comparing Prompt-Based and Standard Fine-Tuning for Urdu Text Classification (https://aclanthology.org/2023.findings-emnlp.449/)
- Anthology ID: 2023.findings-emnlp.449 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 자연어 처리의 발전은 prompt 기반의 미세 조정(fine-tuning)의 효과를 보여준다. prompt 기반 미세 조정은 특정 언어와 태스크에 맞춘 prompt로 몇 개의 라벨링된 예제(few shot)와 함께 가이드를 제공한다.
    2. 저자들은 prompt 기반과 표준 미세 조정을 우르두어와 로마 우르두어 텍스트 분류 작업에서 비교하였다. 다섯 가지 데이터셋과 다국어 변환기를 사용하여 실험을 수행한 결과, prompt 기반 미세 조정은 표준 방식보다 최대 13%의 정확도 향상이 있었다.
    3. 이는 prompt 기반 미세 조정이 제한된 라벨 데이터를 가진 저자의 저-자원 언어에 대한 유망한 대안이 될 수 있다는 가능성을 시사한다.

###### Explore the Way: Exploring Reasoning Path by Bridging Entities for Effective Cross-Document Relation Extraction (https://aclanthology.org/2023.findings-emnlp.450/)
- Anthology ID: 2023.findings-emnlp.450 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Cross-document relation extraction (CodRED)은 different documents에서 언급된 두 entity 간의 관계를 추론하는 작업으로, 기존 연구들은 주로 implicit한 관계만을 포착했다. 그러나 사람들은 일반적으로 하이퍼링크나 추가적인 검색을 통해 explicit한 정보 체인을 활용하여 두 entity 간의 관계를 찾는다. 이에 영감을 받아 우리는 PILOT를 제안하여 문서 내부의 explicit한 단서 정보를 탐색하여 개선된 추론 경로를 제공한다."
    2. "PILOT는 entity 간 경로를 직접적으로 안내하는 bridging entity를 찾고 이를 원하는 경로를 탐색하는 데 사용한다. 우리는 PILOT로 구성된 모델이 CodRED 작업에서 기준 모델들을 능가한다는 것을 보여준다."
    3. "또한 PILOT을 통해 구축된 추론 경로의 타당성을 검증하기 위해 ChatGPT와 같은 대형 언어 모델을 사용한 평가 등 다양한 분석을 제공한다."

###### The student becomes the master: Outperforming GPT3 on Scientific Factual Error Correction (https://aclanthology.org/2023.findings-emnlp.451/)
- Anthology ID: 2023.findings-emnlp.451 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오류 수정 데이터셋을 생성하는 비용이 매우 높기 때문에 대부분의 사실적 주장 수정 방법은 강력한 검증 모델이 수정 프로세스를 안내하게 되어 있다. 이는 좋은 검증 모델이 항상 존재하지 않는 Scientific Claim Correction과 같은 도메인에서는 성능이 크게 하락하게 된다.
    2. 본 논문에서는 SciFix라는 검증기가 필요하지 않지만 기존 방법들보다 높은 성능을 내는 주장 수정 시스템을 소개한다. Fully supervised training과 regularization에 사용될 수 있는 풍부한 주석이 달린 데이터셋을 생성하기 위해 훈련 중 LLMs와 함께 prompting의 힘을 활용한다.
    3. 또한 주장 인식 디코딩 절차를 사용하여 수정된 주장의 품질을 개선한다. 우리의 방법은 주석이 달린 데이터셋을 생성하는 데 사용된 LLM인 GPT3.5 FewShot Prompting보다 성능이 우수하다. 이 모델은 우리의 모델보다 거의 800배 많은 파라미터를 사용했음에도 불구하고 향상된 수정 정확도(58%, 61% 및 64%)를 보여준다.

###### Leveraging Structured Information for Explainable Multi-hop Question Answering and Reasoning (https://aclanthology.org/2023.findings-emnlp.452/)
- Anthology ID: 2023.findings-emnlp.452 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)을 포함한 신경망 모델은 다중 홉 문제 해결에서 우수한 성능을 보이지만, 불명확한 추론, 환영증, 해석 가능성의 부족 등의 여러 가지 문제가 여전히 남아있다. 
    2. 그 대안으로 정보 추출 (IE)는 문자에 근거한 entity, relation, event 등을 식별한다. 추출된 구조적 정보는 사람과 기계에 의해 쉽게 해석될 수 있으며, 이를 활용하여 다중 홉 질문 답변에서 구성 및 활용할 수 있다. 
    3. 실험 결과와 인간 평가를 통해 논문의 프레임워크가 더 정확한 추론 체인을 생성하고 두 개의 벤치마크 데이터셋에서 QA 성능을 크게 향상시킨다는 것을 보였으며, 추출된 구조 자체만으로도 생성된 추론 체인 및 중요도 기반 설명보다 인간에게 더 선호되는 근거화된 설명을 제공한다.

###### Hierarchical Catalogue Generation for Literature Review: A Benchmark (https://aclanthology.org/2023.findings-emnlp.453/)
- Anthology ID: 2023.findings-emnlp.453 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 과학적인 논문 리뷰 생성은 다량의 참고 논문에서 중요한 정보를 추출하고 정리하여 해당 리뷰를 생성하는 것을 목표로 한다. 하지만 명확하고 논리적인 계층이 부족한 상태에서 이를 수행하기 어렵다. 우리는 고품질의 카탈로그를 활용한 리뷰 생성 과정이 이 문제를 효과적으로 완화시킬 수 있다고 관찰했다. 
    2. 따라서, 우리는 리뷰 생성을 위한 첫 단계로 "Hierarchical Catalogue Generation for Literature Review"라는 어려운 작업을 소개한다. 이 작업은 다양한 참고 자료를 가지고 리뷰 논문의 계층적 카탈로그를 생성하는 것을 목표로 한다. 
    3. 우리는 7.6k개의 리뷰 카탈로그와 389k개의 참고 논문을 포함한 새로운 영어 리뷰 카탈로그 데이터셋을 구축했다. 또한, 이 작업을 정확히 평가하기 위해 의미론과 구조에서의 정보성과 ground truth와의 유사성을 평가하기 위한 두 가지 평가 메트릭을 설계했다. 우리의 광범위한 분석은 데이터셋의 고품질과 평가 메트릭의 효과적인 성능을 입증하고 있다.

###### MCC-KD: Multi-CoT Consistent Knowledge Distillation (https://aclanthology.org/2023.findings-emnlp.454/)
- Anthology ID: 2023.findings-emnlp.454 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 큰 언어 모델들은 chain-of-thought(prompting)을 통해 복잡한 추론 능력을 보여주고 있다. 이 논문에서는 이러한 추론 능력을 작은 모델로 전달하는 데에 초점을 맞춰 다양성과 일관성을 강화하는 Multi-CoT Consistent Knowledge Distillation (MCC-KD)를 제안한다.
    2. MCC-KD에서는 각 질문에 대해 여러 개의 추론을 생성하고, 답변 분포 간의 양방향 KL-divergence를 최소화함으로써 추론의 일관성을 강제한다.
    3. 실험 결과, MCC-KD는 다양한 모델 아키텍처(LLaMA/FlanT5)와 다양한 모델 크기(3B/7B/11B/13B)에서 수학적 추론과 상식적 추론 벤치마크에서 뛰어난 성능을 보이며, 일반화 능력도 강하다.

###### An Empirical Study of Frame Selection for Text-to-Video Retrieval (https://aclanthology.org/2023.findings-emnlp.455/)
- Anthology ID: 2023.findings-emnlp.455 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Text-to-video retrieval (TVR)는 쿼리 텍스트가 주어졌을 때 큰 비디오 갤러리에서 가장 관련 있는 비디오를 찾는 것을 목표로 한다. 
    2. 기존 방법들은 일련의 비디오 콘텍스트를 처리하기 위해 비디오 내 프레임의 부분집합을 선택하는데, 이 선택 방법은 비디오의 의미 정보를 보존하면서 시간적으로 중복되는 프레임을 제거하여 검색 효율성을 향상시키는 데 중요하다.
    3. 이 논문에서는 TVR을 위한 프레임 선택의 첫 번째 경험적 연구를 수행하였으며, 프레임 선택 방법을 효과와 효율성 측면에서 체계적으로 분석하였다. 제안된 프레임 선택 기법은 검색 효율성을 향상시키면서 검색 성능을 희생하지 않을 수 있다는 것을 실험적으로 확인하였다.

###### Conditional Natural Language Inference (https://aclanthology.org/2023.findings-emnlp.456/)
- Anthology ID: 2023.findings-emnlp.456 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 서로 다른 조건에 대해 상반되는 정보를 제공하는 문장 쌍을 올바르게 설명하기 위해, 조건부 자연어 추론 (Cond-NLI) 작업을 소개하고 문장 쌍에서 상반되는 측면과 해당 조건을 자동으로 추출하는 것에 초점을 맞추고 있다.
    2. Cond-NLI는 특정 조건을 다루는 각자 다른 답변을 가진 다중 답변 질문이나 다른 조건에 대한 서로 다른 의견을 가진 리뷰와 같은 다양한 정보를 제공하는 데 도움이 될 수 있다.
    3. 우리는 일반적으로 사용되는 특징-기여 설명 모델이 특히 문장이 길고 독립적으로 작성될 때 조건을 찾는 데 적합하지 않음을 보여준다. 우리는 토큰 수준 주석을 필요로하지 않으면서 조건을 성공적으로 추출할 수있는 간단하고 효과적인 모델을 제안한다.

###### Contrastive Distant Supervision for Debiased and Denoised Machine Reading Comprehension (https://aclanthology.org/2023.findings-emnlp.457/)
- Anthology ID: 2023.findings-emnlp.457 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "원격 감독 (Distant Supervision)은 쉽게 얻을 수 있는 질문-답변 쌍을 활용한 MRC(Machine Reading Comprehension)에 대한 유망한 학습 방법이다. 그러나 휴리스틱하게 주석을 단 데이터셋은 불가피하게 잘못된 라벨링을 초래하여 답변 편향과 맥락 잡음 문제를 야기한다."
    2. "이 논문에서는 CDS (Contrastive Distant Supervision)라는 알고리즘을 제안하는데, 신뢰도를 고려한 대조 학습을 통해 혼돈과 잡음이 섞인 인스턴스를 구분하는 방법을 학습한다."
    3. "실험 결과는 CDS가 효과적이며, 수동 주석 없이도 지도 학습된 MRC 모델을 능가할 수 있다는 것을 보여준다."

###### KEPLET: Knowledge-Enhanced Pretrained Language Model with Topic Entity Awareness (https://aclanthology.org/2023.findings-emnlp.458/)
- Anthology ID: 2023.findings-emnlp.458 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근엔 PLM(Pre-trained Language Models)들이 효율성을 보이는데, KE(지식 증강) PLM들은 Wikipedia 같은 entity-rich한 텍스트 자료에서 토큰 간 및 언급된 entity들과 상호작용을 고려하여 pre-training한다. 
    2. 하지만 기존의 KEPLM들은 Wikipedia의 특별한 레이아웃을 간과하여 entity 상호작용이 충분치 않고 biased한 (relation) word semantics을 가지게 된다. 
    3. 따라서 이 논문에서는 topic entity를 고려한 KEPLET를 제안하며, Wikipedia 문장에서 topic entity 정보를 어디에 추가해야 하는지 식별하고, 해당 정보를 token과 entity의 표현에 통합시켜줌으로써 전체 네트워크 학습에 topic entity를 고려시키는 방법을 제시한다.

###### Revisiting Large Language Models as Zero-shot Relation Extractors (https://aclanthology.org/2023.findings-emnlp.459/)
- Anthology ID: 2023.findings-emnlp.459 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 관계 추출 (RE)은 레이블이나 레이블이 없는 데이터를 일정한 정도로 필요로 하는데, 최근의 연구에서는 대규모 언어 모델 (LLM)이 자연어 프롬프트를 통해 즉시 새로운 작업으로 전이될 수 있음을 보여주었다. 이 논문에서는 ChatGPT와 같은 LLM을 zero-shot 관계 추출기로 탐구한다.
    2. 논문에서는 기존의 관계 추출 프롬프트의 단점을 분석하고, chain-of-thought (CoT)와 같은 최근 프롬프트 기술을 채용하여 zero-shot 관계 추출을 개선하려고 시도한다. 이를 위해 QA 형식의 효과적인 질문으로 RE 입력을 재귀적으로 변환하는 SumAsk 프롬프트를 제안한다.
    3. 다양한 벤치마크와 설정에서 종합적인 실험을 수행한 결과, SumAsk는 다양한 모델 크기, 벤치마크 및 설정에서 LLM의 성능을 일관되고 유의미하게 향상시키며, ChatGPT의 zero-shot 프롬프트는 zero-shot과 완전 지도 방법과 경쟁력 있는 또는 우수한 결과를 달성한다. 또한, LLM은 중첩 관계를 추출하는 데 유망한 성능을 보이며, 서로 다른 관계에 따라 성능이 크게 다르다.

###### Multi-Stage Pre-training Enhanced by ChatGPT for Multi-Scenario Multi-Domain Dialogue Summarization (https://aclanthology.org/2023.findings-emnlp.460/)
- Anthology ID: 2023.findings-emnlp.460 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 대화 요약 방법들은 특정 시나리오나 도메인에만 적용되는 한계가 있다.
    2. 이 연구에서는 다중 시나리오 다중 도메인 대화 요약을 위한 새로운 사전 훈련 모델을 제안한다.
    3. 실험 결과, 우리의 사전 훈련 모델은 전체 fine-tuning, zero-shot, few-shot 설정에서 이전의 최첨단 모델들보다 크게 우수한 성능을 보였다.

###### Towards large language model-based personal agents in the enterprise: Current trends and open problems (https://aclanthology.org/2023.findings-emnlp.461/)
- Anthology ID: 2023.findings-emnlp.461 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델(LLMs)을 사용하여 복잡한 목표에 대해 추론하고 목표를 달성하기 위해 일련의 도구나 API를 조율하는 경향이 있다. 그러나 이러한 기능은 미션 크리티컬한 기업 환경에서 사용하기에는 아직 준비되지 않았다.
    2. 이 논문은 LLM 기반의 자율 에이전트 및 도구 합성에 대한 예시를 제시하고 실패하는 경우를 강조하며, 최근 노력들을 조사하고 이러한 솔루션을 기업에 적합하게 만들기 위한 연구 과제를 제시한다.
    3. NLP 연구에서는 신뢰성과 설명 가능성, 일관성과 재현성, 가드레일 및 정책 준수, 합성 도구 설계를 위한 모범 사례, 새로운 메트릭 및 벤치마크 등 여러 개의 개방된 문제들이 있다.

###### CREATOR: Tool Creation for Disentangling Abstract and Concrete Reasoning of Large Language Models (https://aclanthology.org/2023.findings-emnlp.462/)
- Anthology ID: 2023.findings-emnlp.462 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large Language Models, LLMs)은 API의 한계와 암묵적 추론의 불안정성으로 인해 한계가 있다고 알려져 있다. 이 논문에서는 CREATOR라는 새로운 프레임워크를 제안하여 LLMs가 문서와 코드 실현을 통해 자체 도구를 만들 수 있게 한다.
    2. CREATOR를 MATH와 TabMWP 벤치마크에서 평가한 결과, 기존의 사고 과정, 프로그램 과정 등과 비교해 성능이 우수하다는 것을 보였다. 또한, 창조적 도전(Dataset, Creation Challenge)을 소개하여 LLMs의 도구 창조 능력의 필요성과 이점을 강조한다.
    3. 추가적인 연구에서는 LLMs를 도구 생성자로 활용함으로써 지식 전달을 용이하게 하고, LLMs는 다양한 상황에 적응할 수 있는 도구 창조의 능력을 가지고 있음이 확인되며, 문제 해결 시 paradigm을 혁신시킨다는 것을 보여준다.

###### Query-based Image Captioning from Multi-context 360cdegree Images (https://aclanthology.org/2023.findings-emnlp.463/)
- Anthology ID: 2023.findings-emnlp.463 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 360도 이미지는 한 장의 캡션으로 모든 문맥을 설명하기 어렵기 때문에, 이를 해결하기 위해 Query-based Image Captioning (QuIC)이라는 새로운 작업을 제안한다. 이 작업은 360도 이미지에 대한 미세한 장면 이해를 요구하여 사용자 의도에 맞는 내용을 선택하는 데 어려움이 있다.
    2. 우리는 이 작업을 위한 데이터셋을 구축하였고, 실험 결과 이 데이터셋을 기반으로 이미지 캡션 모델을 fine-tuning하면 360도 이미지의 다양하고 제어 가능한 캡션을 생성할 수 있다.
    3. 기존의 이미지 캡션 작업과 비교하여 이 작업은 더 도전적이며, 사용자의 의도에 맞는 다양한 문맥에서의 캡션을 생성하는 능력이 필요하다.

###### Auto Search Indexer for End-to-End Document Retrieval (https://aclanthology.org/2023.findings-emnlp.464/)
- Anthology ID: 2023.findings-emnlp.464 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구에서는 모든 문서를 모델에 인코딩하고 직접 검색된 문서를 생성하는 generative retrieval이라는 새로운 고급 패러다임에 대한 관심이 증가하고 있으나, 이 방법은 아직 "전처리된" 문서 식별자 (docids)에 많이 의존하므로, 검색 성능과 새로운 문서 검색 능력에 제한이 있다.
    2. 본 논문에서는 새로운 완전한 end-to-end 검색 패러다임을 제안한다. 이는 의미적 색인 모듈을 통해 기존 및 새로운 문서의 최적의 docids를 자동으로 학습하고, encoder-decoder 기반 generative model인 Auto Search Indexer (ASI)를 통해 end-to-end 문서 검색을 수행할 수 있다.
    3. 또한, 위의 두 모듈을 결합하기 위해 리파라미터화 메커니즘을 설계하여 공동 최적화 프레임워크로 만든다. 실험 결과는 우리의 모델이 공개 및 산업용 데이터셋에서 선진적인 기준 모델에 비해 우수함을 보여주며, 새로운 문서 처리 능력을 검증한다.

###### ‘Person’ == Light-skinned, Western Man, and Sexualization of Women of Color: Stereotypes in Stable Diffusion (https://aclanthology.org/2023.findings-emnlp.465/)
- Anthology ID: 2023.findings-emnlp.465 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 Stable Diffusion이 성별 및 국적/대륙 식별에 관련된 편견을 어떻게 내포하고 있는지 조사하였다. 그 결과 Stable Diffusion은 별도의 정보 없이 '사람' 또는 '아시아 출신 사람'에 대해 어떤 성별과 국적/대륙 식별을 부여하는지 알 수 있다. Stable Diffusion은 '사람'에 대한 결과로 가장 가깝게 남성의 이미지(평균 유사도 0.64)와 가장 거리가 먼 비이진 성별의 사람의 이미지(평균 유사도 0.41)와, 유럽/북미 (각각 평균 유사도 0.71과 0.68)에 대한 이미지와, 아프리카/아시아 (각각 평균 유사도 0.43과 0.41)에 대한 이미지와 가장 일치하는 것으로 나타났다. 이 결과는 Stable Diffusion이 사람을 유럽/북미 남성으로 표현하는 경향을 나타낸다.
    2. 또한, 대륙적 편견과 그로 인한 피해를 보여준다. 예를 들어, 오세아니아 출신 사람은 팬더(예)로 간주되며 평균 유사도는 파푸아뉴기니인의 경우 0.31에 비해 오스트레일리안/뉴질랜드인의 경우 0.77과 0.74로 높게 나타났다. 이는 오세아니아 원주민들의 지워짐을 나타내며, 실제로 파푸아뉴기니와 오세아니아 전체에서 식민지 정착민의 후손보다 원주민들이 더 많다는 사실을 고려하지 않고 있다.
    3. 마지막으로, 라틴 아메리카, 멕시코, 인도, 이집트 여성들의 성적 대상화 패턴을 뜻하는 의외로 여성들의 성적 대상화 문제를 확인하였다. 이는 NSFW 검출기를 통해 확인되었으며 수동 검토로 확인되었다. 이는 Stable Diffusion이 매체에서 유색 여성을 사물화하여 서양의 페티쉬화를 지속시키고 있다는 것을 보여준다. 이러한 편견적인 표현은 점검되지 않으면 심화될 것이다.

###### Task-Attentive Transformer Architecture for Continual Learning of Vision-and-Language Tasks Using Knowledge Distillation (https://aclanthology.org/2023.findings-emnlp.466/)
- Anthology ID: 2023.findings-emnlp.466 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 사전 훈련된 신경망의 크기와 계산 부하는 많은 응용에서 기계학습 도입의 두 가지 주요 장애물이 되고 있다. 이 논문에서는 sequential task들 간 지식 전달을 가능하게 하는 Continual Learning(CL)을 통해 이 문제를 해결하는데, 기존 CL 알고리즘들은 주로 단일 시각 또는 언어 태스크를 고려한다.
    2. 우리는 동적으로 학습 가능한 매개변수의 수를 증가시키고 지식 증류(knowledge distillation)를 사용하여 비모달 시각-언어 태스크를 학습하기 위한 transformer 기반 CL 아키텍처를 개발한다. 추가 매개변수는 각 태스크에 대해 네트워크를 특화시키는 데 사용된다.
    3. 우리의 접근 방식은 치명적인 Forgetting(catastrophic forgetting)의 도전을 해결하면서 태스크간의 정보 공유를 가능하게 한다. 우리의 모델은 적은 메모리와 시간 오버헤드를 필요로 하기 때문에 다수의 태스크에 대한 확장성 있는 학습을 가능하게 한다. 또한, 우리의 모델은 어려운 시각-언어 태스크에서 최고 성능에 도달한다.

###### Evaluating Verifiability in Generative Search Engines (https://aclanthology.org/2023.findings-emnlp.467/)
- Anthology ID: 2023.findings-emnlp.467 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신뢰할 수 있는 생성 검색 엔진은 높은 사실 인용률과 정확도를 가지는 것이 필수적이다. 지금까지의 생성 검색 엔진들은 정보성과 유창성은 있으나, 지지되지 않은 문장과 부정확한 인용을 자주 포함한다. 이러한 결과는 정보를 찾는 사용자에게 불신과 불신을 주는 결괏값이며, 이에 대응하기 위해 신뢰할 수 있는 생성 검색 엔진의 개발을 촉진하고 기존 상업적 시스템의 부족점을 명확히하기 위해 기여하길 바란다.
    
    2. 인용률과 정확도가 높은 생성 검색 엔진은 사용자가 정보를 확인하는 데 중요한 역할을 하는데, 기존의 생성 검색 엔진들은 지원되지 않은 문장과 부정확한 인용을 자주 함께 포함한다. 
    3. 따라서 이 논문에서는 네 가지 인기 있는 생성 검색 엔진에 대한 사람에 의한 심사를 실시하여, 그들의 결괏값이 정보를 찾는 사용자에게 신뢰성을 제공하는 역할을 적절히 수행할 수 있는지 확인하였다.

###### Enhancing Abstractiveness of Summarization Models through Calibrated Distillation (https://aclanthology.org/2023.findings-emnlp.468/)
- Anthology ID: 2023.findings-emnlp.468 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. DisCal은 생성된 요약문의 정보성을 희생하지 않고 요약문의 추상적 수준을 높이기 위한 혁신적인 접근 방식이다. 
    2. DisCal은 두 가지 감독을 통해 다양한 가짜 요약문을 만들고, 가장 추상적이고 정보성이 높은 가짜 요약문을 찾아 sequence-level distillation에 사용한다. 
    3. 실험결과, DisCal은 요약문의 추상성과 정보성에서 이전 방법들보다 우수한 성능을 보여준다.

###### Visually Grounded Continual Language Learning with Selective Specialization (https://aclanthology.org/2023.findings-emnlp.469/)
- Anthology ID: 2023.findings-emnlp.469 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시각적인 세계에서 작동하는 인공 에이전트의 바람직한 특성은 각각의 작업에 충분히 전문화하면서 전이 가능한 일반화된 지식을 구축하며 언어로 정보화된 작업의 연속적인 학습을 지속적으로 할 수 있는 것이다.
    2. 선택적 전문화는 각 작업에 대해 모델 구성 요소를 신중하게 선택하여 이러한 트레이드오프에 대한 통제를 제공하는 전략이다.
    3. 이 논문은 시각적으로 기반을 둔 지속적인 언어 학습을 위한 선택 전략의 철저한 모델 분석을 제공하고, 이를 통해 공통된 지속적인 학습 기준선을 능가하는 개념적으로 간단한 접근 방식을 개발하여 실험했다. 이들의 결과는 개별 모델 부분의 학습 특성에 더 잘 부합하는 지속적인 학습 알고리즘을 위해 더 많은 노력이 필요함을 보여준다.

###### RoMQA: A Benchmark for Robust, Multi-evidence, Multi-answer Question Answering (https://aclanthology.org/2023.findings-emnlp.470/)
- Anthology ID: 2023.findings-emnlp.470 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. RoMQA는 위키데이터 지식 그래프에서 추출한 관련 제약 조건을 기반으로 생성된 강건하고 다중 증거를 포함한 질문 응답(QA)에 대한 첫 번째 벤치마크입니다.
    2. RoMQA는 이전 QA 데이터셋과 비교하여 더 많은 증거 텍스트에 대한 추론과 평균적으로 많은 정답을 요구하는 사람이 만든 질문을 포함하고 있습니다.
    3. RoMQA를 사용하여 수행된 실험 결과, 현재 모델은 질문 제약 조건의 변화에 견고하지 않지만 관련 질문의 클러스터를 튜닝함으로써 더 견고하게 만들 수 있다는 것을 보여줍니다.

###### Leveraging Multiple Teachers for Test-Time Adaptation of Language-Guided Classifiers (https://aclanthology.org/2023.findings-emnlp.471/)
- Anthology ID: 2023.findings-emnlp.471 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구들은 langauge-guided classifier에 의해 task-specific한 자연어 설명이 주어질 때 새로운 태스크의 예제를 분류하는 방법을 탐구하였으나, 이들의 성능은 언어 설명에 따라 예측할 수 없는 방식으로 많이 다르다고 보고되고 있다.
    2. 이 논문에서는 TALC라는 프레임워크를 소개하는데, 이는 여러 가르치는 선생님들의 설명과 라벨이 없는 테스트 예제들을 활용하여 새로운 태스크에 language-guided classifier를 적응시킨다.
    3. 실험 결과에서 TALC가 이전 연구에 비해 상대적으로 9.3% 좋은 성능을 보이며, 수질과 수량이 다른 설명에도 강건하다는 것을 보여주고 있다.

###### Summarizing Multiple Documents with Conversational Structure for Meta-Review Generation (https://aclanthology.org/2023.findings-emnlp.472/)
- Anthology ID: 2023.findings-emnlp.472 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. PeerSum은 학술논문의 meta-reviews를 생성하기 위한 새로운 데이터셋으로, 논문 요약, 리뷰, 다중 대화의 성격을 가진다. 이러한 정보들은 전문가들에 의해 평가된 메타데이터와 함께 풍부한 관계를 가진다.
    2. 우리는 hierarchical한 대화 구조와 희소 어텐션을 활용하는 모델인 RAMMER를 제안하였으며, 이 모델은 메타데이터 특징을 예측하는 다중 태스크 훈련 목적으로 학습된다.
    3. 실험 결과, RAMMER는 기존의 강력한 기준 모델들보다 자동 평가 메트릭에서 우수한 성능을 보이지만, 충돌하는 정보를 처리하는 데 어려움을 겪는다는 한계가 있어서 meta-review 생성은 어려운 과제이며 더 많은 연구가 필요하다는 것을 알 수 있다.

###### VIPHY: Probing “Visible” Physical Commonsense Knowledge (https://aclanthology.org/2023.findings-emnlp.473/)
- Anthology ID: 2023.findings-emnlp.473 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Vision-language models (VLMs)는 시각적 추론 작업에서 놀라운 성능을 보이며, 이러한 작업은 시각적 사례를 기반으로 그 사례를 해석하고 추론하는 데 필요한 지식을 측정한다. 그러나 VLM의 지식을 보존하고 일반화하는 능력은 평가되지 않았다.
    2. 본 연구에서는 VLM의 "보이는" 물리적 지식 - 정지된 장면의 이미지로부터 쉽게 얻을 수 있는 정보 (객체의 색상, 크기, 공간 등) - 을 평가한다.
    3. 우리는 자동 파이프라인을 구축하여 VLM의 성능을 평가하고, 모델과 인간의 성능 사이에 심각한 격차가 있음을 보여준다. 또한, 언어에 기반한 사전 훈련 모델이 크기와 공간 작업에서 VLM보다 훨씬 우수한 성능을 보여줌으로써, VLM이 이러한 지식을 보존하는 데 어려움을 겪는다는 사실을 강조한다.

###### Two Directions for Clinical Data Generation with Large Language Models: Data-to-Label and Label-to-Data (https://aclanthology.org/2023.findings-emnlp.474/)
- Anthology ID: 2023.findings-emnlp.474 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLMs (Large Language Models)는 희귀하고 민감하며 불균형한 의료 데이터가 있는 임상 텍스트 마이닝 분야에 대한 잠재력이 미개척되어 있다. 
    2. 우리는 AD(알츠하이머 병)-관련 증상 감지를 위한 LLM의 임상 데이터 보강 가능성을 조사한다.
    3. 우리의 연구에서, 전문가의 지식을 통해 AD 증상 진행에 대한 실용적인 분류법과 3개의 데이터셋을 생성하여 진행하였다.
    
    1. 기존 금 데이터셋만 사용한 시스템과 비교하여, 실버와 브론즈 데이터셋은 시스템 성능을 향상시키는 것이 확인되었다.
    2. 이는 LLMs가 전문가 지식을 통합하여 복잡한 과제에 대한 합성 임상 데이터를 생성할 수 있다는 것을 보여준다.
    3. 또한 우리의 라벨-투-데이터 방법은 민감한 정보 없이 적절한 품질을 유지하는 데이터셋을 생성할 수 있다.
    
    (Note: The translation for "label-to-data method" is customized to fit the context better)

###### Stylized Dialogue Generation with Feature-Guided Knowledge Augmentation (https://aclanthology.org/2023.findings-emnlp.475/)
- Anthology ID: 2023.findings-emnlp.475 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 스타일화된 대화 생성 시스템은 원하는 스타일을 효과적으로 재현하면서 일관성있고 문맥에 맞는 대화를 생성하는 것을 목표로 한다. 
    2. 이 논문에서는 특징 기반 스타일 지식 선택 모듈을 포함한 지식증강된 스타일화된 대화 생성 모델을 제안한다.
    3. 실험 결과, 우리의 방법은 두 가지 공개된 스타일화된 대화 벤치마크에서 자동화 및 인간평가 모두에서 만족스러운 성능을 보여준다.

###### Probing LLMs for Joint Encoding of Linguistic Categories (https://aclanthology.org/2023.findings-emnlp.476/)
- Anthology ID: 2023.findings-emnlp.476 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLMs)은 사전 훈련 과정에서 얻은 일반적인 언어 지식으로 인해 NLP 과제에서 인상적인 성능을 발휘합니다. 그러나 LLM 계층에서는 언어적 계층 구조가 형성되고, 하위 계층에서는 구문 작업에 더 적합하고 상위 계층에서는 의미 처리에 사용된다는 것을 알 수 있습니다. 하지만 다른 언어 현상의 인코딩이 모델 내에서 어떻게 상호 작용하며 얼마나 많이 언어 관련 범주의 처리가 동일한 모델 표현에 의존하는지에 대해서는 잘 알려져 있지 않습니다. 
    2. 이 논문에서는 LLMs에서 언어 범주의 공동 인코딩을 테스트하는 프레임워크를 제안합니다. 구문에 초점을 맞추어, 우리는 동일한 언어적 계층의 일부 (관련된 품사 (POS) 클래스) 및 서로 다른 언어적 계층의 일부 (품사 클래스 및 관련 구문 종속성 관계)에서 공동 인코딩의 증거를 찾을 수 있었습니다.
    3. 우리의 다국어 실험은 다국어 LLM에서 동일한 패턴이 나타남을 보여줍니다.

###### On Robustness of Finetuned Transformer-based NLP Models (https://aclanthology.org/2023.findings-emnlp.477/)
- Anthology ID: 2023.findings-emnlp.477 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. BERT, GPT-2, T5 같은 transformer-based pre-trained model들은 많은 NLP 태스크에 대해 fine-tuning 되었고, 매우 효과적임이 알려져 있다. 그러나, fine-tuning 과정에서 이러한 모델들의 layer 별 변화는 연구되지 않았다. 
    2. 이 논문에서는 두가지 metric인 CKA와 STIR을 사용하여 pre-trained와 fine-tuned 언어 모델의 표현 사이의 변화를 특성화하였다. 더 나아가, 여덟 가지 다른 텍스트 변형에 대해 BERT, GPT-2, T5 세 가지 언어 모델의 견고성을 연구하였다.
    3. GPT-2의 표현은 BERT와 T5에 비해 여러 유형의 입력 변형에 대해 더 견고했다. 전반적으로 모델은 큰 변형에도 견고하게 작동하지만, 명사를 제거하거나 동사를 변경하는 것이 가장 영향력이 크다. 이 연구는 인풋 데이터를 전달할 때 고려해야 하는 transformer-based 모델들의 특정 취약점에 대한 유용한 통찰력을 제공한다.

###### Measuring and Mitigating Constraint Violations of In-Context Learning for Utterance-to-API Semantic Parsing (https://aclanthology.org/2023.findings-emnlp.478/)
- Anthology ID: 2023.findings-emnlp.478 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실행 가능한 과제 중심의 의미 파싱에서, 시스템은 사용자의 자연어 발화를 머신이 해석할 수 있는 프로그램(API 호출)으로 번역하는데 목적이 있다. LLMs의 인컨텍스트 학습은 데이터 제한적인 상황에서 강력한 기준으로 작용하며, 이와 관련된 과제에서도 강력한 기준을 제공함을 보여준다. 하지만 LLMs은 환각(hallucinate)하는 경향이 있어서 생성된 내용을 제한하는 것에 대한 도전 과제를 제기한다.
    2. 이 연구에서는 API-CD(API-aware Constrained Decoding) 및 SRD(Semantic-Retrieval of Demonstrations)라는 두 가지 방법을 조사하여 사전 정의된 API의 구조 및 과제에 대한 제약을 적극 활용하는데 대한 효과를 측정하고 분석한다.
    3. 실험 결과, 이러한 전략이 제약 사항 위반을 줄이고 생성된 API 호출의 품질을 개선하는 데 효과적이지만, 구현 복잡성과 대기 시간을 고려해야 한다는 것을 알 수 있다.

###### Entity Disambiguation on a Tight Labeling Budget (https://aclanthology.org/2023.findings-emnlp.479/)
- Anthology ID: 2023.findings-emnlp.479 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 NLP 애플리케이션에서는 작은 라벨링 예산으로 특정 도메인의 entity disambiguation 모델을 훈련하는 어려움이 있다. 따라서 이 논문에서는 특징 다양성과 낮은 rank 방법을 결합한 해결책을 제안한다.
    2. 텐서 모델의 맥락에서 제안한 샘플링 전략은 특징 다양성과 낮은 rank 보정을 조합한 것이다.
    3. 실험 결과, 제안한 접근법은 주어진 성능을 달성하기 위해 필요한 라벨링된 데이터 양을 크게 줄일 수 있다.

###### Topic-DPR: Topic-based Prompts for Dense Passage Retrieval (https://aclanthology.org/2023.findings-emnlp.480/)
- Anthology ID: 2023.findings-emnlp.480 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전 연구들은 단일 벡터로 연속적인 prompt를 최적화하여 사전 훈련된 언어 모델의 의미 이해력을 향상시키는 것에 주로 초점을 맞추었으나, 이러한 방식은 의미 공간의 붕괴를 유발한다. 그 결과, 동일한 의미 정보가 모든 표현들에 스며들어 그 분포가 제한된 영역에서 수렴하게 되어 밀집 검색 도중에 관련성 없는 패스와 관련성 있는 패스를 구분하기 어렵게 한다.
    2. 이러한 문제에 대응하기 위해 우리는 Topic-DPR이라고 불리는 밀집 패스 검색 모델을 제안한다. 단일한 prompt 방법과 달리, 다중 주제 기반 prompt가 확률적 simplex 상에 구성되고, 대조 학습을 통해 동시에 최적화된다. 이러한 방식은 표현들이 주제의 분포와 일치하도록 유도하여 공간의 균일성을 향상시킨다.
    3. 더 나아가, 우리는 반구조적 데이터를 활용한 새로운 양성 및 음성 샘플링 전략을 도입하여 밀집 검색 효율을 향상시킨다. 두 개의 데이터셋에서의 실험 결과는 우리의 방법이 이전의 최첨단 밀집 검색 기법을 능가한다는 것을 확인한다.

###### Quantifying the Dialect Gap and its Correlates Across Languages (https://aclanthology.org/2023.findings-emnlp.481/)
- Anthology ID: 2023.findings-emnlp.481 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 도구를 소수 언어 변형 (예: 푸에르토리코 스페인어 또는 스위스 독일어)에 적용할 때 품질이 감소하는 경향이 있지만, 이와 관련된 연구는 일부 언어에만 국한되어 있다. 
    2. 이 논문에서는 대표적인 large language models (LLMs)를 통해 수많은 고/저 정보 리소스 언어의 지역 방언에서의 기능을 평가하고, 경제, 사회, 언어적 요인과의 연관성을 분석한다. 
    3. 훈련 데이터의 영향은 모델이나 언어에 따라 일관되지 않으므로, 방언 간 격차를 해소하기 위해 일반적인 접근 방식이 적용될 수 없다는 것을 보여준다. 이 연구는 명심하며 데이터 수집을 통해 불균형을 해소하기 위한 가능한 방법들을 찾아낼 수 있는 방언 NLP 분야의 기반을 마련한다.

###### RECAL: Sample-Relation Guided Confidence Calibration over Tabular Data (https://aclanthology.org/2023.findings-emnlp.482/)
- Anthology ID: 2023.findings-emnlp.482 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 가장 최근의 기계 학습 방법들은 신용 모델링이나 금융 사기 탐지와 같이 높은 위험성을 가진 애플리케이션에 필요한 정확한 신뢰도 측정을 제공하지 못하고 있다.
    2. 이 논문은 실제 세계의 탭형 데이터셋은 일반적으로 암시적인 샘플 관계를 포함하고 있으며, 이는 더 정확한 추정을 얻는데 도움이 될 수 있다는 것을 발견하였다.
    3. 이를 위해, 우리는 RECAL이라는 일반적인 사후 훈련 신뢰도 보정 프레임워크를 소개하고, 그래프 신경망을 사용하여 다른 샘플들 사이의 관계를 모델링하여 현재 기계 학습 모델의 예측 신뢰도를 교정한다.

###### Parameter-Efficient Cross-lingual Transfer of Vision and Language Models via Translation-based Alignment (https://aclanthology.org/2023.findings-emnlp.483/)
- Anthology ID: 2023.findings-emnlp.483 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 Pre-trained vision and language models이 다른 언어를 지원하기 위한 연구들은 모델의 성능에 불균형이 생길 수 있는 리소스의 문제로 인해 불완전했다. 
    2. 따라서, 저희는 번역 기반의 정렬 방법을 활용하여 여러 언어 간의 불균형을 완화시키고, 파라미터 효율적인 fine-tuning 방법을 탐구하는 새로운 작은 자원을 사용하는 크로스-언어 전이 학습 프레임워크를 제안한다. 
    3. XTD와 Multi30K 데이터셋에서 수행한 실험 결과, 우리의 프레임워크는 다양한 언어 간의 불균형을 크게 줄이고, 저자원 시나리오에서 특히 크로스-언어 전이 결과를 향상시킬 수 있음이 입증되었다.

###### Lexical Repetitions Lead to Rote Learning: Unveiling the Impact of Lexical Overlap in Train and Test Reference Summaries (https://aclanthology.org/2023.findings-emnlp.484/)
- Anthology ID: 2023.findings-emnlp.484 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이상적인 요약 모델은 참조 훈련 요약을 외우는 대신 새로운 요약 가능한 콘텐츠에 일반화되어야 한다. 이 논문에서는 훈련 요약과 테스트 요약 간의 어휘적 유사성에 따라 테스트 세트를 분할하여 성능을 평가하는 세분화된 평가 프로토콜을 제안한다.
    2. 이 논문에서는 훈련 반복이 모델이 외워지거나 사실적인 오류와 같은 데이터 아티팩트를 재생하도록 만드는 문제를 지적하고, 새로운 테스트 케이스에서의 성능을 향상시키기 위해 훈련 요약에서 어휘 반복을 제한하는 방법을 제안한다.
    3. 새로운 테스트 하위집합과 최근 뉴스 기사에 대한 자동 및 인간 평가 결과, 훈련 요약에서 어휘 반복을 제한함으로써 외우기 공부를 방지하고 일반화를 향상시킬 수 있다는 것을 보여준다.

###### Pseudointelligence: A Unifying Lens on Language Model Evaluation (https://aclanthology.org/2023.findings-emnlp.485/)
- Anthology ID: 2023.findings-emnlp.485 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델들이 많은 벤치마크에서 인간의 성능을 뛰어넘는 반면, 우리는 모델 능력의 타겟화된 평가를 위해 원칙적인 접근 방식을 취해야 한다.
    2. 우리는 의사난수성에 영감을 받아 "의사지성"을 제안하며, "(인지된) 지성은 평가자의 시각에 달려있다"는 원칙을 포착한다.
    3. 우리는 모델과 학습된 평가자 간의 동적 상호작용으로 구성된 복잡성 이론적인 모델 평가 프레임워크를 제안하며, 이 프레임워크가 언어 모델 평가의 두 가지 사례를 추론하고 기존 평가 방법을 분석하는 데 사용될 수 있음을 보여준다.

###### GDA: Grammar-based Data Augmentation for Text Classification using Slot Information (https://aclanthology.org/2023.findings-emnlp.486/)
- Anthology ID: 2023.findings-emnlp.486 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구들은 자연어 처리 과제에서의 저자원 문제를 해결하기 위해 다양한 데이터 증강 방법을 제안하고 있다. 그러나 이들 방법들은 문장 구조의 다양성으로 인해 의미적인 오류를 야기할 수 있고, 의미적으로 노이즈가 있는 데이터를 생산할 수 있다. 이 논문에서는 문맥 정보를 활용하여 의미적인 오류를 방지하기 위한 데이터 증강 전략인 GDA를 제안한다.
    2. GDA는 문맥 정보를 이용하여 문법의 rule들을 구성하고 조작하는 알고리즘을 사용하여 데이터셋을 증강시킨다. 이를 통해 GDA는 인간의 개입 없이 설명 가능하고 신뢰할 수 있는 데이터 증강 방법이 된다. 
    3. GDA는 사전 훈련된 언어 모델을 사용하는 다른 데이터 증강 기법들을 포함하여 평가되었고, 결과적으로 GDA는 다른 모든 데이터 증강 방법들을 19.38% 상회하는 성능을 보여주었다. GDA는 보다 정확하고 다양한 데이터를 위해 단어의 의미를 통합하는 효과적인 데이터 증강 전략이다.

###### Implicit Sense-labeled Connective Recognition as Text Generation (https://aclanthology.org/2023.findings-emnlp.487/)
- Anthology ID: 2023.findings-emnlp.487 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "문맥 사이의 은연결조사를 인식하는 작업(IDRR)은 인접한 텍스트 단락 사이의 은연결조사의 의미 레이블을 식별하는 작업입니다. 기존에는 이를 분류 작업으로 접근하지만, 몇 가지 하위 작업에서는 의미 레이블뿐만 아니라 구체적인 연결조사까지 필요합니다. 해당 논문은 Implicit Sense-labeled Connective Recognition (ISCR)을 제안하여 인접한 텍스트 단락 사이의 은연결조사와 그 의미 레이블을 식별합니다."
    2. "ISCR은 분류 작업으로 처리될 수 있지만, 많은 레이블과 그들 사이의 불균형한 데이터 분포로 인해 어렵습니다. 따라서 본 논문에서는 텍스트 생성 작업으로 다루며, 인코더-디코더 모델을 사용하여 연결조사와 그 의미 레이블을 모두 생성합니다."
    3. "PDTB-3.0의 평가 결과로부터, 기존의 분류 기반 방법보다 우수한 성능을 보였습니다."

###### VISTA: Visual-Textual Knowledge Graph Representation Learning (https://aclanthology.org/2023.findings-emnlp.488/)
- Anthology ID: 2023.findings-emnlp.488 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 이미지나 텍스트 설명을 사용하여 개체와 관계의 지식 그래프를 표현하는 visual-textual knowledge graphs (VTKGs)를 제안한다. 
    2. VTKGs는 이미지로 개체와 관계를 해석하고, 개체와 관계의 의미를 텍스트로 설명할 수 있는 새로운 벤치마크 데이터셋을 구축한다.
    3. VTKGs에 대한 knowledge graph 표현 학습 방법인 VISTA를 제안하고, 실험 결과 VISTA가 실제 VTKGs에서 최신 knowledge graph completion 방법보다 성능이 뛰어나다는 것을 보여준다.

###### Dynamic Stashing Quantization for Efficient Transformer Training (https://aclanthology.org/2023.findings-emnlp.489/)
- Anthology ID: 2023.findings-emnlp.489 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)은 다양한 자연어 처리 (NLP) 작업에서 탁월한 성능을 보여주었지만, 이러한 모델의 훈련은 많은 계산 및 메모리 액세스를 필요로 하기 때문에 하드웨어 비용을 크게 증가시키며, 장치 내 학습과 같은 사용 사례에서 배포하기 어렵다.
    2. 따라서 이 논문에서는 LLM 훈련이 주 메모리에 종속되어 있다는 관찰을 바탕으로, 메모리 작업을 감소시키는 동적 양자화 전략인 DSQ (Dynamic Stashing Quantization)를 제안한다.
    3. 실험 결과, DSQ는 일반적으로 장치 내 학습에 널리 사용되는 16비트 고정소수점과 비교하여 IWSLT17에서 산술 연산량을 20.95배, DRAM 연산량을 2.55배 감소시키는 효과를 보였다.

###### A Comprehensive Evaluation of Large Language Models on Legal Judgment Prediction (https://aclanthology.org/2023.findings-emnlp.490/)
- Anthology ID: 2023.findings-emnlp.490 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대용량 언어 모델 (LLMs)은 법률 분야와 같은 도메인 특화 응용 프로그램에서 큰 잠재력을 보였으나, GPT-4의 법적 평가에 대한 최근 분쟁은 실제 법률 과제에서의 성능에 대한 의문을 제기한다. 
    2. 따라서 우리는 법적 판단 예측 과제에서 LLMs를 기반으로 한 실용적인 기준 솔루션을 설계하고 테스트하여 법률에 대한 능력을 체계적으로 조사한다. LLMs는 유사한 사례들이나 간소화된 객관식 질문들을 통해 도메인 지식을 학습하거나 유사한 사례들로부터 배울 수 있는 정보 검색 (IR) 시스템과 협력할 수 있다는 것을 보여준다.
    3. 우리는 프롬프트에 포함된 유사한 사례들과 다중 선택 옵션, 즉 레이블 후보들이 LLMs가 전문적인 법률 추론에 필수적인 도메인 지식을 회상하는 데 도움이 될 수 있다는 것을 보여준다. 게다가, 강력한 IR 시스템으로부터 약한 LLMs가 얻는 이익이 제한되기 때문에 IR 시스템이 LLM+IR의 성능을 능가하는 흥미로운 역설적인 상황도 제시된다. 이러한 경우에는 LLMs의 역할이 중복이 된다.

###### A Lightweight Method to Generate Unanswerable Questions in English (https://aclanthology.org/2023.findings-emnlp.491/)
- Anthology ID: 2023.findings-emnlp.491 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 질문에 사용 가능한 정보가 없다면, QA 시스템은 대답하지 않아야 한다. 이 논문에서는 존재하지 않는 질문을 생성하는 다른 학습 데이터를 사용하여 QA 모델을 구축하는 방법을 제안하고 있다.
    2. 기존 자동 방법에 비해 우리가 제안하는 학습 무료(lightweight) 전략으로 생성된 데이터는 더 좋은 모델을 만들어주고, 관련성과 가독성도 더 높다.
    3. 우리의 방법은 간단하지만 강력한 베이스라인이 되며, SQuAD 2.0 데이터 (BERT-large에서 +1.6 F1 점)와 TydiQA-MinSpan 데이터 (BERT-large에서 +9.3 F1 점)에서 상당한 성능 향상을 보여준다.

###### Automatic Evaluate Dialogue Appropriateness by Using Dialogue Act (https://aclanthology.org/2023.findings-emnlp.492/)
- Anthology ID: 2023.findings-emnlp.492 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템 평가에서 적절성은 의사소통 언어 능력의 핵심 요소로서 중요하다. 그러나 현재의 평가는 인간의 판단에 많이 의존하며, 시간과 노력이 많이 소요되며, 편향되기 쉽고 객관성이 부족하다.
    2. 본 논문에서는 다이얼로그 행위 전이의 양상을 이용하여 챗봇의 응답 적절성을 평가하는 DAA라는 새로운 방법을 제안한다.
    3. DAA는 인간-인간 대화 체인을 통해 전이 패턴을 학습하고, 챗봇의 전이 패턴과 유사성을 측정하여 적절성을 평가한다는 것을 실험적으로 검증하였다.

###### TabPrompt: Graph-based Pre-training and Prompting for Few-shot Table Understanding (https://aclanthology.org/2023.findings-emnlp.493/)
- Anthology ID: 2023.findings-emnlp.493 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 표 이해(Table Understanding, TU)는 기계가 표 데이터의 의미를 이해할 수 있게 하는 정보 추출의 필수적인 요소이다. 그러나 기존 TU 방법은 레이블이 지정된 표 데이터의 부족에 대처할 수 없다. 또한, 이러한 방법은 주로 표 내의 텍스트 내용에 초점을 맞추고 표의 고유한 위상 정보를 무시하여 표 의미를 잘못 이해할 수 있다.
    2. 이 논문에서는 위의 문제를 해결하기 위해 TabPrompt라는 새로운 프레임워크를 제안한다. 적은 양의 데이터로도 뛰어난 성능을 보이는 프롬프트 기반 학습을 사용하여 적은 양의 TU를 처리한다.
    3. 또한, 그래프 대비 학습(Graph Contrastive Learning, Graph CL)은 위상 정보를 캡처하는 뛰어난 능력을 보여주어 그래프 신경망이 표를 인코딩하는 이상적인 방법이다. 따라서, 표에 맞춤화된 새로운 Graph CL 방법을 개발한다. 이 방법은 사전훈련 단계에서 사전텍스트 작업으로 사용되어 표의 위상 정보를 포함하는 벡터 표현을 생성한다. 강력한 기준선을 능가하는 실험 결과는 우리의 방법의 적은 양의 표 이해 작업에서의 강점을 보여준다.

###### Towards Formality-Aware Neural Machine Translation by Leveraging Context Information (https://aclanthology.org/2023.findings-emnlp.494/)
- Anthology ID: 2023.findings-emnlp.494 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 번역의 자연스러움을 결정하는 중요한 언어적 성질 중 하나인 엄격성(formality)은 대상 언어 환경에 엄격성과 관련된 토큰이 있음에도 불구하고 희소성(sparsity) 때문에 context-aware한 NMT 모델이 이를 제대로 구별하기 어렵습니다. 
    2. 본 논문에서는 새로운 학습 방법을 소개하여 포멀리티 분류기를 사용하여 NMT 모델에 가장 정보를 제공하는 토큰을 강조하여 명시적으로 알립니다. 대상 언어 환경에서 해당 토큰에 집중하도록 모델을 이끕니다. 
    3. 실험 결과는 우리의 방법이 전체적인 번역 품질을 향상시키는 데 도움이 되는데 더불어 대상 언어 환경으로부터 적절한 엄격성을 반영한다는 것을 보여줍니다.

###### Improving Seq2Seq Grammatical Error Correction via Decoding Interventions (https://aclanthology.org/2023.findings-emnlp.495/)
- Anthology ID: 2023.findings-emnlp.495 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 많이 쓰이고 있는 Seq2Seq 접근법은 문법 오류 수정(GEC)에서 유망한 성능을 보이지만 두 가지 문제점이 있다. 
    2. 첫째, Seq2Seq GEC 모델은 병렬 데이터로만 훈련될 수 있고, GEC 작업에서는 노이즈가 많고 양도 제한적인 경우가 많다. 둘째, Seq2Seq GEC 모델의 디코더는 생성 중인 토큰의 정확성을 명시적으로 알 수 없다.
    3. 본 논문에서는 외부 비평가(critic)를 사용하여 토큰의 적절성을 점진적으로 평가하고, 다음 토큰의 선택에 동적으로 영향을 주는 통합 디코딩 개입 프레임워크를 제안한다.

###### Exploring the Potential of Large Language Models in Generating Code-Tracing Questions for Introductory Programming Courses (https://aclanthology.org/2023.findings-emnlp.496/)
- Anthology ID: 2023.findings-emnlp.496 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 초급 프로그래밍 강좌에서 큰 언어 모델 (LLM)을 사용하여 코드 추적 질문을 생성하는 응용에 대해 탐구한다.
    2. 우리는 GPT4를 대상으로 코드 조각과 설명을 기반으로 코드 추적 질문을 생성할 수 있도록 유도하는 대상 프롬프트를 설계했다.
    3. 우리는 인간 전문가가 작성한 질문과 모델이 생성한 질문을 비교하여 모델이 생성한 질문의 품질을 평가하기 위한 인간 평가 메트릭을 도출했으며, LLM이 다양한 코드 추적 질문을 생성하는 능력과 잠재력에 대한 통찰력을 제공한다.

###### Learning Easily Updated General Purpose Text Representations with Adaptable Task-Specific Prefix (https://aclanthology.org/2023.findings-emnlp.497/)
- Anthology ID: 2023.findings-emnlp.497 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 응용 프로그램에서는 동일한 텍스트로부터 여러 가지 예측을 만들어야 하는 경우가 많다. 각 downstream task마다 큰 사전 훈련된 언어 모델을 fine-tuning하는 것은 몇 번의 forward passes 때문에 추론 시간에서 계산적 부담을 초래한다. 따라서, 계산 비용을 분산시키기 위해 언어 모델을 고정시키고 고정된 텍스트 표현을 기반으로 downstream task를 위한 경량 모델을 구축하는 것이 일반적인 해결책이다.
    2. 그러나, 어떻게 보면 더 일반적인 텍스트 표현을 학습하여 이를 새로운 downstream task에 잘 일반화할 수 있는지는 난제가 된다.
    3. 해당 논문에서는 소스 태스크로부터 고정된 텍스트 표현을 학습하기 위한 프리픽스 기반의 방법을 제안하며 실험 결과, 프리픽스 기반 훈련이 멀티태스킹 훈련보다 더 좋은 성능을 보이며, 멀티태스킹 훈련보다 계산 비용이 적은 업데이트를 수행할 수 있다는 것을 보여준다.

###### Good Meta-tasks Make A Better Cross-lingual Meta-transfer Learning for Low-resource Languages (https://aclanthology.org/2023.findings-emnlp.498/)
- Anthology ID: 2023.findings-emnlp.498 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 모델-에이노테그닉 메타-러닝은 저자원 상황에서 적은 양의 다국어 전이 학습을 향상시키기 위한 유망한 기법으로 주목받고 있으나, 이 크로스-린귈 메타-전이 방법에서 데이터 선택 전략의 영향에 대한 관심은 적었다. 이 논문에서는 사후적인 레벨에서 크로스-린귈 메타-트레이닝 데이터(즉, 메타-태스크)를 선택하여 언어 간 격차를 줄이기 위한 다양한 데이터 선택 전략을 구성하는 "MeTaCo-XMT"라는 메타-태스크 수집기 기반의 크로스-린귈 메타-전이 프레임워크를 제안한다.
    2. 통사적 차이는 전이 성능에 영향을 미치므로, 우리는 통사적 유사성 샘플링 전략을 고려하고, 사전 학습 모델을 기반으로 한 구문 인코더 블록과 Word Move's Distance (WMD)를 사용하는 거리 측정 블록을 갖춘 통사적 거리 측정 모델을 제안한다.
    3. Wikiann 및 TydiQA라는 두 개의 다국어 NLP 데이터셋에서의 실험 결과는 기존 강력한 기준과 비교하여 우리의 접근 방식의 유의한 우위를 보여준다.

###### Reasoning Makes Good Annotators : An Automatic Task-specific Rules Distilling Framework for Low-resource Relation Extraction (https://aclanthology.org/2023.findings-emnlp.499/)
- Anthology ID: 2023.findings-emnlp.499 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 relation extraction은 부족한 레이블 데이터로 인해 어려움이 있다. 이 논문에서는 ARIA라는 자동 task-specific 규칙 추출 프레임워크를 제안하여 사람이 규칙을 매뉴얼하게 작성하지 않고도 고품질 규칙을 생성할 수 있도록 한다.
    2. ARIA는 사전 훈련된 언어 모델을 사용하여 규칙을 추론하고 강력한 결합 규칙을 구성하는 방법을 안내한다. 또한 신뢰할 수 있는 모델-레이블 데이터를 발견하여 식별 가능한 규칙 생성을 위해 규칙 세트를 지속적으로 향상시킬 수 있다.
    3. 논문에서 진행한 실험은 저자들이 제안한 ARIA가 낮은 리소스 상황에서 효과적으로 작동함을 보여준다.

