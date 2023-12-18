# Korean Three-Line Summarizations of Papers 201-300 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### Improving Chinese Pop Song and Hokkien Gezi Opera Singing Voice Synthesis by Enhancing Local Modeling (https://aclanthology.org/2023.emnlp-main.200/)
- Anthology ID: 2023.emnlp-main.200 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 가사와 악보를 기반으로 잘 들리는 보컬을 합성하는 데 사용되는 "노래 부르기 합성 (SVS)" 기술에서, 기존의 Transformer 기반 음향 모델은 전체 순서를 전역적으로 처리하고 간단한 L1 손실을 사용한다. 그러나, 이 방식은 순서 내에서의 로컬 모델링과 예측된 멜 스펙트로그램의 어려운 부분에 대한 로컬 최적화의 중요성을 간과한다.
    2. 이 문제를 해결하기 위해, 본 논문에서는 음향 모델에서 로컬 모델링을 개선하기 위한 두 가지 방법을 제안한다. 첫째로, 주변의 동음이의어 토큰에만 초점을 두는 가장 가까운 이웃 로컬 어텐션을 개발한다. 둘째로, 어려운 부분에 더 초점을 맞추기 위한 음소 수준의 로컬 적응적 가중치 손실 함수를 제안한다.
    3. 공개된 중국 팝 음악 및 Hokkien Gezi 오페라 데이터셋에서 우리의 방법의 일반성을 검증하였으며, 실험 결과는 강력한 기준과 비교했을 때 목적적 및 주관적 평가에서 상당한 향상을 보여주었다.

###### What Else Do I Need to Know? The Effect of Background Information on Users’ Reliance on QA Systems (https://aclanthology.org/2023.emnlp-main.201/)
- Anthology ID: 2023.emnlp-main.201 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. NLP 시스템은 관련 콘텍스트를 검색하여 질문에 대답하는 데에서 인상적인 성능을 보여주고 있다. 하지만 점점 커져가는 모델의 크기 때문에 모델의 지식이나 추론을 검색된 콘텍스트에만 제한하는 것은 불가능하고 종종 바람직하지 않다. 이는 모델의 답변 도출에 액세스하는 정보와 사용자가 평가하는 데 사용 가능한 정보간의 불일치를 야기한다.
    2. 본 연구에서는 사용자가 예측을 평가하기에 충분한 정보가 없는 상황에서 QA 시스템과 상호작용하는 방법을 연구하며, 필요한 백그라운드를 추가하면 사용자들이 예측에 과도하게 의존하는 것을 완화시킬 수 있는지 알아보고자 한다.
    3. 우리의 연구는 사용자들이 모델의 정확성을 평가하기에 충분한 정보가 없는 경우에도 모델 예측에 의존한다는 것을 밝혀냈다. 하지만 관련 백그라운드를 제공하는 것은 사용자가 모델의 오류를 더 잘 파악하고 잘못된 예측에 대한 과도한 의존성을 줄이는 데 도움이 된다.

###### GROOViST: A Metric for Grounding Objects in Visual Storytelling (https://aclanthology.org/2023.emnlp-main.202/)
- Anthology ID: 2023.emnlp-main.202 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 시각적인 이야기에 대한 평가는 일관성, 문법적 정확성, 그리고 시각적인 연결성 등 다양한 측면을 고려해야 한다. 
    2. 문제점이 있는 기존 메트릭들을 분석한 결과, 우리는 cross-modal dependencies, temporal misalignment, 그리고 시각적인 연결성에 대한 인간의 직관을 고려한 새로운 평가 도구인 GROOViST를 제안한다. 
    3. GROOViST는 각 구성 요소의 기여도를 개별적으로 평가하고 해석할 수 있는 모듈식 설계의 장점을 갖고 있다.

###### VIBE: Topic-Driven Temporal Adaptation for Twitter Classification (https://aclanthology.org/2023.emnlp-main.203/)
- Anthology ID: 2023.emnlp-main.203 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실세계 소셜 미디어에서 언어 특성이 계속 변화함에 따라 동적인 텍스트 분류의 성능이 저하되고 있다. 이 논문에서는 시간적 적응을 연구하여 과거 데이터에 기반한 모델을 미래에서 테스트하는 방법을 제안한다. 
    2. 기존의 연구는 계속된 사전학습이나 지식 갱신에 초점을 맞추었으나 이는 소셜 미디어 데이터에서의 성능을 저하시킬 수 있다. 따라서 본 논문에서는 잠재 주제 변화를 모델링하여 특징 변화를 반영하는 방법을 제안한다.
    3. 실험 결과, VIBE 모델은 3%의 데이터만을 사용해 이전의 최신 기법들보다 훨씬 우수한 성능을 보였다.

###### TOD-Flow: Modeling the Structure of Task-Oriented Dialogues (https://aclanthology.org/2023.emnlp-main.204/)
- Anthology ID: 2023.emnlp-main.204 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 사전 훈련된 언어 모델 (pre-trained language model; PLM)을 사용한 대화 시스템이 중요한 요소로 사용되고 있지만, 투명성과 조절 가능성에 제한이 있다. 
    2. 이 논문에서는 대화 흐름 그래프를 추론하여 그래프 형태로 대화 데이터를 주석으로 어노테이션하고, 시스템이 예측을 할 때 예측 성능, 투명성 및 조절 가능성을 향상시키기 위해 대화 모델에 바로 통합할 수 있는 TOD-flow 그래프를 제안한다.
    3. 실험에서 이 방법이 사람이 주석을 단 그래프와 더 유사하게 추론되었으며, MultiWOZ와 SGD 벤치마크에서 대화 행위 분류 및 end-to-end 응답 생성 성능이 크게 향상되었다는 것을 보여준다.

###### TopWORDS-Poetry: Simultaneous Text Segmentation and Word Discovery for Classical Chinese Poetry via Bayesian Inference (https://aclanthology.org/2023.emnlp-main.205/)
- Anthology ID: 2023.emnlp-main.205 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 고전 중국 시에는 일반 중국어 텍스트에 흔히 나오지 않는 특수한 단어가 자주 사용되기 때문에, 자연어 처리에 큰 어려움이 있다. 
    2. 이 연구는 사전이나 훈련 말뭉치 없이도 고전 중국 시의 신뢰할 수 있는 텍스트 구분과 단어 발견을 동시에 수행할 수 있는 비지도 학습 방법인 TopWORDS-Poetry를 제안한다. 
    3. 실험 결과는 TopWORDS-Poetry가 Complete Tang Poetry의 고정 시에 존재하는 고유한 시어(이름 있는 단체와 문학적 언급 등)를 성공적으로 인식하고 의미 있는 단어로 나눌 수 있다는 것을 확인한다.

###### Knowledge Rumination for Pre-trained Language Models (https://aclanthology.org/2023.emnlp-main.206/)
- Anthology ID: 2023.emnlp-main.206 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 사전 훈련된 언어 모델(PLM)은 지식 집약적인 NLP 태스크를 처리하는 능력이 부족하다는 것이 밝혀져 왔으며, 몇 가지 연구에서는 외부 지식을 PLM에 통합하는 시도를 하였다. 
    2. 그러나, 유망한 결과를 보이더라도, PLM은 이미 사전 훈련된 매개변수에 풍부한 지식을 인코딩하고 있음에도 불구하고, 지식 집약적인 태스크에 적용할 때 그것을 충분히 활용하지 못한다는 것을 경험적으로 관측하였다. 
    3. 이 논문에서는 PLM이 외부 말뭉치에서 다시 검색하지 않고도 관련된 잠재적 지식을 활용하도록 돕기 위해 "내가 아는 한"과 같은 프롬프트를 PLM에 추가하는 새로운 패러다임인 "Knowledge Rumination"을 제안하고 있다.

###### Struct-XLM: A Structure Discovery Multilingual Language Model for Enhancing Cross-lingual Transfer through Reinforcement Learning (https://aclanthology.org/2023.emnlp-main.207/)
- Anthology ID: 2023.emnlp-main.207 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "크로스-언어 전이 학습은 잘 맞춰진 크로스-언어 표현에 많이 의존하는데, 문법 구조는 크로스-언어 전이에 유리하다고 알려져 있지만, 다국어 사전 훈련 언어 모델에서는 이를 활용한 연구가 제한적이다."
    2. "우리는 이러한 문제를 해결하기 위해 Sturct-XLM이라고 불리는 새로운 다국어 언어 모델을 제안한다. 이 모델은 강화학습을 활용하여 PLM의 크로스-언어 표현 정렬을 개선하기 위해 범용 문법 구조를 자동으로 발견하는 기능을 가지고 있다."
    3. "실험 결과, 우리의 접근법은 XTREME 벤치마크에서 다국어 PLM의 크로스-언어 전이를 향상시키는데 효과적임을 보여주었다."

###### AdaSent: Efficient Domain-Adapted Sentence Embeddings for Few-Shot Classification (https://aclanthology.org/2023.emnlp-main.208/)
- Anthology ID: 2023.emnlp-main.208 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 연구에서는 사전 학습된 Sentence Encoders (SEs)를 기반으로 한 몇 개의 데이터만을 가지고 문장 분류를 효과적으로 수행하는 것이 효율적이고 강건한 것으로 나타났다. 
    2. 이 연구에서는 몇 개의 데이터만 가지고도 효과적으로 도메인에 특화된 문장 분류를 수행하기 위한 전략을 조사한다.
    3. 기존의 SEs에 DAPT(Domain-Adaptive Pre-Training)을 적용하는 것은 효과적이지만 비효율적이므로, AdaSent라는 방법을 제안한다. AdaSent는 SE를 위해 DAPT-ed PLMs에 SEPT(Sentence Embedding Pre-Training) 어댑터를 추가하여 training cost를 크게 감소시키면서도 성능을 유지한다.

###### Interview Evaluation: A Novel Approach for Automatic Evaluation of Conversational Question Answering Models (https://aclanthology.org/2023.emnlp-main.209/)
- Anthology ID: 2023.emnlp-main.209 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화형 질문 답변(CQA)은 정보 검색 대화에서 사용자에게 자연어 답변을 제공하는 것을 목표로 한다. 기존의 CQA 벤치마크들은 전처리된 사람-사람 대화를 사용하여 모델을 평가한다.
    2. 하지만 모델이 예측한 대화 내용을 정답으로 대체하는 것은 CQA 평가의 자연성과 지속 가능성을 떨어뜨린다.
    3. 이 논문에서는 대화형 평가 방식으로 인터뷰 평가라는 새로운 자동 평가 방법을 제안한다. 이 방법은 ChatGPT가 인터뷰어(Q agent) 역할을 하고 CQA 모델이 인터뷰이(A agent) 역할을 한다.

###### TCFLE-8: a Corpus of Learner Written Productions for French as a Foreign Language and its Application to Automated Essay Scoring (https://aclanthology.org/2023.emnlp-main.210/)
- Anthology ID: 2023.emnlp-main.210 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 에세이 채점(Automated Essay Scoring, AES)은 에세이의 품질을 자동으로 평가하는 것을 목표로 한다. AES를 통해 규모 있는 채점, 일관성, 신뢰성, 표준화의 개선이 가능하다. 하지만 AES 시스템 개발의 주요 병목은 코퍼스의 부족이다.
    2. 이 논문에서는 TCFL-8 코퍼스를 제공함으로써 AES를 프랑스어에 적용하는 것을 촉진하고자 한다. 이를 위해 6.5k개의 에세이를 수집하고, CEFR 수준에 따라 최소한 두 명의 채점자가 각 에세이를 채점하고 균형 있는 코퍼스를 작성하는 엄격한 절차를 보고한다.
    3. 또한, 에세이의 언어적 특성과 학습자의 능력과의 관련성, 그리고 RoBERTa와 feature 기반의 두 가지 강력한 베이스라인을 실험하여 프랑스어 AES 작업의 최신 기술 결과를 제시한다. 마지막으로, TCFL-8을 사용한 AES의 도전과제에 대해서 논의한다.

###### Dancing Between Success and Failure: Edit-level Simplification Evaluation using SALSA (https://aclanthology.org/2023.emnlp-main.211/)
- Anthology ID: 2023.emnlp-main.211 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(GPT-4)은 높은 텍스트 간소화 품질을 제공할 수 있으나, 기존의 인간 평가 방법은 시스템의 특정 강점과 약점을 명확히 제시할 수 없는 한계가 있다.
    2. 이를 극복하기 위해, 우리는 일관성 있고 상세한 텍스트 간소화 평가를 가능하게 하는 수정 기반 인간 주석 툴인 SALSA를 소개한다.
    3. 우리는 SALSA를 사용하여 840개의 간소화 문장에 대해 19,000개의 수정 주석을 수집하였고, 하이퍼 파라미터 튜닝된 모델, LLM 및 인간 간소화 전략의 분포에서 차이를 밝혀내었으며, GPT-3.5는 인간보다 더 품질 좋은 수정을 수행하지만 여전히 빈번한 오류를 보여준다.

