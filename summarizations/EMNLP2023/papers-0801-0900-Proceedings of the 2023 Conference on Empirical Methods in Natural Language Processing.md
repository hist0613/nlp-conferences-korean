# Korean Three-Line Summarizations of Papers 801-900 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### Multi-view Contrastive Learning for Entity Typing over Knowledge Graphs (https://aclanthology.org/2023.emnlp-main.800/)
- Anthology ID: 2023.emnlp-main.800 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 그래프 entity typing (KGET)은 지식 그래프 내 entity의 유형을 추론하는 것을 목표로 한다. 기존 방법들은 neighbor와 entity의 유형에 의해 제공된 지식을 효과적으로 인코딩하는 데 초점을 맞추지만, 유형이 함께 클러스터링 될 수 있는 방식에서 제공되는 의미적 지식을 무시한다. 
    2. 본 논문에서는 Multi-view Contrastive Learning for knowledge graph Entity Typing (MCLET)라는 혁신적인 방법을 제안한다. MCLET은 클러스터를 통해 제공되는 coarse-grained 지식을 entity와 유형 embedding에 효과적으로 인코딩한다.
    3. 실험 결과, MCLET이 기존의 최신 기술과 비교하여 강력한 성능을 보여준다.

###### MailEx: Email Event and Argument Extraction (https://aclanthology.org/2023.emnlp-main.801/)
- Anthology ID: 2023.emnlp-main.801 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 본 논문에서는 첫번째로 "MailEx"라는 대화식 이메일 스레드에서 이벤트 추출을 수행하기 위한 데이터셋을 제안한다. 
    2. 이 데이터셋은 이메일 도메인에서 10개의 이벤트 유형과 76개의 인수를 포함하는 새로운 태그 분류 체계를 제안한다. 
    3. 실험을 통해 fine-tuned sequence labeling, fine-tuned generative extraction 및 few-shot in-context learning의 세 가지 접근 방식을 비교하고, 동기적으로 작동하는 것이 얼마나 도전적인지 보여주었다.

###### Optimized Tokenization for Transcribed Error Correction (https://aclanthology.org/2023.emnlp-main.802/)
- Anthology ID: 2023.emnlp-main.802 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 발음의 변화, 오디오 조건의 악화 및 라벨이 부족한 데이터 등에 직면한 음성 인식 시스템의 어려움을 극복하기 위해 반복적인 에러를 수정하는 후처리 단계가 필요하다. 
    2. 이 논문에서는 실제 트랜스크립트 에러로부터 착안해 에러 분포를 사용한 합성된 데이터만을 사용하여 모델을 훈련하는 것이 성능을 크게 향상시킬 수 있다는 것을 실험적으로 보여준다. 
    3. 또한, BPE tokenizer의 어휘에 언어별 조정을 적용함으로써 훈련 데이터의 분포에 적응하는 동시에 트랜스크립트 에러의 지식을 유지하는 균형을 이룰 수 있다고 제안한다.

###### Beware of Model Collapse! Fast and Stable Test-time Adaptation for Robust Question Answering (https://aclanthology.org/2023.emnlp-main.803/)
- Anthology ID: 2023.emnlp-main.803 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 학습 언어 모델 (PLM)은 질문 답변 (QA)에서 큰 성공을 거두었지만, 실제 응용에서의 강건성은 아직 충분치 않아 분포 변화에 대응하기 힘들다. 
    2. 이 논문에서는 테스트 시간 적응 (TTA)이 모델 붕괴를 유발하는 이유를 조사하고 QA의 균형 잡히지 않은 레이블 분포가 그 원인임을 발견하였다. 
    3. Anti-CF를 제안하여 TTA의 안정성과 신뢰성을 향상시키는데 성공하였으며, 다양한 분포 변화 시나리오와 사전 학습 언어 모델에서 좋은 결과를 얻을 수 있음을 실험으로 입증하였다.

###### Generative Adversarial Training with Perturbed Token Detection for Model Robustness (https://aclanthology.org/2023.emnlp-main.804/)
- Anthology ID: 2023.emnlp-main.804 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 일반적인 적대적 학습 방법들은 임베딩 표현에 노이즈를 주지만, 실제 텍스트 기반의 공격은 이산적인 토큰으로 노이즈를 주므로, 임베딩 표현과 텍스트 토큰 간의 간극이 존재하여 적대적 학습의 효과가 제한될 수 있다.
    2. 이 논문에서는 이 간극을 메꾸는 새로운 생성 적대적 학습 프레임워크를 제안한다. 이 프레임워크는 경사 기반 학습, 적대적 샘플 생성, 토큰 노이즈 탐지를 통합하며, 토큰 수준의 지도 및 샘플 활용 효율성 향상을 제공한다.
    3. AdvGLUE 벤치마크의 다섯 개 데이터셋에서 수행된 실험 결과, 이 프레임워크가 모델의 robustness를 크게 향상시키며, 평균 정확도에서 ChatGPT의 최고 성능을 10% 능가한다.

###### Multi-Task Knowledge Distillation with Embedding Constraints for Scholarly Keyphrase Boundary Classification (https://aclanthology.org/2023.emnlp-main.805/)
- Anthology ID: 2023.emnlp-main.805 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 학술 논문의 중요한 키워드를 식별하고 사전에 정의된 클래스 (태스크, 프로세스, 물질 등)에 대해 분류하는 학술 키워드 경계 분류 작업을 위한 새로운 임베딩 제약 조건을 제안한다. 
    2. 이 논문은 기존의 단일 작업 모델 (teachers)과 다중 작업 모델 (student) 간의 임베딩 공간에서의 유사성을 강제하는 다중 작업 지식 전달에 대한 새로운 임베딩 제약 조건을 제안한다. 
    3. 실험 결과는 제안한 접근법이 이전의 연구 및 강력한 베이스라인보다 학술 논문 데이터셋에서 성능이 우수함을 보여준다.

###### Set Learning for Generative Information Extraction (https://aclanthology.org/2023.emnlp-main.806/)
- Anthology ID: 2023.emnlp-main.806 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 Information Extraction (IE)에서 sequence-to-sequence (Seq2Seq) 모델을 사용하기 시작했으나, 구조화된 객체들의 성질로 인해 순서 바이어스(order bias)가 있는 문제가 있다.
    2. 이 논문에서는 구조화된 객체들의 순열을 고려하여 집합 확률을 최적화하는 set learning 접근 방식을 제안한다.
    3. 실험 결과, 이 방법은 기존의 IE 프레임워크에서도 효과를 보여주며 다양한 작업과 데이터셋에서 일관적으로 성능을 향상시킨다.

###### Large Language Models and Multimodal Retrieval for Visual Word Sense Disambiguation (https://aclanthology.org/2023.emnlp-main.807/)
- Anthology ID: 2023.emnlp-main.807 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Visual Word Sense Disambiguation (VWSD)는 텍스트의 문맥에서 모호한 단어의 의미를 더 잘 나타내는 이미지를 후보 집합에서 찾는 도전적인 과제이다."
    2. 이 논문에서는 다양한 접근 방식을 적용하여 이 흥미로운 과제를 해결하기 위한 중요한 단계를 밟는다. 
    3. 문제를 텍스트-텍스트 및 이미지-이미지 검색, 그리고 질문-답변(QA)로 변환하여 관련 모델의 능력을 완벽히 탐구한다.

###### Be Selfish, But Wisely: Investigating the Impact of Agent Personality in Mixed-Motive Human-Agent Interactions (https://aclanthology.org/2023.emnlp-main.808/)
- Anthology ID: 2023.emnlp-main.808 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 협상 대화 시스템을 설계하는 자연스러운 방법은 self-play 강화학습을 통해 원한다. 그러나 이 방법은 협상에서 타협의 가치를 배우지 못하는 결함이 있는 시스템을 만들어 제안 양상을 표현하지 못한다.
    2. 본 논문에서는 협상 이론에 근거하여 훈련 절차를 수정하여 각각 다른 성격을 가진 에이전트를 설계하고 인간 파트너와의 성능을 분석하여 selfish agent를 제안한다.
    3. selfish agent는 자신의 성능을 최대화하면서 타협을 방지하여 자신과 협상 상대에게 가치를 창출하는 방식으로 좋은 성능을 보여주었다. 이러한 결과는 미래에 성공적인 협상 대화 시스템을 설계하는 데에 영향을 끼칠 것으로 기대된다.

###### Doolittle: Benchmarks and Corpora for Academic Writing Formalization (https://aclanthology.org/2023.emnlp-main.809/)
- Anthology ID: 2023.emnlp-main.809 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 학문적 글쓰기의 질을 향상시키는 것은 의미있지만 어려운 과제이다. 기존의 언어 개선 방법들은 문법 오류나 부적절한 단어 사용과 같이 고립된 문장 내에서의 국한된 언어적 특징에 초점을 맞추고 있다.
    2. 이 논문에서는 학문적 글쓰기의 전반적인 품질을 향상시키기 위해 Academic Writing Formalization (AWF) 이라는 더 일반적인 작업을 제안한다. 이를 위해 비-병렬 데이터셋인 Doolittle을 만들고, metric-oriented reinforcement learning (MORL) 기법을 사용하여 기존 언어 모델을 개선시킨다.
    3. 실험 결과, 기존의 텍스트 전환 모델과 문법 오류 수정 모델은 일부 AWF 측면을 다루지만 인간 수행 성능과는 상당한 차이가 있다. 반면, MORL 기법을 적용한 언어 모델은 bet과 ChatGPT와 견줄만한 향상된 성능을 보이지만 Doolittle의 정답 학문적 텍스트와는 아직 미세한 차이가 있다.

###### Token Prediction as Implicit Classification to Identify LLM-Generated Text (https://aclanthology.org/2023.emnlp-main.810/)
- Anthology ID: 2023.emnlp-main.810 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 방식과 달리 새로운 접근법으로 텍스트 생성과 관련된 대규모 언어 모델을 식별하는 방법을 소개한다. 
    2. 이 방법은 기본 언어 모델에 추가적인 분류 레이어를 추가하는 것이 아닌, 분류 작업을 다음 토큰 예측 작업으로 바꾸어 기본 언어 모델을 직접 feine-tune 하는 방식이다. 
    3. 실험 결과는 우리의 방법이 텍스트 분류 작업에서 우수한 성능을 보이며, 간단하고 효율적인 것을 강조하고 있다. 우리의 모델이 추출한 피처에 대한 해석적 연구는 명시적인 분류기가 없더라도 여러 LLMs의 서로 다른 쓰기 스타일을 구별하는 능력을 나타낸다.

###### On Evaluation of Bangla Word Analogies (https://aclanthology.org/2023.emnlp-main.811/)
- Anthology ID: 2023.emnlp-main.811 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 기존의 방글라(Bangla) 단어 임베딩의 품질을 평가하기 위한 벤치마크 데이터셋을 제시한다. 방글라는 세계에서 7번째로 많이 사용되는 언어이지만, 신뢰할만한 NLP 모델을 개발하는 것은 여전히 어렵다. 따라서 방글라 단어 임베딩의 품질을 평가하고 향후 연구를 이끌어가기 위한 벤치마크 데이터셋을 개발하는 것이 중요하다. 
    2. 우리는 방글라 단어 유추 문제를 위한 새로운 평가 데이터셋을 소개하고, 다양한 최신 임베딩 모델을 실험해보았다. 그 결과, 현재의 방글라 단어 임베딩 모델은 두 데이터셋 모두에서 높은 정확도를 달성하기 어려움을 보여주었다. 이는 다국어 NLP 연구에서 상당한 미흡함을 보여준다. 
    3. 따라서 방글라 단어 임베딩의 품질 향상을 위해 이러한 문제를 극복하기 위한 추가적인 연구가 필요하다.

###### Reconstruct Before Summarize: An Efficient Two-Step Framework for Condensing and Summarizing Meeting Transcripts (https://aclanthology.org/2023.emnlp-main.812/)
- Anthology ID: 2023.emnlp-main.812 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 회의는 보통 여러 참가자와 긴 대화가 포함되어 있어 중복되고 사소한 내용을 포함하는데, 이러한 도전을 극복하기 위해 효과적이고 효율적인 회의 요약을 위한 Reconstruct before Summarize (RbS)라는 2단계 프레임워크를 제안한다. 
    2. RbS는 회의 대본을 재구성하여 필수적인 내용을 주석을 달아 활용하는 self-supervised 패러다임을 먼저 사용하고, RPB(Relative Positional Bucketing) 알고리즘을 통해 (기존의) 요약 모델이 요약을 생성할 수 있도록 한다. 
    3. 우리의 제안된 RPB는 추가적인 재구성 과정에도 불구하고, 입력을 크게 압축하여 전통적인 요약 방법에 비해 빠른 처리와 메모리 소비를 줄일 수 있다. 함께 수행한 방법의 효과적이고 효율적인 평가 및 분석을 통해 우리의 방법이 이전의 최고 수준의 접근법보다 더 우수한 성능을 보인다는 것을 검증하였다.

