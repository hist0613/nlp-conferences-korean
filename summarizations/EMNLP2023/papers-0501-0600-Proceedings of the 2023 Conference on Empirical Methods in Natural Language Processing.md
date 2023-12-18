# Korean Three-Line Summarizations of Papers 501-600 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### A Self-enhancement Multitask Framework for Unsupervised Aspect Category Detection (https://aclanthology.org/2023.emnlp-main.500/)
- Anthology ID: 2023.emnlp-main.500 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 작은 seed words 집합을 사용하여 비지도 Aspect Category Detection 문제를 해결하려는 연구이다. seed words와 문장 사이의 유사성을 활용하여 aspect를 학습하는 방식이 최근 많이 연구되었으나, seed words의 품질에 제약을 받아 모델 성능이 저하되는 문제가 있다.
    2. 이를 해결하기 위해 저자들은 initial seed words의 품질을 자동적으로 향상시키고, 전체 데이터셋을 사용하는 대신 고품질의 문장을 자동 선택하는 간단한 프레임워크를 제안한다.
    3. 또한, Aspect Term Extraction과 Aspect Term Polarity를 동시에 학습하여 성능을 향상시키려고 한다. 실험 결과 제안한 프레임워크가 표준 데이터셋에서 강력한 기준에 비해 우수한 성능을 보여주었다.

###### DialCoT Meets PPO: Decomposing and Exploring Reasoning Paths in Smaller Language Models (https://aclanthology.org/2023.emnlp-main.501/)
- Anthology ID: 2023.emnlp-main.501 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Chain-of-Thought (CoT) prompting은 1000억개 이상의 매개변수를 가지는 모델들의 추론 능력을 향상시키는 데 성공했으나, 10억개 미만의 작은 언어 모델(SLMs)에서는 추론 과제의 성능에 소용이 없거나 오히려 해로웠다. 
    2. 이 논문에서는 작은 언어 모델(SLMs)의 추론 능력을 향상시키기 위해 대화 형식으로 중간 추론 단계를 생성하여 최종 답안을 안내하는 Dialogue-guided Chain-of-Thought (DialCoT)를 제안한다. 또한 Proximal Policy Optimization (PPO) 알고리즘을 통해 모델이 최적의 추론 경로를 선택하도록 최적화하여 추론 능력을 더욱 향상시킨다. 
    3. 4개의 산술 추론 데이터셋에서의 포괄적인 실험 결과, 우리의 방법은 최신 경쟁 모델들과 비교하여 상당한 성능 향상을 달성할 수 있음을 보여준다.

###### Recurrent Neural Language Models as Probabilistic Finite-state Automata (https://aclanthology.org/2023.emnlp-main.502/)
- Anthology ID: 2023.emnlp-main.502 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전 연구들은 RNN 언어 모델의 표현 능력을 이해하기 위해 가중치가 없는 형식 언어를 인식하는 능력을 조사해왔다. 그러나 RNN 언어 모델은 가중치가 없는 형식 언어를 설명하지 않는다. 이 연구에서는 RNN 언어 모델이 표현할 수 있는 확률 분포의 클래스를 조사하여 그 능력을 직접적으로 이해할 수 있는 문장을 제시한다. 
    2. 연구 결과, 간단한 RNN은 확률 유한 상태 오토마타(probabilistic finite-state automata)의 하위 클래스와 동등하며, 이는 유한 상태 모델로 표현 가능한 확률 분포의 엄격한 부분집합을 모델링할 수 있다는 것을 보여준다.
    3. 또한, RNN을 사용하여 임의의 결정적 유한 상태 언어 모델을 표현하기 위해 𝛺\left(N |𝛴|\right) 개의 뉴런이 필요하다는 것을 보여준다. 이러한 결과는 RNN 언어 모델이 표현할 수 있는 확률 분포의 클래스를 특성화하는 첫 번째 단계로서, 그 능력과 제한을 이해하는 데 도움을 준다.

###### Revisiting Source Context in Nearest Neighbor Machine Translation (https://aclanthology.org/2023.emnlp-main.503/)
- Anthology ID: 2023.emnlp-main.503 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Nearest neighbor machine translation (kNN-MT)는 추가 예제로부터 유도된 추정치와 대상 토큰 확률을 보간하여 상당한 성능 향상을 이루어낸다" 하지만, 기존 연구는 유사한 예제를 검색할 때 소스 컨텍스트를 명시적으로 고려하지 않아 최적의 성능을 얻지 못할 수 있다고 주장한다. 
    2. 이를 해결하기 위해 저자들은 소스 컨텍스트의 역할을 복원하고, 소스 컨텍스트 강화를 통해 신경 기계 번역의 성능을 향상시키는 간단하고 효과적인 방법을 제안하였다.
    3. 실험 결과, 제안된 방법은 대표적인 kNN-MT 기준선에 통합될 수 있으며, 다양한 설정 및 도메인에서 이러한 강력한 기준선 대비 상당한 성능 향상을 보여준다.

###### Find-2-Find: Multitask Learning for Anaphora Resolution and Object Localization (https://aclanthology.org/2023.emnlp-main.504/)
- Anthology ID: 2023.emnlp-main.504 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 multimodal 이해 tasks 에서 시각적과 언어적 표현에 발생하는 모호성을 해결하기 위해, 이 논문에서는 시각과 언어 정보를 통합하는 novel한 end-to-end joint multitask 학습 프레임워크를 제안한다. 
    2. 이를 위해, Visual-linguistic Ambiguity를 해결하기 위한 Find2Find 데이터셋을 제작하였으며, 이 데이터셋을 활용한 실험결과는 기존의 단일태스크보다 많은 성능의 개선을 보여준다.
    3. 이 논문은 시각-언어 정합의 문제를 바라보는 새로운 시각에서 multimodal understanding의 연구를 진행하고 있다.

###### Background Summarization of Event Timelines (https://aclanthology.org/2023.emnlp-main.505/)
- Anthology ID: 2023.emnlp-main.505 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기사 작성자는 키 이벤트를 강조하기 위해 타임라인을 작성하지만, 이벤트에 대한 역사적 맥락을 모르는 사용자들은 따라가기 어렵다. 
    2. 이 논문에서는 background news summarization이라는 과제를 소개하여 각 타임라인 업데이트에 관련된 이전 이벤트의 요약을 보충한다. 
    3. Fine-tuned된 Flan-T5와 GPT-3.5를 사용하여 강력한 성능을 보이며, Question-Answering 기반의 Background Utility Score를 제안하여 배경 요약의 품질을 평가한다.

###### Superlim: A Swedish Language Understanding Evaluation Benchmark (https://aclanthology.org/2023.emnlp-main.506/)
- Anthology ID: 2023.emnlp-main.506 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Superlim은 스웨덴어 언어 모델의 성능을 평가하기 위한 다중 업무 NLP 벤치마크 및 분석 플랫폼이며, 그 결과를 이루는 데이터셋, 업무, 리더보드를 설명하고 참조 구현에서 얻은 기준 결과를 보고한다. 
    2. 테스트된 모델은 어떤 업무에서도 최고 성능을 보이지 않으며, 이는 Superlim이 실제로 어려운 벤치마크라는 것을 시사하며 이는 벤치마크에 대한 원하는 품질이다.
    3. 가장 적절한 측정 방법 선택, 데이터셋 문서화 및 리더보드의 편리성과 투명성을 고려하는 등, 작은 언어를 위한 데이터셋을 만들 때 클래스함에 대한 도전적인 문제를 다루고 있다.

###### Reasoning with Language Model is Planning with World Model (https://aclanthology.org/2023.emnlp-main.507/)
- Anthology ID: 2023.emnlp-main.507 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large language models, LLMs)은 Chain-of-Thought 스타일의 텍스트에 대해서는 뛰어난 추론 능력을 보여주었으나, 실행 계획 생성, 복잡한 수학 및 논리 추론과 같은 인간에게 쉬운 문제에는 여전히 어려움이 있다.
    2. 이 논문에서는 LLM의 한계를 극복하기 위해 Reasoning via Planning (RAP)라는 새로운 추론 프레임워크를 제안한다. RAP은 LLM을 세계 모델 및 추론 에이전트로 다목적으로 활용하고 Monte Carlo Tree Search(MCTS) 기반의 계획 알고리즘을 도입하여 넓은 추론 공간에서 전략적 탐색을 수행한다.
    3. 실험 결과, RAP은 실행 계획 생성을 포함한 다양한 어려운 추론 문제에서 CoT와 self-consistency를 기반으로 한 강한 베이스라인보다 우수한 결과를 나타내었으며, 예를 들어 LLaMA-33B에서 RAP은 GPT-4의 CoT와 비교하여 실행 계획 생성에서 상대적인 개선률 33%를 달성했다.

###### LLM-enhanced Self-training for Cross-domain Constituency Parsing (https://aclanthology.org/2023.emnlp-main.508/)
- Anthology ID: 2023.emnlp-main.508 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Cross-domain constituency parsing에서 self-training이 성공적으로 적용된다는 것이 증명되었으며, 이 연구에서는 이를 개선하기 위해 큰 언어 모델(LLM)을 사용하여 domain-specific raw corpus를 반복적으로 생성하는 방법을 제안한다.
    2. 구문 분석을 위해 LLM을 이용한 self-training은 LLM의 성능에 상관없이 기존 방법보다 우수한 성능을 보인다고 입증되었다.
    3. 또한, grammar rules과 신뢰도 기준을 사용하여 pseudo 데이터를 선택하면 cross-domain constituency parsing에서 가장 뛰어난 성능을 보인다.

###### Continual Named Entity Recognition without Catastrophic Forgetting (https://aclanthology.org/2023.emnlp-main.509/)
- Anthology ID: 2023.emnlp-main.509 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CNER에서는 기존 모델에 새로운 entity type을 순차적으로 통합하면서 모델을 업데이트하지만 catastrophic forgetting 문제가 심각하게 발생한다. 이 논문에서는 트레이드 오프를 잘 조정하는 pooled feature distillation loss를 도입하여 기존 entity type의 지식을 보존하면서 새로운 entity type을 효과적으로 습득하여 catastrophic forgetting 문제를 완화시킨다.
    2. 추가로, semantic shift 문제로 인해 이전 entity type이 비-엔티티 타입으로 통합되는데 이를 해결하기 위해 confidence-based pseudo-labeling을 제안한다. 또한, 편향된 타입 분포 문제를 해결하기 위해 adaptive re-weighting type-balanced learning 전략을 제안한다.
    3. 다양한 데이터셋을 이용한 실험을 통해 이 방법이 이전 최첨단 기법보다 우수한 성능을 보이며, Micro F1 점수와 Macro F1 점수에서 평균적으로 각각 6.3%와 8.0%의 개선을 보인다.

###### DSI++: Updating Transformer Memory with New Documents (https://aclanthology.org/2023.emnlp-main.510/)
- Anthology ID: 2023.emnlp-main.510 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다른 연구들이 성능이 좋은데도 불구하고, 시간과 함께 문서 집합이 변화하는 경우에 DSI 모델을 성공적으로 적용하는 것은 여전히 개방된 문제이다.
    2. 이 연구에서는 DSI++라는 지속적인 학습 도전 과제를 소개하며, 이는 이전과 새로 색인된 문서에 관련된 질의에 대답할 수 있으면서 동시에 새로운 문서를 계속해서 색인할 수 있는 DSI에 대한 것이다.
    3. 다양한 모델과 문서 식별자 표현에 걸쳐 지속적인 색인을 수행하면 이전에 색인된 문서를 상당히 잊어버리는 경우가 발생한다는 것을 보여주고, 이를 완화하기 위한 두 가지 접근 방식을 조사한다. 이로 인해 DSI++에서의 잊어버리기를 상당한 정도로 완화시키고 평균 Hits@10을 경쟁하는 기준에 비해 +21.1% 향상시킨다.

###### Editing Common Sense in Transformers (https://aclanthology.org/2023.emnlp-main.511/)
- Anthology ID: 2023.emnlp-main.511 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 트랜스포머의 파라미터를 직접 편집하는 것은 다시 학습하지 않고 오픈 소스 트랜스포머 기반 모델을 업데이트할 수 있게 한다.
    2. 기존의 편집 방법은 하나의 정답이 있는 백과사전적인 지식에 대한 문장에 대해만 평가되었다. 그러나 다중 정답을 갖는 상식적인 지식에 대한 연구는 수행되지 않았지만, 트랜스포머의 신뢰성과 유용성을 향상시키는 데 중요하다.
    3. 이 논문에서는 상식 판단이 트랜스포머 안의 특정 파라미터와 인과적으로 연관되어 있는지 조사하고, 그 결과 에디팅 알고리즘인 MEMITCSK를 개발하여 상식적인 도메인에서 성능을 향상시켰습니다.