###### Confidence-based Ensembling of Perspective-aware Models (https://aclanthology.org/2023.emnlp-main.212/)
- Anthology ID: 2023.emnlp-main.212 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 NLP 연구는 어노테이션 작업을 수행할 때 사람들이 라벨을 선택하는데 보여주는 변동성에 집중하고 있다. 어노테이션에서의 의견의 불일치를 활용하면 정확한 모델링과 공정한 평가에 이점이 있다는 것이 입증되었다.
    2. 이 논문에서는 자연어 문장의 지도 분류를 위한 강한 퍼스펙티비스트(perspectivist) 모델을 제안한다. 접근 방식은 플러 학습된 모델의 예측을 결합하여 언어 현상의 어노테이션에 인코딩된 주관성을 포착하기 위해 각 모델의 개별 신뢰도 관련 정보를 사용한다.
    3. 실험 결과는 (1) 아이러니와 혐오 발언 감지 두 가지 케이스 스터디에서, (2) 인도메인 및 크로스 도메인 설정에서 신뢰도 기반의 퍼스펙티비스트 모델의 앙상블이 모든 시나리오에서 분류 성능에 유리하다는 것을 보여준다. 또한, 어노테이터 메타데이터를 사용할 수 없을 때 어노테이션으로부터 자동으로 추출된 퍼스펙티브의 효과적인지도 데모를 제시한다.

###### ToViLaG: Your Visual-Language Generative Model is Also An Evildoer (https://aclanthology.org/2023.emnlp-main.213/)
- Anthology ID: 2023.emnlp-main.213 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대형 비주얼-언어 생성 모델은 이미지/텍스트 생성에서 과거에 없었던 큰 발전을 이루었지만, 이러한 모델들은 독성 콘텐츠, 예를 들어 모욕적인 텍스트나 음란한 이미지를 생성할 수도 있어 윤리적인 위험성을 제기하고 있다. 
    2. 이 연구는 시각-언어 생성에서 독성 생성의 경향성과 독성 데이터에 대한 감수성을 다양한 VLGMs 상에서 탐색한다. 
    3. 우리는 시각-언어 생성에 맞춤화된 독성 메트릭인 WInToRe를 제안하고, 다양한 VLGMs의 독성을 평가하여 일부 모델들이 기대 이상의 독성을 가지고 있다는 사실을 발견하였으며, 독성 제거가 필요하다는 점을 강조한다.

###### GPT-RE: In-context Learning for Relation Extraction using Large Language Models (https://aclanthology.org/2023.emnlp-main.214/)
- Anthology ID: 2023.emnlp-main.214 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델(Large Language Models, LLM)은 in-context learning (ICL)을 통해 혁신적인 성과를 낼 수 있지만, 관계 추출 (RE)에서는 fully-supervised 기준에 비해 큰 차이가 난다. 
    2. 이 논문에서는 task-aware한 representation을 사용하여 ICL의 entity와 relation에 대한 관련성을 높이고, 골드 라벨로 유도된 추론 로직을 포함시켜 RE 작업을 수행하는 GPT-RE를 제안한다. 
    3. GPT-RE는 Semeval과 SciERC 데이터셋에서 SOTA 결과를 얻으며, TACRED와 ACE05 데이터셋에서도 경쟁력 있는 결과를 보여준다. 또한, NULL 예제를 잘못 분류하는 문제도 GPT-RE를 통해 상당히 완화되었다.

###### Sociocultural Norm Similarities and Differences via Situational Alignment and Explainable Textual Entailment (https://aclanthology.org/2023.emnlp-main.215/)
- Anthology ID: 2023.emnlp-main.215 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문화 간 추론을 할 수 있는 시스템을 개발하기 위해서는 해당 문화의 표준에 기반을 둬야 한다. 하지만 현재 사회 규범의 컴퓨터 모델에 대한 연구는 주로 미국 사회에 초점을 맞추고 있다. 
    2. 이 논문은 중국문화와 미국문화 간에 기술적, 문화적 차이를 발견하고 비교하기 위해 중국의 Q&A 플랫폼과 SocialChemistry 데이터셋을 활용한 새로운 접근 방식을 제안한다. 
    3. 반응적 학습을 통해 텍스트에서 사회규범을 추출하고 중국문화와 미국문화 간의 사회규범을 비교하는 높은 품질의 데이터셋을 구축하였다. 이 데이터셋을 활용하여 문화 간 사회규범 추론의 성능을 평가하고, 이를 토대로 문화 간 규범의 차이를 분석하였다.

###### INFORM : Information eNtropy based multi-step reasoning FOR large language Models (https://aclanthology.org/2023.emnlp-main.216/)
- Anthology ID: 2023.emnlp-main.216 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "큰 언어 모델들은 공들여 만든 Chain-of-Thought (CoT) 프롬프트로 추론 태스크에서 뛰어난 성능을 보여주었다. 하지만, CoT 프롬프트의 효과는 다른 인-컨텍스트 예제의 선택에 따라 크게 변동할 수 있다. 또한, 사람이 루트 스텝을 수동으로 작성하는 것은 시간이 많이 소요되어 CoT 프롬프트의 보급에 어려움을 겪고 있다." 
    2. "이 논문에서는 정보 엔트로피를 CoT 프롬프트 선택 기준으로 도입하는 새로운 방법을 제안한다. 정보 엔트로피 점수가 더 높은 CoT 프롬프트를 자동으로 생성하고 적절한 샘플의 개수를 적응적으로 결정하는 방법을 소개한다. 이 세 단계를 통합한 우리의 제안된 INFORM 방법은 GPT-3.5-Turbo 및 text-davinci-003 이라는 두 가지 언어 모델을 사용하여 일곱 가지 추론 벤치마크에서 실험을 진행하였는데, 이 실험에서 INFORM이 성능과 효율성 측면에서 우수함을 입증하였다."
    3. "INFORM은 제안된 정보 엔트로피 기반의 다단계 추론 방법으로서, CoT 프롬프트 생성, CoT 프롬프트 선택, 추론 세 가지 단계에서 각각 정보 엔트로피를 활용하여 큰 언어 모델의 추론 성능을 향상시키는 접근 방법이다."

###### Adaptive Gating in Mixture-of-Experts based Language Models (https://aclanthology.org/2023.emnlp-main.217/)
- Anthology ID: 2023.emnlp-main.217 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다양한 NLP 태스크에서 대형 언어 모델들은 탁월한 언어 이해 능력을 보여주고 있다. 그러나 기존의 MoE (mixture-of-experts) 모델은 고정된 게이팅 네트워크를 채택하고 있어 각 토큰이 동일한 수의 전문가들에 의해 계산된다. 이는 각 시퀀스의 토큰들이 언어적 복잡성과 관련하여 다른 계산 비용을 필요로 한다는 직관과 상반된다.
    2. 이 논문은 MoE에 적응형 게이팅을 도입하여 각 토큰이 전문가의 확률 분포에 따라 가변적인 수의 전문가에 의해 처리될 수 있는 유연한 훈련 전략을 제안한다. 적응형 게이팅은 희소성을 보존하면서 훈련 효율성을 개선한다.
    3. 실험 결과 적응형 게이팅은 최대 22.5%의 훈련 시간을 단축시키면서 추론 품질을 유지한다는 것을 보여주며, 게이팅 결정에 대한 포괄적인 분석을 통해 특정 언어 작업에 어려운 토큰들을 파악한다.

###### On the Automatic Generation and Simplification of Children’s Stories (https://aclanthology.org/2023.emnlp-main.218/)
- Anthology ID: 2023.emnlp-main.218 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대형 언어 모델 (LLMs)의 발전으로 인해 어린이 교육 자료를 자동으로 생성하는 개념이 점점 현실적으로 이루어지고 있다. 
    2. 이 연구에서는 어린이를 대상으로 한 텍스트의 어휘와 가독성 수준을 적절하게 조절하여 이야기를 생성할 수 있는 인기있는 LLM들의 능력을 조사한다.
    3. 그러나 LLM들은 아직 어린이 연령대에 적합한 어휘를 제한할 수 있는 능력이 없으며, 현재 가장 좋은 성능을 보이는 어휘 단순화 모델들도 LLM에 의존하는 한계 때문에 어린이를 대상으로 한 자료에서 좋은 성능을 내지 못한다는 것을 발견했다.

###### When Do Decompositions Help for Machine Reading? (https://aclanthology.org/2023.emnlp-main.219/)
- Anthology ID: 2023.emnlp-main.219 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 복잡한 질문에 대답하기 위해서는 보통 다단계 추론이 필요하지만, 기계 독해모델에서 복잡한 질문을 분해하는 연구는 미흡한 상태이다.
    2. 우리는 머신 독해모델에서 분해가 언제 유용한지를 이해하기 위해 다양한 모델과 데이터셋을 사용하여 실험을 진행하였다. 
    3. 우리는 분해가 적은 데이터셋에서는 정확도를 향상시킬 수 있음을 발견하였으나, 수백개 이상의 예제를 가지고 있는 경우에는 분해가 도움이 되지 않을 수 있다는 것을 보였다.

###### The Curious Case of Hallucinatory (Un)answerability: Finding Truths in the Hidden States of Over-Confident Large Language Models (https://aclanthology.org/2023.emnlp-main.220/)
- Anthology ID: 2023.emnlp-main.220 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large language models)은 놀라운 성능을 보여주지만, 그들의 응답의 신뢰성에 대한 우려가 제기되고 있다. 이 연구는 (불)가능한 질의문에 대한 LLM의 행동을 탐색한다. 
    2. 연구 결과는 모델이 창작된 답을 생성할 때 질문이 (불)가능한지를 반영한다는 강한 증거를 보여준다. 특히, 첫 번째 디코딩 토큰의 표현은 강한 지표이다. 
    3. 이러한 발견은 LLM의 잠재적 표현 내에서의 공간적 구성에 대해 새로운 시각을 제공하며, 질의문 (불)가능성이 관련된 경우 사실적 생성에 더 잘 따르는 개선된 디코딩 기법의 개발을 위한 기반이 된다.

###### Identifying Informational Sources in News Articles (https://aclanthology.org/2023.emnlp-main.221/)
- Anthology ID: 2023.emnlp-main.221 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 뉴스 기사는 기자들이 보도에 사용한 정보 소스에 의해 주도된다. 이 논문에서는 이러한 소스가 언제, 어떻게, 왜 함께 사용되는지 모델링함으로써 우리가 소비하는 정보를 더 잘 이해하고 기사를 작성하는 기자들에게 도움을 줄 수 있다고 주장한다.
    2. 이 논문에서는 정보 검출과 소스 어트리뷰션을 위해 사용된 최대 및 가장 폭넓은 주석이 달린 데이터셋을 만들었음을 보여준다. 이 데이터셋을 사용하여 다양한 소스가 뉴스 기사에서 어떻게 선택되어 함께 사용되는지 조사하는 새로운 작업인 소스 예측을 제안한다.
    3. 이 작업에서 모델은 소스들이 뉴스 스토리텔링에서 어떻게 함께 사용되는지에 대한 패턴이 있다는 것을 보여주며, 이를 통해 이후에는 서술 기반 언어 생성을 위한 소스에 중점을 두고 연구하는 것과 정보를 돕기 위한 소스 추천 시스템을 포함한 컴퓨터 기반 기자학 연구에 집중할 수 있다.

###### Retrofitting Light-weight Language Models for Emotions using Supervised Contrastive Learning (https://aclanthology.org/2023.emnlp-main.222/)
- Anthology ID: 2023.emnlp-main.222 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 BERT와 RoBERTa와 같은 사전 훈련된 언어모델에 감정 측면을 도입하기 위한 새로운 retrofitting 방법을 제안한다. 
    2. 이 방법은 비슷한 감정을 나타내는 텍스트 조각들이 표현 공간에서 가까이 인코딩되고, 다른 감정을 가진 조각들은 멀리 떨어지도록 사전 훈련된 네트워크 가중치를 업데이트한다. 
    3. 이렇게 하면 PLM에 이미 존재하는 언어적 지식이 의도치 않게 변하지 않도록 보장하며, 감정을 인식할 수 있는 텍스트 표현을 생성한다. 이 retrofitting 방법을 사용한 모델은 다양한 클러스터링 및 검색 메트릭을 통해 평가되었을 때 감정을 인지할 수 있는 텍스트 표현을 생성하며, 감정 분석과 풍자 감지와 같은 다운스트림 태스크에서 사전 훈련된 모델 대비 약 1%의 개선 in F1-score를 보인다. 특히, 이미지 어록 학습 환경에서 retrofitting 된 모델의 성능 향상이 사전 훈련된 모델 대비로 더 크게 나타난다.

