# Korean Three-Line Summarizations of Papers 1687-1786 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Co-training and Co-distillation for Quality Improvement and Compression of Language Models (https://aclanthology.org/2023.findings-emnlp.500/)
- Anthology ID: 2023.findings-emnlp.500 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 전달 기법인 Knowledge Distillation(KD)의 성능을 향상시키기 위해 Co-Training and Co-Distillation(CTCD)이라는 새로운 프레임워크를 제안한다. 
    2. CTCD 프레임워크는 두 개의 모델을 동시에 학습시키고 상호적으로 지식을 전달함으로써 성능과 추론 속도를 모두 향상시킨다.
    3. CTCD는 기존 방법들과 결합하여 성능을 더욱 향상시킬 수 있으며, GLUE 벤치마크에서 CTCD로 훈련된 작은 모델이 원래의 큰 모델보다 더 우수한 성능을 보여준다는 결과를 보여준다.

###### ReadPrompt: A Readable Prompting Method for Reliable Knowledge Probing (https://aclanthology.org/2023.findings-emnlp.501/)
- Anthology ID: 2023.findings-emnlp.501 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Pre-trained language models (PLMs)를 통해 지식을 파악하는 task에서 기존 방법들은 prompt의 가독성을 희생시키는 문제가 있었다. 이 논문에서는 ReadPrompt라는 새로운 방법을 제안하여 의미 있는 문장을 prompt로 선택함으로써 가독성을 개선하였다.
    2. ReadPrompt는 현재 지식 파악 벤치마크에서 최고 수준의 성능을 얻을 수 있었다. 또한, 가독성이 높아져 prompt와 실제 지식에 대한 불일치를 발견할 수 있었으며 이는 공격 실험을 통해 기존 접근법의 불신성을 보여준다.
    3. 따라서, 현재의 prompting 방법으로 얻은 지식 파악 결과는 PLMs에 포함된 지식을 과대평가한다고 주장한다.

###### Coherent Entity Disambiguation via Modeling Topic and Categorical Dependency (https://aclanthology.org/2023.findings-emnlp.502/)
- Anthology ID: 2023.findings-emnlp.502 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 entity disambiguation (ED) 방법은 mention context와 후보 entity 간의 일치도에 기반한 판별적 패러다임을 채택하지만, 명확한 문맥 수준의 의존성을 포착하는 데 어려움을 겪어 추상적인 수준에서 일관성 없는 예측 결과를 보인다. 
    2. 우리는 CoherentED라는 ED 시스템을 제안하여 엔티티 예측의 일관성을 향상하는 새로운 디자인을 도입한다. 
    3. 우리는 먼저 무감독적인 variational autoencoder(VAE)를 도입하여 문맥 문장의 latent topic vector를 추출하고, 익숙하지 않은 멘션에 대한 관련 카테고리를 검색할 수 있는 외부 카테고리 memory를 통합한다. 이러한 디자인은 엔티티간 상호작용을 모델링하고 카테고리 수준에서 최대한의 일관성을 유지하도록 도움을 준다.

###### How Predictable Are Large Language Model Capabilities? A Case Study on BIG-bench (https://aclanthology.org/2023.findings-emnlp.503/)
- Anthology ID: 2023.findings-emnlp.503 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 실험 구성에서 대형 언어 모델(Large Language Model; LLM)의 성능을 정확하게 예측할 수 있는가? 이 질문의 답은 LLM 사용자, 개발자 및 연구 커뮤니티에 실용적인 영향을 미친다. 
    2. 연구에서는 BIG-bench 실험 기록을 사용하여 성능 예측 문제를 연구하였으며, MLP 기반 예측기를 사용하여 학습 가능한 패턴의 존재를 확인했다. 
    3. 또한, "small-bench"라고 불리는 작은 부분집합을 찾아 LLM 성능을 최대로 복원할 수 있는데, 이를 위해 MLP 기반 예측기를 통해 학습된 작업 표현을 군집화하고 클러스터 중심에 가까운 작업들을 선정하여 경쟁력 있는 부분집합을 찾아냈다.

###### POSQA: Probe the World Models of LLMs with Size Comparisons (https://aclanthology.org/2023.findings-emnlp.504/)
- Anthology ID: 2023.findings-emnlp.504 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "음체된 언어 이해는 단순히 뇌의 정신적 처리가 아니라 물리적 및 사회적 환경과의 상호작용도 포함된다는 것을 강조한다. 이 논문에서는 최신 대형 언어 모델의 현실 세계 이해력을 확인하기 위해 단순한 크기 비교 질문을 다룬 Physical Object Size Question Answering 데이터셋인 POSQA를 제안한다."
    2. "최신 대형 언어 모델들은 제로샷 설정에서 실망스런 성과를 보인다. 따라서 우리는 고급 프롬프팅 기법과 외부 지식 보완을 통해 그 한계를 넓히려고 한다."
    3. "또한, 문맥 정보와 내부 가중치 중 어느 쪽이 현실 세계 이해력에 주로 기여하는지, 프롬프트 형식의 영향 및 다른 객체의 보고 편향을 분석하였다. 결과적으로 표면 형태의 프롬프트로 인해 LLM 대형 언어 모델들의 현실 세계 이해력이 속임수와 혼란에 취약하며, 이는 인간 행동과 덜 일치한다는 것을 확인하였다."

###### Hierarchical Fusion for Online Multimodal Dialog Act Classification (https://aclanthology.org/2023.findings-emnlp.505/)
- Anthology ID: 2023.findings-emnlp.505 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 음성과 ASR로 생성된 텍스트를 기반으로하는 온라인 다중 모달 대화 행위 (DA) 분류를위한 프레임 워크를 제안한다. 기존의 다중 모달 DA 분류 접근법은 효과적인 오디오 모델링과 늦은 단계 퓨전에 의해 제한되고 있다.
    2. 우리는 모달리티를 더 세분화하여 통합하고, 오디오 특성 추출을 위해 최근의 대형 언어 및 오디오 모델의 발전을 포함하여 다중 모달 DA 분류에서 상당한 개선을 보여준다.
    3. 우리는 DA 분류를 위해 발화와 대화를 모델링하기위한 self-attention 및 cross-attention 메커니즘의 효과도 조사한다. MRDA와 EMOTyDA라는 두 가지 유명한 DA 분류 데이터셋에서 현재의 최첨단 모델과 비교하여 F1 스코어가 3 퍼센트 포인트 증가한다.

###### STEER: Unified Style Transfer with Expert Reinforcement (https://aclanthology.org/2023.findings-emnlp.506/)
- Anthology ID: 2023.findings-emnlp.506 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 스타일 전환은 자연어 처리에서 다양한 응용 분야가 있지만, 단일 소스 스타일에서의 전환은 실제 세계에서는 현실적이지 않은 가정이다.
    2. STEER는 제한된 병렬 데이터에 대한 도전을 극복하기 위해 개발된 통합 프레임워크로, 임의의, 알려지지 않은 스타일에서 목표 스타일로 텍스트를 다시 작성하는 임무에 초점을 맞추고 있다.
    3. STEER는 단일 소스 스타일로부터 다양한 목표 스타일로 전환이 가능하며, 실험 결과는 다양한 스타일의 도전적인 데이터셋에서 경쟁력 있는 기준과 비교했을 때 최고 수준의 결과를 보여준다.

###### Enhancing Argument Structure Extraction with Efficient Leverage of Contextual Information (https://aclanthology.org/2023.findings-emnlp.507/)
- Anthology ID: 2023.findings-emnlp.507 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Argument structure extraction (ASE)은 문서 내에서 인식된 논쟁 구조를 식별하는 것을 목표로 한다. 이전 연구에서는 문맥 정보가 효과적인 ASE 모델을 개발하는 데 중요하다는 것을 보였다.
    2. 그러나 우리는 단순히 문맥 창에 있는 문장을 연결하는 것만으로는 문맥 정보를 충분히 활용하지 못하고 때로는 덜 정보성 있는 문장에 과도한 집중을 할 수 있다는 것을 관찰하였다.
    3. 우리는 이 도전을 해결하기 위해, 모델링 능력을 향상시키고 훈련 데이터를 증강시킴으로써 완전히 문맥 정보를 활용하는 효율적인 ECASE 모델을 제안한다. 또한 우리는 훈련 데이터를 특정 단어나 덜 정보성 있는 문장에 의존하지 않도록 논평 표지점과 문장을 무작위로 마스킹하여 데이터를 증강시킨다. 다양한 도메인의 다섯 개 데이터셋에서의 실험은 우리 모델이 최고의 성능을 달성하는 것을 보여준다. 또한, 부분 제거 연구는 우리 모델의 각 모듈의 효과를 확인한다.

###### Examining Inter-Consistency of Large Language Models Collaboration: An In-depth Analysis via Debate (https://aclanthology.org/2023.findings-emnlp.508/)
- Anthology ID: 2023.findings-emnlp.508 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large Language Model)들은 다양한 응용분야에서 놀라운 성능을 보이고 있지만, 여전히 불일치 문제에 직면한다. 우리는 기존 연구들이 LLM 내부의 불일치 문제에 초점을 맞추었다면, 우리는 여러 개의 LLM들 간의 상호적일관성에 주목하여 협업을 탐구한다.
    2. 우리는 LLM들이 공통 목표를 위해 효과적으로 협업하여 합의를 도출할 수 있는지 검토하기 위해 상식적 추론에 초점을 맞추고 형식적 토론(FORD) 프레임워크를 소개한다.
    3. 우리의 실험결과는 LLM들이 상호적 불일치에도 불구하고 합의에 도달하기 위해 효과적으로 협업할 수 있다는 것을 보여주지만, 능력의 균형이 불균형해서 뛰어난 LLM에게 지배될 수 있다. GPT-4와 같은 더욱 발전된 LLM을 권위적인 판단자로 활용하면 협업 성능을 향상시킬 수 있다.

###### Culturally Aware Natural Language Inference (https://aclanthology.org/2023.findings-emnlp.509/)
- Anthology ID: 2023.findings-emnlp.509 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들은 특정 문화적 맥락에서 언어를 생산하고 소비한다. 이러한 문화적 맥락의 인식은 의사소통에 있어서 매우 중요하다.
    2. 현재의 연구는 텍스트의 문화적 해석에 어떤 인과관계가 있는지 연구하지 않고 문화적 지식 베이스를 구축하는 데에 초점을 맞추고 있다.
    3. 이 연구에서는 문화적 변이를 자연어 이해(NLI) 작업을 통해 구체화하고, 미국과 인도에 위치한 두 가지 문화 그룹의 주장-가설 쌍을 포함한 첫 번째 문화적 자연어 추론(CALI) 데이터셋을 소개한다.

###### End-to-End Autoregressive Retrieval via Bootstrapping for Smart Reply Systems (https://aclanthology.org/2023.findings-emnlp.510/)
- Anthology ID: 2023.findings-emnlp.510 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템에서 댓글 제안 시스템은 매우 중요한 부분이지만, 기존의 검색 아키텍처는 개별 메시지-댓글 유사성만 고려하기 때문에 이러한 작업에 적합하지 않다. 결과적으로 이러한 시스템은 다양한 출력을 얻기 위해 추가적인 후처리 모듈에 의존하게 된다. 하지만 이러한 접근 방식은 초기 검색 모델의 성능에 의해 제약받으며, 다운스트림 다양화 모듈에 충분히 다양한 옵션을 제시하지 못하여 사용자에게 적합하지 않은 제안을 제공하게 된다. 이 논문에서는 텍스트-텍스트 추론 모델인 자동 회귀형 토크 수집 모델을 사용하여 이러한 문제를 극복한다.
    2. 이 논문에서는 자동 회귀형 토크 수집 모델을 사용하여 데이터셋에서 스마트 리플라이 작업을 end-to-end로 학습하는 새로운 접근 방식을 제안한다.
    3. 실험 결과, 이 방법은 성능이 우수한 베이스라인 방법과 비교하여 관련성에서 5.1%-17.9% 향상, 다양성에서 0.5%-63.1% 향상을 보여주었다. 이 코드는 공개적으로 이용 가능하다.