###### Air-Decoding: Attribute Distribution Reconstruction for Decoding-Time Controllable Text Generation (https://aclanthology.org/2023.emnlp-main.512/)
- Anthology ID: 2023.emnlp-main.512 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CTG(Controllable text generation)은 원하는 속성을 가진 텍스트를 생성하는 것을 목표로 하고 있으나, 이 논문에서는 Attribute Collapse 현상을 처음으로 발견하였다. 이는 제어 강도가 임계 값을 초과하면 생성된 텍스트의 유창성이 급격히 하락하여 완전히 사용할 수 없게 만든다.
    2. 이 문제를 해결하기 위해, 우리는 Air-Decoding이라는 새로운 경량 디코딩 프레임워크를 제안한다. 이는 속성 단어와 속성이 아닌 단어 간의 가중치를 균형있게 조정하여 더 유창한 텍스트를 생성하기 위해 속성 분포를 재구성하는 것이 주요 아이디어이다.
    3. 여러 가지 CTG 태스크에서의 실험을 통해 우리의 방법이 새로운 최고 성능을 달성한다는 것을 입증하였다.

###### Homophone Disambiguation Reveals Patterns of Context Mixing in Speech Transformers (https://aclanthology.org/2023.emnlp-main.513/)
- Anthology ID: 2023.emnlp-main.513 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 트랜스포머는 음성 처리에서 핵심 아키텍처이지만, 음향 및 언어 구조에 대한 표현 방식에 대한 이해가 제한적이다. 
    2. 이 연구에서는 텍스트 모델을 위해 개발된 '문맥 혼합' 측정 방법을 음성 언어 모델에 적용하는 방법에 대해 조사한다.
    3. 우리는 트랜스포머 기반 음성 모델에서 이러한 통사적 힌트에 주의를 기울여 동음이의어를 구분하고 문법적 일치를 고려하여 정확한 전사를 식별하는 것을 발견했다.

###### Retrieval-Generation Alignment for End-to-End Task-Oriented Dialogue System (https://aclanthology.org/2023.emnlp-main.514/)
- Anthology ID: 2023.emnlp-main.514 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 지식 베이스(KB)에서 지식을 검색하기 위한 효율적인 retriever 개발은 특화된 과제를 효과적으로 처리하기 위한 task-oriented 대화 시스템에 중요하다. 
    2. 기존의 generative 모델들은 KB에서 검색된 레코드들 사이의 미묘한 차이를 구별하기 어렵기 때문에 생성된 응답의 품질이 좋지 않은 문제가 있다.
    3. 이 논문에서는 최대 마진 우도를 활용하여 지각적인 retriever를 훈련시키는 방법을 제안하며, 응답 생성에서의 신호를 사용하여 훈련한다. 또한, retrieved entity뿐만 아니라 다양한 meta knowledge를 활용하여 generator를 안내함으로써 지식의 활용을 향상시킨다.

###### IfQA: A Dataset for Open-domain Question Answering under Counterfactual Presuppositions (https://aclanthology.org/2023.emnlp-main.515/)
- Anthology ID: 2023.emnlp-main.515 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. KT에서 발생한 알고리즘 결함으로 휴대폰 15만 대가 교환될 예정이다.
    2. KT가 JANUS, JOOM, 인터파크등의 패스트트랙 메뉴를 제거하면서 발생한 결함은 5월부터 지급 앱을 충분히 지원하지 않게 되었다.
    3. 그래서 앱의 결함으로 사용자에게 피해가 발생할 경우 해피콜 상품권으로 배상할 예정이다.

###### How Do Large Language Models Capture the Ever-changing World Knowledge? A Review of Recent Advances (https://aclanthology.org/2023.emnlp-main.516/)
- Anthology ID: 2023.emnlp-main.516 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재 시대에는 큰 언어 모델 (LLM)들이 다양한 과제를 해결하는 데에서 인상적이지만, 배포 후 빠르게 구식화될 수 있다. 이 논문은 기존의 LLM이 항상 변화하는 세계 지식과 일치하도록 조정하는 최근 연구 동향을 종합적으로 검토한다. 
    2. 우리는 연구 작업을 체계적으로 분류하고 깊이 있는 비교와 논의를 제공한다. 
    3. 또한, 존재하는 도전과제를 논의하고 이 분야의 연구를 촉진하기 위한 미래 방향을 강조한다.

###### PreWoMe: Exploiting Presuppositions as Working Memory for Long Form Question Answering (https://aclanthology.org/2023.emnlp-main.517/)
- Anthology ID: 2023.emnlp-main.517 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LFQA(long-form question answering)에서 정보 탐색 질문은 불명확성이나 가정의 오류로 인해 잘못된 정보를 제공할 수 있다. 
    2. 이 논문에서는 모든 종류의 정보 탐색 질문을 처리할 수 있는 통합된 방법 PreWoMe를 제안한다. 
    3. PreWoMe는 질문의 가정을 추출하고 이를 작업 메모리로 활용하여 피드백과 행동을 생성하는 것을 중점으로 하는데, 실험 결과 PreWoMe는 잘못된 질문 뿐만 아니라 일반적인 질문에 대해서도 효과적으로 처리할 수 있다.

###### Memorisation Cartography: Mapping out the Memorisation-Generalisation Continuum in Neural Machine Translation (https://aclanthology.org/2023.emnlp-main.518/)
- Anthology ID: 2023.emnlp-main.518 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신경망을 훈련할 때 일부 데이터를 기억하면서 다른 데이터는 전혀 학습하지 않을 수 있다. 기억 현상은 좋다 나쁘다는 이진적인 특성으로 쉽게 표현할 수 없으며, 개별 데이터 포인트는 기억과 일반화 사이의 연속체에 위치한다.
    2. 우리는 신경기계번역(NMT) 모델을 대상으로 기억과 일반화 지도에 5백만 개의 데이터 포인트를 위치시키는 자원을 구축하기 위해 대조적인 기억 메트릭을 사용한다.
    3. 데이터 포인트의 특징과 모델의 per-datum 훈련 신호가 NMT에서의 기억에 예측적으로 작용하는 방식 및 이 지도의 하위 집합이 NMT 시스템의 성능에 미치는 영향에 대해 설명한다.

###### DecipherPref: Analyzing Influential Factors in Human Preference Judgments via GPT-4 (https://aclanthology.org/2023.emnlp-main.519/)
- Anthology ID: 2023.emnlp-main.519 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간의 좋아하는 요소는 작업과 장르에 따라 다양하지만, 인간 판단에 가장 좋아하지 않는 요소들은 일관되며, 예를 들어, 결과물이 너무 간결하거나 초점을 벗어난 내용이나 가공된 사실을 포함한다.
    2. Bradley-Terry-Luce (BTL) 모델을 사용하여 인간 판단에 내재된 선호도를 밝혀준다.
    3. 이 연구 결과는 미래 LLMs의 행동을 조정하는 중요한 단계인 균형 잡힌 데이터셋 구성에 영향을 미친다.

###### Gender Biases in Automatic Evaluation Metrics for Image Captioning (https://aclanthology.org/2023.emnlp-main.520/)
- Anthology ID: 2023.emnlp-main.520 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 모델 기반 평가 메트릭(CLIPScore와 GPTScore 등)은 다양한 언어 생성 작업에서 인간 판단과 상당한 상관관계를 나타냈다. 그러나 이러한 메트릭이 공정성에 미치는 영향은 여전히 미개척 상태이다.
    2. 미리 학습된 모델들은 사회적 편견을 우연히 인코딩할 수 있으므로, 이러한 모델을 평가 목적으로 사용하면 편향을 계속해서 유지 및 증폭시킬 수 있다.
    3. 이 논문에서는 이미지 캡션 작업에서의 모델 기반 자동 평가 메트릭의 성별 편향에 대한 체계적인 연구를 수행하고, 사전 학습된 모델을 사용하는 것의 부정적인 결과와 평가 메트릭의 편향을 완화하는 방법을 제시한다.

###### QA-NatVer: Question Answering for Natural Logic-based Fact Verification (https://aclanthology.org/2023.emnlp-main.521/)
- Anthology ID: 2023.emnlp-main.521 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사실 점검 시스템은 증거에 기반하여 주장의 진위를 평가한다. 이 논문에서는 natural logic 연산자를 예측하기 위해 질문-답변 방식을 사용하는 방법을 제안한다.
    2. 이 방법은 instruction-tuned 언어 모델의 일반화 능력을 활용하여 주석이 달린 훈련 데이터의 필요성을 제거하고 결정론적 추론 시스템에 의존한다.
    3. 실험 결과, 이 방법은 다른 자연어 연산자 시스템에 비해 FEVER에서 4.3%의 정확도 향상을 보였으며, 또한 다나ish 검증 데이터셋에서도 주석을 더하지 않은 모델들을 능가하는 성능을 보였다.

###### Increasing Probability Mass on Answer Choices Does Not Always Improve Accuracy (https://aclanthology.org/2023.emnlp-main.522/)
- Anthology ID: 2023.emnlp-main.522 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(LM)을 적용할 때 주어진 선택지 외의 어휘 토큰에도 확률이 지정되는데, 이러한 확률의 분포가 동일한 의미의 다른 형태에 걸쳐져 있는 것이 모델의 실제 성능을 과소평가하는 원인이 될 수 있다. 이를 "surface form competition" (SFC) 가설이라고 한다. 이 논문에서는 SFC의 영향을 처음으로 정량화하고 제한하는 수학적 형식을 제안한다.
    2. SFC를 줄이기 위한 간단한 방법을 찾아냈는데, 예를 들어 해당 답변 선택지를 프롬프트에 포함시키는 것과 단지 한 예제로만 인문학적 학습을 사용하여 주어진 답변 선택지에 대한 확률이 증가하도록 한다. 이 방법은 대부분의 경우에 SFC의 영향을 없앤다는 것을 보여준다.
    3. 3개의 다양한 데이터셋과 6개의 LMs에서의 실험을 통해 여러 가지 예상치 못한 결과를 확인할 수 있다. 예를 들어, SFC를 줄이기 위한 정규화 및 프롬프팅 방법은 일부 LMs에 대해 효과 없거나 성능을 떨어뜨릴 수 있다. 결론적으로 다중 선택 과제에 대해 LMs를 효과적으로 프롬프팅하기 위한 실용적인 통찰력을 제공한다.

###### Generating Data for Symbolic Language with Large Language Models (https://aclanthology.org/2023.emnlp-main.523/)
- Anthology ID: 2023.emnlp-main.523 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 성능과 복잡성을 모두 가져오지만, 최근 작업에서는 LLMs를 작업 추론기가 아닌 데이터 생성기로 변환시키는 것이 시작되었습니다. 그러나 이러한 접근 방식은 주로 자연 언어 작업에만 적용되어 왔고, 복잡한 구조화된 출력을 가진 기호 언어 작업에 대해서는 아직 탐구되지 않았습니다.
    2. 우리는 SymGen이라는 기법을 제안합니다. 이 기법은 LLMs를 활용하여 다양한 주석 비용이 많이 드는 기호 언어 데이터를 생성합니다. SymGen은 생성을 이끄는 정보성 단서와 데이터의 정확성을 향상시키기 위한 합의 기반 검증기로 구성됩니다.
    3. 다양한 설정에서 6개의 기호 언어 작업에 대해 광범위한 실험을 수행하였습니다. LLMs와 비교하여 1% 크기의 작업 모델이 유사하거나 더 좋은 성능을 달성할 수 있으며, 추론 및 배포 비용을 크게 줄일 수 있음을 보여줍니다. 또한, 작업 모델을 훈련할 때 인간 주석 데이터 양의 10 배 이상의 효과가 있는 사람이 작성한 데이터와 동등한 효과가 있는 생성된 데이터를 보여주어 주석 작업의 상당한 양을 절약할 수 있습니다. SymGen은 주석 비용이 많이 드는 복잡한 작업을 위한 데이터 생성으로 한 발 더 나아가며, 코드는 URL에서 공개되었습니다.