###### Longtriever: a Pre-trained Long Text Encoder for Dense Document Retrieval (https://aclanthology.org/2023.emnlp-main.223/)
- Anthology ID: 2023.emnlp-main.223 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 훈련된 언어 모델(PLM) 기반의 집약된 검색은 내재적 의미를 모델링할 때 강력한 성능을 보이지만, 기존의 모델은 계산 비용이 많이든다는 문제가 있다.
    2. 이 논문에서는 'Longtriever'라는 새로운 검색 모델을 소개하며, 장문 문서 검색의 핵심적인 문제들인 계산 비용, 불완전한 문서 이해, 희귀한 어노테이션에 대응한다.
    3. Longtriever는 장문 문서를 짧은 블록으로 나눈 뒤, 블록 내 지역적 의미와 블록 간 전역적 문맥 의미를 밀접하게 모델링하여 효율적으로 처리한다. 또한 사전 훈련 단계를 도입하여 기저 의미 상관관계를 더욱 잘 이해할 수 있다는 결과를 실험을 통해 입증하였다.

###### Revisiting De-Identification of Electronic Medical Records: Evaluation of Within- and Cross-Hospital Generalization (https://aclanthology.org/2023.emnlp-main.224/)
- Anthology ID: 2023.emnlp-main.224 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 익명화 작업은 전자 의료 기록에서 보호되어야 할 정보를 감지하고 제거하는 작업을 말하는데, 이전 연구들은 일반적으로 병원 내 환경에 초점을 맞추고 있고 큰 성과를 거두었지만, 병원 간 환경을 간과하고 있다. 
    2. 본 논문은 중국의 세 병원에서 가져온 EMR로 이루어진 새로운 익명화 데이터셋을 소개하고 병원 내 및 병원 간 일반화를 평가하는 기준을 마련하였다. 
    3. 병원 간에는 상당한 도메인 차이가 있으며, 거의 완벽한 성능을 가진 모델도 병원 간 이식에서 어려움을 겪는다. 사전 훈련된 언어 모델과 일부 도메인 일반화 방법을 사용하면 이 문제를 완화시킬 수 있다는 실험 결과도 제시되었다.

###### Small Language Models Fine-tuned to Coordinate Larger Language Models improve Complex Reasoning (https://aclanthology.org/2023.emnlp-main.225/)
- Anthology ID: 2023.emnlp-main.225 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대형 언어 모델들은 chain-of-thought (CoT) 생성에서 뛰어난 추론 능력을 보여주지만, 복잡한 다단계 추론 문제를 해결하기 위한 prompt 분해는 이러한 모델이 동시에 분해와 해결을 할 수 있는 능력에 의존한다.
    2. 우리는 기존의 대형 언어 모델들은 fine-tuning할 수 없기 때문에 변형이 어렵다고 보며, 문제 분해와 해결 생성은 하나의 대형 언어 모델로 처리하는 것보다 각각 별도의 모듈로 다루는 것이 더 나은 방법이라고 주장한다.
    3. 우리는 DaSLaM이라는 모델을 소개하는데, 이 모델은 분해 생성 모듈을 사용하여 복잡한 문제를 작은 하위 문제로 분해하고, 해결자 모듈을 사용하여 이 하위 문제에 대한 답을 구한다. 이때 우리는 상대적으로 작은 규모의 언어 모델을 분해 생성기로 사용하여 성능을 향상시키고, 해결자 모델과 상호 작용하면서 하위 문제를 안내한다. 이로써 우리의 방법은 어떤 해결자 모델에도 적용 가능하다는 것을 보여준다.

###### Language Representation Projection: Can We Transfer Factual Knowledge across Languages in Multilingual Language Models? (https://aclanthology.org/2023.emnlp-main.226/)
- Anthology ID: 2023.emnlp-main.226 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 사전학습 언어 모델은 사실 기반의 다국어지식 저장소 역할을 한다. 그러나 리소스가 풍부한 언어와 리소스가 제한된 언어 사이에는 실질적인 지식 이전에 큰 성능 차이가 존재하며, 다국어 사전학습 언어 모델에서의 언어 간 암묵적인 실제 지식 전달이 제한되었음을 시사한다. 
    2. 본 논문에서는 상대적으로 풍부한 실제 지식을 영어에서 다른 언어로 명시적으로 전달하는 것의 실현 가능성을 연구한다. 이를 위해, 두 개의 기본 파라미터 없는 언어 표현 전사 모듈(LRP2)을 제안한다. 첫 번째 모듈은 다른 언어의 표현을 영어와 유사한 표현으로 변환하고, 두 번째 모듈은 영어와 유사한 표현을 해당 다른 언어의 표현으로 되돌린다. 
    3. mLAMA 데이터셋에서의 실험결과는 LRP2가 실제 지식 검색의 정확도를 크게 향상시키고, 다양한 다른 언어 간의 지식 이전을 용이하게 하는 것을 보여준다. 또한 LRP2의 작동 메커니즘을 표현 공간과 언어 간 지식 뉴런으로부터 규명한다.

###### Structural Priming Demonstrates Abstract Grammatical Representations in Multilingual Language Models (https://aclanthology.org/2023.emnlp-main.227/)
- Anthology ID: 2023.emnlp-main.227 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델들은 인간과 유사하게 동작하여, 인간의 언어 구조 대단위에서의 형태소 특징 및 문법 패턴을 인식할 수 있다는 것을 보여준다.
    2. 그러므로, 크로스리규얼 구조 준비 실험을 사용하여 다국어 언어 모델에서 언어 구조 표상을 측정하고 인간의 행동 결과와 비교한다.
    3. 이 연구 결과는 다국어 언어 모델의 문법적 표현이 언어 간에 유사하며 서로 다른 언어로 생성된 텍스트에도 영향을 미칠 수 있다는 것을 보여준다.

###### ReasoningLM: Enabling Structural Subgraph Reasoning in Pre-trained Language Models for Question Answering over Knowledge Graph (https://aclanthology.org/2023.emnlp-main.228/)
- Anthology ID: 2023.emnlp-main.228 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Knowledge Graph Question Answering (KGQA)은 대규모 지식 그래프에서 자연어 질문에 대한 답을 찾는 것을 목표로 한다. 전통적인 방법에서는 pre-trained language model (PLM)과 graph neural network (GNN)을 따로 사용하여 모델링하였다. 그러나 PLM과 GNN은 구조적인 처리나 특징 상호작용에 있어서 직접적인 연동이 없어서 정보 공유가 제한되었다. 
    2. 우리는 위 두 모듈 접근 방식을 단순화하고 KGQA에 직접적인 서브그래프 추론을 지원하는 더 강력한 PLM인 ReasoningLM을 개발하기 위해 노력했다.
    3. 우리의 실험 결과, ReasoningLM은 Parameter의 수가 적고 학습 데이터가 줄어들더라도 기존 모델을 큰 폭으로 앞질러 나감을 보여주었다.

###### Deep Natural Language Feature Learning for Interpretable Prediction (https://aclanthology.org/2023.emnlp-main.229/)
- Anthology ID: 2023.emnlp-main.229 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구에서는 주요 복잡한 작업을 중간 단계의 더 쉬운 하위 작업 집합으로 나누는 일반적인 방법을 제안한다. 이 하위 작업은 최종 목표 작업과 관련된 바이너리 질문으로 자연어로 포뮬레이션된다.
    2. 우리의 방법은 이러한 질문에 대한 답변으로 각 예시를 나타내는 벡터로 표현 가능하게 한다. 우리는 이 표현을 "Natural Language Learned Features (NLLF)"라고 부른다.
    3. NLLF 벡터는 이진 질문에 대한 zero-shot inference를 다룰 수 있는 능력을 가지며, 어떠한 훈련 과정에서든 사용될 수 있다. 이 벡터는 분류기의 성능을 향상시키는 데 도움이 되는데, 또한 의사 결정 트리와 같은 해석하기 쉬운 기계 학습 모델의 입력으로 사용될 수 있다.

###### ROBBIE: Robust Bias Evaluation of Large Generative Language Models (https://aclanthology.org/2023.emnlp-main.230/)
- Anthology ID: 2023.emnlp-main.230 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지금은 LLMs의 공정성을 측정하고 개선하기 위해 충분한 도구를 개발해야 할 때이다. 이 논문에서는 다양한 프롬프트 기반 데이터셋을 사용하여 텍스트 도메인과 인구 특성 축을 통해 사회적 편향성을 측정하는데 초점을 맞추었다. 또한, LLMs을 다양한 데이터셋에서 테스트하는 것은 편향성을 더욱 완전하게 파악하고, 사회적으로 소외된 인구 그룹들에게 공정한 대우를 보장하기 위해 도움이 될 수 있다.
    2. 이 논문은 6가지 다른 프롬프트 기반 편향 및 독성 메트릭을 12개의 인구 특성 축과 5개의 LLMs 패밀리에 걸쳐 비교하는 벤치마킹 분석을 수행한다. 또한, 비교 벤치마크를 통해 모델의 편향성과 독성에 대한 통찰력을 얻을 수 있다. 이를 통해 LLMs의 사전 훈련 말뭉치에서 인구 특성 용어의 빈도에 대해 조사하고, 이것이 모델의 편향과 관련이 있는지 알아본다.
    3. 또한, 이 논문은 3가지 편향/독성 완화 기술의 성능을 측정하여 평가했다. ROBBIE는 모델 배포 시 실무자에게 인사이트를 제공하고, 잠재적인 피해를 측정하는 것뿐만 아니라 피해가 어떻게 발생하는지 이해하기 위해 데이터를 특성화하고, 발견된 피해를 완화하고, 어떤 편중점을 조정해야 하는지를 강조한다. 또한, 향후 LLMs에서 편향을 보다 폭넓게 측정하도록 동기부여하기 위해 분석 코드를 공개하였다.

###### Enhancing Task-oriented Dialogue Systems with Generative Post-processing Networks (https://aclanthology.org/2023.emnlp-main.231/)
- Anthology ID: 2023.emnlp-main.231 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 태스크 지향형 대화 시스템에서 비미분 가능한 모듈까지 포함하여 임의의 모듈의 출력을 수정하는 후 처리 네트워크(PPN)가 제안되었습니다. 
    2. PPN은 NLU, DST, Policy 모듈을 분류 기반 접근법으로 후 처리하여 대화 성능을 성공적으로 개선하였으나, NLG 모듈에는 적용할 수 없습니다.  
    3. 따라서 우리는 dialogue act contribution이라는 새로운 척도를 사용하여 GenPPN에서 NLG에 대한 후 처리 구성 요소를 제안하고, RL을 통해 GenPPN을 최적화합니다. 이를 통해 MultiWOZ 데이터셋을 기반으로 한 시뮬레이션 및 인간 평가 실험을 통해 GenPPN이 태스크 완료 성능을 향상시킨다는 것을 확인하였습니다.

###### Adapting Language Models to Compress Contexts (https://aclanthology.org/2023.emnlp-main.232/)
- Anthology ID: 2023.emnlp-main.232 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformer 기반 언어 모델은 강력하고 다양한 분야에 적용 가능한 도구이지만, 유한한 문맥 창과 긴 텍스트 문서 처리의 계산 비용 때문에 제약이 있다.
    2. 이 논문에서는 사전 훈련된 언어 모델을 AutoCompressors로 적용하여, 긴 문맥을 요약 벡터로 압축하고 모델이 이 벡터를 소프트 프롬프트로 활용하는 방법을 제안한다.
    3. AutoCompressors는 긴 문장 처리에 대한 perplexity 향상과 함께 정확도를 높이고 추론 비용을 줄이는 효과를 보여주며, LMs의 문맥 창을 확장하는 간단하고 경제적인 해결책으로 등장한다.

###### Selective Labeling: How to Radically Lower Data-Labeling Costs for Document Extraction Models (https://aclanthology.org/2023.emnlp-main.233/)
- Anthology ID: 2023.emnlp-main.233 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인보이스, 영수증, 계산서, 세금 양식 등과 같은 시각적으로 풍부한 문서에 대한 자동 추출 모델을 구축하는 것은 최근에 상당한 관심을 받고 있다. 그러나 새로운 문서 유형의 추출 모델을 개발하는 주요 병목은 학습에 필요한 여러 천 개의 고품질 레이블이 지정된 문서를 구하기 위한 비용이다. 이 논문에서는 이 문제에 대한 해결책으로 선택적 레이블링을 제안한다.
    2. 선택적 레이블링은 부분적으로 레이블이 지정된 문서로 학습한 모델이 예측한 후보 추출물에 대해 "예/아니오" 레이블을 제공하는 것으로 레이블링 작업을 간소화하는 것을 주요 아이디어로 한다.
    3. 실험 결과, 선택적 레이블링은 10배 정도의 레이블링 데이터 구입 비용 절감과 무시할 수 있는 정확도 감소를 보이는 것으로 나타났다. (active learning)

###### TRAVEL: Tag-Aware Conversational FAQ Retrieval via Reinforcement Learning (https://aclanthology.org/2023.emnlp-main.234/)
- Anthology ID: 2023.emnlp-main.234 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인 고객 서비스에서 사용자의 의도와 일치하는 FAQ 질문을 효율적으로 검색하는 것은 중요하다. 
    2. 기존의 방법들은 동적인 대화 문맥을 활용하여 사용자의 질문과 FAQ 질문의 의미 연관성을 향상시키려고 하지만, 대화 문맥에는 잡음이 존재하여 정확한 의미 모델링이 어려워진다. 
    3. 따라서 이 연구에서는 FAQ 질문의 태그를 도입하여 관련 없는 정보를 제거하고, 강화학습 프레임워크에 통합하여 동적인 대화 문맥에서 관련 없는 정보의 부정적인 영향을 최소화한다.

