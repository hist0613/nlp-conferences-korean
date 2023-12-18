# Korean Three-Line Summarizations of Papers 1487-1586 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Verb Conjugation in Transformers Is Determined by Linear Encodings of Subject Number (https://aclanthology.org/2023.findings-emnlp.300/)
- Anthology ID: 2023.findings-emnlp.300 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer와 같은 딥 아키텍처는 해석하기 어려운 "black-box" 표현으로 비판받을 때가 있다. 
    2. 우리는 인과적 개입 분석을 사용하여 언어적 특징이 일부 선형적이고 해석 가능한 형식으로 표현된다는 것을 보여준다. 
    3. 특히, 우리는 BERT의 동사 활용 능력이 주어의 수에 대한 선형 인코딩에 의존하며, 이는 동사 위치에서 마지막 레이어에서, 특히 주어의 수에 대한 여러 신호가 있는 경우 중간 레이어에서 위치별로 분산된다는 것을 보여준다.

###### MUX-PLMs: Data Multiplexing for High-throughput Language Models (https://aclanthology.org/2023.findings-emnlp.301/)
- Anthology ID: 2023.findings-emnlp.301 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT와 Bard와 같은 대규모 언어 모델의 널리 퍼짐은 이러한 기술에 대한 전례 없는 수요를 불러왔다. 하지만 점점 커지는 모델 크기에 따라 증가하는 추론 비용과 하드웨어 부족은 접근성을 제한하고, 고효율을 위한 효율 접근 방식이 절실하게 필요하다. 
    2. 여러 개의 입력 및 출력 (MIMO) 알고리즘은 데이터 다중화와 같은 방법을 통해 신속한 처리량의 수행을 통해 한 입력의 비용으로 여러 개의 입력에 대한 추론이 가능한 해결책을 제공한다. 그러나 현재 이러한 방법은 현대적 시스템에 배포하기에 충분히 효율적이지 않다. 
    3. 우리는 MUX-PLMs라는 클래스의 고처리량 사전 훈련 언어 모델 (PLMs)을 개발하여 원하는 하위 작업에 대해 고처리량 및 고성능을 제공하기 위해 데이터 다중화와 함께 훈련할 수 있다. 우리의 신규 다중화 및 복구 모듈은 입력을 효과적으로 혼합하고 분리하여 vanilla PLMs와 경쟁력이 있으면서도 1-4 %의 성능 하락만으로도 추론 속도를 2배/5배 향상시킬 수 있는 MUX-PLMs를 제공한다.

###### That was the last straw, we need more: Are Translation Systems Sensitive to Disambiguating Context? (https://aclanthology.org/2023.findings-emnlp.302/)
- Anthology ID: 2023.findings-emnlp.302 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 모호한 텍스트의 번역은 번역 시스템에 동떨어진 문맥을 가능한 한 명확하게 하는 도전적인 과제이다.
    2. 이전 연구들은 언어 특징에 따른 문법적 모호성에 주목해 왔으나, 이 논문에서는 영어 원문 자체에서 나타나는 의미적 모호성에 초점을 맞춘다.
    3. 기존 MT 모델들은 문맥이 비유적 해석을 시사하는 경우에도 영어 관용구를 일관되게 독자적으로 번역하나, LMs는 문맥에 대해 훨씬 더 인식하며 대상 언어에 따라 성능 격차가 남아있다는 결론을 얻었다. LMs은 context-aware translation을 위한 강력한 기반이 될 수 있다.

###### MindGames: Targeting Theory of Mind in Large Language Models with Dynamic Epistemic Modal Logic (https://aclanthology.org/2023.findings-emnlp.303/)
- Anthology ID: 2023.findings-emnlp.303 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. '이해의 이론'은 지능의 중요한 구성 요소이지만, 그 평가는 아직 많은 논란의 대상이다.
    2. 이전 연구에서는 인공지능 모델에 인간 창의/Perspective of intelligence (ToM)을 적용하기 위해 인간이 만든 표준화된 테스트나 규칙 기반의 템플릿을 사용했다.
    3. 이 논문에서는 ToM의 특정 구성 요소를 분리하기 위해 동적 지식 로직을 활용하고, 이러한 문제를 영어로 표현하기 위해 새로운 언어 표현 기법을 소개한다.

###### LATENTLOGIC: Learning Logic Rules in Latent Space over Knowledge Graphs (https://aclanthology.org/2023.findings-emnlp.304/)
- Anthology ID: 2023.findings-emnlp.304 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프 추론을 위한 논리 규칙 학습은 해석 가능한 설명과 다양한 도메인에 일반화가 가능하다는 장점이 있지만, 기존 방법들은 거대한 탐색 공간에서 검색하는 것이 어렵고, 비효율적인 최적화 기법이 사용된다는 어려움이 있다.
    2. 이 논문에서는 LatentLogic이라는 새로운 프레임워크를 제안하여 잠재 공간에서 규칙을 생성함으로써 논리 규칙을 효율적으로 발견하는 방법을 소개한다.
    3. 벤치마크 데이터셋에 대한 실험 결과, 제안한 방법의 효과와 효율성을 입증하였다.

###### RobustEmbed: Robust Sentence Embeddings Using Self-Supervised Contrastive Pre-Training (https://aclanthology.org/2023.findings-emnlp.305/)
- Anthology ID: 2023.findings-emnlp.305 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(PLM)은 다양한 자연어 처리 태스크에서 우수한 성능을 보여주었지만, 새로운 샘플에 대해 일반화가 잘 되지 않고 적대적인 시나리오에서의 견고성이 부족하다. 
    2. 이 논문에서는 RobustEmbed라는 자기 지도 학습 문장 임베딩 프레임워크를 제안하여 다양한 텍스트 표현 과제에서의 일반화와 적대적 공격에 대한 견고성을 강화한다.
    3. 실험 결과는 RobustEmbed가 적대적 상황에서 이전 최고 성능 모델보다 우수한 성능을 보인다는 것을 확인하였으며, 의미적 텍스트 유사성(STS) 태스크와 전이 태스크에서도 상대적인 개선을 나타냈다.

###### More than Votes? Voting and Language based Partisanship in the US Supreme Court (https://aclanthology.org/2023.findings-emnlp.306/)
- Anthology ID: 2023.findings-emnlp.306 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 미국 대법원에서 공정성에 대한 정당성과 이념의 유통성과 역학을 이해하는 것은 법관구역 연구를 위해 중요하다. 
    2. 이 논문에서는 대법원 변론에서 법관들의 언어 분석을 통해 정당 선호도를 연구하고, 이를 투표 패턴과의 일치와 비교한다. 
    3. 결과적으로, 법관들의 언어적 정당성과 투표 이념 사이에 강한 상관관계가 있다는 것을 보였다.

###### Automatic Evaluation of Attribution by Large Language Models (https://aclanthology.org/2023.findings-emnlp.307/)
- Anthology ID: 2023.findings-emnlp.307 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델 (LLM) 개발은 외부 참조를 통해 생성된 문장의 근거를 생성하고 지원하는 것에 초점을 맞추고 있다. 하지만 생성된 문장이 인용된 참조에 완전히 의해 지지되는지를 검증하는 attribution 평가는 여전히 미해결된 문제이다.
    2. 이 논문에서는 LLM이 제공한 attribution을 자동 평가하는 두 가지 접근 방법을 탐구한다. 첫째, LLM을 prompt시켜서 평가하는 방법과, 둘째, 작은 크기의 LLM을 fine-tuning시켜서 평가하는 방법을 사용한다.
    3. 우리는 generative search engine인 New Bing의 12개 도메인으로 구성된 테스트 샘플을 수동으로 준비하여, 이러한 중요한 문제에 대한 미래 연구의 기반을 마련하기 위한 문제 정의, 테스트 베드 및 결과를 제공한다.

###### Modeling Highlighting of Metaphors in Multitask Contrastive Learning Paradigms (https://aclanthology.org/2023.findings-emnlp.308/)
- Anthology ID: 2023.findings-emnlp.308 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "시간을 함께 보내다"와 같은 은유적인 언어는 의미를 돈(source domain)에서 시간(target domain)으로 옮기며, 이를 통해 시간 투자의 노력과 같은 특정 측면을 강조한다. 이 논문에서는 은유적인 문장에서 강조된 주요 측면을 식별하는 작업을 소개하고, 강조된 측면과 소스 도메인을 함께 예측하는 다중 작업 접근 방식을 제안한다.
    2. 소스 도메인과 강조된 측면 간의 상호작용을 고려하여, 사전 훈련된 대조 학습 모델을 기반으로 한 공동 학습 접근 방식과 지속적 학습 접근 방식을 제안한다.
    3. 실험 결과는 소스 도메인에 대한 정보가 강조된 측면을 예측하는 데 더 나은 성능을 발휘하며, 그 반대의 경우도 마찬가지라고 보여주었다.

###### LDM2: A Large Decision Model Imitating Human Cognition with Dynamic Memory Enhancement (https://aclanthology.org/2023.findings-emnlp.309/)
- Anthology ID: 2023.findings-emnlp.309 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)의 빠른 발전에 따라 인공 일반 지능을 가능하게 하기 위해 LLM을 사용하여 결정을 내릴 수 있는 요구가 높아졌다. 여러 기존 방법들은 사람의 결정 과정을 모방하도록 LLM을 촉발시키기 위해 수동으로 제작된 예제를 활용한다. 
    2. 그러나 최적의 프롬프트를 설계하는 것은 어렵고 패턴화된 프롬프트는 더 복잡한 환경에 일반화되기 어렵다. 
    3. 본 논문에서는 LDM2라는 새로운 모델을 제안한다. 이 모델은 동적 메모리 메커니즘을 활용하여 동적 프롬프트를 구성하고, 현재 상태에 따라 LLM을 적절한 결정을 내리도록 안내한다. 두 단계로 구성된 LDM2는 인간의 행동을 LLM의 강력한 요약 능력을 활용하여 상태-액션 튜플로 분해하여 메모리에 저장하고, 현재 상태를 기반으로 가장 관련있는 일부 튜플을 검색할 수 있도록 LLM에 의해 생성된 인덱스로 이루어진 메모리를 사용한다. 이후, LDM2은 더 적합한 결정 과정을 발견하고 가치 있는 상태-액션 튜플을 추가하여 메모리를 보강하기 위해 트리 탐색을 사용한다. 탐색과 메모리 강화의 동적 순환은 LDM2가 전역 환경을 더 잘 이해할 수 있게 한다.

###### ZARA: Improving Few-Shot Self-Rationalization for Small Language Models (https://aclanthology.org/2023.findings-emnlp.310/)
- Anthology ID: 2023.findings-emnlp.310 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. end-task 답변과 자유로운 텍스트 설명을 동시에 생성하는 언어 모델 (LM)을 self-rationalization 모델이라고 하는데, 최근의 연구에서는 rationale이 포함된 예시로 few-shot prompting LMs를 사용하여 self-rationalization의 큰 성능 향상을 보였다.
    2. 그러나 이러한 설명을 활용하는 능력은 대규모 LMs에만 나타나며, 접근성이 낮은 것으로 알려져 있다.
    3. 이 논문에서는 작은 LMs에 대한 설명 활용을 탐구하며, plausibility judgment 문제를 자연 언어 추론으로 감소시킴으로써 자가 교육을 위한 pseudo-parallel 데이터를 자동으로 구성하는 ZARA라는 새로운 접근 방식을 제안한다.

###### ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversation (https://aclanthology.org/2023.findings-emnlp.311/)
- Anthology ID: 2023.findings-emnlp.311 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화형 AI 모델들은 최근 많은 발전을 보였지만, 비독성 사용자-인공지능 상호작용 환경 유지는 점점 중요해지고 있다. 그러나 이전 연구들은 대부분 소셜미디어 콘텐츠에서 파생된 벤치마크에 기반해 왔으며, 실제 사용자-인공지능 상호작용에서의 독특한 도전들은 충분히 탐구되지 않아왔다.
    2. 본 연구에서는 오픈소스 챗봇의 실제 사용자 질문을 기반으로 한 새로운 벤치마크인 ToxicChat을 소개한다. 이 벤치마크는 현재 독성 감지 모델에게 어려움을 줄 수 있는 다양하고 미묘한 현상을 포함하고 있으며, 소셜미디어 콘텐츠와 비교할 때 상당한 도메인 차이를 보여준다.
    3. 기존 독성 데이터셋으로 학습된 모델들을 ToxicChat에 적용한 결과, 그들의 한계점이 드러났다. 이 연구는 실제 사용자-인공지능 대화에서 독성 감지의 잠재적으로 간과되는 도전들을 밝혀주며, ToxicChat은 사용자-인공지능 상호작용에 안전하고 건전한 환경을 구축하기 위한 추가적인 발전을 이끌기 위한 가치 있는 자원이 될 수 있다.

