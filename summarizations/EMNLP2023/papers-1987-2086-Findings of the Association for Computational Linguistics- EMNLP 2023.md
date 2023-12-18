# Korean Three-Line Summarizations of Papers 1987-2086 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### UPTON: Preventing Authorship Leakage from Public Text Release via Data Poisoning (https://aclanthology.org/2023.findings-emnlp.800/)
- Anthology ID: 2023.findings-emnlp.800 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "공개적인 글 작성자가 이미 적대적인 모델이 글을 분석하여 작성자를 파악하는 상황에서 '익명성'을 유지하고자 할 때 어떻게 계정이 교란(sabotage)될 수 있을까?"라는 질문에 대한 해답으로 블랙박스 데이터 조로 (black-box data poisoning methods)를 활용하여 글의 작성자 특징을 약화시켜 작성자 파악을 어렵게 만드는 새로운 방법을 소개한다.
    2. UPTON은 이전의 적대적 공격과 달리 테스트 샘플을 수정하는 것이 아닌 모델의 출력을 바꾸는 백도어 작업과도 다르다. UPTON은 실제 작성자의 청정 글을 사용하여 이미 훈련된 AA 모델에 효과적이다.
    3. 실험 결과 UPTON은 AA 모델의 정확도를 실용적이지 않은 수준(약 35%)으로 낮추면서 글은 여전히 가독성을 유지한다.

###### IAEval: A Comprehensive Evaluation of Instance Attribution on Natural Language Understanding (https://aclanthology.org/2023.findings-emnlp.801/)
- Anthology ID: 2023.findings-emnlp.801 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인스턴스 속성(IA)은 테스트 예측과 관련하여 훈련 인스턴스를 구분하는 작업으로, 데이터 이해와 데이터 처리 최적화에 도움을 주는데, 이러한 IA 방법들의 평가에 대한 문제가 여전히 남아있다.
    2. 이 연구에서는 sufficiency, completeness, stability, plausibility라는 네 가지 요구 사항을 커버하는 체계적이고 포괄적인 평가 체계인 IAEval을 소개합니다. 이를 평가하기 위해 독자적인 메트릭을 설계하였습니다.
    3. IAEval을 사용하여 세 가지 대표적인 IA 방법을 평가하고, 이를 통해 IA 방법들을 종합적으로 비교할 수 있는 능력을 입증하였습니다. IAEval을 사용하면 연구자들은 모델 디버깅과 같은 응용 프로그램에 가장 적합한 IA 방법을 선택할 수 있습니다.

###### Scene Graph Enhanced Pseudo-Labeling for Referring Expression Comprehension (https://aclanthology.org/2023.findings-emnlp.802/)
- Anthology ID: 2023.findings-emnlp.802 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Referring Expression Comprehension (ReC)은 자연어 표현에 기반하여 이미지의 객체를 지역화하는 작업이다. 기존 방법들은 대부분 지도 학습 문제로 접근하여 이미지-텍스트 쌍이나 지역-텍스트 쌍과 같은 비용이 많이 드는 주석이 필요하다. "
    2. 저자들은 scene graph 기반 프레임워크를 제안하여 고품질 가짜 지역-질의 쌍을 자동으로 생성한다. 
    3. 실험 결과, 이 방법은 기존의 가짜 라벨링 방법보다 RefCOCO, RefCOCO+ 및 RefCOCOg에서 각각 약 10%, 12% 및 11%의 성능 향상을 보여주며, RefCOCO 데이터셋에서 최고 성능 비지도 학습 방법보다 15% 이상 우수하다.

###### Noisy Self-Training with Synthetic Queries for Dense Retrieval (https://aclanthology.org/2023.findings-emnlp.803/)
- Anthology ID: 2023.findings-emnlp.803 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 존재하는 신경 기반 정보 검색 모델들은 학습 데이터가 풍부하고 학습 데이터가 증가함에 따라 성능이 향상되는 유망한 결과를 보여주지만, 고품질의 주석이 달린 데이터를 수집하는 것은 과도하게 비용이 많이 든다. 
    2. 따라서 우리는 외부 모델에 의존하지 않고 신경 기반 정보 검색기를 자체 진화 방식으로 개선하는 새로운 노이즈 있는 자기 학습 프레임워크를 도입한다.
    3. 실험 결과, 우리의 방법은 일반 범주 (예: MS-MARCO)와 영역 밖 범주 (즉, BEIR)의 정보 검색 벤치마크에서 기존 방법보다 일관되게 향상되었다. 저자원 환경에서의 추가 분석은 우리의 방법이 데이터 효율성이 뛰어나며 레이블이 달린 학습 데이터의 30%만으로도 경쟁력 있는 기준선보다 뛰어나다는 것을 보여준다. 또한 리랭커 트레이닝을 위해 프레임워크를 확장하면, 제안된 방법은 다양한 도메인의 작업에서 추가적인 향상을 보인다.

###### Leveraging GPT-4 for Automatic Translation Post-Editing (https://aclanthology.org/2023.findings-emnlp.804/)
- Anthology ID: 2023.findings-emnlp.804 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "번역 후 편집" 작업은 NMT 모델의 출력물을 수정하고 품질을 향상시키기 위해 여전히 필요하지만, 이 연구에서는 GPT-4를 사용하여 다양한 언어 쌍에 대한 NMT 출력물을 자동으로 수정하는 방법을 탐구한다.
    2. GPT-4는 번역 후 편집 작업에 능숙하며, 번역 품질을 개선하고 다양한 종류의 주요 번역 오류를 제거하는 의미 있는 수정물을 생성한다.
    3. 그러나 GPT-4가 가끔 가상의 수정물을 생성할 수 있다는 점을 보여줌으로써, 전문 번역 후 편집기로서의 사용에 주의가 필요함을 알려준다.

###### Uniform Complexity for Text Generation (https://aclanthology.org/2023.findings-emnlp.805/)
- Anthology ID: 2023.findings-emnlp.805 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델은 요약 및 기계 번역과 같은 생성형 NLP 태스크에서 유망한 결과를 보였지만, 서술 생성의 문맥에서는 여전히 일관된 텍스트 생성 요소를 포함하지 못하는 문제점이 있다. 
    2. 이 논문에서는 텍스트 생성을 위한 통제 가능한 복잡성을 담은 벤치마크 테스트인 UCTG를 제안한다. 
    3. 실험 결과, GPT-2와 같은 모델들은 작문에서 사용된 입력 프롬프트의 복잡성을 유지하는 데 어려움이 있음을 발견하였다.

###### Cue-CoT: Chain-of-thought Prompting for Responding to In-depth Dialogue Questions with LLMs (https://aclanthology.org/2023.findings-emnlp.806/)
- Anthology ID: 2023.findings-emnlp.806 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템에는 강력한 언어 이해 및 생성 능력이 있는 ChatGPT와 같은 대형언어 모델이 있지만, 이전의 작업들은 사용자 상태에 대한 언어적 단서를 간과하고 대화 맥락을 기반으로 직접 응답을 생성하도록 유도한다.
    2. 이 논문에서는 대화 중에 나타나는 언어적 신호를 활용하여 LLM의 추론을 개선하는 Cue-CoT 방법을 제안한다. 이를 통해 더 개인 맞춤형이고 매력적인 응답을 제공할 수 있다.
    3. 실험 결과, Cue-CoT 방법은 모든 데이터셋에서 표준적인 프롬프트 방법보다 도움이되고 수용 가능성 면에서 우수한 성능을 보여주었다.

###### CONTRASTE: Supervised Contrastive Pre-training With Aspect-based Prompts For Aspect Sentiment Triplet Extraction (https://aclanthology.org/2023.findings-emnlp.807/)
- Anthology ID: 2023.findings-emnlp.807 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "기존의 효율적인 fine-tuning 기술에 초점을 맞춘 ASTE(Aspect Sentiment Triplet Extraction) 작업은 있는 반면, 우리는 여러 ABSA 작업의 성능을 동시에 향상시킬 수 있는 일반적인 접근 방식을 제안하고자 한다."
    2. 우리는 CONTRASTE라는 새로운 사전 훈련 전략을 제시하여 ASTE 성능을 향상시킨다. 또한, 우리의 기술이 ACOS, TASD, AESC와 같은 다른 ABSA 작업에서의 장점을 나타낼 수 있음을 보여준다.
    3. 우리는 aspect-based prompts를 설계하고 마스킹된 감정과 함께 aspect-aware sentiment 표현을 훈련하는 대조학습을 적용함으로써 사전 훈련을 진행한다. 또한, 태깅 기반의 Opinion Term Detector 및 회귀 기반의 Triplet Count Estimator와 기존 모델을 결합하는 멀티태스크 접근 방식을 제안한다.

###### Towards Anytime Fine-tuning: Continually Pre-trained Language Models with Hypernetwork Prompts (https://aclanthology.org/2023.findings-emnlp.808/)
- Anthology ID: 2023.findings-emnlp.808 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 빠르게 변화하는 세상에서 사전 훈련 된 모델을 다양한 도메인과 작업에 적용하기 위해 계속적 사전 훈련이 긴요하다. 이 논문에서는 기존의 계속적 사전 훈련 접근 방식의 언제든지(feel fine-tuned)의 효과를 조사하였고, 보이지 않는 도메인에서 감소하는 성능을 확인하였다.
    2. 따라서 우리는 prompt-guided continual pre-training 방법을 제안한다. 이 방법은 하이퍼 네트워크를 훈련하여 도메인 특정 프롬프트를 생성한다. 이렇게 생성된 프롬프트는 fine-tuning시에 도메인 식별기능을 줄이고 도메인 간의 지식 전달을 촉진한다.
    3. 실험 결과에서는 우리의 방법이 두 개의 실제 데이터셋에서 각각 3.57%와 3.4%의 개선 효과를 보여주었다.

###### Language Guided Visual Question Answering: Elevate Your Multimodal Language Model Using Knowledge-Enriched Prompts (https://aclanthology.org/2023.findings-emnlp.809/)
- Anthology ID: 2023.findings-emnlp.809 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시각적 질문 응답 (VQA)은 이미지에 대한 질문에 대답하는 작업이다. VQA는 이미지와 질문에 대한 이해를 전제로 하여 자연어 응답을 제공한다. 이 논문에서는 이미지에 없는 상식 지식, 세계 지식, 아이디어와 개념에 대한 추론을 필요로 하는 지식 강화 VQA에 초점을 맞춘다.
    2. 우리는 라셔널, 이미지 캡션, 씬 그래프 등의 형태로 언어 가이던스 (LG)를 사용하는 멀티모달 프레임워크를 제안하여 질문에 보다 정확하게 답변한다.
    3. CLIP 및 BLIP 모델을 사용하여 A-OKVQA, Science-QA, VSR, IconQA 데이터셋의 다중 선택 질문 응답 작업에서 우리의 방법을 평가하고, 우리는 언어 가이던스의 사용이 시각적 질문 응답에 대한 간단하지만 강력하고 효과적인 전략임을 보여주었다.

###### XLS-R fine-tuning on noisy word boundaries for unsupervised speech segmentation into words (https://aclanthology.org/2023.findings-emnlp.810/)
- Anthology ID: 2023.findings-emnlp.810 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 발화 스트림에서 명확한 단어 경계가 없어서 비문텍스트 지도 없이 말문자열을 단어 단위로 분할하는 작업은 특히 도전적이다.
    2. 이 논문에서는 최신 self-supervised speech models을 활용하여 낮은 리소스 조건에서도 새로운 작업에 빠르게 적응하는 것을 입증한 학습 방법을 사용한다.
    3. 제안된 방법은 여러 언어를 포함한 다섯 개의 언어집합에서 측정된 F1 점수가 과거보다 약 130% 높은 새로운 최고 성능을 보이면서도 fine-tuning 도중 미처 보지 못한 언어들의 음성도 zero-shot 방식으로 세그멘트화 할 수 있다.

###### Automatic Prompt Augmentation and Selection with Chain-of-Thought from Labeled Data (https://aclanthology.org/2023.findings-emnlp.811/)
- Anthology ID: 2023.findings-emnlp.811 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Chain-of-thought (CoT)은 복잡한 추론 작업에서 대형 언어 모델의 추론 능력을 향상시키는데 성공했지만, 대부분의 CoT 연구는 합리적인 체인들을 수동으로 디자인하여 LLMs에게 제공하여 현실적인 응용에 어려움을 가지고 있다.
    2. 이 논문은 작은 레이블된 데이터셋으로부터 합리적인 체인들을 자동으로 추가하고, 레이블에 기반하여 저품질의 체인들을 제거하여 후보 체인의 풀을 생성하는 방법인 AutomateCoT를 제안한다.
    3. Automate-CoT은 CoT 기법을 빠르게 다른 작업에 적용할 수 있도록 하며, 실험적 결과는 산술 추론, 상식적 추론, 기호적 추론 및 비추론 작업에서 경쟁력 있는 성과를 보여준다.