###### Continual Dialogue State Tracking via Example-Guided Question Answering (https://aclanthology.org/2023.emnlp-main.235/)
- Anthology ID: 2023.emnlp-main.235 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 시스템은 자주 새로운 서비스에 맞추어 업데이트되지만, 이전에 학습한 서비스의 성능을 저하시키는 문제가 있다. 
    2. 이 논문에서는 대화 상태 추적(DST)을 단순한 자연어 이해 작업으로 구성하고, 서비스 간의 작업 변경을 최소화하기 위해 예시를 기반으로 하는 질문-답변 작업을 제안한다. 
    3. 제안한 방법은 서비스별로 특정 정보를 기억하는 것을 완화하고, 대화에서 필요한 정보를 추출하기 위해 주어진 질문과 예시를 문맥화하여 학습하는 경량 모델을 제안한다.

###### Lost in Translation, Found in Spans: Identifying Claims in Multilingual Social Media (https://aclanthology.org/2023.emnlp-main.236/)
- Anthology ID: 2023.emnlp-main.236 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. CSI (Claim span identification)는 사회적 미디어 게시물에서 검증할 가치가 있는 주장이나 어설션을 포함하는 텍스트 부분을 식별하는 중요한 단계이다. 
    2. 우리는 CSI를 위한 새로운 데이터셋 X-CLAIM을 생성하여 여러 인도어 언어와 영어로 구성되어 있음을 보여준다. 
    3. 우리는 state-of-the-art 언어 모델(XLM-R)을 사용하여 강력한 기준 성능을 보여주고, 저자원 언어인 영어로부터의 제로샷 전송 또는 번역된 데이터로 훈련하는 대안적 크로스-언어 전이 방법에 비해 여러 언어로 훈련하는 것의 장점을 보인다.

###### COVID-19 Vaccine Misinformation in Middle Income Countries (https://aclanthology.org/2023.emnlp-main.237/)
- Anthology ID: 2023.emnlp-main.237 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "이 논문은 COVID-19 백신에 대한 잘못된 정보를 가진 다국어 데이터셋을 소개하며, 브라질, 인도네시아, 나이지리아에서 수집한 트위터 데이터를 포함한다. 해당 데이터셋은 5,952개의 트윗에 대한 주제, COVID-19 백신과의 관련성, 그리고 잘못된 정보의 유무에 대한 주석을 포함하고 있다."
    2. "도메인 특이성, 데이터 부족, 데이터 불균형과 같은 도전을 해결하기 위해 우리는 COVID-19 백신 잘못된 정보 탐지 모델의 개발을 위해 도메인 특정 사전 훈련과 대규모 언어 모델을 사용한 텍스트 augmentation 두 가지 접근 방식을 채택한다."
    3. "최고의 잘못된 정보 탐지 모델은 기준 모델과 비교하여 macro F1-score에서 2.7에서 15.9 백분율 향상을 보여주며, 이 모델을 사용하여 브라질과 인도네시아의 COVID-19 백신 잘못된 정보율과 새로운 COVID-19 케이스 수의 백분율 변화와 긍정적인 관련성이 있음을 분석 결과로 보여준다."

###### Contrastive Learning of Sentence Embeddings from Scratch (https://aclanthology.org/2023.emnlp-main.238/)
- Anthology ID: 2023.emnlp-main.238 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 학습된 언어 모델을 활용하여 합성 데이터로 문장 임베딩을 학습하는 contrastive learning 방법이 주로 사용되고 있다. 이 연구는 제한된 도메인에서 unlabeled 데이터를 활용하여 contrastive learning을 수행하는 SynCSE라는 새로운 프레임워크를 제안한다.
    2. SynCSE는 unlabeled 데이터에 대해 긍정/부정 어노테이션을 구성하거나 무작위로 문장과 해당 어노테이션을 생성하는 데 활용할 수 있다. 특히, SynCSE는 수동으로 데이터를 수집하지 않고도 문장 임베딩을 학습하는 첫 번째 contrastive learning 방법을 구성한다.
    3. 문장 유사도 및 reranking 작업에서의 실험 결과는 SynCSE-partial 및 SynCSE-scratch가 비지도 기준 모델을 크게 능가하며, SynCSE-partial은 대부분의 setting에서 지도학습 기준 모델과 유사한 성능을 달성한다.

###### A Rose by Any Other Name would not Smell as Sweet: Social Bias in Names Mistranslation (https://aclanthology.org/2023.emnlp-main.239/)
- Anthology ID: 2023.emnlp-main.239 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 기계 번역의 이름에 대한 분야별 차이가 있는지 질문합니다. 우리는 미국의 인종 및 민족 소수자에 관련된 이름의 번역 품질이 전통적인 언어 패턴을 기준으로 표준화하는 기계 번역 시스템의 경향으로 인해 낮을 것이라고 가정합니다. 
    2. 우리는 인구 통계학적으로 관련된 이름의 데이터 세트를 개발하고, 왕복 번역에 기반한 번역 평가 절차를 제안합니다. 
    3. 이름의 인구 통계학적 특성이 번역 품질에 미치는 영향을 분석하여, 여성 관련 이름의 번역을 올바르게 하는 능력이 남성 관련 이름보다 현저히 낮다는 것을 발견했습니다. 이러한 효과는 특히 여성 관련 이름이 인종 (흑인) 및 민족 (히스패닉) 소수자와 관련된 경우에 두드러집니다.

###### Investigating Efficiently Extending Transformers for Long Input Summarization (https://aclanthology.org/2023.emnlp-main.240/)
- Anthology ID: 2023.emnlp-main.240 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 사전학습 모델은 자연어 처리 작업에 매우 능숙하지만, 긴 시퀀스 입력을 처리하는 것은 여전히 큰 도전이다.
    2. 이 논문에서는 긴 입력 요약 작업을 위해 미리 학습된 Transformer 모델을 가장 효율적으로 적용하기 위한 아키텍처 변경과 사전학습 패러다임을 탐구한다.
    3. 그 결과, 전역 인코더 토큰을 가진 단계적인 블록-로컬 Transformer 구조가 성능과 효율성의 균형을 잘 이루며, 긴 시퀀스에 대한 사전학습 단계가 요약 작업 성능을 의미있게 향상시킨다는 것을 발견했다.

###### CS2W: A Chinese Spoken-to-Written Style Conversion Dataset with Multiple Conversion Types (https://aclanthology.org/2023.emnlp-main.241/)
- Anthology ID: 2023.emnlp-main.241 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 음성 텍스트는 비유차와 문법적 오류를 포함하여 하위 태스크에 대한 막대한 과제를 제기한다. 이 문제를 해결하기 위해 우리는 CS2W라는 중국어 음성-문장 변환 데이터셋을 제시한다.
    2. CS2W는 대화 형식의 텍스트에서 추출한 7,237개의 음성 문장을 포함하며, 비유차, 문법적 오류, 음성 인식 오류 및 구어적인 표현을 포함하는 변환 문제를 다룬다.
    3. 우리의 주석 규칙, 데이터 및 코드는 https://github.com/guozishan/CS2W에서 공개적으로 이용 가능하다.

###### Unifying Cross-Lingual Transfer across Scenarios of Resource Scarcity (https://aclanthology.org/2023.emnlp-main.242/)
- Anthology ID: 2023.emnlp-main.242 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 세계의 많은 언어에서 데이터의 부족으로 인해, 다른 정보가 있는 resource-rich 언어로부터 지식을 전이해야 하는 필요가 있다. 그러나 부족한 정도는 다양한 차원에서 크게 달라진다. 
    2. 이 논문에서는 충분한 데이터가 없는 난감한 상황에서 cross-lingual transfer 도구를 사용하는 방법을 연구한다. 
    3. 실험결과, 매우 다국어적인 Transformers의 언어와 작업에 효율적인 매개변수를 사용하는 것이 가장 좋은 구성이며, 기계 번역 및 다양한 대상 언어의 자연어 데이터를 동시에 사용하여 학습시키는 것이 가장 좋은 성능을 보여준다.

###### A Tale of Pronouns: Interpretability Informs Gender Bias Mitigation for Fairer Instruction-Tuned Machine Translation (https://aclanthology.org/2023.emnlp-main.243/)
- Anthology ID: 2023.emnlp-main.243 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 instruction fine-tuned 모델들은 자연어 처리(NLP) 태스크를 여러 개 해결할 수 있지만, 현재의 연구들은 주로 성능 기준에만 초점을 맞추고 공정성과 윤리적 고려사항을 무시한다.
    2. 기계 번역(MT)에서는 성별에 대한 편견과 고정관념을 지속시키는 비성별적인 번역이 생길 수 있다. 이 연구에서는 IFT 모델들이 남성형식의 번역을 선호하는 것을 발견했고, 이를 해결하기 위해 few-shot learning을 이용한 편향 보완 방법을 제안한다.
    3. 발견한 문제에 기반하여 구체적인 해석 가능성 메서드를 사용하여 모델들이 비성별적인 번역에서 대상 직업의 성별을 나타내는 대명사를 무시하는 경향을 발견하였다.

###### DisCo: Distilled Student Models Co-training for Semi-supervised Text Mining (https://aclanthology.org/2023.emnlp-main.244/)
- Anthology ID: 2023.emnlp-main.244 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 많은 텍스트 마이닝 모델들은 downstream 태스크에서 대용량 deep pre-trained language model (PLM)을 fine-tuning하는 방식으로 구성된다. 그러나 최근에는 라벨링된 샘플이 제한된 상황에서 경량 모델을 사용할 때 성능을 유지하는 것이 큰 도전이 된다.
    2. 우리는 DisCo라는 세미-지도학습 (SSL) 프레임워크를 제안한다. 이는 대량 PLM에서 생성된 작은 student model들의 집단을 knowledge distillation을 이용해 fine-tuning하는 것이다.
    3. DisCo는 서로 다른 distillation 전략과 다양한 input augmentation에 의해 생산된 model view와 data view 사이에서 지식 공유를 촉진하는 co-training 기술을 사용하여 여러 작은 student model들의 집단을 최적화한다. 결과적으로 DisCo는 성능을 유지하면서 기준 PLM에 비해 7.6배 작고, 4.8배 빠른 추론 속도를 가진 student model을 생성할 수 있음을 실험 결과로 입증하였다.

###### Dynosaur: A Dynamic Growth Paradigm for Instruction-Tuning Data Curation (https://aclanthology.org/2023.emnlp-main.245/)
- Anthology ID: 2023.emnlp-main.245 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Instruction tuning"은 대형 언어 모델의 지침 이해 및 적절한 응답 생성 능력을 향상시키기 위해 등장했으나, 기존 방법들은 주로 데이터를 직접 주석을 달거나 기존의 LLM을 사용하는 것으로 한정되어 있었다. 
    2. 이 논문에서는 기존 주석이 있는 데이터셋과 지침을 연결시켜 자동으로 지침 튜닝 데이터를 구축하는 "Dynosaur"라는 동적 성장 패러다임을 제안한다. 
    3. Dynosaur는 비용 절감과 고품질의 튜닝 데이터 제공, 지속적인 모델 개선 등의 장점을 제공하며, 새로운 주석 데이터셋이 사용 가능해질 때마다 지속적으로 튜닝 데이터를 생성하여 지속적인 학습을 지원한다.

###### Are All Steps Equally Important? Benchmarking Essentiality Detection in Event Processes (https://aclanthology.org/2023.emnlp-main.246/)
- Anthology ID: 2023.emnlp-main.246 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어는 종종 이벤트를 높은 단위(goal) 이벤트로 나눌 수 있으며, 세부 단계(step) 이벤트들의 순서로 구성될 수 있다. 하지만 이러한 이벤트 프로세스의 중요성은 세부 단계 이벤트들이 중요하지 않을 수 있다는 사실에 있다.
    2. 이 논문에서는 현재 모델들이 목표 이벤트에 대한 세부 단계 이벤트들의 필수성을 얼마나 잘 이해하는지를 연구한다.
    3. 기존 최신 모델들이 인간 수준의 성능을 보이지 못하는 것으로 나타나며, 이러한 중요하지만 도전적인 과제에 대한 미래 연구의 필요성이 나타난다.

###### Language Model is Suitable for Correction of Handwritten Mathematical Expressions Recognition (https://aclanthology.org/2023.emnlp-main.247/)
- Anthology ID: 2023.emnlp-main.247 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 손으로 쓴 수식을 인식하는 작업에서 기존 방법들은 트리 디코더를 사용하여 계층적인 트리 구조를 파악하지만 CFG와 미리 생성된 트리플렛 데이터에 의존하여 확장성이 제한되고 시각적으로 모호한 도전을 간과하고 있다.
    2. 이 연구에서는 LaTeX 수식의 특징적인 언어 특성을 조사하여 구조적인 정보와 의미적인 정보를 동시에 제공할 수 있는 언어 모델의 사용을 제안한다.
    3. 실험 결과, RLFN 모델은 CROHME 2014/2016/2019 데이터셋에서 기존 최첨단 모델들보다 뛰어난 성능을 보여주었다.