###### Evaluating Dependencies in Fact Editing for Language Models: Specificity and Implication Awareness (https://aclanthology.org/2023.findings-emnlp.511/)
- Anthology ID: 2023.findings-emnlp.511 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large Language Model, LLM)을 지식 기반(Knowledge Base, KB)으로 사용하는 잠재력이 큰 관심을 불러일으켰다. LLM에서 습득한 지식을 유지하기 위해서는 학습된 사실의 편집이 내부적인 논리적 제약조건을 준수해야 하는데, 이는 지식의 의존성(dependency of knowledge)로 알려져 있다. 
    2. 기존 연구에서는 사실의 편집이 관련 없는 것들을 방해하지 않으면서 그것의 단어 변형에 적용되어야 한다는 의존성 문제를 부분적으로 해결하였지만, 사실과 그 논리적 함축사이의 의존성을 간과하고 있다. 
    3. 이 논문에서는 의존성 개념을 고려한 편집 과정을 포괄적으로 평가하기 위한 StandUp이라는 질문-답변 데이터셋과 평가 프로토콜을 제안한다. StandUp에서는 판단규칙을 기반으로 편집된 사실의 영향과 논리적 함축사이의 관계를 감시하는 통제된 환경을 구축한다. StandUp 기반의 실험 결과, 기존의 지식 편집 방법은 지식의 표면 형태에 민감하며, 편집된 사실의 함축사를 추론하는 능력이 제한적임을 보여준다.

###### Effects of Human Adversarial and Affable Samples on BERT Generalization (https://aclanthology.org/2023.findings-emnlp.512/)
- Anthology ID: 2023.findings-emnlp.512 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. BERT 기반 모델들은 리더보드에서 성능이 우수하지만, 일반화를 필요로 하는 실제 환경에서는 성능이 떨어진다. 이 논문에서는 일반화를 위해 학습 데이터의 양보다는 품질에 초점을 맞춘다. 
    2. 그들은 훈련 데이터의 두 가지 특성인 h-adversarial (서로 다른 ground-truth 레이블을 가지지만 보이지 않는 차이가 있는 샘플 pair)와 h-affable (같은 ground-truth 레이블을 가지지만 작은 차이가 있는 샘플 pair)에 대한 영향을 조사하였다. 
    3. 실험 결과, 학습 샘플의 수가 일정한 경우, 10-30%의 h-adversarial이 있다면 텍스트 분류와 관계 추출 작업에서 F1 점수를 최대 20 포인트 향상시킬 수 있다는 것을 발견하였다. 그러나 이 범위를 넘어서면 성능이 정체되거나 저하될 수 있다. 반면에, h-affables은 일반화 성능에 기여하지 않을 뿐만 아니라 일반화 성능을 저하시킬 수도 있다.

###### Logic Unveils Truth, While Disguise Obscures It: Transition Logic Augmented Response Selection for Multi-Turn Dialogue (https://aclanthology.org/2023.findings-emnlp.513/)
- Anthology ID: 2023.findings-emnlp.513 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 턴 응답 선택은 후보 풀에서 대화 맥락에 대한 응답을 검색하는 작업이다. 하지만 이전 방법들에서는 오픈 도메인 대화에서의 one-to-many 속성으로 인해 false negative가 발생하여 최적화 과정에 영향을 미친다.
    2. 이 논문에서는 순차적 변분 계단 자동인코더를 제안하여 오픈 도메인 대화의 다양한 특성의 one-to-many 전이 패턴을 포착한다. 이를 통해 학습된 전이 논리는 변장한 잠재적인 양성 예시를 식별하는 데 도움을 준다.
    3. 또한, 우리는 TRIGGER 프레임워크를 제안하여 모델 용량에 따라 false negative의 범위를 동적으로 업데이트하여 훈련 과정에서 부정적인 샘플링을 조정한다. 두 가지 벤치마크에서 수행된 실험은 우리의 방법의 효과를 검증한다.

###### Are Language Models Worse than Humans at Following Prompts? It’s Complicated (https://aclanthology.org/2023.findings-emnlp.514/)
- Anthology ID: 2023.findings-emnlp.514 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구에서는 일부러 무의미하거나 오도하는 prompt를 주어진 경우에도 모델이 놀랍도록 잘 수행할 수 있다는 것을 발견하였다. 이러한 결과는 모델의 행동이 "인간처럼"이 아님을 증거로 볼 수 있다. 
    2. 본 연구에서는 이러한 연구의 가설 중 하나를 도전하며, 인간들이 병적인 지시사항을 주어진 경우에도 잘 수행할 수 있다는 사실을 발견하였다.
    3. 따라서, 무의미한 prompt로 높은 성능을 얻는 것은 모델의 지시 이해에 반하는 것이 아니라고 주장하지만, 모델이 오도하는 지시를 따르지 않는 것은 우려를 증가시킨다고 강조한다.

###### A Sequence-to-Structure Approach to Document-level Targeted Sentiment Analysis (https://aclanthology.org/2023.findings-emnlp.515/)
- Anthology ID: 2023.findings-emnlp.515 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 document-level의 targeted sentiment analysis task를 다루었으며, review 문서에서 다중 수준 entity로 이루어진 opinion targets를 추출하고 그들의 sentiment를 예측하는 것을 목표로 한다.
    2. 우리는 Seq2Struct 방법론을 제안하는데, 이 방법론은 다중 opinion targets 간의 계층 구조를 명시적으로 모델링하고 문장 간의 관련된 entity 간의 장거리 종속성을 포착할 수 있다.
    3. 실험 결과, 우리의 Seq2Struct 방법은 다양한 사전 훈련 모델과 비교하여 우수한 성능을 보여주며, opinion targets의 다중 수준 target-sentiment pairs를 명시적으로 나타낼 수 있는 장점이 있다.

###### Generating Extractive Answers: Gated Recurrent Memory Reader for Conversational Question Answering (https://aclanthology.org/2023.findings-emnlp.516/)
- Anthology ID: 2023.findings-emnlp.516 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화형 질의응답(CQA)은 전통적인 단일 턴 기계 독해(MRC)보다 복잡한 작업이다. CQA 모델은 대화 기록에 따라 주어진 컨텐츠에서 답변을 추출하여 후속 질문에 대답해야 한다.
    2. GRMR은 기존 추출형 MRC 모델을 일반화된 시퀀스-투-시퀀스 프레임워크에 통합하는 새로운 아키텍처이다. 이 모델은 이전 질문과 답변을 단순히 연결하는 대신, 적은 저장 공간을 사용하고 과거 기억을 깊게 선택적으로 고려할 수 있다.
    3. CoQA 데이터셋에서의 실험 결과, 우리 모델은 가장 적은 공간을 차지하면서 대부분의 모델과 비슷한 결과를 달성한다.

###### Text2Tree: Aligning Text Representation to the Label Tree Hierarchy for Imbalanced Medical Classification (https://aclanthology.org/2023.findings-emnlp.517/)
- Anthology ID: 2023.findings-emnlp.517 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의료 텍스트 분류에서 Deep learning 기법들은 많은 text 태스크에서 유망한 성능을 보이지만, 심하게 불균형하고 부족한 샘플로 인해 여전히 어려움을 겪고 있다.
    2. 기존 방법들이 외부 의료 정보와 함께 보조 의미를 중점으로 하게 되는 반면, 본 논문은 의료 텍스트의 데이터 문제를 다시 생각하고, 내부 레이블 계층을 deep learning 모델 학습에서만 활용하는 Text2Tree라는 새로운 framework agnostic 알고리즘을 제안한다.
    3. 실험 결과, 공식적인 공개 데이터셋과 실제 의료 기록에서 우리의 접근 방식이 고전적인 imbalance classification 방법보다 우수한 성능을 일관되게 보였다.

###### Impact of Co-occurrence on Factual Knowledge of Large Language Models (https://aclanthology.org/2023.findings-emnlp.518/)
- Anthology ID: 2023.findings-emnlp.518 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델들은 다양한 응용 분야에서 성공을 거두었지만, 사실적인 오답을 많이 내놓는 경향이 있다. 우리는 사전 훈련 데이터의 간단한 동시 발생 통계에 지나치게 의존하는 것이 오류 발생의 주된 요인 중 하나라는 가설을 세우고 있다.
    2. 우리의 결과는 자주 동시 발생하는 단어들을 올바른 대답보다 선호한다는 co-occurrence bias에 취약하다는 것을 보여준다. 따라서 LLM은 사전 훈련 데이터에서 주어와 목적어가 드물게 동시 발생하는 사실을 기억하기 어렵다.
    3. 우리는 바이어스가 낮은 데이터셋에서 재조정(finetuning)하여 바이어스를 완화시키는 것을 제안한다. 또한, 훈련 중보지 않은 드문 사실을 재조정 후에 기억하기 위해서는 추가적인 연구가 필요하다.

###### CTQScorer: Combining Multiple Features for In-context Example Selection for Machine Translation (https://aclanthology.org/2023.findings-emnlp.519/)
- Anthology ID: 2023.findings-emnlp.519 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 몇 가지 예시로 입력된 경우에 대형 언어 모델은 기계 번역을 수행할 수 있음을 보였다. 그러나 번역 품질은 예시의 품질과 관련성과 같은 다양한 특성에 따라 다르며, 기존 연구는 주로 개별 특성에 중점을 두었다.
    2. 이 논문에서는 예시 선택에 영향을 미치는 다양한 특성을 결합하는 일반적인 프레임워크를 제안한다.
    3. 실험 결과, CTQ Scorer는 무작위 선택과 문헌에서 보고된 강력한 단일 요인 베이스라인보다 훨씬 우수한 성능을 보여준다. 또한 강력한 BM25 검색 기반 베이스라인과 비교하여 평균적으로 2.5 COMET 점수 향상을 확인할 수 있다.

###### Swap and Predict – Predicting the Semantic Changes in Words across Corpora by Context Swapping (https://aclanthology.org/2023.findings-emnlp.520/)
- Anthology ID: 2023.findings-emnlp.520 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단어의 의미는 시간과 도메인에 따라 변할 수 있고, 단어의 의미변화를 감지하는 것은 시간에 민감한 NLP 애플리케이션에서 중요한 작업이다.
    2. 두 개의 텍스트 corpus에서 주어진 대상 단어가 의미를 변화시키는지 예측하는 문제를 고려하고, 매스킹된 언어 모델의 컨텍스트화된 단어 임베딩의 분포를 살펴봄으로써 단어 의미의 변화를 예측할 수 있다.
    3. 사전 훈련된 언어 모델을 사용하여 실제로 fine-tuning을 하지 않고도 제안한 컨텍스트 교환 방법은 네 개의 언어(영어, 독일어, 스웨덴어, 라틴어)와 다른 시간 범위(50년 이상, 약 5년)에서 단어 의미 변화를 정확하게 예측할 수 있다.

###### Beyond Layout Embedding: Layout Attention with Gaussian Biases for Structured Document Understanding (https://aclanthology.org/2023.findings-emnlp.521/)
- Anthology ID: 2023.findings-emnlp.521 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 구조화된 문서 이해에서 layout 정보를 효과적으로 인코딩하는 것은 중요한 문제이다. 하지만, 기존 방법들은 수백만 개의 학습 가능한 parameter를 필요로 하고 있는데, 이를 반드시 필요한 것인지 의문이 남아있다.
    2. 이 논문에서는 극좌표가 카르테시안 좌표에 비해 상대적인 위치를 더 효과적으로 측정할 수 있기 때문에 더 나은 선택임을 알아냈다. 또한, 거리와 각도를 2D 가우시안 커널에 입력하여 layout 편향을 모델링하여 텍스트의 주변에 더 집중할 수 있도록 하는 방법을 제안한다.
    3. LAGaBi는 transformer 기반 모델에 적용 가능하며, BERT 및 LayoutLM과 같은 다양한 모델에 대해 수행되는 실험 결과에서 수백만 개의 layout parameter를 48개로 줄인 LAGaBi가 경쟁력 있는 성능을 달성한다.

###### ESPVR: Entity Spans Position Visual Regions for Multimodal Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.522/)
- Anthology ID: 2023.findings-emnlp.522 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Multimodal Named Entity Recognition (MNER)은 텍스트-only Named Entity Recognition (NER)의 성능을 향상시키기 위해 시각적 정보를 활용한다. 그러나 기존의 로컬 시각 정보 확보 방법은 다음과 같은 한계가 있다."
    2. "이 논문에서는 Entity Spans Position Visual Regions (ESPVR) 모듈을 제안하여 텍스트에 해당하는 가장 관련성 높은 시각적인 지역을 확보할 수 있다. 실험 결과, 제안된 방법은 Twitter-2017에서 최고 성능을 달성하고, Twitter-2015에서 경쟁력 있는 결과를 보여준다."
    3. "(ESPVR 모듈은) 시각적인 기존 방법들과 달리 문장 내 entity와 관련된 시각적인 영역을 정확히 확보할 수 있다."