###### Mind the Gap: Automated Corpus Creation for Enthymeme Detection and Reconstruction in Learner Arguments (https://aclanthology.org/2023.findings-emnlp.312/)
- Anthology ID: 2023.findings-emnlp.312 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 강한 주장을 작성하는 것은 학습자에게 어려울 수 있으며, 학습자들은 논증을 이해하기 어려울 수 있다. 이 논문에서는 학습자의 주장에 빠진 ADU(Argumentative Discourse Unit)가 있는지 감지하고 채우는 두 가지 새로운 작업을 소개한다.
    2. 확립하지 않은 ADU의 부재는 논리적 흐름을 이해하지 못하게 만들 수 있다. 학습자의 인수의 질을 향상시키기 위해 이러한 작업들을 연구한다.
    3. ICLEv3 corpus에서 ADU를 삭제하여 감소시키는 방식으로 인수의 부재를 감지하고 복원하는 작업을 자동으로 수행하는 방식을 제시하였으며, 이를 통해 다양한 baseline 접근 방식을 검토하였다.

###### Dior-CVAE: Pre-trained Language Models and Diffusion Priors for Variational Dialog Generation (https://aclanthology.org/2023.findings-emnlp.313/)
- Anthology ID: 2023.findings-emnlp.313 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 변분 대화 모델은 사전 훈련된 언어 모델을 사용하여 가능도 및 사후 분포를 파라미터화하였다. 그러나 사전 분포에 대한 가우시안 가정은 이러한 분포와 호환되지 않으므로 생성된 응답의 다양성을 제한한다.
    2. 이 논문에서는 이러한 도전에 대처하기 위해 확산 사전을 사용하는 계층적 조건부 변분 오토인코더(CVAE)인 Dior-CVAE를 제안한다. 우리는 확산 모델을 사용하여 사전 분포의 복잡성을 증가시키고, PLM에 의해 생성된 분포와의 호환성을 확보한다.
    3. 또한, 우리는 응답 생성을 위해 latent 변수의 사용을 적극적으로 장려하기 위해 cross-attention 메커니즘에 메모리 드롭아웃을 제안한다. 실험 결과, 대화 사전 훈련 없이도 더 다양한 응답을 생성할 수 있는 것을 보여주었다.

###### Retrieving Multimodal Information for Augmented Generation: A Survey (https://aclanthology.org/2023.findings-emnlp.314/)
- Anthology ID: 2023.findings-emnlp.314 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large Language Model, LLM)이 인기를 얻으면서, 다양한 형태의 지식을 활용하여 LLM의 생성 능력을 향상시키는 것이 중요한 동향이 되었지만, 어떤 단계에서 어떻게 다양한 형태의 모달리티를 통합해야 하는지에 대한 통일된 인식이 부족하다.
    2. 이 논문에서는 이미지, 코드, 테이블, 그래프, 오디오와 같은 형태의 다중모달 지식을 검색하여 생성 모델을 보조하고 향상시키는 방법을 조사한다. 이러한 방법들은 사실성, 추론, 해석 가능성, 강건성과 같은 중요한 문제에 대한 유망한 해결책을 제공한다.
    3. 이 조사를 통해 기존 기법을 LLM 분야에 적용하기 위해 스칼라들에게 깊은 이해를 제공하고 그 응용 방법에 대한 이해를 높여줄 것으로 기대된다.

###### Improving Contrastive Learning of Sentence Embeddings with Focal InfoNCE (https://aclanthology.org/2023.findings-emnlp.315/)
- Anthology ID: 2023.findings-emnlp.315 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. SimCSE의 원래 공식은 contrastive learning에서 hard negative 샘플의 잠재력을 충분히 활용하지 못한다. 
    2. 이 연구는 SimCSE와 hard negative mining을 결합한 비지도형 contrastive learning 프레임워크를 소개하여 문장 임베딩의 품질을 향상시키고자 한다. 
    3. 다양한 STS 벤치마크에서의 실험결과, 우리의 방법은 Spearman 상관관계 및 표현 정렬 및 일관성의 관점에서 문장 임베딩을 개선시킨다.

###### The Vault: A Comprehensive Multilingual Dataset for Advancing Code Understanding and Generation (https://aclanthology.org/2023.findings-emnlp.316/)
- Anthology ID: 2023.findings-emnlp.316 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "The Vault"은 여러 프로그래밍 언어로 된 고품질 코드-텍스트 쌍의 오픈소스 데이터셋으로, 대용량 언어 모델이 코드를 이해하고 생성하는 데 사용된다. 
    2. 이 논문에서는 규칙과 딥러닝을 사용하여 고품질의 코드-텍스트 쌍을 추출하는 방법을 제안하고, 결과적으로 4300만 개의 고품질 코드-텍스트 쌍 데이터셋을 구축했다. 
    3. 이 데이터셋을 사용하여 다양한 코드 언어 모델을 학습시킬 때 다른 데이터셋보다 우수한 성능을 보이며, 코드 생성, 코드 요약, 코드 검색과 같은 일반적인 코딩 작업에 활용될 수 있다.

###### SDOH-NLI: a Dataset for Inferring Social Determinants of Health from Clinical Notes (https://aclanthology.org/2023.findings-emnlp.317/)
- Anthology ID: 2023.findings-emnlp.317 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "건강결과에 영향을 주는 사회적 및 행동적 결정인자(SDOH)는 건강관리자가 적절한 치료 기회를 식별하고 격차를 해소하기 위해 체계적으로 식별할 수 있도록 돕는 첫 번째 단계이다. 그러나 진전은 실제 환자 정보의 개인정보 및 규제 제약으로 인해 공개적으로 사용 가능한 고품질 레이블 데이터 부족으로 지체되고 있다. 본 논문에서는 공개적으로 사용 가능한 기록을 기반으로하는 새로운 데이터 세트인 SDOH-NLI를 소개하고 공개한다."
    2. "우리는 SDOH 추출을 자연어 추론(natural language inference) 작업으로 정의하고, 사회적인 이력 스니펫과 SDOH 요소의 교차 제품을 가정으로하는 바이너리 텍스트 함의 레이블을 인간 평가자에서 얻었다."
    3. "우리는 "off-the-shelf" 함의 모델뿐만 아니라 우리의 데이터로 fine-tuning한 모델을 평가하고, 우리의 데이터 세트가 일반적으로 사용되는 NLI 데이터 세트보다 어려운 점을 강조한다."

###### On the Zero-Shot Generalization of Machine-Generated Text Detectors (https://aclanthology.org/2023.findings-emnlp.318/)
- Anthology ID: 2023.findings-emnlp.318 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간이 쓴 텍스트와 구별하기 힘든 정도로 자연스러운 큰 언어 모델들의 만연 현상은 기계 생성 텍스트의 탐지를 전례 없이 중요하게 한다.
    2. 이 논문은 중요한 연구 질문으로 진행되며, 기계 생성자가 훈련되지 않은 새로운 생성자 출력에서 기계 생성 텍스트 탐지기의 성능이 어떻게 나올지 알아보고 있다.
    3. 실험 결과로는 모든 탐지기가 일반화되지는 않지만, 중간 크기 모델의 데이터로 훈련된 탐지기가 큰 버전에 대해 제로샷(zero-shot) 일반화가 가능하다는 일관된 흥미로운 패턴을 관찰할 수 있었다.

###### Complex Event Schema Induction with Knowledge-Enriched Diffusion Model (https://aclanthology.org/2023.findings-emnlp.319/)
- Anthology ID: 2023.findings-emnlp.319 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 복잡한 이벤트 스키마의 개념은 이벤트와 그들의 다차원적인 관계를 나타내는 그래프 구조를 가리키며, 그러나 이전의 이벤트 스키마 인덕션 연구는 오류 전파와 데이터 품질 문제로 인해 어려움을 겪었습니다.
    2. 이러한 도전에 대응하기 위해, 우리는 지식-풍부한 이산확산 모델을 제안합니다. 우리는 대용량 언어 모델(Large Language Models, LLMs)의 풍부한 이벤트 시나리오 지식을 파이썬 스타일의 prompt를 통해 추출하여 훈련 데이터에 통합시킵니다. 
    3. 또한, 오류 전파 문제를 해결하기 위해 자기회귀적이지 않은 방식으로 이산확산 과정을 사용하여 동시에 모든 노드와 링크를 생성하고, 이벤트 아규먼트 간의 entity relationship 예측 모듈을 개발합니다. 실험 결과, 우리의 접근 방식은 다양한 평가 메트릭에서 뛰어난 성능을 달성합니다.

###### Exploiting Emotion-Semantic Correlations for Empathetic Response Generation (https://aclanthology.org/2023.findings-emnlp.320/)
- Anthology ID: 2023.findings-emnlp.320 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "공감 대화 생성은 대화의 언어에서 발화자의 감정을 이해하여 공감적인 응답을 생성하는 것을 목표로 한다. 하지만 최근 연구들은 감정 단어들을 정적인 벡터로만 취급하여 세밀한 감정을 파악하기 어렵게 한다. 그래서 우리는 감정 단어들이 문법 의미론적인 다른 역할과 상관관계를 가지고 있다고 보고, 문맥과 감정의 상호작용을 통해 동적인 감정-의미 벡터를 생성하는 모델을 제안한다."
    2. "우리의 모델은 문맥과 감정의 상호작용을 반영하기 위해 의존성 트리를 도입하고, 동적인 감정-의미 벡터와 의존성 트리를 기반으로 다이내믹한 상관 그래프 합성곱 신경망을 제안한다."
    3. "실험 결과, 우리의 모델은 문맥과 감정을 더 정확하게 이해하고 유창하고 정보가 풍부한 공감적인 응답을 생성한다. 또한, 분석 결과는 감정과 의미 사이의 상관관계가 대화에서 자주 사용되며, 공감적 지각과 표현에 큰 의미가 있다는 것을 보여준다."

###### Long-Range Language Modeling with Selective Cache (https://aclanthology.org/2023.findings-emnlp.321/)
- Anthology ID: 2023.findings-emnlp.321 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 트랜스포머 기반 언어 모델은 시퀀스 길이에 따라 계산 비용이 제곱으로 증가한다. 그러므로 이 연구에서는 이전 문맥으로부터 선택적으로 중요한 key-value 쌍을 저장하는 셀렉티브 캐시를 도입하였다. 이 캐시를 잘 활용함으로써 한정된 캐시 크기 내에서 더 긴 문맥 이력을 저장할 수 있게 되었다.
    2. 사람의 언어 처리 실험을 통해 fixated token에 대응하는 key-value 쌍을 선택하여 셀렉션하는 첫 번째 방법을 설계하였다. 또한, 이러한 인지적인 선택 프로세스를 훈련 가능한 과정으로 언어 모델에 통합하여 성능을 개선했다.
    3. 제안된 셀렉티브 캐시는 다양한 데이터셋에서 언어 모델링 성능을 향상시키는 것을 입증하였다. 동일한 저장된 key-value 쌍(캐시 크기)으로 비교했을 때, 셀렉티브 캐시는 XL 캐시와 압축 캐시보다 상당한 차이로 우수한 결과를 보였다.

###### Medical Text Simplification: Optimizing for Readability with Unlikelihood Training and Reranked Beam Search Decoding (https://aclanthology.org/2023.findings-emnlp.322/)
- Anthology ID: 2023.findings-emnlp.322 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의학 분야에서의 텍스트 간소화는 기술 용어와 복잡한 구조로 인해 의사소통을 개선하는 데 더욱 유용한 AI 응용 프로그램으로 등장했으나, 의학 간소화 방법은 생성된 텍스트의 품질과 다양성이 낮을 수 있다.
    2. 이 연구에서는 의료 분야에서 텍스트 간소화의 읽기 가능성을 더욱 향상시키기 위한 방법을 탐색한다.
    3. 우리는 (1) 간소한 용어 생성을 장려하는 새로운 비실제손실, (2) 단순성을 최적화하는 재순위 빔 서치 디코딩 방법을 제안하였으며, 세 개의 데이터셋에서 가독성 측정 지표에서 더 좋은 성능을 달성한다.

###### FaLA: Fast Linear Adaptation for Replacing Backbone Models on Edge Devices (https://aclanthology.org/2023.findings-emnlp.323/)
- Anthology ID: 2023.findings-emnlp.323 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 비정상적인 On-device 시나리오에서 개인화된 다운스트림 작업을 위한 언어 모델 백본 교체 문제를 연구한다.
    2. 기존의 전체 모델 튜닝이나 전이 학습은 로컬 디바이스의 훈련 비용을 상당히 소모하고, 심층 변환기 레이어 내에서 광범위한 역전파를 요구한다. 
    3. 이 문제를 해결하기 위해 우리는 백본 교체 후 개인화된 NLP 분류 작업을 위한 경량화된 튜닝 방법을 제안한다. 이 방법은 사용자의 이전 및 새로운 백본에 해당하는 문서에서 계산된 개인화된 행렬을 활용하여 상위 레이어 매개변수 튜닝을 수행하고, 역전파 계산을 크게 줄인다.