###### Vicinal Risk Minimization for Few-Shot Cross-lingual Transfer in Abusive Language Detection (https://aclanthology.org/2023.emnlp-main.248/)
- Anthology ID: 2023.emnlp-main.248 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 고자원 언어에서 중간 및 저자원 언어로의 효과적인 교차 언어 전이 학습은 유망한 결과를 보여주고 있다. 그러나 대상 언어의 자원 부족은 여전히 도전 과제이다.
    2. 이 연구에서는 데이터 증강과 지속적인 사전 학습을 이용하여 도메인 적응을 향상시키고 교차 언어 악성 언어 감지를 개선하기 위해 노력한다.
    3. 데이터 증강 전략은 적은 양의 교차 언어 악성 언어 감지를 향상시킬 수 있는 것으로 나타났으며, 특히 MIXAG 방법은 다양한 도메인 및 다국어 환경에서 유의한 향상을 보였다.

###### SuperDialseg: A Large-scale Dataset for Supervised Dialogue Segmentation (https://aclanthology.org/2023.emnlp-main.249/)
- Anthology ID: 2023.emnlp-main.249 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 세분화는 대화 시스템에 있어서 중요한 작업으로, 대화 내용을 더 잘 이해하는 데 도움을 준다. 그러나 최근의 비지도 대화 세분화 방법은 명시적인 지도 신호의 부족으로 성능이 제한되고 있다.
    2. 본 논문에서는 document-grounded 대화를 활용하여 대화 세분화 지점의 명확한 정의를 제공하고, SuperDialseg라는 대규모 지도 학습 데이터셋을 제작하였다.
    3. 실험 결과, SuperDialseg로 학습한 모델은 도메인 내 데이터에 대해서 매우 효과적이며, 다른 도메인의 데이터에도 좋은 일반화 능력을 보여준다는 것을 확인하였다.

###### ATFormer: A Learned Performance Model with Transfer Learning Across Devices for Deep Learning Tensor Programs (https://aclanthology.org/2023.emnlp-main.250/)
- Anthology ID: 2023.emnlp-main.250 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 점점 커지는 딥 뉴럴 네트워크의 훈련과 추론 효율성은 특정 하드웨어 플랫폼에서 텐서 연산자의 성능에 매우 의존한다. 따라서, 자동 텐서 생성 및 매개 변수 조정과 함께 컴파일 기반의 최적화 플로우가 효율적인 모델 배포에 필요하다.
    2. 성능 모델을 사용한 컴파일 기반 방법은 동적이고 적절한 코드 최적화를 제공할 수 있지만, 그들은 대략적인 측정 정확도와 다른 하드웨어 플랫폼 간의 낮은 이식성과 함께 큰 설계 공간 탐색에 문제가 있다.
    3. 이 논문에서는 ATFormer라는 간단하면서도 효율적인 디자인을 제안하는데, 이는 attent-ion에서 영감을 받은 모듈을 사용하여 전체 스케쥴링 공간에서 전역적이고 장거리적인 종속성을 포착하여 최적화된 연산자의 성능을 정확히 예측할 수 있다.

###### mRedditSum: A Multimodal Abstractive Summarization Dataset of Reddit Threads with Images (https://aclanthology.org/2023.emnlp-main.251/)
- Anthology ID: 2023.emnlp-main.251 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다중모달 온라인 토론의 증가로 인해 시간을 절약하고 콘텐츠 과부하를 줄이기 위해 자동 요약이 필요하지만, 기존의 요약 데이터셋은 토론, 다중 모달 둘 다를 다루지 않기 때문에 이를 위해 적합하지 않다.
    2. 이 논문에서는 첫 번째로 다중모달 토론 요약 데이터셋인 mRedditSum을 제공한다. 이 데이터셋은 3,033개의 토론 쓰레드로 구성되어 있으며, 이미지와 텍스트로 기술된 문제에 대한 조언을 요청하는 게시물과 다양한 의견을 표현한 댓글이 포함되어 있다.
    3. 실험 결과, GPT-3.5, BART, T5와 같은 인기있는 요약 모델은 시각적인 정보를 통합할 때 일관적으로 성능이 향상되었으며, 또한 클러스터 기반의 다단계 요약 방법을 소개하여 기존의 기준에 비해 더 나은 성능을 보여주었다.

###### Sparse Low-rank Adaptation of Pre-trained Language Models (https://aclanthology.org/2023.emnlp-main.252/)
- Anthology ID: 2023.emnlp-main.252 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 파라미터 효율적인 pre-trained language models fine-tuning은 효과와 효율성이 입증되었으나, 고정된 내재적인 rank로 이루어지기 때문에 항상 이상적인 선택이 아닐 수 있다.
    2. 기존의 low-rank adaptation 방법을 확장하여 동적으로 내재적인 rank를 조정할 수 있는 sparse low-rank adaptation (SoRA)라는 혁신적인 접근법을 제안한다.
    3. SoRA는 gate unit을 통해 카디널리티를 조절하여 sparse한 방식으로 rank를 업데이트하며, zeroed-out된 rank에 해당하는 파라미터 블록을 제거하여 concise하면서도 rank-optimal한 LoRA로 줄일 수 있는 표현 능력을 강화한 결과를 보여준다.

###### Human Learning by Model Feedback: The Dynamics of Iterative Prompting with Midjourney (https://aclanthology.org/2023.emnlp-main.253/)
- Anthology ID: 2023.emnlp-main.253 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트에서 이미지를 생성하기 위한 Text-to-Image 모델은 사용자들이 피드백을 받아 자신의 프롬프트를 업데이트하는 반복 과정을 거치는 경우가 많다. 
    2. 이 논문은 인지학적 연구인 참조 게임과 대화 정렬에서 영감을 받아 이러한 반복 과정에서 사용자 프롬프트의 동적을 분석한다. 
    3. 사용자 프롬프트는 특정 특성으로 수렴하며, 이러한 수렴이 사용자가 중요한 세부 정보를 놓친 것을 깨닫고 프롬프트를 수정함으로써 발생하는 것인지 모델의 "선호"에 적응함으로써 발생하는 것인지 연구하였다.

###### ULF: Unsupervised Labeling Function Correction using Cross-Validation for Weak Supervision (https://aclanthology.org/2023.emnlp-main.254/)
- Anthology ID: 2023.emnlp-main.254 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 수동 데이터 레이블링에 비용 대비 효과적인 대안은 약한 지도 (weak supervision)이다. 본 논문에서는 k-fold 교차 검증의 원리를 기반으로 약한 지도에서의 노이즈 감소 기법을 연구한다.
    2. ULF라는 새로운 알고리즘을 제안하여 동작하며, 이는 홀드아웃 된 LFs에 특정한 편향성을 인식하고 수정하기 위해 나머지 모든 LFs로부터 학습된 모델을 활용하여 WS 데이터를 노이즈 제거한다.
    3. 여러 데이터셋에서의 평가 결과 ULF는 수작업 레이블링의 필요없이 WS 학습을 향상시키는 효과가 있다는 것을 확인한다.

###### The Art of SOCRATIC QUESTIONING: Recursive Thinking with Large Language Models (https://aclanthology.org/2023.emnlp-main.255/)
- Anthology ID: 2023.emnlp-main.255 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Chain-of-Thought (CoT) prompting은 대형 언어 모델이 중간 단계를 생성함으로써 복잡한 추론 문제를 해결할 수 있게 한다. 그러나, 순차적으로 생성되는 CoT는 초기 결정에 매우 의존하므로 초기 단계의 오류가 누적되어 최종 답변에 영향을 미친다."
    2. "이 연구에서는 인간의 인지 과정에서 영감을 받아 재귀적인 사고 과정을 모방하는 SOCRATIC QUESTIONING이라는 알고리즘을 제안한다. 이 알고리즘은 충분한 정보를 수집하기 위해 대형 언어 모델을 활용하여 부분 질문을 제기하고 대답하는 방식으로 원래 질문을 해결한다."
    3. "다양한 복잡한 추론 과제인 MMLU, MATH, LogiQA, 그리고 시각적 질의응답에 대한 폭넓은 실험에서는 SOCRATIC QUESTIONING이 CoT, Tree-of-Thought와 같은 최신 prompting 방법보다 유의한 성능 향상을 보인다."

###### Ideology Takes Multiple Looks: A High-Quality Dataset for Multifaceted Ideology Detection (https://aclanthology.org/2023.emnlp-main.256/)
- Anthology ID: 2023.emnlp-main.256 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사람들의 의견과 사회에 대한 입장에 대한 통찰력을 얻는 것은 정치, 경제 및 사회과학 분야에서 많은 응용 가능성이 있는 "Ideology detection(ID)"연구에 있어서 중요한 과제이다.
    2. 기존의 ID 작업 데이터셋은 텍스트를 전체적으로 좌파 또는 우파로 라벨링 하지만, 텍스트는 다양한 주제를 담고 있을 수 있으며 결정은 주제마다 개별적으로 내려지는 경우가 일반적이다.
    3. 이 논문에서는 사회과학적 이론을 활용하여, 다각적 인식(Ideology)을 보다 완전하고 정교하게 표현하기 위해 새로운 다각적 인식(MID) 작업을 위한 5개 도메인과 12개 facet을 포함하는 독자적인 스키마를 설계하였고, 이를 위해 12,594개의 Twitter 포스트 데이터셋을 구축하고 각각의 facet에 대한 Relevance 및 Ideology 레이블을 붙였다.

###### Transductive Learning for Textual Few-Shot Classification in API-based Embedding Models (https://aclanthology.org/2023.emnlp-main.257/)
- Anthology ID: 2023.emnlp-main.257 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소개된 논문은 소유 및 폐쇄적인 API가 자연어 처리 응용 프로그램에 미치는 영향과 적은 양의 레이블된 데이터로 모델을 사용하는 few-shot classification에 대해 알려주고 있다. 
    2. 그들은 gated API를 통해 사전 학습된 모델의 임베딩을 제공하는 시나리오를 소개하고, NLP 커뮤니티에서 소홀히 여겨진 transductive inference라는 학습 패러다임을 제안한다. 
    3. 또한, 개선된 실험 환경을 제안하고 4개 다른 언어에 걸쳐 8개의 데이터셋과 151개의 클래스로 구성된 벤치마크를 편집하여 자신들의 방법을 평가하였다.

###### MEGA: Multilingual Evaluation of Generative AI (https://aclanthology.org/2023.emnlp-main.258/)
- Anthology ID: 2023.emnlp-main.258 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 생성적 AI 모델은 영어에 대해서 많은 NLP 태스크에서 높은 성능을 보여주었지만, 다른 언어에 대한 이해와 생성에 대한 능력은 여전히 불문명하다. 이 논문에서는 다양한 언어들을 포함한 LLM 모델들의 성능을 평가하는 16개의 NLP 데이터셋을 포함하는 벤치마킹을 제안한다.
    2. Chat-GPT와 GPT-4를 포함한 생성 모델들과 SOTA의 non-autoregressive 모델을 비교하여 성능을 평가한다. 저자들은 저자별, 언어별, 태스크별 성능을 분석하고 저자들과 언어 리소스 부족 언어를 대상으로 한 generative LLMs의 성능 향상에 대한 도전점을 논의한다.
    3. 이 연구는 다국어 환경에서 generative LLMs를 평가하는 프레임워크를 개발하고, 이 분야의 미래적 발전 방향을 제시한다.

###### Support or Refute: Analyzing the Stance of Evidence to Detect Out-of-Context Mis- and Disinformation (https://aclanthology.org/2023.emnlp-main.259/)
- Anthology ID: 2023.emnlp-main.259 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인터넷에서의 거짓 정보와 오염된 정보는 다양한 형태의 온라인 피해의 주요 원인으로 사회적 문제가 되고 있다. 이 논문에서는 다양한 종류의 다양한 증거들에 대한 정보를 추출하는 알고리즘을 제안하여 소셜 미디어 플랫폼에서 잘못된 문맥에 있는 정보를 식별하는 데 있어 새로운 접근 방식을 제시한다.
    2. 정보의 스탠스(stance)는 다른 감지 결과에 대한 편향성을 나타내므로, 다양한 다중모달(evidence)의 스탠스를 통합적인 프레임워크에서 추출할 수 있는 'stance extraction network (SEN)'을 소개한다.
    3. 대규모 공개 데이터셋에서의 실험 결과에서 우리의 제안된 방법이 최신 기준 모델을 능가하는 것을 보여주며, 최고의 모델은 정확도에서 3.2%의 성능 향상을 얻었다.