###### What Makes it Ok to Set a Fire? Iterative Self-distillation of Contexts and Rationales for Disambiguating Defeasible Social and Moral Situations (https://aclanthology.org/2023.findings-emnlp.812/)
- Anthology ID: 2023.findings-emnlp.812 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 도덕적 판단은 특정 맥락에 매우 의존하는데, 실생활 상황에서 인간의 도덕적 판단의 세세한 부분과 복잡성을 정확하게 나타내기 위해서는 다양한 유연한 맥락 이해가 필요하다.
    2. 이 논문에서는 행동이 도덕적으로 더 또는 덜 허용되는 상황을 설명하는 지식과 함께 상황의 이유를 정당화하는 태스크, 'defeasible moral reasoning'을 소개한다.
    3. 학습 데이터의 질을 높이기 위해 GPT-3의 작은 양의 seed knowledge로부터 시작하여, self-distillation, targeted filtering, self-imitation learning 등의 반복적인 과정을 거쳐 얻은 학생 모델을 사용하여 고품질의 데이터셋을 구축하고 최종적으로 우수한 성능을 달성했다.

###### An Empirical Study on Multiple Knowledge from ChatGPT for Emotion Recognition in Conversations (https://aclanthology.org/2023.findings-emnlp.813/)
- Anthology ID: 2023.findings-emnlp.813 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 감정 인식에서 다양한 지식(co-reference, 주제, 감정 원인 등)은 효과적이었지만, ERC에서 이러한 지식을 탐색하는 것은 주석 달린 데이터의 부족과 관련 비용이 높은 문제 때문에 아직 미개척된 상태입니다. 
    2. 대형 언어 모델(LLMs)의 등장은 이 공백을 메우는데 유망한 가능성을 제시합니다. 
    3. 우리는 LLMs에 의해 생성된 이러한 지식을 효과적으로 통합하기 위해 Multiple Knowledge Fusion Model (MKFM)을 제안하고, ERC에서 이러한 지식이 모델에 미치는 영향을 실험적으로 연구하였습니다.

###### Exploiting Contrastive Learning and Numerical Evidence for Confusing Legal Judgment Prediction (https://aclanthology.org/2023.findings-emnlp.814/)
- Anthology ID: 2023.findings-emnlp.814 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 법적인 사건에 대한 설명 텍스트가 주어졌을 때, 법적 판단 예측(LJP)은 사건의 범죄, 적용되는 법조항, 그리고 처벌기간을 예측하는 것을 목표로 한다. 이 논문에서는 텍스트의 숫자를 활용하여 처벌기간을 예측하기 위한 표현을 강화하는 방법과, 각각의 subtask에 동시에 도움을 주기 위해 positive 예측 쌍을 구성하는 최적의 전략을 탐색하기 위한 moco-based supervised contrastive learning을 제안한다. 
    2. 이전 연구에서는 표준 교차 엔트로피 분류 손실로 다양한 오류를 구분할 수 없었고, 처벌기간을 예측하기 위해 텍스트에서의 숫자를 무시했다.
    3. 실험 결과, 제안된 방법은 혼동되는 법적인 사건에 대해 특히 새로운 최고 성능을 달성한다. Ablation study도 각 구성 요소의 효과를 입증한다.

###### One For All & All For One: Bypassing Hyperparameter Tuning with Model Averaging for Cross-Lingual Transfer (https://aclanthology.org/2023.findings-emnlp.815/)
- Anthology ID: 2023.findings-emnlp.815 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 언어 모델은 레이블된 인스턴스 없이도 대상 언어에서 작업을 수행할 수 있는 zero-shot cross-lingual transfer (ZS-XLT)를 가능하게 한다. 하지만, 현재 모델 선택은 소스 언어 검증에 기반하고 있으며, 이는 대상 언어에서의 성능을 최적화하는 데는 부족한 모델 선택을 한다.
    2. 이 논문에서는 하이퍼파라미터 튜닝을 대체하기 위해 다른 실행 결과의 모델을 누적 평균하는 무감독 평가 프로토콜을 제안한다. 
    3. 실험 결과, 소스 언어 검증에 기반한 기존 모델 선택은 suboptimal한 ZS-XLT 성능을 보여주고, 하지만 우리의 누적 평균 모델은 ZS-XLT 성능을 향상시키고 대상 언어 검증 성능 기반의 모델 선택과 근사한 결과를 보여준다.

###### Dimensions of Online Conflict: Towards Modeling Agonism (https://aclanthology.org/2023.findings-emnlp.816/)
- Anthology ID: 2023.findings-emnlp.816 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 민주적 대화에 있어서의 다양한 시각과 강력한 토론을 촉진하기 위해 아고니즘은 중요한 역할을 한다. 그러나 온라인 갈등의 경우, 건설적인 대화를 저해하는 혐오적인 적대감이 존재한다. 이 논문에서는 트위터 대화를 수집하여 갈등의 다양한 차원을 라벨링하는 포괄적인 주석 스키마를 제안한다.
    2. 주석 스키마를 이용하여 약 4,000개의 대화에 대해 여러 라벨을 부여한 후, 로지스틱 회귀 및 트랜스포머 기반 모델을 학습시킨다. 이를 통해 대화의 맥락을 반영하여 갈등을 식별하고 주제의 변동에 강인한 모델을 구축한다.
    3. 결과는 맥락적 라벨이 갈등을 식별하는 데 도움이 되며, 콘텐츠의 조절에 기여할 수 있는 개념화된 갈등 차원과 풍부하게 주석 달린 데이터셋을 제공한다.

###### Learning under Label Proportions for Text Classification (https://aclanthology.org/2023.findings-emnlp.817/)
- Anthology ID: 2023.findings-emnlp.817 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 데이터가 각 클래스에 대한 비율만 주어지는 LLP(Learning from Label Proportions) 환경에서 NLP 작업을 수행하는 방법을 제안한다.
    2. 기존 기법인 DLLP의 불규칙성을 파악하여 robust한 새로운 공식을 제안하였다.
    3. self-supervised 목적과 결합한 우리의 방법은 다양한 메트릭에서 장단거리 텍스트를 포함한 대규모 모델에 대해 기준선과 비교하여 약 87%의 실험 구성에서 더 좋은 결과를 도출하였다.

###### MetaReVision: Meta-Learning with Retrieval for Visually Grounded Compositional Concept Acquisition (https://aclanthology.org/2023.findings-emnlp.818/)
- Anthology ID: 2023.findings-emnlp.818 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들은 과거 경험에서 습득한 기본 개념을 상기하고 이 기본 개념을 새로운 조합에 대해 일반화하여 새로운 구성 개념을 학습하는 능력을 갖고 있다. 이 논문에서는 이러한 인간의 구성 학습 절차에서 영감을 받아, MetaReVision이라는 retrieval-enhanced meta-learning 모델을 제안하여 시각적으로 기반된 구성 개념 학습 문제를 해결한다.
    2. 제안된 MetaReVision은 retrieval 모듈과 meta-learning 모듈로 구성되어 있으며, 검색된 기본 개념을 지원 세트로 활용하여 시각-언어 모델을 meta-train하여 기반된 구성 개념 인식에 사용한다. 
    3. 실험 결과, MetaReVision은 경쟁적인 기준선보다 우수한 성능을 보이며, retrieval 모듈이 구성 학습 과정에서 중요한 역할을 함을 보여준다.

###### PR-MCS: Perturbation Robust Metric for MultiLingual Image Captioning (https://aclanthology.org/2023.findings-emnlp.819/)
- Anthology ID: 2023.findings-emnlp.819 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이미지 캡션 평가를 위한 자동 평가 메트릭은 lexical perturbation에 취약한 취약점이 있다. 본 논문에서는 이러한 변형에 강한 Perturbation Robust Multi-Lingual CLIPScore(PR-MCS)를 제안한다.
    2. PR-MCS는 복수의 언어에 적용 가능한 참조 없는 이미지 캡션 평가 메트릭으로, 원본 텍스트와 편집된 텍스트를 구별하기 위해 CLIP의 텍스트 인코더를 fine-tuning하는 방법을 사용하여 perturbation의 강건성을 달성한다.
    3. 실험에서 PR-MCS는 모든 다섯 개 언어에서 다양한 변형 유형의 lexical noise를 잘 포착하면서 인간의 판단과 강한 상관관계를 유지하며, 기준 메트릭을 크게 능가한다.

###### Pre-training Multi-task Contrastive Learning Models for Scientific Literature Understanding (https://aclanthology.org/2023.findings-emnlp.820/)
- Anthology ID: 2023.findings-emnlp.820 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 과학문학 이해와 같은 태스크에서 사전 훈련된 언어 모델 (LM)은 기존 작업에서의 유용성을 보여왔으며, 특히 대조학습을 통해 튜닝된 경우에 더 효과적이다. 
    2. 그러나 다양한 과학문학 이해 작업에서 사전 훈련 데이터를 공동으로 활용하는 것은 아직 탐구되지 않은 분야이다.
    3. 이 논문에서는 하나의 통합적인 프레임워크인 SciMult를 제안하며, 과학문학 이해 작업 간의 공통 지식 공유를 도모하고 작업별 특정 기술이 서로 간섭하지 않도록 하는 데 초점을 맞춘다.

###### BLM-s/lE: A structured dataset of English spray-load verb alternations for testing generalization in LLMs (https://aclanthology.org/2023.findings-emnlp.821/)
- Anthology ID: 2023.findings-emnlp.821 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 NLP 모델들은 이미 잘 알려진 벤치마크에서 인간 수준의 성능을 달성하고 있는 것으로 보인다. 이에 이러한 모델들이 자연어의 더 깊은 이해를 테스트하기 위해 새로운 벤치마크가 필요하다. 
    2. 이 논문에서는 사람의 분석적 지능 테스트에 영감을 받은 Blackbird의 언어 매트릭스를 도입하여 Predicate-Argument 구조에 대한 새로운 BLM(task)을 정의하고 이를 연구하기 위한 구조화된 데이터셋을 개발한다. 
    3. 이 데이터셋은 동사 변형의 문맥 문장에서 다른 변형을 선택하는 문제를 다루고, 문장 임베딩에 동사 정보가 어떻게 인코딩되며 모델이 인수 구조의 복잡한 속성에 대해 어떻게 일반화되는지에 대한 연구를 촉진하기 위해 만들어졌다.

###### Efficiently Enhancing Zero-Shot Performance of Instruction Following Model via Retrieval of Soft Prompt (https://aclanthology.org/2023.findings-emnlp.822/)
- Anthology ID: 2023.findings-emnlp.822 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "명령어 따르기 모델의 제로샷 성능을 향상시키려면 전체 데이터셋 크기 또는 모델 크기를 확장해야 하지만, 이 논문에서는 prompt tuning을 통해 얻은 soft prompt의 검색을 통해 효율적으로 hard prompt의 제로샷 태스크 일반화를 돕는 방법을 탐구한다."
    2. "특히, prompt tuning을 통해 각 prompt에 대한 soft prompt 임베딩을 학습하고, 이를 기반으로 훈련 데이터 인스턴스와의 매핑을 저장한 다음 추론 중에 쿼리 인스턴스에 가장 가까운 훈련 인스턴스와 해당 prompt 임베딩을 검색한다."
    3. "soft prompt의 검색은 추가 파라미터를 0.007%만 소모하면, 테스트되지 않은 태스크에서 T0의 성능을 향상시키며, BIG-bench 벤치마크의 T0 평균 정확도를 2.39% 포인트 향상시킨다. 또한, 유사한 정답 선택 형식에 대해 훈련된 소스 임베딩을 검색하는 것이 유사한 태스크 유형에 대해 훈련된 소스 임베딩보다 중요하다는 흥미로운 결과를 보고한다."

###### Geographical Erasure in Language Generation (https://aclanthology.org/2023.findings-emnlp.823/)
- Anthology ID: 2023.findings-emnlp.823 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 방대한 양의 세계 지식을 인코딩하지만, 이러한 모델은 인터넷 데이터의 특정 그룹에 대한 정보를 지나치게 포착해 알려진 그룹에 대한 정보 불균형이 생성된 언어로 전파될 위험이 있다.
    2. 이 연구에서는 언어 모델이 특정 국가의 등장을 미리 예측하는 지리적 소거의 한 형태를 연구하고 운용한다.
    3. 훈련 코퍼스에서 특정 국가의 언급 빈도가 낮을수록 지리적 소거가 강하게 상관되는 것을 발견하였고, 특정 목적을 위해 세부적으로 조정하여 소거 현상을 완화할 수 있다.

###### Can Foundation Models Watch, Talk and Guide You Step by Step to Make a Cake? (https://aclanthology.org/2023.findings-emnlp.824/)
- Anthology ID: 2023.findings-emnlp.824 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. AI의 엄청난 발전에도 불구하고, 실제 상황에서 사람들에게 견주어진 작업을 대화를 통해 협력적인 지침을 제공하는 시스템을 개발하는 것은 여전히 큰 과제이다.
    2. 이 논문에서는 사람 사용자와 사람 강사 간의 자연스러운 상호작용을 기반으로 한 새로운 멀티모달 벤치마크 데이터셋인 WTaG를 만들었다.
    3. 다양한 작업에서 기존 모델을 빠르게 적응시킬 수 있는지 연구하였고, 양적, 질적 및 인간 평가 결과에서 일부 경우에는 특정 작업 훈련 없이도 모델이 어느 정도의 성능을 보일 수 있지만, 빠르고 신뢰할 수 있는 적응은 여전히 큰 과제로 남아있다.