###### XLM-V: Overcoming the Vocabulary Bottleneck in Multilingual Masked Language Models (https://aclanthology.org/2023.emnlp-main.813/)
- Anthology ID: 2023.emnlp-main.813 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 다국어 언어 모델은 100개 이상의 언어에 걸쳐 공유하는 하나의 어휘집에 의존한다. 그러나 이 어휘집 병목현상은 XLM-R과 같은 다국어 모델의 표현 능력을 제한하고 있다.
    2. 이 논문에서는 서로 어휘 중복이 거의 없는 언어들 사이에서 토큰 공유를 강조하지 않고, 각 언어에 충분한 커버리지를 얻기 위해 어휘 용량을 할당하는 방식으로 대규모 다국어 어휘를 확장하는 새로운 접근 방식을 소개한다.
    3. 이 개선된 어휘를 활용하여 XLM-V라는 백만 토큰 어휘를 사용하는 다국어 언어 모델을 훈련시켰고, XNLI, MLQA, XQuAD, TyDiQA 및 WikiAnn과 같은 다양한 작업에서 XLM-R보다 우수한 성능을 보였다. 특히 저자원 언어 작업에서 XLM-R 대비 MasakhaNER에서 11.2%, Americas NLI에서는 5.8%의 절대적인 성능 향상을 보였다.

###### Character-LLM: A Trainable Agent for Role-Playing (https://aclanthology.org/2023.emnlp-main.814/)
- Anthology ID: 2023.emnlp-main.814 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large language models, LLMs)은 사람의 지시를 이해하고 고품질의 텍스트를 생성할 수 있는 능력을 갖고 있기 때문에 인간 행동을 시뮬레이션하는 에이전트로 사용될 수 있다. 
    2. 이 논문에서는 LLM이 단순한 인간 행동보다 더 높은 형태로 사람을 시뮬레이션할 수 있는지를 알아보기 위해, 제한된 프롬프트 대신 특정 인물의 프로필, 경험 및 감정 상태를 갖는 에이전트를 훈련시키는 방법을 제안한다. 
    3. 실험 결과는 훈련된 에이전트를 인터뷰하고 에이전트가 자신의 캐릭터와 경험을 기억하는지를 평가하는 테스트 환경을 구축하여 효과를 평가하였으며, 흥미로운 관찰 결과를 제시하여 인간의 시뮬레이션에 도움이 되는 방향으로 발전시킬 수 있다.

###### Natural Language Decompositions of Implicit Content Enable Better Text Representations (https://aclanthology.org/2023.emnlp-main.815/)
- Anthology ID: 2023.emnlp-main.815 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사람들이 텍스트를 해석할 때, 언어 자체를 벗어나는 추론에 의존한다. 이 논문에서는 이러한 관찰을 바탕으로 의미를 고려한 텍스트 분석 방법을 소개한다.
    2. 큰 규모의 언어 모델을 사용하여 observed한 텍스트와 추론적으로 관련된 명제들의 집합을 생성하고, 이로 인해 생성된 내용의 타당성을 사람들의 판단을 통해 확인한다.
    3. 이러한 내재적인 내용을 명시적으로 표현하면, 주장의 유사성을 평가하거나 의견 데이터의 의미를 추론하는 등의 다양한 문제 상황에서 유용하게 활용될 수 있다.

###### A Scalable Framework for Table of Contents Extraction from Complex ESG Annual Reports (https://aclanthology.org/2023.emnlp-main.816/)
- Anthology ID: 2023.emnlp-main.816 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "회사의 ESG (환경, 사회, 지배구조) 연차 보고서을 구조화하는 것은 효과적인 Table of Contents (ToC) 추출의 핵심입니다."
    2. "이 논문에서는 초기 트리 구조를 구축한 다음 노드 하나씩 독립적으로 모델링하여 적절한 작업을 수행하는 새로운 ToC 추출 프레임워크를 제안합니다."
    3. "실험 결과, 우리의 방법이 이전 최첨단 베이스라인보다 우수한 성능을 보여주며 실행 시간의 일부분만 사용하여 처리 가능함을 입증하였습니다."

###### Semantic Space Grounded Weighted Decoding for Multi-Attribute Controllable Dialogue Generation (https://aclanthology.org/2023.emnlp-main.817/)
- Anthology ID: 2023.emnlp-main.817 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "사용자의 성격, 감정, 대화 행위와 같은 다양한 속성으로 chatbot의 발화 생성을 제어하는 것은 실용적으로 유용하지만 연구되지 않은 문제이다."
    2. "우리는 DASC라는 새로운 프레임워크를 제안한다. 이는 가중치 기반 디코딩 패러다임으로 강력한 제어성을 가지고 속성 의미 공간에서의 근거화를 통해 성능 향상을 이끈다."
    3. "실험 결과, DASC는 3 가지 측면의 동시 제어로 발화 생성 작업에서 높은 제어 정확도를 달성할 수 있으며, 분포에서 벗어난 강인성 테스트에서도 흥미로운 및 합리적으로 이치에 맞는 응답을 생성한다."

###### How do languages influence each other? Studying cross-lingual data sharing during LM fine-tuning (https://aclanthology.org/2023.emnlp-main.818/)
- Anthology ID: 2023.emnlp-main.818 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 언어 모델(MLM)은 다른 언어의 데이터에서 학습되어 개별 언어의 표현이 다른 언어의 데이터의 도움을 받을 수 있는 모델이다. 
    2. 이 논문에서는 TracIn이라는 훈련 데이터 속성(TDA) 방법을 사용하여 개별 언어의 테스트 예측에 가장 영향력 있는 훈련 샘플을 분석하여 MLM의 크로스-언어 공유 메커니즘을 새로운 관점에서 분석한다. 
    3. 이 연구에서는 MLM이 fine-tuning 동안 다른 언어의 데이터에 의존하는 것을 발견하였고, 테스트 언어 자체의 데이터로 습득된 지식을 보강하고 보완하는데 다른 언어의 훈련 샘플이 도움이 된다는 결과를 얻었다.

###### COFFEE: Counterfactual Fairness for Personalized Text Generation in Explainable Recommendation (https://aclanthology.org/2023.emnlp-main.819/)
- Anthology ID: 2023.emnlp-main.819 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델이 우리의 디지털 생활에 점점 통합됨에 따라, 개인화된 텍스트 생성(PTG)은 다양한 응용 분야에서 중요한 구성 요소로 부상하고 있다. 
    2. 그러나 PTG 모델의 학습에 사용되는 사용자 작성 텍스트의 편향은 언어적인 품질의 다른 수준을 사용자의 보호된 특성과 연결시킬 수 있으며, 모델은 이러한 편향을 상속받아 사용자의 보호된 속성과 관련하여 텍스트를 생성함으로써 불공평한 대우를 유발할 수 있다.
    3. 이 논문에서는 PTG의 공정성을 모색하고, 개인화된 설명 생성에 대한 공정성을 달성하는 일반적인 프레임워크를 제안한다. 초록에서 제안한 방법은 다양한 실험과 인간 평가를 통해 효과적임을 입증하였다.

###### NameGuess: Column Name Expansion for Tabular Data (https://aclanthology.org/2023.emnlp-main.820/)
- Anthology ID: 2023.emnlp-main.820 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델의 최근 발전으로 데이터베이스 산업을 포함한 여러 산업에서 혁신이 이루어지고 있다. 그러나 대량의 테이블 데이터를 처리할 때 일반적인 문제점 중 하나는 약어로 된 열 이름의 널리 사용되는 것으로, 이는 데이터 검색, 접근 및 이해 과제에서 성능에 부정적인 영향을 미칠 수 있다.
    2. 이 문제를 해결하기 위해 우리는 NameGuess라는 새로운 작업을 소개하였는데, 이는 데이터베이스 스키마에 사용되는 열 이름을 자연어 생성 문제로 확장하는 것이다. 우리는 새로운 데이터 제작 방법과 실제 테이블에서 추출한 예제를 포함한 사람에 의해 주석이 달린 평가 벤치마크를 사용하여 38.4K 개의 약어-확장 열 쌍의 학습 데이터셋을 생성하였다.
    3. 이 논문에서는 NameGuess의 동의어성과 모호성과 같은 복잡성에 대응하기 위해 테이블 내용과 열 헤더 이름에 의존하는 자기회귀 언어 모델을 개선하여 인간 수준의 성능을 달성하였고, 향후 가능성을 확인하기 위해 다양한 LLMs에 대한 포괄적인 분석을 수행하였다.

###### BLESS: Benchmarking Large Language Models on Sentence Simplification (https://aclanthology.org/2023.emnlp-main.821/)
- Anthology ID: 2023.emnlp-main.821 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 대형 언어 모델(Large Language Models, LLMs)의 텍스트 단순화(Text Simplification) 작업에서 최근 최첨단 모델들의 성능을 평가하는 BLESS 벤치마크를 제시한다.
    2. 여러 가지 사이즈, 구조, 사전 훈련 방법 및 접근성을 가진 44개 모델을 선정하여 위키피디아, 뉴스 및 의학과 같은 다양한 도메인의 세 가지 테스트 세트에서 평가한다.
    3. 이 평가는 자동적인 메트릭 뿐 아니라 다양한 모델들이 수행한 일반적인 수정 작업의 유형에 대한 대규모의 양적 조사 및 일부 모델 출력물에 대한 수동적인 질적 분석을 포함한다.

###### To Build Our Future, We Must Know Our Past: Contextualizing Paradigm Shifts in Natural Language Processing (https://aclanthology.org/2023.emnlp-main.822/)
- Anthology ID: 2023.emnlp-main.822 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어처리 (NLP)는 방법론, 자금 조달, 대중 인식에 영향을 미치는 비판적인 변화의 시기에 있다. 이 논문에서는 과거를 더 잘 이해하여 미래를 형성하는 방법을 알아보고자 한다.
    2. 우리는 26명의 NLP 연구자와 심층적인 인터뷰를 통해 문화, 인센티브, 인프라 등이 NLP 분야를 형성하는 요소를 연구했다. 
    3. 우리는 NLP 분야의 변화에 대한 주기적인 패턴 및 벤치마크 문화와 소프트웨어 인프라의 변화와 같은 다양한 변화를 확인하고, 과거와 현재에 대한 연구를 통해 앞으로의 방향에 대한 공유된 비전과 우려를 논의한다.

###### PALS: Personalized Active Learning for Subjective Tasks in NLP (https://aclanthology.org/2023.emnlp-main.823/)
- Anthology ID: 2023.emnlp-main.823 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 주관적인 NLP 문제에 대해 개인화된 솔루션을 활용할 수 있다. 학습된 모델은 각 독자에 대해 독립적으로 내용에 대한 지각을 추론한다. 훈련 데이터를 얻기 위해 일반적으로 텍스트를 사용자에게 무작위로 할당하여 주석을 달아야 하는데, 이는 비용이 많이 들고 효율성이 떨어진다.
    2. 개인화된 문맥에서 더 나은 개인마다 선호하는 학습을 위해 active learning 패러다임을 처음으로 적용하는 것을 제안한다. 이는 관련성이 더 높은 훈련 샘플을 선택하여 주석 작업을 완화하는 것을 목표로 한다.
    3. 새로운 개인화된 활동 학습 기법(PALS)을 제시한다. 이 기법은 학습자 개인의 선호도에 대한 문맥에서 텍스트의 관련성을 판단하는 새로운 다섯 가지 측정 지표를 사용한다. 이 기법은 aggression과 toxicity로 개별적으로 라벨링된 Wiki 토론 텍스트와 Unhealthy Conversations 데이터셋에서 검증되었다. PALS 기법은 무작위 선택보다 30% 이상 우수한 결과를 보여준다. 또한 우수한 품질을 유지하면서 필요한 주석 수를 줄이기 위해 사용될 수 있다.