###### Intuitive Multilingual Audio-Visual Speech Recognition with a Single-Trained Model (https://aclanthology.org/2023.findings-emnlp.324/)
- Anthology ID: 2023.findings-emnlp.324 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 음성-시각 인식 작업에 대한 신규 접근법을 제시하여, 멀티리근 데이터셋에서 단일 모델을 소개한다. 인간의 인지 체계에서 사람들은 어떠한 의식적인 노력이나 안내 없이도 다른 언어를 직관적으로 구별할 수 있는데, 이런 특성을 반영하여 언어들 사이의 내재적인 유사성과 차이를 구별하는 모델을 제안한다. 
    2. 우리는 대부분 사전 훈련된 음성-시각 표현 모델에 prompt fine-tuning 기술을 도입하여 네트워크가 언어 분류와 해당 언어로 된 음성을 인식할 수 있도록 한다.
    3. 우리의 연구는 강건하고 효율적인 다국어 음성-시각 인식 시스템을 개발하는 데 기여하며, 언어별 모델의 필요성을 줄인다.

###### Controllable Chest X-Ray Report Generation from Longitudinal Representations (https://aclanthology.org/2023.findings-emnlp.325/)
- Anthology ID: 2023.findings-emnlp.325 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "방사선학 보고서는 의료 검사 결과의 세부 텍스트 설명이다. 각 보고서는 관련 임상 소견의 존재/부재와 위치를 기술하며, 보통 같은 환자의 이전 검사와 비교하여 진화하는 과정을 설명한다. 자동 보고 시스템을 통합하여 보고 속도를 높이는 전략 중 하나는 있으나, 임상 적합성을 위해서는 높은 정확성과 해석 가능성이 필요하다."
    2. "기존의 방사선학 자동 보고 접근 방식은 대체로 이전 검사를 입력으로 제공하지 않아 일부 유형의 검사에서 필요한 비교를 할 수 없으며, 해석 가능성에 불신불명의 방법만 제공한다."
    3. "이 논문에서는 기존의 해부학 토큰을 이용한 시각적 입력 형식을 활용하여 (1) 종단적인 표현 학습 - 이전 검사를 추가 입력으로 활용하여 현재와 이전의 시각적 정보를 합쳐서 보고서 생성 모델에 제공하는 방법을 제안하고, (2) 문장-해부학 dropout - 원본 보고서의 문장 중 입력으로 제공된 해부학 영역에 해당하는 문장만을 예측하도록 모델을 훈련시키는 훈련 전략을 소개한다. MIMIC-CXR 데이터셋을 활용한 실험을 통해 제안된 접근 방식이 최고 수준의 결과를 달성하면서 해부학별 제어 가능한 보고서 생성을 가능케 한다."

###### Is ChatGPT a Good Multi-Party Conversation Solver? (https://aclanthology.org/2023.findings-emnlp.326/)
- Anthology ID: 2023.findings-emnlp.326 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델(LLMs)은 자연어 처리 분야에서 영향력 있는 도구로 등장했지만, 복잡한 정보 교환을 포함하는 다자간 대화(MPCs)를 처리하는 능력은 아직 알려지지 않았다.
    2. 본 논문에서는 ChatGPT와 GPT-4와 같은 생성형 LLMs의 MPC에서의 잠재력을 탐구하고, 세 가지 MPC 데이터셋에서 다섯 가지 대표적인 작업을 기반으로 평가하여 제로샷 학습 능력을 분석한 연구를 수행한다.
    3. 연구 결과, ChatGPT는 여러 MPC 작업에서 성능이 좋지 않았지만 GPT-4의 결과는 향후 유망한 미래를 보여준다. 또한, 발화자와 수신자 아키텍처를 포함한 MPC 구조를 도입하여 성능을 향상시켰다. 이 연구는 생성형 LLMs를 MPC에 적용하는 평가와 분석을 제공하며, 효과적이고 강건한 MPC 에이전트의 개발과 창조에 빛을 비추고 있다.

###### Improving End-to-End Speech Processing by Efficient Text Data Utilization with Latent Synthesis (https://aclanthology.org/2023.findings-emnlp.327/)
- Anthology ID: 2023.findings-emnlp.327 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 레이블이 달린 음성 데이터는 텍스트 데이터에 비해 적고 비용이 많이 들기 때문에, 우리는 E2E 음성 처리 모델을 위한 효율적인 텍스트 데이터 활용 프레임워크인 Latent Synthesis (LaSyn)을 제안한다.
    2. LaSyn은 텍스트 데이터를 사전 훈련된 음성 모델의 중간 잠재 표현인 음성 표현으로 변환하기 위해 잠재 합성기를 훈련시키고, 이를 통해 텍스트 데이터를 음향 데이터로 보강하여 모델을 훈련한다.
    3. 실험 결과, LaSyn은 저자원 자동음성인식 (ASR) 및 구술언어이해 (SLU) 작업에서 종래와 비교하여 음성 모델의 성능을 크게 향상시킬 수 있다는 것을 보여준다.

###### Bipartite Graph Pre-training for Unsupervised Extractive Summarization with Graph Convolutional Auto-Encoders (https://aclanthology.org/2023.findings-emnlp.328/)
- Anthology ID: 2023.findings-emnlp.328 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 문장 표현은 비지도 문서 추출 요약에서 중요한 문장을 식별하는 데 중요하다. 그러나 사전 훈련 및 문장 순위 매기기의 전통적인 두 단계 패러다임은 서로 다른 최적화 목표 때문에 격차가 발생한다.
    2. 따라서 우리는 정보를 최적화하고 구별할 수 있는 문장 표현을 얻기 위해 specifically designed to optimize informative and distinctive sentence representations를 사용하는 것이 중요하다고 주장한다.
    3. 우리의 방법은 사전 훈련된 그래프 오토 인코더를 제안하여 문장-단어 일대다 그래프를 통해 문장의 내부적인 특징과 문장 간의 일관된 특징을 명시적으로 모델링하여 문장 임베딩을 얻는다. 이러한 세부 조정된 문장 임베딩은 비지도 요약을 위한 그래프 기반 순위 알고리즘에서 사용된다.

###### Bayesian Multi-Task Transfer Learning for Soft Prompt Tuning (https://aclanthology.org/2023.findings-emnlp.329/)
- Anthology ID: 2023.findings-emnlp.329 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Prompt 튜닝은 대규모 사전 훈련 언어 모델을 하위 작업에 적용하기 위해 프롬프트를 최적화하는 방식이며, 특히 다중 작업 전이 학습 환경에서 효과적으로 작동한다. 
    2. 그러나 이 방법은 일부 원본 작업들이 서로 부정적이거나 긍정적인 영향을 미칠 수 있다는 사실을 중요하게 간과하고 있다.
    3. 따라서 우리는 소스 태스크로부터 지식을 추출할 때 소스 태스크 사이의 상관 관계를 고려하여 목표 태스크로의 전이를 개선하는 베이지안 접근법을 제안한다.

###### CCIM: Cross-modal Cross-lingual Interactive Image Translation (https://aclanthology.org/2023.findings-emnlp.330/)
- Anthology ID: 2023.findings-emnlp.330 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 급부 상황으로 “Text image machine translation (TIMT)”은 원본 언어 텍스트 이미지를 대상 언어 텍스트로 변환하는 작업에 큰 주목을 받는다. 
    2. 기존 모델들은 호환성 저하로 인해 원본 언어 정보를 부여하기 어렵기 때문에 번역 성능이 저하되었으며, 이를 해결하기 위해 우리는 Cross-modal Cross-lingual Interactive Model (CCIM)을 제안한다. 
    3. 다양한 실험 결과를 통해, CCIM이 기존 모델보다 성능이 향상되었고, 작은 모델 크기로 빠른 디코딩 속도를 가진 것을 확인할 수 있었다.

###### TRAMS: Training-free Memory Selection for Long-range Language Modeling (https://aclanthology.org/2023.findings-emnlp.331/)
- Anthology ID: 2023.findings-emnlp.331 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer 아키텍처는 여러 AI 모델에 필수적이지만, 특히 long-range 언어 모델링에서는 여전히 도전을 겪고 있다.
    2. 이 연구에서는 TRAining-free Memory Selection (TRAMS)라는 전략을 소개하는데, 이는 attention 계산에 참여하는 토큰을 간단한 메트릭을 기반으로 선택한다.
    3. TRAMS 전략을 테스트한 결과, 추가적인 학습이나 파라미터 추가 없이도 성능이 향상된다는 것을 보여주었다.

###### A Critical Analysis of Document Out-of-Distribution Detection (https://aclanthology.org/2023.findings-emnlp.332/)
- Anthology ID: 2023.findings-emnlp.332 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 사전 훈련은 최근 문서 이해 작업에서 많이 사용되지만, 배포 과정에서는 OOD (out-of-distribution) 샘플을 만나면 보수적인 fallback 정책을 활성화해야 한다고 기대된다. 
    2. 이 논문에서는 문서는 다중 모달로 구성되어 있지만, 기존의 OOD 탐지 방법은 이미지나 텍스트와 같은 단일 모달 입력에만 초점을 맞추고 있다. 
    3. 그렇기 때문에 우리는 문서 OOD 탐지를 위해 공간 정보를 활용하는 spatial-aware adapter를 제안하고, 실험 결과 이를 사용하면 경쟁적인 기준에 비해 우수한 성능을 달성할 수 있다는 것을 보여주었다.

###### Improving Neural Machine Translation by Multi-Knowledge Integration with Prompting (https://aclanthology.org/2023.findings-emnlp.333/)
- Anthology ID: 2023.findings-emnlp.333 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 prompt을 활용한 신경기반 기계 번역(NMT) 시스템의 성능 개선에 큰 진전이 이루어졌는데, 해당 논문은 다양한 종류의 지식(Multi-knowledge)들을 NMT 모델에 효과적으로 통합하여 번역 성능을 향상시키는 방법에 초점을 맞춘다.
    2. 우리는 문장, 용어/구, 번역 템플릿과 같은 다양한 종류의 지식을 NMT 모델에 통합하는 통합 프레임워크를 제안한다.
    3. 실험 결과, 우리의 접근법은 강력한 기준선을 크게 능가하여 고품질 번역과 용어 일치 정확성을 달성하는 것을 보여주었다.

###### Active Learning Principles for In-Context Learning with Large Language Models (https://aclanthology.org/2023.findings-emnlp.334/)
- Anthology ID: 2023.findings-emnlp.334 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델(LLM)은 소수의 라벨링된 예제(데모)만 사용하여 in-context 학습을 통해 주어진 작업을 효과적으로 수행할 수 있다. 그러나 최적의 성능을 위해 데모를 선택하는 과정은 이전 연구에서 제한적으로 다루어졌다.
    2. 이 논문에서는 약간의 주어진 데이터로 가장 효과적인 데모를 식별하기 위해 pool-based Active Learning(AL) 문제로 접근한다. 이를 위해 불확실성, 다양성 및 유사성을 기반으로 한 표준 AL 알고리즘을 비교하고, 유사성 기반 알고리즘이 더 우수한 성능을 보인다는 일관된 결과를 얻는다.
    3. 다양한 GPT 및 OPT 모델을 사용한 24개 분류 및 다중선택 태스크에 대한 광범위한 실험 결과와 철저한 분석을 통해 테스트 예제와 의미적으로 유사한 데모를 사용하는 것의 중요성을 명확히 보여준다. 실제로, GPT-2 (124M)로 "유사한" 데모를 사용할 경우 GPT-Neox (20B)의 무작위 데모보다 높은 평균 분류 성능을 보여준다.

###### InteMATs: Integrating Granularity-Specific Multilingual Adapters for Cross-Lingual Transfer (https://aclanthology.org/2023.findings-emnlp.335/)
- Anthology ID: 2023.findings-emnlp.335 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 언어 모델(MLLMs)들은 다양한 cross-lingual transfer task에서 매우 성공적인 성과를 보여왔으나, 특히 긴 문맥을 다룰 때 zero-shot low-resource 언어에서 성능이 낮다. 
    2. 기존 연구들은 MLLMs의 cross-lingual alignment을 증진시키기 위해 대규모 병렬 데이터셋에서 전체 모델을 fine-tuning하는 방식을 주로 사용하였고, 이는 계산 리소스를 많이 필요로 한다.
    3. 이 논문에서는 다양한 granuality 레벨의 텍스트를 이용하여 pre-train된 다국어 adapter를 통합하는 InteMATs라는 새로운 접근 방법을 제안한다. InteMATs의 효과는 광범위한 실험을 통해 입증되었다.

###### PlugMed: Improving Specificity in Patient-Centered Medical Dialogue Generation using In-Context Learning (https://aclanthology.org/2023.findings-emnlp.336/)
- Anthology ID: 2023.findings-emnlp.336 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 환자 중심의 의료 대화 시스템은 환자에게 특정한 응답을 제공하는 것을 강조함으로써 의료 지식을 덜 알고 있는 사용자에게 진단 해석 서비스를 제공하려고 한다. 
    2. 큰 언어 모델 (LLM)들은 의료 분야에서 일부 업무에서도 높은 성능을 보이지만 응답의 특수성을 보장하는 것은 어렵다. 
    3. 우리는 PlugMed라는 새로운 시스템을 제안하고, 이는 큰 언어 모델에게 실제 대화를 제시함으로써 특정 대화 전략을 강화하고, 적합한 응답을 선택할 수 있도록 한다. 또한 응답의 특수성을 효과적으로 평가하기 위해 새로운 평가 방법을 소개한다.