###### Video-Helpful Multimodal Machine Translation (https://aclanthology.org/2023.emnlp-main.260/)
- Anthology ID: 2023.emnlp-main.260 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 다중 모달 기계 번역(MMT) 데이터셋은 이미지와 비디오 자막에 대한 설명 또는 교육 비디오 자막으로 구성되어 있으며, 언어적 모호성이 드물어 시각 정보가 적절한 번역을 생성하는 데 효과적이지 못하다.  
    2. 본 논문에서는 EVA라는 새로운 MMT 데이터셋을 제시하여 많은 양의 훈련 데이터와 모호한 자막 및 비디오에서 인과 관계 파악을 위한 도움을 준다.
    3. EVA의 실험 결과, 시각 정보와 제안된 방법들이 번역 성능을 향상시키며, 기존의 MMT 모델보다 우수한 성능을 보여준다.
    
    Note: The second summary sentence is quite long, you can consider summarizing it with the main point of the sentence in two separate sentences if required.

###### Large Language Models are Temporal and Causal Reasoners for Video Question Answering (https://aclanthology.org/2023.emnlp-main.261/)
- Anthology ID: 2023.emnlp-main.261 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Large Language Models (LLMs)의 사전 정보를 활용한 Video Question Answering (VideoQA)에서 언어적 편향을 완화하고, 시각적 콘텐츠도 고려하는 Flipped-VQA 프레임워크를 제안합니다."
    2. 이 프레임워크는 LLMs 기반 모델인 LLaMA-VQA를 개발하여 여러 도전적인 VideoQA 벤치마크에서 다른 기반 모델보다 우수한 성능을 보여주었습니다.
    3. 추가적으로, Flipped-VQA는 OPT와 GPT-J와 같은 다양한 LLMs에 적용 가능하며, 언어적인 단축키를 활용 뿐만 아니라 언어적 편향을 완화시키는 것을 실험적으로 입증하였습니다.

###### Uncertainty Guided Global Memory Improves Multi-Hop Question Answering (https://aclanthology.org/2023.emnlp-main.262/)
- Anthology ID: 2023.emnlp-main.262 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 트랜스포머는 많은 자연어 처리 작업과 특히 다중 홉 질문 답변 (MHQA) 작업에 있어서는 표준이 되었다. 기존들은 답변을 예측한 사실로 컨텍스트를 제한하는 반면, 두 번째 그룹은 멀티홉 추론을 위해 긴 입력 인코딩 모델의 attention 메커니즘에 의존한다. 
    2. 하지만 attention 기반의 토큰 표현은 추론 단계를 연결하는 데 필요한 명시적인 전역적 컨텍스트 정보가 부족하다. 
    3. 이 문제를 해결하기 위해 우리는 전체 문서에서 관련 정보들을 모아 메모리에 저장하고, 이를 지역적 컨텍스트와 결합해서 작업을 수행하는 GEMFormer를 제안한다. 실험 결과는 MHQA 데이터셋에서 기초 모형에 비해 미리 학습된 모형을 global elements을 포함한 메모리 증강 입력으로 미세 조정하는 것이 모델의 성능을 개선하는 것을 보여주었다. 또한, 전역적 컨텍스트 메모리는 올바른 답변을 도출하는 데 필요한 사실 정보를 담고 있다는 것을 확인하였다.

###### Prompting Large Language Models with Chain-of-Thought for Few-Shot Knowledge Base Question Generation (https://aclanthology.org/2023.emnlp-main.263/)
- Anthology ID: 2023.emnlp-main.263 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 베이스를 활용한 질문 생성 작업에서 비용이 많이 드는 주석화된 데이터에 의존하여 fine-tuning하는 현재의 방법은 소수의 데이터로도 잘 동작하지 않음이 문제이다.
    2. 이 논문에서는 large language model을 활용하여 적은 데이터로도 잘 작동하는 질문 생성 방법을 제안한다. 추가적으로, reasoning을 고려한 "Chain-of-Thought (CoT)" prompting을 활용하여 복잡한 질문을 생성하는 논리 체인 생성 방법 (KQG-CoT)을 제안한다.
    3. 실험 결과는 KQG-CoT가 다른 baseline들보다 일관적으로 더 좋은 결과를 보이는 것을 보여주며, 특히 PathQuestions 데이터셋에서는 BLEU-4, METEOR, ROUGE-L에서 18.25, 10.72, 10.18 절대점수 차이로 기존 few-shot의 최고 성능을 뛰어넘는다.

###### TrojanSQL: SQL Injection against Natural Language Interface to Database (https://aclanthology.org/2023.emnlp-main.264/)
- Anthology ID: 2023.emnlp-main.264 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트-투-SQL 기술은 데이터베이스 접근 및 조작의 효율성을 크게 향상시켰으나, 악의적인 사용자 상호작용에서 발생하는 취약점에 대한 연구는 제한적이다.
    2. TrojanSQL을 제안함으로써, 최신 텍스트-투-SQL 파서가 악성 SQL 문을 쉽게 생성하여 사용자 쿼리를 무효화하거나 데이터베이스의 민감한 정보를 침해할 수 있다는 것을 보여준다.
    3. 실험 결과는 fine-tuning 기반의 중간 크기 모델과 prompting 기술을 사용하는 LLM 기반 파서 모두 이러한 유형의 공격에 취약하며, 공격 성공률은 각각 99%와 89%로 매우 높음을 보여준다.

###### Preserving Privacy Through Dememorization: An Unlearning Technique For Mitigating Memorization Risks In Language Models (https://aclanthology.org/2023.emnlp-main.265/)
- Anthology ID: 2023.emnlp-main.265 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large Language models, LLMs)은 민감한 개인정보가 노출될 위험이 있는 데이터를 포함한 방대한 양의 데이터로 학습된다.
    2. 이 논문에서는 기존의 기억 문제를 해결하고 지식의 불필요한 재현을 방지하기 위해 "DeMem"이라는 새로운 재학습 접근 방식을 제안한다.
    3. DeMem은 강화 학습 피드백 루프를 통해 효율적으로 학습 모델을 조정하고, LLMs이 사전 훈련 데이터를 잊기 위한 변형 정책을 학습하도록 유도한다. 실험 결과, DeMem은 개인정보 보호와 LLM 성능 유지 사이의 균형을 유지하면서 강력한 기준선과 최신 기법을 능가한다.

###### MingOfficial: A Ming Official Career Dataset and a Historical Context-Aware Representation Learning Framework (https://aclanthology.org/2023.emnlp-main.266/)
- Anthology ID: 2023.emnlp-main.266 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 중국연구에서는 전통적인 연구에서는 확인할 수 없던 역사적 인물의 뉘앙스를 이해하는 것이 주요한 관심사이다. 이 논문에서는 중국의 명나라 관리들에 대한 연구를 조사하기 위해 MingOfficial이라는 대규모 다중 모달 데이터셋을 제안한다.
    2. MingOfficial 데이터셋은 구조화된 데이터 (경력 기록, 주석이 달린 인사 유형)와 텍스트 데이터 (역사적 텍스트)로 구성되어 있으며, 관료의 사회 구조를 조사하고 다운스트림 테스크에서 성능을 향상시키기 위해 그래프 신경망 (GNN)과 결합되어 있다.
    3. 실험 결과 MingOfficial은 관료의 정체성을 탐색적으로 분석하는데 도움이 되며, 유의미한 특성 (예: 군사력을 가진 민간 관리)을 식별하는 작업에서도 성능을 대폭 향상시킬 수 있음을 보여준다. 이 데이터셋은 중국 연구분야뿐만 아니라 다른 분야의 컴퓨팅 접근 방법에 대한 영감을 제공하기 위해 공개되었다.

###### DPP-TTS: Diversifying prosodic features of speech via determinantal point processes (https://aclanthology.org/2023.emnlp-main.267/)
- Anthology ID: 2023.emnlp-main.267 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 심층 생성 모델의 발전으로 최근 TTS 모델은 사람과 유사한 음성을 합성할 수 있으나, 흥미로운 TTS의 제작은 여전히 문제가 있다.
    2. 우리는 Determinantal Point Processes (DPPs)를 기반으로 한 TTS 모델인 DPP-TTS를 제안하여 음성 샘플의 다양성을 개선한다.
    3. DPP-TTS는 각 샘플과 다른 샘플 사이에도 지각적 다양성을 고려하여 음성 샘플을 생성하여 자연스러움을 유지한다.

###### Meta-Learning Online Adaptation of Language Models (https://aclanthology.org/2023.emnlp-main.268/)
- Anthology ID: 2023.emnlp-main.268 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델은 광범위한 세계지식을 인코딩하지만, 정적으로 학습된 언어 모델은 지식이 오래되어 모델의 유효한 수명을 제한한다. 
    2. 이 논문에서는 온라인 파인튜닝이 모델 정보 흡수에 있어서 부적합한 문제를 발견하였다. 
    3. 따라서, 이 논문에서는 중요한 정보에 충분히 주의를 기울이지 못하는 문제를 해결하기 위해 동적, 문맥-지능적 학습률을 제안하고, 개선된 정보 흡수를 위한 Context-aware Meta-learned Loss Scaling (CaMeLS)를 제안한다.

###### Self-Detoxifying Language Models via Toxification Reversal (https://aclanthology.org/2023.emnlp-main.269/)
- Anthology ID: 2023.emnlp-main.269 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 Language Model detoxification 방법들은 세분화(finetuning)와 decoding을 기반으로 한다. 그러나 전자는 자원이 많이 소모되고, 후자는 추가 구성 요소가 필요하며 생성 유창성을 저하시킬 수 있다.
    2. 저자는 PLM 자체가 'self-detoxification'을 달성할 수 있는 가벼운 방법을 제안한다. 이 방법은 부정적인 이동 prompt를 PLMs에 일으켜유해한 내용을 생성하도록 유도한다는 관찰에 기초한다.
    3. 실험 결과, 저자들의 방법은 세분화나 추가 구성 요소 없이도 최첨단 방법들과 비교 가능한 성능을 달성할 수 있다는 것을 보여준다.

###### Interactive Text Generation (https://aclanthology.org/2023.emnlp-main.270/)
- Anthology ID: 2023.emnlp-main.270 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 유저들은 텍스트, 이미지, 코드 등과 상호작용하는 에디터를 매일 사용하지만, 기계 학습 모델은 이러한 상호작용을 반영한 설정으로 훈련되는 경우가 거의 없다. 훈련할 때 실제 유저를 사용하는 것은 느리고 비용이 많이 들며, 모델이 배울 수 있는 내용이 유저 인터페이스 디자인 선택에 특정되기 때문이다.
    2. 이 논문에서는 유저 시뮬레이터를 사용하여 실제 유저를 수반하지 않고, 모델을 목표 텍스트로 안내하는 편집을 제공하여 상호작용적으로 훈련시킬 수 있는 새로운 Interactive Text Generation 과제를 제안한다.
    3. Imitation Learning을 사용하여 상호작용 모델을 훈련시킨 결과, 경쟁력 있는 비상호작용 세대 모델보다 훨씬 우수한 결과를 얻을 수 있었다.

###### Knowledge Distillation ≈ Label Smoothing: Fact or Fallacy? (https://aclanthology.org/2023.emnlp-main.271/)
- Anthology ID: 2023.emnlp-main.271 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 전이를 위한 메소드로 제안된 지식 압축(Knowledge Distillation, KD)은 실제로 정규화의 한 형태라는 최근 연구들이 있다. 
    2. 두 방법 사이의 관계를 다시 검토하기 위해 각 방법으로 훈련된 모델들의 예측 신뢰도를 비교했다.
    3. 다양한 크기의 모델들이 포함된 4개의 텍스트 분류 작업 실험에서, KD와 LS는 대부분 상반된 방향으로 모델의 신뢰도를 조정하며, KD에서 학생은 지식과 함께 신뢰도도 선생으로부터 상속 받아 전통적인 지식 전달 관점이 강화됨을 보여준다.

###### Analyzing Cognitive Plausibility of Subword Tokenization (https://aclanthology.org/2023.emnlp-main.272/)
- Anthology ID: 2023.emnlp-main.272 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현재 subword tokenization은 토큰화에 대한 국제적인 비교 평가가 부족한 상태이다. 기존의 연구는 토큰화 알고리즘의 위력이 downstream task에서 어떤 영향을 주는지, 수학적 기준들에 대해 집중했다.
    2. 우리 연구는 subword tokenization의 인지적 타당성에 초점을 맞춘 새로운 평가 방법론을 제시한다.
    3. 우리의 결과는 Unigram 알고리즘이 인지적으로 덜 타당성이 있으며 파생형 형태소의 커버리지 면에서도 문제가 있다는 것을 보여준다.

###### POE: Process of Elimination for Multiple Choice Reasoning (https://aclanthology.org/2023.emnlp-main.273/)
- Anthology ID: 2023.emnlp-main.273 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델은 다지선다 추리 태스크에 대한 in-context 학습을 수행할 수 있지만, 이러한 태스크에서 옵션들은 동등하게 처리된다. 
    2. 우리는 인간들이 종종 마지막으로 올바른 대답을 고르기 전에 잘못된 옵션들을 먼저 제거하는데, 이러한 두 단계 전략이 언어 모델이 이러한 태스크에서 더 잘 수행되도록 할 수 있다고 주장한다. 
    3. 우리는 이를 위해 두 단계 점수화 방법인 POE를 제안하며, 8가지 추리 태스크에 대한 제로샷 실험을 통해 POE의 효과를 입증하고, 논리 추론 태스크에서 특히 우수한 성능을 나타내는 것으로 나타났다.