###### ViStruct: Visual Structural Knowledge Extraction via Curriculum Guided Code-Vision Representation (https://aclanthology.org/2023.emnlp-main.824/)
- Anthology ID: 2023.emnlp-main.824 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최신 VLM(Vision-Language Model)은 객체 간의 관계와 같은 구조적 지식 추출에서는 여전히 성능이 제한적이다.
    2. 이 논문에서는 ViStruct라는 VLM을 훈련시키기 위한 훈련 프레임워크를 제안한다. 프로그래밍 언어의 내재된 구조를 활용하여 시각적 구조 정보를 표현한다.
    3. ViStruct는 시각적 구조를 점진적으로 이해하기 위해 과정 기반 학습을 도입하고, 시각적 이벤트 구조와 같은 복잡한 구조 이해에 하위 수준의 지식이 기여할 수 있다는 가정을 제시한다.

###### LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models (https://aclanthology.org/2023.emnlp-main.825/)
- Anthology ID: 2023.emnlp-main.825 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대용량 언어 모델 (LLMs)은 놀라운 능력으로 인해 다양한 응용 분야에서 사용되고 있다. (CoT) prompting 및 in-context learning (ICL)과 같은 기술의 발전으로 LLM에 전달되는 프롬프트는 점점 길어지고 수만 개의 토큰을 초과하기도 한다.
    2. 이 논문에서는 고압축률에서도 의미적 일관성을 유지하기 위한 예산 컨트롤러, 압축 내용 간의 상호 의존성을 더 잘 모델링하기 위한 토큰 수준의 반복 압축 알고리즘, 그리고 언어 모델 사이에서 분포 정렬을 위한 instruction tuning 기반의 메소드를 포함하는 특허 압축 방법을 제안한다.
    3. GSM8K, BBH, ShareGPT 및 Arxiv-March23와 같이 다양한 시나리오에서 수행된 실험과 분석을 통해 제안된 접근 방식이 최첨단 성능을 발휘하며 성능 손실이 거의 없이 최대 20배 압축이 가능하다는 것을 보여준다.

###### EXPLAIN, EDIT, GENERATE: Rationale-Sensitive Counterfactual Data Augmentation for Multi-hop Fact Verification (https://aclanthology.org/2023.emnlp-main.826/)
- Anthology ID: 2023.emnlp-main.826 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에 자동 다중 점프 사실 검증 작업이 큰 관심을 받고 있다. 그러나 이러한 잘 설계된 모델들은 도메인 이외의 데이터에서 성능이 좋지 않다. 
    2. 우리는 라벨을 뒤집어 생성하면서 복잡한 논리적 관계를 보존하는 언어적으로 다양하고 논리적인 카운터팩처얼을 생성하기 위해 "Explain-Edit-Generate" 아키텍처를 통한 합리적인 방법을 개발함으로써 이러한 한계를 극복한다. 
    3. 실험 결과, 우리의 접근 방식이 SOTA 기준을 능가하며, 언어적으로 다양한 카운터팩처얼 데이터를 유지하면서 논리적인 관계를 깨지 않고 생성할 수 있다는 것을 보여준다.

###### An Exploration of Left-Corner Transformations (https://aclanthology.org/2023.emnlp-main.827/)
- Anthology ID: 2023.emnlp-main.827 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "왼쪽 꼭짓점 변환은 context-free 문법에서 왼쪽 재귀를 제거하여 간단한 기술로 문법을 위에서 아래로 구문 분석 가능하게 만드는 중요한 단계입니다."
    2. 본 논문은 semiring-weighted production rule을 지원하고, 이동할 수 있는 왼쪽 꼭짓점을 더 세밀하게 제어하기 위해 이전의 왼쪽 꼭짓점 변환 방법을 일반화합니다.
    3. 실험을 통해 GLCT의 효율성과 9개 언어의 문법에서 왼쪽 재귀를 제거하는 능력을 확인하였습니다.

###### Characterizing and Verifying Scientific Claims: Qualitative Causal Structure is All You Need (https://aclanthology.org/2023.emnlp-main.828/)
- Anthology ID: 2023.emnlp-main.828 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 과학적 명제는 현상 또는 변수 간의 잠재적인 관계에 대한 임시의 진술이기 때문에 그들은 과학적인 명제 검증의 범주에서 연구 질문이나 가설의 구체적인 형태로 시작된다. 
    2. 이 논문은 과학적인 명제 검증에서 풀어야 할 과제에 대해 깊이있게 탐구하며, 과학적 명제에 내재된 인과구조 정보를 간과하고 있어 인과추론의 포괄적인 체인을 만들지 못한다고 주장한다.
    3. 우리는 풍부한 인과구조를 헤체로 형성하고, 주로 원인 요인들 간의 인과 추론을 용이하게 하기 위해 관심 요인에 대한 엄격한 관찰과 양방향 주의 기반의 그래프 신경망을 제안한다.

###### FOCUS: Effective Embedding Initialization for Monolingual Specialization of Multilingual Models (https://aclanthology.org/2023.emnlp-main.829/)
- Anthology ID: 2023.emnlp-main.829 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 높은 자원을 가진 언어로 미리 훈련된 모델 가중치를 시작점으로 사용하면, 특히 저자원 언어에 대해 고품질 언어 모델을 얻기 위한 데이터와 계산 필요성을 줄일 수 있다. 하지만, 대상 언어에 특화된 새로운 토크나이저를 사용하려면 소스 모델의 임베딩 행렬을 전이할 수 없다.
    2. 본 논문에서는, FOCUS라는 새로운 임베딩 초기화 방법을 제안한다. 이 방법은 소스 모델의 임베딩 행렬에 포함된 정보를 기반으로 새로운 토크나이저를 위한 임베딩 행렬을 효과적으로 초기화한다.
    3. 실험 결과, FOCUS는 무작위 초기화와 이전 연구에 비해 언어 모델링과 다양한 하위 작업(NLI, QA, NER)에서 우수한 성능을 보였다.

###### ByteSized32: A Corpus and Challenge Task for Generating Task-Specific World Models Expressed as Text Games (https://aclanthology.org/2023.emnlp-main.830/)
- Anthology ID: 2023.emnlp-main.830 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구에서는 언어 모델이 과학적이고 상식적인 추론 태스크의 명확하고 해석 가능하며 대화식인 세계 모델을 생성하는 능력을 조사한다. 이를 실행하기 위해, 20,000줄의 파이썬 코드로 이루어진 ByteSized32라는 텍스트 게임 데이터셋을 소개한다.
    2. 실험 결과로, GPT-4 모델이 이러한 게임을 템플릿으로 사용하여 새로운 주제에 대한 게임을 28%의 경우에 성공적으로 생성할 수 있는 것을 보여준다. 
    3. 또한, 게임의 진실성, 기술적 유효성, 태스크 사양 준수도 및 이김 여부 등을 평가하기 위한 자동화된 메트릭을 소개하여 전문가의 평가와 높은 일치도를 보여준다.

###### Skill-Based Few-Shot Selection for In-Context Learning (https://aclanthology.org/2023.emnlp-main.831/)
- Anthology ID: 2023.emnlp-main.831 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. In-context learning은 몇 가지 예제를 제공하여 대규모 언어 모델을 하위 작업에 적응시키는 패러다임인데, 이 때 적절한 예제를 선택하는 few-shot selection이 중요하다. 
    2. 기존의 기반 임베딩 방법은 타깃 작업에 중요하지 않은 surface natural language 특징에 쉽게 영향을 받을 수 있는 문제를 해결하기 위해 Skill-KNN을 제안했다.
    3. Skill-KNN은 모델을 학습하거나 미세 조정할 필요 없이 입력 데이터를 최적화하여 효과적으로 few-shot selection을 수행하며, 다양한 데이터셋과 backbone 모델에서 기존 방법들보다 우수한 성능을 보였다.

###### MaNtLE: Model-agnostic Natural Language Explainer (https://aclanthology.org/2023.emnlp-main.832/)
- Anthology ID: 2023.emnlp-main.832 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 설명 기법인 LIME과 달리, MaNtLE은 예측의 내부 추론을 자연어로 설명하는 모델이다.
    2. MaNtLE은 수천 개의 합성 분류 작업을 활용하여 신뢰할 수 있는 자연어 설명을 생성한다.
    3. 실험 결과, MaNtLE로 생성된 설명은 평균적으로 LIME과 Anchors보다 최소 11% 더 신뢰성이 있으며, 사람 평가에서도 MaNtLE을 이용한 설명을 통해 모델의 동작을 더 정확하게 예측할 수 있다는 것을 보여준다.

###### PTP: Boosting Stability and Performance of Prompt Tuning with Perturbation-Based Regularizer (https://aclanthology.org/2023.emnlp-main.833/)
- Anthology ID: 2023.emnlp-main.833 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 연구에서 prompt tuning이 downstream 자연어 이해 태스크에서 fine-tuning보다 언어 모델의 성능을 더 잘 활용할 수 있음을 보여주었다. 그러나 기존의 prompt tuning 방법은 훈련 불안정성 문제가 있으며, 랜덤 시드에 따른 점수의 분산이 크다.
    2. 이 논문에서는 prompt tuning의 불안정성을 해결하기 위해 주어진 데이터의 작은 변화가 손실 계면에 큰 변동을 일으키는 이전적 경향을 발견하고, 이를 완화하기 위해 왜곡 기반 규제기법을 소개한다.
    3. 실험 결과, 이러한 규제기법을 적용한 PTP 방법은 prompt tuning의 훈련 불안정성을 크게 완화하고 성능을 향상시킨다고 보여진다. 또한, 기존의 prompt tuning 방법들보다 SuperGLUE와 FewGLUE 벤치마크에서 각각 1.94%와 2.34%의 성능 향상을 이룬다.

###### Ling-CL: Understanding NLP Models through Linguistic Curricula (https://aclanthology.org/2023.emnlp-main.834/)
- Anthology ID: 2023.emnlp-main.834 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 심리언어학 및 언어 습득 연구에서의 언어 복잡성에 대한 특성화를 활용하여 NLP 태스크를 해결하기 위해 모델이 학습하는 언어적 지식을 이해하기 위해 데이터 기반 교육과정을 개발한다.
    2. 우리의 접근 방식은 데이터, 언어 복잡성에 대한 기존 지식, 그리고 모델이 훈련 중에 보이는 행동을 기반으로 한 언어 교육과정을 개발하는 것에 있다.
    3. 우리의 교육 과정 학습 접근법은 여러 벤치마크 NLP 데이터셋의 평가를 통해 각 태스크를 해결하기 위해 필요한 도전과 추론을 나타내는 언어 지표(지수) 세트를 식별한다. 이 작업은 NLP의 모든 영역에서 향후 연구에 지침을 제공하며, 언어 복잡성을 연구 및 개발 프로세스의 초기에 고려할 수 있도록 한다. 또한, 우리의 연구는 NLP의 표준과 공정한 평가를 검토할 필요성을 제기한다.

###### Towards Unsupervised Recognition of Token-level Semantic Differences in Related Documents (https://aclanthology.org/2023.emnlp-main.835/)
- Anthology ID: 2023.emnlp-main.835 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 두 문서 간의 의미적 차이를 자동으로 강조하는 것은 다양한 응용 분야에 유용할 수 있다. 우리는 의미적 차이를 인식하는 것을 토큰 수준의 회귀 작업으로 정의하고, 마스크된 언어 모델에 의존하는 세 가지 비지도 학습 접근법을 연구한다.
    2. 우리의 연구 결과는 단어 정렬 및 문장 수준 비교 학습을 기반으로 한 접근 방식이 골드 레이블과 강력한 연관성을 가지고 있다는 것을 보여준다.
    3. 하지만 모든 비지도 학습 접근법은 여전히 큰 개선余地을 남겨두고 있다.

###### Towards a Better Understanding of Variations in Zero-Shot Neural Machine Translation Performance (https://aclanthology.org/2023.emnlp-main.836/)
- Anthology ID: 2023.emnlp-main.836 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 기계번역은 지식 공유를 촉진하지만 zero-shot 번역의 품질이 낮은 경우가 많다. 이 논문에서는 zero-shot 번역 품질의 변동성에 관한 연구를 제시하고, 번역 방향에 따라 예측 가능한 결과를 얻을 수 있다는 것을 발견하였다.
    2. 목표 언어의 번역 품질, 어휘의 중복성, 언어적 특성은 zero-shot 번역 성능의 변동성에 영향을 미치는 세 가지 요소로 확인되었다.
    3. 학습 모델의 크기가 작을 경우, 언어가 속한 언어 가족이나 쓰기 체계도 zero-shot 번역에 영향을 준다. 또한 off-target 문제는 성능의 불충분함을 나타내는 증상으로, zero-shot 번역 문제를 해결하기 위해서는 더 많은 노력이 필요하다.