###### Scaling Laws vs Model Architectures: How does Inductive Bias Influence Scaling? (https://aclanthology.org/2023.findings-emnlp.825/)
- Anthology ID: 2023.findings-emnlp.825 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer 모델의 확장 특성에 대한 관심이 많아졌으나,다양한 귀납적 가중치와 모델 아키텍처의 스케일링 특성에 대한 연구가 많이 이루어지지 않았다.
    2. 이 논문은 Transformer, Switch Transformer, Universal Transformer, Dynamic convolutions, Performers, MLP-Mixers 등의 10가지 다양한 모델 아키텍처의 스케일링 특성에 대해 체계적인 연구를 수행하였고, 모델 아키텍처가 스케일링과 관련하여 중요한 고려사항임을 보여주었다.
    3. 또한, 다양한 스케일에서 최상의 성능을 보이는 모델이 다르게 변할 수 있다는 사실을 실험을 통해 입증하였다. 이 연구 결과는 현재 커뮤니티에서 모델 아키텍처를 평가하는 방법에 상당한 영향을 미칠 것으로 기대된다.

###### Not All Languages Are Created Equal in LLMs: Improving Multilingual Capability by Cross-Lingual-Thought Prompting (https://aclanthology.org/2023.findings-emnlp.826/)
- Anthology ID: 2023.findings-emnlp.826 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 다국어 능력이 뛰어나지만, 언어에 따라 성능이 크게 달라지는 문제가 있다.
    2. 본 연구에서는 크로스-언어적 사고 활성화 (XLT)라는 간단하고 효과적인 방법을 소개하여 LLM의 다국어 능력을 체계적으로 향상시킨다.
    3. 실험 결과, XLT는 다양한 다국어 태스크의 성능을 획기적으로 향상시키고, 다국어 간 각 태스크의 평균 성능과 최고 성능 간의 격차를 크게 줄였다. 특히, 산술적 추론 및 개방형 질의응답 태스크에서 평균 10점 이상의 성능 향상을 보였다.

###### DetectLLM: Leveraging Log Rank Information for Zero-Shot Detection of Machine-Generated Text (https://aclanthology.org/2023.findings-emnlp.827/)
- Anthology ID: 2023.findings-emnlp.827 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델과 함께 텍스트의 자동 생성이 급속히 진행되면서, 기계 생성 텍스트를 수동으로 구별하는 것은 현실적으로 불가능하다. 이를 방지하기 위해 기계 생성 텍스트를 감지하는 방법을 개발해야 한다. 
    2. 본 논문에서는 머신러닝 라인크 정보를 활용하여 기계 생성 텍스트를 감지하기 위한 두 가지 zero-shot 방법을 소개한다. 
    3. 실험 결과, 제안한 방법들은 이전 연구에 비해 3.9와 1.75 AUROC(Area Under the Receiver Operating Characteristic) point를 개선하였으며, 실제 사용에 더 적합한 DetectLLM-NPR 방법이 적은 수의 변형만으로도 동일한 성능을 달성할 수 있다는 것을 보여준다.

###### From Complex to Simple: Unraveling the Cognitive Tree for Reasoning with Small Language Models (https://aclanthology.org/2023.findings-emnlp.828/)
- Anthology ID: 2023.findings-emnlp.828 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 논문은 dual process theory를 기반으로 인간의 복잡한 논리적 추론 능력을 언어 모델에 적용하는 첫 번째 연구이다.
    2. 이 연구에서는 인과 시스템과 비판적 추론 시스템이라고 불리는 두 가지 주요 구성 요소를 사용하여 Cognitive Tree (CogTree)를 구성한다.
    3. 실험 결과, GPT-3.5 (175B 파라미터)와 비교하여 파라미터 수가 7B 이하로 훨씬 작은 언어 모델로도 유사한 성능을 달성할 수 있다는 것을 보여준다.

###### Macedon: Minimizing Representation Coding Rate Reduction for Cross-Lingual Natural Language Understanding (https://aclanthology.org/2023.findings-emnlp.829/)
- Anthology ID: 2023.findings-emnlp.829 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 교차 언어 자연어 이해(Cross-lingual NLU)는 NLP의 기본적인 작업 중 하나이다. 최근의 사전 훈련된 다국어 언어 모델들은 교차 언어 NLU 작업에서 탁월한 성능을 보여주었다. 그러나 이러한 모델들은 충분한 훈련 데이터를 필요로 하며, 저자원 언어에는 제한적인 데이터가 있을 경우 정확도가 떨어질 수 있다.
    2. 이 논문에서는 풍부한 고언어 자료와 제한된 저자원 언어 자료로 크로스-언어 모델을 훈련하는 방법을 연구한다. 기존의 방법들은 적대적 훈련과 상호 정보 추정을 통해 언어에 중립적인 표현을 학습하려고 하지만, 데이터가 아주 제한적인 경우에는 정확한 데이터 분포를 추정하기가 어렵다.
    3. 그래서 우리는 representation coding rate reduction 방법을 통해 언어 관련 정보를 제거하는 새로운 접근법인 Macedon을 제안한다. Macedon은 언어 관련 정보를 인코딩하는 데 추가적인 코드를 사용하지 않는다. 실험 결과 Macedon이 최신 교차 언어 NLU 접근 방식보다 우수한 성능을 보인다.

###### Adversarial Robustness for Large Language NER models using Disentanglement and Word Attributions (https://aclanthology.org/2023.findings-emnlp.830/)
- Anthology ID: 2023.findings-emnlp.830 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLM (Large Language Models)은 여러 응용 프로그램에 널리 사용되지만, 복잡한 명명된 엔터티 인식 (NER) 태스크에서는 fine-tuned pre-trained language models (PLM)에 비해 성능이 낮다고 알려져 있다.
    2. 이 논문은 LLM NER 모델과 그 instruction fine-tuned variant가 공격에 대해 얼마나 robust한지 조사한다.
    3. 특히, entity와 non-entity 영향을 별도로 포착하는 임베딩을 학습하는 데 도움이 되는 disentanglement와 중요한 단어를 식별하는 word attribution 기술을 이용한 새로운 공격 방법을 제안한다.

###### LLMs – the Good, the Bad or the Indispensable?: A Use Case on Legal Statute Prediction and Legal Judgment Prediction on Indian Court Cases (https://aclanthology.org/2023.findings-emnlp.831/)
- Anthology ID: 2023.findings-emnlp.831 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLM)은 법과 같은 중대한 영역에서의 효능을 검토하기 위해, 인도의 대법원 사건에 대해 최신 LLM을 사용하여 법령 예측과 판결 예측 두 가지 인기있는 작업에 적용하였다.
    2. 우리는 LLM이 법령 예측에서 우수한 예측 성능을 보이는 반면, 판결 예측에서는 여러 표준 모델과 비교했을 때 성능이 낮아지는 것을 확인하였다.
    3. LLM이 생성하는 설명은 예측과 함께 중간에서 양호한 품질을 보이며, LLM 예측 결과에는 성별 및 종교적 편향이 있는 것으로 나타났다. 또한, LLM을 이러한 중요한 법적 작업에 배치하는 윤리적 문제에 대한 법적 전문가의 의견을 제시한다.

###### You Are What You Annotate: Towards Better Models through Annotator Representations (https://aclanthology.org/2023.findings-emnlp.832/)
- Anthology ID: 2023.findings-emnlp.832 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 처리(NLP) 작업에서 Annotator disagreement는 일반적이다. 이 논문은 annotators의 다양한 시각을 직접 모델링하고, annotator embeddings과 annotation embeddings을 생성하여 annotators의 혼자만의 독특한 특성을 모델링하는 방법을 제안한다.
    2. 제안된 접근 방식을 TID-8 데이터셋에서 실험한 결과, annotator disagreement를 통해 모델이 더 나은 학습을 할 수 있으며, 모델 사이즈를 1% 미만으로 증가시킬 수 있다.
    3. 이러한 embedding을 통해 개별 annotators의 독특한 경향과 주관성을 포착함으로써, 우리의 모델은 다양한 시각을 포용할 수 있게 된다.

###### Large Language Models Are Better Adversaries: Exploring Generative Clean-Label Backdoor Attacks Against Text Classifiers (https://aclanthology.org/2023.findings-emnlp.833/)
- Anthology ID: 2023.findings-emnlp.833 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 백도어 공격은 트리거 텍스트를 훈련 및 테스트 데이터에 삽입하여 모델 예측을 조작한다. 
    2. 기존의 텍스트 백도어 공격보다 실제적이고 도전적인 클린-레이블 공격에 초점을 맞추어, 균일한 스타일 기반 트리거를 텍스트에 자동으로 삽입하는 LLMBkd 공격을 제안한다. 
    3. 이 논문에서는 LLMBkd의 효과성과 효율성을 입증하며, 적은 노력과 모델 훈련 없이 다양한 스타일에 걸쳐 공격 성공률을 일관되게 높일 수 있다고 보여준다.

###### Noise-Robust Fine-Tuning of Pretrained Language Models via External Guidance (https://aclanthology.org/2023.findings-emnlp.834/)
- Anthology ID: 2023.findings-emnlp.834 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습 다음에 fine-tuning으로 이루어지는 PLMs (Pretrained Language Models)은 자연어 처리 분야에서 상당한 발전을 이루었지만, 복잡한 주석 작업으로 인해 데이터 레이블은 종종 소음이 발생하며, 이러한 소음 레이블로 PLMs을 fine-tuning하는 전략을 개발하는 것이 필수적이다.
    2. 이 논문에서는 소음 레이블을 사용하여 PLMs을 fine-tuning하기 위해 ChatGPT와 같은 Large Language Models (LLMs)의 안내를 도입한 혁신적인 접근 방식을 소개한다.
    3. 실제로 합성 및 실제 소음 데이터셋에 대한 실험을 통해 우리의 프레임워크가 최첨단 기준선에 비해 우수한 장점을 갖고 있음을 보였다.

###### Probabilistic Tree-of-thought Reasoning for Answering Knowledge-intensive Complex Questions (https://aclanthology.org/2023.findings-emnlp.835/)
- Anthology ID: 2023.findings-emnlp.835 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)은 chain-of-thought (CoT) 추론을 통해 지식에 근거한 복잡한 질문에 대답할 수 있지만, 필요한 지식이 모델 파라미터에 없거나 최신이 아닐 때 사실적으로 잘못된 추론 결과를 생성하는 경향이 있다.
    2. 이 논문에서는 확률적 Tree-of-thought Reasoning (ProbTree)라는 새로운 접근 방식을 제안한다. 이 방법은 쿼리 트리로 복잡한 질문을 번역한 후, 확률적 추론을 사용하여 답변 가능성을 고려하며 리프 노드에서는 파라미터 지식을 사용하는 Closed-book QA와 외부 지식을 사용하는 Open-book QA의 자신감 있는 답변 중 더 좋은 답을 선택함으로써 부정적인 검색 문제를 해결한다.
    3. 본 논문에서 제안하는 ProbTree 방법은 SOTA 방법보다 우수한 성능을 나타내며, 지식에 근거한 확률적 추론의 효과를 입증한다.

###### Ensemble-Instruct: Instruction Tuning Data Generation with a Heterogeneous Mixture of LMs (https://aclanthology.org/2023.findings-emnlp.836/)
- Anthology ID: 2023.findings-emnlp.836 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. In-context learning (ICL)을 사용하여 Self-Instruct나 Alpaca와 같은 기술은 많은 양의 인간 지도를 필요로하지 않고도 강력한 대화형 에이전트를 훈련시킬 수 있다. 하지만 이러한 방법들은 매우 큰 언어 모델에 의존하므로 제한된 라이센스를 가지고 있다. 본 논문에서는 이러한 기술을 훨씬 작은 크기의 언어 모델에 적용하여 보다 효과적인 방법을 제안하였다.
    2. 제안된 방법은 ICL 템플릿을 카테고리화하고 단순화하여 언어 모델이 더 쉽게 학습할 수 있도록 하며, 여러 언어 모델 출력을 앙상블하여 고품질의 합성 예시를 선택하는 데 도움을 준다.
    3. 실험 결과, 우리는 제안된 방법이 Self-Instruct보다 더 높은 품질의 지시문 튜닝 데이터를 생성하며, 기본 언어 모델 및 지시문 튜닝 언어 모델의 성능을 크게 향상시키고, 작은 튜닝된 언어 모델이 더 유용한 예시를 생성한다는 것을 알게 되었다.

###### The Less the Merrier? Investigating Language Representation in Multilingual Models (https://aclanthology.org/2023.findings-emnlp.837/)
- Anthology ID: 2023.findings-emnlp.837 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 언어 모델을 사용하여 자연어 처리(NLP) 과제의 성능을 개선하는 교양 언어 모델은 여러 언어를 하나의 모델에 통합하여 교차 언어 전이 학습을 이용한다. 
    2. 그러나 현재 있는 다양한 언어 모델들은 일부 언어를 지원하지 않으며, 특히 저자원 환경에서는 성능이 떨어지는 경우가 많다. 
    3. 이 논문에서는 다중 언어 모델에 대한 다양한 언어의 언어적 표현과 모델의 성능을 조사하여 언어 그룹별로 다른 특징을 분석하고 이를 개선할 수 있는 방안을 제시한다.