###### Flatness-Aware Prompt Selection Improves Accuracy and Sample Efficiency (https://aclanthology.org/2023.findings-emnlp.523/)
- Anthology ID: 2023.findings-emnlp.523 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델의 능력이 증가함에 따라, 언어 프롬프트(prompt)를 사용하는 것이 점점 주류화되고 있다. 따라서 효과적인 언어 프롬프트를 자동으로 선택하는 전략들이 개발되고 있다.
    2. 이 논문에서는 언어 프롬프트의 기대 효용을 측정하기 위해 새로운 평가 지표인 pFlat을 소개한다. 이 메트릭은 통계 학습에서 모델의 매개 변수 변동에 대한 강건성을 측정하는 flatness 정규화에서 영감을 받았다.
    3. 실험적으로, pFlat을 기존 메트릭과 결합하면 성능과 샘플 효율성이 모두 개선됨을 보여준다. 6개의 분류 벤치마크에서 10%의 피어슨 상관 관계 평균 증가 및 기존 메트릭 대비 5% 더 높은 정확도를 가진다.

###### Detecting Erroneously Recognized Handwritten Byzantine Text (https://aclanthology.org/2023.findings-emnlp.524/)
- Anthology ID: 2023.findings-emnlp.524 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 손글씨 텍스트 인식(HTR)은 인쇄된 텍스트인 OCRed 텍스트와 비교하여 오류가 훨씬 많이 발생한다. 본 연구에서는 비잔틴 그리스어에서 이러한 문제점을 조사하고 오류 감지를 학습하는 텍스트 분류 시스템을 실험한다.
    2. 현대 그리스어로 사전 훈련한 대규모 마스킹된 언어 모델이 평균 정밀도 점수 95%를 달성한다고 보고한다.
    3. 문서 분석 결과, 고대 그리스어로 사전 훈련한 모델이 오래된 세기의 텍스트에 대해 분류기에서 유리한 결과를 나타낸다. 이 분류기를 손글씨 텍스트 후처리기 앞에 적용하면 후처리 오류를 크게 줄일 수 있다.

###### Improving Factual Consistency for Knowledge-Grounded Dialogue Systems via Knowledge Enhancement and Alignment (https://aclanthology.org/2023.findings-emnlp.525/)
- Anthology ID: 2023.findings-emnlp.525 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델 (PLMs) 기반의 지식 주도형 대화 시스템은 지식 소스와 일치하지 않는 응답을 생성하기 쉽다. 이 연구는 Transformers 내의 FFNs (feedforward networks)가 사실적인 지식 표현에 책임이 있다는 이전 연구를 바탕으로, FFN의 사실적인 표현 능력을 향상시키기 위한 두 가지 방법을 조사한다.
    2. 첫 번째로, 특정한 지식-주도 대화 입력 패턴에 따라 사실적인 지식 표현을 강화하기 위해 Transformers 내에 확장된 FFNs를 도입하는 K-Dial을 제안한다.
    3. RLFC (reinforcement learning for factual consistency) 방법을 적용하여 응답에서 FFN의 표현을 직접적으로 실제 지식에 일치시키고, 지식의 일관성 선호도에 맞게 조정한다. WoW와 CMU_DoG 데이터셋에서의 실험 결과는 우리의 방법이 FFN 모듈의 지식 전달 능력을 효과적으로 향상시키는 것을 보여주며, 지식 주도형 대화 시스템의 사실적인 일관성을 향상시키는 효과를 검증한다.

###### TRIP: Accelerating Document-level Multilingual Pre-training via Triangular Document-level Pre-training on Parallel Data Triplets (https://aclanthology.org/2023.findings-emnlp.526/)
- Anthology ID: 2023.findings-emnlp.526 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 다국어 시퀀스 투 시퀀스 사전 학습 방법은 문서 수준의 단일 언어 말뭉치와 문장 수준의 양방향 말뭉치, 때로는 합성 문서 수준 양방향 말뭉치를 사용하는 경우가 많은데, 이는 문서 수준의 번역과 같은 크로스-언어 문서 수준 태스크에서의 성능 향상을 저해한다.
    2. 우리는 문서 수준 삼중 언어 병렬 말뭉치를 찾아 활용하여 시퀀스 투 시퀀스 다국어 사전 학습을 개선하는 방법을 제안한다.
    3. 실험 결과, 우리의 방법은 다국어 문서 수준 기계 번역 벤치마크와 교차 언어 요약 벤치마크에서 강력한 최고 수준 점수를 달성하며, 최대 3.11 d-BLEU 포인트와 8.9 ROUGE-L 포인트의 개선을 보여준다.

###### Frequency Balanced Datasets Lead to Better Language Models (https://aclanthology.org/2023.findings-emnlp.527/)
- Anthology ID: 2023.findings-emnlp.527 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. attention 기반 transformer 언어 모델을 훈련하기 위해 필요한 데이터 양의 역할을 이해하기 위해 실험을 수행한 결과를 보고한다.
    2. 매우 높은 빈도로 등장하는 토큰이 학습에 부정적인 영향을 미칠 수 있다는 이전 연구들의 지적을 고려하여, pre-training 데이터에서 높은 빈도의 토큰을 줄이기 위한 샘플링 전략의 영향을 조사했다.
    3. 결과적으로, 균형 잡힌, 언어적으로 올바른 데이터셋으로 pre-training 하는 것이 pre-training 데이터 양을 최대 3배 줄일 수 있었음을 실험 결과를 통해 보였다.