###### CodeTransOcean: A Comprehensive Multilingual Benchmark for Code Translation (https://aclanthology.org/2023.findings-emnlp.337/)
- Anthology ID: 2023.findings-emnlp.337 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 코드 번역 데이터셋은 한 쌍의 인기있는 프로그래밍 언어에만 초점을 맞추고 있어 실제 응용 프로그램의 다양한 요구 사항을 충족시키지 못합니다. 본 연구에서는 최대한 다양한 프로그래밍 언어를 지원하는 대규모 벤치마크인 CodeTransOcean을 구축하였습니다. 
    2. CodeTransOcean은 다중 유명 프로그래밍 언어 간의 번역을 지원하는 MultilingualTrans, 출처언어 언어와 인기있는 프로그래밍 언어 간의 번역을 지원하는 NicheTrans, 대용량 언어 모델로 번역된 코드의 실행 가능성을 평가하는 LLMTrans 등 세 가지 독창적인 다국어 데이터셋으로 구성되어 있습니다. 
    3. 또한 CodeTransOcean은 딥러닝 코드를 다른 프레임워크로 번역하는 교차 프레임워크 데이터셋인 DLTrans와 함께, 코드 번역을 위한 다국어 모델링 접근 방법을 개발하여 낮은 리소스 언어 쌍과 높은 리소스 언어 쌍의 번역 품질을 향상시키고 훈련 효율성을 향상시킬 수 있는 가능성을 보였습니다.

###### impact of sample selection on in-context learning for entity extraction from scientific writing (https://aclanthology.org/2023.findings-emnlp.338/)
- Anthology ID: 2023.findings-emnlp.338 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)의 프롬프트 기반 사용은 많은 자연어 문제를 해결하는데 점점 더 인기있는 방법이다. 
    2. 이 논문에서는 GPT-3.5를 사용하여 과학 문서로부터 entity 추출을 위한 in-context 샘플 선택 방법에 대한 포괄적인 분석을 제공한다. 
    3. 도메인 종속적인 방법의 효과는 상당히 다르지만, entity 타입이 많은 문제에서 더 유의미한 향상이 있다고 결과에서 나타났다.

###### Goodtriever: Adaptive Toxicity Mitigation with Retrieval-augmented Models (https://aclanthology.org/2023.findings-emnlp.339/)
- Anthology ID: 2023.findings-emnlp.339 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 독성을 완화하는 데 많은 노력을 기울였지만, 기존 방법들은 모델 파라미터의 극단적인 수정이나 계산량이 많은 보조 모델의 사용을 필요로 한다. 
    2. 이전의 접근 방식들은 언어의 변화하는 특성을 무시하는 경향이 있었다.
    3. 이 연구에서는 독성 완화의 현재 상태를 고려하는 포괄적인 관점을 제시하며, Goodtriever라는 유연한 방법론을 소개한다. Goodtriever는 인코딩 시에 검색 기반 접근 방식을 도입하여 독성 제어된 텍스트 생성을 가능하게 한다.

###### Robustness Tests for Automatic Machine Translation Metrics with Adversarial Attacks (https://aclanthology.org/2023.findings-emnlp.340/)
- Anthology ID: 2023.findings-emnlp.340 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 전략적으로 만들어진 텍스트에 대한 기계 번역 평가 메트릭의 성능을 조사하여 메트릭의 강인성을 밝힌다. BERTScore, BLEURT, COMET 세 가지 인기있는 기계 번역 평가 메트릭에 대한 단어-문자 수준의 공격을 시도하였다.
    2. 우리의 인간 실험은 자동 평가 메트릭이 전략적으로 훼손된 번역을 지나치게 저하시키는 경향을 검증한다.
    3. 우리는 BERTScore 평가에서 일관성 없음을 발견하였는데, 원문과 전략적으로 훼손된 문장을 유사하게 판단하면서 레퍼런스에 비해 훼손된 번역을 원본보다 훨씬 나쁘게 평가한다. 이러한 취약성 패턴을 확인하여 더 견고한 메트릭 개발에 동기부여한다.

###### Time-Considerable Dialogue Models via Reranking by Time Dependency (https://aclanthology.org/2023.findings-emnlp.341/)
- Anthology ID: 2023.findings-emnlp.341 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 generative dialogue model은 뛰어난 성능을 보이며 다양한 응용 분야에 사용되고 있지만, 기존의 대화 모델들은 사람들이 지속적으로 인식하는 시간 정보를 고려하지 않는다.
    2. 이 논문에서는 시간 정보를 적극적으로 활용하는 시간을 고려할 수 있는 대화 모델을 구축하는 것을 목표로 한다. 
    3. 제안된 메트릭을 사용하여 응답을 다양한 시간에 대한 자연스러움으로 분류하고, 이를 활용하여 기존 대화 모델을 시간을 고려하는 모델로 개선하는 reranking 방법을 제안하고, 인간에 의해 주관적으로 평가한 성능을 평가한다.

###### Non-Compositionality in Sentiment: New Data and Analyses (https://aclanthology.org/2023.findings-emnlp.342/)
- Anthology ID: 2023.findings-emnlp.342 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 구문이 결합될 때 그 의미는 종종 부품들의 합 이상이다. 그렇다면 감성 분석 같은 NLP 작업에서도 그렇다. 그러나 그런 NLP 연구들은 대부분의 경우 감성을 계산함에 있어서는 구성적이다라고 주장한다.
    2. 그 대신, 우리는 구문의 감성에 따른 비구성성 평가를 얻기 위해 노력했다.
    3. 우리의 기여는 다음과 같다: a) 이러한 비구성성 평가를 얻기 위한 방법론, b) NonCompSST라는 259개의 구문에 대한 평가 자원과 그 자원의 분석, c) 이 새로운 자원을 사용하여 감성 분석에 대한 컴퓨터 모델의 평가.

###### MPrompt: Exploring Multi-level Prompt Tuning for Machine Reading Comprehension (https://aclanthology.org/2023.findings-emnlp.343/)
- Anthology ID: 2023.findings-emnlp.343 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델은 다양한 자연어 태스크에서 우수한 성능을 보여주었지만, 새로운 데이터셋에 대해 fine-tuning을 하는 데 많은 자원이 필요하다는 단점이 있다. 
    2. 본 논문에서는 multi-level prompt tuning (MPrompt) 방법을 제안하여 컨텍스트 및 태스크에 관련된 정보를 고려하여 fine-tuning을 수행한다. 도메인별 prompt에 대한 독립성 제약도 소개되었고, prompt 생성을 위해 문맥 관련 지식을 활용하는 prompt generator도 제안되었다. 
    3. 실험 결과, QA 형식의 12개 벤치마크에서 평균적으로 최신 기법 대비 1.94%의 성능 개선을 달성하였다.

###### DocTrack: A Visually-Rich Document Dataset Really Aligned with Human Eye Movement for Machine Reading (https://aclanthology.org/2023.findings-emnlp.344/)
- Anthology ID: 2023.findings-emnlp.344 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시각적으로 풍부한 문서를 읽고 이해할 수 있는 Document AI 모델의 필요성은 기술적, 언어적, 인지적 장벽을 극복하는 것을 요구한다. 그러나 적합한 데이터셋의 부재가 이 분야의 발전을 방해하고 있다.
    2. 이 문제에 대응하기 위해 우리는 인간의 시선 추적 기술을 사용하여 시각적으로 풍부한 문서와 정렬된 휴먼 아이포인트 정보를 포함하는 DocTrack 데이터셋을 소개한다.
    3. 우리의 연구 결과는 Document AI 모델이 큰 진전을 이루었지만, 인간처럼 정확하고 지속적이며 유연하게 시각적으로 풍부한 문서를 읽을 수 있는 정도에는 아직 멀었다는 것을 시사한다. 이러한 결과는 문서 인텔리전스의 미래적인 연구와 개발에 잠재적인 함의가 있다.

###### Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs (https://aclanthology.org/2023.findings-emnlp.345/)
- Anthology ID: 2023.findings-emnlp.345 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 LLMs는 자연어 이해 및 생성을 포함한 다양한 작업에서 큰 발전을 보였지만, 오류 가능성 때문에 고위험 결정 상황에서의 사용은 아직 제한적이다. 
    2. selective prediction은 LLMs의 신뢰성을 향상시키기 위해 쓰이는 기술로, 대답을 확신할 수 없는 경우 예측을 하지 않고 기권할 수 있게 한다.
    3. 이 논문에서는 특정 작업에 LLM을 적응시키는 동시에 자가 평가 능력을 향상시키기 위해 매개 변수 효율적 튜닝을 사용하는 새로운 프레임워크를 제안하고, 이를 통해 다양한 질문-응답 데이터셋에서 제일 성능이 좋은 selective prediction 방법보다 우월한 결과를 보였다.

###### Bi-Drop: Enhancing Fine-tuning Generalization via Synchronous sub-net Estimation and Optimization (https://aclanthology.org/2023.findings-emnlp.346/)
- Anthology ID: 2023.findings-emnlp.346 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기훈련된 언어 모델을 한정된 학습 데이터로 세밀 조정할 경우 과적합되어 성능이 감소하는 문제가 있다. 이 논문에서는 Bi-Drop이라는 세밀 조정 전략을 제시한다. 이는 드롭아웃에서 동적으로 생성된 다양한 서브넷의 기울기를 사용하여 모델 파라미터를 선택적으로 업데이트한다.
    2. Bi-Drop은 배치 내에서 서브넷을 추정하므로 비동기적 서브넷 추정을 수행하는 이전 방법의 위상유지 문제를 극복한다. 또한, Bi-Drop은 서브넷 추정을 위해 한 번의 미니배치만 필요로 하기 때문에 학습 데이터의 유틸리티가 높다.
    3. GLUE 벤치마크 실험 결과, Bi-Drop은 이전 세밀 조정 방법보다 일관되게 우수한 성능을 보여준다. 또한, 실험 결과는 Bi-Drop이 도메인 전이, 데이터 불균형, 저자원 시나리오에서 우수한 일반화 능력과 강건성을 가지고 있는 것을 보여준다.

###### ClozEx: A Task toward Generation of English Cloze Explanation (https://aclanthology.org/2023.findings-emnlp.347/)
- Anthology ID: 2023.findings-emnlp.347 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Cloze questions의 설명을 생성하는 새로운 task인 ClozEx를 소개한다. 이 task는 특히 제2언어로 영어를 배우는 학습자들을 위해 만들어졌으며, 적절한 설명과 함께 cloze questions을 생성하는 것이 목표이다.
    2. 우리는 cloze questions과 해당 설명으로 이루어진 dataset을 소개한다. 이 dataset은 언어 능력을 평가하고 유익하고 정확한 설명을 제공하여 언어 학습을 돕는 것을 목표로 한다.
    3. 우리는 fine-tuned된 다양한 기본 모델과 encoder-decoder 및 decoder-only 아키텍처로 task에 대처했다. 또한 large language models (LLMs)가 사전 정의된 prompt만을 사용하여 좋은 설명을 생성할 수 있는지도 탐구하였다. 평가 결과는 encoder-decoder 모델이 우리의 dataset으로 학습될 때 유창하고 유효한 설명을 제공할 수 있는 잠재력을 가지고 있음을 보여준다.

###### Is Probing All You Need? Indicator Tasks as an Alternative to Probing Embedding Spaces (https://aclanthology.org/2023.findings-emnlp.348/)
- Anthology ID: 2023.findings-emnlp.348 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단어 벡터 표현에 인코딩된 언어 정보를 식별하고 제어하는 능력은 설명 가능성과 편향 제거 등 다양한 용도로 활용될 수 있다. 이를 위해 사용되는 "프로브(probes)"라고 불리는 단순한 분류 작업을 통해 embedding 공간에서 인코딩된 정보를 평가한다. 그러나 훈련 가능한 분류기의 사용은 프로브 결과와 분류기의 특성을 얽어 매우 복잡하게 만든다.
    2. 이 논문에서는 보조 모델의 훈련 없이 embedding 공간을 조회하여 특정 속성의 존재 여부를 확인하기 위해 사용되는 "인디케이터(indicator) 작업"에 대해 소개하고, 이러한 작업이 프로브와는 반대 방향을 가리킬 수 있고, 이 모순이 embedding 공간 내에서 특성의 존재 여부를 결정하기를 복잡하게 만든다고 주장한다. 
    3. 이러한 주장을 두 가지 테스트 케이스를 통해 실험적으로 검증하였는데, 하나는 성별 편향 제거와 관련된 것이며, 다른 하나는 embedding 공간에서 형태론적 정보를 삭제하는 것과 관련되었다. 이를 통해 적절한 인디케이터의 적용이 프로브 대비 더 정확한 정보를 제공한다는 것을 보였고, embedded 표현으로부터 정보를 추출할 때 인디케이터 작업을 고려해야 한다는 결론을 내렸다.