###### SuperTweetEval: A Challenging, Unified and Heterogeneous Benchmark for Social Media NLP Research (https://aclanthology.org/2023.findings-emnlp.838/)
- Anthology ID: 2023.findings-emnlp.838 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어를 위한 NLP의 성숙도가 일반 목적의 모델, 메트릭 및 벤치마크와 비교하면 많이 부족하다. 이로 인해 특정 task에 대해 최고의 성능을 보여주는 모델과 다른 모델과의 비교가 어렵다.
    2. 이 문제를 해결하기 위해 저자들은 SuperTweetEval이라는 통합 벤치마크를 소개한다. 이 벤치마크는 다양한 태스크와 데이터셋을 포함하며, 별도로 조합, 수정 및 구축되었다.
    3. SuperTweetEval 위에서 다양한 모델의 성능을 비교한 결과, 최신의 언어 모델 기술에도 불구하고 소셜 미디어에서의 NLP는 여전히 어려운 문제임을 보여준다.

###### Enabling Unsupervised Neural Machine Translation with Word-level Visual Representations (https://aclanthology.org/2023.findings-emnlp.839/)
- Anthology ID: 2023.findings-emnlp.839 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 단일언어 말뭉치만 사용하여 상당한 성과를 내고있는 비지도형 신경 기계 번역이 중요한 발전을 이루고 있다. 그러나 이러한 방법들은 여전히 유사한 단어들을 헷갈리는 기본적인 결함이 있는데, 이러한 문제를 해결하기 위해 이 논문에서는 단어 수준에서 이미지를 사용하여 어휘 매핑을 증강하는 방법을 제안한다.
    2. 특히, 이 방법은 모델에 시각적 표현을 삽입하여 해당 임베딩 레이어 정보를 수정한다. 또한, 가시적 행렬을 채택하여 이미지가 다른 관련없는 단어에 미치는 영향을 분리한다. 
    3. 30만 개 이상의 자체 수집 이미지와 함께 수행된 실험은 더 정확한 단어 번역을 생성하는 효과가 있음을 검증하며, 최대 2.81 BLEU 점수 향상을 달성하였다. 이는 양방향 사전을 사용하는 것과 비교해 별로나아 보내도 좋다.

###### Pragmatics in Language Grounding: Phenomena, Tasks, and Modeling Approaches (https://aclanthology.org/2023.findings-emnlp.840/)
- Anthology ID: 2023.findings-emnlp.840 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들은 명시적으로 말하는 내용 이상의 의미를 부여하기 위해 맥락을 크게 의존하며, 간결하면서도 효과적인 커뮤니케이션을 가능하게 한다. 
    2. 인간과 자연스럽게 상호작용하기 위해서는 사용자를 대상으로 하는 AI 시스템도 유사한 논리적 스킬을 요구하며, 언어를 효과적으로 사용하기 위해 공유된 언어 목표와 관습, 시각적인 세계와 같은 다양한 유형의 맥락에 의존해야 한다. 
    3. 우리는 기존의 지면화된(settings)된 환경과 논리 모델링 접근법을 조사하고, 각 작업이 언어적 의미를 어떻게 풍부하게 하는지 분석한다. 또한, 미래의 지면화된 작업 설계에 대한 권고사항을 제시하고, 보다 폭넓은 커뮤니케이션 맥락과 기회에 초점을 맞춘 연구 방향을 제안한다.

###### MISCA: A Joint Model for Multiple Intent Detection and Slot Filling with Intent-Slot Co-Attention (https://aclanthology.org/2023.findings-emnlp.841/)
- Anthology ID: 2023.findings-emnlp.841 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구는 복잡한 현실 상황과 관련이 있는 다중 의도 감지와 슬롯 채우기 문제의 연구가 점점 인기를 얻고 있다고 말하며, 최근에는 그래프에 기반한 합성 모델이 주로 사용되지만, 이러한 모델은 의도-슬롯 간 상관관계 정보를 잘못된 레이블 노드로 전달할 수 있는 그래프 구성으로 인해 불확실성이 발생할 수 있다고 지적한다. 
    2. 본 논문에서는 이러한 문제를 해결하기 위해 MISCA라는 합성 모델을 제안한다. MISCA는 의도-슬롯 공동 어텐션 메커니즘과 레이블 어텐션 메커니즘을 도입하여 상관관계를 효과적으로 포착하고 그래프 구성에 의존하지 않고 의도와 슬롯 간의 상관관계 정보를 양방향으로 전달하도록 한다. 실험 결과는 MISCA가 이전 모델보다 우수한 성능을 보여주며 MixATIS 및 MIxSNIPS 두 개의 벤치마크 데이터셋에서 새로운 최고 성능을 달성한다고 보여준다. 
    3. 이에 MISCA의 어텐션 메커니즘의 효과적인 성능을 강조한다.

###### Enhancing Emotion Recognition in Conversation via Multi-view Feature Alignment and Memorization (https://aclanthology.org/2023.findings-emnlp.842/)
- Anthology ID: 2023.findings-emnlp.842 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화에서의 감정 인식 (ERC)은 자연어 처리 커뮤니티에서 증가하는 관심을 받고 있다. 이전 연구에서는 주로 사전학습 언어 모델 (PLM)을 fine-tuning하여 의미-전망 특징을 추출한 다음, 다양한 그래프 신경망을 통해 이러한 의미-전망 특징을 기반으로 문맥-전망 특징을 모델링하였다.
    2. 그러나 간단한 그래프 신경망만을 통해 발화 간 상호작용을 완벽하게 모델링하기는 어렵고, 의미-전망 특징과 문맥-전망 특징이 완전히 일치하지 않는다.
    3. 본 논문에서는 사전학습 대화 모델을 사전 지식 도구로 삼아 상호작용을 모델링하고 의미-전망 특징과 문맥-전망 특징을 맞추기 위해 지도 대조 학습을 채택하였다. 두 가지 전망의 특징은 보완적인 방식으로 함께 작동하여 다양한 관점에서 ERC에 기여한다. 또한, 소수의 인스턴스로부터 tail class의 패턴을 학습하기 위해 메모리화를 통한 새로운 반항적 학습 패러다임을 제안한다. 네 가지 널리 사용되는 벤치마크에서 지속적으로 최고의 결과를 얻을 수 있었다. 반복적인 실험을 통해 우리가 제안한 다중 전망 특징 정렬과 메모리화의 효과를 입증하였다.

###### Mandarin classifier systems optimize to accommodate communicative pressures (https://aclanthology.org/2023.findings-emnlp.843/)
- Anthology ID: 2023.findings-emnlp.843 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전 연구에 따르면, 명사 분류에 대한 이전 작업들은 성별 시스템이 언어 학습과 처리에 대한 의사소통 압력을 맞추기 위해 최적화되어 있다고 주장하고 있습니다.
    2. 우리는 중국어처럼 성별이 없다고 여겨지는 언어도 성별표시기와 같은 기능적 역할을 하는 명사 분류 장치를 가지고 있다는 것을 보여줍니다.
    3. 레이피히 코퍼라스 콜렉션(LCC)에서 추출한 약 1백만 개의 중국어 명사구와 해당 fastText 임베딩을 기반으로, 우리는 명사-분류 기호 조합이 성별 시스템을 구성하는 동일한 빈도, 유사성 및 공기출현 상호작용에 민감함을 보여줍니다.

###### Probing Representations for Document-level Event Extraction (https://aclanthology.org/2023.findings-emnlp.844/)
- Anthology ID: 2023.findings-emnlp.844 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "프로빙 분류기 프레임워크는 다양한 자연어 처리 (NLP) 애플리케이션에 대한 딥 뉴럴 네트워크 모델의 해석에 사용되었다. 이 연구는 문장 수준의 NLP 태스크에 대해 주로 집중되었다. 이 논문은 문서 수준의 정보 추출 (IE)에 대한 학습된 표현에 프로빙 패러다임을 처음 적용한 것이다."
    2. "우리는 문서 수준 이벤트 추출에 관련된 표면적, 의미적 및 이벤트 이해 능력을 분석하기 위해 여덟 가지 임베딩 프로브를 설계했다. 이를 표준 데이터셋에서 학습한 세 가지 다른 LLM 기반 문서 수준 IE 접근 방식에서 배운 표현에 적용했다."
    3. "우리는 이 모델들의 훈련된 인코더들이 인자 감지와 레이블링을 어느 정도 향상시킬 수 있는 임베딩을 제공하지만, 이벤트 수준의 태스크는 약간 향상시키지만, 일관성 및 이벤트 유형 예측에 도움이 되는 정보를 포기해야 함을 발견했다."

###### Cultural Compass: Predicting Transfer Learning Success in Offensive Language Detection with Cultural Features (https://aclanthology.org/2023.findings-emnlp.845/)
- Anthology ID: 2023.findings-emnlp.845 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 기술의 보편성이 증가함에 따라, 문화적 다양성을 고려하는 것이 머신 러닝 분야에서 중요해졌다는 것을 알 수 있다. 특히, 문화적 뉘앙스에 크게 의존하는 주관적인 작업인 Offensive Language Detection (OLD)과 같은 작업에 대해서도 문화적 특징이 교차 문화적 전이 학습의 성공을 정확하게 예측할 수 있는지에 대한 연구가 필요하다. 
    2. 이 연구에서는 문화적 특징과 전이 학습의 효과를 연구하였고, 연구 결과 문화적 가치 조사가 OLD 작업에서 교차 문화적 전이 학습의 성공을 예측할 수 있으며, 모욕적인 단어 간 거리를 사용하면 더욱 개선될 수 있음을 밝혀냈다.
    3. 이러한 결과를 바탕으로 우리는 문화적 정보를 데이터셋에 통합하고, 문화적 정보가 풍부한 조사와 같은 데이터 소스를 활용하여 문화적 적응력을 향상시킬 것을 권장한다. 이 연구는 포용적이고 문화적으로 민감한 언어 기술을 위한 노력의 한 걸음이라고 할 수 있다.

###### Linguistically Motivated Sign Language Segmentation (https://aclanthology.org/2023.findings-emnlp.846/)
- Anthology ID: 2023.findings-emnlp.846 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수화 세그멘테이션은 수화 처리 시스템에서 중요한 작업이며, 수화 인식, 전사, 기계 번역과 같은 후속 작업을 가능하게 한다. 이 연구에서는 개별 수화와 몇 개의 수화로 구성된 구(phrase)로의 세그멘테이션을 고려한다.
    2. 주어진 수화 언어 말뭉치에서 관찰된 언어적 단서를 바탕으로, 두 작업을 동시에 모델링하기 위한 새로운 접근법을 제안한다. 
    3. 제안된 방법을 통해 최종 모델이 다른 수화 언어로 이루어진 도메인 외 비디오 컨텐츠에도 적용될 수 있음을 보여주며, 광학 플로우와 3D 핸드 정규화를 포함시킴으로써 모델의 효율성을 증가시킬 수 있다.

###### Re-weighting Tokens: A Simple and Effective Active Learning Strategy for Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.847/)
- Anthology ID: 2023.findings-emnlp.847 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 제한된 주석 자원으로 텍스트 및 이미지 분류 작업에서 기계 학습 모델을 향상시키기 위해 널리 사용되는 액티브 러닝은 Named Entity Recognition (NER) 분야에서 상대적으로 덜 주목받고 있다.
    2. NER에서 데이터 불균형의 난제로 인해 시퀀스 라벨러는 충분한 학습 신호를 갖지 못해 액티브 러닝의 효과가 제한되고 있다.
    3. 이 논문에서는 동적으로 부드러운 가중치를 각각의 토큰에 할당하는 새로운 재가중 기반 액티브 러닝 전략을 제안하고, 다양한 토큰 수준의 획득 함수와 호환되며 강인한 액티브 러너의 개발에 기여한다.

###### Language-Agnostic Bias Detection in Language Models with Bias Probing (https://aclanthology.org/2023.findings-emnlp.848/)
- Anthology ID: 2023.findings-emnlp.848 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사회적 편향성을 평가하기 위해 "LABDet"라는 강력하고 언어에 중립적인 기법을 사용하여 PLM에 있는 사회적 편향성을 평가한다. 
    2. 우리는 LABDet을 사용하여 훈련된 PLM에서의 인종적 편향성을 조사하고, 이는 역사적이고 정치적인 맥락과 일치하는 결과를 보임을 보여준다.
    3. LABDet은 다양한 템플릿과 언어에 대하여 신뢰성과 적용 가능성을 검증하였으며, 코드와 데이터셋을 공개하였다.

###### CompleQA: Benchmarking the Impacts of Knowledge Graph Completion Methods on Question Answering (https://aclanthology.org/2023.findings-emnlp.849/)
- Anthology ID: 2023.findings-emnlp.849 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프 완성(KGC)의 성공이 downstream 태스크에서 얼마나 성능 향상으로 이어지는지는 깊게 연구되지 않은 중요한 질문이다. 이 논문은 대표적인 KGC 방법이 Knowledge Graph Question Answering(KGQA)에 미치는 영향을 포괄적으로 평가하기 위해 새로운 벤치마크인 CompleQA를 소개한다.
    2. CompleQA는 5개의 독립적인 도메인에서 300만 개의 삼중자를 포함하는 지식 그래프와 5000개 이상의 질문-답변 쌍, 이러한 질문들과 일치하는 완성 데이터셋을 포함한다.
    3. 우리는 두 개의 최신 KGQA 시스템과 함께 네 가지 잘 알려진 KGC 방법을 평가하여, 효과적인 KGC가 지식 그래프의 불완전성이 질문-답변 성능에 미치는 영향을 상당히 완화시킬 수 있음을 보여준다. 놀랍게도, 최상의 성능을 낸 KGC 방법은 최고의 QA 결과로 이어지지 않을 수 있어 KGC를 수행할 때 downstream 응용 프로그램을 고려해야 함을 강조한다.