###### Uncertainty-aware Parameter-Efficient Self-training for Semi-supervised Language Understanding (https://aclanthology.org/2023.findings-emnlp.528/)
- Anthology ID: 2023.findings-emnlp.528 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 사전 학습 언어 모델(PLMs)의 최근 성공은 주로 대량의 라벨이 달린 데이터에 의존하는데, 이는 보통 저자원 상황에서는 성능이 떨어지는 문제점을 가지고 있다.
    2. 이 논문에서는 UPET라는 새로운 Unsertainty-aware Parameter-Efficient self-Training 프레임워크를 제안하여 라벨이 달린 데이터 부족 문제를 효과적으로 해결하는데, Monte Carlo 드롭아웃을 활용하여 신뢰도가 높은 가짜 라벨을 선택한다.
    3. 실험 결과, UPET은 효율성과 성능 면에서 상당한 개선을 보여주었다. (GitHub: https: //github.com/wjn1996/UPET)

###### TR-Rules: Rule-based Model for Link Forecasting on Temporal Knowledge Graph Considering Temporal Redundancy (https://aclanthology.org/2023.findings-emnlp.529/)
- Anthology ID: 2023.findings-emnlp.529 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시간적 지식 그래프(TKG)는 실제 세계의 동적 사실을 모델링하는 데 효과적인 방법으로 증명되었습니다. 본 논문에서는 TKG에서 미래 이벤트(외삽)를 예측하는 데 많은 노력이 기울여졌습니다.
    2. 기존의 임베딩 기반 방법보다 해석 가능성이 높다고 여겨지는 rule 기반 지식 그래프 외삽 방법도 최근에는 TKG에 전이되었습니다. 그러나 rule 기반 모델은 동적인 설정에서 사용될 때 시간적 중복으로 인해 정확하지 않은 rule 신뢰도 계산을 초래합니다.
    3. 본 논문에서는 시간적 중복 문제를 해결하는 간단하고 효과적인 전략을 제시하고, 순환적인 rule 외에도 non-cyclic rule을 적절하게 탐지하고 활용하여 더 많은 정보를 모델링하는 방법을 제안합니다. 실험 결과, TR-Rules은 세 가지 기준에 대해 최상의 성능을 달성하였습니다.

###### On the Transferability of Visually Grounded PCFGs (https://aclanthology.org/2023.findings-emnlp.530/)
- Anthology ID: 2023.findings-emnlp.530 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 시각적으로 기반된 문법 유도에 대한 관심이 크게 증가했으나, 이 작업에 사용된 모델들은 훈련 도메인과 다른 텍스트 도메인에서의 성능을 평가받지 못했기 때문에 시각적 기반의 개선이 얼마나 전이 가능한지 알 수 없다.
    2. 이 연구는 시각적 기반의 개선이 얼마나 전이 가능한지를 평가하기 위해 VC-PCFG 모델을 타겟 도메인에 직접 적용하는 zero-shot 전이 학습 설정에서 실험을 진행했다. 
    3. 실험 결과, 시각적 기반의 이점은 훈련 도메인과 유사한 도메인의 텍스트에 전이되지만, 원격 도메인에는 전이되지 않는 것으로 나타났다. 또한, 도메인 간의 렉서스 오버랩이 VC-PCFG의 전이 가능성에 가장 중요한 요소임을 발견하였다.

###### Analysis of Style-Shifting on Social Media: Using Neural Language Model Conditioned by Social Meanings (https://aclanthology.org/2023.findings-emnlp.531/)
- Anthology ID: 2023.findings-emnlp.531 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 소셜미디어 대화의 스타일 변화를 평가하기 위한 새로운 프레임워크를 제안한다. 
    2. 개인화된 신경망 언어 모델을 통해 각 개인의 대화 스타일의 변화를 예측한 놀라움 (surprisals)에 기반한 스타일 새로운 프레임워크를 제안한다.
    3. 지식 그래프와 미리 학습된 언어 모델을 활용하여 개인화된 언어 모델을 구축하고, 이 모델은 테스트 세트에서 개인의 언어를 예측하는 우수한 성능을 보여주었다.

###### Linguistic Compression in Single-Sentence Human-Written Summaries (https://aclanthology.org/2023.findings-emnlp.532/)
- Anthology ID: 2023.findings-emnlp.532 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 요약은 정보를 압축하는 데 많은 인지적 노력이 필요하다. 이 논문에서는 인간이 작성한 요약에서 언어적 패턴을 분석하는 대규모 공부를 제시한다.
    2. 어휘 확장, 어휘 다양성의 증가, 특정 단어들의 위치 배치와 같은 언어적 압축 패턴을 분석해봤을 때, 그 유형에 관계없이 요약은 일반적으로 원본과 비교하여 작성되며, 작성자와 독자 간에는 어휘 다양성과 단어의 특이성에 대한 선호도가 일치하지 않는다는 것을 발견하였다.
    3. 이러한 언어학적 변화가 독자의 품질 판단에 어떤 영향을 미치는지에 대한 인간 연구를 통해, 요약 작성자와 독자 간에는 문법과 문법적 변화의 사용이 독자의 선호와 일치한다는 결과를 얻었다.

###### MCLF: A Multi-grained Contrastive Learning Framework for ASR-robust Spoken Language Understanding (https://aclanthology.org/2023.findings-emnlp.533/)
- Anthology ID: 2023.findings-emnlp.533 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ASR 오류에 대한 강인성을 향상시키는 것은 SLU에서 매우 중요하다. 
    2. 이 논문에서는 MCLF라고 불리는 이중 단계 다중 granular 대조 학습 프레임워크를 제안한다. 
    3. 실험 결과와 상세한 분석을 통해 우리의 방법이 효과적임을 보여준다.

###### Beyond Candidates : Adaptive Dialogue Agent Utilizing Persona and Knowledge (https://aclanthology.org/2023.findings-emnlp.534/)
- Anthology ID: 2023.findings-emnlp.534 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전 연구는 개인화와 지식을 둘 다 기반으로 하는 대화 에이전트를 구축하기 위한 것을 제안해왔지만 실제 대화에 직접 적용하는 것은 아직 한계가 있다.
    2. 이 논문은 주어진 데이터셋에서 전체 문장 형태의 개인화와 지식 후보 세트가 필요한 경우가 많기 때문에, 미리 정의된 후보 문장들 대신 사람들이 그들 마음의 의미적 개념을 활용하는 방법을 따르도록 제안한다.
    3. 본 논문에서는 전체 문장 기반의 후보 문장을 사용한 개인화와 지식을 활용하는 기존 기준선을 능가하는 모델을 제안하고, 인간 평가와 각 구성요소의 효과를 입증하기 위해 핵심 내용을 제시한다.

###### SmartSpanNER: Making SpanNER Robust in Low Resource Scenarios (https://aclanthology.org/2023.findings-emnlp.535/)
- Anthology ID: 2023.findings-emnlp.535 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Named Entity Recognition (NER)은 자연어 처리에서 가장 기본적인 작업 중 하나이다. 
    2. SpanNER 방법은 SeqLab에 비해 nested NER에 더 적합하지만, 실험 결과 SpanNER 방법은 학습 데이터 양에 매우 민감하다. 
    3. 따라서, 저자들은 SmartSpanNER이라고 불리는 새로운 SpanNER 방법을 제안하여 low resource scenario에서 SpanNER의 견고성을 향상시켰다.

###### ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding (https://aclanthology.org/2023.findings-emnlp.536/)
- Anthology ID: 2023.findings-emnlp.536 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ZeroSCROLLS는 훈련 데이터 없이 테스트 및 소규모 검증 데이터셋만으로 구성된 Zero-shot 벤치마크로, 장문 텍스트에 대한 자연어 이해 능력을 평가한다. 
    2. ZeroSCROLLS를 사용하여 클로드(Claude)가 ChatGPT보다 우수한 성능을 보여주고, GPT-4가 가장 높은 평균 점수를 달성하는 것을 발견하였다. 그러나 ZeroSCROLLS에서 여러 개의 도전과제 중에는 모델이 기본 성능을 넘기기 어려운 집계 작업과 같은 부분에서 개선의 여지가 남아있다.
    3. 현재 기술 수준은 계속 변화하고 있기 때문에 ZeroSCROLLS 리더보드에서 사용자들이 자신의 아이디어를 평가하도록 연구자들에게 초대장을 내린다.

###### Data Selection Curriculum for Abstractive Text Summarization (https://aclanthology.org/2023.findings-emnlp.537/)
- Anthology ID: 2023.findings-emnlp.537 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존에는 임의로 섞은 대규모 데이터를 사용해 학습하지만, ATS 모델의 데이터 선택과 데이터 순서에 대한 영향은 아직 체계적으로 연구되지 않은 분야이다. 
    2. 이 연구는 학습 인스턴스의 학습 난이도를 정확하게 평가하는 것이 어려운 과제로 출발하여, 개선의 난이도와 예상 성능을 종합적으로 고려하는 데이터 선택 커리큘럼 (DSC) 점수 시스템을 제안한다.
    3. 실험 결과, CNN/DailyMail 데이터셋에서 우리의 접근 방식은 강력한 기준 모델들을 능가하며, 사용 가능한 인스턴스의 20%만을 사용하여 성능을 개선할 수 있다.

###### Romanization-based Large-scale Adaptation of Multilingual Language Models (https://aclanthology.org/2023.findings-emnlp.538/)
- Anthology ID: 2023.findings-emnlp.538 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 다국어 사전 훈련 언어 모델(mPLMs)은 NLP의 다국어 전이에서 사실상 최고 수준의 성능을 보여주고 있지만, 일부 언어 모델에 대한 vocabulary 크기 증가 및 파라미터 제약으로 인해 저자원 언어에 대한 적용에 어려움이 있다.
    2. 이 논문에서는 UROMAN이라는 대량의 복제를 통해 transliteration 기술을 활용하여 mPLMs의 저자원 및 미확인 언어 처리 능력을 향상시키는 가능성을 탐구한다.
    3. UROMAN 기반의 변환은 많은 언어에서 강력한 성능을 제공하며, 특히 본문스크립트가 없거나 훈련 데이터가 제한된 언어의 경우 특히 높은 성과를 보여준다는 연구 결과를 보여준다.

###### Measuring bias in Instruction-Following models with P-AT (https://aclanthology.org/2023.findings-emnlp.539/)
- Anthology ID: 2023.findings-emnlp.539 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Instruction-Following Language Models (IFLMs)는 많은 하위 정보 탐색 작업을 해결하기 위한 유망하고 다용도 도구이다. 그러나 기존 및 새로운 IFLMs가 편향된 언어 상호작용에 취약한지 여부를 판단하기 위한 공유 자원이 절박하게 필요합니다."
    2. 우리는 P-AT (Prompt Association Test)를 제안하여 IFLMs의 사회적 편향 존재를 테스트하는 새로운 자원을 개발했습니다.
    3. 우리의 자원은 2310개의 프롬프트로 구성되어 있으며, 여러 가족의 IFLM에서 성별 및 인종 편향을 발견하였습니다.

###### Open-ended Commonsense Reasoning with Unrestricted Answer Candidates (https://aclanthology.org/2023.findings-emnlp.540/)
- Anthology ID: 2023.findings-emnlp.540 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. '묵시적 다단계 추론'을 필요로 하는 'Open-ended Commonsense Reasoning' 문제에 대한 새로운 방법을 제안한다.
    2. 사전 정의된 정한 후보 답안이나 정해진 정답 범위 없이 평소의 상식으로 문제를 해결하는 것을 목표로 한다.
    3. 사전 학습된 언어 모델을 활용하여 외부 지식 베이스에서 추론 경로를 반복적으로 탐색하고, 이를 통해 공통감각 질문에 가장 정확한 답을 찾는다. 이 방법은 다른 접근법에 비해 정량적, 정성적으로 좋은 성능을 보여준다.

###### Speaking Style Conversion in the Waveform Domain Using Discrete Self-Supervised Units (https://aclanthology.org/2023.findings-emnlp.541/)
- Anthology ID: 2023.findings-emnlp.541 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. DISSC는 녹음의 리듬, 음고와 음색을 텍스트 없이도 대상 화자로 변환하는 경량 방법이다. 
    2. 기존 음성 변환 방법들은 주로 음색에만 초점을 두고 개인의 고유한 말투(프로소디)을 무시한다. 
    3. DISSC는 사전 훈련된 자기 감독 모델을 사용하여 음성을 이산 유닛으로 인코딩함으로써 간단하고 효과적이며 빠르게 훈련될 수 있으며, 기존 방법들보다 우수한 성능을 보여준다.

###### Knowledge-Selective Pretraining for Attribute Value Extraction (https://aclanthology.org/2023.findings-emnlp.542/)
- Anthology ID: 2023.findings-emnlp.542 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Attribute Value Extraction (AVE)은 제품 프로필에서 속성 값을 검색하는 작업이다. 
    2. 기존 방법들은 소수의 속성에 대한 성능이 만족스럽지 않으며, 일반화 능력이 부족해 이를 대처하기 어렵다. 
    3. 이 논문에서는 사전학습과 전이학습을 활용하여 성능을 향상시키는 방법을 제안하고, 지식 선택 프레임워크 (KSelF)를 사용하여 성능을 더욱 향상시킨다.

###### New Datasets and Controllable Iterative Data Augmentation Method for Code-switching ASR Error Correction (https://aclanthology.org/2023.findings-emnlp.543/)
- Anthology ID: 2023.findings-emnlp.543 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 음성 인식 (ASR) 시스템의 널리 사용으로 인해, ASR 오류 수정 작업을 통해 인식 결과의 품질을 개선하기 위해 더 많은 관심이 기울여지고 있다. 특히, 양/다양한 언어로 이뤄진 code-switching ASR에서는 더 큰 도전과 연구 가치가 있다.
    2. 이 논문에서는 실제 ASR 시스템과 자동 주석 달기 도구로부터 얻은 code-switching ASR 수정 데이터셋을 제시한다. 이 데이터셋은 싱가포르, 말레이시아, 홍콩의 이중 언어 사용자들의 중국어-영어 혼용 대화를 포함하고 있다. 
    3. 이 작업을 기반으로 기존 ASR 오류 수정 시스템의 성능을 향상시키기 위해 조절 가능한 반복 (CI) 데이터 증강 방법을 제안하였다. 소량의 훈련 데이터로, 우리의 제안하는 방법은 중국어-영어 코드-스위칭 ASR 수정을 위해 단일 언어 말뭉치로부터 반복적으로 풍부한 가짜 병렬 데이터를 생성할 수 있다. 실험 결과, 우리의 방법은 rule-based, back-translation-based 데이터 증강 방법 및 대규모 언어 모델 ChatGPT와 비교했을 때 가장 좋은 성능을 보였다.

###### Efficient k-NN Search with Cross-Encoders using Adaptive Multi-Round CUR Decomposition (https://aclanthology.org/2023.findings-emnlp.544/)
- Anthology ID: 2023.findings-emnlp.544 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Cross-encoder 모델은 쿼리-아이템 쌍을 함께 인코딩하고 점수를 매기는 데에는 많은 비용이 들어가고, 따라서 직접적인 k-NN 검색에는 사용하기 힘들다. 
    2. 이 논문에서는 ANNCUR와 같은 기존 방법들보다 효과적으로 상위 k개 이웃 항목의 근사 오차를 최소화하는 ADACUR이라는 방법을 제안한다. 
    3. 다른 데이터셋에서도 ADACUR은 이전의 전통적인 방법 및 최신 방법인 ANNCUR, dual-encoder 기반의 retrieve-and-rerank와 비교하여 리콜 에러를 일관되게 감소시키며, 경쟁 제품들보다 더 많은 계산 자원을 사용하지 않는다.

###### Isotropic Representation Can Improve Zero-Shot Cross-Lingual Transfer on Multilingual Language Models (https://aclanthology.org/2023.findings-emnlp.545/)
- Anthology ID: 2023.findings-emnlp.545 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 사전학습 언어 모델 (mPLM)의 발전과 함께 zero-shot cross-lingual transfer는 큰 가능성을 보여주고 있다. 그러나 국지적인 문맥 표현 분포로 인해 발생하는 misalignment 문제는 형태학적 차이에 의해서만 발생하는 것으로 생각되었던 것과는 달리, 우리는 이 논문에서 이러한 문제를 완화하기 위해 향상된 등방성(isotropy)과 제약 조건이 있는 코드 스위칭(constrained code-switching)을 제안한다.
    2. 우리의 방법은 이러한 등방성 표현의 misalignment 문제를 완화하고 구문 구조적인 지식을 유지하는데 도움을 주며, 강력한 mPLM 백본에 비해 상당한 성능 향상을 보인다.
    3. 세 가지 zero-shot cross-lingual transfer task에 대한 실험을 통해 우리의 방법이 강력한 mPLM 백본에 대해 혁신적인 개선을 이루었고 최고 수준의 방법들을 더욱 향상시킨다는 것을 보여준다.

###### Blackbird language matrices (BLM), a new task for rule-like generalization in neural networks: Can Large Language Models pass the test? (https://aclanthology.org/2023.findings-emnlp.546/)
- Anthology ID: 2023.findings-emnlp.546 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델의 일반화 능력을 평가하고 그들의 지능적 행동의 측면과 한계를 알아내는 방법은 무엇인가?
    2. 이 논문에서는 LLM의 문제해결 능력을 평가하기 위해 RAVEN IQ 테스트와 유사한 BLM task를 제안한다.
    3. 현재 ChatGPT와 같은 최신 생성 모델은 BLM task를 이해하고 해결하는 능력이 있으나, 전반적으로 정확한 답을 찾지 못하고 있다.

###### DistillCSE: Distilled Contrastive Learning for Sentence Embeddings (https://aclanthology.org/2023.findings-emnlp.547/)
- Anthology ID: 2023.findings-emnlp.547 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "본 논문은 지식 증류 기법과 자기 학습 패러다임 하에서 대조적 학습을 수행하는 DistillCSE 프레임워크를 제안한다."
    2. "DistillCSE의 장점은 기본 모델이 추가적인 지도 신호를 제공하여 지식 증류를 통해 더 강력한 모델을 학습할 수 있는 자가 강화 특성이다."
    3. "기존 지식 증류 방식의 구현에서는 상대적으로 큰 분산을 가진 교사 모델의 logits로 인해 문제가 발생하는데, 이 문제를 완화하기 위해 본 논문에서는 두 가지 간단하면서도 효과적인 지식 증류 솔루션을 제안한다."

###### GSAP-NER: A Novel Task, Corpus, and Baseline for Scholarly Entity Extraction Focused on Machine Learning Models and Datasets (https://aclanthology.org/2023.findings-emnlp.548/)
- Anthology ID: 2023.findings-emnlp.548 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NER 모델은 정보 추출 및 텍스트 이해와 같은 다양한 NLP 작업에서 중요한 역할을 한다. 하지만 기존의 NER 데이터셋은 ML 모델과 모델 구조와 같은 미세한 타입을 별도의 entity 타입으로 다루지 않아 기본 모델이 이를 인식하지 못한다.
    2. 본 논문에서는 100개의 수동으로 주석이 달린 전문과 ML 모델 및 데이터셋 주변의 10개 entity 타입을 위한 첫 번째 baseline 모델을 공개한다.
    3. 우리의 데이터셋은 "our BERT-based model" 또는 "an image CNN"과 같은 비공식적인 언급뿐만 아니라 ML 모델과 데이터셋이 어떻게 언급되고 활용되는지에 대한 세부적인 이해를 제공한다.

###### Open Domain Multi-document Summarization: A Comprehensive Study of Model Brittleness under Retrieval (https://aclanthology.org/2023.findings-emnlp.549/)
- Anthology ID: 2023.findings-emnlp.549 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "다중 문서 요약(MDS)은 주제와 관련된 문서 집합을 입력으로 가정한다. 하지만 실제로 이러한 문서 집합이 항상 사용 가능한 것은 아니고, 정보 필요에 따라 검색해야 하는 경우도 있다. 이를 "open-domain MDS"라고 부르며, 이 더 어려운 상황에서의 과제를 형식화하고, 기존 데이터셋, 검색기, 요약기를 사용하여 적용한다.
    2. 우리는 다양한 자동 평가와 인간 평가를 통해, 1. 현재의 요약기들은 open-domain MDS에 적용할 때 성능이 크게 저하되는 것을 확인하였고, 2. open-domain 환경에서의 추가 학습은 불완전한 검색에 대한 민감도를 낮출 수 있다는 것을 확인하였으며, 3. 요약기는 중복 문서의 검색이나 검색 문서의 순서에는 민감하지 않지만, 관련 없는 문서의 검색과 같은 다른 오류에는 민감하다는 것을 밝혀냈다.
    3. 우리의 결과에 기반하여 open-domain MDS에 대한 미래 연구를 위한 실용적인 가이드라인을 제시하며, 예를 들어 몇 개의 검색된 문서를 선택하여 요약할지 선택하는 방법 등을 제안한다. 우리의 결과는 open-domain 환경에서의 further progress를 위해 새로운 검색과 요약 방법, 학습 및 평가를 위한 주석이 필요하다는 것을 시사한다."

###### Few-shot Unified Question Answering: Tuning Models or Prompts? (https://aclanthology.org/2023.findings-emnlp.550/)
- Anthology ID: 2023.findings-emnlp.550 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. QA 태스크는 특정한 질문 유형, 지식 도메인 또는 추론 기술을 다루기 때문에 특정한 카테고리의 QA 태스크에 대한 모델 개발이 필요하다. 
    2. 본 논문은 저자들이 모델 튜닝과 힌트(tuning, model, and prompts) 이라는 두 가지 패러다임을 제시하여 리소스가 제한된 상황에서 통합된 QA 모델을 개발한다. 
    3. 실험 결과 prompt tuning이 model tuning만큼 성능을 내며, parameter-sharing이 성능을 향상시키는 것을 확인했다. 또한, pre-training을 통한 prompt 초기화가 효과적이며, prompt tuning은 저자의 말로 보면 low-resource 상황에서 효과적이다.

###### Finding Common Ground: Annotating and Predicting Common Ground in Spoken Conversations (https://aclanthology.org/2023.findings-emnlp.551/)
- Anthology ID: 2023.findings-emnlp.551 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들과 의사소통할 때 우리는 단순히 단어들의 시퀀스를 생성하는 것이 아니다. 대신에 우리는 인식상태와 청자의 인식상태 모델을 사용하여 청자의 의도된 방식으로 의식상태를 좌지우지하는 어구들을 만든다.
    2. 인식상태의 중요한 부분은 공통 지식(common ground)이며, 이는 화자가 믿고, 청자도 믿고 그런식으로 계속해서 이어가는 내용이다. 
    3. 본 논문에서는 공통 지식을 파악하기 위한 새로운 어노테이션 및 말뭉치를 도입하였고, 이후 시작적인 실험을 통해 대화에서 명제를 추출하고, 각 화자의 관점에서 공통 지식의 상태를 추적하는 방법을 설명한다.

###### Getting MoRE out of Mixture of Language Model Reasoning Experts (https://aclanthology.org/2023.findings-emnlp.552/)
- Anthology ID: 2023.findings-emnlp.552 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델(Large Language Models, LLMs)은 다양한 질의응답(Question Answering, QA) 데이터셋에서 더 뛰어난 성과를 보이지만, 단일 모델로는 다양한 추론 능력을 필요로하는 질문 유형에 대해 일반화하는 것이 여전히 어렵다.
    2. 본 논문에서는 다양한 특화된 언어 모델을 앙상블하는 Mixture-of-Reasoning-Experts (MORE) 프레임워크를 제안하여 이러한 문제를 해결한다.
    3. 실험 결과, MORE은 12개의 QA 데이터셋에서 네 가지 추론 유형에서 단일 특화된 모델보다 더 높은 정확성을 보여주며, 해석 가능한 디자인은 다른 기준선과 비교하여 선별적인 질문 응답 결과를 개선한다는 것을 보여준다.

###### “You Are An Expert Linguistic Annotator”: Limits of LLMs as Analyzers of Abstract Meaning Representation (https://aclanthology.org/2023.findings-emnlp.553/)
- Anthology ID: 2023.findings-emnlp.553 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델들은 언어 사용에 있어서 놀라운 능력을 보여주지만, 실제 문장 구조에 대한 정확한 의미 분석 능력에는 제약이 있다.
    2. 이 연구에서는 GPT-3, ChatGPT, GPT-4 모델들의 Abstract Meaning Representation (AMR) 파싱 능력을 조사하였다.
    3. 모델들은 일부 핵심적인 의미 구조를 재현할 수 있지만, 자주 발생하는 오차와 fully accurate한 파싱 결과를 도출하는 능력의 제한이 여전히 존재함을 발견하였다.

###### Zero-Shot Data Maps. Efficient Dataset Cartography Without Model Training (https://aclanthology.org/2023.findings-emnlp.554/)
- Anthology ID: 2023.findings-emnlp.554 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 데이터 맵은 컴퓨터 모델이 데이터에 적합한지를 진단하는데 유용한 도구로 알려져 있다. 이 논문에서는 제로샷 모델을 사용하여 데이터 맵을 더 빠르게 생성하는 방법을 제안한다.
    2. 제로샷 모델을 사용하여 각 데이터 포인트에 대한 신뢰도와 변동성을 계산한다. 이러한 방법은 기존의 방법과 비교하여 약 14배 빠르게 데이터 맵을 생성할 수 있다.
    3. 실험 결과 제로샷 데이터 맵이 기존의 방법과 일치함을 확인하였고, 또한 코드를 공개하였다. (링크 첨부된다.)

###### Isotropy-Enhanced Conditional Masked Language Models (https://aclanthology.org/2023.findings-emnlp.555/)
- Anthology ID: 2023.findings-emnlp.555 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 생성 모델은 추론 과정을 가속화하기 위해 자주 사용되지만 생성 품질은 어느 정도 희생됩니다. 우리는 추론 속도를 높이고 생성 품질을 균형있게 유지하기 위해 CMLM과 Disco와 같은 반복적인 NAR 모델을 제안합니다.
    2. 우리는 반복적인 NAR 모델에서 표시되는 다른 예측 대상 토큰들의 표현이 유사하고 구별되지 않는 anisotropic 문제에 대해 더 깊이 있는 분석을 제시합니다.
    3. 우리의 연구는 대조 학습 방법의 효과를 분석하고 훈련 과정에서 토큰 표현 학습을 강화하기 위해 Look Neighbors 전략을 제안합니다. 실험 결과는 우리의 방법이 조건부 마스크 언어 모델의 성능을 일관되게 향상시키고 anisotropic 문제를 완화하는 것을 보여줍니다.

###### Scaling Law for Document Neural Machine Translation (https://aclanthology.org/2023.findings-emnlp.556/)
- Anthology ID: 2023.findings-emnlp.556 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 규모 변화 법칙이 큰 언어 모델의 발전에 중요한 역할을 한다. 이 논문에서는 문서 번역 분야에서 규모 변화 법칙을 체계적으로 조사한다.
    2. 모델 규모, 데이터 규모, 시퀀스 길이라는 세 가지 요소의 번역 품질에 미치는 영향을 깊이 분석한다.
    3. 연구 결과, 모델 규모가 제한된 경우 시퀀스 길이를 늘릴 때 모델 성능을 효과적으로 향상시킬 수 있으며, 그러나 시퀀스 길이는 무한정으로 확장될 수 없으며 모델 규모와 말뭉치 크기와 적절하게 조화를 이루어야 한다. 또한 적절한 문맥을 제공하는 것이 문서의 초기 부분의 번역 품질을 효과적으로 향상시킬 수 있는데, 그러나 뒷부분에서의 번역 품질 개선을 방해하는 주된 요인은 exposure bias이다.

###### Automatic Pronunciation Assessment - A Review (https://aclanthology.org/2023.findings-emnlp.557/)
- Anthology ID: 2023.findings-emnlp.557 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 몇 년 동안 언어 처리와 딥러닝이 급격히 성장함에 따라 발음 평가 및 컴퓨터 지원 발음 훈련엔 높은 진척이 있었다. 
    2. 이 논문에서는 음운 및 운율의 발음 평가에 사용되는 방법들을 검토하고, 주요 연구 동향에서 관찰된 주요 도전과제들을 분류하며, 기존의 한계와 사용 가능한 자원들을 강조한다.
    3. 그 후, 남아있는 도전과제들과 향후 연구 방향에 대해 논의한다.

###### Segmented Recurrent Transformer: An Efficient Sequence-to-Sequence Model (https://aclanthology.org/2023.findings-emnlp.558/)
- Anthology ID: 2023.findings-emnlp.558 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 및 비전과 같은 다양한 분야에서 Transformer는 우수한 성능을 보여주었지만, sequence 길이에 따라 계산 비용이 2차적으로 증가하여 자원이 제한된 애플리케이션에는 사용하기 어렵다. 
    2. 우리의 접근 방식은 전체 sequence를 segment로 나누고 개별 segment에 attention을 적용하는 것이다.
    3. segmented attention과 가벼운 RAF neurons을 결합하여 제안된 transformer는 계산 및 메모리 비용이 낮으면서 순차적 처리 능력을 갖는 모델을 구현한다.

###### PUNR: Pre-training with User Behavior Modeling for News Recommendation (https://aclanthology.org/2023.findings-emnlp.559/)
- Anthology ID: 2023.findings-emnlp.559 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 뉴스 추천은 사용자의 행동을 기반으로 클릭 동작을 예측하는 것을 목표로 한다. 사용자 표현을 효과적으로 모델링하는 것이 선호하는 뉴스를 추천하는 핵심이다.
    2. 기존 연구들은 대부분 감독 학습 fine-tuning 단계에서의 개선에 집중되어 있다. 그러나 사용자 표현에 최적화된 PLM 기반의 비지도 사전학습 방법이 여전히 부족하다.
    3. 이 연구에서는 사용자 행동에 대한 마스킹과 생성이라는 두 가지 작업으로 구성된 비지도 사전학습 패러다임을 제안한다. 이를 통해 훨씬 강력하고 포괄적인 사용자 뉴스 패턴을 모델링할 수 있다.

###### Monte Carlo Thought Search: Large Language Model Querying for Complex Scientific Reasoning in Catalyst Design (https://aclanthology.org/2023.findings-emnlp.560/)
- Anthology ID: 2023.findings-emnlp.560 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 새로운 촉매 발견을 위해서는 여러 화학적 성질과 트레이드 오프를 포함한 복잡한 추론이 필요하며, 이는 경우의 수 증가로 이어진다. 이 논문에서는 Monte Carlo Tree Search(MCTS) 기반의 방법론을 제안하여 이러한 화학적 추론을 개선하고 화학적 변환과정에 대한 새로운 인사이트를 찾는다.
    2. 큰 언어 모델 (LLM) 을 사용하여 경계를 넘어 간단한 인자의 지시사항 추론이 가능해졌으나, LLM 을 사용한 목표지향적인 조합 탐색은 세밀하게 연구되지 않았다.
    3. MCTS 기반의 새로운 방법론을 도입하여 이전 방법보다 25.8% 성능을 향상시키고, 과학자들의 추론과 발견 과정을 혁신적인 통찰력으로 보완할 수 있는 가능성을 제시한다.

###### Measure Children’s Mindreading Ability with Machine Reading (https://aclanthology.org/2023.findings-emnlp.561/)
- Anthology ID: 2023.findings-emnlp.561 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 심리학 연구에서 기계 학습 기술의 발전으로 많은 이득을 보았다. 
    2. 이전 연구들은 아이들의 마음 읽기에 대한 자동 점수 모델을 구축할 수 있다는 것을 보여주었지만, 점수를 매기는 동안 이야기나 비디오 클립의 특징을 고려하지 않았기 때문에 정확성이 저하되었다.
    3. 우리 연구에서는 어린이의 마음 읽기 평가 중에 질문과 관련된 이야기와 비디오에서 추출한 특징을 활용하기 위해 멀티모달 학습 프레임워크를 제안한다. 실험 결과, 제안된 모델이 인간 전문가가 평가한 점수와 일치함을 보여주며, 실용적인 자동 어린이 마음 읽기 점수 시스템에 대한 잠재력을 강조한다.

###### Crosslingual Transfer Learning for Low-Resource Languages Based on Multilingual Colexification Graphs (https://aclanthology.org/2023.findings-emnlp.562/)
- Anthology ID: 2023.findings-emnlp.562 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어학에서, colexification은 하나의 어휘 형태가 두 개 이상의 다른 의미를 전달하는 현상을 의미한다. 이전 연구들은 주석이 달린 단어 목록에 의존하므로 확장성과 NLP에서의 유용성이 제한된다. 
    2. 이 논문에서는 주석이 달리지 않은 병렬 말뭉치에서 직접 1,335개의 언어로 2,000여 개 개념의 colexification 패턴을 식별한다. 그리고 이 colexification 패턴을 기반으로 multilingual 그래프를 구축하기 위한 두 가지 간단하고 효과적인 방법을 제안한다.
    3. 제안하는 방법을 이용하여 훈련한 고품질 multilingual 임베딩은 transfer learning에 적합하며, roundtrip 번역, 문장 검색 및 문장 분류 작업에서 여러 transfer learning 기준을 능가하는 결과를 보인다. 이는 multilingual NLP에서 colexification을 정보 출처로 사용하는 이점을 보여준다.

###### Injecting structural hints: Using language models to study inductive biases in language learning (https://aclanthology.org/2023.findings-emnlp.563/)
- Anthology ID: 2023.findings-emnlp.563 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들과 transformer 언어 모델은 구조적인 지도 없이 언어를 학습할 수 있다. 이 논문에서는 학습에 영향을 주는 인지적 기대에 대해 조사한다.
    2. 학습을 위해 구조적인 바이어스를 사용하여 인공 학습자의 학습에 영향을 준다. 이를 세 가지 타입의 인지적 기대로 조사한다.
    3. 연구를 통해 토큰 간의 복잡한 상호 작용이 가장 효과적인 인지적 기대라는 것을 보여준다.

###### Machine Reading Comprehension using Case-based Reasoning (https://aclanthology.org/2023.findings-emnlp.564/)
- Anthology ID: 2023.findings-emnlp.564 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기계 독해 분석에서 정답 추출을 위한 CBR(Case-Based Reasoning)을 기반으로 하는 정확하고 해석 가능한 방법을 제안한다. 
    2. CBR-MRC 방법은 유사한 질문에 대한 맥락화된 답변들이 서로 의미적으로 유사하다는 가설을 기반으로 한다. 
    3. CBR-MRC는 큰 리더 모델과 비교할 만큼 높은 정확도를 제공하며, 신뢰성이 높고 디버깅 가능한 QA 시스템 구축에 유용한 선택이 될 수 있다.

###### Unleashing the Power of Language Models in Text-Attributed Graph (https://aclanthology.org/2023.findings-emnlp.565/)
- Anthology ID: 2023.findings-emnlp.565 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 그래프 기반의 텍스트 표현 학습은 실제 문제를 해결하는 데 강력한 도구로 입증되었다. 기존의 방법들은 언어 모델이나 그래프 신경망을 활용하여 이러한 데이터에서 지식을 추출할 수 있도록 했으나, 노드나 단어들 간의 관계 활용이 부족하거나 메모리 비용이 너무 큰 문제가 있다.
    2. 이 논문에서는 텍스트와 그래프를 동시에 모델링하는 Node Representation Update Pre-training Architecture (NRUP)을 제안한다. NRUP에서는 원래 노드와 단어 노드를 모두 포함한 계층적인 텍스트-속성 그래프를 구성한다.
    3. 또한, 생성된 그래프의 다른 수준에 대해 네 가지 자기 지도 학습 작업을 적용하며, 학습 epoch 동안 노드의 특징을 업데이트하는 사전 학습 프레임워크를 설계한다. 실험 결과, 우리의 방법은 벤치마크 데이터셋에서 기준선들과 비교해서 우수한 성능을 보여주며, 그 유효성과 일반성을 증명한다.

###### Locally Differentially Private Document Generation Using Zero Shot Prompting (https://aclanthology.org/2023.findings-emnlp.566/)
- Anthology ID: 2023.findings-emnlp.566 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델로 인한 개인정보 위험에 대한 많은 연구가 있었지만, 이 연구는 사전 훈련된 대규모 언어 모델이 개인 정보 보호에 효과적으로 기여할 수 있다는 독특한 시각을 제시합니다.
    2. 우리는 DP-Prompt라는 로컬로 차이 동질적 개인 정보 보호 기법을 제안하며, 사전 훈련된 대규모 언어 모델의 성능에 기여하고 동시에 다운스트림 유용성에 미치는 영향을 최소화합니다.
    3. DP-Prompt (with ChatGPT)는 기존 방법보다 훨씬 우수한 결과를 보여주며, IMDB 데이터셋의 경우 정적 공격자에 대해 저자 식별 F1 점수를 46% 감소시키고 적응적 공격자에 대해 26% 감소시키면서 깨끗한 감성 F1 점수를 완벽하게 복구합니다.

###### Contrastive Deterministic Autoencoders For Language Modeling (https://aclanthology.org/2023.findings-emnlp.567/)
- Anthology ID: 2023.findings-emnlp.567 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Variational autoencoder (VAE) 모델의 훈련은 후단붕괴(posterior collapse) 문제 때문에 표현 퀄리티 손실이 발생하는데, 특히 텍스트에 적용할 때 이러한 문제가 발생한다. 이 논문에서는 이미지에 대해 설계된 deterministic 모델을 텍스트에 적용하는 방법을 소개한다.
    2. 이 논문에서는 양질의 언어 모델링을 위한 벤치마크인 Batch-normed VAEs (BN-VAEs)를 대체하기 위해 결정론적 모델을 사용하는 것으로 VAE 모델의 리파라미터화(reparametrization) 단계를 건너뛰고 후방 배추(collapse)를 회피하면서 텍스트 생성 및 표현과 관련된 다양한 작업에서 더 나은 성능을 보임을 보여준다.
    3. LSTM 및 Transformer 기반 VAE 아키텍처에 대해 일관된 성능 향상을 보여주며, BERT/GPT-2와의 적절한 비교를 수행한다. 또한, 모델의 양적인 면을 보완하기 위해 보간을 통해 latent space를 질적으로 검토한다.

###### CHiLL: Zero-shot Custom Interpretable Feature Extraction from Clinical Notes with Large Language Models (https://aclanthology.org/2023.findings-emnlp.568/)
- Anthology ID: 2023.findings-emnlp.568 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CHiLL (Crafting High-Level Latents)은 선형 모델을 위한 기능의 자연어 명세를 위한 접근 방식으로, 전문가가 작성한 질의를 통해 LLMs에게 가이드를 제공하여 건강 기록에서 해석 가능한 기능을 생성한다.
    2. 생성된 노이즈 라벨은 간단한 선형 분류기를 훈련시키는 데 사용된다. LLM에게 질의를 기반으로 기능을 생성하는 것은 의사들이 다운스트림 태스크에 대해 임상적으로 의미 있는 기능을 수동으로 추출하지 않고도 도메인 전문성을 활용하여 기능을 개발할 수 있게 한다.
    3. 우리는 실제 위험 예측 태스크에 영감을 받았지만, 재현 가능한 대리 데이터인 MIMIC-III와 MIMIC-CXR 데이터를 사용하여 이 접근 방식을 평가한다. 자동으로 추출된 기능을 사용하는 선형 모델이 참조 기능을 사용하는 모델에 비해 성능이 비슷하며 "Bag-of-Words" 기능을 사용하는 모델보다 해석 가능성이 더 높다는 것을 확인한다. 또한 학습된 기능 가중치가 임상적인 예상과 일치함을 검증한다.

###### Guiding LLM to Fool Itself: Automatically Manipulating Machine Reading Comprehension Shortcut Triggers (https://aclanthology.org/2023.findings-emnlp.569/)
- Anthology ID: 2023.findings-emnlp.569 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에 LLMs (Language Models)을 사용한 MRC(Machine Reading Comprehension) 시스템이 인상적인 결과를 보이고 있으나, 신뢰성에 대한 위협으로 spurious correlation과 관련된 shortcut 사용이 나타났다.
    2. 우리는 LLMs을 편집자로 보고, LLMs를 속이기 위해 텍스트를 수정하도록 가이드하는 프레임워크를 소개한다.
    3. 우리는 ShortcutQA라는 데이터셋을 공개하며, LLMs의 shortcut 조작에 대한 내재적 취약점을 강조한다.

###### Large Language Models Meet Harry Potter: A Dataset for Aligning Dialogue Agents with Characters (https://aclanthology.org/2023.findings-emnlp.570/)
- Anthology ID: 2023.findings-emnlp.570 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대화형 큰 언어 모델들은 오픈 도메인 대화 에이전트를 만드는 데에 많은 잠재력을 보이고 있다. 그러나 특정 캐릭터나 인물과 대화형 에이전트를 조율하는 것은 캐릭터 표현의 복잡성과 포괄적인 주석의 부재로 인해 아직 큰 도전이다.
    2. 이 논문에서는 대화 에이전트와 캐릭터 조율의 연구를 발전시키기 위한 Harry Potter Dialogue (HPD) 데이터셋을 소개한다. HPD 데이터셋은 Harry Potter 시리즈의 영어와 중국어 대화 세션을 모두 담고 있으며, 대화 장면, 발화자, 캐릭터 관계 및 속성 등의 중요한 배경 정보로 주석이 되어 있다.
    3. 이 모델들을 특정 캐릭터와 조율하는 능력을 평가하기 위해 HPD를 사용하는 벤치마크를 수행하여 모델들의 성능을 평가하였고, 제안된 데이터셋은 캐릭터와 정렬된 응답에 더 잘 부합하는 모델을 가리키는 소중한 가이드로 작용할 수 있다는 사실을 확인하였다.

###### Quick Back-Translation for Unsupervised Machine Translation (https://aclanthology.org/2023.findings-emnlp.571/)
- Anthology ID: 2023.findings-emnlp.571 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 비지도 기계 번역에서 Transformer와 back-translation 알고리즘의 결합은 많은 발전을 이루었다. 
    2. 하지만 Transformer는 back-translation 동안 자동회귀 추론의 런타임에 어려움을 겪으며, back-translation은 합성 데이터의 효율 부족으로 제한된다.
    3. 우리는 Quick Back-translation (QBT)라는 Transformer back-translation의 성능 향상 기술을 제안한다. QBT는 인코더를 생성 모델로 재사용하고, 인코더로부터 생성된 시퀀스를 사용하여 디코더를 학습시키는 방법으로, 데이터 처리량과 활용도를 향상시킨다.

###### SIR-ABSC: Incorporating Syntax into RoBERTa-based Sentiment Analysis Models with a Special Aggregator Token (https://aclanthology.org/2023.findings-emnlp.572/)
- Anthology ID: 2023.findings-emnlp.572 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 특정 입력 토큰에 따라 원하는 출력이 달라지는 Aspect-Based Sentiment Classification (ABSC)과 같은 작업에 대해, 구문 의존성 정보를 transformer 기반 언어 모델 (예: RoBERTa)에 직접 통합하는 간단하지만 효과적인 방법을 제안합니다.
    2. 우리의 모델인 SIR-ABSC (Syntax-Integrated RoBERTa for ABSC)는 이전의 ABSC 접근 방식과는 다르게 의존성 트리 상의 언어 모델과 그래프 신경망을 결합하여 구문을 포착하는 대신, 새로운 어그리게이터 토큰을 사용하여 구문을 언어 모델에 직접 통합합니다.
    3. 그 결과, SIR-ABSC는 이러한 더 복잡한 모델들보다 우수한 성능을 보여주며, ABSC에서 새로운 state-of-the-art 결과를 얻을 수 있습니다.

###### Citance-Contextualized Summarization of Scientific Papers (https://aclanthology.org/2023.findings-emnlp.573/)
- Anthology ID: 2023.findings-emnlp.573 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 과학논문의 요약은 원문과 해당 원문에 인용된 참고자료간의 관계를 나타내지 못하는 현재의 접근 방식으로 이루어진다. 
    2. 우리는 "citance"라고 불리는 참고문의 인용문이 존재하는 문장을 기반으로 정보를 포함한 요약을 생성할 수 있는 문맥화 요약 방법을 제안한다. 
    3. 따라서 우리는 논문의 citances을 추출하고 모델링하며, 인용된 논문에서 관련된 부분을 검색한 후 각각의 citance에 적합한 필사적 요약을 생성하는 방법을 제안한다.

###### SegAugment: Maximizing the Utility of Speech Translation Data with Segmentation-based Augmentations (https://aclanthology.org/2023.findings-emnlp.574/)
- Anthology ID: 2023.findings-emnlp.574 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 말-번역 end-to-end 시스템은 데이터 부족으로 인해 제약을 겪었다. 이 논문은 문장 수준의 다이나믹한 데이터를 생성하고자, SegAugment라는 새로운 데이터 증강 전략을 제안하였다.
    2. SegAugment는 각 문서의 음성을 다른 길이 제한으로 재분할하여 대상 텍스트를 얻는 방식을 사용한다. 실험 결과, MuST-C 데이터셋의 여덟 개 언어 쌍에서 2.5 BLEU 점의 평균 증가 및 mTEDx의 저자원 시나리오에서 최대 5 BLEU 점의 증가를 보였다.
    3. 또한, 강력한 시스템과 결합하면 MuST-C에서 state-of-the-art 결과를 얻을 수 있었고, 제안된 방법은 문장 수준 데이터도 성공적으로 증강시킬 수 있으며, 추론 시점에서 수동 및 자동 분할 사이의 차이를 줄일 수 있었다.

###### Intersectional Stereotypes in Large Language Models: Dataset and Analysis (https://aclanthology.org/2023.findings-emnlp.575/)
- Anthology ID: 2023.findings-emnlp.575 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(LLM) 내 교차된 인구 그룹을 대상으로 한 편견에 대한 선행 연구들은 주로 개인적인 범주에 중점을 두고 있으며, 이를 보완하기 위해 이 연구는 ChatGPT 모델과 수동으로 검증한 교차된 편견 데이터셋을 소개한다.
    2. 또한, 이 논문은 이 데이터셋을 활용하여 세 가지 최신 LLM에서 교차된 편견 전파를 종합적으로 분석한다. 
    3. 연구 결과는 LLM에서 편견의 확산을 줄이기 위한 지속적인 노력에서 교차된 편견에 중점을 두는 것의 긴요성을 강조한다.

###### Dataset Bias Mitigation in Multiple-Choice Visual Question Answering and Beyond (https://aclanthology.org/2023.findings-emnlp.576/)
- Anthology ID: 2023.findings-emnlp.576 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Vision-language (VL) understanding tasks에서 모델들은 올바른 이해 없이도 다양한 VL 태스크를 올바르게 해결하기 위해 dataset bias를 활용할 수 있다. 이 논문에서는 dataset biases를 해결하기 위해 Adversarial Data Synthesis (ADS)와 Intra-sample Counterfactual Training (ICT)를 제안한다.
    2. ADS는 합성 훈련 데이터와 합성 평가 데이터를 생성하는 것이다. ICT는 특히 counterfactual 데이터를 집중하여 모델이 합성 훈련 데이터를 활용하도록 돕는 것이다.
    3. 실험 결과, ADS와 ICT는 서로 다른 벤치마크에서 모델의 성능을 일관되게 향상시키는데 효과적이었다. 또한 도메인이 다른 경우에도 성능 향상이 있었다.

###### The Intended Uses of Automated Fact-Checking Artefacts: Why, How and Who (https://aclanthology.org/2023.findings-emnlp.577/)
- Anthology ID: 2023.findings-emnlp.577 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 사실 확인은 잘못된 정보를 대항하는 교정자, 소셜 미디어 사용자 및 기타 이해 관계자가 사용할 수 있는 인식 도구로 제시된다. 그럼에도 불구하고, 이와 관련된 논문들은 필요한 방법, 목표 및 이해 관계자에 대해 충분히 논의하지 않고 있다. 
    2. 이 논문은 서술된 사실 확인 기술의 목표와 수단 사이에 일관성이 없거나 현실성이 부족하며, 이에 대한 비판과 이해 관계자의 피드백이 제한되어 있다는 문제점에 대해 분석하여 문제를 제기한다.
    3. 따라서, 사실 확인 자산의 사용에 대해 생각하고 쓰기 위해 몇 가지 권고사항을 제시한다.

###### Retrieval-based Knowledge Transfer: An Effective Approach for Extreme Large Language Model Compression (https://aclanthology.org/2023.findings-emnlp.578/)
- Anthology ID: 2023.findings-emnlp.578 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 사전 훈련된 언어모델(Large-scale pre-trained language models)은 다양한 자연어 처리(NLP) 태스크에서 탁월한 성능을 보여주었으나, 모델의 대규모 크기는 실제 응용에서 배치하는 것에 엄청난 도전을 제기한다.
    2. 우리는 극도의 모델 압축을 위해 LLM의 지식을 극소 규모 모델에 전달하는 새로운 압축 패러다임인 Retrieval-based Knowledge Transfer (RetriKT)을 소개한다.
    3. 우리의 접근 방식은 LLM에서 지식을 추출하여 지식 저장소를 구축하고, 극소 규모 모델이 관련 정보를 검색하고 효과적인 추론을 위해 그것을 활용하도록 한다.

###### COUNT: COntrastive UNlikelihood Text Style Transfer for Text Detoxification (https://aclanthology.org/2023.findings-emnlp.579/)
- Anthology ID: 2023.findings-emnlp.579 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어 플랫폼에서의 혐오 및 독성 텍스트는 온라인 커뮤니티 내의 극단화와 분열을 야기시키고 건설적인 대화를 방해하는 요소이다. 이 논문에서는 텍스트 톡스화 (text detoxification)를 통해 안전하고 비-독성적인 텍스트를 생성하는 방법을 소개한다.
    2. 기존의 방법들은 supervised training에서 encoder-decoder 모델을 사용하여 표준 likelihood-based objective를 가진 골드 표준 출력을 생성하지만, 이러한 모델들은 사전에 학습된 auto-encoder identity mapping에서 벗어나기 어려워 한다.
    3. 이 논문에서는 새로운 contrastive unlikelihood objective (COUNT)를 소개하여 톡스적인 스타일 전이에 초점을 맞춰 톡식이 아닌 스타일 전이 학습에 집중하도록 한다. COUNT를 ParaDetox와 APPDIA 두 가지 데이터셋에서 벤치마킹한 결과, 순조로운 플루언시, 콘텐츠 보존, 그리고 톡스화 (highest "J" score)에서 상당한 개선을 보였다.

###### KICGPT: Large Language Model with Knowledge in Context for Knowledge Graph Completion (https://aclanthology.org/2023.findings-emnlp.580/)
- Anthology ID: 2023.findings-emnlp.580 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프 완성(KGC)은 지식 그래프의 불완전함을 해결하고 하위 응용 프로그램을 지원하는 데 중요하다. KGC는 triple-based와 test-based 방법으로 분류될 수 있는데, 이 중 triple-based 방법은 제한된 구조적 정보와 개체들의 불균형한 분포로 인해 long-tail 개체들에 대해 어려움을 겪는다. 이 논문에서는 훈련 오버헤드를 증가시키지 않으면서 long-tail 문제를 완화하기 위해 대규모 언어 모델과 triple-based KGC 검색기를 통합하는 KICGPT 프레임워크를 제안한다. 
    2. KICGPT 모델에서는 지식의 구조적 지식을 LLM에 안내하기 위해 Knowledge Prompt라는 in-context 학습 전략을 제안한다. 
    3. 벤치마크 데이터셋에서의 실험 결과는 KICGPT 모델이 더 가볍고 훈련 오버헤드 없이 더 효과적임을 보여준다.

###### Show, Write, and Retrieve: Entity-aware Article Generation and Retrieval (https://aclanthology.org/2023.findings-emnlp.581/)
- Anthology ID: 2023.findings-emnlp.581 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기사 이해는 자연어 처리에서 중요한 도전 과제로, 기사 생성이나 이미지-기사 검색 등 다양한 응용분야에 사용된다. 기존 연구는 사전학습 언어 모델을 사용하여 기사의 모든 토큰을 균일하게 인코딩했으나, 실제 기사는 실제 세계의 사건에 기반하고, 정확한 NER(Named Entity Recognition)가 어려운 많은 네임드 엔티티(Named Entities)를 참조할 수 있다.
    2. 본 논문에서는 ENGINE 프레임워크를 제안하여 네임드 엔티티를 언어 모델에 명시적으로 포함시키는 방법을 제시한다. 이 방법은 네임드 엔티티 추출 모듈과 모델의 엔티티 인식 및 예측 기능을 향상시킬 수 있는 엔티티 인식 기능을 포함한다.
    3. 실험 결과, ENGINE 모델은 GoodNews, VisualNews, WikiText와 같은 세 가지 공개 데이터셋에서 기사 생성 및 기사 검색 성능을 향상시킬 수 있으며, 기사 생성에서는 perplexity가 4-5 개 향상되었고, 기사 검색에서는 recall@1이 3-4% 향상되었다.

###### A Language Model with Limited Memory Capacity Captures Interference in Human Sentence Processing (https://aclanthology.org/2023.findings-emnlp.582/)
- Anthology ID: 2023.findings-emnlp.582 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사람들의 문장 처리 난이도에 영향을 미치는 두 가지 주된 요소는 기대치와 작업 메모리에서의 검색이다.
    2. 기존의 unified 모델들은 Transformer 언어 모델의 self-attention 메커니즘과 인간의 문장 처리에서의 cue-based retrieval 이론 사이의 유사점에 기반하여 작성되었으나, 이들은 구문에 특화된 attention head를 식별하는 것을 요구하고 수백 개의 메모리 검색이 병렬적으로 이루어진다는 인지적으로 불가능한 암묵적 가정을 사용한다.
    3. 본 논문에서는 인지 이론에서 가정되는 메모리 시스템과 더 가까운 단일 self-attention head를 가진 반복 신경 언어 모델을 개발하여, 우리의 모델의 단일 attention head가 인간의 실험에서 관찰되는 의미론적 및 구문론적 중간 개입 효과를 포착할 수 있다는 것을 보여준다.

###### Annotations Are Not All You Need: A Cross-modal Knowledge Transfer Network for Unsupervised Temporal Sentence Grounding (https://aclanthology.org/2023.findings-emnlp.583/)
- Anthology ID: 2023.findings-emnlp.583 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. TSG (Temporal Sentence Grounding)의 문제를 다루는 이 논문은 필수적인 작업에서 상당한 성과를 거두었지만, 실제 응용 프로그램에서는 상당한 인력이 필요한 비디오-쿼리 짝 지은 주석에 심하게 의존한다.
    2. 이를 위해 저자는 데이터가 부족한 상황에서 cross-modal task에서 얻은 지식을 이용하여 실제 시나리오에 적용하여, video-frame에 적용된다. 
    3. 실험 결과, 이러한 방법을 통해 unsupervised task에서도 supervised 작업보다 좋은 성과를 내는 것을 확인하였다.

###### Parameter Efficient Multi-task Fine-tuning by Learning to Transfer Token-wise Prompts (https://aclanthology.org/2023.findings-emnlp.584/)
- Anthology ID: 2023.findings-emnlp.584 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 작은 trainable 파라미터를 사용하여 pre-trained language model (PLM)을 고정시키면서 prompt tuning을 이용한 다양한 작업에서 성공적인 결과를 얻었지만, 각 개별 예제에 대해 더 적합한 prompt를 생성하는 방법과 cross-task feature를 활용하여 multi-task learning 시나리오에 prompt tuning을 확장하는 방법은 아직 논의되지 않았다.
    2. 이 논문에서는 token-wise prompt tuning (TPT)를 제안하여 메모리 네트워크를 사용하여 multi-task learning을 위한 더 세분화된 soft prompt tokens을 구축한다. 이 토큰들은 입력 예제와 대조되는 방식으로 bank에서 검색되어 인스턴스별 prompt로 조합된다.
    3. 14개의 데이터셋에 대한 실험 결과는 TPT로 향상된 모델이 전체 파라미터로 fine-tuning된 모델보다 훨씬 좋은 성능을 발휘하며, 0.035%의 파라미터만 조정하여 최고 수준의 결과를 달성했다.

###### A Rewriting Approach for Gender Inclusivity in Portuguese (https://aclanthology.org/2023.findings-emnlp.585/)
- Anthology ID: 2023.findings-emnlp.585 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 성별 포함 및 성별 중립 언어를 자연 언어 처리 모델에 통합하는 연구에 대한 관심이 높아졌다. 그 중 일반성 중립적인 문장을 성별 언어로 변경하는 gender-neutral rewriting이 주목을 받았는데, 이는 작은 자원을 가진 언어(예: 포르투갈어)에는 대용량 데이터셋을 사용하기 어렵다는 한계가 있다. 
    2. 이 논문에서는 법칙 기반과 신경 기반 모델을 사용하여 포르투갈어에 대한 gender-neutral rewriting을 수행하는 툴을 제안한다. 신경 기반 접근 방식은 법칙 기반 모델이 생성한 예제를 사용하여 대규모 다국어 기계 번역 모델을 fine-tuning하는 것에 기반한다. 
    3. 다양한 소스와 맥락의 텍스트를 기반으로 두 모델을 평가하였으며, future work의 평가를 위해 성별 중립 언어와 새로운 대명사를 명시적으로 포함한 포르투갈어 데이터셋과 500개의 문장에 대한 수동으로 주석이 달린 골든 콜렉션을 제공한다.

###### EARA: Improving Biomedical Semantic Textual Similarity with Entity-Aligned Attention and Retrieval Augmentation (https://aclanthology.org/2023.findings-emnlp.586/)
- Anthology ID: 2023.findings-emnlp.586 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 생물의학 텍스트 처리에서 의미론적 텍스트 유사성을 측정하는 것은 기본적인 작업이지만, 생물의학 분야의 STS 데이터셋은 일반적인 분야에 비해 상대적으로 작지만 의미론적으로 더 복잡하여 overfitting 문제와 잘 정의된 텍스트 표현이 어렵다. 
    2. 본 논문에서 이러한 문제를 해결하기 위해 entity-aligned, attention-based, retrieval-augmented PLMs라는 제안을 하였다. 
    3. 실험 결과 EARA는 도메인 내 및 도메인 외 데이터셋에서 최고의 성능을 보여주며, 소스 코드도 제공된다.

###### Neuro-Symbolic Sentiment Analysis with Dynamic Word Sense Disambiguation (https://aclanthology.org/2023.findings-emnlp.587/)
- Anthology ID: 2023.findings-emnlp.587 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 감성 분석은 단어의 의미 이해에 크게 의존하는 태스크이다. 기존의 신경망 모델은 인간에게 해석하기 어려운 벡터로 단어의 의미를 표현한다.
    2. 이 논문은 WSD (Word Sense Disambiguation) 시스템을 적용하는 데에 어려움이 있는데, 그 중에서도 i) 어떤 단어들을 disambiguate해야 하는지와 ii) downstream 모델에 명확하게 이해가능한 단어 의미를 어떻게 모델링할지에 대한 문제를 해결한다.
    3. Neurosymbolic 프레임워크를 제안하여 모호한 단어를 식별하고 어떤 의미론적으로 명확한 단어로 paraphrase함으로써 감성 예측의 정확성을 향상시키는 것을 목표로 한다. 이 프레임워크를 사용하면 어떤 단어가 어떤 의미론적으로 명확한 단어로 paraphrase되었는지 이해할 수 있다.