###### IDTraffickers: An Authorship Attribution Dataset to link and connect Potential Human-Trafficking Operations on Text Escort Advertisements (https://aclanthology.org/2023.emnlp-main.524/)
- Anthology ID: 2023.emnlp-main.524 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간 노예거래 문제는 온라인 광고와 관련이 있어 경찰에게 가해주는 어려움이 증가하고 있다. 이 문제를 해결하고자 이 논문에서는 인터넷 에스코트 시장에서 인간 노예거래 판매자를 식별하기 위한 데이터셋인 IDTraffickers을 소개한다.
    2. 우리는 DeCLUTR-small 모델을 훈련하여 저자 식별에 대한 벤치마크를 구축하였고, 폐쇄집합 분류 환경에서 0.8656의 Macro-F1 점수를 달성했다.
    3. 또한, 훈련된 분류기에서 추출한 스타일 표현을 활용하여 저자 확인을 수행하였고, 개방집합 순위 환경에서 평균 R-정밀도 점수 0.9852을 얻었다. 이러한 데이터셋과 벤치마크의 공개는 보다 효과적으로 에스코트 광고를 연결하고 노예거래 지표를 식별하는 강력한 접근법을 개발하기 위해 미래의 연구자들에게 도움을 줄 것으로 기대된다.

###### Evaluating Bias and Fairness in Gender-Neutral Pretrained Vision-and-Language Models (https://aclanthology.org/2023.emnlp-main.525/)
- Anthology ID: 2023.emnlp-main.525 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습된 기계 학습 모델은 기존 데이터의 편견을 지속시키고 심지어 강화하는 경향이 있는데, 이는 사용자 경험에 영향을 주는 불공정한 결과로 이어질 수 있다. 
    2. 이 논문에서는 사전학습과 세밀 조정 단계에서의 성별 편견을 측정하고 그 영향에 대해 연구한다. 
    3. 전체적으로 사전학습과 세밀 조정 사이에 성별 편향 증폭은 독립적인 것으로 나타난다. 또한 성별 중립적 데이터에 대한 지속적인 사전 학습이 VQAv2 및 검색 작업에서 공정성을 증가시키는 동시에 작업 성능에 큰 영향을 주지 않는 것을 발견했다.

###### Improving Dialogue Discourse Parsing via Reply-to Structures of Addressee Recognition (https://aclanthology.org/2023.emnlp-main.526/)
- Anthology ID: 2023.emnlp-main.526 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 문맥 파싱은 대화의 관계 기반 구조를 반영하기 위해 대화 관계에 따라 의미 관계를 형성함으로써 데이터 희소성 문제를 완화한다. 
    2. 이전 연구들은 관련 작업 (예: 읽기 이해)과 함께 대화 문맥 파싱을 학습하는 다중 작업 접근법을 채택하여 일반화성을 제한하지만, 우리는 인접 작업(수신자 인식)과 대화 문맥 파싱을 통합하는 다중 작업 프레임워크를 제안한다.
    3. 실험 결과, 우리의 제안 방법은 Molweni와 STAC 데이터셋에서 SOTA 기준보다 우수한 성능을 보였으며, 코드는 https://github.com/yxfanSuda/RLTST 에서 사용 가능하다.

###### Improving Language Models’ Meaning Understanding and Consistency by Learning Conceptual Roles from Dictionary (https://aclanthology.org/2023.emnlp-main.527/)
- Anthology ID: 2023.emnlp-main.527 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 사전 훈련 언어 모델 (PLM)은 비인간적인 행동으로 인해 신뢰성이 떨어지고 있다. 
    2. 이 논문에서는 개념적 역할 이론을 기반으로 한 실제 접근 방식을 제안하여 PLM의 의미 인식 능력을 개선하여 모순된 행동 문제를 완화한다. 
    3. 실험 결과는 이 방법이 다양한 유형의 일관성을 동시에 개선하고 지식 통합을 효율적으로 가능하게 하며 다른 언어에도 적용하기 쉽다는 것을 보여준다.

###### DALE: Generative Data Augmentation for Low-Resource Legal NLP (https://aclanthology.org/2023.emnlp-main.528/)
- Anthology ID: 2023.emnlp-main.528 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. DALE은 저자들이 법률 NLP 분야에서의 저자들과의 작업에 있어 낮은 자원 환경(low-resource)에서의 유용하며 창의적인 데이터 증강(Data Augmentation) 프레임워크로 소개된다.
    2. DALE은 법률 문서에서 효과적인 데이터 증강을 생성함에 있어 다른 프레임워크에서 제시되는 도전과제들을 해결한다.
    3. DALE은 선행된 논문들이 가져온 방법들의 과제들을 극복하기 위해 저작자들이 개발한 생태계 특화 언어 모델에 기반한 자율적 텍스트 노이즈 제거 목적으로 사전 훈련되었다.

###### FedID: Federated Interactive Distillation for Large-Scale Pretraining Language Models (https://aclanthology.org/2023.emnlp-main.529/)
- Anthology ID: 2023.emnlp-main.529 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사용자 데이터 개인정보 보호에 대한 우려와 규제로 인해 분산 학습 패러다임이 필요하지만, 현재의 federated learning (FL)은 통신 오버헤드, 이질성 처리 불가능성, 흰색 상자 추론 공격 등의 중요한 한계가 있다.
    2. 따라서 이 논문에서는 이러한 한계를 완화하기 위해 FedID라는 새로운 기법을 제안한다. 이는 서버가 보유한 작은 양의 레이블 데이터를 사용하여 지식 전달 중 로컬 모델을 보완한다.
    3. 실험 결과, 우리의 제안한 FedID 프레임워크는 동질적이고 이질적인 federated 시나리오에서 최상의 결과를 얻을 수 있다.

###### trlX: A Framework for Large Scale Reinforcement Learning from Human Feedback (https://aclanthology.org/2023.emnlp-main.530/)
- Anthology ID: 2023.emnlp-main.530 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간 피드백을 통한 강화 학습은 학습된 보상 모델을 바탕으로 대형 언어 모델을 인간의 기호와 더 잘 일치시키기 위해 온라인 최적화를 통해 인간 피드백을 활용한다. 
    2. 현재의 RLHF 패러다임은 대규모 아키텍처에 대한 구현과 확장에 어려움을 겪는다. 
    3. 본 논문에서는 70 억 개 이상의 파라미터를 가진 모델에 대해 RLHF fine-tuning을 위한 AutoRLHF 라이브러리를 제안하며, 다양한 유형의 분산 트레이닝 및 계산 및 메모리 절약 기능을 구현하여 다양한 컴퓨팅 리소스를 지원한다.

###### This is not a Dataset: A Large Negation Benchmark to Challenge Large Language Models (https://aclanthology.org/2023.emnlp-main.531/)
- Anthology ID: 2023.emnlp-main.531 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 문법적 지식과 일반화 능력을 일부 보여주지만, 부정(negation)을 해석하는 데 실패한다. 
    2. LLMs는 긍정문을 분류하는 데 능숙하지만, 부정문에는 어려움을 겪고 부정에 대한 깊은 이해력이 부족하다는 것을 밝혀냈다.
    3. 부정 문장에 대한 모델의 성능을 향상시키기 위해 모델을 fine-tuning하는 것은 도움이 되지만, 부정 이해의 일반화 부족은 여전히 지속되며, 부정에 대한 언어 모델의 계속되는 도전을 강조한다.

###### MT2: Towards a Multi-Task Machine Translation Model with Translation-Specific In-Context Learning (https://aclanthology.org/2023.emnlp-main.532/)
- Anthology ID: 2023.emnlp-main.532 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문장 수준 번역, 문서 수준 번역, 번역 메모리, 용어 제약 번역 등은 기계 번역에 중요한 역할을 한다. 그러나 이전 연구들은 각각의 작업을 해결하기 위해 별도의 모델이나 방법을 사용하여, 서로 다른 작업 간의 지식 전달을 방해하고 시스템 구축의 복잡성을 증가시킨다.
    2. 이 논문에서는 사전 훈련된 언어 모델의 기계 번역 과제에서의 잠재력을 탐색하고, 여러 번역 작업을 통합하는 Multi-Task Machine Translation (MT2) 모델을 제안한다.
    3. 우리는 모델 훈련을 위해 문맥 학습을 수행하는 새로운 In-Context Learning (ICL) 패러다임을 설계하였으며, 문맥 정보를 통합하여 성능을 개선하는 문맥 학습 작업으로 모든 번역 작업을 모델링할 수 있다. 또한, 검색 및 정렬 방법과 두 가지 문맥 종속적인 훈련 전략을 채택하여 모델이 번역에 있어 문맥 정보를 더 잘 이해하고 활용할 수 있도록 한다. 실험 결과는 우리 모델의 우수한 성능과 제안한 방법의 효과를 입증한다.

###### CleanCoNLL: A Nearly Noise-Free Named Entity Recognition Dataset (https://aclanthology.org/2023.emnlp-main.533/)
- Anthology ID: 2023.emnlp-main.533 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CoNLL-03 corpus은 명명된 entity 인식(NER)에서 가장 잘 알려진 벤치마크 데이터셋으로 알려져 있지만, 이 데이터는 주석 오류, 불완전함 및 불일치를 포함하여 이전의 연구에서 문제점으로 지적되고 있다.
    2. 이 논문에서는 자동 일관성 체크를 사용하여  English CoNLL-03의 모든 라벨의 7.0%를 수정하는 종합적인 다시 라벨링 작업을 제안한다.
    3. 실험적 평가에서, 우리의 데이터에서 state-of-the-art 접근법은 F1-score (97.1%)을 달성하는데, 이 데이터는 주석 노이즈로 인해 잘못 계산된 정확한 예측의 비율이 47% 에서 6% 으로 줄어든 것으로 나타난다.

###### Disentangling Transformer Language Models as Superposed Topic Models (https://aclanthology.org/2023.emnlp-main.534/)
- Anthology ID: 2023.emnlp-main.534 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 주제 모델링은 토픽의 질을 일괄성 측정으로 측정하는데, Neural Topic Models(NTM)에서 기계가 학습한 주제를 디코더 가중치로 추론한다. 그러나, Transformer-based Language Models(TLM)에서는 가설화된 합성 속성으로 인해 최종 logit은 해석이 불가능하게 된다고 한다.
    2. 이 연구에서는 TLM을 여러 일관된 주제와 연결시킬 수 있는 가중치 기반의 접근 방식을 제안하여 TLM을 해석 가능하게 만드는 방법을 제안하고, GPT-2 모델에서 Wikipedia 코퍼스를 사용하여 이를 실현할 수 있다는 것을 실험적으로 보여주었다. 
    3. 또한, 제안한 방법론을 LLaMA 모델에 적용하여 주제를 분리하고 분석할 수 있다고 제안한다.

###### Conversational Semantic Parsing using Dynamic Context Graphs (https://aclanthology.org/2023.emnlp-main.535/)
- Anthology ID: 2023.emnlp-main.535 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 대화 기록의 맥락에서 사용자 발화를 실행 가능한 논리 형태(Sparql 등)로 인터랙티브하게 매핑하는 대화적 의미 파싱 작업을 다룬다.
    2. 우리는 동적으로 생성되는 서브그래프를 활용하여 발화와 그 맥락에 대한 정보를 표현하는데, 이 서브그래프는 노드의 개수가 발화마다 다르다.
    3. 실험 결과, 동적 맥락 모델링이 정적 접근 방식에 비해 성능이 우수하며, 단순하고 복잡한 질문 모두에서 성능 향상을 보여줌을 확인하였다.

###### Not all quantifiers are equal: Probing Transformer-based language models’ understanding of generalised quantifiers (https://aclanthology.org/2023.emnlp-main.536/)
- Anthology ID: 2023.emnlp-main.536 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer 기반 언어 모델(TLM)의 행동에 일반화된 양자가 어떻게 영향을 미치는지에 대한 연구는 종종 논리적으로 정의된 작업을 활용하지 않아 일반화된 양자의 논리적 중요성을 정확하게 포착하지 못했다는 문제가 있다.
    2. 이 논문에서는 논리적으로 정의된 텍스트 강조 (textual entailment) 문제를 활용하여 다양한 일반화된 양자가 TLM에 어떤 영향을 미치는지 조사한다. 
    3. 결과적으로, TLM은 일반적으로 가장 일반적인 일반화된 양자의 논리적 의미를 이해할 수 있지만, 다른 양자들은 TLM에 다양한 방식으로 영향을 준다는 것을 밝혀냈다.

###### Structure-aware Knowledge Graph-to-text Generation with Planning Selection and Similarity Distinction (https://aclanthology.org/2023.emnlp-main.537/)
- Anthology ID: 2023.emnlp-main.537 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 그래프(Knowledge graph)-텍스트(KG-to-text) 생성 작업은 입력 지식 그래프에서 유래된 복잡한 정보를 정확하게 전달하는 일관적이고 매력적인 문장을 합성하는 것을 목표로 한다. 
    2. 이 작업에서의 주요 도전 과제 중 하나는 다양한 KG 및 대상 텍스트의 구조 사이의 간극을 줄이면서 입력 KG의 세부 정보를 보존하는 것이다. 
    3. 본 논문에서는 pre-trained language models와 graph structure-aware 모듈을 효율적으로 통합하는 새로운 접근 방식을 제안한다.