###### SEER : A Knapsack approach to Exemplar Selection for In-Context HybridQA (https://aclanthology.org/2023.emnlp-main.837/)
- Anthology ID: 2023.emnlp-main.837 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 복합적인 문맥에서의 질문 답변은 비구조화된 텍스트와 구조화된 테이블로부터 정보를 다양한 방식으로 결합해야하는 복잡한 과제입니다.
    2. 이 논문에서는 대규모 언어 모델이 소수의 exemplar를 기반으로 예측을 수행하는 인 콘텍스트 학습에 대한 효과적인 exemplar 선택 방법인 SEER를 제안합니다.
    3. SEER는 Knapsack 정수 선형 프로그램으로 exemplar 선택을 수행하며, 다양성 제약과 용량 제약을 고려하여 적절한 exemplar 집합을 선택할 수 있습니다.

###### Conversation Chronicles: Towards Diverse Temporal and Relational Dynamics in Multi-Session Conversations (https://aclanthology.org/2023.emnlp-main.838/)
- Anthology ID: 2023.emnlp-main.838 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어처리 분야에서, 오픈 도메인 챗봇은 중요한 연구 주제로 등장하였다. 그러나 기존의 오픈 도메인 챗봇 연구의 주요한 한계는 단일 세션 대화에만 초점을 두고, 여러 연속적 세션에서의 문맥적 정보를 이해할 필요성을 간과한다는 것이다.
    2. 이 논문에서는 타임 인터벌과 발화자 간의 관계가 포함된 긴 시간 동안의 대화 설정을 구현하기 위해 Conversation Chronicles라는 새로운 1M 개의 멀티-세션 대화 데이터셋을 소개한다.
    3. 이 데이터를 활용하여 학습된 ReBot이라는 대화 모델은 630M개의 파라미터만을 사용하여 긴 시간 동안의 문맥을 잘 이해하며 높은 인간 참여 점수를 보여준다.

###### DueT: Image-Text Contrastive Transfer Learning with Dual-adapter Tuning (https://aclanthology.org/2023.emnlp-main.839/)
- Anthology ID: 2023.emnlp-main.839 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 대조적 학습을 통해 구축된 비전 및 언어 모델에 대한 새로운 전이 학습 방법인 DueT을 제안한다. DueT은 이미지와 텍스트 인코더에 어댑터를 삽입하여, 유니모달 말뭉치로 사전 학습 된 모델을 초기화한 후 고정시킨다.
    2. DueT은 오직 이러한 어댑터만 학습하여, 학습 가능한 파라미터의 수를 줄이고 효율적인 학습을 가능하게 한다.
    3. 더 나아가, DueT의 어댑터는 일반적인 어댑터와는 달리 게이팅 메커니즘을 갖추어, 사전 학습된 유니모달 인코더에서 획득한 지식의 전이와 연결을 효과적으로 수행하면서, 잊혀지지 않도록 한다. DueT은 영어와 일본어 도메인에서의 0-샷 이미지 및 텍스트 검색에서 간단한 미세조정, 이미지 인코더 고정 및 텍스트 인코더 학습만 하는 기존 방법, 그리고 LoRA 기반 어댑터 방법보다 정확성과 파라미터 효율성 면에서 성능이 우수하다.

###### Towards a Unified Conversational Recommendation System: Multi-task Learning via Contextualized Knowledge Distillation (https://aclanthology.org/2023.emnlp-main.840/)
- Anthology ID: 2023.emnlp-main.840 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화식 추천 시스템에서 (Conversational Recommendation System) 추천 및 대화 모듈을 별도로 사용하는 것은 추천 결과와 생성된 응답간의 불일치를 초래한다. 
    2. 이를 해결하기 위해, 이 논문에서는 단일 모델이 추천과 대화 과제를 동시에 학습하는 다중 과제 학습을 제안한다. 
    3. 실험 결과, 본 학습 방법을 사용하여 추천 성능을 대폭 향상시킬 수 있으며 유창성을 향상시키고 다양성 측면에서도 유사한 결과를 달성할 수 있다는 것을 보여준다.

###### CLAIR: Evaluating Image Captions with Large Language Models (https://aclanthology.org/2023.emnlp-main.841/)
- Anthology ID: 2023.emnlp-main.841 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이미지 캡션의 기계 생성 평가는 유의미성, 시각적 구조, 객체 상호작용, 다양성 및 특이성과 같은 다양한 유사성 측면을 고려해야 하는 도전적인 과제이다.
    2. 기존 방법들은 특정 측면을 캡처하려고 노력하지만, 인간의 판단과 밀접하게 일치하는 전체적인 점수를 제공하지는 못한다.
    3. 이 논문에서는 CLAIR이라는 새로운 방법을 제안하는데, 이는 대규모 언어 모델의 zero-shot 언어 모델링 능력을 활용하여 후보 캡션을 평가한다. CLAIR은 기존 방법과 비교하여 인간의 평가와 강한 상관관계를 보여준다.

###### MoPe: Model Perturbation based Privacy Attacks on Language Models (https://aclanthology.org/2023.emnlp-main.842/)
- Anthology ID: 2023.emnlp-main.842 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 연구는 대형 언어 모델이 학습 데이터에 있는 민감한 정보를 무심코 노출시킬 수 있다고 보여주고 있다. 
    2. 이 논문에서는 모델의 파라미터에 노이즈를 추가하고, 로그 우도의 하강을 측정하여 사전 훈련된 언어 모델의 학습 데이터에 주어진 텍스트가 있는지 신뢰성 있게 확인할 수 있는 새로운 메서드인 MoPe를 제안한다.
    3. 70M에서 12B까지의 다양한 크기의 언어 모델에 대해 MoPe가 기존의 손실 기반 공격과 최근 제안된 불안정성 기반 방법보다 더 효과적임을 실험적으로 보여준다.

###### q2d: Turning Questions into Dialogs to Teach Models How to Search (https://aclanthology.org/2023.emnlp-main.843/)
- Anthology ID: 2023.emnlp-main.843 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 언어 모델의 대화 기능 중 하나는 주어진 대화 응답의 기반 정보를 독립적으로 검색할 수 있는 능력이다. 그러나 모델이 검색 질의 방법을 학습시키기 위한 훈련 데이터 확보는 시간과 자원이 많이 소요된다.
    2. 본 논문에서는 정보 탐색 대화를 질문에서 생성하는 자동 데이터 생성 파이프라인인 q2d를 제안한다.
    3. 실험 결과, 우리는 기존 방법과 비교해 인간이 작성한 대화 데이터와 유사한 품질의 자동 생성 대화를 생성할 수 있다는 것을 보여주었다.

###### Aligning Large Language Models through Synthetic Feedback (https://aclanthology.org/2023.emnlp-main.844/)
- Anthology ID: 2023.emnlp-main.844 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델(Large Language Models, LLMs)의 인간적 가치와의 조화를 이루는 것은 ChatGPT와 같은 프로프라이터리 LLMs로부터의 인간의 신호와 피드백, 혹은 확연한 인간 어노테이션에 의존하기 때문에 점점 더 중요해지고 있다.
    2. 본 연구에서는 상당한 양의 인간 어노테이션 없이도, 인공적인 피드백을 활용한 새로운 맵핑 학습 프레임워크를 제안한다. 
    3. 실험 결과, 우리의 모델인 ALMoST는 InstructGPT나 인간 어노테이션만을 사용하여 훈련된 최근 오픈소스 모델들보다 맵핑 벤치마크에서 뛰어난 성능을 보이고, 인간 평가에서도 다른 모델들에 비해 55.0%와 58.5%의 선호도를 가졌다.

###### You Told Me That Joke Twice: A Systematic Investigation of Transferability and Robustness of Humor Detection Models (https://aclanthology.org/2023.emnlp-main.845/)
- Anthology ID: 2023.emnlp-main.845 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 유머 감지는 대화형 인공지능에게 매우 관련 있는 작업이다. 그러나 지금까지는 영어 데이터셋만 존재하고, 해당 데이터셋에서 훈련된 모델이 얼마나 일반화되고 실제 상황에서 작동하는지에 대한 연구가 부족하다.
    2. 이 연구에서는 기존 데이터셋을 자세히 분석하고, 각각의 데이터셋에서 RoBERTa 기반 및 나이브 베이즈 분류기를 훈련하고 나머지 데이터셋에서 테스트함으로써 이러한 공백을 채우고자 한다.
    3. 훈련 및 테스트를 동일한 데이터셋에서 수행하면 좋은 결과를 얻을 수 있지만, 모델의 전이성은 크게 다르다. 전체적으로 서로 다른 출처의 농담이 포함된 데이터셋에서 훈련된 모델은 더 높은 전이성을 보이며, 훈련 데이터의 양은 더 적은 영향을 미친다.

###### Reading Order Matters: Information Extraction from Visually-rich Documents by Token Path Prediction (https://aclanthology.org/2023.emnlp-main.846/)
- Anthology ID: 2023.emnlp-main.846 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 다중 모달 사전 훈련 모델은 시각적으로 풍부한 문서에서의 정보 추출을 크게 향상시켰으나, 실제 세계의 스캔된 문서에서는 OCR 시스템에 의해 인식된 텍스트가 제대로 정렬되지 않는 독서 순서 문제가 있다. 이러한 독서 순서 문제를 해결하기 위해 우리는 Token Path Prediction (TPP)을 제안한다. 
    2. TPP는 문서 내에서 토큰 시퀀스로서 entity mentions을 예측하는 간단한 예측 방법으로, 문서 레이아웃을 토큰의 완전한 방향 그래프로 모델링하고 entity로서 그래프 내의 토큰 경로를 예측한다.
    3. 또한, 스캔된 문서에 대한 NER의 벤치마크 데이터셋을 수정하여 실제 상황을 반영할 수 있도록하며, 실험 결과는 우리의 방법의 효과를 보여주고 문서에 대한 다양한 정보 추출 작업에 대한 보편적인 솔루션이 될 수 있는 잠재력을 제시한다.

###### Empower Nested Boolean Logic via Self-Supervised Curriculum Learning (https://aclanthology.org/2023.emnlp-main.847/)
- Anthology ID: 2023.emnlp-main.847 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문장 생성 모델이 갖는 인지 능력을 평가하기 위해 해당 논문은 boolean 로직에 초점을 맞춘다. 은 random selector만 하는 것으로 나타났으며 이를 개선하기 위해 Curriculum Logical Reasoning (Clr) 방법론을 제안한다.
    2. Clr 방법은 훈련 데이터를 점차적으로 복잡한 논리 패턴으로 증강하여 모델의 일반화 능력을 향상시키는 self-supervised learning method이다.
    3. 실험 결과 boolean 로직은 일반적인 논리적인 태스크를 개선시키는 좋은 기반이 되며 Clr은 보다 어렵고 복잡한 논리 패턴을 학습할 수 있는 능력을 제공한다.

###### The Sentiment Problem: A Critical Survey towards Deconstructing Sentiment Analysis (https://aclanthology.org/2023.emnlp-main.848/)
- Anthology ID: 2023.emnlp-main.848 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 sentiment analysis (SA)에 대한 사회기술적 측면을 조사하기 위해 응용, 모델 및 데이터셋에 대해 비판적으로 접근한 189편의 피어 리뷰 논문을 조사했습니다.
    2. 사회기술적 시스템에서 SA가 중요한 요소로 자리잡아 사회 및 기술적 사용자에게 영향을 미침을 인식하고 이를 기반으로 조사를 진행했습니다.
    3. 우리의 연구는 금융, 정부, 의학 등과 같은 분야에서 이 용어에 대한 별개의 개념화를 드러내며, 명확한 정의와 프레임워크의 부재로 인한 잠재적인 도전과 편향이 존재한다고 보여줍니다. 이 문제를 해결하기 위해, 우리는 도덕 시트를 제안하여 SA의 공정한 활용을 지원하기 위해 실무자들에게 안내할 수 있습니다.

###### Poisoning Retrieval Corpora by Injecting Adversarial Passages (https://aclanthology.org/2023.emnlp-main.849/)
- Anthology ID: 2023.emnlp-main.849 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 적대적 사용자가 훈련 쿼리와 유사도를 최대화하기 위해 이산 토큰을 왜곡하여 적은 수의 적대적 패턴을 생성하는 새로운 dense retrieval 시스템 공격을 제안한다.
    2. 공격자가 본 적이 없는 쿼리에 대해 이러한 적대적 패턴을 검색 결과로 인출하는 데 이 공격이 매우 효과적인 것을 보여준다.
    3. 더 놀랍게도, 이 적대적 패턴은 도메인 밖의 쿼리와 공격 성공률이 높은 코퍼스에 직접적으로 적용될 수 있으며, 금융 문서나 온라인 포럼에서 제기된 질문의 94% 이상을 오도할 수 있다.