###### Role of Context in Unsupervised Sentence Representation Learning: the Case of Dialog Act Modeling (https://aclanthology.org/2023.findings-emnlp.588/)
- Anthology ID: 2023.findings-emnlp.588 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단어 형태와 단어 의미는 크게 연결되어 있지 않다는 관찰에 근거하여, 단어 표현의 비지도학습은 단어 발생 주변의 문맥 정보를 포착하는 작업을 수반한다.
    2. 그러나 문장에서도 동일한 패턴이 유효할지는 의문이다. 이 논문에서는 문장 표현 추론에서 문맥의 역할을 무시하지 않고 고려한 대화 행위 태그 프로빙 태스크를 제안한다.
    3. 결과는 문맥 기반의 문장 표현이 콘텐츠 기반의 문장 표현보다 명확한 이점이 없으나, 거의 모든 접근 방식에서 문장 벡터의 차원을 증가시키는 것이 매우 명확한 이점을 가진다는 것을 보여준다.

###### CLMSM: A Multi-Task Learning Framework for Pre-training on Procedural Text (https://aclanthology.org/2023.findings-emnlp.589/)
- Anthology ID: 2023.findings-emnlp.589 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 절차적 레시피에서 학습하는 도메인 특화 인공지능 모델인 ***CLMSM***을 제안한다. 이 모델은 Multi-Task Learning Framework를 사용하여 레시피의 개체 간 미묘한 차이를 학습하는 Contrastive Learning과 절차의 단계별 문맥을 학습하는 새로운 Mask-Step Modelling 목적을 최적화한다.
    2. 우리는 ***CLMSM***을 세 가지 데이터셋에서 개체 추적 및 절차 간 작업 조정과 같은 여러 후속 태스크에서 성능을 테스트하였는데, 그 중 하나는 사전 학습 데이터셋과 맞지 않는 open-domain 데이터셋이었다. 
    3. 우리는 ***CLMSM***이 레시피 (in-domain)에서 베이스라인을 능가할 뿐만 아니라 open-domain 절차적 NLP 태스크에도 일반화할 수 있는 능력을 보여준다.