###### SOUL: Towards Sentiment and Opinion Understanding of Language (https://aclanthology.org/2023.emnlp-main.538/)
- Anthology ID: 2023.emnlp-main.538 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 감성 분석은 자연어 처리의 잘 알려진 과제로서, 감성 극성 분류는 가장 인기있고 대표적인 태스크 중 하나이다. 그러나 pretrained language model의 성공에도 불구하고, 그들은 종종 감성 분석의 더 넓은 복잡성을 잡아내지 못한다.
    2. 이 문제를 해결하기 위해, Sentiment and Opinion Understanding of Language (SOUL)이라는 새로운 태스크를 제안한다. SOUL은 Review Comprehension (RC)와 Justification Generation (JG)이라는 두 가지 서브태스크를 통해 감성 이해를 평가한다.
    3. 실험 결과는 SOUL이 작은 language model과 큰 language model 모두에 대해 어려운 태스크임을 보여주며, 인간의 성능과 비교하여 최대 27%의 성능 차이를 보인다. 또한, 전문가와 GPT-4를 사용한 평가는 작은 language model이 추론 기반의 이유 생성에서의 한계를 강조한다.

###### Regulation and NLP (RegNLP): Taming Large Language Models (https://aclanthology.org/2023.emnlp-main.539/)
- Anthology ID: 2023.emnlp-main.539 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 자연어 처리와 인공 지능 분야에서의 과학적 혁신은 가장 빠른 속도로 진행되고 있다. 
    2. 이 논문에서는 현재 AI 안전성과 AI 윤리 운동에 의해 주도되는 편향된 이야기에 지배되는 AI 규제 및 거버넌스에 관한 중요한 논쟁이 있다고 주장한다. 
    3. 그리고 NLP 연구에서는 현재 위험 평가에 대한 논의가 증가하고 있으나 과학적 기초가 부족하여 이와 관련된 규제에 대한 연구의 신뢰성을 저해하고 있다고 주장한다.

###### MedEval: A Multi-Level, Multi-Task, and Multi-Domain Medical Benchmark for Language Model Evaluation (https://aclanthology.org/2023.emnlp-main.540/)
- Anthology ID: 2023.emnlp-main.540 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. MedEval은 의료 분야의 언어 모델 개발을 촉진하기 위한 다중 수준, 다중 과제 및 다중 도메인 의료 벤치마크다. 이 데이터셋은 8가지 검사 방법으로부터 35개의 인체 부위에 걸친 정보를 제공하며, 전문가 주석을 통해 다양한 수준에서의 데이터 활용과 다양한 작업을 지원한다.
    2. 우리는 의료 분야에 대응된 기본 모델부터 ChatGPT와 같은 대형 언어 모델까지 10가지 일반 및 도메인 특화된 언어 모델을 zero-shot 및 fine-tuning 설정에서 체계적으로 평가했다.
    3. 이 연구를 통해 우리는 대형 언어 모델의 활용에 있어 instruction tuning의 중요성과 의료 분야에서의 강점과 한계에 대한 유용한 통찰력을 제공한다.

###### Seeing through the mess: evolutionary dynamics of lexical polysemy (https://aclanthology.org/2023.emnlp-main.541/)
- Anthology ID: 2023.emnlp-main.541 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단어는 여러 의미를 가질 수 있다. 예를 들어, 단어 "mess"는 음식을 제공하는 장소이거나 혼란스러운 상황을 나타낼 수 있다. 이 연구에서는 다의성(polysemy)로 이어지는 기작을 조사하기 위해 어휘 의미의 진화에 대한 수학적 모델을 제안하고 분석한다.
    2. 이 모델에서는 어휘 처리와 전달에 영향을 미치는 요인들인 단어 빈도, 비준수주의(non-conformism), 의미 구별력을 고려하고 있다.
    3. 낮은 빈도, 비준수주의 사용을 선호하는 경향, 그리고 높은 의미 구별력이 다의성을 유지하는 여러 의미가 생성될 수 있는 조건임을 수학적으로 증명하였으며, 영어 단어의 의미 발전을 다루는 역사 언어 데이터로 이러한 예측을 통계적으로 검증하였다.

###### Are Embedded Potatoes Still Vegetables? On the Limitations of WordNet Embeddings for Lexical Semantics (https://aclanthology.org/2023.emnlp-main.542/)
- Anthology ID: 2023.emnlp-main.542 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지식 베이스 임베딩 (KBE) 모델은 WordNet을 포함한 지식 베이스의 구조적 정보를 인코딩하는 데에 널리 사용되는데, 기존의 문헌은 주로 link prediction을 평가하는 것에 초점을 맞추어 왔으며, 모델의 의미적 능력을 탐구하는 것을 소홀히 했다.
    2. 본 논문에서는 WordNet의 KBE 모델이 link prediction에서의 성능과 의미 정보를 인코딩하는 능력 사이에 잠재적인 연결이 없을 수 있다고 조사하고, 현재의 평가 프로토콜의 한계를 강조한다.
    3. 결과적으로, WN18RR 벤치마크에서 성능이 우수한 KBE 모델 중 일부는 두 가지 의미적 태스크 및 두 가지 후속 태스크에서 부적절한 결과를 나타내고 있으며, 이는 KBE 모델의 의미적 능력을 평가하기 위한 link prediction 벤치마크의 무력함을 보여주며, 더 효과적인 평가 접근 방식의 필요성을 제시한다.

###### Evaluation Metrics in the Era of GPT-4: Reliably Evaluating Large Language Models on Sequence to Sequence Tasks (https://aclanthology.org/2023.emnlp-main.543/)
- Anthology ID: 2023.emnlp-main.543 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델들의 평가는 불안정하고 일관성 없는 상황이며, 자동 평가 메트릭의 품질은 생성 모델의 발전 속도에 따라 따라가지 못하고 있다.
    2. 우리는 여러 개의 벤치마크 (text summarisation, text simplification, GEC)에서 여러 개의 LLMs 를 automatic과 human 평가를 통해 초기 형태의 성능 평가를 제공함으로써 현재 모델의 성능을 향상시키고자 한다. 
    3. 우리는 ChatGPT가 대부분의 메트릭에서 인간 평가자들에게 따르면 다른 인기 있는 모델보다 일관적으로 더 우수한 성능을 보이지만, 전통적인 자동 평가 메트릭을 사용할 때는 훨씬 저조한 점수를 얻는 것으로 나타냈다.

###### Event-Location Tracking in Narratives: A Case Study on Holocaust Testimonies (https://aclanthology.org/2023.emnlp-main.544/)
- Anthology ID: 2023.emnlp-main.544 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구는 이야기 이해의 공간적 차원에 초점을 맞추며, 이야기 텍스트에서의 사건 위치 추적(task)을 제안한다고 한다. 이 작업은 이야기가 진행됨에 따라 발생하는 위치의 연속열을 추출하는 것을 목표로 한다.
    2. 이 위치 추적(task)을 위해 다양한 수준의 컨텍스트 인식을 가지는 구조를 제안하고, 좁은 컨텍스트에서 강력한 방법을 적용하는 등 다양한 기준선 비교를 통해 성능을 평가한다.
    3. 홀로코스트 피난민의 증언을 테스트 케이스로 삼아, 이 데이터셋을 산업화수단으로 연구하는 것의 도덕적, 역사적 중요성을 주장하며, 더 많은 문맥을 인식하는 모델이 보다 정확한 위치 연속열을 생성할 수 있음을 실험 결과로 입증한다.

###### Dialogizer: Context-aware Conversational-QA Dataset Generation from Textual Sources (https://aclanthology.org/2023.emnlp-main.545/)
- Anthology ID: 2023.emnlp-main.545 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "대화형 질문응답(ConvQA)에서의 데이터 부족 문제를 해결하기 위해, 대화 채우기(dialog inpainting) 방법이 제안되었다. 그러나 원래의 대화 채우기 모델은 대화 복원(task)에만 초점을 맞춰 학습되기 때문에, 질문-답변 정렬의 부족한 학습으로 인해 문맥적 연관성이 낮은 질문을 생성하게 된다."
    2. "따라서 저희는 Dialogizer라는 새로운 프레임워크를 제안한다. 이 프레임워크는 텍스트 소스로부터 고문맥 연관성을 가진 ConvQA 데이터셋을 자동으로 생성할 수 있는 능력을 갖추고 있다."
    3. "우리의 프레임워크를 사용하여 다중 도메인의 문서를 기본 소스로 활용하여 4개의 ConvQA 데이터셋을 생성하였으며, 다양한 메트릭을 사용한 자동 평가 및 인간 평가를 통해, 우리의 프레임워크가 기준선 대화 채우기 모델보다 더 높은 품질의 데이터셋을 생성하는 능력을 검증하였다."

###### Learning to Predict Task Transferability via Soft Prompt (https://aclanthology.org/2023.emnlp-main.546/)
- Anthology ID: 2023.emnlp-main.546 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델을 중간 단계 작업에 미세 조정(fine-tuning)하는 것은 대상 작업의 성능을 크게 향상시킬 수 있지만, 성공적인 전이를 위한 소스 작업을 효율적으로 찾는 방법은 아직 충분히 연구되지 않았다.
    2. 우리는 전이 가능성(transferability)을 예측하기 위해 유사도 점수 함수를 학습하는 것을 제안한다. 소프트 프롬프트를 과업 특정 정보를 요약한 과업 임베딩으로 취급하여 테스크 쌍을 무작위로 샘플링하여 점수 함수를 훈련시킨다.
    3. 실험 결과, 우리의 방법은 효율적으로 전이 학습에 유용한 소스 작업을 식별한다는 것을 보여준다.

###### Chain-of-Questions Training with Latent Answers for Robust Multistep Question Answering (https://aclanthology.org/2023.emnlp-main.547/)
- Anthology ID: 2023.emnlp-main.547 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Chain-of-Questions"은 서브 질문을 생성하고 답하는 방식으로 다단계 질문에 대한 강력한 답변을 제공할 수 있는 프레임워크이다. 
    2. 우리는 인간이 주석을 단 질문 분해 의미 표현(QDMR)에서 서브 질문에 대한 지도를 얻지만, QDMR에는 서브 질문에 대한 주석된 답변이 포함되어 있지 않다. 
    3. 이를 극복하기 위해, 우리는 서브 답변을 잠재 변수로 취급하고, Hard-EM과 MAPO의 동적 혼합을 통해 서브 답변을 추론하는 새로운 방법을 제안한다.

###### Mirror: A Universal Framework for Various Information Extraction Tasks (https://aclanthology.org/2023.emnlp-main.548/)
- Anthology ID: 2023.emnlp-main.548 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정보 추출 (IE) 태스크 간의 지식 공유는 다양한 데이터 형식과 태스크 변이 때문에 언제나 어려움이 되어왔습니다. 이 논문에서는 IE 문제를 다양한 IE 태스크에 대한 통합된 multi-slot tuples 으로 재구성하고 다양한 IE 태스크에 대한 범용 프레임워크로 Mirror를 제안합니다.
    2. 기존 IE 태스크를 multi-span 순환 그래프 추출 문제로 바꾸고, 포괄적인 그래프 디코딩 알고리즘을 사용하여 모든 범위를 한 번에 추출하는 방법을 제안합니다. 이 그래프 구조는 놀랄만큼 유연하며 복잡한 IE 작업 뿐만 아니라 기계 독해 및 분류 작업도 지원합니다.
    3. 전이학습을 위해 57개의 데이터셋으로 모델 사전훈련을 수행한 후, 8개의 하위 태스크에서 30개의 데이터셋에 대한 실험을 진행하였고, SOTA (State-of-the-Art) 시스템과 비교하여 우수한 호환성을 나타냈습니다. 소스 코드, 모델 가중치 및 사전훈련된 코퍼스는 https://github.com/Spico197/Mirror 에서 제공됩니다.

###### “Mistakes Help Us Grow”: Facilitating and Evaluating Growth Mindset Supportive Language in Classrooms (https://aclanthology.org/2023.emnlp-main.549/)
- Anthology ID: 2023.emnlp-main.549 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 선생님들의 성장 마인드셋 지원 언어 (GMSL)는 시간이 흐름에 따라 기술을 향상시킬 수 있다고 강조하는 이론이 학업 성취 격차를 크게 줄이고 학생들의 학습 결과를 향상시킬 수 있다는 것이 입증되었다. 
    2. 하지만 대부분의 선생님들은 GMSL을 적용하기 어려워 이 분야에서 효과적인 코칭이 부족한 상황이다. 
    3. 우리는 대형 언어 모델 (LLMs)이 GMSL 사용을 지원하기 위한 자동화된 개인화 된 코칭을 제공할 수 있는지 조사한다.