###### The Cost of Compression: Investigating the Impact of Compression on Parametric Knowledge in Language Models (https://aclanthology.org/2023.findings-emnlp.349/)
- Anthology ID: 2023.findings-emnlp.349 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 압축은 빠른 추론, 작은 메모리 풋프린트 및 로컬 배포를 가능하게 해주지만, 일반적으로 파악되는 평가 지표 외에도 박제된 지식을 측정하는 세부적인 평가 지표에 대한 연구는 아직 충분히 이루어지지 않았으며, 이 연구를 충족시키기 위해 LAMA 및 LM-Harness 벤치마크를 사용하여 일반적으로 사용되는 압축 기법이 모델 성능에 미치는 영향을 체계적으로 분석한다고 주장한다.
    2. LLM 압축 기술의 주된 trade-off은 압축 정도와 압축된 모델의 품질에 대한 영향 사이에서 이루어지고 있으며, 기존의 연구들은 주로 퍼플렉서티(perplexity)나 다운스트림 태스크 정확도와 같은 일반적인 지표에 초점을 맞추고 있다.
    3. 본 연구는 대규모 언어 모델에서 일반적으로 사용되는 압축 기법의 영향을 체계적으로 분석하여 실제적인 통찰력을 제공함으로써 실무자들이 압축에 대한 결정을 내릴 수 있게 하는 것을 목표로 한다.

###### CoEdIT: Text Editing by Task-Specific Instruction Tuning (https://aclanthology.org/2023.findings-emnlp.350/)
- Anthology ID: 2023.findings-emnlp.350 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CoEdIT은 텍스트 편집을 위한 최신 텍스트 편집 시스템으로, 사용자의 지시에 따라 원하는 텍스트의 속성을 지정하고 수정된 텍스트를 출력한다. 
    2. 우리는 다양한 텍스트 편집 벤치마크에서 최고 성능을 달성하며, 공개적으로 사용 가능한 가장 큰 크기의 LLM보다 약 60배 작으면서 경쟁력을 가지고 있다. 
    3. 뿐만 아니라, 이 모델은 이전에 보지 못한 편집 지침의 일반화를 할 수 있으며, 편집 동작의 다른 조합을 포함하는 복합 지침에 일반화할 수 있는 능력을 보인다.

###### Exploring Large Language Models for Multi-Modal Out-of-Distribution Detection (https://aclanthology.org/2023.findings-emnlp.351/)
- Anthology ID: 2023.findings-emnlp.351 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신뢰할 수 있는 기계 학습을 위해 out-of-distribution(OOD) 탐지는 필수적이다. 이 논문에서는 큰 언어 모델을 활용하여 OOD 탐지의 성능을 향상시키기 위해 월드 지식을 적용하는 방법을 제안한다. 
    2. 제안하는 방법은 consistency-based uncertainty calibration을 이용하여 각 생성물의 신뢰도를 추정하는 것이다. 이미지에서 시각적 객체를 추출하여 월드 지식을 활용하는 것도 추가로 도입된다.
    3. 실험 결과, 제안하는 방법은 기존 기법보다 일관성 있게 더 좋은 성능을 보였다.

###### Better Together: Enhancing Generative Knowledge Graph Completion with Language Models and Neighborhood Information (https://aclanthology.org/2023.findings-emnlp.352/)
- Anthology ID: 2023.findings-emnlp.352 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 지식 그래프(KG)는 종종 불완전함으로, 잠재력을 제한한다. 이를 해결하기 위해 Knowledge Graph Completion (KGC) 기법이 사용된다. 
    2. 그러나 기존의 KGC 방법은 연산량이 많아 대규모 KG에는 적합하지 않다. 
    3. 이 논문에서는 이웃 노드를 추가 정보로 사용하여 언어 모델 기반의 KGC 방법을 개선하는 방법을 제안하고, 실제로 KGT5와 전통적인 KGC 방법들보다 더 우수한 성능을 보인다는 것을 실험을 통해 보여준다.

###### DeltaScore: Fine-Grained Story Evaluation with Perturbations (https://aclanthology.org/2023.findings-emnlp.353/)
- Anthology ID: 2023.findings-emnlp.353 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 생성 작업에 대한 다양한 평가 메트릭이 개발되었지만, 이러한 메트릭은 흥미로움과 유창성과 같은 서술의 복잡한 측면을 평가하는 데 제한적이다.
    2. 이 논문에서는 미세한 서술 측면의 평가를 위해 편작 기법을 사용하는 새로운 방법인 DeltaScore를 소개한다.
    3. DeltaScore는 사전 학습된 언어 모델을 사용하여 사전-후처리 상태의 가능성 차이를 계산하여 각 측면의 품질을 측정하며, 플루언시, 일관성, 관련성, 논리성, 흥미로움에 대해 강력한 성능을 보인다.

###### MuG: A Multimodal Classification Benchmark on Game Data with Tabular, Textual, and Visual Fields (https://aclanthology.org/2023.findings-emnlp.354/)
- Anthology ID: 2023.findings-emnlp.354 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구에서는 다중 소스로부터 수집한 데이터를 통합하는 것이 전통적으로 단일 모달 데이터보다 장점이 있는 것이 증명되어, 다양한 신규 다중 모달 응용 프로그램들이 등장하였다.
    2. 우리는 MuG라는 다중 모달 분류 벤치마크를 제안하여 연구자들이 자신들의 모델을 평가하고 개선할 수 있는 환경을 제공한다.
    3. MuG는 타블로, 텍스트, 비주얼 모달을 포괄한 4가지 다양한 게임 장르에서 수집된 8개의 데이터셋으로 구성되어 있으며, 이를 통해 다중 모달 분류기의 어려운 특징과 다양한 종속성을 시험할 수 있다.

###### Don’t waste a single annotation: improving single-label classifiers through soft labels (https://aclanthology.org/2023.findings-emnlp.355/)
- Anthology ID: 2023.findings-emnlp.355 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 보통 객관식 단일 라벨 분류 작업에서 데이터 주석 및 훈련 방법의 한계를 다룬다. 
    2. 기존 방법은 주석 달 때 매번 한 샘플에 대해 하나의 라벨을 선택하도록 요구하는데, 이는 모호성과 맥락 부재로 인해 적절한 라벨을 결정하기 어려울 수 있다. 
    3. 따라서 이 논문에서는 모호한 주석의 정보를 활용하여 훈련시키는 소프트 라벨 방법을 제안하고, 이를 사용하면 성능과 보정(calibration)이 향상된다고 밝혔다.

###### Black-Box Tuning of Vision-Language Models with Effective Gradient Approximation (https://aclanthology.org/2023.findings-emnlp.356/)
- Anthology ID: 2023.findings-emnlp.356 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Parameter-efficient fine-tuning (PEFT) 방법은 대규모 vision-language 모델을 특정 과제나 시나리오에 적응시키는 효과적인 방법을 제공하고 있다. 그러나 대규모 모델은 남용 방지나 상업적인 이유로 인해 종종 오픈소스가 아니기 때문에, 흰 상자 PEFT 방법의 적용에는 장벽이 있다.
    
    2. 이 논문에서는 모델 접근성에 대한 의존성을 완화하기 위해, 검정 상자 모델에 대한 텍스트 프롬프트 최적화와 출력 특징 적응을 위한 협력적 검은 상자 튜닝 (CBBT)를 소개한다.
    
    3. 제안된 CBBT는 열 한 가지의 하류 벤치마크에서 괄목할 만한 개선을 이루며, 기존의 검은 상자 VL 적응 방법과 비교했을 때 높은 수준의 성능을 달성한다.

###### How to Determine the Most Powerful Pre-trained Language Model without Brute Force Fine-tuning? An Empirical Survey (https://aclanthology.org/2023.findings-emnlp.357/)
- Anthology ID: 2023.findings-emnlp.357 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 컴퓨터 비전 분야에서 전이능력 추정 (transferability estimation)은 매우 중요한 관심사로 여겨져왔다.
    2. 이 논문에서는 전이능력 추정 방법을 철저히 조사하고 가장 적합한 모델을 찾기 위해 GLUE 벤치마크에 기반한 상세한 실험을 실시한다.
    3. 이미 존재하는 방법들의 강점과 약점을 보여주며, H-Score가 효과적이고 효율적인 성능을 갖는다는 것을 보여준다.

###### Licon: A Diverse, Controllable and Challenging Linguistic Concept Learning Benchmark (https://aclanthology.org/2023.findings-emnlp.358/)
- Anthology ID: 2023.findings-emnlp.358 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 개념 학습은 이미지로부터 개념을 학습하는 데 중점을 둔 기존 방법 대부분이 있지만, 시각적 정보는 추상적인 개념을 완전히 표현하지 못하기 때문에 기존 개념과 관련된 새로운 개념을 도입하는 데 어려움이 있다. 
    2. 본 연구에서는 인간이 언어적 설명을 통해 대부분의 개념을 학습하는 사실을 바탕으로, Linguistic Concept Learning benchmark (Licon)을 소개한다. 다양한 형태 (예: 일반 속성, 이미지, 텍스트)의 개념이 언어적 설명으로 정의된다. 
    3. 또한, EnC라는 entailment 기반 개념 학습 방법을 설계하여 개념들 간의 관계를 모델링한다고 한다. 다양하고 조절 가능한 개념은 개념 분류, 속성 예측, 개념 관계 인식 등의 도전적인 평가 과제를 지원한다.

###### InterroLang: Exploring NLP Models and Datasets through Dialogue-based Explanations (https://aclanthology.org/2023.findings-emnlp.359/)
- Anthology ID: 2023.findings-emnlp.359 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 개발된 NLP explainability 방법들은 우리에게 다양한 방식으로 '블랙박스'를 열어주지만, 대화 인터페이스를 제공하는 인터랙티브 도구가 부족하다.
    2. 우리는 TalkToModel 프레임워크를 NLP 도메인에 적용하고, 자유 텍스트 인지를 포함하는 NLP 특정 작업에 대한 일반적인 적용 가능성을 보여준다. 
    3. 모델 동작을 설명하기 위해 우리는 합리화(rationalization)와 특징 속성(feature attribution)이 도움이 된다는 것을 밝혀냈고, 설명 대화를 기반으로 모델 결과를 신뢰할 수 있게 예측할 수 있다는 것을 보였다.

###### INVITE: a Testbed of Automatically Generated Invalid Questions to Evaluate Large Language Models for Hallucinations (https://aclanthology.org/2023.findings-emnlp.360/)
- Anthology ID: 2023.findings-emnlp.360 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델들은 여러 번의 대화를 통해 자유로운 대화를 처리할 수 있게 되었으나, 그들은 주장의 근거가 없거나 잘못된 진술을 할 수 있는 경향이 있다 (hallucinations). 
    2. 기존 평가 방법들은 TruthfulQA와 같은 QA 테스트 세트에서 LLMs를 테스트하는 것이지만, LLMs는 점점 더 큰 텍스트 코퍼스에서 사전훈련을 받기 때문에 훈련 중에 이러한 테스트 세트에 노출되어 테스트 세트의 모델 성능을 과소평가하게 만든다. 
    3. 이 논문에서는 이러한 리스크를 대응하기 위해 LLMs가 잘못된 질문에 대해 강력하게 대응할 수 있도록 돕기 위한 INVITE라는 프레임워크를 제안한다. 이 프레임워크는 유사한 entity로 대체된 주제나 객체로 유효한 사실을 왜곡하여 새로운 일괄적인 무효 질문을 생성하는데 사용된다.

###### Multimodal Automated Fact-Checking: A Survey (https://aclanthology.org/2023.findings-emnlp.361/)
- Anthology ID: 2023.findings-emnlp.361 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 잘못된 정보는 종종 잘못 된 캡션을 가진 이미지와 같은 다양한 매체에서 전달된다. 라기에는는 멀티 모달 잘못된 정보가 사람들에게 더 신뢰도 높은 것으로 인식되며 텍스트만 있는 것보다 더 빠르게 확산된다. 
    2. 이 논문에서는 텍스트, 이미지, 오디오 및 비디오와 같은 실제 팩트 체킹에 흔한 네 가지 다양한 매체에 초점을 맞추고, 멀티모달 잘못된 정보에 대한 특수한 하위 작업을 포함하는 AFC (자동 팩트 체크)를 위한 프레임 워크를 개념화한다.
    3. 또한 우리는 다른 커뮤니티에서 사용되는 관련 용어들을 논의하고 우리의 프레임 워크에 매핑한다.