###### NeuSTIP: A Neuro-Symbolic Model for Link and Time Prediction in Temporal Knowledge Graphs (https://aclanthology.org/2023.emnlp-main.274/)
- Anthology ID: 2023.emnlp-main.274 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 지식 그래프 완성(Neuro-symbolic models for knowledge graph completion, KGC) 모델은 정적 사실을 다루는 데는 매우 강력하지만, 시간적 사실을 다루는 시간적 지식 그래프 완성(Temporal KGC) 모델은 제한적이다. 
    2. 우리는 Allen predicates를 사용하여 시간적 일관성을 보장하는 새로운 NS 모델인 NeuSTIP을 제안한다. 
    3. 우리의 실험 결과는 link prediction에서 경쟁력 있는 성능을 보이며, time interval prediction에서도 최고의 성능을 달성함을 보여준다.

###### Standardizing Distress Analysis: Emotion-Driven Distress Identification and Cause Extraction (DICE) in Multimodal Online Posts (https://aclanthology.org/2023.emnlp-main.275/)
- Anthology ID: 2023.emnlp-main.275 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회적 발언에 대한 영향력이 커지면서, 사회적 미디어 위에서의 혐오 발언이 주목받고 있다. 그러나, 이전의 자동화된 방법들은 주로 텍스트 콘텐츠만을 분석하는 것이 한계였다. 이 연구에서는 다중모달 온라인 포스트로부터의 고통 파악과 원인 추출 문제를 제안하고 이에 대한 다중태스크 딥 프레임워크를 개발한 것으로, 이 연구는 고통의 내용을 동시에 감지하고 감정 정보를 활용하여 원인 구문을 식별한다. 
    2. 우리는 zero-shot 전략을 사용하여감정 정보를 훈련 프로세스에 통합하였으며, 다중모달 입력의 특징을 퓨즈 (fuse)하기 위해 새로운 메커니즘을 고안했다.
    3. 또한 우리는 Distress and Cause annotated Multimodal (DCaM) 데이터셋을 도입하였으며, 기존 벤치마크와의 비교를 통해 우리의 방법을 철저하게 평가하였다.

###### Out-of-Distribution Generalization in Natural Language Processing: Past, Present, and Future (https://aclanthology.org/2023.emnlp-main.276/)
- Anthology ID: 2023.emnlp-main.276 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 처리 (NLP)의 기계 학습 (ML) 시스템은 테스트 분포가 훈련 데이터 분포와 다른 out-of-distribution (OOD) 데이터에 일반화하는 데 중요한 도전을 겪고 있다. 이로 인해 NLP 모델의 robustness와 높은 정확성에 대한 의문이 제기되며, 이러한 정확성은 체계적인 편향에 민감함으로 인해 인위적으로 과장될 수 있다.
    2. 이 연구는 OOD 관점에서 자연어 이해의 일반화 도전에 대한 최근의 진전, 방법 및 평가에 대한 첫 번째 포괄적인 리뷰를 제시하여 이러한 공백을 메울 것을 목표로 한다. 
    3. 우리는 이미 존재하는 연구에 대한 편리한 접근을 제공함으로써 이 분야의 향후 연구를 격려하길 바란다.

###### Noisy Exemplars Make Large Language Models More Robust: A Domain-Agnostic Behavioral Analysis (https://aclanthology.org/2023.emnlp-main.277/)
- Anthology ID: 2023.emnlp-main.277 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 프롬프트 엔지니어링의 진전으로 인해 대형 언어 모델 (LLMs)이 멋진 정확성으로 다중 점프 논리 추론 문제를 해결할 수 있게 되었으나, 몇 회의 프롬프트 기법의 강건성을 조사한 연구는 거의 없다.
    2. 따라서 우리는 도메인에 무관한 간섭을 통해 LLM의 멀티합 추론 과제의 강건성을 시험하는 체계적인 접근법을 제안한다.
    3. 우리는 질문에 중간 추론 단계를 포함한 (오타와 같은 어휘적 간섭 및 의미적 간섭과 같은) 여러 수준의 변형을 포함하며 LLM에 대한 행동 분석을 진행한다.

###### Can Large Language Models Capture Dissenting Human Voices? (https://aclanthology.org/2023.emnlp-main.278/)
- Anthology ID: 2023.emnlp-main.278 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "큰 언어 모델(LLM)은 다양한 태스크 해결에서 인상적인 성과를 보였으며, instruction fine-tuning에 의해 zero-shot 상황에서도 일반화가 가능함이 입증되었으나, 특히 자연어 추론(NLI)의 범위 내에서 LLM이 인간의 불일치 분포와 얼마나 일치하는지는 잘 연구되지 않았다."
    2. "본 논문에서는 MCE(Monte Carlo Estimation)와 LPE(Log Probability Estimation) 두 가지 기법을 사용하여 LLM의 분포와 인간의 일치 여부를 평가한다."
    3. "결과적으로, 우리는 LLM이 NLI 태스크를 해결하는 능력이 제한적이며 동시에 인간의 불일치 분포를 잘 포착하지 못한다고 보여준다. 사람들과 견해가 차이가 많은 데이터 샘플에서는 推論 및 인간 일치 성능이 더욱 떨어지므로, 자연어 이해(NLU) 능력 및 더 큰 인간 집단에 대한 대표성에 대한 우려가 제기된다."

###### DecoMT: Decomposed Prompting for Machine Translation Between Related Languages using Large Language Models (https://aclanthology.org/2023.emnlp-main.279/)
- Anthology ID: 2023.emnlp-main.279 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구는 단어 순서와 어휘 유사성과 같은 언어적 특징을 공유하는 관련 언어 사이에서의 기계 번역에 대해 조사한다. 
    2. 기계 번역을 단어 묶음 번역의 일련의 순서로 분해하는 DecoMT라는 새로운 few-shot prompting 접근법을 제안한다. 
    3. 여러 언어 가족 간에 수행된 자동 및 인간 평가를 통해, DecoMT가 다양한 established few-shot 기준 모델보다 우수한 성능을 보여준다는 것을 입증한다.

###### Prototype-based HyperAdapter for Sample-Efficient Multi-task Tuning (https://aclanthology.org/2023.emnlp-main.280/)
- Anthology ID: 2023.emnlp-main.280 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Parameter-efficient fine-tuning (PEFT)은 사전 훈련된 언어 모델을 downstream task에 효과적으로 적용하는데, 일부 파라미터만 업데이트함으로써 작동한다. 그러나 대부분의 기존 방법들은 각각의 task를 독립적으로 적용하며, 다른 task 사이에서의 지식 전달을 고려하지 않으며, 데이터가 적은 경우에만 적용 가능하다. 
    2. 이 문제에 대해, 우리는 Adapter-tuning과 Hypernetwork 기반의 Prototye-based HyperAdapter (PHA)라는 새로운 프레임워크를 제안한다. 이는 효율적인 샘플링 방법을 통해 조건부 모듈을 생성하여 기존의 PEFT 기법들보다 비슷한 성능 향상을 이끌어낸다. 
    3. 다양한 데이터셋을 기반으로 한 실험 결과, PHA가 학습 가능한 파라미터, stream tasks에서의 정확성 및 샘플 효율성 간에 더 나은 균형을 이룬다는 것을 보여준다.

###### Towards Building More Robust NER datasets: An Empirical Study on NER Dataset Bias from a Dataset Difficulty View (https://aclanthology.org/2023.emnlp-main.281/)
- Anthology ID: 2023.emnlp-main.281 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 연구들은 Named Entity Recognition(NER) 시스템의 robustness 문제를 보여주고 있다. NER 모델은 종종 context의 evidence를 고려하지 않고 단순한 entity 패턴에 의존하여 예측을 수행한다. 이로 인해 최신 기술을 갖춘 NER 모델들도 out-of-distribution entity 패턴이 소개될 때 out-of-domain 시나리오에서 일반화가 잘 되지 않는다.
    2. 예전 연구는 NER 데이터셋의 bias가 robustness 문제의 원인이며, 더 간단하고 정규한 entity 패턴은 shortcut learning을 유도한다고 추론하였다. 그러나 이 논문에서는 dataset difficulty 관점에서 NER 데이터셋의 bias를 철저히 조사하여 새로운 통찰을 제시한다.
    3. 우리는 기존 데이터셋의 entity-context 어려움 분포를 정량화하고 이들이 모델의 robustness와의 관계를 설명한다. 이를 기반으로, 우리는 entity-context 분포를 변경하여 NER 데이터셋의 bias를 해결하기 위해 세 가지 접근법을 탐구하고, 실험을 통해 사실성을 입증한다. 마지막으로, 우리는 de-biased된 데이터셋이 다른 모델에 전이될 수 있으며, 기존의 robustness 개선 방법에도 도움을 줄 수 있음을 보여줌으로써, 보다 robust한 데이터셋을 구축하는 것이 보다 robust한 NER 시스템을 구축하는 데 근본적인 역할을 한다는 것을 보여준다.

###### GradSim: Gradient-Based Language Grouping for Effective Multilingual Training (https://aclanthology.org/2023.emnlp-main.282/)
- Anthology ID: 2023.emnlp-main.282 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 세계의 대부분 언어들은 자연어처리 모델에 낮은 리소스 도전과제를 제시합니다. 다국어 훈련을 통해 언어 간 지식을 공유할 수 있습니다. 하지만 모든 언어가 서로 긍정적으로 영향을 미치는 것은 아니며, 다국어 훈련에 가장 적합한 언어 집합을 선택하고 특성이나 데이터 분포가 호환되지 않는 언어 간의 부정적인 간섭을 피하는 방법은 여전히 연구되어야할 문제입니다.
    2. 이 논문에서는 그레디언트 유사도를 기반으로 한 언어 그룹화 방법인 GradSim을 제안합니다. 세 가지 다양한 다국어 벤치마크 데이터셋에서의 실험 결과, 이 방법이 다른 유사도 측정 방법보다 가장 큰 성능 향상을 이끌며, 크로스-언어 모델 성능과 더 나은 상관관계를 가짐을 보입니다.
    3. 우리는 저자들이 제안한 방법을 사용하여 낮은 리소스를 가진 아프리카 언어에 대한 감성 분석 벤치마크인 AfriSenti에서 새로운 최고 성적을 달성하였고, 더 나아가 언어 그룹화에 있어서 언어의 주제 뿐만 아니라 언어 특성 및 변형 모델의 하위 레이어들이 언어와 태스크 특정 정보를 포착한다는 사실을 밝혀내었습니다.

###### Discovering Universal Geometry in Embeddings with ICA (https://aclanthology.org/2023.emnlp-main.283/)
- Anthology ID: 2023.emnlp-main.283 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구는 독립 성분 분석 (ICA)을 활용하여 단어 또는 이미지의 임베딩 내에서 일관된 의미 구조를 밝힌다.
    2. PCA의 백색화 과정 이후 남아 있는 이방성 정보를 활용하여 사전 훈련된 모델의 임베딩에서 독립적인 의미 구성 요소를 추출한다.
    3. 임베딩의 기하 패턴에서 탐색한 범용적인 의미 구조의 발견은 임베딩 내의 표현에 대한 이해를 향상시킨다.

###### Toward a Critical Toponymy Framework for Named Entity Recognition: A Case Study of Airbnb in New York City (https://aclanthology.org/2023.emnlp-main.284/)
- Anthology ID: 2023.emnlp-main.284 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Critical toponymy"은 장소 이름과 이를 참조하는 장소의 권력, 자본, 저항의 역동성을 연구한다. 그러나 이 장소 이름이 일상 대화에서 어떻게 사용되고, 이들에 대한 상황적인 설명을 무시하는 경우가 많다.
    2. 본 논문에서는 뉴욕의 Airbnb에 등재된 47,440개의 리스트를 기반으로 문화적, 경제적 자본이 사람들이 장소를 참조하는 방식에 어떤 영향을 미치는지를 측정하는 컴퓨터 기반 방법을 개발하고, 장소를 특징 지을 때 중요한 언어적 특징을 인식하는 새로운 named entity recognition (NER) 모델을 소개한다.
    3. 이 연구 결과는 critical toponymy와 관련하여 새로운 연구 방향을 제시하며, 이웃상태, 주거 및 관광 시장, 젠트리피케이션에 관한 이전에 연구되지 않았던 언어적 신호들을 다룬다.

###### Well Begun is Half Done: Generator-agnostic Knowledge Pre-Selection for Knowledge-Grounded Dialogue (https://aclanthology.org/2023.emnlp-main.285/)
- Anthology ID: 2023.emnlp-main.285 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 기반 대화 시스템에서 정확한 지식 선택은 매우 중요하다. 이 연구에서는 기존의 문헌을 지식 선택이 생성 전에, 후에, 생성 과정에서 어떻게 사용되었는지의 관점으로 분류하여 제안한다.
    2. 우리는 LLMs(예: ChatGPT)를 위해 지식 선택을 생성 전에 수행하는 것이 가벼우면서도 효과적인 방법이라는 것을 실험 결과를 통해 입증하였다.
    3. 우리의 제안인 GATE는 지식의 다양한 구조와 가변적인 지식 요구 사항들 중에서 문맥과 관련된 지식을 선택하여 후속 응답 생성 모델에 대비하는, 생성기-중립적인(knowledge selection method) 방법이다.