###### Unnatural Error Correction: GPT-4 Can Almost Perfectly Handle Unnatural Scrambled Text (https://aclanthology.org/2023.emnlp-main.550/)
- Anthology ID: 2023.emnlp-main.550 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 Large Language Models (LLMs)는 여러 작업에서 놀라운 성능을 보이지만, 이들의 내부 작업 방식에 대해서는 여전히 많은 불명확한 점이 남아 있다.
    2. 우리는 이 논문에서, 많은 순차적인 변경을 겪었을 때 LLM의 복원력에 대한 실험적인 통찰력을 제시한다.
    3. 실험 결과에서는 GPT-4를 비롯한 몇 가지 고급 LLM들이 단어의 첫글자와 마지막 글자만 유지되면 의미를 잘 이해할 수 있다는 typoglycemia 현상과 유사한 능력을 보임을 확인하였다.

###### Detecting and Mitigating Hallucinations in Multilingual Summarisation (https://aclanthology.org/2023.emnlp-main.551/)
- Anthology ID: 2023.emnlp-main.551 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신뢰할만한 자동 요약 모델을 위해서는, hallucination(환상) 문제를 해결해야 한다. 특히 저자들은 low-resource 언어에서 cross-lingual transfer 요약을 할 경우, 신뢰도를 평가하기 위한 새로운 메트릭인 mFACT를 개발하여, 세계적으로 유명한 다수의 faithful metric 기반으로 영어를 제외한 다른 언어의 신뢰성을 측정하고자 한다.
    2. 저자들은 mFACT가 다른 대안 메트릭과 비교하여 hallucination을 감지하는 데 가장 적합하다는 것을 다국어로 여러 실험을 통해 입증하였다. 
    3. 또한, 저자들은 크로스-언어 전송에서의 hallucination 문제를 완화하기 위한 간단하고도 효과적인 방법을 제안하며, 이는 강한 기준인 MAD-X와 같은 크로스-언어 전송을 위한 대안 모델과 비교했을 때, 성능과 신뢰성 모두에 큰 향상을 가져왔다고 보여주었다.

###### Exploring Linguistic Probes for Morphological Inflection (https://aclanthology.org/2023.emnlp-main.552/)
- Anthology ID: 2023.emnlp-main.552 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 형태소 변화(cross-linguistic)에 대한 컴퓨터 모델링 연구는 대개 언어 독립적인 데이터 분할 알고리즘을 사용하고 있다. 본 논문에서는 이 접근 방식을 보완하기 위해 유형별형태현 시스템(conjugational classes)과 특징 집합(feature sets)의 형태론적 일반화 측면을 테스트하기 위한 언어별 조사 방법을 제안한다.
    2. 이 조사 방법을 영어, 스페인어, 스와힐리어와 같이 형태론적 특징이 다른 세 가지 언어에 적용한 결과, 세 개의 형태소 변화 시스템이 철자 및 음운론적 자료를 통해 다른 일반화 전략을 사용한다는 증거를 발견하였다.
    3. 이러한 조사 방법을 통해 유형별형태현 시스템과 특징 집합에 대한 언어별 일반화 전략의 차이를 밝힘으로써, 형태소 변화에 대한 언어 간 컴퓨터 모델링 연구의 발전에 기여할 수 있다.

###### AMR Parsing with Causal Hierarchical Attention and Pointers (https://aclanthology.org/2023.emnlp-main.553/)
- Anthology ID: 2023.emnlp-main.553 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 번역 기반의 AMR 파서가 그들의 간단함과 효과적인 성능으로 인해 인기를 얻고 있다. 그러나 이러한 간단함은 AMR 그래프의 구조적 지역성을 무시하고, 상호 참조를 나타내기 위해 불필요한 토큰을 도입하는 단점을 갖고 있다.
    2. 본 논문에서는 AMR 파싱의 새로운 목표 형태와 CHAP라는 새로운 모델을 소개하며, 인과적인 계층적 어텐션과 포인터 메커니즘을 갖춘 CHAP를 Transformer 디코더에 구조를 통합할 수 있도록 설계되었다.
    3. 실험 결과, 추가 데이터 없이 수행한 실험에서 기준 모델보다 우수한 성능을 보여주었다.

###### FLatS: Principled Out-of-Distribution Detection with Feature-Based Likelihood Ratio Score (https://aclanthology.org/2023.emnlp-main.554/)
- Anthology ID: 2023.emnlp-main.554 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 응용에서 NLP 모델이 OOD (out-of-distribution) 인스턴스를 감지하는 것은 중요하다.
    2. 기존의 OOD 감지 방법은 많지만 대부분 경험적이다고 주장하며, 이 논문에서는 OOD-ness를 측정하기 위해 외부 분포 \mathcal Pout 와 내부 분포 \mathcal Pin 간의 likelihood ratio를 사용한다.
    3. FLATS는 likelihood ratio를 기반으로 한 OOD 감지를 위한 원칙적인 해결책으로, pout(x) 추정을 통해 다른 OOD 감지 방법을 향상시킬 수 있다는 것을 실험으로 보였다.

###### Self-Evolution Learning for Mixup: Enhance Data Augmentation on Few-Shot Text Classification Tasks (https://aclanthology.org/2023.emnlp-main.555/)
- Anthology ID: 2023.emnlp-main.555 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 분류 작업에서는 라벨링 된 데이터가 한정되어있는 few-shot 시나리오를 자주 만나며, 데이터 부족 문제를 해결하는 것이 중요하다. 
    2. 이 논문에서는 텍스트 분류에서 데이터 augmentation을 위해 적응적이고 모델 친화적인 pseudo 샘플을 생성할 수 있는 self-evolution learning (SE) 기반의 mixup 접근 방식을 제안한다. 
    3. 실험 결과, SE가 다양한 mixup 방법에 일관되고 큰 향상을 가져옴을 보여주었고 딥한 분석을 통해 SE가 모델의 일반화 능력을 향상시킨다는 것을 입증하였다.

###### IC3: Image Captioning by Committee Consensus (https://aclanthology.org/2023.emnlp-main.556/)
- Anthology ID: 2023.emnlp-main.556 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이미지 캡셔닝 모델들은 보통 하나의 "가장 좋은" 이미지 캡션을 생성하도록 훈련되지만, 이는 캡션에서 가능한 세부 정보의 일부만에 초점을 맞추고 다른 유용한 정보를 무시하게 만든다. 
    2. 이 논문에서는 "IC3"라는 새로운 방법론을 소개하여 여러 주석 작성자의 시각에서 고수준의 세부 정보를 포착하는 단일 캡션을 생성한다. 
    3. 실험 결과, IC3로 생성된 캡션은 기준 모델을 사용한 캡션보다 더욱 도움이 되는 것으로 판명되었고, IC3는 최고 수준의 자동 추출 시스템의 성능을 최대 84% 향상시킬 수 있었다.

###### SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models (https://aclanthology.org/2023.emnlp-main.557/)
- Anthology ID: 2023.emnlp-main.557 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 언어 생성 모델인 GPT-3와 같은 LLM은 다양한 유저 입력에 대해 매우 유창한 답변을 생성할 수 있지만, 거짓된 사실과 비현실적인 주장을 할 수 있어 신뢰성을 떨어뜨릴 수 있다.
    2. 본 논문에서는 외부 데이터베이스 없이 검증 모듈을 통해 black-box 모델의 답변을 사실 여부로 확인할 수 있는 "SelfCheckGPT"를 제안한다.
    3. 실험 결과, SelfCheckGPT는 비현실적인 문장과 사실적인 문장을 감지하고 사실성을 평가하는데 있어 다른 방법들보다 더 높은 성능을 보여주었다.

###### Fair Without Leveling Down: A New Intersectional Fairness Definition (https://aclanthology.org/2023.emnlp-main.558/)
- Anthology ID: 2023.emnlp-main.558 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 교차하는 민감한 그룹이 존재하는 분류(setting)에서 intersectional group fairness 문제를 고려한다. 기존의 공정성 척도들의 단점을 보여주고, 절대적 및 상대적인 성능을 결합하는 새로운 정의인 𝛼-Intersectional Fairness를 제안한다.
    2. 이 새로운 정의는 differential fairness 개념의 일반화로 볼 수 있으며, 제안된 정의의 여러 가지 바람직한 특성과 다른 공정성 척도들과의 관계를 분석한다.
    3. 이 논문에서 제안된 정의를 사용하여 여러 인기있는 fair machine learning 접근 방식들을 벤치마크하고, 간단한 기준표에 비해 어떠한 개선도 이루어지지 않음을 보여준다. 결과는 이전 정의로 측정된 공정성의 증가가 "하향 조정" 효과를 숨기고 있다고 밝혀진다. 즉, 가장 우수한 그룹의 성능이 저하됨으로써 최악의 성능을 개선하지 못한다.

###### Revisiting Instruction Fine-tuned Model Evaluation to Guide Industrial Applications (https://aclanthology.org/2023.emnlp-main.559/)
- Anthology ID: 2023.emnlp-main.559 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Instruction Fine-Tuning (IFT)은 대규모 언어 모델(LLM)의 zero-shot 능력을 강화하는 강력한 패러다임이지만, 이로 인해 새로운 평가 메트릭의 요구사항이 발생한다. 
    2. 우리는 LLM 기반 메트릭이 이러한 요구 사항에 잘 적응되는 것을 보여주고, 실제 산업 환경에서 나타나는 task-specialization 전략의 trade-off를 정량화하기 위해 이를 활용한다. 
    3. 우리의 연구 결과는 실제 IFT 모델 배포에 대한 실용적인 통찰력을 제공한다.

###### CLAD-ST: Contrastive Learning with Adversarial Data for Robust Speech Translation (https://aclanthology.org/2023.emnlp-main.560/)
- Anthology ID: 2023.emnlp-main.560 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "레이블되지 않은 텍스트를 기반으로 훈련된 MT 모델은 소음이 섞인 ASR 출력을 번역할 때 강건성이 부족하여 전반적으로 번역 품질이 저하된다. 우리는 대상 언어의 깨끗한 버전에 노이즈 입력의 표현을 근접시킴으로써 하향식 MT 모델의 강건성 문제를 해결한다."
    2. "이를 위해 대립적인 예제를 활용하여 ASR 출력과 해당 인간 트랜스크립트를 짝지은 대입적인 학습 방법을 도입하여 네트워크 파라미터를 최적화한다."
    3. "또한, MT 로그-우도 손실과 대입적 손실을 교대로 사용하여 훈련을 안정화시키는 교육 전략을 도입한다. 이 방법은 깨끗한 텍스트의 번역 품질에 영향을 주지 않으면서 영어-독일어 및 영어-프랑스어 음성 번역에서 최대 3 BLEU 점수의 상당한 향상을 이끌어냈다."

###### M2DF: Multi-grained Multi-curriculum Denoising Framework for Multimodal Aspect-based Sentiment Analysis (https://aclanthology.org/2023.emnlp-main.561/)
- Anthology ID: 2023.emnlp-main.561 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에 주목받은 MABSA (Multimodal Aspect-based Sentiment Analysis)는 세밀한 Sentiment Analysis 작업인데 기존의 연구들은 주로 이미지 정보를 활용하여 성능을 향상시키려고 하지만, 데이터셋에는 텍스트와 관련이 없는 많은 노이즈 이미지들이 있어 모델 학습에 부정적인 영향을 줄 수 있다고 한다.
    2. 이 논문은 데이터를 수정하지 않고 노이즈 이미지의 부정적인 영향을 감소시킬 수 있는 방법을 연구한다. 
    3. Curriculum Learning의 아이디어를 활용하여, 데이터의 순서를 조정함으로써 노이즈 제거를 실현하는 M2DF (Multi-grained Multi-curriculum Denoising Framework)를 제안하였고, 실험적인 결과에서 이 프레임워크가 MABSA 의 세 가지 서브 태스크에서 최신 연구들을 일관되게 능가한다고 보여졌다.

###### Detection of Multiple Mental Disorders from Social Media with Two-Stream Psychiatric Experts (https://aclanthology.org/2023.emnlp-main.562/)
- Anthology ID: 2023.emnlp-main.562 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 "Mental Disease Detection (MDD)" 연구는 하나의 장애만을 감지하는 것에 초점을 두고 있어, 병이 동시에 발생할 수 있는 것을 간과하고 있다. 
    2. 우리는 모든 병의 공통된 단서를 학습하면서도 각각의 병마다 특정성을 포착하는 MDD 프레임워크를 제안한다.
    3. 텍스트와 증상 기능을 동시에 처리하는 two-stream 아키텍처는 두 가지 모드의 강점을 결합하여 지식 기반의 설명력을 제공한다. 희귀 클래스에서 특히 10% 이상의 감지 성능을 향상시킬 수 있는 것으로 실험 결과를 보여준다.