###### Open-source Large Language Models are Strong Zero-shot Query Likelihood Models for Document Ranking (https://aclanthology.org/2023.findings-emnlp.590/)
- Anthology ID: 2023.findings-emnlp.590 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정보 검색 분야에서 Query Likelihood Models (QLMs)은 문서의 내용에 대한 쿼리 생성 확률을 기반으로 문서 순위를 매긴다. 
    2. 최근에는 미세 조정이 없이 구조화되지 않은 텍스트 데이터에만 사전 훈련된 LLMs이 QLMs로서 유망한 순위 매기기 능력을 보여준다.
    3. 그러나, 추가적인 지시어 미세 조정이 존재하지 않는 한 그런 LLMs의 순위 매기기 효과는 방해받을 수 있음을 밝힌다.

###### On General Language Understanding (https://aclanthology.org/2023.findings-emnlp.591/)
- Anthology ID: 2023.findings-emnlp.591 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "자연어 처리는 경험 중심적이며, 의미와 측정에 관한 본질적인 논쟁에 빠지고 있다."
    2. "이 논문에서는 현재 모델 품질의 측정 방법의 적절성을 물을 수 있는 이해 모델의 개요를 제시한다."
    3. "언어 이해는 다양한 현상으로 구성되며, 이해 지표의 선택이 벤치마킹의 한계를 표시하고 NLP 사용의 윤리를 고려하는 시작이 된다."