###### PROTEGE: Prompt-based Diverse Question Generation from Web Articles (https://aclanthology.org/2023.findings-emnlp.362/)
- Anthology ID: 2023.findings-emnlp.362 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. StackOverflow, Quora와 같은 온라인 지식 공유 커뮤니티 및 대화형 어시스턴트(chatbot)와 같은 응용 프로그램에게 풍부하고 다양한 지식 베이스(KB: knowledge base)가 필수적이다. 
    2. 이 논문은 도메인 특정한 긴 형태의 텍스트 내용(웹 기사 등)에서 Q&A 기반 지식 베이스의 자동 생성 문제에 초점을 맞춘다.
    3. PROTEGE라는 다양한 질문 생성 프레임워크를 제안하여, 다양성과 충실성을 모두 달성한다고 실험 결과를 통해 보여준다.

###### GPT-4 as an Effective Zero-Shot Evaluator for Scientific Figure Captions (https://aclanthology.org/2023.findings-emnlp.363/)
- Anthology ID: 2023.findings-emnlp.363 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 자연어처리(NLP) 태스크에서 최고 수준의 정확성을 보이는 딥 모델들에게서도 spurious 패턴에 의존하는 것으로 알려져 있어서, robustness가 제한된다는 것이 보고되고 있다.
    2. 유사한 counterfactual이 이미 데이터셋에 있는지 자동으로 찾는 기계나 사람이 데이터셋에 counterfactual을 추가하는 방법은 spurious correlation이 여전히 문제가 된다.
    3. 이 논문은 "여러 개의" counterfactual을 합성하고, 이 집합에서 예측 분포에 대한 집단적인 결정을 내리면서 각 용어의 인과관계를 강력하게 지도하는 방법을 제안한다.

###### Mulan: A Multi-Level Alignment Model for Video Question Answering (https://aclanthology.org/2023.findings-emnlp.364/)
- Anthology ID: 2023.findings-emnlp.364 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 비디오에 대한 질문에 답하는 것을 목표로 하는 VideoQA에서는 비디오와 텍스트 간의 세밀한 시맨틱 상호작용에 관심이 부족한 것이 현재 주된 문제이다.
    2. 그러므로 이 논문에서는 객체 수준, 프레임 수준 및 비디오 수준에서 비주얼과 텍스트 간의 alignment를 수립하는 Multi-Level Alignment Model for Video Question Answering인 Mulan을 제안한다.
    3. 실험 결과, 우리의 방법은 최소한의 비주얼-언어 사전학습 데이터 및 줄어든 학습 가능한 매개변수 수를 활용할 때에도 최신 기법들보다 뛰어난 성능을 보인다.

###### HARE: Explainable Hate Speech Detection with Step-by-Step Reasoning (https://aclanthology.org/2023.findings-emnlp.365/)
- Anthology ID: 2023.findings-emnlp.365 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어의 확대로 인해 혐오 발언의 정확한 탐지는 온라인 안전을 보장하기 위해 중요해졌다. 이 논문에서는 큰 언어 모델들의 추론 능력을 활용하여 혐오 발언에 대한 설명의 비어있는 부분을 채우는 hate speech detection 프레임워크 'HARE'를 소개한다. 
    2. 기존 주석 체계에서의 추론 갭을 해결하기 위해 모델이 생성한 데이터를 활용한 접근법이 사용되었으며, 이를 통해 훈련된 모델의 설명의 질을 향상시키고 보지 못한 데이터셋에 대한 일반화 성능을 크게 향상시킬 수 있었다.
    3. 실험 결과는 기존의 인간 주석을 사용한 베이스라인들보다 모델이 생성한 데이터를 사용한 접근법이 일관되게 우월한 성능을 발휘하며, 훈련된 모델의 설명의 질을 향상시키고 보이지 않는 데이터에 대한 일반화를 개선시켜줌을 보여준다.

###### ReLM: Leveraging Language Models for Enhanced Chemical Reaction Prediction (https://aclanthology.org/2023.findings-emnlp.366/)
- Anthology ID: 2023.findings-emnlp.366 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 화학적 지식을 활용하여 실제 화학 반응 예측의 정확성을 향상시키는 새로운 프레임워크인 ReLM을 제안하였다.
    2. Graph Neural Networks (GNNs)을 사용하는 기존 기술은 텍스트 정보를 활용할 수 없고, 충분한 훈련 데이터가 없어 실제 응용에 적용하기에 한계가 있다.
    3. ReLM은 GNNs에 언어 모델의 화학적 지식을 활용하여 신뢰성을 자가 평가하고 예측 성능을 향상시킨다. 실험 결과, ReLM은 다양한 화학 반응 데이터셋에서 최신 GNN 기반 방법보다 뛰어난 성능을 보여준다.

###### Decomposing Complex Queries for Tip-of-the-tongue Retrieval (https://aclanthology.org/2023.findings-emnlp.367/)
- Anthology ID: 2023.findings-emnlp.367 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 아이템을 다시 찾을 때, 사용자들은 잊어버리거나 식별할 수 없는 세부 정보에 대해 창의적인 전략을 사용하는데, 이는 문서 텍스트를 벗어난 정보 (예: 책 표지의 설명)나 개인적인 문맥 (예: 언제 책을 읽었는지), 콘텐츠 요소 (예: 책의 캐릭터나 사건)를 설명하는 복잡한 질의 형태일 수 있다. 
    2. 이 논문에서는 이러한 복잡한 질의를 처리하기 위해 LLM을 사용하여 질의를 힌트로 분해하고 이를 특화된 검색기에 서브질의로 라우팅한 다음 결과를 앙상블하는 간단하면서도 효과적인 프레임워크를 제안한다.
    3. 이 접근 방식은 off-the-shelf 검색기 (예: 책 표지 이미지를 검색하기 위한 CLIP)를 활용하거나 검색기 별 논리 (예: 날짜 제한)를 통합할 수 있다는 것을 보여주며, 새로운 데이터셋에서 Recall@5에 대해 골드 책 검출을 최대 6% 향상시킬 수 있다.

###### Values, Ethics, Morals? On the Use of Moral Concepts in NLP Research (https://aclanthology.org/2023.findings-emnlp.368/)
- Anthology ID: 2023.findings-emnlp.368 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP의 윤리적 측면을 연구한 많은 논문들이 있으나, 이들 논문들에는 기초적인 용어와 이론에 대한 논의가 거의 이루어지지 않았다.
    2. 이 논문에서는 철학적인 윤리 개념과 이미 존재하는 도덕적인 NLP 연구를 체계적으로 조사하여 이들의 철학적 기반과 용어, 데이터 기반에 대해 분석한다. 
    3. 이를 통해 논문 작성자는 NLP 분야에서의 도덕적인 논의에 대한 정보 제공과 함께 향후 연구에 대한 세 가지 권고사항을 제시한다.

###### Self-Supervised Behavior Cloned Transformers are Path Crawlers for Text Games (https://aclanthology.org/2023.findings-emnlp.369/)
- Anthology ID: 2023.findings-emnlp.369 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 텍스트 게임에 대한 self-supervised behavior cloning transformer를 소개한다. 이는 가상 환경에서의 다단계 추론에 대한 어려운 벤치마크로, 기존의 Behavior Cloning Transformers는 이와 같은 작업에서 뛰어나지만 지도 학습 데이터에 의존한다. 
    2. 우리의 방법은 게임에서 보상을 얻을 수 있는 공통된 매크로 동작 순서로 정의된 트라젝터리를 탐색하면서 학습 데이터를 자동으로 생성한다. 빠른 모델 훈련을 통해 이러한 트라젝터리의 일반성과 유효성을 결정하고, 본 연구에서는 본문에서 제시된 벤치마크 텍스트 게임 세 가지에 대해 지도 학습 시스템의 약 90% 성능을 달성함을 보여주었다.

###### Adapting Pretrained Text-to-Text Models for Long Text Sequences (https://aclanthology.org/2023.findings-emnlp.370/)
- Anthology ID: 2023.findings-emnlp.370 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이미 존재하는 짧은 문맥 모델로부터 긴 문맥 모델을 구축하는 효과적인 방법을 제안한다. 
    2. transformer에서 full attention을 pooling-augmented blockwise attention으로 대체하고, 다양한 길이의 span을 가진 masked-span prediction task로 모델을 pretrain하는 방법을 제안한다. 
    3. 또한, 대용량 오픈 도메인 코퍼스에서 랜덤하게 연결된 짧은 문서를 사용하는 것이 기존의 긴 문서 코퍼스를 사용하는 것보다 성능이 우수함을 확인하고 이를 통해 긴 텍스트 QA 작업에서 경쟁력 있는 성능을 달성하였다.

###### xDial-Eval: A Multilingual Open-Domain Dialogue Evaluation Benchmark (https://aclanthology.org/2023.findings-emnlp.371/)
- Anthology ID: 2023.findings-emnlp.371 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 오픈 도메인 대화 평가를 위한 레퍼런스-프리 학습 메트릭은 미리 학습된 언어 모델과 고품질의 인간 주석을 통해 발전하고 있다. 하지만 현재의 연구는 주로 영어 대화에 초점을 맞추고 있으며, 다른 언어로의 일반화 여부는 충분히 검토되지 않았다.
    2. 이 논문에서는 오픈 소스 영어 대화 평가 데이터셋을 기반으로 한 xDial-Eval을 소개한다. xDial-Eval은 12개의 턴 수준 데이터와 6개의 대화 수준 데이터를 포함하며, 영어 대화 데이터는 상용 기계 번역 시스템을 이용하여 다른 언어로 확장되었다.
    3. xDial-Eval을 통해 이전에 제안된 BERT 기반 메트릭과 최근 등장한 대형 언어 모델들을 포괄적으로 분석하고, 강력한 자기 지도 및 다국어 기준선을 수립했다.

###### MathDial: A Dialogue Tutoring Dataset with Rich Pedagogical Properties Grounded in Math Reasoning Problems (https://aclanthology.org/2023.findings-emnlp.372/)
- Anthology ID: 2023.findings-emnlp.372 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 대화 튜터는 교육을 개인화하고 접근성을 높이는데 큰 잠재력을 가지고 있지만, 충분히 크고 고품질의 데이터셋이 부족하여 연구가 지연되고 있다.
    2. 이 논문에서는 인간 교사와 Large Language Model (LLM)을 결합하여 이러한 대화를 생성하기 위한 프레임워크를 제안한다.
    3. 이를 통해 알고리즘 풀이에 능한 모델들을 튜터로 사용할 수 있으며, MathDial 데이터셋을 통해 더 효과적인 튜터로 모델을 fine-tuning할 수 있다고 입증하였다.

###### Towards Making the Most of ChatGPT for Machine Translation (https://aclanthology.org/2023.findings-emnlp.373/)
- Anthology ID: 2023.findings-emnlp.373 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT는 높은 resource를 갖는 언어에 대해서는 상업용 시스템과 비교 가능한 결과를 보이지만, 낮은 resource나 먼 언어 쌍의 번역 같은 복잡한 작업에서는 성능이 뒤처지는 것으로 알려져 있다. 이 연구에서는 ChatGPT의 번역 능력을 더 발전시키기 위해 temperature, task 정보, domain 정보 등을 고려하여 두 개의 (단순하지만 효과적인) 프롬프트를 제안한다.
    2. ChatGPT의 성능은 크게 temperature에 따라 달라지며, 낮은 temperature일수록 더 좋은 성능을 달성할 수 있다.
    3. 태스크 정보를 강조함으로써 ChatGPT의 성능을 더 향상시킬 수 있으며, 특히 복잡한 MT 작업에서 도움이 된다. 또한 domain 정보를 도입함으로써 ChatGPT의 일반화 능력을 활성화시키고 특정 도메인에서의 성능을 향상시킬 수 있다.

###### Enhancing Reasoning Capabilities by Instruction Learning and Chain-of-Thoughts for Implicit Discourse Relation Recognition (https://aclanthology.org/2023.findings-emnlp.374/)
- Anthology ID: 2023.findings-emnlp.374 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 암시적 담화 관계 인식은 두 가지 주장 사이의 관련성을 이해하는 것을 목표로 한다. 본 논문에서는 생성 모델을 기반으로한 분류 방법을 제안한다.
    2. 우리의 접근법은 명령어 템플릿과 컨텍스트 내 학습을 결합하여 생성 모델을 개선시키는데 활용되며, 이렇게 함으로써 암시적 담화 관계 인식 작업에 효과적으로 대응한다.
    3. 실험 결과, PDTB 2.0, PDTB 3.0 및 CoNLL16 공유 작업 데이터셋에서 평가한 결과, 기존 최고 성능 모델과 비교하여 우수한 성능을 보였다.