###### Understanding the Role of Input Token Characters in Language Models: How Does Information Loss Affect Performance? (https://aclanthology.org/2023.emnlp-main.563/)
- Anthology ID: 2023.emnlp-main.563 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Pre-trained language models (PLMs)가 언어에 대해 어떤 것을 학습하는지 이해하는 것은 자연어처리에서 여전히 고민되고 있는 문제이다. 
    2. 이 논문에서는 입력 토큰 문자의 정보 손실이 PLMs의 성능에 미치는 영향을 연구하였는데, 단 하나의 문자만 사용하여 pre-training한 모델조차도 일반적인 NLU 벤치마크와 probing tasks에서 높은 성능을 유지하는 것을 발견하였다. 
    3. 예를 들어, 토큰의 첫 번째 문자만 사용하여 pre-training한 모델은 SuperGLUE와 GLUE 태스크에서 각각 전체 토큰 모델의 약 90%와 77%의 성능을 유지한다.

###### Improved Unsupervised Chinese Word Segmentation Using Pre-trained Knowledge and Pseudo-labeling Transfer (https://aclanthology.org/2023.emnlp-main.564/)
- Anthology ID: 2023.emnlp-main.564 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 미지도 중국어 단어 분할(UCWS)은 사전에 훈련된 언어 모델에서 언어학적 지식을 사용하여 parameter-free 접근 방식을 통해 진전을 이루었다. 그러나 이러한 접근 방식은 단어 분할을 수행하기 위해 사전에 훈련된 언어 모델을 여러 번 추론해야 하므로 훈련 시간이 증가하는 문제가 있다.
    2. 이 논문에서는 훈련 효율성을 유지하면서 UCWS 성능을 향상시키기 위한 새로운 방법을 제안한다.
    3. 실험 결과, 기존 접근 방식에 비해 훈련 시간을 크게 줄이며 8가지 UCWS 작업에서 최고 수준의 성능을 달성하는 것을 입증한다.

###### EasyQuant: An Efficient Data-free Quantization Algorithm for LLMs (https://aclanthology.org/2023.emnlp-main.565/)
- Anthology ID: 2023.emnlp-main.565 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 언어 모델의 크기가 커서 실제 적용에는 많은 제약이 있는데, 이 논문에서는 데이터에 독립적인 양자화 기법을 제안하여 일반화 성과를 보장한다.
    2. EasyQuant라는 훈련 없이 수행되는 가중치만을 양자화하는 알고리즘을 제안한다. 가중치와 양자화 범위의 outlier를 처리하여 양자화 오류를 줄인다.
    3. EasyQuant은 훈련 데이터에 의존하지 않으므로 양자화된 언어 모델의 일반화 성능을 안전하게 보장하며, 병렬로 구현된다는 장점이 있다. 이 논문은 데이터에 의존하지 않는 방식에서 거의 손실 없이 양자화를 수행한 첫 번째 연구이며, 데이터 의존적인 방법보다 10배 빠르게 실행할 수 있다.

###### Polar Ducks and Where to Find Them: Enhancing Entity Linking with Duck Typing and Polar Box Embeddings (https://aclanthology.org/2023.emnlp-main.566/)
- Anthology ID: 2023.emnlp-main.566 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. DUCK은 entity linking 기법 중에서도 밀집 검색(dense retrieval) 기반의 방법으로 효율성이 뛰어나지만, 임베딩 공간의 구조에 민감하기 때문에 생성 모델에 비해 한계가 있다. 이 논문에서는 DUCK이라는 접근 방식을 소개하며 entity의 구조적인 정보를 임베딩 공간에 주입하는 것을 제안한다.
    2. 우리는 프로그래밍 언어에서의 "덕 타이핑"을 영감으로 하여 entity의 유형을 그래프 상에서 다른 entity와의 관계에 기반하여 정의한다.
    3. 실험 결과, DUCK 방법은 표준 entity disambiguation 목표 검증에서 새로운 최고 성능을 달성하며, 다른 타입 감지 기법을 능가하고, 파라미터가 18배 더 많은 생성 모델과 같은 결과를 보여준다.

###### APrompt: Attention Prompt Tuning for Efficient Adaptation of Pre-trained Language Models (https://aclanthology.org/2023.emnlp-main.567/)
- Anthology ID: 2023.emnlp-main.567 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델의 계속적인 성장으로 인해 새로운 작업에 대해 세밀하게 튜닝하는 과정이 매우 매개변수 집약적이 되었다. 
    2. 우리는 APrompt라는 새로운 Attention Prompt 튜닝 방법을 제안하여 대규모 사전 훈련 언어 모델을 효과적이고 효율적으로 적응시킨다. 
    3. 실험 결과는 우리의 방법이 다양한 규모의 사전 훈련 모델에서 최신 기준 모델과 전체 튜닝 방법을 능가한다는 것을 일관되게 보여준다.

###### What’s “up” with vision-language models? Investigating their struggle with spatial reasoning (https://aclanthology.org/2023.emnlp-main.568/)
- Anthology ID: 2023.emnlp-main.568 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 vision-language 모델들은 강력하지만, 그들은 "오른쪽"과 "왼쪽" 등의 기본적인 공간 관계를 신뢰할 수 있는 방식으로 구분할 수 있을까? 
    2. 우리는 기존의 VQAv2와 같은 데이터셋보다 객체의 공간적인 관계를 더 정확하게 분리하여 모델의 공간적인 추론 능력을 수치화하기 위해 세 가지 새로운 corpus를 제작하였다.
    3. 우리는 18개의 VL 모델을 평가하였는데, 그 결과 모든 모델들이 성능이 낮았다. 따라서 우리는 이러한 놀라운 행동의 원인에 대해 연구하였으며, 향후 연구에 도움이 되고자 우리의 데이터와 코드를 공개하였다.

###### IBADR: an Iterative Bias-Aware Dataset Refinement Framework for Debiasing NLU models (https://aclanthology.org/2023.emnlp-main.569/)
- Anthology ID: 2023.emnlp-main.569 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 일반적으로 사용되는 NLU (자연어 이해) 모델의 편향 제거 방법은 수동 데이터 분석에 많이 의존하여 모든 잠재적인 편향된 특징을 전부 다룰 수 없다. 
    2. 본 논문에서는 IBADR이라는 반복적인 편향 인식 데이터셋 개선 프레임워크를 제안하여 편향을 사전에 정의하지 않고도 NLU 모델의 편향을 제거한다. 
    3. 실험 결과와 깊은 분석을 통해 IBADR이 기존의 데이터셋 개선 방법에 비해 우수한 성능을 보여주며 SOTA에 도달하면서 모델 중심적인 방법과 호환될 수 있음을 보여준다.

###### Learning Preference Model for LLMs via Automatic Preference Data Generation (https://aclanthology.org/2023.emnlp-main.570/)
- Anthology ID: 2023.emnlp-main.570 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최신의 대형 언어 모델은 호 hallunciantion, 고정관념(stereotype) 등과 같은 문제점들이 있으나, 그 성능을 향상시키기 위해서는 preference model을 학습하는 것이 중요하다. 
    2. 그러나 이러한 preference model의 학습은 인간에 의해 어노테이트된 데이터에 의존하므로 다양성과 확장성이 제한된다.
    3. 본 논문에서는 "자동 생성된" 데이터로부터 preference model을 학습하는 방법을 제안하며, 해당 방법은 자연어처리 모델이 동시에 인간의 선호도를 배우고 인간의 가치와 일치하는 방법을 가능케 한다는 것을 보여준다.

###### Multilingual k-Nearest-Neighbor Machine Translation (https://aclanthology.org/2023.emnlp-main.571/)
- Anthology ID: 2023.emnlp-main.571 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "k-nearest-neighbor 기계 번역은 캐시된 예제들의 데이터 스토어를 생성하여 기계 번역의 품질을 크게 향상시켰다. 그러나 이러한 향상은 고자원 언어 쌍에서만 가능하며, 저자원 언어에 대해서는 여전히 도전과제이다."
    2. "우리는 여러 언어의 표현을 하나의 데이터 스토어로 결합하여 이 문제를 해결한다. 실험 결과, 저자원 번역의 품질뿐만 아니라 고자원 번역의 품질을 상당히 향상시키는 것이 일관적으로 관찰되었다."
    3. "언어 간 유사성을 이용하여 데이터 스토어를 생성함으로써 크기가 1/4로 줄이고 5.3배의 속도 향상을 달성할 수 있다는 것을 실험을 통해 보여주었다."

###### Understanding Computational Models of Semantic Change: New Insights from the Speech Community (https://aclanthology.org/2023.emnlp-main.572/)
- Anthology ID: 2023.emnlp-main.572 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 현재의 언어 사용 커뮤니티를 언어적으로 묘사하는 널리 사용되는 의미 변화 모델의 서술적 타당성을 조사했다. 우리는 퀘벡 영어에서의 접촉 유발 의미 변화라는 사회언어학적 문제에 초점을 맞춰 모델을 검증하기 위해 타입 수준과 토큰 수준의 워드 임베딩, 실증적 언어적 특성, 모트리올에서 온 15명의 화자들의 수용 가능성 평가 및 질적 의견을 분석했다. 결과적으로, 전산적 접근 방식의 전반적인 타당성을 확인하였지만 다양한 의미 변화 추정량의 보완재적 성격과 실제적 문제점을 강조하였다. 알려진 바에 의하면, 이 연구는 의미 변화 모델을 사용하여 기술되는 언어 사용 커뮤니티와 실질적으로 관련짓는 첫 번째 연구이다.
    2. 우리는 컴퓨터적 접근 방식의 의미 변화 모델들이 현대의 언어 사용 커뮤니티의 언어적 특성을 제대로 설명하는지 조사했다. 퀘벡 영어에서 발생하는 접촉 유발 의미 변화에 초점을 맞추고, 40개의 대상 단어를 타입 수준과 토큰 수준의 워드 임베딩, 경험적 언어적 특성, 몬트리올에서 왔다는 15명의 화자들의 수용 가능성 평가 및 질적 의견을 분석했다. 결과는 전반적으로 컴퓨터적 접근 방식의 타당성을 확인하며, 다양한 의미 변화 추정량의 필요성과 실제적 문제를 강조한다.
    3. 우리는 현대의 언어 사용 커뮤니티의 언어적 특성을 설명하는 널리 사용되는 의미 변화 모델의 기술적 타당성을 조사했다. 우리는 퀘벡 영어의 사회언어학적 문제에서의 접촉으로 인한 의미 변화에 집중하고, 타입 수준과 토큰 수준의 워드 임베딩, 경험적 언어적 특성, 몬트리올에서 온 15명의 화자들의 수용 가능성 평가 및 질적 의견을 분석하였다. 결과는 컴퓨터적 접근 방식의 전반적인 타당성을 확인하면서도 다양한 의미 변화 추정량의 상호 보완재성과 실용적 문제를 강조한다.

###### Causal Reasoning through Two Cognition Layers for Improving Generalization in Visual Question Answering (https://aclanthology.org/2023.emnlp-main.573/)
- Anthology ID: 2023.emnlp-main.573 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 VQA(Vision Question Answering) 모델들은 단일 모달 (unimodal) 측면을 개선하는데 주력하고 있어서 학습 분포를 벗어난 문맥에서 이미지의 질문에 대답하는 능력이 제한적이다.
    2. 본 논문에서는 양방향 인과 추론을 강조하여 다중 모달 (multimodal) 예측을 개선하는 CopVQA라는 모델을 제안한다.
    3. CopVQA는 다양한 시각화 기법을 사용하여 다중 모달 예측을 개선하고, 인과 추론의 역할을 강조하여 VQA의 성능과 일반화 능력을 향상시킨다. 또한, 모델 크기의 1/4로 경량화한 상태에서 PathVQA 데이터셋에서 우수한 정확도를 달성한다.

###### StructGPT: A General Framework for Large Language Model to Reason over Structured Data (https://aclanthology.org/2023.emnlp-main.574/)
- Anthology ID: 2023.emnlp-main.574 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 대형 언어 모델 (LLM)이 구조화된 데이터에 대해 추론 능력을 통합적으로 개선하기 위한 것이다.
    2. StructGPT라고 불리는 IRR (Iterative Reading-then-Reasoning) 프레임워크를 개발하여 구조화된 데이터를 기반으로하는 질문-답변 과제를 해결한다.
    3. 실험 결과, 구조화된 세 가지 유형의 데이터에서 StructGPT가 LLM의 성능을 크게 개선시켜주었다.