###### USB: A Unified Summarization Benchmark Across Tasks and Domains (https://aclanthology.org/2023.findings-emnlp.592/)
- Anthology ID: 2023.findings-emnlp.592 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 커뮤니티에서는 요약 벤치마크를 많이 만들었지만, 제어와 신뢰성과 관련된 여러 문제를 동시에 해결하기 위해 필요한 풍부한 주석을 제공하는 것은 없다. 
    2. 저자들은 위키피디아에서 파생된 벤치마크를 소개하고, 크라우드소싱된 풍부한 주석을 추가하여 8가지 관련된 작업을 지원한다.
    3. 이 논문에서는 이 벤치마크에서 다양한 방법을 비교하고, 보통 큰 규모의 퓨샷 모델보다 중간 규모의 파인튜닝 모델이 여러 작업에서 일관되게 우월한 성능을 내는 것을 발견한다.

###### tagE: Enabling an Embodied Agent to Understand Human Instructions (https://aclanthology.org/2023.findings-emnlp.593/)
- Anthology ID: 2023.findings-emnlp.593 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지능적 에이전트가 인간과 상호작용할 때 자연어가 주요한 의사소통 방식으로 사용되는데, 이에 대한 연구는 NLU(natural language understanding)과 관련하여 감정 분석, 의도 예측, 질문 응답, 요약 등으로 집중되어 있다. 
    2. 그러나 몸을 가진 에이전트가 필요로 하는 상황에서 NLU에 초점을 맞춘 연구는 아직 한정적이다. 이 논문에서는 복잡한 작업 지시문에서 일련의 작업을 추출하는 진보적인 신경망 모델을 제안한다. 
    3. 제안된 모델은 인코더-디코더 프레임워크와 중첩 디코딩을 결합하여 복잡한 지시문에서 작업과 해당 인수를 효과적으로 추출한다. 실험 결과는 제안한 방법이 강력한 기준 모델보다 우수함을 보여준다.