###### DADA: Dialect Adaptation via Dynamic Aggregation of Linguistic Rules (https://aclanthology.org/2023.emnlp-main.850/)
- Anthology ID: 2023.emnlp-main.850 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 대규모 언어 모델은 주로 표준 미국 영어에 초점을 맞추고 있어 다른 영어 방언에 적용할 때 성능이 크게 저하되는 문제가 있다.
    2. 이 논문에서는 DADA(Dialect Adaptation via Dynamic Aggregation)라는 모듈식 방법을 제안하며, 이를 통해 SAE로 훈련된 모델에 다양한 방언에 대한 강건성을 부여한다.
    3. DADA의 구성적 아키텍처는 특정 방언 변형에 대한 대상적 적응뿐만 아니라 다양한 방언에 대한 동시 적응을 가능하게 한다는 것을 보여주고 있다.

###### Clustering Pseudo Language Family in Multilingual Translation Models with Fisher Information Matrix (https://aclanthology.org/2023.emnlp-main.851/)
- Anthology ID: 2023.emnlp-main.851 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다중 언어 번역 연구에서는 언어 가족의 이해와 활용이 매우 중요하지만, 조상 가족에 기반한 언어들의 클러스터링은 모델의 훈련 단계에서 사용된 데이터셋의 변동으로 인해 최적의 결과를 얻기 어렵다. 
    2. 이 논문에서는 언어쌍이 모델 파라미터에 유사한 영향을 미치는 경우, 언어간 유사성을 보여주는 pseudo language families를 소개한다. 
    3. 실험 결과에서는 이 pseudo language families를 사용하면 기존의 언어 가족보다 낯선 언어 쌍에 대한 다중 언어 번역 모델을 적응시키는 데 성능이 향상되었다고 보여졌다.

###### Unifying Discrete and Continuous Representations for Unsupervised Paraphrase Generation (https://aclanthology.org/2023.emnlp-main.852/)
- Anthology ID: 2023.emnlp-main.852 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Unsupervised paraphrase generation"은 다양한 NLP 응용에서 이점을 얻을 수 있는 어려운 작업이다. 
    2. 현재의 unsupervised 방법들은 주로 번역 또는 무디파잉을 활용하는데, 이는 번역 말뭉치가 필요하며 표면 구조에서 원래 문장과 지나치게 유사한 패러프레이즈를 생성한다. 
    3. 이 논문에서는 번역 데이터에 의존하지 않고 서로 다른 표면 구조에서 다양한 가닥의 pseudo-paraphrases를 생성하는 self-supervised pseudo-data construction 방법을 제안하고, 의미와 entity를 이산 및 연속 변수로 인코딩하여 유사성을 제어하고 정확한 entity를 유지할 수 있는 unsupervised paraphrasing 모델을 제안한다.

###### The Benefits of Label-Description Training for Zero-Shot Text Classification (https://aclanthology.org/2023.emnlp-main.853/)
- Anthology ID: 2023.emnlp-main.853 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 훈련된 언어 모델은 훈련 데이터에서 의미적 지식을 전달하여 downstream 태스크에서 특정 레이블 집합을 분류함으로써 zero-shot 텍스트 분류를 개선시켰다. 
    2. 이 논문에서는 최소한의 노력으로 zero-shot 정확도를 더 향상시키는 방법을 제안한다. 
    3. 텍스트 데이터 대신 레이블을 언어로서 설명하는 소량의 fintuning 데이터를 활용하여 다양한 주제와 감성 데이터셋에서 zero-shot보다 17-19% 높은 정확도를 보인다.

###### Multilingual Pixel Representations for Translation and Effective Cross-lingual Transfer (https://aclanthology.org/2023.emnlp-main.854/)
- Anthology ID: 2023.emnlp-main.854 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 픽셀 표현을 사용하여 다국어 기계 번역 모델을 효과적으로 학습하는 방법을 도입하고 보여줍니다.
    2. 단어 부분 표현과 비교하여 픽셀 표현을 사용하면 언어와 문자 스크립트의 다양한 범위에 대해 성능이 향상되는 것을 실험적으로 보여줍니다.
    3. 픽셀 표현의 다양한 특성과 여러 스크립트 간 및 내부에서의 매개 변수 공유를 탐색하여 어떤 상황에서 양호한 전이를 이뤄낼 수 있는지 파악합니다.

###### Finding Authentic Counterhate Arguments: A Case Study with Public Figures (https://aclanthology.org/2023.emnlp-main.855/)
- Anthology ID: 2023.emnlp-main.855 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 연구들은 세부 개인에 대한 혐오적 컨텐츠에 대항하는 카운터 혐오(Counterhate) 인수를 제공하기 어렵다. 
    2. 본 연구에서는 여러 он라인 기사에서 가져온 54,816개의 혐오적 트윗-문단 쌍으로 이루어진 코퍼스를 제시한다.
    3. 온라인 기사에서 인수를 찾는 것은 인수를 지지하지 않는 주장을 만들 수 있는 카운터 혐오 발생 방법에 비해 효과적인 대안이 될 수 있음을 보여준다.

###### Can We Edit Multimodal Large Language Models? (https://aclanthology.org/2023.emnlp-main.856/)
- Anthology ID: 2023.emnlp-main.856 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문에서는 multimodal Large Language Models (LLMs)를 편집하는 데 중점을 둔다. Single-modal LLMs를 편집하는 것보다 multimodal 모델 편집은 더 어렵고, 편집 과정에서 더욱 신중한 고려가 필요하다.
    2. 이를 위해, 우리는 multimodal LLMs를 편집하고 평가하기 위한 새로운 벤치마크인 MMEdit를 구축하고 혁신적인 메트릭을 제공한다.
    3. 우리는 다양한 모델 편집 기준에 대한 포괄적인 실험을 수행하고, multimodal LLM의 다른 구성 요소를 편집하는 것의 영향을 분석한다. 기존의 베이스라인은 일부 경우에는 multimodal LLMs를 편집할 수 있지만 효과는 여전히 만족스럽지 못하며, 이 작업의 어려움을 나타낸다.

###### Exploring Discourse Structure in Document-level Machine Translation (https://aclanthology.org/2023.emnlp-main.857/)
- Anthology ID: 2023.emnlp-main.857 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 문서 수준 기계 번역(DocMT) 방법의 성능이 만족스럽지 못한 이유는 긴 범위의 정보를 활용하기 어렵기 때문이다.
    2. 이 논문에서는 문맥의 구조를 활용하여 문서 수준 기계 번역에서 성능을 향상시키는 방법을 제안한다.
    3. 실험 결과, RST-Att 모델이 이전 연구보다 더 나은 성능을 보여주며, 담화 정보를 활용한다는 것을 입증한다.

###### ClusterLLM: Large Language Models as a Guide for Text Clustering (https://aclanthology.org/2023.emnlp-main.858/)
- Anthology ID: 2023.emnlp-main.858 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "ClusterLLM"는 ChatGPT와 같은 instruction-tuned 큰 언어 모델의 피드백을 활용하는 텍스트 클러스터링 프레임워크이다. 기존의 unsupervised 방법과 비교했을 때, ClusterLLM은 (1) LLM의 기능을 활용하여 새로운 능력을 갖게 되면서, (2) 텍스트 명령 및 주석 데이터를 통해 사용자의 클러스터링 선호도를 이해할 수 있다는 이점이 있다. 
    2. ChatGPT에 하드 트리플렛 질문을 주어 작은 embedder에 대한 세밀한 튜닝이 가능하며, 비용 효율적으로 ChatGPT를 쿼리할 수 있다고 실험적으로 보여준다.
    3. 의사 결정된 세부사항으로부터 연속성이 가장 큰 클러스터 계층 구조를 튜닝함으로써, ChatGPT의 답변과 일관성이 가장 큰 클러스터링 세부성을 얻을 수 있다. ClusterLLM은 14개 데이터셋에서 클러스터링 품질을 일관되게 향상시키는 것을 보여주며, 데이터셋 당 평균 비용은 약 $0.6 수준이다.

###### CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code (https://aclanthology.org/2023.emnlp-main.859/)
- Anthology ID: 2023.emnlp-main.859 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. NL→Code 모델의 한계 중 하나는 생성된 출력을 신뢰할 수 있는 방식으로 평가하는 것이다. 이 논문에서는 BERTScore를 기반으로한 새로운 code generation 평가 메트릭인 CodeBERTScore를 제안한다.
    2. CodeBERTScore는 BERTScore와 달리 생성된 토큰뿐만 아니라 생성된 코드 이전의 자연어 입력을 인코딩하여, 생성된 코드와 주어진 자연어 컨텍스트의 일관성을 모델링한다.
    3. CodeBERTScore는 인간의 선호도와 기능적인 정확성과 더 높은 상관관계를 가지며, 높은 점수를 받은 코드는 인간에게 선호되고 실행시 정확하게 작동하는 경향이 있다.

###### Learn and Consolidate: Continual Adaptation for Zero-Shot and Multilingual Neural Machine Translation (https://aclanthology.org/2023.emnlp-main.860/)
- Anthology ID: 2023.emnlp-main.860 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 다국어 기계번역 (MNMT) 모델은 한 모델에서 여러 개의 번역 방향을 다룰 수 있고, 훈련에 없던 언어쌍 사이에서도 zero-shot 번역을 할 수 있지만, 어떤 언어쌍에 대해서는 상대적으로 번역 품질이 낮다. 
    2. 본 논문에서는 제한된 새 데이터가 도착할 때 supervised 및 zero-shot 번역 모두에 대해 MNMT 모델을 지속적으로 업데이트하는 방법을 제안한다.
    3. 실험 결과 및 추가 분석에서, 우리의 방법이 초기에 성능이 약했던 번역 방향에서 기존의 MNMT 모델의 성능을 효과적으로 개선하고, 원래 성능이 좋았던 번역 방향에서의 성능 강화를 통해 실제 상황에서의 유연성을 제공함을 보여준다.

###### e-THERAPIST: I suggest you to cultivate a mindset of positivity and nurture uplifting thoughts (https://aclanthology.org/2023.emnlp-main.861/)
- Anthology ID: 2023.emnlp-main.861 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 정신건강 환자들을 위한 전 세계적으로 접근 가능한 대화 시스템은 필수적인데, 이를 위해서는 사용자의 성별, 연령, 페르소나, 감정 등에 따라 맞는 말을 할 수 있어야 한다. 이 논문에서는 이 목표를 위해, 사용자의 프로파일과 속성에 맞는 응답을 생성하는 새로운 대화 시스템인 "e-THERAPIST"를 제안한다. 
    2. 저자들은 PsychoCon이라고 불리는 특별한 대화 데이터셋을 구성했고 이는 (i) 대화 수준에서 - 사용자의 프로파일 정보 (성별, 나이, 페르소나)와 치료사의 심리치료 접근 방식을 포함하고 있고 (ii) 문장 수준에서 - 사용자의 감정과 치료사의 예의와 대인관계 행동을 포함하고 있다.
    3. 논문에서는 정확한 예의롭고 대인관계적 행동을 익히기 위한 새로운 보상 모델을 고안했으며, 이를 사용하여 PsyCon에서 e-THERAPIST를 학습하는데 사용했다. 실험 결과로, 제안된 e-THERAPIST의 각 구성 요소의 효과성을 검증하였고, 이가 심리치료 환경에 대한 잠재적 영향력을 나타냈다.

###### AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages (https://aclanthology.org/2023.emnlp-main.862/)
- Anthology ID: 2023.emnlp-main.862 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 아프리카는 6개 이상의 언어 계열에서 2,000개 이상의 언어가 존재하며 모든 대륙 중 언어 다양성이 가장 높다. 하지만 아프리카 언어에 대해 NLP 연구가 매우 부족하다.
    2. 이 논문에서는 아프리카 언어에 대한 고품질 주석된 데이터셋인 AfriSenti를 소개한다. 이 데이터셋은 14개의 아프리카 언어에 대한 110,000개 이상의 트윗을 포함하고 있으며, 이를 기반으로 한 센티멘트 분석 벤치마크를 제시한다.
    3. 이 논문은 AfriSenti 데이터셋에 대한 베이스라인 실험 결과와 그 유용성에 대해 논의하고 있다.