###### Improving Multi-Criteria Chinese Word Segmentation through Learning Sentence Representation (https://aclanthology.org/2023.findings-emnlp.850/)
- Anthology ID: 2023.findings-emnlp.850 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 CWS(Co-witness Segmentation) 모델들은 사전 훈련된 언어 모델의 지식과 경쟁력 있는 성능을 보였다. 하지만 이러한 모델들은 전체 문맥의 의미를 이해하는 것보다 단어 내에서의 분할 지식을 학습하는 경향이 있다.
    2. 이 문제를 해결하기 위해 우리는 다양한 드롭아웃 마스크에서 비지도학습 문장 표현 학습을 다중 기준 훈련 프레임워크에 통합하는 context-aware 접근법을 소개한다. 
    3. 실험 결과, 우리의 접근법은 9개의 CWS 벤치마크 데이터셋 중 6개의 F1 점수에서 최고 성능을 보이며, 9개 중 8개의 OOV(Out-of-vocabulary) 재현율에서도 최고 성능을 보인다. 더 나아가 다양한 문장 표현 목적으로 큰 개선을 이끌어낼 수 있다는 것을 실험으로 발견했다.

###### A Joint Matrix Factorization Analysis of Multilingual Representations (https://aclanthology.org/2023.findings-emnlp.851/)
- Anthology ID: 2023.findings-emnlp.851 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. joint matrix factorization 기반의 분석 도구를 제안하여, 다국어 및 단일 언어 모델의 잠재 표현을 비교할 수 있다.
    2. 이 도구를 사용하여 다국어 사전 훈련 모델에 의해 학습된 표현이 얼마나 그리고 어떤 방식으로 형태-문법적 특징이 반영되는지 조사하였다.
    3. 우리의 연구 결과는 상위 및 하위 레이어 간 형태-문법적 정보 인코딩의 차이를 보여주며, 이는 언어 속성에 영향을 받는 특정 카테고리의 차이를 나타낸다. 또한, 인자분해 결과의 계층적 클러스터링은 언어학자들이 수작업으로 만든 계통수와 관련이 있다.

###### Don’t Add, don’t Miss: Effective Content Preserving Generation from Pre-Selected Text Spans (https://aclanthology.org/2023.findings-emnlp.852/)
- Anthology ID: 2023.findings-emnlp.852 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에 소개된 Controlled Text Reduction (CTR) 태스크는 전통적인 summarization-style 태스크에서 텍스트 생성 단계를 적용시키기 위해 사용되는데, 입력 텍스트의 특정 내용("하이라이트")에 맞는 일관된 텍스트를 생성하는 모델을 도전한다. 
    2. 현재 신뢰할만한 CTR 모델이 없고, 기존 기준 모델의 성능은 보통적인 유용성에는 부족하다. 
    3. 이 논문에서는 이러한 한계를 극복하기 위해 content-preservation 제약 조건을 강화하는 방법과 silver training 데이터의 품질을 개선하는 방법을 제안한다. 이를 통해 현재의 기준 모델보다 최대 30 ROUGE-L 점 향상된 신뢰할 수 있는 CTR 모델을 제공한다.

###### A Computational Interface to Translate Strategic Intent from Unstructured Language in a Low-Data Setting (https://aclanthology.org/2023.findings-emnlp.853/)
- Anthology ID: 2023.findings-emnlp.853 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현실 세계의 많은 태스크는 인간과 AI 시스템이 협력적으로 수행하는 setup을 가진다. 이 논문에서는 인간의 고위수준 전략 의도를 해석하고 실행 가능한 목표와 제약 사항으로 변환하는 계산화 인터페이스를 제안한다.
    2. 게임 환경을 활용하여 언어 전략을 해당하는 목표와 제약 사항으로 매핑하는 데이터셋을 구축하고, 이 데이터셋으로 학습시킨 모델이 언어로부터 전략적 의도를 추론하는데 있어서 인간 해석보다 유의미한 성능을 보인다고 보여주었다. 
    3. 또한, 저자들은 이 작업에 대해 ChatGPT보다 데이터가 적은 상황에서도 (p < 0.05) 뛰어난 성능을 보인다고 보여주었다.

###### HFMRE: Constructing Huffman Tree in Bags to Find Excellent Instances for Distantly Supervised Relation Extraction (https://aclanthology.org/2023.findings-emnlp.854/)
- Anthology ID: 2023.findings-emnlp.854 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Multi-instance learning (MIL)은 multi-instance bag에서 가장 대표적인 특징을 찾기 위해 AVG (평균), ONE (최소한 하나), ATT (문장 수준 어텐션)과 같은 집계 전략을 사용한다. 그러나 이 전략들은 제 3자 벡터를 훈련시켜 문장 수준 특징을 선택하도록 하여 문장 간에 자연스럽게 존재하는 내재적 연관성을 무시한다. 
    2. 이 논문에서는 circular cosine similarity 개념을 소개하여 한 가방 내의 문장들 간에 내재적인 연관성을 명시적으로 나타낸다. 또한 이전 방법들을 어설픈 노이즈 제거 과정으로 간주하고, Huffman 트리를 기반으로 하는 relation extraction framework (HFMRE)를 구현하여 훈련 중에 노이즈와 집계된 특징을 연속적으로 탐지한다.
    3. 실험 결과는 우리의 방법이 인기 있는 DSRE 데이터셋에서 이전의 기준을 능가하는 탁월한 효과를 나타내고 있다.

###### DISCO: A Large Scale Human Annotated Corpus for Disfluency Correction in Indo-European Languages (https://aclanthology.org/2023.findings-emnlp.855/)
- Anthology ID: 2023.findings-emnlp.855 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Disfluency correction (DC)은 Automatic Speech Recognition (ASR)의 결과물에서 불필요한 요소를 제거하여 읽기 쉽고 해석 가능한 텍스트를 생성한다. 이 논문에서는 English, Hindi, German, French로 말하는 포괄적인 DC 말뭉치를 소개하고 여러 언어로 된 DC 모델의 결과를 상세히 분석한다.
    2. DC 모델의 결과로, 영어는 97.55점, 힌디어는 94.29점, 독일어는 95.89점, 프랑스어는 92.97점의 F1 스코어를 얻었다.
    3. DC의 이점을 증명하기 위해, DC를 최신 기계 번역 (MT) 시스템과 함께 사용할 때 평균적으로 BLEU 점수를 5.65점 향상시킨다는 것을 보였고, 코드와 주석 달린 데이터셋을 공개하였다.

###### Towards Being Parameter-Efficient: A Stratified Sparsely Activated Transformer with Dynamic Capacity (https://aclanthology.org/2023.findings-emnlp.856/)
- Anthology ID: 2023.findings-emnlp.856 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Sparse activation을 사용하는 MoE 모델은 낮은 계산 요구를 유지하면서 파라미터 수를 크게 증가시키는 데 효과가 있다. 그러나 최근 연구에서 이러한 MoE 모델은 전문가 수가 증가함에 따라 성능 향상이 줄어든다는 것을 밝혀냈다.
    2. 본 논문에서는 모든 전문가가 동일한 용량을 갖기 때문에 이러한 파라미터 비효율성이 발생한다고 가정하고, SMoE 모델을 제안한다. SMoE 모델은 다른 토큰이나 작업의 다양한 복잡성 요구에 동적인 용량을 할당할 수 있는 계층적 구조를 갖추고 있다.
    3. 우리는 4개, 15개, 94개 언어 쌍을 포함하는 3개의 다국어 기계 번역 벤치마크에서 SMoE의 효과를 입증한다. 우리는 SMoE가 동일하거나 더 적은 파라미터로 여러 최첨단 MoE 모델을 능가한다는 것을 보여준다.

###### Misery Loves Complexity: Exploring Linguistic Complexity in the Context of Emotion Detection (https://aclanthology.org/2023.findings-emnlp.857/)
- Anthology ID: 2023.findings-emnlp.857 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어 상에서 긍정적, 부정적 감정들은 언제나 동등하게 표현되지만, 부정적 감정이 더 많은 관심을 받는다는 negativity bias에 따라 부정적 감정은 언어적으로 더 복잡하게 표현될 수 있다. 
    2. 우리는 readability와 언어적 복잡성 메트릭을 사용하여 소셜 미디어 플랫폼인 Reddit에서 온 감정의 표현을 더 잘 이해하기 위해 연구를 진행한다. 
    3. 결과적으로, 부정적 감정은 긍정적 감정에 비해 보다 복잡한 텍스트를 생성하고, 이러한 복잡성은 트랜스포머 모델의 감정 감지 성능에 영향을 미치는 것으로 나타났다.

###### Probing the “Creativity” of Large Language Models: Can models produce divergent semantic association? (https://aclanthology.org/2023.findings-emnlp.858/)
- Anthology ID: 2023.findings-emnlp.858 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 평가 방법들은 단어의 유사성만 평가하고 교육적 가치를 고려하지 않기 때문에, 자동 MCQ 평가를 위해 지식 종속 가능성(KDA) 메트릭을 제안한 연구다.
    2. 새로운 augmentation과 contrastive learning 기법을 활용하여 NLP 모델의 robustness를 향상시켰다. 이 방법은 counterfactual을 집합적으로 조합하여 spurious correlations에 영향받지 않게 인과관계를 감독한다.
    3. 대규모 언어 모델은 상당한 예술적 콘텐츠 생성 능력을 가지고 있으며, GPT-4는 사람보다 더 창의적인 단어 연상 능력을 가진다는 연구 결과가 나왔다.

###### Code-Switching with Word Senses for Pretraining in Neural Machine Translation (https://aclanthology.org/2023.findings-emnlp.859/)
- Anthology ID: 2023.findings-emnlp.859 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NMT에서는 polysemous 단어를 처리하는 것이 어려워 다의어성은 큰 문제다. 이 논문에서는 지식베이스(word sense-specific information)에서 정보를 얻어 NMT 모델을 pretraining 하는 Word Sense Pretraining for NMT (WSP-NMT)를 소개하고, 번역 품질을 향상시키는 것을 보였다.
    2. WSP-NMT는 다양한 도전적인 데이터와 자원 부족한 상황에서도 안정성 있는 결과를 보여주었으며, DiBiMT disambiguation 벤치마크에서도 미세한 정확도 향상을 보였다.
    3. 이 연구는 NMT를 위한 다국어 pretraining에서 단어의 의미 정보와 구조화된 지식을 통합하는 장점과 어려움에 대한 흥미로운 새로운 통찰력을 얻었다.

###### DiffusionSL: Sequence Labeling via Tag Diffusion Process (https://aclanthology.org/2023.findings-emnlp.860/)
- Anthology ID: 2023.findings-emnlp.860 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시퀀스 레이블링은 기존에는 조건부 분포를 잡기 위해 판별 모델을 사용했으나, 본 논문에서는 생성 모델을 이용하여 Tag Diffusion Process를 생성하여 discrete tag 데이터를 생성한다.
    2. BTConverter를 통해 고도의 정제 기능을 가지는 Diffusion 모델을 활용하여, DiffusionSL은 다양한 벤치마크 데이터셋과 여러 태스크에서 기존 SOTA baseline을 압도하고 gpt-3.5-turbo를 크게 능가하는 성능을 보여준다.
    3. Discrete 특성의 문제를 해결하기 위해, Bit-Tag Converter (BTConverter)를 제안하고 노이즈 제거 과정을 모델링하기 위해 Bit Diffusion Transformer (BitDiT)를 소개한다.

###### COMET-M: Reasoning about Multiple Events in Complex Sentences (https://aclanthology.org/2023.findings-emnlp.861/)
- Anthology ID: 2023.findings-emnlp.861 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "말하는 사람의 의도된 의미를 이해하는 것은 텍스트에 명시되지 않은 것들을 추론하여 이해하는 것을 필요로 한다. 복잡한 문장에서는 문맥적 지식을 기반으로 이벤트 간의 관계를 이해하는 것이 필요하다."
    2. 본 논문에서는 다중 이벤트 문장에서 특정 이벤트를 위한 상식 추론을 생성할 수 있는 COMET-M(다중 이벤트)를 제안한다. COMET-M은 단순한 문장에서 이벤트 중심의 추론을 생성하는 COMET에 비해 복잡한 다중 이벤트 문장에서 더 나은 성능을 보인다.
    3. COMET-M은 자연어 텍스트와 관련된 코레퍼런스 해결, 대화 및 이야기 이해와 같은 하위 작업에 대한 잠재력을 가지고 있다.