###### Instances and Labels: Hierarchy-aware Joint Supervised Contrastive Learning for Hierarchical Multi-Label Text Classification (https://aclanthology.org/2023.findings-emnlp.594/)
- Anthology ID: 2023.findings-emnlp.594 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Hierarchical multi-label text classification (HMTC)은 계층구조를 활용하여 다중 라벨 분류를 수행한다. 
    2. 기존 방법들은 샘플 생성을 위해 대조 학습을 사용하지만 같은 배치 내의 유사한 샘플들 사이의 상관관계를 무시하여 노이즈를 도입하는 경향이 있다. 
    3. 이 논문에서는 supervised contrastive learning과 HMTC 간의 간극을 메우기 위해 HJCL( Hierarchy-aware Joint Supervised Contrastive Learning) 방법을 제안하고 효과를 입증하였다.

###### Uncovering Limitations in Text-to-Image Generation: A Contrastive Approach with Structured Semantic Alignment (https://aclanthology.org/2023.findings-emnlp.595/)
- Anthology ID: 2023.findings-emnlp.595 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트에서 이미지를 생성하는 모델들은 복잡하거나 상세한 이미지를 생성하는 데에 여전히 어려움을 겪고 있다. 
    2. 우리는 텍스트-이미지 생성 모델의 성능을 평가하기 위해 구조적 의미 일치 (SSA) 방법을 제안한다. 
    3. SSA는 구조적 의미 임베딩을 학습하고 다양한 모달리티에서 일치시키는데 초점을 맞추며, 이를 통해 텍스트-이미지 세대 모델의 의미 일관성을 향상시킨다.

###### An Intent-based and Annotation-free Method for Duplicate Question Detection in CQA Forums (https://aclanthology.org/2023.findings-emnlp.596/)
- Anthology ID: 2023.findings-emnlp.596 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)의 등장으로 Community Question Answering (CQA) 포럼은 교육 튜닝의 용도로 활용 가능한 훌륭한 질문과 답변을 제공하며, 이에 대한 instruction tuning을 위해 LLM을 학습하는 데 효과적으로 사용할 수 있다. 
    2. 그러나 CQA의 콘텐츠 양이 계속해서 증가함에 따라 중복 질문의 문제가 발생하며, 이로 인해 콘텐츠의 품질에 위협이 될 수 있다. 
    3. 이 논문에서는 Intent-DQD라는 새로운 의도 기반 중복 탐지기를 제안하여 CQA에서 중복 질문을 탐지하는 문제를 해결한다. Intent-DQD는 CQA 포럼의 특성을 활용하고, 질문의 의도를 인식하고 매칭하기 위해 훈련 레이블을 추출한다. Intent-DQD는 의도 수준 관계를 효과적으로 종합하고 질문 수준의 관계를 구축하여 의도 인식 중복 탐지를 가능하게 한다.

###### Accelerating Multiple Intent Detection and Slot Filling via Targeted Knowledge Distillation (https://aclanthology.org/2023.findings-emnlp.597/)
- Anthology ID: 2023.findings-emnlp.597 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 비자기회귀(Spoken Language Understanding) 모델들은 추론 속도가 빠르기 때문에 주목을 받고 있지만, 대부분의 기존 방법은 추론 중 참조에 대한 사전 지식이 거의 없기 때문에 다중 모달성(multi-modality) 문제가 발생한다.
    2. 복잡한 프레임워크가 한계로 인해 희망하는 추론 속도를 달성하지 못하는 문제가 있다.
    3. 따라서 저자들은 지식 증류(knowledge distillation) 방법을 활용하여 다중 의도(Multi-intent) SLU를 위한 목표 지식 증류 프레임워크(TKDF)를 제안한다. 이 방법은 선생 모델로부터 지식을 전달하여 학습 속도를 높이고 성능을 개선한다.

###### Type-Aware Decomposed Framework for Few-Shot Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.598/)
- Anthology ID: 2023.findings-emnlp.598 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 몇몇 two-stage prototypical network 기반 few-shot named entity recognition (NER) 작업의 성공에도 불구하고, span detection 단계에서의 false spans와 type classification 단계에서의 부정확하고 불안정한 prototypes 문제는 여전히 도전적인 문제로 남아있다.
    2. 이 논문에서는 이러한 문제를 해결하기 위해 Type-Aware Decomposed framework인 TadNER를 제안한다. 세가지 성분으로 이루어진 이 프레임워크는, type-aware span filtering 전략과 type-aware contrastive learning 전략을 도입하여 문제를 해결한다.
    3. 다양한 벤치마크 실험을 통해 제안된 TadNER 프레임워크가 새로운 state-of-the-art 성능을 얻는 것을 입증하였다.

###### A Closer Look into Using Large Language Models for Automatic Evaluation (https://aclanthology.org/2023.findings-emnlp.599/)
- Anthology ID: 2023.findings-emnlp.599 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에서는 큰 언어 모델 (Large Language Models, LLMs)을 텍스트 품질 평가에 사용하는 것이 인기를 끌고 있다.
    2. 이 논문에서는 *LLM 평가*와 *G-Eval*에 대해 분석하고, 평가 과정의 세부 사항이 얼마나 잘 LLM의 평가와 인간의 평가 점수가 일치하게 하는지에 대해 논의한다.
    3. 우리는 G-Eval에서 사용된 자동 Chain-of-Thought (CoT)이 항상 인간의 점수와 일치하게 만들지 못한다는 사실을 발견했다. 또한, G-Eval과 같이 LLM이 숫자 평가만 출력하도록 강제하는 것은 최적화되지 않는다는 것을 보여준다. 마지막으로, LLM에게 자신의 평가를 설명하도록 요청하면 ChatGPT와 인간의 평가 사이의 상관 관계를 일정하게 향상시키고, 두 메타 평가 데이터셋에서 최신 기술 (SoTA) 상관 관계도 향상시킨다.