###### Quantifying Character Similarity with Vision Transformers (https://aclanthology.org/2023.emnlp-main.863/)
- Anthology ID: 2023.emnlp-main.863 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 레코드링크는 다른 소스로부터의 데이터를 연결해야하는 많은 사회과학 연구에 필수적이며, 현재 사용되고 있는 문자열 매칭 방법은 구현과 확장에 유리하지만 정확도가 저조하다. 
    2. 본 연구에서는 Vision Transformers (ViT)를 사용하여 OCR을 통해 생성된 문서들에서 문자 치환 비용을 측정하기 위한 기반 방법을 개발한다. 
    3. 모델은 보편적인 문자 유사도를 학습하고 자원이 제한된 상황에서도 적용 가능하며, 3,000년 전의 중국 고대 문자에 대한 유사도도 표현할 수 있다.

###### Syllogistic Reasoning for Legal Judgment Analysis (https://aclanthology.org/2023.emnlp-main.864/)
- Anthology ID: 2023.emnlp-main.864 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large Language Models, LLMs)의 놀라운 발전으로 인해 법적 판단 보조 도구가 빠르게 발전하고 있지만, 신뢰할 수 있는 법적 판단 분석 결과없이 모델이 생성한 결과를 신뢰하기는 어렵다.
    2. 법적 판단 분석을 위해 법조 인지 연구자들은 논리주의 추론을 이용하여 소송 당사자의 주장을 선택하고 평가하는 것이 일반적이지만, 법적 판단 분석을 위한 논리주의 추론의 발전은 자원의 부족으로 인해 방해받고 있다.
    3. 이 논문에서는 법적 판단 분석을 위한 대규모 논리주의 추론 데이터셋을 구축하고, 대형 언어 모델을 벤치마크로 선택하여 그들의 법적 판단 분석 능력을 깊이 있는 분석을 수행한다.

###### Improving Transformer-based Program Repair Model through False Behavior Diagnosis (https://aclanthology.org/2023.emnlp-main.865/)
- Anthology ID: 2023.emnlp-main.865 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 딥러닝 모델을 활용한 자동 프로그램 복구에 대한 연구는 최근 큰 관심을 받고 있다. 그러나 현재 이 분야의 연구들은 모델의 잘못된 동작을 탐지하고 수정하는 것에 대한 조사가 부족하다.
    2. 이 논문에서는 transformer 기반의 프로그램 복구 모델의 잘못된 동작을 진단하고 수정하기 위한 방법론을 제안한다. 이를 위해 모델의 동작을 측정하는 행동 벡터, 잘못된 동작을 식별하는 행동 판별자 (BeDisc), 그리고 잘못된 동작을 수정하는 두 가지 방법을 제안한다.
    3. 대규모 실험을 통해 BeDisc는 86.6%의 불균형 정확도로 잘못된 동작을 분류할 수 있었으며, 첫 번째 처리 방법인 초기 중단은 60.4%의 잘못된 동작을 제거하면서 97.4%의 복구 정확도를 유지했고, 두 번째 처리 방법인 가림막 우회는 상위 1위 복구 정확도를 평균 40.5% 향상시켰다는 결과를 보였다. 이 실험 결과는 프로그램 복구 모델에서 잘못된 동작을 조사하는 것이 중요함을 보여준다.

###### SUT: Active Defects Probing for Transcompiler Models (https://aclanthology.org/2023.emnlp-main.866/)
- Anthology ID: 2023.emnlp-main.866 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 프로그램 번역의 현재 모델들은 여전히 기본적인 구문 오류를 범하는데, 특히 소스 언어에 없는 문법 요소가 있는 경우 더 많이 발생한다.
    2. 우리는 프로그래밍 언어 번역을 위한 BLUE, CodeBLUE, 연산 정확도와 같은 메트릭이 이러한 문제를 보여주지 못한다고 지적하고 새로운 메트릭을 도입한다.
    3. 우리는 정확성과 테스트 점수에 대한 해석 가능한 평가 메커니즘을 포함한 SUT(Syntactic Unit Tests)라는 새로운 활성 결함 접근 스위트를 개발하였고, 실험 결과로 ChatGPT와 같은 강력한 모델도 이러한 기본 유닛 테스트에서 실수를 저지른다는 것을 보여주었다.

###### KCTS: Knowledge-Constrained Tree Search Decoding with Token-Level Hallucination Detection (https://aclanthology.org/2023.emnlp-main.867/)
- Anthology ID: 2023.emnlp-main.867 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델은 인간 수준의 자연어 생성 능력을 보여주었으나, 그들이 잘못된 정보를 생성하는 문제인 '환각' 문제는 그들의 배치에 중대한 위험을 야기한다.
    2. 이 문제를 해결하기 위한 일반적인 방법은 관련 지식을 검색하고 해당 지식으로 언어 모델을 fine-tuning하는 것이다. 그러나 이 메서드는 훈련 비용이 매우 높으며, 멀티태스킹 모델에서 치명적인 잊어버림을 일으킬 수 있다.
    3. 이 논문에서는 지식 제약 디코딩 방법인 KCTS (Knowledge-Constrained Tree Search)를 제안한다. KCTS는 지식 분류기 점수와 MCTS (Monte-Carlo Tree Search)를 사용하여 언어 모델이 각 디코딩 단계에서 기준 지식과 일치하는 텍스트를 생성하도록 안내한다.

###### CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2SQL (https://aclanthology.org/2023.emnlp-main.868/)
- Anthology ID: 2023.emnlp-main.868 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 Text-to-SQL 생성기는 대화 내용에서 전체 스키마를 인코딩해야 하는데, 이는 열 천 개 이상의 컬럼을 가진 대형 데이터베이스에서는 고비용이거나 실용적이지 않다. 
    2. 논문에서는 효과적인 검색을 위해 두 단계로 진행되는 프로세스를 제안하고, LLM을 사용하여 쿼리에 대답할 충분한 후보 스키마를 생성하여 대량 검색 결과의 일부를 추출한다.
    3. 존재하지 않는 스키마 하위집합에 대한 벤치마크를 도입하고, 제안한 방법이 SOTA retrieval 기반 augmentation 방법보다 더 높은 recall을 달성한다는 것을 보여준다.

###### This Reads Like That: Deep Learning for Interpretable Natural Language Processing (https://aclanthology.org/2023.emnlp-main.869/)
- Anthology ID: 2023.emnlp-main.869 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 프로토타입 학습은 해석 가능한 결정을 위한 머신 러닝 방법으로, 새로운 데이터를 분류하기 위해 학습된 프로토타입과의 유사성을 활용한다. 이 논문은 컴퓨터 비전에 주로 적용되던 프로토타입 네트워크를 자연어 처리에 확장하는 것을 제안한다.
    2. 우리는 사전 학습된 문장 임베딩의 정보적인 차원에 초점을 맞춘 가중 유사도 측정을 도입하여 유사성 계산을 개선하는 방법을 제안한다.
    3. 또한, 프로토타입과 입력 문장으로부터 예측에 관련 있는 단어를 추출하는 후처리 설명 기능을 제안하고, 이전의 프로토타입 기반 방법에 비해 예측 성능과 설명의 충실성을 향상시키는 것을 실험적으로 입증한다.

###### Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs (https://aclanthology.org/2023.emnlp-main.870/)
- Anthology ID: 2023.emnlp-main.870 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 시각과 언어 모델(VLMs)은 다양한 과제에서 놀라운 제로샷 성능을 보여주었지만, 구성적인 장면 이해와 같은 측면을 전부 포착하기는 어렵다고 최근 연구들이 보여주었다.
    2. 시각적 측면에서는 "SG Component"를 이미지 트랜스포머에 도입하여 SG 정보를 예측하도록 학습하고, 텍스트 측면에서는 SG를 활용하여 장면의 다양한 구성 요소를 강조하는 미세한 캡션을 생성한다.
    3. 우리의 방법은 작은 SG 데이터셋에서도 사전 훈련된 VLMs의 구조적 이해를 향상시킬 수 있음을 보여주고, ZS 능력이 약간 감소하는 것 외에도 여러 인기 있는 VLMs의 성능을 향상시킨다.

###### TLM: Token-Level Masking for Transformers (https://aclanthology.org/2023.emnlp-main.871/)
- Anthology ID: 2023.emnlp-main.871 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformer 모델에서 attention mechanism을 상속 받은 structured dropout (attention dropout, DropHead 등) 방법들이 제안되었는데, 이 논문은 overfitting을 줄이기 위해 구조 수준이 아닌 token-level에서 regularization을 수행하기 위한 새로운 scheme을 제안한다.
    2. Token-Level Masking (TLM) training strategy를 제안하여 self-attention의 연결을 정규화하는데 효과적이고 구현하기 쉬운 두 가지 masking 기법을 개발하였다.
    3. TLM의 일반성과 효과성을 다양한 NLP task에서 평가한 결과, attention dropout과 DropHead에 비해 일관적으로 우수한 성능을 보이며, 예를 들어 GLUE에서 BERT-large와 함께 0.5 포인트 성능을 향상시켰다.

###### Addressing NER Annotation Noises with Uncertainty-Guided Tree-Structured CRFs (https://aclanthology.org/2023.emnlp-main.872/)
- Anthology ID: 2023.emnlp-main.872 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실제 NER 데이터셋은 주석 오류, 일관성 부재, 주관적 표현으로 인해 소음이 많이 발생한다. 이러한 소음은 기존 지도 학습 방법에 대한 중대한 도전 과제를 제공한다.
    2. 우리는 NER에 대해 소음을 해결하기 위한 새로운 통합된 접근 방식을 제시한다. 우리의 방법은 NER을 구성 트리 구문 분석 문제로 간주하며, 불확실성 평가를 위해 트리 구조화된 CRFs를 활용한다.
    3. 네 개의 실제 데이터셋에 대한 광범위한 실험을 통해 우리의 모델이 부분적이고 잘못된 주석 오류를 해결하는 데 탁월한 성능을 보인다는 것을 입증한다. 특히, 90% 주석 소음이 있는 극단적인 시나리오에서도 우리의 모델은 뛰어난 성과를 보인다.

###### Hi Guys or Hi Folks? Benchmarking Gender-Neutral Machine Translation with the GeNTE Corpus (https://aclanthology.org/2023.emnlp-main.873/)
- Anthology ID: 2023.emnlp-main.873 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 특히 문법적 성별 언어로의 번역에서 성별 평등은 우리의 커뮤니케이션 방식에 내재되어 있으며, 기계 번역에서는 종종 남성 중심 및 성별 고정관념적인 표현을 사용하여 성별 불평등을 유지한다. 
    2. 우리의 연구는 포용적인 언어에 대한 요구를 해결하기 위해 영어에서 이탈리아어로의 성별 중립적인 번역에 집중하여, 이를 위한 벤치마크를 제안하고 자동 평가 방법을 탐구한다. 
    3. GeNTE라는 자연스러운, 양방향 테스트 세트를 소개하며, 기존 기준 기반 평가 접근 방식을 살펴보고 한계를 강조하고 성별 중립적인 번역을 평가하기에 더 적합한 비교용 없는 방법을 제안한다.

###### Multilingual Holistic Bias: Extending Descriptors and Patterns to Unveil Demographic Biases in Languages at Scale (https://aclanthology.org/2023.emnlp-main.874/)
- Anthology ID: 2023.emnlp-main.874 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "HolisticBias 데이터셋의 다국어 확장인 Multilingual HolisticBias를 소개한다. 이 데이터셋은 50개 언어에 걸쳐 분산된 20,459개의 문장으로 구성되어 있으며, 13개의 인구통계적 축으로 분류된다. Multilingual HolisticBias는 다양한 언어에서 인구통계적 불균형을 밝히고, 그에 대한 완화 방안을 정량화하는데 사용될 목적으로 만들어진다."
    2. "연구 결과, 영어로부터 다른 언어로의 번역은 남성을 인용했을 때 여성을 인용한 경우보다 평균적으로 8 spBLEU 더 우수한 번역 품질을 보인다. 그리고 XX-to-EN 방향으로, 소스 입력이 성별(남성 또는 여성)만 다른 경우 남성 번역이 여성 번역보다 평균 4 spBLEU 더 우수하다는 것을 비교 분석하였다."
    3. "문장을 공통 다국어 문장 표현 공간에 임베딩할 때 대부분의 언어에서 남성 번역이 영어 중립 문장에 대해 여성 번역보다 더 가깝다는 것을 확인하였다."