###### Modeling Legal Reasoning: LM Annotation at the Edge of Human Agreement (https://aclanthology.org/2023.emnlp-main.575/)
- Anthology ID: 2023.emnlp-main.575 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 일반적인 언어 생성 모델은 document class-prediction 태스크를 수행하기 위해 사용되는데, 현재까지의 연구들은 단순한 classification 태스크에 대해서만 검증을 진행하고 있다. 본 논문에서는 법적 추론을 포함한 매우 복잡한 태스크에 대한 LMs의 성능을 실험적으로 검증하였다.
    2. 총 8명의 법조계 전문가로 구성된 팀이 레이블링한 미국 연방 대법원 판례 데이터셋을 활용하여 다양한 LMs의 성능을 실험적으로 평가하였다.
    3. 실험 결과, 사람들에게 제시된 주어진 지시사항에 대해서 LMs의 성능이 낮게 나타났고, 잘 동작하는 모델은 LEGAL-BERT 모델과 같은 fine-tuning된 in-domain 모델이었다. 실험 결과는 법학 분야에서 generative LMs의 사용에 대해 주의를 요구하며, 인간 주석을 포함한 전통적인 분류 방법의 지속적인 중요성을 강조한다.

###### Model-tuning Via Prompts Makes NLP Models Adversarially Robust (https://aclanthology.org/2023.emnlp-main.576/)
- Anthology ID: 2023.emnlp-main.576 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 NLP 연구에서는 기존의 다음과 같은 절차를 따르는데, 미세조정된 언어 모델 위에 MLP (다층 퍼셉트론)을 올려 downstream 태스크에 사용하는데 이런 모델은 적은 대량 공격에도 취약하다.
    2. 그래서 본 논문에서는 MVP (Model-tuning Via Prompts)라는 알터너티브 방법을 제안하고, 실제로 이 방법이 공격 반대로 더 강한 방어력을 보인다는 것을 보였다. 
    3. MVP는 MLP 대신 입력에 prompt template을 추가하고 텍스트 채움/완성 방식을 통해 예측한다. MVP는 기존 방법에 비해 평균 8%의 성능 개선을 보여주었으며, adversarial training과 결합하면 더 큰 향상을 보이게 된다.

###### Learning Co-Speech Gesture for Multimodal Aphasia Type Detection (https://aclanthology.org/2023.emnlp-main.577/)
- Anthology ID: 2023.emnlp-main.577 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 뇌손상으로 발생하는 언어 장애인 실명-,와 전미크(aphasia)와 같은 특정한 aphasia 유형을 정확하게 식별하는 것은 효과적인 치료를 위해 중요한데, 이를 감지하기 위한 방법 개발에는 미비한 점이 있다.
    2. 이 연구에서는 동시에 발생하는 손동작(co-speech gestures)을 분석할 때의 식별력을 갖는 화제 정보를 생성하는 다중 모달 그래프 신경망을 제안한다.
    3. 실험 결과 gesture 기능이 acoustics 기능보다 우수함을 보여주었으며, 기존 방법에 비해 우수한 성능 (F1 84.2%)을 달성했다.

###### STINMatch: Semi-Supervised Semantic-Topological Iteration Network for Financial Risk Detection via News Label Diffusion (https://aclanthology.org/2023.emnlp-main.578/)
- Anthology ID: 2023.emnlp-main.578 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 상용 뉴스는 자동 금융 위험 감지에 풍부한 의미론적 내용과 적시성 있는 정보를 제공하지만, 비싼 대규모 주석과 훈련 데이터의 희박함으로 인해 상용 뉴스의 전체적인 활용에 제약이 있다.
    2. 논문에서는 상용 뉴스-기업 지식 그래프(NEKG)와 함께 반지도 학습 기법인 STINMatch를 제안하여 위험 감지 향상을 강화한다. 
    3. 제안된 모델은 레이블 상관 행렬과 상호 일관성 규제 기술을 텍스트와 그래프 모듈의 반복 학습 프레임워크에 통합하여 레이블 확산 및 위상 구조를 따르는 문서 수준 의미론과 레이블 상관 관계 간의 깊은 상호 작용을 가능하게 한다.

###### Centering the Margins: Outlier-Based Identification of Harmed Populations in Toxicity Detection (https://aclanthology.org/2023.emnlp-main.579/)
- Anthology ID: 2023.emnlp-main.579 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 AI 모델 평가 방법은 특정 인구 하위 그룹 간의 성능 차이를 찾아보는 것인데, 이는 취약한 그룹을 중심으로 하지만, 교차하는 부분 그룹이나 여러 그룹 간에 공유되는 피해의 패턴을 감추는 위험이 있다.
    2. 이 논문에서는 장애 연구와 관련 학문의 틀을 활용하여 가장자리 (margins)에 초점을 맞추어 독성 탐지 도메인에서 "가장자리"를 구현한다.
    3. 이 연구 결과, 인구 통계 아웃라이어의 경우 모델 성능이 일관되게 나빠지며, 텍스트 아웃라이어 또한 예외값에 비해 성능이 더 나쁘다는 것을 발견하였다. 따라서 예외 분석은 더 크고 다양한 교차 그룹에서 겪는 피해를 발견하는 데 특히 유익하다.

###### Describe Me an Auklet: Generating Grounded Perceptual Category Descriptions (https://aclanthology.org/2023.emnlp-main.580/)
- Anthology ID: 2023.emnlp-main.580 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인간 화자는 인스턴스 수준에서 추상화된 지각적 개념에 대한 설명을 생성할 수 있다. 추가로, 이러한 설명은 다른 화자들이 해당 개념의 임시 표현을 배우는 데 사용될 수 있다.
    2. 본 논문에서는 다중 모달 언어 모델에서 범주 수준의 지각적 Grounding을 테스트하기 위한 프레임워크를 소개한다.
    3. 설명 모델의 성능 문제를 인식하고, 이러한 문제가 범주 수준에서 언어를 적절하게 구체화하지 못함에 기인한다는 주장을 한다.

###### Revisiting Automated Topic Model Evaluation with Large Language Models (https://aclanthology.org/2023.emnlp-main.581/)
- Anthology ID: 2023.emnlp-main.581 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 토픽 모델은 대용량의 텍스트 컬렉션을 이해하는 데 도움을 준다. 그러나 그 출력을 자동으로 평가하고 최적의 토픽 수를 결정하는 것은 오랜 동안의 과제이며, 현재까지 효과적인 자동화된 해결책이 없다. 이 논문은 이러한 작업에 대해 대형 언어 모델(Large Language Models, LLMs)을 사용하는 것을 제안한다.
    2. LLMs는 기존의 자동 메트릭보다 더 강한 인간 판단과 잘 상관되는 토픽을 적절하게 평가한다. 그러나 평가 작업의 설정은 중요한데, LLMs는 단어 세트의 일관성 평가에서는 더 좋은 성능을 보이고 intrusion detection에서는 성능이 떨어진다.
    3. 또한, LLMs는 합리적인 토픽 수를 결정하는 데 도움이 될 수 있다. 연구 질문을 LLM의 프롬프트에 통합시켜 사용하면 최적의 토픽 수를 추정하는 데 도움이 된다.

###### ORCHID: A Chinese Debate Corpus for Target-Independent Stance Detection and Argumentative Dialogue Summarization (https://aclanthology.org/2023.emnlp-main.582/)
- Anthology ID: 2023.emnlp-main.582 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 에이전트는 몇 년 동안 계속해서 주목받고 있으며, 최근의 대형 언어 모델 (LLM)의 진전으로 인해 이러한 트렌드가 더욱 촉진되었다. 
    2. 대립 감지 (stance detection)와 대화 요약 (dialogue summarization)은 논쟁적인 대화를 포함하는 응용 시나리오에서 대화 에이전트의 핵심 작업 두 가지이다. 
    3. 중국어의 언어 자료 부족으로 인해 이러한 작업에 대한 연구가 제한되어 있다. 이 문제를 해결하기 위해 우리는 첫 번째 중국어 데이터 집합인 ORCHID (Oral Chinese Debate)를 제안한다.

###### On the Benefits of Learning to Route in Mixture-of-Experts Models (https://aclanthology.org/2023.emnlp-main.583/)
- Anthology ID: 2023.emnlp-main.583 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Switch Transformer"와 같은 MoE (Mixture-of-Expert) Transformer 모델은 모델 크기를 확장하면서 계산 시간을 일정하게 유지하는 데 성공했다. 
    2. 우리는 이러한 모델의 핵심 요소인 라우터가 토큰을 똑똑하게 라우팅하는 능력이 MoE 모델에 상당한 이점을 제공한다는 이론적 및 경험적 증거를 제시한다. 
    3. 실제 데이터에 대한 실험에서도 학습 가능한 라우터가 비학습 가능한 라우터보다 상당한 이점을 제공함을 관찰했다.

###### SEAHORSE: A Multilingual, Multifaceted Dataset for Summarization Evaluation (https://aclanthology.org/2023.emnlp-main.584/)
- Anthology ID: 2023.emnlp-main.584 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 요약 시스템의 신뢰할 수 있는 자동평가는 다면적이고 주관적인 특성 때문에 어렵다. 특히 영어 외의 언어에서는 인간평가 데이터가 부족하여 어려움이 있다.
    2. 이 연구는 다국어이고 다면적인 요약 평가를 위한 데이터셋 SEAHORSE를 소개한다. SEAHORSE에는 6개의 언어, 9개의 시스템, 4개의 데이터셋을 포함한 96,000개의 요약과 인간평가 결과가 있으며, 텍스트 품질의 6가지 측면(comprehensibility, repetition, grammar, attribution, main ideas, conciseness)으로 평가된다.
    3. SEAHORSE를 활용하여 학습된 메트릭은 여러 도메인에서 좋은 성능을 달성하였으며, 이 데이터셋과 메트릭은 다국어 및 다면적 요약 평가에 대한 향후 연구를 위해 공개되었다.

###### Query2doc: Query Expansion with Large Language Models (https://aclanthology.org/2023.emnlp-main.585/)
- Anthology ID: 2023.emnlp-main.585 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "query2doc"는 희소하고 밀집한 정보 검색 시스템의 성능을 향상시키기 위한 간단하면서도 효과적인 쿼리 확장 접근 방법을 제안한다.
    2. 제안된 방법은 큰 언어 모델 (LLM)을 활용하여 의사문서를 생성한 다음, 생성된 의사문서를 사용하여 쿼리를 확장한다.
    3. 실험 결과, query2doc은 모델 파인튜닝 없이도 BM25의 성능을 3%에서 15% 향상시키며, 상위 성능 검색기에도 도메인 내 및 도메인 외 결과에 이점을 제공한다.

###### We Need to Talk About Reproducibility in NLP Model Comparison (https://aclanthology.org/2023.emnlp-main.586/)
- Anthology ID: 2023.emnlp-main.586 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 NLP 태스크의 여러 모델을 비교할 때 NLP 연구자들은 자주 재현성 문제를 마주하게 된다. 많은 연구들에서 표준 데이터 분할은 재현 가능하고 신뢰할 수 없는 결론을 도출하게 되는 문제가 있으며, 이를 해결하기 위해 더 랜덤한 반복을 사용하는 방법도 시도되었다.
    2. 그러나 NLP 모델 간의 비교에서 재현성의 개선은 데이터 분할 전략에 의해 발생하는 추정기와 재현성의 관계에 대한 조사의 부족으로 제한되어 있다.
    3. 이 연구에서는 모델의 비교에서 재현성을 결론에 관한 확률적 함수로 정의하고, 재현성이 모델 성능 추정기의 신호 대 잡음 비율에 의해 정성적으로 지배된다는 것을 이론적으로 설명한다. 따라서 제안된 방법을 사용하여 NLP 모델을 비교하는 것을 권장한다.

###### Explore-Instruct: Enhancing Domain-Specific Instruction Coverage through Active Exploration (https://aclanthology.org/2023.emnlp-main.587/)
- Anthology ID: 2023.emnlp-main.587 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Instruction-tuning은 다양성을 개선함으로써 크기가 더 작은 작업 스펙트럼을 다룰 수 있는 모델을 만들 수 있지만, 기존 데이터는 개별 도메인의 불 충분한 커버리지로 인해 세부적인 이해와 상호작용이 제한된다. 따라서 우리는 Explore-Instruct라는 새로운 접근법을 제안하여 Large Language Models (LLMs)를 통해 도메인별 instruction-tuning 데이터의 커버리지를 향상시키는 활동적 탐색을 실시한다."
    2. "Explore-Instruct은 대표적인 도메인 사용 사례 위에 구축되었으며, 탐색 알고리즘을 이용하여 다양하고 도메인 중심적인 instruction-tuning 데이터를 얻는다."
    3. "우리의 결과는 도메인 별 커버리지를 개선하는 이 접근법의 효과를 검증하고, 도메인별 데이터를 사용하는 기존의 베이스라인을 포함한 여러 곳에서 상당한 발전을 이루었다는 것을 보여준다."