###### On Event Individuation for Document-Level Information Extraction (https://aclanthology.org/2023.findings-emnlp.862/)
- Anthology ID: 2023.findings-emnlp.862 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정보 추출(IE) 시스템이 전체 문서를 처리하는 데 능숙해짐에 따라, 전통적인 템플릿 채우기 작업이 문서 수준의 IE 벤치마크로 새롭게 다시 관심을 받고 있다. 그러나 이 연구에서는 템플릿 채우기가 이러한 목적에 적합한지에 대해 의문을 제기한다. 
    2. 이 연구에서는 이 작업이 "이벤트 개별화(event individuation)"라 불리는 어려운 질문에 대한 명확한 답변을 요구하며, 심지어 전문가들 사이에서도 의견이 분분한 문제에 대해 논의한다. 
    3. 주석 작업 및 오류 분석을 통해 이는 템플릿 채우기 메트릭의 유용성, 작업에 대한 데이터셋의 품질 및 모델의 학습 능력에 대한 우려를 제기하며, 가능한 해결책을 고려한다.

###### AniEE: A Dataset of Animal Experimental Literature for Event Extraction (https://aclanthology.org/2023.findings-emnlp.863/)
- Anthology ID: 2023.findings-emnlp.863 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 바이오 의학 분야에서의 이벤트 추출 (extraction)과 관련된 데이터셋인 AniEE를 소개한다.
    2. 이 데이터셋은 동물 실험 단계에 초점을 맞추어 생성되었으며, 분산된 entity와 중첩된 이벤트를 포함한 고품질의 데이터셋을 제공한다.
    3. 최근의 우수한 NER 및 EE 모델에서 이 데이터셋을 평가하고 비교하였다.

###### From Words to Wires: Generating Functioning Electronic Devices from Natural Language Descriptions (https://aclanthology.org/2023.findings-emnlp.864/)
- Anthology ID: 2023.findings-emnlp.864 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구에서는 최근의 언어 모델이 코드 생성과 유사하게 고급 텍스트 설명으로부터 전자 회로 설계 능력을 가지고 있다는 것을 보여준다. 
    2. 우리는 두 가지 벤치마크인 PINS100과 MICRO25를 소개하는데, 전자 부품에 대한 모델의 지식을 평가하고, 진단 생태계에서 일반적인 마이크로컨트롤러 회로와 코드를 설계하는 능력을 평가한다.
    3. GPT-4와 Claude-V1 같은 모델은 전체 디바이스를 생성할 때 60%부터 96%의 Pass@1 결과를 달성하였으며, 복잡한 회로 설계와 실용적인 유틸리티를 향상시키기 위해 개발 영역을 제안하며, 만족스러운 성능의 양적 분석 결과와 평가 도전 과제를 제시한다.

###### Data-efficient Active Learning for Structured Prediction with Partial Annotation and Self-Training (https://aclanthology.org/2023.findings-emnlp.865/)
- Anthology ID: 2023.findings-emnlp.865 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 논문에서는 액티브 러닝을 활용하여 구조화된 레이블 공간의 주석 비용을 줄이는 실용적인 방법을 제안한다. 이 방법은 부분 주석을 활용하여 정보가 가장 풍부한 하위 구조만 주석 작업을 진행하여 구조화된 결과의 주석 비용을 줄인다.
    2. 또한, 현재 모델의 자동 예측을 가상의 레이블로 사용하여 미주석 하위 구조에 대한 의사 레이블로 활용하는 self-training을 활용한다.
    3. 이러한 부분 주석과 self-training의 조합을 효과적으로 활용하기 위해, 현재 모델의 능력에 따라 적응적으로 부분 선택 비율을 결정하기 위한 오차 추정기(error estimator)를 도입한다. 이를 통해 독립된 4가지 구조화된 예측 작업을 평가한 결과, 읽기 시간을 고려한 공정한 비교 기준에서 부분 주석과 적응적 선택 비율을 사용하는 self-training은 강력한 전체 주석 기준에 비해 주석 비용을 감소시키는 것을 확인하였다.

###### Explicit Alignment and Many-to-many Entailment Based Reasoning for Conversational Machine Reading (https://aclanthology.org/2023.findings-emnlp.866/)
- Anthology ID: 2023.findings-emnlp.866 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 'Conversational Machine Reading (CMR)'은 주어진 문서를 기반으로 multi-turn 대화 상호작용을 통해 사용자의 초기 질문에 대답하는 작업이다. 이 논문에서는 진행 기반 질문 생성 및 중간 의사 결정에 중요한 역할을 하는 document와 사용자가 제공한 정보 사이의 정렬을 고려한 pipeline framework를 제안한다.
    2. 제안된 방법은 explicit한 방식으로 document와 사용자 정보를 정렬하고, 가볍고 많은-many entailment 추론 모듈을 사용하여 결정을 내린다. 또한, 문서와 이전 질문을 기반으로 질문을 생성한다.
    3. 실험 결과 제안된 방법은 CMR 벤치마크 데이터셋 ShARC에서 state-of-the-art 성능을 달성하였다.

###### Harnessing Dataset Cartography for Improved Compositional Generalization in Transformers (https://aclanthology.org/2023.findings-emnlp.867/)
- Anthology ID: 2023.findings-emnlp.867 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신경망은 언어 모델링을 혁신하고 다양한 하위 과제에서 뛰어난 성능을 보이지만, 신경망 모델이 인간의 인지 능력에 비해 구조적 일반화(compositional generalization)를 어느 정도 달성하는지는 여전히 논쟁의 여지가 있다.
    2. 이 논문에서는 기존의 아키텍처와 학습 패러다임 대신 데이터셋 매핑의 힘을 활용하는 혁신적인 방법론을 제안한다.
    3. 이 방법을 사용하여 요약의 데이터 중 일부를 선택함으로써 모델의 정확성을 현저히 향상시키고, CFQ 및 COGS 데이터셋에서 최대 10%의 향상을 얻을 수 있다는 결과를 보였다.

###### Roles of Scaling and Instruction Tuning in Language Perception: Model vs. Human Attention (https://aclanthology.org/2023.findings-emnlp.868/)
- Anthology ID: 2023.findings-emnlp.868 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델(LLM)은 자연어를 이해하는 능력을 갖추었으나, 이러한 성능을 얻기 위해 scaling과 instruction tuning이 어떤 영향을 미치는지는 알려져 있지 않다.
    2. 이 연구는 여러 크기의 LLMs (LLaMA, Alpaca, Vicuna)의 self-attention과 인간의 독서 주의를 비교하여 scaling과 instruction tuning이 언어 관찰에 미치는 영향을 평가한다.
    3. 실험 결과, scaling은 편패 패턴에 의존성을 줄이고, 실질적인 어텐션 향상으로 인간의 독서와 유사하게 만든다는 것을 보여주었으며, instruction tuning은 이러한 효과를 보이지 않는다는 것을 보여준다. 하지만, instruction tuning은 모델이 명령에 민감하게 반응하는 능력을 향상시킨다.

###### Efficient Data Learning for Open Information Extraction with Pre-trained Language Models (https://aclanthology.org/2023.findings-emnlp.869/)
- Anthology ID: 2023.findings-emnlp.869 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. OpenIE (Open Information Extraction)은 문장에서 모든 트리플 (주어, 술어, 목적어)을 추출하는데 어려움이 있는 자연어 처리 작업이다. 이 논문에서는 T5 모델의 사전 훈련 과제를 이용하여 OpenIE의 작업 형태를 전환시키고, 대량의 훈련 데이터가 필요하지 않도록 하는 'OK-IE'라는 새로운 프레임워크를 소개한다.
    2. 또한, '앵커'라는 혁신적인 개념을 도입하여 모델의 출력 순서를 제어하는 기능을 추가하였으며, 이를 통해 모델 수렴에 영향을 미치는 순서 페널티의 영향을 제거하고 훈련 시간을 크게 줄일 수 있다.
    3. 실험 결과, 기존 SOTA 방법에 비해 OK-IE는 훈련 데이터의 1/100 (900개 인스턴스)와 훈련 시간의 1/120 (3분)만으로도 비슷한 결과를 얻을 수 있다.

###### Survival of the Most Influential Prompts: Efficient Black-Box Prompt Search via Clustering and Pruning (https://aclanthology.org/2023.findings-emnlp.870/)
- Anthology ID: 2023.findings-emnlp.870 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 프롬프트 기반 학습은 pretrained language model (LLM)들에게 효과적인 패러다임이다. 이 논문은 프롬프트 기반 검색 공간의 설계와 최적화의 중요성을 강조하며, 클러스터링과 가지치기를 통해 영향력 있는 프롬프트 토큰에 초점을 맞추는 블랙박스 검색 방법인 ClaPS를 제안했다.
    2. ClaPS는 단순한 검색 방법을 사용하여 복잡한 방식보다 우수한 성능을 보이면서 검색 비용을 크게 줄였다. ClaPS는 다양한 task와 LLM에서 최고의 성능을 달성하며, 검색 공간 설계와 최적화의 중요성을 강조한다.
    3. 이 연구에서는 프롬프트 기반 학습의 유용성과 효율성을 향상시키는데 검색 공간 설계와 최적화의 역할이 중요하다는 것을 밝혀냈다.

###### Towards Zero-shot Learning for End-to-end Cross-modal Translation Models (https://aclanthology.org/2023.findings-emnlp.871/)
- Anthology ID: 2023.findings-emnlp.871 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 음성 번역에서의 주요 문제 중 하나는 다른 모달리티 간의 불일치입니다. 두 번째 문제인 다중 모달리티를 포함하는 병렬 데이터의 희소성은 end-to-end 다중 모달 모델이 카스케이드 모델보다 성능이 좋지 않은 경향이 있습니다. 
    2. 우리는 이러한 문제들에 대해, 두 개의 사전 훈련된 단일 모달 모듈을 단어 회전자의 거리를 통해 연결하여 end-to-end 제로샷 음성 번역 모델을 제안합니다.
    3. 우리의 실험은 MuST-C 벤치마크에서 우리의 end-to-end 제로샷 접근 방식이 CTC 기반 카스케이드 모델보다 더 나은 성능을 발휘하며, 지도 학습을 통해 훈련된 end-to-end 모델이 최신 베이스라인에 맞추어주는 것을 보여줍니다.

###### LLMaAA: Making Large Language Models as Active Annotators (https://aclanthology.org/2023.findings-emnlp.872/)
- Anthology ID: 2023.findings-emnlp.872 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 NLP에서의 supervised learning 방법은 대량의 품질 좋은 주석이 담긴 데이터를 필요로 하지만, 실제로 이러한 데이터를 획득하는 것은 비용이 많이 든다. 
    2. 이 논문에서는 대규모 언어 모델을 주석자로 사용하여 효율적으로 주석을 달고 학습하는 active learning 방법을 제안한다.
    3. 실험 결과, LLMaAA 모델은 수백개의 주석된 예제로 학습했을 때 기존 방법보다 더 우수한 성능을 보여준다.

###### NLMs: Augmenting Negation in Language Models (https://aclanthology.org/2023.findings-emnlp.873/)
- Anthology ID: 2023.findings-emnlp.873 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 부정은 문장의 의미를 뒤집는 자연어 처리에서 기본 구성 요소이다. 그러나 사전 훈련된 언어 모델에서는 학습이 덜 이루어져 잘못된 추론 결과를 내면서 부정의 중요성이 충분히 반영되지 않는다.
    2. 이 논문은 사전 훈련된 언어 모델에서 부정의 이해를 향상시키기 위해 가중 교차 엔트로피 손실과 탄성 가중치 결합 규제를 포함한 언어 모델 목적을 제안한다.
    3. 실험 결과로는, 부정화된 LAMA 데이터셋에서 BERT-base의 평균 top 1 오류율을 1.1%, BERT-large를 0.78%, RoBERTA-base를 3.74%, RoBERTA-large를 0.01%로 줄였다. 이는 BERT 오류율을 8%로 줄이며 기존 방법들보다 우수한 결과를 보여준다. 본 논문은 또한 부정화된 augmented 모델이 원래의 자연어 추론 작업 및 부정화된 벤치마크에서 고전적인 모델보다 우수한 결과를 보여준다는 실험적 증거를 제공한다.

###### Parameter-Efficient Prompt Tuning Makes Generalized and Calibrated Neural Text Retrievers (https://aclanthology.org/2023.findings-emnlp.874/)
- Anthology ID: 2023.findings-emnlp.874 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Prompt tuning"은 사전 훈련된 모델의 몇 개의 작업 특정 파라미터를 업데이트하는 것을 말하는데, 이 방법은 언어 이해 및 생성 작업에서 전체 파라미터 튜닝과 비교할 만한 성능을 보여주고 있다.
    2. 이 논문에서는 텍스트 검색에 대한 prompt tuning 문제를 연구한다. in-domain, cross-domain 및 cross-topic 설정에 대해 효율적인 파라미터 튜닝 방법을 소개하고 있다.
    3. 실험 결과 0.1%의 모델 파라미터만 업데이트하여 prompt tuning 전략은 전체 파라미터를 업데이트하는 전통적인 방법보다 검색 모델의 일반화 성능을 크게 향상시킬 수 있다고 보여주었다.