###### GlobalBench: A Benchmark for Global Progress in Natural Language Processing (https://aclanthology.org/2023.emnlp-main.875/)
- Anthology ID: 2023.emnlp-main.875 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어처리 시스템의 성능 차이는 리소스 할당의 불균형과 소수 언어에 대한 최적의 인센티브 부족으로 설명될 수 있다. 
    2. 이 논문에서는 이러한 문제를 해결하기 위해 모든 언어의 모든 NLP 데이터셋의 진행 상황을 동적으로 추적하는 GlobalBench를 소개한다. 
    3. GlobalBench는 정확성 뿐만 아니라 언어별 유용성과 균등성을 추적하여 언어 기술이 세계 인구에 어떻게 제공되고 있는지 다각도로 보여주며, 소수 언어에 집중한 연구 노력을 장려한다.

###### DetGPT: Detect What You Need via Reasoning (https://aclanthology.org/2023.emnlp-main.876/)
- Anthology ID: 2023.emnlp-main.876 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 컴퓨터 비전 분야에서는 대형 언어 모델의 발전으로 인해 상당한 발전이 있었다. 이 논문에서는 구체적인 객체 이름에 의존하는 기존 객체 검출 방법과는 달리, 우리의 접근법은 자연어 지시문을 사용하여 시스템과 상호작용할 수 있는 "추론 기반 객체 검출"이라는 새로운 패러다임을 제안하고 있다.
    2. 제안된 방법은 사용자의 지시문과 시각적인 장면의 문맥 내에서 추론을 수행하고, 개방 어휘 객체 검출기를 활용하여 관심 대상을 자동으로 찾을 수 있다. 예를 들어, 사용자가 "차가운 음료수"를 원한다고 표현하면, DetGPT는 이미지를 분석하여 냉장고를 식별하고, 일반적인 냉장고 내용에 대한 지식을 활용하여 음료수의 위치를 찾을 수 있다.
    3. 이러한 유연성은 로봇공학, 자동화, 자율주행 등 다양한 분야에 적용 가능한 시스템을 만들 수 있게 한다. 저자들은 제안된 패러다임과 DetGPT가 더 정교하고 직관적인 인간-기계 상호작용의 잠재력을 보여준다고 말하며, 이를 통해 더 다양하고 상호작용적인 객체 검출 시스템을 개발할 수 있는 방향으로 기여할 것을 희망한다.

###### Language Models with Rationality (https://aclanthology.org/2023.emnlp-main.877/)
- Anthology ID: 2023.emnlp-main.877 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델(Large Language Models, LLM)은 문제해결 능력은 있으나, 내재된 "신념(beliefs)"이 답과 어떻게 연결되는지는 항상 명확하지 않다. 이러한 해석의 부재는 LLM의 보편적 사용에 방해가 된다. 
    2. 이 논문에서는 모델의 신념과 추론적 관계를 명시화하고, 모순을 해결하여 일관된 신념 네트워크에서 따라야 하는 해설 체인(chain-of-thought)을 통해 답을 지원한다. 
    3. REFLEX(Rational, Self-Reflecting Layer)라고 불리는 우리의 방법론은 LLM 위에 합리적이고 자기 반성적인 계층을 추가함으로써 모델 신념을 명확히 하고 모순을 해결한다. 이로써 일관된 신념 체계에서 온전한 해설 체인을 통해 지원되는 답을 도출한다.

###### Self-Improvement of Non-autoregressive Model via Sequence-Level Distillation (https://aclanthology.org/2023.emnlp-main.878/)
- Anthology ID: 2023.emnlp-main.878 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Non-autoregressive Transformer (NAT) 모델은 빠른 추론 속도를 가지고 있지만, NAT 모델의 본질적인 다중성(multi-modality) 문제 때문에 성능이 저하된다."
    2. "기존 작업들은 이 문제를 해결하기 위해 Autoregressive Transformer (AT) 모델이 생성한 압축된 데이터로 원시 데이터의 타겟을 대체하는 것으로 흔히 개선한다."
    3. "이 논문에서는 NAT 모델 자체에 의해 압축된 데이터를 생성하는 Sequence-Level Self-Distillation (SLSD) 방법을 제안한다. 이 방법은 추가적인 교사 네트워크를 필요로하지 않고, 같은 유형의 NAT 모델에서 생성된 자기압축 데이터를 사용하여 다른 NAT 모델에 적용할 수 있다."

###### Mitigating Temporal Misalignment by Discarding Outdated Facts (https://aclanthology.org/2023.emnlp-main.879/)
- Anthology ID: 2023.emnlp-main.879 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델은 사전 훈련 중 보았던 방대한 정보를 유지할 수 있지만, 이러한 지식이 날이 지나 황폐해질 수 있으며 업데이트하기 어렵다. 
    2. 따라서 우리는 지식이 얼마동안 유효할지 예측하는 FDP (Fact Duration Prediction)를 제안하여 모델이 구식 정보를 말하는 것을 피하고 최신 지식을 찾아야 하는 예측을 할 수 있도록 했다.
    3. 또한, 우리는 Fact Duration 모델링이 업계에서 핵심적인 임무를 담당하는 지식 기반 작업에서 보정을 향상시키는 것을 실험을 통해 보여주었다.

###### Open-world Semi-supervised Generalized Relation Discovery Aligned in a Real-world Setting (https://aclanthology.org/2023.emnlp-main.880/)
- Anthology ID: 2023.emnlp-main.880 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 관심을 받는 Open-world Relation Extraction (OpenRE)은, 기존 접근법에서는 미분류된 데이터의 모든 인스턴스가 새로운 클래스에 속한다고 가정하여 실용성을 제한하는 경향이 있다.
    2. 우리는 OpenRE 설정이 실제 데이터의 특성과 더 일치하도록해야한다고 주장한다. 
    3. 이를 위해 우리는 KNoRD라는 방법을 제안하는데, 이는 미분류 데이터에서 암묵적 및 명시적으로 표현된 관계를 효과적으로 분류하는것에 대해 알려준다.

###### IEKG: A Commonsense Knowledge Graph for Idiomatic Expressions (https://aclanthology.org/2023.emnlp-main.881/)
- Anthology ID: 2023.emnlp-main.881 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 연구들은 대용어 표현 (IE)을 이해하기 위해 PTLMs에 대용어를 포함한 문장으로 fine-tuning을 하는 것이었지만, 이 논문에서는 IEs의 비유적 해석을 위한 일반 상식 지식 그래프인 IEKG를 구축하여 PTLMs를 지식 모델로 변환한다.
    2. 실험 결과들은 다양한 PTLMs가 IEKG로 KM로 변환될 수 있다는 것을 보여준다. IEKG의 품질과 훈련된 KMs의 능력은 자동 및 인간 평가를 통해 검증된다. 
    3. 자연어 이해 애플리케이션을 통해 PTLM에 IEKG의 지식을 주입하면 IE 이해 능력이 향상되고 훈련 중에 보지 못한 IEs에 대해서도 일반화할 수 있음을 보여준다.

###### Bias Neutralization in Non-Parallel Texts: A Cyclic Approach with Auxiliary Guidance (https://aclanthology.org/2023.emnlp-main.882/)
- Anthology ID: 2023.emnlp-main.882 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Wikipedia와 많은 뉴스 사이트에 적용되고 있는 객관성은 많은 대형 언어 모델들의 가이드라인이자 목표다. 하지만, 기존 방법들은 평행 텍스트(편향된 문장과 편향이 없는 문장)을 훈련 데이터로 사용하며 새로운 도메인으로의 전이 성능이 좋지 않으며 중요한 편향 독립적 문맥을 잃을 수 있다.
    2. 이 논문에서는 새로운 접근인 FairBalance을 제안하는데, 이는 평행 텍스트 없이 편향 중립화를 가능하게 하는 사이클 일관성 적대 신경망을 사용하며, 모델 디자인은 편향 독립적인 콘텐츠를 보존하고, 부가적인 가이드를 통해 편향 유발 단어의 열을 강조해서 편향 중립화 품질을 향상시킨다.
    3. 다양한 실험 결과는 FairBalance가 다른 방법에 비해 주관적 편향 중립화를 크게 개선하는 것을 보여준다.

###### Fighting Fire with Fire: The Dual Role of LLMs in Crafting and Detecting Elusive Disinformation (https://aclanthology.org/2023.emnlp-main.883/)
- Anthology ID: 2023.emnlp-main.883 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대규모 언어 모델 (LLM)은 큰 영향력을 가지고 있지만 악용 가능성에 대한 우려가 있다. 이 논문에서는 "파이어(Fire)로 불(Fire)을 끄는" 전략을 제안하여 사람이 작성하거나 LLM이 생성한 잘못된 정보에 맞서는 방법을 제시한다.
    2. 먼저, GPT-3.5-turbo를 사용하여 진실과 위조된 LLM 생성 콘텐츠를 만든다. 그런 다음 cloze-style prompt에 zero-shot in-context semantic reasoning 기법을 적용하여 진실과 위조된 게시글 및 뉴스 기사를 구분한다.
    3. 실험에서는 GPT-3.5-turbo가 이전의 맞춤형 및 fine-tuned 디스인포메이션 탐지기에서 관찰된 감소와 달리 in-distribution 및 out-of-distribution 데이터셋에서 일관적으로 68-72%의 정확도를 달성하는 것을 관찰했다.

###### SMoP: Towards Efficient and Effective Prompt Tuning with Sparse Mixture-of-Prompts (https://aclanthology.org/2023.emnlp-main.884/)
- Anthology ID: 2023.emnlp-main.884 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 방법과 달리 SMoP는 짧은 소프트 프롬프를 사용하여 효율적인 학습과 추론을 할 수 있으며, 성능의 향상을 유지한다.
    2. SMoP는 다양한 데이터 하위 집합을 처리하는 여러 개의 짧은 소프트 프롬프를 학습하는 게이팅 메커니즘을 사용한다.
    3. 실험 결과, SMoP는 기준선 방법보다 더 나은 성능을 보여주며, 학습 및 추론 비용을 줄일 수 있다.

###### BRAINTEASER: Lateral Thinking Puzzles for Large Language Models (https://aclanthology.org/2023.emnlp-main.885/)
- Anthology ID: 2023.emnlp-main.885 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델들의 성공은 NLP 커뮤니티에서 인공지능적인 상식 기능을 필요로 하는 작업에 대한 관심을 끌었지만, 전형적인 상식 연관성과 다른 논리를 요구하는 문제인 lateral thinking puzzles은 아직 관심을 받지 못하고 있다.
    2. 본 논문에서는 lateral thinking 역량과 상식 연관성을 파악하는 BrainTeaser라는 다중선택형 QA 과제를 개발하였다.
    3. 실험 결과 instruction 모델과 상식 모델 모두 인간의 성능과 큰 차이를 보였으며, adversarial format에 대한 일관성을 고려했을 때 차이가 더욱 컸다는 것을 보여주었다.

###### When are Lemons Purple? The Concept Association Bias of Vision-Language Models (https://aclanthology.org/2023.emnlp-main.886/)
- Anthology ID: 2023.emnlp-main.886 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 비전-언어 모델인 CLIP과 같은 모델들은 영상 분류와 이미지-텍스트 검색에서 탁월한 성능을 보이지만, 더 세부적인 영상-언어 대응이 필요한 Visual Question Answering (VQA)와 같은 태스크에서는 성능이 나오지 않는다. 
    2. 이 논문에서는 이러한 이유에 대해 연구하고, 모델들이 보이는 Concept Association Bias (CAB)라는 현상을 VQA에 적용하는데 어려움을 일으키는 원인으로 제시한다. 
    3. CAB는 모델이 입력을 개념들의 모음으로 취급하고, 다른 부족한 개념을 모드간적으로 채우려고 시도하여 예상치 못한 zero-shot 예측을 만들어내는 경향을 가진다는 것을 실험을 통해 보여준다.

###### What Comes Next? Evaluating Uncertainty in Neural Text Generators Against Human Production Variability (https://aclanthology.org/2023.emnlp-main.887/)
- Anthology ID: 2023.emnlp-main.887 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 생성(NLG) 과제에서는 어떤 입력에 대해 여러 의사소통 목표가 가능하며, 각 목표는 다양한 방식으로 단어로 표현될 수 있다. 이 논문에서는 인간의 생성변이를 데이터 불확실성과 연결하여 분석하고, 생성 시스템의 불확실성을 조사하기 위해 예측된 확률 분포와 디코딩 알고리즘에 기반한 출력 문자열 공간을 조사한다. 
    2. 테스트 입력에 대해, 생성자의 다양성에 대한 맞춤법을 측정하여 NLG 모델과 디코딩 전략을 분석한다. 
    3. 이를 통해, 여러 샘플과 가능한 경우 다중 참조를 통해 생성자를 검사함으로써 모델의 불확실성 표현에 대한 이해 수준을 증가시킬 수 있다는 것을 보여준다.