###### Practical Computational Power of Linear Transformers and Their Recurrent and Self-Referential Extensions (https://aclanthology.org/2023.emnlp-main.588/)
- Anthology ID: 2023.emnlp-main.588 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. RNN 아키텍처의 계층 구조를 고려한 연구에서, 선형화된 어텐션을 사용하는 자동회귀 Transformer인 LTs는 RNN과 동등한 기능을 하면서도 self-attention 네트워크로 표현될 수 있다는 것을 밝혔다.
    2. 표준 Transformer에 관한 잘 알려진 결과들이 LTs/FWPs에도 그대로 적용될 수 있다는 것을 보였다.
    3. 자세한 실험을 통해 재귀적인 FWPs와 자기 참조 가중치 행렬과 같은 최근의 FWP 확장이 LT의 특정한 제한을 극복하고, 예를들어 Parity 문제에서 일반화를 가능하게 한다는 것을 보였다.

###### InterFair: Debiasing with Natural Language Feedback for Fair Interpretable Predictions (https://aclanthology.org/2023.emnlp-main.589/)
- Anthology ID: 2023.emnlp-main.589 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP 모델에서의 디바이스(bias) 제거 방법은 기존에는 민감한 속성 (예: 성별 또는 인종)과 관련된 정보를 제거하는 데 초점을 맞췄다. 
    2. 우리는 대신 이러한 민감한 정보를 피해하는 대신 설명과 함께 "공정하게" 사용해야 한다고 주장한다. 
    3. 두 가지 상호작용 설정에서 우리는 사용자의 피드백을 통해 작업 성능과 편향 완화 간에 더 나은 공정한 균형을 달성할 수 있다는 것을 보여주었다.

###### Just Adjust One Prompt: Enhancing In-Context Dialogue Scoring via Constructing the Optimal Subgraph of Demonstrations and Prompts (https://aclanthology.org/2023.emnlp-main.590/)
- Anthology ID: 2023.emnlp-main.590 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현대 대형 언어 모델(Large Language Models, LLMs)을 챗봇으로 사용하는 것은 환영, 공감 부족 등의 문제를 가지고 있다. 이러한 문제를 식별하는 것은 챗봇의 성능 향상에 도움이 된다.
    2. 기존 LLM 기반의 metric은 특정 데이터셋을 선택하고 각각의 evaluation dimension(일관성, 정보성 등)에 맞는 훈련 작업을 개발하는 것을 요구한다. 이는 시간이 많이 소요되며 새로운 evaluation dimension에 대해 반복적으로 수행되어야 할 수도 있다.
    3. 우리는 대화 평가의 다양한 요구 사항에 효율적이고 유연하게 적응할 수 있는 차원에 구애받지 않는 점수 매기는 방법을 제안한다. 우리의 방법은 LLM의 in-context learning(ICL) 능력을 최대한 활용하여 인간의 평가 결과로부터 학습한다.

###### Multilingual estimation of political-party positioning: From label aggregation to long-input Transformers (https://aclanthology.org/2023.emnlp-main.591/)
- Anthology ID: 2023.emnlp-main.591 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Scaling analysis는 정치적 주체(예: 정치인 또는 정당)에 대해 (일반적으로 긴) 텍스트 집합(예: 국회 연설 또는 선거 선언문)을 기반으로 정의된 척도에 따라 점수를 매기는 컴퓨터 정치학 기술이다. 
    2. 이 연구에서는 정당 선언문에 대한 자동 스케일링 분석의 두 가지 접근 방식인 라벨 집계와 원시 텍스트에서 직접 스케일링 값을 계산하는 Transformer 기반 모델을 구현하고 비교한다. 
    3. 41개 국가와 27개 언어에 걸친 Comparative Manifestos Project 데이터셋의 분석 결과, 최신 모델을 통해 효율적으로 처리할 수 있으며, 라벨 집계가 가장 좋은 결과를 도출한다.

###### ART: rule bAsed futuRe-inference deducTion (https://aclanthology.org/2023.emnlp-main.592/)
- Anthology ID: 2023.emnlp-main.592 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 추론 기반 미래 이벤트 결론 도출을 위해 시각적 현상(비디오)과 규칙 기반 전제를 기반으로 올바른 미래 이벤트를 결론 짓는 ART (rule bAsed futuRe-inference deducTion)를 제안한다.
    2. 다양한 원격 감지 공용 지식을 활용하여 ARTNet을 개발하였고, ARTNet은 대상 비디오 캐릭터를 식별하고 미래 이벤트와 관련된 시각적 단서를 인지하는 방식으로 작동한다. 
    3. 실험적 연구를 통해 시각적 관찰을 통한 타당한 추론에 대한 ARTNet의 합리성과 기존 방법에 대한 효과성을 검증하였다.

###### EpiK-Eval: Evaluation for Language Models as Epistemic Models (https://aclanthology.org/2023.emnlp-main.593/)
- Anthology ID: 2023.emnlp-main.593 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인공지능 시대에서는 대형 언어 모델의 역할이 점점 중요해지고 있다. 그러나 이러한 모델들이 다양한 학습 문서로부터 지식을 효과적으로 통합하는 능력은 아직 탐구되지 않았다.
    2. 본 논문에서는 LLMs의 이러한 정보 통합 능력을 조사한 최초의 연구를 제시한다. 이를 위해 LLMs의 능력을 평가하기 위한 새로운 질문-답변 벤치마크인 EpiK-Eval을 도입했다.
    3. 다양한 LLMs에 대한 평가 결과, 이 영역에서 상당한 약점이 드러났다. 불충분한 학습 목표의 본질에 기인한 것으로 보인다. 그 결과, 지식 통합을 개선하기 위한 방법을 추진하여 LLMs의 전반적인 효과성과 성능을 대폭 향상시킬 수 있다고 주장한다.

###### From Dissonance to Insights: Dissecting Disagreements in Rationale Construction for Case Outcome Classification (https://aclanthology.org/2023.emnlp-main.594/)
- Anthology ID: 2023.emnlp-main.594 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 법적 NLP에서의 Case Outcome Classification(COC)은 정확성 뿐만 아니라 신뢰성과 설명 가능성도 갖추어야 한다. 기존의 설명 가능한 COC 연구는 단일 전문가의 주석에 한정되어 있다.
    2. 이 논문에서는 국제 인권법 분야에서의 두 전문가의 약한 합의를 바탕으로한 새로운 데이터셋 RaVE를 수집하여 그들의 분쟁을 연구하고, COC특수 부분 범주를 보완하는 데 사용된다.
    3. 이 연구는 법적 NLP에서 사례의 사실과 관련된 측면을 식별하는 것을 중심으로하는 벤치마크 데이터셋을 작성하는 데 있어서 간과된 복잡성을 밝히고 있다.

###### On Bilingual Lexicon Induction with Large Language Models (https://aclanthology.org/2023.emnlp-main.595/)
- Anthology ID: 2023.emnlp-main.595 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 NLP의 핵심 과제인 BLI(Bilingual Lexicon Induction)는 아직 크로스-언어 단어 표현 계산에 의존하고 있는데, 이 논문에서는 최신 세대의 큰 언어 모델 (LLM)이 이를 보완할 수 있는 잠재력을 검토하고 있다.  
    2. 이 논문은 multilingual LLM(mLLM)에 대해 제공과 세밀한 조정(fine-tune)을 통해 BLI를 수행할 수 있는지 그 방법과, 기존의 접근 방식과 어떻게 구분될 수 있는지 연구하고 있다. 
    3. 연구 결과는 mLLM에 대한 zero-shot prompting, few-shot in-context prompting, 그리고 표준적인 BLI에 특화된 fine-tuning의 성능을 실험적으로 검증하여, mLLM이 강력한 BLI 능력을 보여주고 있다는 것을 보여준다.

###### Statistical Depth for Ranking and Characterizing Transformer-Based Text Embeddings (https://aclanthology.org/2023.emnlp-main.596/)
- Anthology ID: 2023.emnlp-main.596 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer 기반 텍스트 임베딩의 인기로 인해 이러한 임베딩의 분포를 측정하기 위한 통계 도구가 필요하다. 따라서 본 논문에서는 문장을 중심으로 한 텍스트 임베딩 (TTE) depth를 측정하기 위한 통계적 방법과 이를 자연어처리 파이프라인에서 모델링과 분포적 추론에 활용하는 방법을 제안한다. 
    2. 우선 TTE depth와 관련된 rank sum test를 정의하고, 두 개의 말뭉치가 임베딩 공간에서 유의미하게 다른지 여부를 확인하기 위해 사용한다. 
    3. 그리고 TTE depth와 해당 rank sum test를 사용하여 합성된 데이터와 인간이 생성한 데이터 간의 분포 차이를 측정하여 최근의 합성 데이터 증강 방법이 인간이 생성한 텍스트와 유의미한 분포 변화를 일으키는 것을 보여준다.

###### CRaSh: Clustering, Removing, and Sharing Enhance Fine-tuning without Full Large Language Model (https://aclanthology.org/2023.emnlp-main.597/)
- Anthology ID: 2023.emnlp-main.597 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 대규모 언어 모델의 일반화 능력 향상을 위해 인스트럭션 튜닝이 효과적으로 인식되었으나, 공개적으로 접근 가능한 중앙 언어 모델을 개인적인 인스트럭션 데이터로 튜닝하는 경우, 개인 정보 보호 문제가 필연적이다.
    2. 이 논문은 Offsite-Tuning (OFT)에 초점을 맞추고, centralized LLMs와 downstream emulators 사이에서 transformer 블록을 전송하는 대표적인 기술이다. 
    3. 연구 결과, LLM의 레이어에서 독특한 모듈 구조가 나타나며, 튜닝과 중간 예측 사이에서 미묘하지만 중요한 표현에 변화가 있다는 사실을 밝혀냈다. 이를 바탕으로 CRaSh를 제안하여 OFT의 성능을 대폭 향상시켰다.

###### From Multilingual Complexity to Emotional Clarity: Leveraging Commonsense to Unveil Emotions in Code-Mixed Dialogues (https://aclanthology.org/2023.emnlp-main.598/)
- Anthology ID: 2023.emnlp-main.598 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 중 감정을 이해하는 것은 인간의 소통에서 중요한 요소로, Emotion Recognition in Conversation(ERC)을 위한 NLP 연구를 촉발시킨다. 이 연구의 동기는 언어 혼용 대화에서의 감정적인 다이내믹스를 이해하는 것이 상대적으로 덜 연구되었다는 것이다.
    2. 우리는 감정적 지능이 세상적인 지식을 포함하는 것이라고 인식하며, 단순한 정보를 대화의 맥락과 통합해 감정을 깊게 이해할 수 있는 혁신적인 접근법을 제안한다.
    3. 우리의 실험 결과는 상식을 ERC에 체계적으로 통합함으로써 상당한 성능 향상을 얻을 수 있음을 보여주며, 양적 평가와 질적 분석은 우리의 가설의 타당성을 뒷받침하며, ERC에서의 상식 통합의 중요성을 또한 확인한다.

###### Large Language Models are biased to overestimate profoundness (https://aclanthology.org/2023.emnlp-main.599/)
- Anthology ID: 2023.emnlp-main.599 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. GPT-4와 다른 LLMs(대형 언어 모델)에 대한 연구에서, 일상적인, 동기 부여, 의사 강조한 문장의 심오성을 판단하는 능력을 인공지능 모델들이 인간과 유사한 추론 능력을 가졌는지 여부가 논쟁 중이다.
    2. 모든 유형의 문장과 유형에 상관없는 확인기법을 사용하여 LLMs와 사람들 간에 문장 간의 상관관계가 있었다는 것을 발견했다.
    3. 그러나, LLMs는 비문 같은 문장의 심오함을 과장 평가했으며, Tk-instruct는 문장의 심오함을 예외적으로 과소평가했다. 몇 가지 샷 학습 방법은 LLMs 평가를 사람들과 가깝게 만들었다. 또한, RLHF로 인한 잠재적인 편향에 대한 통찰력을 제공하며, 이는 문장의 심오함을 과장 평가하는 편향 증가를 유발한다.