###### X-SNS: Cross-Lingual Transfer Prediction through Sub-Network Similarity (https://aclanthology.org/2023.findings-emnlp.875/)
- Anthology ID: 2023.findings-emnlp.875 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 언어 모델의 "Cross-lingual transfer (XLT)" 기능은 미세 조정(fine-tuning)과정에서 포함되지 않은 언어에서도 해당 작업에서 모델의 성능을 상당한 정도로 보존한다는 것을 알려주고 있다.
    2. 이 논문은 XLT의 효능을 고려하고 특정 조건에 기반하여 가장 적합한 원본 언어를 선택함으로써 XLT의 효과를 강화하는 방법을 제안한다.
    3. 실험에서는 sub-network의 유효성도 확인하며 제안하는 방법이 다양한 작업에서 기존 기준 모델 보다 효과적임을 보여주었다.

###### Noise-Robust Semi-Supervised Learning for Distantly Supervised Relation Extraction (https://aclanthology.org/2023.findings-emnlp.876/)
- Anthology ID: 2023.findings-emnlp.876 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 노이즈가 있는 DSRE에서 기존 방법들은 노이즈가 있는 라벨에 영향을 받을 수밖에 없으며, 이러한 접근법은 개별 문장에 대한 관계 라벨 추출에 적합하지 않다.
    2. 이러한 문제를 해결하기 위해, 우리는 세미-슈퍼바이즈드-러닝 (Semi-Supervised-Learning) 기법을 사용한 새로운 DSRE 프레임워크를 제안한다.
    3. 실험 결과, 우리의 프레임워크는 기존 최고 수준의 방법들과 비교하여 문장 수준의 관계 추출 성능을 크게 향상시켰다.

###### Towards Concept-Aware Large Language Models (https://aclanthology.org/2023.findings-emnlp.877/)
- Anthology ID: 2023.findings-emnlp.877 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLMs는 토큰 수준에서 작동하기 때문에 인간 개념과 그 구조를 얼마나 잘 포착하는지 분석한다.
    2. 컨셉을 사용하여 LLM의 사전 학습 방법과 기존 LLM의 출력을 사용하는 간단한 접근법을 탐구한다.
    3. 이러한 결과는 컨셉을 고려한 LLM의 가능성을 보여준다.

###### ChatGPT Beyond English: Towards a Comprehensive Evaluation of Large Language Models in Multilingual Learning (https://aclanthology.org/2023.findings-emnlp.878/)
- Anthology ID: 2023.findings-emnlp.878 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 대형 언어 모델(Large Language Models, LLM)이 자연어 처리(NLP) 분야에서 가장 중요한 획기적인 발전으로 등장하여 연구와 개발을 근본적으로 변화시키고 있다. 그 중 ChatGPT는 최근 개발된 가장 흥미로운 LLM 시스템 중 하나로, 언어 생성 능력과 대중의 관심을 끌 정도로 인상적인 기술을 보여준다. 이 연구는 ChatGPT와 유사한 LLM을 다양한 언어와 대규모 데이터셋에서 평가하여, 다양한 다국어 NLP 응용에 대해 더 포괄적인 정보를 제공하기 위한 목적을 가지고 있다.
    
    2. 이 연구에서는 ChatGPT를 7가지 다른 과제에 대해 37개의 다양한 언어로 평가하고, 언어 리소스의 상, 중, 하 및 극도로 낮은 수준을 고려한다. 기존 모델의 성능과 비교해 본 결과, ChatGPT의 다양한 NLP 과제와 언어에 대한 성능이 좋지 않음을 보여준다. 따라서 이는 더 나은 모델과 다국어 학습에 대한 더 나은 이해를 개발하기 위해 추가적인 연구를 요구한다.
    
    3. ChatGPT와 유사한 LLM 모델을 이용한 다국어 NLP 응용에 대한 포괄적인 정보를 제공하기 위해, 다양한 언어와 과제에 대해 ChatGPT의 성능을 평가하고, 기존 모델과의 비교를 통해 더 나은 모델과 다국어 학습에 대한 이해의 필요성을 제시한다.

###### Subspace Chronicles: How Linguistic Information Emerges, Shifts and Interacts during Language Model Training (https://aclanthology.org/2023.findings-emnlp.879/)
- Anthology ID: 2023.findings-emnlp.879 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 모델링을 통해 학습된 표현 공간은 자연어 처리에 필수적이다. 그러나 다양한 유형의 언어적 정보가 어떻게 훈련 중에 특정 시기에 나타나고 상호작용하는지에 대한 이해는 제한적이다.
    2. 정보 이론적 접근법을 이용하여 훈련된 표현 공간의 서브스페이스뿐만 아니라 작업 성능의 직접적인 비교를 가능하게 하는 새로운 분석 도구를 활용하여 구문, 의미, 추론 등을 다루는 9가지 작업을 분석하였다.
    3. 우리는 작업과 시간에 따라 표현 서브스페이스가 어떻게 나타나고 정보를 공유하며 나중에 특화될 수 있는 중요한 학습 단계를 식별하였다. 특히 구문적 지식은 전체 훈련의 0.5% 이후 빠르게 습득되며, 의미와 추론 작업은 후반부에서 장거리 문맥적인 특성과 고도의 특화를 통해 성능이 개선된다.

###### Not All Demonstration Examples are Equally Beneficial: Reweighting Demonstration Examples for In-Context Learning (https://aclanthology.org/2023.findings-emnlp.880/)
- Anthology ID: 2023.findings-emnlp.880 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델 (LLM)은 모델의 스케일 업으로 한정된 수의 데모 예제가 입력 시퀀스에 추가될 때 하류 작업에 빠르게 적응할 수 있는 In-Context Learning (ICL) 능력을 갖추었다. 그러나, 현재의 ICL은 모든 데모 예제를 동등하게 처리하는데, 이는 일반적으로 예제의 품질이 균일하지 않아서 개선이 필요하다.
    2. 우리는 이 논문에서 어떻게 대략적으로 최적의 데모 예제 가중치를 결정하고 ICL 중에 이를 적용하는지 조사한다. 우리는 또한 추가적인 유효성 검사 데이터 없이 가중치의 품질을 평가하기 위해 마스크된 자체 예측 (MSP) 점수를 설계하였다.
    3. 실험 결과, 8개의 텍스트 분류 작업에서 우리의 접근법은 기존의 ICL에 비해 큰 성능 향상을 보였다.

###### Difference-Masking: Choosing What to Mask in Continued Pretraining (https://aclanthology.org/2023.findings-emnlp.881/)
- Anthology ID: 2023.findings-emnlp.881 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 랜덤 마스킹 방식에서는 토큰을 임의로 가리지만, 어떤 토큰을 가릴지 결정하는 것이 학습 결과를 크게 개선할 수 있다는 직관이 있다.
    2. 이 논문에서는 self-supervised objective를 기반으로한 Difference-Masking 이라는 마스킹 전략을 소개하고, 사전훈련된 모델이 도메인별 데이터에서 계속 사전훈련을 하면서 어떤 토큰을 가릴지 자동으로 결정한다.
    3. 실험적으로, Difference-Masking은 다양한 언어와 멀티모달 비디오 작업에서 계속된 사전훈련 설정에서 다른 기준 모델보다 우수한 성능을 보여주었다.

###### Learn From One Specialized Sub-Teacher: One-to-One Mapping for Feature-Based Knowledge Distillation (https://aclanthology.org/2023.findings-emnlp.882/)
- Anthology ID: 2023.findings-emnlp.882 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Knowledge distillation"은 과잉 파라미터화된 language model을 압축하는 데 효과적인 기술로 알려져 있다. 이 논문에서는 이 과제를 N개의 지역적 하위 과제로 분할하는 새로운 방법을 제안하였다. 특정 서브 티처(sub-teacher)로부터 특정 서브 스튜던트(sub-student)가 학습을 진행하도록 하는 이 방법은 성능을 향상시킨다고 확인되었다.
    2. 제안된 방법은 다른 distillation 기법과 결합될 수 있으며, 벤치마크 데이터셋 대부분에서 더 높은 성능을 유지한다는 것이 실험적으로 입증되었다.
    3. 더 나아가, "Masked One-to-One Mapping"이라는 제안된 방법의 변형은 학습 단계마다 일부 서브 과제(sub-task)에 집중하여 학습함으로써 이식된 지식을 효과적으로 소화하고 높은 성과를 이끌어냈다.

###### IMU2CLIP: Language-grounded Motion Sensor Translation with Multimodal Contrastive Learning (https://aclanthology.org/2023.findings-emnlp.883/)
- Anthology ID: 2023.findings-emnlp.883 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. IMU2CLIP는 Inertial Measurement Unit (IMU) 모션 센서 레코딩을 텍스트와 비디오로 대응시키기 위한 새로운 사전 훈련 접근 방식으로, Contrastive Language-Image Pre-training (CLIP)의 공간에 IMU 데이터를 투영하여 사용한다.
    2. 이 방식을 통해 IMU2CLIP은 IMU 센서로 측정된 인간의 동작을 해당하는 텍스트 설명과 비디오로 변환할 수 있으며, 이 모달리티 간의 의사소통과 투명성(transitivity)을 유지한다.
    3. 또한, 우리는 운동 센서 데이터를 활용한 운동 기반 미디어 검색 또는 LM 기반의 운동 센서 데이터와의 다중모달 추론과 같은 IMU 기반 웨어러블 AI 응용 프로그램을 소개한다. 뿐만 아니라, IMU2CLIP는 각 응용 프로그램에 맞게 fine-tuning을 수행하여 downstream 성능을 크게 향상시키는 것을 보여주고 있으며, 이는 이 접근 방식이 새로운 사전 훈련 리소스로서의 범용성을 증명한다.

###### Conditioning on Dialog Acts improves Empathy Style Transfer (https://aclanthology.org/2023.findings-emnlp.884/)
- Anthology ID: 2023.findings-emnlp.884 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 대화 행위(dialog acts)가 스타일 변환에 미치는 역할을 탐구한다. 특히, 공감 감정을 전달하는 스타일 변환에 초점을 맞추고 있다. 
    2. 이 논문에서는 two novel few-shot prompting strategies를 사용하여 대상 행위(target act)나 대화 행위 조건(dialog-act-conditioned)에 따라 문장을 공감적으로 변환한다. 
    3. 실험 결과, 대상 행위 prompt는 문맥의 의미를 유지한 채 공감 감정을 효과적으로 향상시키는 반면, 대화 행위 조건 prompt는 의미와 대화 행위 유형을 보존하면서 공감을 강화시킨다는 것을 보여주었다. 각각의 대화 행위는 다른 프롬프팅 방법에서 다양하게 혜택을 받으며, 대화 행위의 역할에 대한 추가적인 연구의 필요성을 강조한다.

###### Systematic Assessment of Factual Knowledge in Large Language Models (https://aclanthology.org/2023.findings-emnlp.885/)
- Anthology ID: 2023.findings-emnlp.885 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구들은 대규모 언어 모델의 저장된 지식을 평가하기 위해 기존의 질문-답변 벤치마크를 사용해왔으나, 이 방법은 대부분 예비 훈련 데이터와 중복되는 일반적인 도메인에만 초점을 맞추기 때문에 사실적인 지식의 범위에 제한이 있다.
    2. 이 논문에서는 지식 그래프(KG)를 활용하여 대규모 언어 모델의 사실적인 지식을 체계적으로 평가하는 프레임워크를 제안한다. 이 프레임워크는 주어진 KG에 저장된 사실들로부터 질문과 기대되는 답변의 세트를 자동으로 생성하고, 대규모 언어 모델이 이러한 질문에 대한 정확성을 평가한다.
    3. 실험 결과, 우리는 ChatGPT가 모든 도메인에서 일관되게 우수한 성능을 보여준다는 것을 발견했다. 또한, 지시어 세부 튜닝, 도메인 및 질문 복잡성에 따라 대규모 언어 모델의 성능이 달라지며, 적대적인 문맥에 취약하다는 것을 발견했다.

###### From Speculation Detection to Trustworthy Relational Tuples in Information Extraction (https://aclanthology.org/2023.findings-emnlp.886/)
- Anthology ID: 2023.findings-emnlp.886 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Speculation detection은 텍스트의 사실성을 파악하기 위한 중요한 NLP 태스크이다. 그러나 추출된 추측 정보들은 구조가 없어 downstream 태스크에서 직접적으로 활용하기 어렵다.
    2. 이 논문에서는 speculations를 OIE 튜플에서 연구하고, 각 튜플이 추측적인지 판단하는 새로운 연구 과제를 정의한다.
    3. LSOIE 데이터셋을 분석하고, 이 새로운 연구 과제를 위한 기준 모델인 SpecTup을 제안한다.

###### Tokenization Consistency Matters for Generative Models on Extractive NLP Tasks (https://aclanthology.org/2023.findings-emnlp.887/)
- Anthology ID: 2023.findings-emnlp.887 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 추출적인 작업에서 생성 모델은 널리 사용되어 왔으며, 최근 추출형 질문 답변(QA)에서도 최고 성과를 보여주고 있다. 그러나 본 논문에서는 모델을 훈련할 때 자주 간과되는 토큰화 불일치 문제에 대해 연구하였다.
    2. 토큰화 불일치 문제는 토크나이저에 의해 입력과 출력이 일관되지 않게 토큰화되어 추출 작업의 특성을 손상시키고 성능 하락 및 공허한 결과를 초래한다. 
    3. 우리는 이 문제에 대한 간단하면서도 효과적인 해결책을 제안하고, 추출적인 QA에 대한 사례 연구를 수행하였다. 일관된 토큰화를 통해 모델이 도메인 내 및 도메인 외 데이터셋에서 더 좋은 결과를 보여주며, 특히 BART 모델을 SQuAD에서 학습하고 8개의 QA 데이터셋에서 평가할 때 평균 F1값이 +1.7 상승하는 것을 확인했다.