###### Large-Scale and Multi-Perspective Opinion Summarization with Diverse Review Subsets (https://aclanthology.org/2023.findings-emnlp.375/)
- Anthology ID: 2023.findings-emnlp.375 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 의견 요약 솔루션은 정보 선택을 위한 디자인 부재로 인해 대규모의 리뷰를 요약하고 다양한 관점에서 의견 요약을 제공하는 데에 있어서 부족하다.
    2. 그래서, 우리는 대규모 다각도 의견 요약을 위한 감독 학습 요약 프레임워크 SubSumm을 제안한다. SubSumm은 리뷰 샘플링 전략 세트와 두 단계의 훈련 방법으로 구성되어 있다.
    3. SubSumm은 여러 관점과 질 수준의 리뷰 하위집합을 선택하기 위해 감성 방향과 대비 정보 가치를 고려하는 샘플링 전략을 사용하며, 이를 통해 수많은 입력을 활용하여 요약 생성 모델을 훈련시킬 수 있다는 것을 실험 결과로 보여준다.

###### Topic-Informed Dialogue Summarization using Topic Distribution and Prompt-based Modeling (https://aclanthology.org/2023.findings-emnlp.376/)
- Anthology ID: 2023.findings-emnlp.376 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 요약에서 다중 주제를 다루는 것은 문서와 달리 주제 이동에 취약하므로 중요한 문제로 고려되어야 합니다.
    2. 우리는 대화 주제 분포를 반영하는 새로운 대화 요약 모델을 제안합니다. 대화 주제 분포를 추정하는 효과적인 주제 발견 모델을 사용하여 대화 인코더 및 디코더 벡터의 출력에 주제 정보를 전달합니다.
    3. 실험 결과로는 우리 모델이 ROUGE 점수에서 최신 기법보다 우수한 성능을 보이며, 인간 평가 결과로는 우리의 프레임워크가 포괄적인 요약을 잘 생성한다는 것을 보여줍니다.

###### Disentangling Structure and Style: Political Bias Detection in News by Inducing Document Hierarchy (https://aclanthology.org/2023.findings-emnlp.377/)
- Anthology ID: 2023.findings-emnlp.377 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 언론 신문 기사에서 정치적 편견을 식별하는 방법은 각 신문 매체의 글쓰기 스타일에 영향을 받아 overfitting과 일반화 능력의 한계가 있다. 
    2. 우리는 문장 수준의 의미와 문서 수준의 retorical structure을 고려하여 정치적 편견을 식별하는 더 견고하고 스타일에 구애받지 않는 방법을 제안한다. 
    3. 우리는 다양한 어텐션 헤드의 앙상블을 통해 긴 문서의 구조를 효과적으로 인코딩하는 새로운 다중 헤드 계층적 어텐션 모델을 소개하고, 이는 도메인 종속성을 극복하며 이전 방법보다 더 견고하고 정확한 결과를 보여준다.

###### Measuring and Narrowing the Compositionality Gap in Language Models (https://aclanthology.org/2023.findings-emnlp.378/)
- Anthology ID: 2023.findings-emnlp.378 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구에서는 어휘 모델들이 서브 문제들의 답을 올바르게 합성함으로써 전체적인 해결책을 찾는 구성적 추론 작업의 능력을 조사했다.
    2. 우리는 서브 문제들의 답을 모델들이 올바르게 대답하지만 전체적인 해결책을 생성하지 못하는 비율을 측정하는데 이를 구성성 갭(compositionality gap)이라고 명명하였다.
    3. 우리는 GPT-3 모델들에서 모델 크기가 커짐에 따라 단일-홉의 질문-답변 작업 성능이 더 빠르게 개선되는 반면, 다중-홉 작업 성능은 그렇지 않아서 구성성 갭이 줄어들지 않는다는 것을 보였다.

###### Unsupervised Candidate Answer Extraction through Differentiable Masker-Reconstructor Model (https://aclanthology.org/2023.findings-emnlp.379/)
- Anthology ID: 2023.findings-emnlp.379 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 질문 생성은 광범위한 응용 분야에서 사용되는 데이터 증강 접근 방법이지만, 기존의 후보 답안 추출 방법은 언어적 규칙이나 주석이 달린 데이터에 의존하여 부분적 주석 문제와 일반화 도전에 직면한다.
    2. 이 연구에서는 문맥 단락의 내재적 구조를 활용하여 자가 일관성을 강화하는 Differentiable Masker-Reconstructor (DMR) 모델을 통해 감지력 있는 정보 토큰을 추출하는 비지도 후보 답안 추출 방법을 제안한다.
    3. DMR 모델의 효과를 입증하기 위해 전수 조사된 답안을 가진 두 개의 데이터셋을 구성하고, 감독 없는 방법 중에서도 성능이 우수하며 감독 방법과 동등한 성능을 보여준다.

###### HoneyBee: Progressive Instruction Finetuning of Large Language Models for Materials Science (https://aclanthology.org/2023.findings-emnlp.380/)
- Anthology ID: 2023.findings-emnlp.380 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 저자들은 재료 과학 (materials science)에 특화된 천억 개의 파라미터를 가진 언어 모델인 HoneyBee를 만들기 위해 신뢰할 수 있는 데이터 정제 과정인 MatSci-Instruct를 제안한다. 
    2. MatSci-Instruct는 상업적으로 사용 가능한 대형 언어 모델에게 나열 모듈 (예: Chat-GPT)을 사용하여 생성을 하고 독립적인 확인자 모듈 (예: Claude)에서 확인함으로써 생성된 데이터의 신뢰성을 향상시킨다.
    3. MatSci-Instruct를 사용하여 다양한 척도를 통해 생성된 데이터의 품질을 측정하고, HoneyBee 모델의 성능을 점진적으로 개선하는 반복적인 과정을 거친 결과를 평가하여 재료 과학 작업에서 기존 언어 모델보다 뛰어난 성과를 보였다.

###### Prompt-Based Editing for Text Style Transfer (https://aclanthology.org/2023.findings-emnlp.381/)
- Anthology ID: 2023.findings-emnlp.381 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 텍스트 스타일 전환에서 텍스트 쿼리를 사용하여 사전 훈련된 언어 모델(PLM)을 쿼리하는 "Prompting 접근법"이 탐구되었지만, 이러한 생성 과정은 덜 제어 가능하며 초기 예측 오류가 후속 단어 예측에 영향을 줄 수 있다.
    2. 이 논문에서는 텍스트 스타일 전환을 위한 프롬프트 기반 편집 접근법을 제안한다. 특히, 스타일 분류를 위해 PLM에 프롬프트를 제공하고, 분류 확률을 사용하여 스타일 점수를 계산한다. 그런 다음, 문장 수준 변환 작업을 위한 포괄적인 점수 함수를 최대화하기 위해 단어 수준 편집과 이산적 탐색을 수행한다.
    3. 실험에서는 세 가지 스타일 전환 벤치마크 데이터셋에서 자동 및 인간 평가를 수행하고, 매개변수가 20배 더 많은 기존 시스템보다 우수한 성능을 보이는 것을 보여준다. 추가적인 실험 결과 분석은 우리의 방법의 효과를 더욱 명확히 보여준다.

###### Representativeness as a Forgotten Lesson for Multilingual and Code-switched Data Collection and Preparation (https://aclanthology.org/2023.findings-emnlp.382/)
- Anthology ID: 2023.findings-emnlp.382 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 세계적으로 다양한 언어를 사용하며 code-switching (CSW)은 다른 언어들이 섞이는 일반적인 현상이다. 하지만 최근의 대규모 다국어 언어 모델(MMLM)의 발전에도 불구하고, 성공적인 CSW 시스템을 구축하는 데는 아직 큰 진전이 없다. 
    2. 이 논문은 CSW 데이터셋에 대한 수집과 준비 (예: 전사 및 주석) 단계에서의 이슈들을 검토하여 이러한 문제의 원인을 조사한다. 
    3. 분석 결과, 대부분의 CSW 데이터가 영어에만 집중되어 다른 언어 쌍/튜플이 무시되고, 위치, 사회-인구학적 및 등록 상의 변동성을 무시하여 데이터 수집과 준비 과정에서 대표성에 결함이 있다는 사실을 밝혀냈다. 또한, CSW 데이터셋의 대표성에 대한 명확한 데이터 선택 및 필터링 과정이 부족하다는 문제도 있다.

###### NERvous About My Health: Constructing a Bengali Medical Named Entity Recognition Dataset (https://aclanthology.org/2023.findings-emnlp.383/)
- Anthology ID: 2023.findings-emnlp.383 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이름 있는 entity를 인식하는 능력인 Named Entity Recognition (NER)은 생명 과학 분야의 여러 다운스트림 작업에서 유용하다. 특히 NER은 환자들이 일상적으로 사용하는 비공식 언어로 이루어진 Consumer Health Questions (CHQs)를 다룰 때 어렵다. 
    2. 이 논문에서는 Bengali 언어의 문장 구조의 유연성과 지역 방언의 차이로 인해 이러한 어려움이 더욱 커진다고 언급한다. 
    3. 이러한 데이터의 부족으로 인해, 이 논문에서는 Bengali 언어의 건강 관련 텍스트에서 named entities를 인식하는 종합적인 데이터셋인 'Bangla-HealthNER'를 제공한다.

###### Sparse Black-Box Multimodal Attack for Vision-Language Adversary Generation (https://aclanthology.org/2023.findings-emnlp.384/)
- Anthology ID: 2023.findings-emnlp.384 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 딥러닝 모델은 실제 상황에서 다양한 플랫폼의 안전한 관리를 위해 상품 제한, 혐오 발언 모니터링 등 다양한 분야에서 널리 사용되고 있다. 하지만 불법적인 판매자들은 금지된 제품에 대해 대규모로 왜곡을 추가하여 감지 모델을 속일 수 있으므로, 이러한 왜곡에 대한 모델의 취약성을 시뮬레이션하고 평가하는 것은 도전적이다.
    2. 이 논문에서는 Sparse Multimodal Attack (SparseMA)라는 새로운 블랙박스 다중모달 공격을 제안한다. SparseMA는 희소한 왜곡을 이용하여 불법적인 판매자들의 공격 행동을 블랙박스 상황에서 시뮬레이션한다. 또한, SparseMA는 이미지 패치와 텍스트 단어를 이산 공간에서 동등하게 처리하여 이미지와 텍스트 간의 간극을 좁힌다.
    3. 실험 결과 SparseMA는 다른 모달성에 대한 모델의 취약성을 식별하는 데에 탁월한 성능을 보이며, 기존의 다중모달 공격과 단일모달 공격을 능가한다. SparseMA는 우리가 알기로는 처음으로 제안된 블랙박스 다중모달 공격 방법으로, 다중모달 모델의 강건성을 평가하는 데에 효과적인 도구로 사용될 수 있다.

###### Towards a Unified Framework for Reference Retrieval and Related Work Generation (https://aclanthology.org/2023.findings-emnlp.385/)
- Anthology ID: 2023.findings-emnlp.385 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 관련 작업 생성 과제는 사람들에게 시간과 노력을 절약하기 위해 자동으로 관련 연구 주제에 대한 통합적인 설문 조사를 생성하는 것을 목표로 한다. 기존 방법은 대규모 과학적 말뭉치에서 사람이 주석을 단 참고 문헌을 정보원으로 사용함으로써 이 작업을 단순화했지만 시간과 비용이 많이 든다.
    2. 본 논문에서는 대규모 언어 모델(LLM)을 기반으로 참고 문헌 검색과 관련 작업 생성 프로세스를 통합된 프레임워크로 결합하는 통합 참고문헌 검색 및 관련 작업 생성 모델(UR3WG)을 제안한다. UR3WG는 먼저 LLM의 세계 지식을 활용하여 초록을 확장하고 후속 검색 단계를 위한 쿼리를 생성한다. 그런 다음 중요성을 고려한 렉시콘 개선형 밀집 검색이 제안되어 관련 참고 문헌을 검색한다. 또한 리트리버를 최적화하기 위해 다중 층위 대조 학습을 제안한다.
    3. 이 작업은 단순히 참고 문헌의 주요 포인트를 요약하는 것이 아니므로 복잡한 관계를 분석하고 논리적으로 제시해야 한다. 또한 LLM을 활용하여 관련 작업을 생성하기 위해 인스트럭션 튜닝 방법을 제안한다. 널리 적용된 두 개의 데이터셋에서의 실험 결과는 우리 모델이 생성 및 검색 메트릭에서 최신 기법을 능가한다는 것을 보여준다.

###### Visual Storytelling with Question-Answer Plans (https://aclanthology.org/2023.findings-emnlp.386/)
- Anthology ID: 2023.findings-emnlp.386 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이미지 시퀀스로부터 흥미로운 내러티브를 생성하는 시각적 스토리텔링은 기존 모델들이 주로 외부 지식 소스나 고급 그래프 구조와 같은 이미지 시퀀스의 표현을 향상시키는 데 초점을 맞추었다. 
    2. 그러나 최근 연구들에서는 이러한 이야기들이 자주 반복되거나 논리적으로 알맞지 않으며 세부 정보가 부족하다는 문제점이 있다. 
    3. 이 논문에서는 이미지 시퀀스를 시각적 접두사로 변환하여 언어 모델이 해석할 수 있는 연속적인 임베딩의 시퀀스로 표현한 후, 질문-답변 쌍의 시퀀스를 기반으로 강조할 시각적 개념을 선택하고 이를 내러티브로 결합하는 계획을 수립하는 새로운 프레임워크를 제안한다.