###### Merging Generated and Retrieved Knowledge for Open-Domain QA (https://aclanthology.org/2023.emnlp-main.286/)
- Anthology ID: 2023.emnlp-main.286 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 오픈 도메인 질문응답 시스템은 검색 모듈로 구축되는 경우가 많은데, 주어진 소스로부터 문단을 검색하는 것은 지식의 커버리지 부족으로 알려져 있다. 
    2. 이 논문에서는 검색된 결과와 대조적으로, parameter 지식에 기반한 large language model들이 문맥을 생성하게 함으로써 QA 성능을 향상시킬 수 있다고 한다.
    3. 논문은 두 가지 정보 소스를 효과적으로 결합하여 더 나은 오픈 도메인 QA 성능을 제공하는 COMBO라는 프레임워크를 제안하고 있다.

###### Best of Both Worlds: Towards Improving Temporal Knowledge Base Question Answering via Targeted Fact Extraction (https://aclanthology.org/2023.emnlp-main.287/)
- Anthology ID: 2023.emnlp-main.287 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Temporal question answering (QA)은 사건의 시간 간격을 단언하는 사실들에 대한 추론을 요구하는 복잡한 질문 응답 과제의 특수한 범주이다.
    2. 기존의 작업은 주로 지식 베이스 질문 응답 (KBQA)에 의존했으며, 이 시스템들이 질문응답에 필요한 모든 관련 사실들을 검색하지 못하는 문제가 있다.
    3. 이 논문에서는 KBQA가 교차 시간 사실을 검색하지 못하는 경우에 대응하기 위해 대상이 되는 시간적 사실 추출 기술을 사용하여 KBQA를 보조하는 방법을 제안한다.

###### Text Fact Transfer (https://aclanthology.org/2023.emnlp-main.288/)
- Anthology ID: 2023.emnlp-main.288 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트 스타일 전환은 텍스트의 사실적인 내용을 변경하지 않으면서 스타일을 조작하는 중요한 작업이다. 이 논문에서는 텍스트의 사실적인 내용을 스타일을 변경하지 않고 다른 주제로 전환하는 "텍스트 사실 전달" 작업을 제안한다.
    2. 기존 언어 모델은 출처 텍스트의 구체성과 문장 표현을 보존하지 못하고 오류를 조작하는 경향이 있어 텍스트 사실 전달 작업에서 어려움을 겪는다.
    3. 이 문제를 해결하기 위해, 우리는 최소한의 수정으로 출처 텍스트를 변경하는 새로운 조합인 end-to-end question generation과 specificity-aware question answering을 사용하는 ModQGA 프레임워크를 설계했다. ModQGA는 출처 텍스트의 스타일을 희생하지 않고 사실적인 내용을 정확하게 전달할 수 있다는 실험 결과를 보여준다.

###### A Cheaper and Better Diffusion Language Model with Soft-Masked Noise (https://aclanthology.org/2023.emnlp-main.289/)
- Anthology ID: 2023.emnlp-main.289 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에 제안된 확산 모델들은 이미지 생성과 같은 다양한 생성 작업에 활용되어왔으나 기존의 확산 모델은 연속적인 데이터를 위해 구축된 방식이기 때문에 언어와 같은 이산적인 데이터 모델링에는 제한이 있다.
    2. 이 논문에서는 언어 모델링을 위한 새로운 확산 모델, Masked-Diffuse LM을 소개하며, 언어의 언어적 특징에서 영감을 받아 훨씬 더 낮은 훈련 비용과 더 좋은 성능을 제공한다.
    3. 우리는 제안된 Masked-Diffuse LM을 통해 5가지 제어 생성 작업에서 실험을 통해 최신 확산 모델보다 더 좋은 생성 품질과 더 효율적인 성능을 보여줌으로써 우리의 방법의 효과를 입증하였다.

###### Mirages. On Anthropomorphism in Dialogue Systems (https://aclanthology.org/2023.emnlp-main.290/)
- Anthology ID: 2023.emnlp-main.290 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 대화 시스템은 사람들에게 사람과 같은 존재로 여겨질 수 있도록 개발되고 사용된다. 그러나 이 논문에서는 이러한 인간화 현상이 불필요하고 위험한 상황을 초래할 수 있다고 주장한다.
    2. 자연어 처리 연구자들은 이러한 인간화 현상을 유발시키는 요인을 연구하고 그 효과를 완화시키기 위한 자원을 개발하였으나, 이러한 연구들은 분산되어 있고, 인간화의 많은 측면이 아직 탐구되지 않았다.
    3. 논문은 대화 시스템의 인간화에 기여하는 언어적 요소와 그로 인해 발생할 수 있는 피해에 대해 논의하며, 앞으로의 대화 시스템 개발에 있어서 디자인, 개발, 출시, 설명 등에 특별한 주의를 기울여야 하며, 사용자들이 인간화를 유도할 수 있는 다양한 언어 신호들에 주의해야 한다고 제안한다.

###### Cognitive Dissonance: Why Do Language Model Outputs Disagree with Internal Representations of Truthfulness? (https://aclanthology.org/2023.emnlp-main.291/)
- Anthology ID: 2023.emnlp-main.291 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 신경 언어 모델은 사실적인 문장의 진실 여부를 평가하기 위해 질의나 내부 표현 방식으로 사용될 수 있다. 이전 연구들은 이 두 가지 절차가 때때로 일치하지 않으며, 내부 표현이 LM의 출력보다 더 정확한 경향이 있다고 발견했다. 이를 통해 일부 연구자들은 LMs가 "거짓말"을 하거나 비협력적인 의사소통 의도를 인코드한다고 결론을 내렸다.
    2. 이 논문에서는 이러한 질의-내부 표현의 불일치가 다른 방식으로 발생할 수 있는지 확인하였고, 이를 confabulation, deception, heterogeneity 세 가지 클래스로 구분하였다.
    3. 많은 경우에는 내부 표현의 우수성은 단순히 불확실한 답변에 대한 더 나은 보정(calibration)으로 설명될 수 있으며, 일부 입력의 서브셋에서는 질의와 내부 표현이 서로 다르게 수행되어 정확도를 더욱 향상시킬 수 있다고 한다.

###### KEBAP: Korean Error Explainable Benchmark Dataset for ASR and Post-processing (https://aclanthology.org/2023.emnlp-main.292/)
- Anthology ID: 2023.emnlp-main.292 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사용자 만족도와 밀접한 연관이 있는 Automatic Speech Recognition (ASR) 시스템은 다양한 응용 분야에서 중요한 역할을 한다. 그러나 기존의 ASR 평가 방법은 한 개의 통합 점수만을 제공해 특정한 시스템 취약점을 이해하기에는 불충분하다. 
    2. 이 논문에서는 ASR 및 후처리 (Post-processing)에 대한 한국어 오류 설명 벤치마크 데이터셋인 KEBAP을 소개함으로써 이전 ASR 평가 방법의 한계를 해결하고자 한다. 
    3. KEBAP은 음성 및 텍스트 수준에서 ASR 시스템을 포괄적으로 분석하여 음성 인식 정확도와 사용자 가독성을 모두 고려한 균형 잡힌 평가를 가능하게 한다.

###### Adaptive Policy with Wait-k Model for Simultaneous Translation (https://aclanthology.org/2023.emnlp-main.293/)
- Anthology ID: 2023.emnlp-main.293 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. SiMT (Simultaneous machine translation)에서는 높은 품질의 번역 모델과 함께 강력한 read/write 정책이 필요한데, 기존 방법들은 고정된 wait-k 정책과 wait-k 번역 모델을 사용하거나, 번역 모델과 연계하여 adaptive policy를 훈련시키지만 더 유연한 접근 방식을 제안한다.
    2. 이 연구에서는 향후 정보로 인해 발생하는 번역 분포의 다양성을 기반으로 어떤 번역 모델에 대한 read/write 결정을 내리는 DaP(Divergence-based Adaptive Policy)를 소개한다.
    3. 실험 결과는 DaP가 번역 정확도와 지연 시간 간의 개선된 균형을 제공하며 강력한 기준 모델을 능가한다는 것을 보여준다.

###### Cross-Document Event Coreference Resolution on Discourse Structure (https://aclanthology.org/2023.emnlp-main.294/)
- Anthology ID: 2023.emnlp-main.294 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Cross-document event coreference resolution (CD-ECR)은 여러 개의 문서에서 동일한 실제 이벤트를 참조하는 이벤트 언급을 군집화하는 작업이다. 
    2. 기존 연구들은 주로 pair-wise 유사도 비교 문제로 모델링하고 이벤트 언급의 지역적인 문맥을 고려하며 장거리 이벤트 언급의 상호작용을 무시했다. 
    3. 본 논문에서는 글로벌 정보로서 담론 구조를 활용하여 CD-ECR을 개선하고, tree 구조와 shortest dependency path를 사용하여 이벤트 언급의 유사도를 캡처하여 coreferent 이벤트를 해결하는 모델을 제안한다.

###### Post-hoc Utterance Refining Method by Entity Mining for Faithful Knowledge Grounded Conversations (https://aclanthology.org/2023.emnlp-main.295/)
- Anthology ID: 2023.emnlp-main.295 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 언어 생성 모델은 뛰어난 성능을 보이지만, 생성된 응답은 주어진 소스에 부합하지 않거나 사실에 어긋나는 환상적인 담화로 인해 고질적인 문제가 있다.
    2. REM은 소스 지식을 기반으로 생성된 환상적인 발언의 품질과 신뢰성을 향상시키기 위해 후처리 시스템을 제안한다.
    3. REM은 주어진 지식에서 주요 엔티티를 추출하여 환상을 수정함으로써 발언의 품질을 개선하는 것을 목표로 한다고 제안한 방법이다.

###### Can We Edit Factual Knowledge by In-Context Learning? (https://aclanthology.org/2023.emnlp-main.296/)
- Anthology ID: 2023.emnlp-main.296 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 초대형 언어 모델은 매개변수에 거대한 사실 지식을 보유하고 있지만, 이러한 지식은 잘못된 정보나 오래된 정보일 수 있다. 
    2. 이 논문에서는 gradient 기반의 방법이 아닌 in-context learning (ICL)을 활용하여 지식 편집을 수행하는 방법을 제안한다.
    3. 실험 결과, ICL 기반의 지식 편집은 gradient 기반 방법과 비교해 성능은 비슷하지만, 관련 없는 사실에 대한 수정과 이전에 저장된 지식에 대한 잊어버리기가 적은 부작용을 가지고 있다.

###### EDIS: Entity-Driven Image Search over Multimodal Web Content (https://aclanthology.org/2023.emnlp-main.297/)
- Anthology ID: 2023.emnlp-main.297 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실제 검색 엔진 결과와

###### GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints (https://aclanthology.org/2023.emnlp-main.298/)
- Anthology ID: 2023.emnlp-main.298 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Multi-query attention(MQA)은 시간을 크게 단축시키지만, 품질 저하의 문제를 야기할 수 있고, 빠른 추론을 위해 별도의 모델을 훈련시키는 것이 원하는 바가 아닐 수 있다. 
    2. 이 논문에서는 기존의 다양한 헤드를 사용하는 언어 모델 체크포인트를 5%의 원래 pre-training compute만을 사용하여 MQA를 사용하는 모델로 업 트레이닝하기 위한 방법을 제안한다.
    3. 또한, 여러 개의 쿼리 헤드 수보다는 적은 개수의 중간 (intermediate) 키-값 헤드를 사용하는 GQA라는 새로운 기법을 도입하고, GQA로 업 트레이닝된 모델이 MQA와 속도가 비교 가능하면서 품질도 유사하게 달성됨을 보여준다.

###### Towards a Mechanistic Interpretation of Multi-Step Reasoning Capabilities of Language Models (https://aclanthology.org/2023.emnlp-main.299/)
- Anthology ID: 2023.emnlp-main.299 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 연구에서는 언어 모델이 다단계 추론 작업에 강력한 능력을 가지고 있다는 것을 보였으나, 사전 훈련된 코퍼스에서 기억한 답을 이용하여 이러한 작업을 수행한다는 것은 아니라는 사실을 알기 어렵다. 
    2. 본 논문에서는 언어 모델이 정확한 추론 과정과 비슷한 추론 트리를 내재적으로 담고 있는지를 탐구함으로써 이 질문에 답하려고 한다. 
    3. MechanisticProbe라는 새로운 접근법을 사용하여 추론 트리를 모델의 어태션 패턴으로 복원하는 실험을 진행하였고, 이를 통해 언어 모델이 많은 경우에 아키텍처 내에서 다단계 추론 과정을 거친다는 결론을 도출하였다.