###### Dialogue Medical Information Extraction with Medical-Item Graph and Dialogue-Status Enriched Representation (https://aclanthology.org/2023.findings-emnlp.888/)
- Anthology ID: 2023.findings-emnlp.888 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 여러 턴의 의사-환자 대화에는 환자의 증상, 의사의 진단 및 처방과 같은 풍부한 의료 지식이 포함되어 있습니다. 이러한 의료 지식을 적절하게 채굴하고 표현할 경우, 진단 보조 및 처방 권장과 같은 다양한 임상 응용에 도움이 될 수 있습니다.
    2. 우리는 자유로운 텍스트 대화에서 구조화된 지식을 추출하기 위해 "대화 의료 정보 추출"이라는 중요한 과제를 목표로 합니다. 이 작업은 사전에 정의된 임상적인 의미 있는 의료 항목(증상, 수술 등) 및 그 상태(양성, 음성 등)를 대화에서 인식하는 것을 목표로 합니다.
    3. 기존 접근 방식과 달리 우리는 상호 그래프를 제안하여 항목 간의 관계를 모델링합니다. 또한 대화와 상태를 기반으로 하는 두 가지 연속적인 주의 메커니즘을 제안하여 항목 표현을 개선합니다. 이 방법으로 DMIE 작업에서 의료 항목과 상태 간의 관계를 모델링할 수 있습니다.

###### LogicAttack: Adversarial Attacks for Evaluating Logical Consistency of Natural Language Inference (https://aclanthology.org/2023.findings-emnlp.889/)
- Anthology ID: 2023.findings-emnlp.889 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델들은 NLI(자연어 추론) 태스크에서 높은 성능을 보였지만, 이러한 모델들은 평가 데이터의 단순한 휴리스틱이나 아티팩트에 의존하여 이러한 높은 성과를 달성하고 있으며, 이는 여전히 논리적 일관성에 결여되어 있다는 것을 시사한다.
    2. 논리적 일관성을 평가하기 위해 우리는 다양한 논리 형태의 전제와 가설을 사용하여 NLI 모델을 공격하는 LogicAttack이라는 방법을 제안한다.
    3. 우리의 접근법은 명제 논리학에서의 추리 규칙들, 예를 들어 Modus Tollens와 Bidirectional Dilemma 등을 활용하여 효과적인 적대적 공격을 생성하고, 여러 NLI 모델에 걸쳐 공통적인 취약점을 식별해낸다.

###### Decomposed Prompt Tuning via Low-Rank Reparameterization (https://aclanthology.org/2023.findings-emnlp.890/)
- Anthology ID: 2023.findings-emnlp.890 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Prompt tuning의 전통적인 방법과는 다르게 저자들은 soft prompt 초기화를 위해 저차원 행렬로 다양한 방식을 제안한다.
    2. Empirical studies를 통해 low-rank 행렬이 효과적인 초기화 방법임을 보여주며, 기존 방법에 비해 trainable parameter 개수를 크게 줄임과 동시에 효과를 유지한다.
    3. high-resource와 low-resource 시나리오에서 SuperGLUE 벤치마크 실험 결과, 제안된 방법의 효과를 입증한다.

###### SGP-TOD: Building Task Bots Effortlessly via Schema-Guided LLM Prompting (https://aclanthology.org/2023.findings-emnlp.891/)
- Anthology ID: 2023.findings-emnlp.891 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대화 연구에서 최소한의 인간 노력으로 end-to-end 태스크 봇을 구축하고 유지하는 것은 오랜 동안의 과제이다. 본 논문에서는 SGP-TOD라는 새로운 방법을 소개하는데, 큰 언어 모델을 기반으로 Task-Oriented 대화 시스템을 쉽게 구축하는데 사용된다. 
    2. SGP-TOD는 사용자와 상호작용하는 LLM, belief instruction 및 대화 정책을 추적하는 DST Prompter, 그리고 제공된 대화 정책을 따르는 적절한 응답을 생성하기 위해 LLM을 지시하는 Policy Prompter로 구성된다.
    3. Multiwoz, RADDLE, STAR 데이터셋에 대한 실험 결과에서 SGP-TOD는 훈련 데이터 없이 학습하는 전략으로 최고 수준의 zero-shot 성능을 보여주며, 적은 수의 데이터로 학습하는 방법을 현저히 능가한다. 또한 도메인 확장 환경에서는 단순히 부가적인 스키마 규칙을 추가함으로써 적절하게 새로운 기능에 적응한다.

###### Ethical Reasoning over Moral Alignment: A Case and Framework for In-Context Ethical Policies in LLMs (https://aclanthology.org/2023.findings-emnlp.892/)
- Anthology ID: 2023.findings-emnlp.892 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 position paper에서는 LLMs를 특정한 윤리 원칙에 동화시키는 대신, 일반적인 윤리적 추론 능력을 주입하여 그들이 전 세계적으로 가치 다양성을 다룰 수 있도록 해야 한다는 주장을 한다.
    2. 우리는 윤리 정책을 제공하면, LLM은 그 정책에 윤리적으로 일관된 결정을 내릴 수 있어야 한다고 주장한다.
    3. 우리는 도덕적 딜레마를 다양한 형식의 도덕적 이론과 다른 추상화 수준에서 다루는 프레임워크를 개발하였으며, GPT-x 모델들과의 초기 실험 결과는 GPT-4가 거의 완벽한 윤리적 추론자이지만, 여전히 모델들은 서양과 영어권 사회의 도덕적 가치에 편향성을 가지고 있다.

###### Vector-Quantized Prompt Learning for Paraphrase Generation (https://aclanthology.org/2023.findings-emnlp.893/)
- Anthology ID: 2023.findings-emnlp.893 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어의 딥 생성 모델링은 유창한 문장을 생성하거나 한 언어에서 다른 언어로 번역하는 등 여러 성과를 거두었다. 
       하지만 파라프레이즈 생성을 위한 생성 모델링 기술의 발전은 표현 다양성과 의미 보존 간의 복잡한 충돌을 다루는 것에 아직 크게 뒤처져 있다.
    2. 이 논문에서는 사전 훈련된 모델과 인스턴스에 따라 다른 프롬프트를 활용하여 다양하고 고품질의 파라프레이즈를 생성하는 방법을 제안한다.
    3. 실험 결과는 제안된 방법이 Quora, Wikianswers, MSCOCO 등 3개의 벤치마크 데이터셋에서 우수한 성과를 달성했음을 보여준다.

###### Rethinking the Construction of Effective Metrics for Understanding the Mechanisms of Pretrained Language Models (https://aclanthology.org/2023.findings-emnlp.894/)
- Anthology ID: 2023.findings-emnlp.894 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델의 내부 관계를 보존하면서 입력 텍스트를 벡터 집합으로 효과적으로 매핑하는 것이 기대되지만, 내재적으로 해석 가능성이 떨어지는 경우는 해석 가능한 흰 상자 모델을 설계하고 메트릭을 계산하는 것이 어려워진다.
    2. 이 논문에서는 흰 상자 모델의 해석 가능성을 달성하고 메트릭 계산의 엄격성을 보장하는 새로운 메트릭 구성을 위한 접근 방식을 제안한다. tree topological probe라는 모델을 사용하여 이러한 메트릭을 계산한다.
    3. 실험 결과를 바탕으로 BERT-large에서 토폴로지 프로브를 사용하여 BERT와 비슷한 사전 훈련된 언어 모델의 동작 메커니즘과 특정 하위 모듈의 성능 향상 전략에 대한 짐작을 제시한다.

###### PARROT: Zero-Shot Narrative Reading Comprehension via Parallel Reading (https://aclanthology.org/2023.findings-emnlp.895/)
- Anthology ID: 2023.findings-emnlp.895 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 'Parrot'은 병렬 독서를 통해 일련의 이야기를 이해하기 위한 영감을 제공함으로써, 이야기 이해에 대한 zero-shot 접근 방식을 제시한다.
    2. 이 방법은 한 이야기를 다른 이야기의 지도 신호로서 활용하여 텍스트 내용을 추상화하고 진정한 이야기 이해를 발전시킨다.
    3. 두 가지 이야기 이해 벤치마크에서 진행한 평가에서 'Parrot'은 이전 zero-shot 접근법을 능가하며 완전한 지도 모델의 성능과 비슷한 결과를 달성한다.

###### BioDEX: Large-Scale Biomedical Adverse Drug Event Extraction for Real-World Pharmacovigilance (https://aclanthology.org/2023.findings-emnlp.896/)
- Anthology ID: 2023.findings-emnlp.896 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의약품 안전 모니터링을 향상시키기 위해 자연어 처리를 이용한 BioDEX라는 대형 리소스를 소개하고, 의약품이나 환자에 대한 핵심 정보를 예측하는 작업을 진행한다.
    2. 65,000개의 초록과 19,000개의 전문 논문, 256,000개의 의약품 안전 보고서로 구성된 BioDEX를 사용하여 의약품 부작용 이벤트를 추출하고, 이를 통해 전문가들을 돕는 모델을 구축한다.
    3. Human performance는 72.0% F1이지만, 우리의 모델은 59.1% F1 (검증 시 62.3%)를 달성하여 큰 발전 가능성을 보여준다. 또한, 이 모델이 전문가들을 돕는 방식도 탐구한다.

###### Coarse-to-Fine Dual Encoders are Better Frame Identification Learners (https://aclanthology.org/2023.findings-emnlp.897/)
- Anthology ID: 2023.findings-emnlp.897 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Frame identification은 문장에서 대상 단어와 관련된 의미적 프레임을 찾는 것을 목표로 한다. 그러나 최근 연구들은 프레임 정의를 모델링하여 대상과 후보 프레임 간의 유사성이나 일치 점수를 측정하지만, 이러한 연구들은 정의의 충분한 표현 학습이 부족하거나 1000개가 넘는 후보 프레임 중에서 가장 적합한 프레임을 효과적으로 선택하는 데 어려움이 있다.
    2. 우리는 CoFFTEA라는 새로운 아키텍처를 제안한다. CoFFTEA는 대조 학습과 두 개의 인코더를 사용하여 프레임과 대상 간의 정렬을 효율적으로 모델링한다. CoFFTEA는 더 높은 유사도의 프레임을 구별하기 위해 점진적 학습 방법을 사용한다. 실험 결과는 CoFFTEA가 이전 모델보다 0.93점의 전체 점수와 1.53점의 R@1을 달성했음을 보여준다.
    3. 추가 분석 결과 CoFFTEA는 프레임과 프레임, 대상과 대상 간의 관계를 더 잘 모델링할 수 있다는 것을 시사한다.

###### Sound of Story: Multi-modal Storytelling with Audio (https://aclanthology.org/2023.findings-emnlp.898/)
- Anthology ID: 2023.findings-emnlp.898 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재까지의 이야기 이해 및 전달에 관한 연구들은 소리에 대해 거의 주의를 기울이지 않았다. 그러나 실생활에서는 이야기를 전달할 때 이야기 자체와 함께 시각화 및 소리를 사용한다. 따라서 본 논문에서는 소리가 이야기의 의미를 전달하는 중요한 역할을 한다며, 이야기 이해 및 전달 연구 영역을 소리를 고려하는 방향으로 확장시키기 위해 배경음 사운드를 도입하는 것을 제안한다.
    2. 이를 위해 "Sound of Story (SoS)"라는 새로운 데이터셋을 소개하는데, 해당 데이터셋은 이미지와 텍스트 시퀀스와 이야기에 해당하는 사운드 또는 배경 음악을 갖춘 쌍으로 구성되어 있다. 음악 역시 이야기의 의미를 전달하기 때문에 음악 없이 정리된 대형 데이터셋이어서 이야기에 관한 다중모달 이해를 연구하는데 유용하다.
    3. 이러한 데이터셋을 활용하여 소리와 관련된 이야기 이해와 생성 작업의 벤치마크를 설정하고, 각 작업에 대한 강력한 기준선을 제시한다. 제안된 데이터셋과 작업은 다중모달 이해 관점에서 이야기를 탐색하는 데에 도움이 될 것으로 기대한다.

###### Synthesize, if you do not have: Effective Synthetic Dataset Creation Strategies for Self-Supervised Opinion Summarization in E-commerce (https://aclanthology.org/2023.findings-emnlp.899/)
- Anthology ID: 2023.findings-emnlp.899 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 전자상거래에서 의견 요약은 제품 리뷰에서 제시된 의견을 좁히는 과정이다. 그러나 대량의 지도 데이터셋이 없어 특정 측면 및 일반 의견 요약 생성에 어려움이 있다. 
    2. 이 논문에서는 범용 및 특정 측면 의견 요약에 맞춘 SDC 전략을 제안한다. 
    3. 실험 결과, 우리의 모델은 다른 모델에 비해 입력 리뷰에 대해 더 충실한 요약을 생성하며, 이슈별 의견 요약에서도 인간이 지정한 측면이나 씨드 단어의 도움 없이 기존 기법을 능가하는 결과를 보였다.