###### Investigating Online Community Engagement through Stancetaking (https://aclanthology.org/2023.findings-emnlp.387/)
- Anthology ID: 2023.findings-emnlp.387 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 Reddit 커뮤니티에서 stance markers가 사용되는 문맥의 stance-relevant properties를 고려하지 않은 채로 커뮤니티 간의 유사성을 탐구한 대규모 컴퓨팅 작업에 대해 다룬다.
    2. 우리는 1798개의 Reddit 커뮤니티를 위한 stance context 표현을 제안하고, 이 표현이 텍스트나 marker 유사도 측정치와는 다른 커뮤니티 아이덴티티 패턴을 포착한다는 것을 보여준다.
    3. 또한, 우리는 stance context 표현을 cross-community posting patterns과 커뮤니티의 소셜 네트워크 특성과 연결해 보다 포괄적인 커뮤니티 간 및 커뮤니티 내 참여 패턴을 관찰한다. 우리의 연구 결과는 stance의 풍부한 특성을 이용하여 온라인 다중 커뮤니티 공간에서 커뮤니티 아이덴티티와 참여 패턴을 드러내는 데의 강점을 강조한다.

###### ASSERT: Automated Safety Scenario Red Teaming for Evaluating the Robustness of Large Language Models (https://aclanthology.org/2023.findings-emnlp.388/)
- Anthology ID: 2023.findings-emnlp.388 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델이 사회에 통합됨에 따라, 다양한 환경에서 신뢰성을 유지하기 위해 다양한 프롬프트에 대한 강건함 평가가 점점 중요해지고 있다. 
    2. 이 논문에서는 자동화된 안전 시나리오 레드팀인 ASSERT를 제안하며, semantic alignment augmentation, target bootstrapping, adversarial knowledge injection 등 세 가지 방법을 소개한다. 
    3. 이를 통해 AI 안전 분야에서 강건성 설정을 포괄적으로 커버하는 테스트 스위트를 알고리즘적으로 생성하고 모델 성능에 미치는 도메인 효과를 분석한다.

###### Learning to Correct Noisy Labels for Fine-Grained Entity Typing via Co-Prediction Prompt Tuning (https://aclanthology.org/2023.findings-emnlp.389/)
- Anthology ID: 2023.findings-emnlp.389 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 세부적인 entity typing (FET) 작업은 텍스트에서 entity에 의미적인 유형을 할당하는 것을 목표로 하는데, 이 작업에서는 labeling noise 문제가 있어 현재의 방법들은 노이즈 분포를 추정하여 잘못된 라벨을 식별하지만 다양한 노이즈 분포 편차로 혼란스러워한다.
    2. 우리는 FET에서 noise 수정을 위해 Co-Prediction Prompt Tuning을 소개하는데, 이는 여러 예측 결과를 활용하여 잘못된 라벨을 식별하고 수정한다.
    3. 실험 결과, 우리의 노이즈 수정 접근법은 먼 감독, ChatGPT, 크라우드소싱을 이용하여 주석을 단 다양한 유형의 훈련 샘플의 품질을 signficantly 향상시키는 것을 보여준다.

###### Co2PT: Mitigating Bias in Pre-trained Language Models through Counterfactual Contrastive Prompt Tuning (https://aclanthology.org/2023.findings-emnlp.390/)
- Anthology ID: 2023.findings-emnlp.390 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사회적 편향을 제거하기 위한 효과적이고 효율적인 debias-while-prompt tuning 방법인 Co2PT를 제안한다. 
    2. Co2PT는 downstream task에서 counterfactual contrastive prompt tuning을 통해 편향을 완화하는데 효과적이며, 기존 upstream debiased language model에 적용 가능한 적응성을 보여준다.
    3. 3가지의 extrinsic bias 벤치마크 실험을 통해 Co2PT의 bias 완화 역량을 입증하였으며, downstream task에서의 편향 완화를 위한 발전 가능성을 제공한다.

###### A Hierarchical Encoding-Decoding Scheme for Abstractive Multi-document Summarization (https://aclanthology.org/2023.findings-emnlp.391/)
- Anthology ID: 2023.findings-emnlp.391 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습 언어 모델 (PLM)은 추상적 단일 문서 요약 (SDS)에서 뛰어난 성과를 거두었다. 그러나 이러한 이점은 다중 문서 요약 (MDS)에 충분히 적용되지 않을 수 있다. 
    2. 이전 연구들은 새로운 MDS 아키텍처를 설계하거나 단순한 SDS 태스크로 PLM을 적용하는 방식을 사용했다. 그러나 전자는 이전 사전 학습의 노력을 활용하지 못하며, 후자는 MDS 태스크에 특유한 복잡한 문서 간 관계에 충분히 주의를 기울이지 못할 수 있다. 
    3. 대신에 우리는 PLM을 활용하여 MDS 작업을 위해 다중 문서 상호 작용을 더 잘 이용하기 위해 인코더와 디코더에 계층 구조를 강제로 적용한다. 다양한 도메인의 10개의 MDS 벤치마크에서 우리의 방법은 기존의 최고 모델보다 우수한 성능을 보여주었다.

###### Universal Domain Adaptation for Robust Handling of Distributional Shifts in NLP (https://aclanthology.org/2023.findings-emnlp.392/)
- Anthology ID: 2023.findings-emnlp.392 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 환경에 기계 학습 시스템을 배포할 때, 사용자가 알 수 없는 도메인에서 사전 지식을 효과적으로 활용하면서도 이상한 입력에 경고를 내놓는 것이 매우 바람직하다. 
    2. 컴퓨터 비전에서 지식 전이를 포함하는 UniDA(Universal Domain Adaptation) 기법은 주어진 도메인으로의 적응능력과 이상 값 검출능력을 동시에 달성하기 위해 연구되었다.
    3. 이 논문에서는 UniDA 기법을 자연어 입력에 적용해보고, 다양한 난이도와 특성을 가진 여러 데이터셋을 포함하는 종합적인 Natural Language benchmark를 제안한다.

###### Aligning Language Models to User Opinions (https://aclanthology.org/2023.findings-emnlp.393/)
- Anthology ID: 2023.findings-emnlp.393 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간과 상호작용하는 LLM을 개발하는 중요한 측면은 모델의 행동을 사용자에게 일치시키는 것이다. 
    2. 우리는 PEW 조사를 통해 사용자의 의견, 인구통계학적 특성, 이념과 상관관계가 서로 독립적임을 발견하였고, 이 통찰력을 활용하여 LLM을 사용자의 의견과 인구통계학적 특성, 이념으로 일치시키는 방법을 제안한다. 
    3. 우리의 연구는 사용자 의견을 언어 모델과 일치시키는 데 중요한 요소로 생각할 수 있는 연구 방향을 열어준다.

###### CCSRD: Content-Centric Speech Representation Disentanglement Learning for End-to-End Speech Translation (https://aclanthology.org/2023.findings-emnlp.394/)
- Anthology ID: 2023.findings-emnlp.394 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 심층 신경망은 음성 입력에서 특징을 추출하는 데에 성공했지만, 이러한 특징은 음성의 의미와 직접적으로 관련이 없는 음색과 화자 식별과 같은 비언어적인 요소를 포함할 수 있다.
    2. 이 논문에서는 음성 통역을 위해 음성 표현을 콘텐츠 중심의 구조로 분리하는 CCSRD라는 프레임워크를 제안한다. 이를 위해 음성의 콘텐츠 정보를 인코딩하는 콘텐츠 인코더, 비언어적 특징을 모델링하는 비콘텐츠 인코더, 그리고 순환 복원자, 특징 복원자, 화자 분류기로 구성된 구분 모듈을 활용하여 분리된 표현을 학습한다.
    3. MuST-C 벤치마크 데이터셋을 통한 실험 결과, CCSRD는 기준선 대비 두 가지 설정에서 다섯 가지 번역 방향에 걸쳐 평균 +0.9 BLEU의 성능 향상을 보여주며, 최첨단 엔드 투 엔드 음성 통역 모델과 단계별 모델을 능가한다.

###### Miracle: Towards Personalized Dialogue Generation with Latent-Space Multiple Personal Attribute Control (https://aclanthology.org/2023.findings-emnlp.395/)
- Anthology ID: 2023.findings-emnlp.395 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 개인화된 대화 시스템은 챗봇 에이전트가 인간과 유사한 상호작용을 할 수 있도록 하는 것을 목표로 한다. 그러나 기존 접근 방식은 문장 설명을 사용하여 사용자 프로필 모델링, 사용자 임베딩의 암묵적 유도, 또는 ChatGPT와 같은 모델에 대한 수작업 프롬프트를 사용하고 있다.
    2. 이 논문에서는 복잡한 개인화된 대화 생성 작업을 수행하기 위해 Miracle 이라는 새로운 방법론을 제안한다. 이 방법은 복잡한 성격을 여러 가지 다양한 속성으로 분리하고, 조건부 변분 오토인코더를 사용하여 잠재적인 속성 공간 내의 밀집 개인화된 응답과 조화를 이룬다.
    3. 실험 결과, Miracle은 성격의 조절 가능성과 응답 생성 품질 측면에서 몇 가지 강력한 기준선을 능가한다.

###### Towards Multilingual Interlinear Morphological Glossing (https://aclanthology.org/2023.findings-emnlp.396/)
- Anthology ID: 2023.findings-emnlp.396 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인터리니어 형태 밝힘 (Interlinear Morphological Glosses)은 언어 문서화 작업에서 만들어진 주석이다. 이 논문에서는 이러한 주석을 자동으로 생성하는 작업을 연구하고 있다.
    2. 형태 밝힘 생성을 위해 Conditional Random Field (CRF)를 사용하며, 이를 통해 L1 모포(morphs)를 레이블링하고 동시에 L2 단어에 매치시키고 있다.
    3. 저자들은 이러한 접근법이 몇 가지 저리어 데이터에서 효과적이며 데이터 효율성도 높아지며, 알려지지 않은 모포(morphs)에 주석을 달기 어려운 문제도 해결할 수 있음을 실험적으로 보여주고 있다.

###### Transformer Working Memory Enables Regular Language Reasoning And Natural Language Length Extrapolation (https://aclanthology.org/2023.findings-emnlp.397/)
- Anthology ID: 2023.findings-emnlp.397 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 RNN 모델과 달리, Transformer는 완벽히 정규 언어(regular languages)를 모델링할 수 없다고 알려져 있으나, 이 논문에서는 RegularGPT라는 새로운 Transformer 변형 모델을 제안한다.
    2. RegularGPT는 Weight-Sharing, Adaptive-Depth, Sliding-Dilated-Attention이라는 새로운 기법을 결합하여 규칙 언어 (PARITY와 같은)를 효과적으로 모델링할 수 있는 작업 메모리 (working memory)를 구축한다.
    3. 또한 RegularGPT를 자연어 길이 외삽(natural language length extrapolation) 작업에 적용하여, 이전 연구에서 길이 외삽에 필요하다고 여겨져 오던 로컬 윈도우어 어텐션 효과를 재발견하는 것으로 나타냈다.

###### Enhancing Conversational Search: Large Language Model-Aided Informative Query Rewriting (https://aclanthology.org/2023.findings-emnlp.398/)
- Anthology ID: 2023.findings-emnlp.398 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 검색을 향상시키기 위해 질문 재작성은 맥락-의존 사용자 질문을 독립적인 형태로 변환하는 데 중요한 역할을 한다. 
    2. 기존 방법은 사람이 재작성한 질문을 사용하여 모델을 훈련시키지만, 이러한 인간 재작성은 최적의 검색 성능을 위한 충분한 정보를 갖지 못할 수 있다. 
    3. 이 논문에서는 큰 언어 모델을 쿼리 재작성 도구로 사용하여 잘 설계된 지시사항을 통해 정보성 있는 쿼리 재작성을 생성하는 방법을 제안한다. 게다가 초기 쿼리 재작성이 있는 경우에는 LLM의 수정 편집자 역할을 도입하여 "재작성 후 편집" 프로세스를 형성한다.

###### Distilling ChatGPT for Explainable Automated Student Answer Assessment (https://aclanthology.org/2023.findings-emnlp.399/)
- Anthology ID: 2023.findings-emnlp.399 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동화된 학생 답안 평가를 위해 명시적이고 정확한 피드백을 제공하는 것은 매우 중요하다.
    2. 이 논문에서는 ChatGPT, 즉 최첨단 대형 언어 모델을 사용하여 학생 답안 점수화와 근거 생성을 동시에 수행하는 새로운 프레임워크를 소개한다.
    3. 실험 결과 및 인간 평가를 통해 우리의 방법이 ChatGPT의 근거 생성 결과와 비교 가능하다는 것을 보여준다. 우리의 접근 방식은 교육에서 설명 가능한 자동 평가를 구현하기 위한 실질적인 해결책을 제공한다.