###### Text Representation Distillation via Information Bottleneck Principle (https://aclanthology.org/2023.emnlp-main.888/)
- Anthology ID: 2023.emnlp-main.888 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 사전 훈련 언어 모델(PLM)은 텍스트 표현 분야에서 큰 성공을 보였으나, 컴퓨팅 비용과 고차원 표현의 문제로 실제 적용에 있어서 중요한 도전 과제가 되고 있다.
    2. 이 논문에서는 큰 모델을 작은 표현 모델로 전달하는 효과적인 방법인 지식 전달 (Knowledge Distillation) 기법인 IBKD를 제안한다.
    3. IBKD는 정보 병목 (Information Bottleneck) 원리에서 영감을 받아, 선생 모델과 학생 모델 간의 최종 표현 간 상호 정보량을 최대화하고, 동시에 학생 모델의 표현과 입력 데이터 간의 상호 정보량을 감소시키는 것을 목표로 한다. 이를 통해, 학생 모델은 중요한 학습 정보를 보존하면서 불필요한 정보를 피하므로 과적합의 위험을 줄일 수 있다.

###### Let GPT be a Math Tutor: Teaching Math Word Problem Solvers with Customized Exercise Generation (https://aclanthology.org/2023.emnlp-main.889/)
- Anthology ID: 2023.emnlp-main.889 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문에서는 대규모 언어 모델에서(math word problem solving capabilities) 학생 모델로 양자화하는 새로운 접근방식을 제시한다. 
    2. 우리의 접근 방식은 학생 모델의 약점을 고려하여 맞춤형 학습 경험을 제공하기 위해 교육 과학 원리(지식 추적, 맞춤형 학습)와 일치하는 목표 중심의 문제들을 생성하는 방식으로 설계되었다. 
    3. 실험 결과는 우리의 방법이 LLMs (예: GPT-3와 PaLM)보다 정확성에서 훨씬 우수한 성능을 보이며, 매우 적은 파라미터를 사용한다는 것을 나타내고 있다. 또한, 우리의 방법론 내의 다양한 구성 요소들의 효능을 입증하기 위해 포괄적인 분석을 제공한다.

###### FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions (https://aclanthology.org/2023.emnlp-main.890/)
- Anthology ID: 2023.emnlp-main.890 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Theory of mind (ToM) 평가는 현재 상호작용성이 없는 이야기를 사용하여 모델을 테스트하는 것에 초점을 맞추고 있다.
    2. 우리는 정보 불균형 대화적 맥락에서 질문에 답변하는 것을 통해 ToM을 엄격하게 테스트하는 새로운 벤치마크인 FANToM을 소개한다.
    3. 우리는 FANToM이 최신 LLMs에 대해 도전적인 것을 보여주고, 순차적 추론 또는 파인튜닝에도 인간보다 성능이 현저히 떨어진다.

###### Exploring the Boundaries of GPT-4 in Radiology (https://aclanthology.org/2023.emnlp-main.891/)
- Anthology ID: 2023.emnlp-main.891 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 큰 규모 언어 모델 (LLM)의 성공은 도메인과 응용 분야에 걸친 통합적인 기반 모델로 자연어 처리 패러다임을 크게 변경하였다. 본 논문에서는 GPT-4, 지금까지 가장 강력한 LLM,를 방사선학 보고서를 기반으로 하는 텍스트 기반 응용 애플리케이션에서 최신의 방사선학 전용 모델과 성능을 비교하여 평가한다. 
    2. 다양한 프롬프트 전략을 탐구하고, GPT-4를 다양한 방사선학 작업에 대해 평가한 결과, GPT-4는 현재의 최고 방사선학 모델과 비교하여 우수한 성능을 보여주거나 동등한 성능을 보여준다.
    3. GPT-4는 방사선학에 대한 지식 수준이 충분하며, 복잡한 문맥에서 세세한 도메인 지식이 필요한 경우에 가끔씩 오류가 발생한다는, 인증된 방사선과사의와의 광범위한 오류 분석을 통해 보인다.

###### A Frustratingly Easy Post-Training Quantization Scheme for LLMs (https://aclanthology.org/2023.emnlp-main.892/)
- Anthology ID: 2023.emnlp-main.892 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델을 포함한 대규모 인공지능 모델에서 효율적인 추론은 성능을 향상시키기 위해 매개변수 수가 계속 증가함에 따라 중요해졌다. 
    2. 본 논문에서는 메모리 및 컴퓨팅 병목 현상을 해결함으로써, 인퍼런스 중에 계산 부담을 완화하기 위한 양자화 방법을 제안한다. 줄어든 비트 수로 모델을 표현하면서, DRAM 액세스 빈도를 최소화하고 밀도 높은 행렬 형식을 통해 연산 병렬성을 완전히 활용하여 양자화된 모델은 엔드 투 엔드 지연 시간을 낮추고 자원 활용을 최적화한다. 
    3. Z-Fold라고 불리는 단순한 사후 학습 양자화 방법을 제안한다. 이 방법은 대규모 언어 모델에서 널리 사용되는 Transformer 구조의 특징을 완전히 활용한다.

###### A Comprehensive Evaluation of Biomedical Entity Linking Models (https://aclanthology.org/2023.emnlp-main.893/)
- Anthology ID: 2023.emnlp-main.893 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 바이오 의학 entity linking(BioEL)은 문서에 언급된 entity를 UMLS나 MeSH와 같은 의학 데이터베이스의 항목에 연결하는 과정이다. 
    2. 이 연구에서는 최근 9가지 최첨단 biomedical entity linking 모델을 통합된 프레임워크 아래에서 포괄적으로 평가하였다. 
    3. 평가 결과, 현재의 방법들은 유전자와 단백질을 올바르게 연결하는 데 어려움이 있으며, 맥락을 링크 결정에 효과적으로 통합하는 데 어려움이 있는 것으로 나타났다.

###### Exploring Jiu-Jitsu Argumentation for Writing Peer Review Rebuttals (https://aclanthology.org/2023.emnlp-main.894/)
- Anthology ID: 2023.emnlp-main.894 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문제의 핵심은 심층모델들이 surface-level 추론을 반박하는 대신에 underlying beliefs와 world views에 기반한 "attitude roots"와 "attitude themes"를 파악하여 대응하는 것이 더 효과적일 수 있다는 것이다.
    2. 이 논문은 Jiu-Jitsu와 마찬가지로 기존의 논리를 무효화시키는 대신에 상대방의 태도와 테마를 파악하고 그에 알맞은 반박을 선택하는 Jiu-Jitsu argumentation을 사용하여 "attitude and theme-guided rebuttal generation"을 소개한다.
    3. 기존의 피어 리뷰 데이터셋에 attitude roots, attitude themes, 및 canonical rebuttals을 추가하여 end-to-end attitude and theme-guided rebuttal generation 및 두 가지 하위 태스크의 성능을 평가한다.

###### LIMIT: Language Identification, Misidentification, and Translation using Hierarchical Models in 350+ Languages (https://aclanthology.org/2023.emnlp-main.895/)
- Anthology ID: 2023.emnlp-main.895 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. NLP 태스크에 대한 deep model의 정확성은 뛰어나지만, spurious pattern에 의존하는 한계로 인해 robustness가 제한된다고 보고되고 있다. 
    2. 기존의 데이터 증강 기법들은 spurious correlation에 영향을 받는다는 문제가 있는데, 이 논문에서는 "여러 개"의 counterfactual을 생성하여 더 robust한 supervision을 제공함으로써 매우 다양한 영역에서 성능을 개선할 수 있는 방법을 제안한다. 
    3. MCS-350 데이터셋을 통해 저자들은 언어 탐지를 위한 새로운 hierarchical model인 LIMIT을 제안하고, 이 모델은 오류를 55% (from 0.71 to 0.32) 개선하는 동시에 저자들의 새로운 benchmark인 FLORES-200에서도 40% (from 0.23 to 0.14) 개선하는 결과를 보였다.

###### FreeAL: Towards Human-Free Active Learning in the Era of Large Language Models (https://aclanthology.org/2023.emnlp-main.896/)
- Anthology ID: 2023.emnlp-main.896 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다양한 NLP 태스크에 대한 고품질 레이블된 데이터 수집은 시간과 노력이 많이 드는 작업이다. 본 연구에서는 큰 언어 모델 (LLM) 시대에서 어노테이션 비용을 감소시키는 방법을 탐구한다.
    2. FreeAL이라는 혁신적인 협력 학습 프레임워크를 제안하여 LLM으로부터 태스크별 지식을 상호작용적으로 추출하고 걸러낸다.
    3. 다양한 실험 결과에서 FreeAL은 인간의 감독 없이 SLM과 LLM의 제로샷 성능을 크게 향상시킴을 보여준다.

###### API-Assisted Code Generation for Question Answering on Varied Table Structures (https://aclanthology.org/2023.emnlp-main.897/)
- Anthology ID: 2023.emnlp-main.897 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 테이블 기반 질의응답 (TableQA)에서의 실행 가능한 프로그램 생성은 다양한 테이블 구조에 대한 적응이 어려운 문제였으나, 본 논문에서는 (1) Pandas 데이터 프레임을 다중 인덱스로 표현하는 통합 테이블QA 프레임워크, (2) 강력한 질의 언어로써의 Python, 그리고 (3) NL 질문을 Pandas 데이터 프레임에서 실행 가능한 Python 프로그램으로 변환하기 위한 few-shot prompting을 제안한다.
    2. 또한, 복잡한 관계형 질문에 대한 응답을 위해, 우리의 프레임워크는 Python 프로그램에서 호출할 수 있는 사용자 정의 API를 허용한다. 
    3. 본 논문에서는 관계형, 다중 테이블, 계층적 행렬 형태의 테이블을 다루는 네 가지 TableQA 데이터셋으로 실험을 수행하였고, 과거 최고 수준 시스템보다 뛰어난 성능 향상을 얻었다.

###### Data Factors for Better Compositional Generalization (https://aclanthology.org/2023.emnlp-main.898/)
- Anthology ID: 2023.emnlp-main.898 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 진단용 데이터 세트인 SCAN과 COGS는 scratch로 학습된 모델의 성능이 매우 낮음을 보여주고 있다. 그러나 더 크고 일반적인 데이터 세트에서 학습된 최신 모델들은 더 나은 일반화 능력을 보여준다. 
    2. 본 논문에서는 이런 모순을 해소하기 위해 데이터 세트의 규모, 패턴 복잡성, 예제 난이도 등 다양한 데이터 요소를 가진 Transformer 모델들을 학습시켜 실증적 분석을 수행한다. 
    3. 이를 통해 데이터 세트의 복잡성이 여러 다른 일반화 도전 과제에 대해 더 나은 일반화 성능을 보여주는 것을 발견하고, 단어 관계를 더 효과적으로 이해할 수 있도록 더 다양한 예제를 제공하고 예제 반복 빈도를 감소시켜 일반화 능력을 향상시킨다는 것을 알아내었다.

###### ChatEdit: Towards Multi-turn Interactive Facial Image Editing via Dialogue (https://aclanthology.org/2023.emnlp-main.899/)
- Anthology ID: 2023.emnlp-main.899 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 대화를 통한 얼굴 이미지 편집을 탐구하며, ChatEdit 벤치마크 데이터셋을 제공하여 이 문맥에서의 이미지 편집과 대화 능력을 평가한다. 
    2. ChatEdit는 CelebA-HQ 데이터셋을 기반으로 구축되었으며, 이미지에 대한 사용자 편집 요청에 대응하는 다중 턴 대화를 포함하고 있다. 
    3. 우리는 사용자 요청을 추적하고 응답을 생성하기 위한 대화 모듈과 이미지를 해당 요청에 맞게 편집하기 위한 이미지 편집 모듈로 구성된 프레임워크를 제안하며, 기존의 방식과 달리 에러 적립 및 속성 잊기 문제를 완화하기 위해 이전 턴의 출력을 조작하는 대신 전체 대화 기록에서 현재 턴의 사용자 요청을 직접 추적하고 초기 이미지를 편집한다.

