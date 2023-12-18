# Korean Three-Line Summarizations of Papers 2187-2247 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### Cache me if you Can: an Online Cost-aware Teacher-Student framework to Reduce the Calls to Large Language Models (https://aclanthology.org/2023.findings-emnlp.1000/)
- Anthology ID: 2023.findings-emnlp.1000 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소규모 및 중소기업들은 큰 규모의 훈련 데이터셋을 만들거나 큰 규모의 언어 모델을 사전 훈련하는 비용을 감당할 수 없기 때문에 LLM을 사용해야 하는데, 현재 이러한 서비스는 호출당 결제해야 하는 형태로 운영 비용이 많이 든다.
    2. 또한, 고객의 입력내용은 시간이 지나도 매우 유사한 경우가 많아 LLM에게 유사한 입력을 반복해서 요청하는 문제가 있다.
    3. 이 논문에서는 이러한 문제를 해결하기 위해 이전 LLM의 응답을 캐시화하고 이를 사용하여 SME 측에서 저렴한 지역 모델을 훈련시키는 방법을 제안한다. 실험 결과, 약간의 성능 저하와 함께 상당한 운영 비용 절감이 가능함을 보여준다.

###### ParroT: Translating during Chat using Large Language Models tuned with Human Translation and Feedback (https://aclanthology.org/2023.findings-emnlp.1001/)
- Anthology ID: 2023.findings-emnlp.1001 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT와 같은 대형 언어 모델은 다양한 기계 번역 역량을 보여주지만, 이러한 모델은 제한된 API를 통해서만 접근 가능하고 이는 연구 및 발전에 제한을 가한다. 
    2. 따라서, 우리는 ParroT이라는 프레임워크를 제안하는데, 이는 오픈 소스 언어 모델 (예 : LLaMA), 인간이 작성한 번역 및 피드백 데이터를 기반으로 채팅 중 번역 능력을 향상시키고 규제하는 것을 목표로 한다.
    3. 번역 지시, 대조 지시 및 오류 안내 지시와 같은 세 가지 지시 유형을 활용하여 ParroT 모델을 finetuning하는 방법을 제안하며, 실험결과 번역 지시는 기본 LLM의 번역 성능을 크게 개선하고, 오류 안내 지시는 더 나은 결과를 이끌 수 있다는 것을 보여준다.

###### Dense Retrieval as Indirect Supervision for Large-space Decision Making (https://aclanthology.org/2023.findings-emnlp.1002/)
- Anthology ID: 2023.findings-emnlp.1002 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대부분의 NLU 태스크는 많은 라벨을 가지고 있는데, training instance 당 라벨이 부족하고 다양한 세부 라벨 중에서 선택하는 것이 어렵기 때문에, 이러한 큰 라벨 공간에서의 결정을 학습하는 것은 특히 어렵다. 
    2. 이 논문에서는 단지 로짓만 예측하는 것이 아니라, 학습 데이터에서 결정항목을 검색함으로써 큰 공간의 결정 문제를 학습하는 학습-검색 문제로 재구성하여, 더 의미 있는 대표적인 결정 공간 표현과 함께 예측 일반화를 향상시키는 해결책 DDR을 제안한다. 
    3. 라벨 크기가 수백에서 수십 만까지 변하는 태스크에서 NLU를 수행하여 평가한 결과, DDR은 기존의 강력한 베이스라인보다 높은 성능을 보인다.

###### One-Model-Connects-All: A Unified Graph Pre-Training Model for Online Community Modeling (https://aclanthology.org/2023.findings-emnlp.1003/)
- Anthology ID: 2023.findings-emnlp.1003 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "온라인 커뮤니티는 커뮤니티, 사용자, 사용자 생성 텍스트 콘텐츠로 구성되어 있으며 사회 문제 해결에 도움이 될 수 있는 다양한 정보를 가지고 있다. 이전 연구에서는 이 세 가지 구성 요소와 그들 사이의 관계를 완전히 활용하지 못했으며, 다양한 하위 작업에 대응할 수 없었다."
    2. "이 논문에서는 동시에 커뮤니티, 사용자 및 텍스트를 고려하는 프레임워크에 초점을 맞추고 있으며, 이는 소셜 미디어와 관련된 다양한 하위 작업과 쉽게 연결될 수 있다. 구체적으로, 우리는 온라인 커뮤니티를 모델링하기 위해 삼중 이질적 그래프를 사용한다."
    3. "텍스트 재구성과 엣지 생성을 통해 커뮤니티, 사용자, 텍스트 간의 구조적 및 의미적 지식을 학습한다. 미리 훈련된 이 모델을 활용하여 위반 감지, 감성 분석, 커뮤니티 추천과 같은 다양한 하위 작업에서 유망한 결과를 얻을 수 있다. 우리의 탐구는 온라인 커뮤니티 모델링을 개선할 것이다."

###### In-Image Neural Machine Translation with Segmented Pixel Sequence-to-Sequence Model (https://aclanthology.org/2023.findings-emnlp.1004/)
- Anthology ID: 2023.findings-emnlp.1004 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "In-Image Machine Translation (IIMT)"는 이미지에 있는 텍스트를 한 언어에서 다른 언어로 번역하는 것을 목표로 한다. 기존의 cascade 방법은 OCR을 이용한 후 NMT와 텍스트 렌더링을 순차적으로 사용했으나, 이 방법은 OCR과 NMT의 오차가 누적되어 번역 품질이 저하된다.
    2. 이 논문에서는 end-to-end 모델을 제안하여 OCR, NMT, 텍스트 렌더링 파이프라인 대신 사용한다. 이 모델은 segmented pixel sequences를 입력과 출력으로 사용하는 encoder-decoder 패러다임을 채택한다. 
    3. end-to-end 학습을 통해 우리의 모델은 오차 전파를 피하고 번역 품질을 높이는데 성공하며, 도메인 데이터에서의 강건성을 보여주고 불완전한 단어에 대해 둔감하다. 실험 결과, 우리의 방법은 cascade 방법과 현존하는 end-to-end 모델보다 우수한 성능을 보인다.

###### NarrativeXL: a Large-scale Dataset for Long-Term Memory Models (https://aclanthology.org/2023.findings-emnlp.1005/)
- Anthology ID: 2023.findings-emnlp.1005 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 GPT 3.5를 사용하여 Project Gutenberg의 1,500권의 소설에서 각 장면을 요약하고, 이를 기반으로 대규모 읽기 이해 데이터셋을 구축한다. 데이터셋은 990,595개의 질문으로 구성되어 있으며, 가장 가까운 대안들보다 1개의 차원 크기가 크다.
    
    2. 이 데이터셋은 대부분의 질문에 대한 "정착 요구"를 가지고 있어서 얼마나 오래 기억 능력이 필요한지를 알 수 있다. 따라서 오랜 기간의 기억 성능 평가에 도움이 될 것이다.
    
    3. 이 데이터셋은 유용한 정보이며, 기존 언어 모델에서도 기억 요구가 컨텍스트 길이를 초과하지 않는 한에도 질문이 쉽지 않음을 보여준다. 또한, 이 데이터셋을 적은 인력 투입으로 확장할 수 있는 코드도 제공된다.
    
    (Most of the technical terms are already in English)

###### Dialogue Act-Aided Backchannel Prediction Using Multi-Task Learning (https://aclanthology.org/2023.findings-emnlp.1006/)
- Anthology ID: 2023.findings-emnlp.1006 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화에서 청취자의 작은 응원 표현인 backchanneling은 자연스러운 대화에 필수적이며 말하는 사람의 의도와 발화 유형과 밀접한 관계가 있다. 
    2. 우리는 multi-task learning 접근법을 제안하여 대화 행위 분류와 함께 backchannel 예측을 위한 텍스트 표현을 학습한다.
    3. 이를 통해 "Yeah" 또는 "Really?"와 같은 구체적인 backchannel의 예측을 F1에서 최대 2.0% 개선할 수 있음을 보였다.

###### mReFinED: An Efficient End-to-End Multilingual Entity Linking System (https://aclanthology.org/2023.findings-emnlp.1007/)
- Anthology ID: 2023.findings-emnlp.1007 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 end-to-end 다국어 entity linking (MEL) 방법은 entity mentions가 주어진 상태로 가정하고, 낮은 품질의 다국어 훈련 말뭉치로 인해 entity mention detection 단계를 건너뛰었다.
    2. 이 논문에서는 mReFinED라는 첫 번째 end-to-end 다국어 entity linking을 제안하고, bootstrapping mention detection 프레임워크를 도입하여 훈련 말뭉치의 품질을 개선한다.
    3. 실험 결과, mReFinED는 최고의 기존 작업을 능가하면서도 44배 더 빠른 속도로 end-to-end MEL 작업을 수행한다.

###### Sub-network Discovery and Soft-masking for Continual Learning of Mixed Tasks (https://aclanthology.org/2023.findings-emnlp.1008/)
- Anthology ID: 2023.findings-emnlp.1008 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 지금까지 Continual learning(CL) 연구에서는 catastrophic forgetting(CF) 문제를 해결하는 것에만 초점을 맞추었었으나, 이 논문은 지식 전달(KT) 측면에서도 성과를 보이고 있다.
    2. 이 논문은 각각의 작업에 대한 지식을 발견하여 서브 네트워크를 통해 각 작업의 지식을 완벽하게 유지하여 catastrophic forgetting을 극복하는 방법을 제안한다.
    3. 또한, 이전 지식을 보존하고 새로운 작업이 과거의 지식을 활용하여 transfer learning을 이룩할 수 있도록 소프트-마스킹 메커니즘을 제안하였으며, 다양한 작업 혼합에서 강력한 베이스라인보다 일관되게 우수한 성능을 보여주었다.

###### PIVOINE: Instruction Tuning for Open-world Entity Profiling (https://aclanthology.org/2023.findings-emnlp.1009/)
- Anthology ID: 2023.findings-emnlp.1009 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 닫힌 세계 정보 추출(Closed-world IE)과 달리, 개방 세계 정보 추출에서는 미리 정의된 체계를 벗어난 entity와 relation이 존재할 수 있는 상황을 고려한다.
    2. 우리는 instruction tuning을 통해 원하는 entity profile을 추출할 수 있는 인공지능 모델을 개발하고, INSTRUCTOPENWIKI라는 다양한 instruction을 활용한 대규모 데이터셋을 구축한다.
    3. 실험 결과, 우리의 모델인 PIVOINE은 전통적인 방법과 ChatGPT 기반의 기준선을 훌륭히 능가하며, 보지 못한 instruction과 체계 외의 경우에서도 탁월한 일반화 능력을 보여준다. 따라서, PIVOINE은 개방 세계 entity profiling의 해결책으로서 희망찬 가능성을 보여준다.

###### DiQAD: A Benchmark Dataset for Open-domain Dialogue Quality Assessment (https://aclanthology.org/2023.findings-emnlp.1010/)
- Anthology ID: 2023.findings-emnlp.1010 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 평가에서 기존 연구들은 실제 사용자 설정과 멀리 떨어진 대화들의 일관성과 같은 하위 메트릭만을 제공하며, 온전한 대화와 인간-학습적인 평가 데이터셋을 제공하기 어렵다. 
    2. 본 논문에서는 오픈 도메인 대화의 품질을 자동 평가하기 위해 대규모 대화 품질 평가 데이터셋(DiQAD)을 공개한다. 
    3. 이 데이터셋은 인간 판단을 따르는 차원에 기반한 평가 기준을 수립하고, 약 10만개의 실제 사용자 간 대화를 이 기준에 따라 어노테이트하여 구성되었다.

###### Tuna: Instruction Tuning using Feedback from Large Language Models (https://aclanthology.org/2023.findings-emnlp.1011/)
- Anthology ID: 2023.findings-emnlp.1011 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오픈 소스 대규모 언어 모델 (LLM)인 LLaMA와 같은 모델에 Instruct-GPT 및 GPT-4와 같은 더 강력한 LLM의 직접적인 출력을 사용하여 모델 동작을 인간의 선호도에 맞추는 것은 경제적인 방법이지만, instruction-tuned 모델은 하나의 입력당 하나의 응답만을 보고있어 더 좋은 응답의 지식이 부족하다.
    2. 이 연구에서는 확률적 순위 지정과 문맥적 순위 지정 접근 방식을 사용하여 instruction-tuned LLM을 fine-tuning하여 더 나은 응답 생성 확률을 높이는 방법을 제안한다. 확률적 순위 지정은 instruction-tuned 모델이 teacher LLM에서 고품질 및 저품질 응답의 상대적 순위를 물려 받도록 하며, 문맥적 순위 지정을 통해 모델은 강력한 LLM의 문맥 이해 능력을 사용하여 자체적으로 응답 분포를 개선할 수 있다.
    3. 또한, 우리는 확률적 순위 지정과 문맥적 순위 지정을 instruction-tuned LLM에 순차적으로 적용한다. 이를 Tuna라고 부르는 결과 모델은 Super Natural Instructions (119개의 테스트 과제), LMentry (25개의 테스트 과제), Vicuna QA에서 일관되게 성능을 향상시키며, 몇 가지 강력한 강화 학습 기준선보다 더 좋은 결과를 얻을 수 있다.

###### Emptying the Ocean with a Spoon: Should We Edit Models? (https://aclanthology.org/2023.findings-emnlp.1012/)
- Anthology ID: 2023.findings-emnlp.1012 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에 인기를 끄는 직접적인 모델 편집 방법은 사실적인 오류를 LLM(Large Language Models) 생성물에서 수정하는 수단으로 사용되지만, 이 방법에 대해 의문을 제기합니다.
    2. 우리는 모델 편집을 정의되고 목적이 더 잘 정의된 세 가지 유사한 접근법과 비교합니다: (1) retrieval-based architectures, (2) concept erasure methods, 그리고 (3) attribution methods.
    3. 우리는 직접 모델 편집을 LLM의 단점을 해결하기 위한 체계적인 해결책으로 신뢰할 수 없고, 모델 설명 가능성을 향상시키는데는 잠재력이 있지만, 사실성을 신뢰할 수 있다는 개념을 강화함으로써 위험을 초래할 수 있다고 주장합니다. 따라서 LLM 배치 프로세스의 일부로 모델 편집의 신중한 홍보와 적용, 그리고 편집을 중요한 구성 요소로 의존하지 않는 경우에만 LLM의 사용 사례를 책임 있게 제한할 것을 요구합니다.

###### A Causal View of Entity Bias in (Large) Language Models (https://aclanthology.org/2023.findings-emnlp.1013/)
- Anthology ID: 2023.findings-emnlp.1013 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전학습 모델들은 entity bias로 인해 부적절한 예측을 하는데, 이러한 문제를 개선하기 위해 인과성 기반의 방법을 제안한다. 제안한 방법은 원래 entity를 주변 entity로 대체하여 편향 정보를 줄이고 의미 정보를 보존하는 인과적 개입 기술을 사용한다.
    2. 인과 구조 모델을 기반으로 한 훈련 시 개입은 관계 추출 및 기계 독해 작업에서 사전 학습 모델의 OOD 성능을 향상시키는 것으로 보입니다.
    3. 그리고 상황에 따른 개입은 GPT-3.5의 엔터티 기반 지식 충돌을 효과적으로 줄여 기계 독해 작업의 정확도를 향상시키는 것으로 보입니다.

###### T5Score: Discriminative Fine-tuning of Generative Evaluation Metrics (https://aclanthology.org/2023.findings-emnlp.1014/)
- Anthology ID: 2023.findings-emnlp.1014 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 생성된 텍스트를 평가하기 위한 임베딩 기반 메트릭은 주로 두 가지 패러다임으로 나눌 수 있다. 유인적인 평가 메트릭은 감독된 인간 주석에 따라 어떤 출력물이 더 높은 품질을 가지는지 직접 예측하는데 훈련되고, 생성적인 평가 메트릭은 생성 모델의 확률에 따라 텍스트를 평가하는 것을 훈련한다.
    2. 본 논문에서는 두 가지 방식의 장점을 결합하여, 사용 가능한 데이터로부터 감독 및 비감독 신호를 모두 사용하는 프레임워크를 제안한다.
    3. 실험 결과, T5Score는 segment 수준에서 기존 최고의 메트릭에 비해 모든 데이터셋에서 가장 우수한 성능을 달성한다.

###### T-Projection: High Quality Annotation Projection for Sequence Labeling Tasks (https://aclanthology.org/2023.findings-emnlp.1015/)
- Anthology ID: 2023.findings-emnlp.1015 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 주어진 sequence labeling task와 언어에 대해 레이블링된 데이터가 적을 때, annotation projection은 자동으로 주석이 달린 데이터를 생성하기 위한 전략 중 하나로 제안되었다.
    2. 본 논문에서는 annotation projection을 위한 새로운 접근 방식인 T-Projection을 제안한다. 이 방법은 사전 훈련된 텍스트 대 텍스트 언어 모델과 최신 기계 번역 기술을 활용한다.
    3. 실험 결과, T-Projection은 이전의 annotation projection 방법보다 뛰어난 성능을 보여주었으며, 고품질 훈련 데이터 부족 문제를 자동으로 해결하는데 도움을 줄 수 있다고 한다.

###### MTGER: Multi-view Temporal Graph Enhanced Temporal Reasoning over Time-Involved Document (https://aclanthology.org/2023.findings-emnlp.1016/)
- Anthology ID: 2023.findings-emnlp.1016 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문서의 사실과 시간은 복잡하게 얽혀 있어 문서에서의 시간적 추론이 어렵다. 이전 연구는 시간을 암묵적으로 모델링하여 이러한 복잡한 관계를 처리하기 어렵다. 
    2. 우리는 이 문제에 대응하기 위해, 시간이 관련된 문서에 대한 시간적 추론을 위한 새로운 Multi-view Temporal Graph Enhanced Reasoning (MTGER) 프레임워크를 제안한다. 
    3. MTGER는 다양한 시간 그래프를 통해 사실들 간의 시간적 관계를 명시적으로 모델링하며, multi-view 메카니즘을 통해 time-focused와 fact-focused 정보를 모두 포착하여 상호 보완할 수 있도록 한다.

###### MSCFFN: A New FFN with Multi-Space Cross to Accelerate Transformer (https://aclanthology.org/2023.findings-emnlp.1017/)
- Anthology ID: 2023.findings-emnlp.1017 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Transformer 모델은 다양한 자연어 처리 작업에서 인상적인 성과를 거두었지만, 몇몇 분야에서는 사용이 제한되고 있으며, 무거운 계산 복잡성이 주요한 제한 사항 중 하나이다. 
    2. 이 논문에서는 Transformer의 FFN (feed forward network) 구조를 재설계하여 계산 복잡성을 줄이고 정확한 결과를 보장하는 MSCFFN이라는 새로운 구조를 제안한다. 
    3. Long-Range Arena 벤치마크에서 실험을 통해 제안한 방법의 효과를 검증하였으며, 결과로는 MSCFFN이 더 빠른 속도로 비슷하거나 더 나은 정확도를 달성할 수 있다는 것을 보여준다.

###### Dialect Transfer for Swiss German Speech Translation (https://aclanthology.org/2023.findings-emnlp.1018/)
- Anthology ID: 2023.findings-emnlp.1018 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 스위스 독일어는 공식적인 글자체가 없으며 다양한 방언으로 구성되어 있으며, 약 5백만 명의 사용자만 있는 자원이 부족한 언어이다. 
    2. 이 논문은 스위스 독일어와 표준 독일어 간의 차이와 다양한 방언의 포함 및 배제가 스위스 독일어 음성 번역 모델의 성능에 어떤 영향을 미치는지에 대해 연구하였다.
    3. 방언 다양성과 언어적 차이가 스위스 독일어 음성 번역에 상당한 어려움을 초래하며, 이는 경험적 연구에서 유추된 언어학적 가설과 일치한다는 것을 보였다.

###### Masked Path Modeling for Vision-and-Language Navigation (https://aclanthology.org/2023.findings-emnlp.1019/)
- Anthology ID: 2023.findings-emnlp.1019 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 지시에 기반한 시각-언어 네비게이션 (VLN) 에이전트는 실제 환경에서 학습되어 진다. VLN의 주요 도전은 학습 데이터의 한정성으로 인해 모델의 효과적인 일반화 능력이 제한되는 것이다. 이 논문에서는 외부 도구를 사용하여 pseudo-labeled 데이터를 생성하거나 훈련 중 web-scaled 이미지-텍스트 쌍을 통합함으로써 이 문제를 완화하려는 기존의 방법들을 소개한다. 
    2. 이 논문에서 제안하는 MPM (Masked Path Modeling)은 자체 수집한 데이터를 사용하여 에이전트를 사전 훈련함으로써 외부 도구의 필요성을 없앤다. 에이전트는 탐색 환경을 탐험하고 해당 에이전트 동작과 함께 탐험한 경로를 기록한다. 그 다음에는 훈련 데이터를 사용하여 원래의 동작 순서를 복원하도록 훈련시킨다. 
    3. 실험 결과는 MPM의 성공률에서 유의미한 개선을 보여주었으며, 훈련 전에 에이전트가 저물지 않은 환경을 탐색할 수 있는 경우 추가적인 개선 가능성을 보여주었다.

###### Learning Interpretable Style Embeddings via Prompting LLMs (https://aclanthology.org/2023.findings-emnlp.1020/)
- Anthology ID: 2023.findings-emnlp.1020 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 글 작가 스타일에 대한 내용-독립적인 표현을 학습하는 스타일 표현 학습은 해석 가능한 표현이 아니기 때문에 감독되고 설명이 가능한 작가 식별과 같은 하위 응용 프로그램에서 활용이 복잡한 과제가 있다.
    2. 이 연구에서는 프롬프트를 사용하여 많은 수의 텍스트에서 스타일 메트릭을 수행하여 합성 스타일 메트릭 데이터셋을 생성한다. 이 합성 데이터를 사용하여 LISA 임베딩이라고 불리는 사람이 읽고 이해할 수 있는 스타일 표현을 학습한다.
    3. 우리는 이 연구를 통해 합성 데이터셋(StyleGenome)과 해석 가능한 스타일 임베딩 모델(LISA)을 리소스로 공개한다.

###### Exploring Context-Aware Evaluation Metrics for Machine Translation (https://aclanthology.org/2023.findings-emnlp.1021/)
- Anthology ID: 2023.findings-emnlp.1021 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기계 번역 평가 연구는 주로 개별 문장의 질에 초점을 맞추었으며, 문맥 정보의 중요성을 간과해왔다.
    2. 이 논문에서는 Cont-COMET이라는 문맥-인식 기계 번역 평가 메트릭을 제안하였다. 이 접근 방식은 평가할 문장의 이전과 다음 문맥을 동시에 고려하고, 인간 주석 기준에 맞게 메트릭을 학습한다.
    3. WMT의 공식 테스트 프레임워크에서 수행된 실험과 평가 결과, Cont-COMET은 시스템 수준과 문장 수준 모두에서 개선되었다.

###### GRACE: Discriminator-Guided Chain-of-Thought Reasoning (https://aclanthology.org/2023.findings-emnlp.1022/)
- Anthology ID: 2023.findings-emnlp.1022 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다단계 추론에서, 언어 모델은 쉽게 잘못된 단계에도 높은 확률을 할당할 수 있다. 이 문제를 해결하기 위해, 우리는 GRACE라고 불리는 단계별 디코딩 방법을 제안한다. 
    2. GRACE는 실제와 잘못된 단계 사이의 대조적인 손실을 통해 훈련된 판별기를 사용하여 디코딩 과정에서 다음 단계 후보들을 평가한다. 
    3. GRACE는 유의미한 성능 향상을 보여주며, greedy decoding, 검증자, 그리고 self-consistency와 비교해 대부분의 설정에서 우수한 결과를 낸다.

###### QADYNAMICS: Training Dynamics-Driven Synthetic QA Diagnostic for Zero-Shot Commonsense Question Answering (https://aclanthology.org/2023.findings-emnlp.1023/)
- Anthology ID: 2023.findings-emnlp.1023 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. '영상 대응 Question-Answering(QA)'는 일부 특정 벤치마크를 넘어선 일반적인 상황에 대해 모델이 추론할 수 있어야 한다. 
    2. 우리는 QA에서 LLMs를 사용하는 일련의 과정에서 생기는 잡음과 문법 오류, 그리고 잘못된 정답을 제거하고, 진단 및 보정을 위한 훈련 동태 구조 기반 프레임워크인 QADYNAMICS를 제안한다. 
    3. 실험 결과, 우리의 접근 방식은 33%의 합성 데이터만 사용하여 모든 베이스라인 모델들보다 성능이 뛰어났으며, 전문가 평가에서도 QA의 품질을 크게 향상시켰다.

###### RexUIE: A Recursive Method with Explicit Schema Instructor for Universal Information Extraction (https://aclanthology.org/2023.findings-emnlp.1024/)
- Anthology ID: 2023.findings-emnlp.1024 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Universal Information Extraction (UIE)는 다양한 대상, 이질적인 구조 및 수요별 스키마에 의해 도전적인 영역이다. 
    2. 기존 작업들은 Named Entity Recognition (NER) 및 Relation Extraction (RE)과 같은 몇 가지 작업들을 통합함으로써 성공을 거두었으나, quadruples 및 quintuples와 같은 일반적인 스키마를 추출할 때는 진정한 UIE 모델로서 부족하다. 
    3. 이 논문에서는 거의 모든 추출 스키마를 포괄하는 형식적인 정의를 통해 진정한 UIE를 재정의하였으며, RexUIE라는 Recursive Method with Explicit Schema Instructor for UIE를 제안한다.

###### PromptARA: Improving Deep Representation in Hybrid Automatic Readability Assessment with Prompt and Orthogonal Projection (https://aclanthology.org/2023.findings-emnlp.1025/)
- Anthology ID: 2023.findings-emnlp.1025 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "가독성 평가는 독자의 독해 능력에 따라 텍스트를 자동으로 분류하는 것을 목표로 한다. 하이브리드 ARA 모델은 심층 및 언어적 특징을 모두 사용하여 최근 주목을 받고 있다. 그러나 심층 특징은 훈련 데이터 부족으로 완전히 탐구되지 않았으며, 심층 및 언어적 특징의 퓨전은 기존의 하이브리드 ARA 모델에서는 효과적이지 않다."
    2. 우리는 PromptARA라는 신규 하이브리드 ARA 모델을 제안하여 심층 특징 표현을 개선하기 위해 prompt를 활용하고 심층 및 언어적 특징을 퓨전하기 위해 직교 투영 계층을 사용한다.
    3. 4개의 영어와 2개의 중국어 말뭉치에서 수행된 일련의 실험 결과는 제안된 모델의 효과적임을 보여준다. 실험 결과는 제안된 모델이 최고의 성능을 가진 모델에 우월하다는 것을 나타낸다.

###### Does Listener Gaze in Face-to-Face Interaction Follow the Entropy Rate Constancy Principle: An Empirical Study (https://aclanthology.org/2023.findings-emnlp.1026/)
- Anthology ID: 2023.findings-emnlp.1026 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 (문자와 말)는 일반적으로 엔트로피 비율 일정성 (ERC) 원칙을 따른다고 가정되며, 텍스트의 정보 밀도는 시간에 따라 일정하다. 최근에는 독발에서 사용되는 비언어적 제스처에서도 이 원칙이 발견되었지만, 청취자의 비언어적 신호에도 ERC 원칙이 적용되는지 여전히 불분명하다.
    2. 우리는 대화에서 추출한 청취자의 시선 행동에 초점을 맞추고, 비디오로 기록된 대화의 시선 데이터를 처리하고 정보 밀도를 계산하기 위해 transformer 기반 신경 시퀀스 모델을 훈련시켰다. 또한 사전 훈련된 언어 모델을 사용하여 해당 말의 정보 밀도를 계산한다. 
    3. 우리의 결과는 (1) 대화에서 청취자의 시선 행동이 대체로 ERC 원칙을 따르고, (2) 말의 정보 밀도와 청취자의 시선 행동 간에 일치가 있는 것을 보여준다.

###### Incorporating Object-Level Visual Context for Multimodal Fine-Grained Entity Typing (https://aclanthology.org/2023.findings-emnlp.1027/)
- Anthology ID: 2023.findings-emnlp.1027 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Fine-grained entity typing(FGET)에서는 entity를 언급하는 문맥에서 적절한 세부 유형을 지정하는 것이 중요한데, 기존 접근 방식은 텍스트 문맥 정보만 사용하였다. 
    2. 이 논문에서는 visual context도 활용하기 위해 멀티모달 fine-grained entity typing(MFGET)이라는 새로운 작업을 제안하고, MFGET를 위한 대규모 데이터셋인 MFIGER를 구축한다. 
    3. 실험 결과는 우리의 접근 방식이 기존 텍스트 기반 방법보다 분류 성능이 우수함을 보여주었다.

###### Exploring the Numerical Reasoning Capabilities of Language Models: A Comprehensive Analysis on Tabular Data (https://aclanthology.org/2023.findings-emnlp.1028/)
- Anthology ID: 2023.findings-emnlp.1028 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 금융, 경제, 과학과 같은 실제 세계 도메인에서는 숫자 데이터가 중요한 역할을 한다. 따라서 숫자를 이해하고 추론하는 능력은 이러한 분야에서 필수적이다.
    2. 이 논문에서는 표현, 숫자 감각, 조작, 복잡한 추론 등 네 수준을 포함하는 숫자 추론 기술을 위한 완전한 계층적 분류 체계를 제안한다.
    3. 최신 모델들의 모든 추론 유형에 대한 포괄적인 평가를 실시하고, 다양하고 포괄적인 숫자 확인 도구를 개발하여 다른 모델 유형에 대한 도전적인 추론 유형을 식별한다. FlanT5와 GPT3.5는 다른 모델에 비해 강력한 숫자 추론 능력을 보인다.

###### Assessing Privacy Risks in Language Models: A Case Study on Summarization Tasks (https://aclanthology.org/2023.findings-emnlp.1029/)
- Anthology ID: 2023.findings-emnlp.1029 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델들은 다양한 태스크에서 최고의 성능을 보여주면서 NLP 분야를 혁신했지만, 이러한 모델들이 학습 데이터의 정보를 공개할 수 있다는 우려가 있다. 
    2. 이 연구에서는 요약 태스크에 대해 멤버십 추론(MI) 공격을 연구하며, 샘플과 모델의 API에 대한 블랙박스 접근권을 통해 샘플이 학습 데이터의 일부인지 판단할 수 있는지 조사한다. 
    3. 우리는 텍스트 유사성과 문서 수정에 대한 모델의 내성을 MI 신호로 활용하고, 널리 사용되는 데이터셋에서의 효과를 평가한다. 결과적으로, 요약 모델은 참조 요약이 없는 경우에도 데이터 멤버십을 공개할 위험이 있다는 것을 보여준다. 또한, MI 공격에 대비하여 요약 모델을 훈련하기 위한 여러 가지 안전장치에 대해 논의하고, 개인정보 보호와 유효성 사이의 본질적인 trade-off에 대해 논의한다.

###### BERT Has More to Offer: BERT Layers Combination Yields Better Sentence Embeddings (https://aclanthology.org/2023.findings-emnlp.1030/)
- Anthology ID: 2023.findings-emnlp.1030 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. BERT 기반 모델의 문장 표현을 특징 추출기로 사용하는 것은 BERT를 전체적으로 fine-tune 하는 것보다 한 번의 전처리로 데이터의 표현을 계산한 후 후속 작업에 사용함으로써 시간을 훨씬 절약할 수 있다.
    2. 이 논문에서는 BERT 기반 모델의 특정 레이어의 조합이 데이터셋과 모델에 따라 훨씬 좋은 결과를 얻을 수 있다고 제안한다.
    3. 다양한 BERT 기반 모델과 작업, 데이터셋에 대해 우리의 방법의 효과를 실험적으로 보여주었는데, 7개의 표준 의미론적 텍스트 유사성 데이터셋에서는 Spearman correlation을 최대 25.75% 향상시키고 평균 16.32% 향상시켰다.

###### Extrapolating Multilingual Understanding Models as Multilingual Generators (https://aclanthology.org/2023.findings-emnlp.1031/)
- Anthology ID: 2023.findings-emnlp.1031 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 마스크된 언어 모델을 통해 사전 훈련된 다국어 이해 모델은 많은 언어 이해 태스크에서 좋은 결과를 달성했지만, 디코더 기반의 인과 언어 모델과 비교했을 때 품질이 낮은 텍스트를 생성하는 능력이 부족합니다.
    2. 우리는 적은 수의 추가 매개 변수를 사용하여 다국어 인코더를 다국어 생성기로 적응시키기 위해 '의미 기반 정렬-덴오이징' (Semantic-Guided Alignment-then-Denoising, SGA) 접근법을 제안합니다. 실험 결과, 이 접근 방법은 초기화 기반 방법보다 우수한 성능을 보여주며, 기계 번역에서 9.4 BLEU, 질문 생성에서 8.1 Rouge-L, 이야기 생성에서 5.5 METEOR의 개선 효과를 얻었습니다.
    3. 그러나 mBERT와 비교했을 때 단순히 SGA로 XLM-Rlarge가 지도학습 환경에서 여전히 뒤쳐지는 것을 관찰하였으며, 이는 이해 모델이 강력한 생성기로 발전시키기 위해 더 많은 탐구가 필요함을 보여줍니다.

###### SAC3: Reliable Hallucination Detection in Black-Box Language Models via Semantic-aware Cross-check Consistency (https://aclanthology.org/2023.findings-emnlp.1032/)
- Anthology ID: 2023.findings-emnlp.1032 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현대 언어 모델의 신뢰성을 이해하기 위한 핵심 단계로 환각 탐지(Hallucination detection)가 있다. 본 연구에서는 어떤 증상 확인방식인 self-consistency로는 파악할 수 없는 1) 질문 수준과 2) 모델 수준의 환각에 대해 다시 살펴보았다.
    2. 우리는 이 발견을 바탕으로 Self-consistency checking의 원칙을 기반으로 한 새로운 샘플링 기반 방법인 semantic-aware cross-check consistency (SAC3)를 제안한다.
    3. 우리의 SAC3 방식은 의미론적으로 동등한 질문 왜곡과 크로스 모델 응답 일관성 확인과 같은 발전된 기술을 활용하여 질문 수준과 모델 수준의 환각을 모두 감지할 수 있는 추가적인 메커니즘을 포함하고 있다.

###### Test-Time Self-Adaptive Small Language Models for Question Answering (https://aclanthology.org/2023.findings-emnlp.1033/)
- Anthology ID: 2023.findings-emnlp.1033 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 instruction-finetuned large language models(LMs)는 다양한 태스크에서 현저한 성능을 보여주었으나, 특정 태스크에 대해서는 전이와 지식 적응 능력이 제한적이기 때문에 최적이 아닐 수 있다.
    2. 이 논문에서는 unlabeled test data만 가지고 작동하는 self-adaptive LMs의 능력을 보여주고 조사한다. 
    3. 우리의 제안된 self-adaption 전략은 높은 복원력과 다양한 프롬프트에 대한 안정성을 가진 벤치마크 QA datasets에서 유의한 성능 향상을 보여준다.

###### ExpNote: Black-box Large Language Models are better Task Solvers with Experience Notebook (https://aclanthology.org/2023.findings-emnlp.1034/)
- Anthology ID: 2023.findings-emnlp.1034 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 다양한 작업을 푸는 데 큰 힘을 보이고 일반적인 문제 해결자로 간주되지만, 특정 작업에서는 여전히 실패한다. 이 논문에서는 검은 상자 언어 모델의 능력을 향상시키는 문제에 초점을 맞추고 있으며, 훈련 데이터로부터 경험을 반영하고 기억된 경험을 테스트 중에 외부 메모리에서 검색하는 자동화된 프레임워크인 ExpNote를 제안한다.
    2. ExpNote를 다양한 작업에서 평가하였고 실험 결과로는 검은 상자 언어 모델의 성능이 크게 향상되었음을 보여주었다.
    3. ExpNote의 데이터와 코드는 https://github.com/forangel2014/ExpNote에서 확인할 수 있다.

###### Evaluating Parameter-Efficient Finetuning Approaches for Pre-trained Models on the Financial Domain (https://aclanthology.org/2023.findings-emnlp.1035/)
- Anthology ID: 2023.findings-emnlp.1035 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수백만, 수십억, 심지어 수조 개의 trainable한 파라미터를 가진 대규모 언어 모델들이 인기를 끌고 있다. 하지만 이 모델들은 빠르게 오버피티마이즈(over-parameterize) 되는 위험성을 가지고 있으며, 완전히 fine-tuning하기 위한 적응 비용이 크게 증가한다.
    2. 미세조정하는 동안 미리 훈련된 가중치를 모두 고정시키는 'parameter-efficient tuning' 접근 방식은 전통적인 fine-tuning 대안으로 인기를 얻고 있다.
    3. 이 논문은 금융과 같은 도메인별 분야에서 parameter-efficient tuning 방법을 활용하여 일련의 금융 BERT 모델의 성능을 완전히 fine-tuned 모델과 비교하였고, 시간과 자원 효율성에서 이득을 얻으면서도 전통적인 fine-tuning과 성능이 비슷하다는 것을 확인하였다.

###### Can Retriever-Augmented Language Models Reason? The Blame Game Between the Retriever and the Language Model (https://aclanthology.org/2023.findings-emnlp.1036/)
- Anthology ID: 2023.findings-emnlp.1036 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 미세 조정 전처리 언어 모델에 retriever를 추가하는 것이 자연어처리에 있어서 인기가 있는데, 이 논문에서는 이러한 모델들의 강점과 약점을 다양한 태스크를 통해 평가하였고, 판단에 필요한 정보를 검색하기 위한 단순 유사도 측정은 충분하지 않음을 보였다. 
    2. 또한, 필요한 문장만 주어진 경우에도 언어 모델들은 강한 판단 능력을 보이지 않았으며, 첨가된 retriever의 성능이 저하되는 현상도 발견되었다.
    3. 더 큰 언어 모델은 성능을 향상시키지만, 개선의 여지가 여전히 많은 것으로 나타났으며, 멀티합-검색-읽기는 GPT-3.5와 같은 대형 언어 모델에 대해 효과적인 방법이지만 다른 언어 모델(예: Flan-T5-xxl)에는 일반화되지 않는다는 것을 분석했다.

###### BERTwich: Extending BERT’s Capabilities to Model Dialectal and Noisy Text (https://aclanthology.org/2023.findings-emnlp.1037/)
- Anthology ID: 2023.findings-emnlp.1037 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다이얼렉트, 비공식적이거나 맞춤법이 틀린 텍스트와 같은 비표준 텍스트를 다루는 NLP 애플리케이션에서는 BERT와 같은 언어 모델의 성능이 저하된다. BERT의 모델링 능력을 비표준 텍스트에 대응시키기 위해 어떻게 해야 할까?
    2. fine-tuning은 모델을 특정 작업에 맞게 조정하는 데 도움이 되지만, 비표준 언어에 모델을 적응시키기 위해 필요한 깊이 있는 변화를 가져오지 못한다. 
    3. 이 논문에서는 BERT의 인코더 스택을 추가적인 인코더 층으로 둘러싸는 기존 아이디어를 소개하며, 이 방법이 최근 연구를 통해 미세 조정 데이터에 문자 수준의 노이즈를 포함시킴으로써 다이얼렉트 텍스트로의 zero-shot 전이를 촉진하고 단어와 그와 대응되는 노이즈가 있는 단어 사이의 임베딩 공간의 거리를 줄일 수 있는 것을 발견했다.

###### Closed Boundary Learning for Classification Tasks with the Universum Class (https://aclanthology.org/2023.findings-emnlp.1038/)
- Anthology ID: 2023.findings-emnlp.1038 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Universum class"는 관심 클래스에 속하지 않는 샘플들의 모음으로, 관계 추출, 개체명 인식, 감성 분석 등 NLP의 많은 분류 기반 작업에서 일반적으로 등장한다. 하지만, 기존 방법들은 Universum 클래스를 관심 클래스와 동등하게 처리하여, 과적합, 잘못된 분류, 모델의 강성 감소와 같은 문제가 발생한다.
    2. 이 논문에서는 closed boundary learning 방법을 제안하여, 관심 클래스에는 닫힌 결정 경계를 적용하고 특징 공간에서 모든 닫힌 경계 외부를 Universum 클래스의 공간으로 지정한다.
    3. 제안된 방법은 Universum 클래스의 독특한 특성에 맞춰 닫힌 경계를 임의의 모양으로 정의하고, Universum 클래스의 규칙 기반 확률 추정 및 경계 학습 손실을 제안하여, 분류 모델의 정확성과 강성을 동시에 향상시킨다.

###### Revisiting Entropy Rate Constancy in Text (https://aclanthology.org/2023.findings-emnlp.1039/)
- Anthology ID: 2023.findings-emnlp.1039 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "균일한 정보 밀도 (UID) 가설은 인간들이 발화나 담화에 정보를 균등하게 분배하는 경향이 있다고 주장한다."
    2. 기존 연구에서 영어 텍스트의 확률에 대한 n-gram 언어 모델을 기반으로 엔트로피 비율 일정성 원리를 제안했으나, 이 논문은 피드포워드 언어 모델을 사용하여 해당 가설을 재평가하였다.
    3. 실험 결과는 엔트로피 비율 일정성을 지지하는 명확한 증거를 찾지 못하였으며, 이는 균일한 정보 밀도 가설과 효율적인 의사소통에 대한 언어학적 이론에 대한 함의를 논의한다.

###### Calibrated Seq2seq Models for Efficient and Generalizable Ultra-fine Entity Typing (https://aclanthology.org/2023.findings-emnlp.1040/)
- Anthology ID: 2023.findings-emnlp.1040 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정보 추출에서의 초 세부 entity typing은 텍스트 안의 entity 언급에 대해 미세한 의미론적 유형을 예측하여 정보 추출에 중요한 역할을 한다. 그러나 이 작업은 출력 공간 내 이종의 entity 타입 때문에 상당한 어려움을 가지고 있다.
    2. 이 논문에서는 CASENT라고 불리는 seq2seq 모델을 소개하여 교정된 신뢰 점수로 초 세부 유형을 예측한다.
    3. UFET 데이터셋에서 상당한 실험을 진행하였고 이전의 모델보다 F1 점수와 교정 오차에서 뛰어난 성능을 보여주며 추론 속도를 50배 이상 향상시켰으며, 훈련 시보지 않은 다섯 가지 특수 도메인 entity typing 데이터셋에서도 일반화 능력을 보였다.

###### Learning Semantic Role Labeling from Compatible Label Sequences (https://aclanthology.org/2023.findings-emnlp.1041/)
- Anthology ID: 2023.findings-emnlp.1041 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. SRL (Semantic role labeling)은 여러 개의 분리된 label set을 가지고 있지만, 이들을 어떻게 상호 도움을 줄 수 있는지에 대한 질문이 있다. 이 논문에서는 VerbNet과 PropBank 라벨을 하나의 시퀀스로 모델링하는 방식을 제안하고, Semlink 제약 조건을 활용하여 디코딩을 함께 수행하여 전반적인 F1 스코어를 향상시키고 있다.
    2. 이 모델은 VerbNet과 PropBank 사이에서의 cross-task interaction을 적용하고 있는데, 특히 Constrained Marginal Model을 활용하여 Semlink에 정의된 지식을 사용하여 PropBank-only 데이터로부터 더 많은 효과를 얻고 있다.
    3. CoNLL05 기준으로, 이 모델은 state-of-the-art F1 스코어를 달성하고 있으며, in-domain 모델에 비해 3.5 (VerbNet)와 0.8 (PropBank) 점수로 우수한 성능을 보여주고 있다.

###### QUADRo: Dataset and Models for QUestion-Answer Database Retrieval (https://aclanthology.org/2023.findings-emnlp.1042/)
- Anthology ID: 2023.findings-emnlp.1042 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전에 계산된 데이터베이스로부터 효과적으로 답변을 검색하는 자동 질문응답(QA) 시스템을 설계하기 위한 효과적인 방법은 훈련/테스트 데이터의 부족이다.
    2. 이 논문에서는 이런 문제를 해결하기 위해 15,211개의 입력 질문과 각각 30개의 비슷한 질문/답변 쌍으로 구성된 소스를 제공한다. 
    3. 뿐만 아니라 이 리소스에 대한 포괄적인 실험 결과를 보고하며, 답변 관련성, 훈련 전략 및 모델 입력 구성과 같은 QA 시스템의 다양한 중요한 측면에 대한 품질과 특성을 테스트한다.

###### Give Me the Facts! A Survey on Factual Knowledge Probing in Pre-trained Language Models (https://aclanthology.org/2023.findings-emnlp.1043/)
- Anthology ID: 2023.findings-emnlp.1043 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Pre-trained Language Models (PLMs)는 방대한 라벨 없는 데이터로 훈련되어 다양한 세계지식이 담겨 있다. 이는 PLMs의 다운스트림 태스크 성능과 지식 베이스로서의 사용을 정당화하는 데에 관심이 모여왔다. 
    2. 본 논문에서는 PLMs의 사실적인 지식을 조사하는 방법과 데이터셋에 대해 조사한다.
    3. 저자들은 사실적인 조사 방법과 데이터셋을 주제로 하여, PLMs를 지식 베이스로 사용하기 위해 지식 보존과 prompt 최적화에 대한 연구 방향을 제안한다.

###### Is ChatGPT the ultimate Data Augmentation Algorithm? (https://aclanthology.org/2023.findings-emnlp.1044/)
- Anthology ID: 2023.findings-emnlp.1044 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. GPT-3.5인 ChatGPT의 활용성을 평가하기 위해 zero-shot learning, 새로운 데이터 생성 또는 사람 주석가의 대체와 같은 방법을 사용하여 주석 비용을 절감하는 연구가 이루어져왔다.
    2. ChatGPT를 사용하여 paraphrasing 및 zero-shot 생성으로 새로운 데이터를 생성하고, 이를 다른 7개 알고리즘과 비교한다.
    3. ChatGPT는 어떤 간단한 데이터에서는 탁월한 성능을 보이지만, 전반적으로 다른 알고리즘보다 더 우수한 성능을 보이지 않으며, 민감한 내용으로 인해 종종 답변을 거부하는 경향이 있기 때문에 실무자에게 더 큰 부담을 요구한다.

###### Enhanced Simultaneous Machine Translation with Word-level Policies (https://aclanthology.org/2023.findings-emnlp.1045/)
- Anthology ID: 2023.findings-emnlp.1045 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 SiMT (Simultaneous Machine Translation) 분야에서는 번역 과정의 각 단계마다 READ할지, WRITE할지를 결정하는 정책들의 도입으로 주목할 만한 발전이 있었다. 그러나 많은 기존 연구에서는 subword 단위에서 연산이 수행되는 것으로 가정하고 있으나, 대부분의 실제 시나리오에서는 입력과 출력의 표준 단위가 보통 단어 수준이기 때문에, 이 논문에서 subword 단위에서 개발 및 검증된 정책이 단어 수준에서 작동하는 정책에 비해 훌륭하다는 것을 증명하였다.
    2. 또한, 논문에서는 언어 모델(LMs)을 사용하여 SiMT 모델을 향상시키는 방법을 제안하였는데, 이때 제안된 단어 수준 정책은 LMs와 SiMT 모델 간의 subword 차이를 해결하는데 핵심적인 역할을 한다.
    3. WordSiMT의 코드는 https://github.com/xl8-ai/WordSiMT에서 확인할 수 있다.

###### Causal Intervention-based Few-Shot Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.1046/)
- Anthology ID: 2023.findings-emnlp.1046 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "작은 수의 labeled 샘플로 새로운 entity 클래스를 인식하는 few-shot NER 시스템은 abundant한 데이터셋에 비해 overfitting 문제를 직면한다."
    2. "우리는 spurious correlation으로부터 발생하는 이 overfitting 문제를 해결하기 위해 인과적 개입 기반 few-shot NER 방법을 제안한다."
    3. "우리의 실험 결과는 우리의 접근법이 새로운 최고 성능을 달성한다는 것을 보여준다."

###### TADI: Topic-aware Attention and Powerful Dual-encoder Interaction for Recall in News Recommendation (https://aclanthology.org/2023.findings-emnlp.1047/)
- Anthology ID: 2023.findings-emnlp.1047 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 뉴스 추천 시스템에서 뉴스 리콜은 사용자의 관심에 따라 뉴스를 추천하는 중요한 부분이다. 기존 뉴스 리콜 연구들은 모든 단어를 동일하게 인코딩하는 문제와 관련 단어의 혼란을 해결하지 못한다. 하지만, TADI 모델은 뉴스 주제에 따라 단어들에 가중치를 부여하여 관련 단어 중요도 문제를 해결한다.
    2. TADI는 Dual-encoder Interaction (DI)이라 불리는 강력한 상호작용 모듈을 제공하여 두 개의 인코더가 강력하게 상호작용하도록 한다. DI는 두 개의 보조 타겟을 기반으로 강력한 상호작용을 도와준다.
    3. 다양한 실험을 통해 TADI와 최신 기법들을 비교한 결과, TADI의 효과를 확인하였다.

###### Unveiling the Power of Argument Arrangement in Online Persuasive Discussions (https://aclanthology.org/2023.findings-emnlp.1048/)
- Anthology ID: 2023.findings-emnlp.1048 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이전의 온라인 토론에 대한 연구는 개별 댓글을 조사하고 토론의 상호 작용적인 성격을 무시하는 경향이 있다. 
    2. 이 논문에서는 개별 댓글을 의미론적인 논쟁 단위의 시퀀스로 표현하며, 논평이 상반된 관점에 대한 논쟁을 해결하는 것은 필수적이므로, 이 모델을 확장하여 다양한 논쟁 배열 패턴으로 타입 시퀀스를 군집화하고 토론을 이러한 패턴의 시퀀스로 표현한다.
    3. 이러한 패턴 시퀀스는 토론의 전반적인 구조를 포착하는 논쟁 전략의 상징적인 표현이며, 이 새로운 접근 방식을 통해 Change My View 온라인 토론 포럼의 34,393개의 토론에서 전략을 심층 분석하여, 우리의 토론 모델이 신뢰성 예측에 효과적임을 보여주었고, LLM 기반 분류기를 능가하였다.

###### FFAEval: Evaluating Dialogue System via Free-For-All Ranking (https://aclanthology.org/2023.findings-emnlp.1049/)
- Anthology ID: 2023.findings-emnlp.1049 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 오픈 도메인 대화 시스템 평가는 아직 미해결된 문제이다. 자동 평가 메트릭은 대화 생성 작업에서 인간 평가와의 상관관계가 낮다. 본 연구에서는 FFAEval이라는 신뢰성과 효율성을 갖춘 인간 평가 프레임워크를 제안한다.
    2. 이 프레임워크는 대화 기록을 공유함으로써 평가자들이 여러 대화 시스템과 동시에 다중 턴으로 대화할 수 있도록 한다.
    3. FFAEval은 기존 평가 방법에 비해 점수 기반 인간 평가와 강한 상관관계를 가지며, 효율성과 안정성을 증명한 추가 실험도 진행되었다.

###### Orca: A Few-shot Benchmark for Chinese Conversational Machine Reading Comprehension (https://aclanthology.org/2023.findings-emnlp.1050/)
- Anthology ID: 2023.findings-emnlp.1050 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화식 기계 독해(CMRC) 태스크는 대화에서의 질문에 대답하는 것을 목표로 하며, 폭넓은 응용 분야로 인해 최근 연구 주제로 떠오르고 있다. 
    2. 하지만 기존의 CMRC 벤치마크는 각 대화마다 정적인 Passage를 할당받기 때문에 실제 시나리오와 일치하지 않아 모델의 이해력을 합리적으로 평가하기 어렵다.
    3. 이 논문에서는 실제 시나리오와 일치하도록 Conversational Knowledge-driven Comprehension Benchmark (Orca)를 제안하고, 다양한 도메인에 대한 모델의 일반화 능력을 평가하기 위해 제로샷/퓨샷 설정도 제공한다.

###### VER: Unifying Verbalizing Entities and Relations (https://aclanthology.org/2023.findings-emnlp.1051/)
- Anthology ID: 2023.findings-emnlp.1051 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 실제 세계에서 개체와 개체 간의 관계는 매우 중요하다. 우리는 개체와 관계를 이해함으로써 세계를 이해한다. 이 논문에서는 VER: Verbalizing Entities and Relations을 제안하여 개체와 관계를 문장으로 표현하는 모델을 구축한다.
    2. 우리의 모델은 임의의 개체 또는 개체 집합을 입력으로 받아서 개체와 관계를 표현하는 문장을 생성한다. 실험 결과, 우리의 모델은 개체와 개체 관계를 높은 품질의 문장으로 표현할 수 있으며, 정의 모델링, 관계 모델링 및 생성적 상식 추론과 같은 다양한 개체 및 관계 작업을 용이하게 한다.
    3. 이 모델은 사전을 참조하는 것과 같이 사람들이 개체와 관계를 이해하기 위해 자연어 설명을 활용하고, 개체 간의 관계를 표현하기 위해 문장을 생성하는 방법을 사용한다.

###### The Linearity of the Effect of Surprisal on Reading Times across Languages (https://aclanthology.org/2023.findings-emnlp.1052/)
- Anthology ID: 2023.findings-emnlp.1052 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "심리 언어학에서는 '놀람 이론'이라는 것이 있는데, 사람이 문맥에 따라 단어를 처리하는데 사용하는 노력은 해당 단어의 놀람과 긍정적으로 상관관계를 가진다고 한다."
    2. "이 논문에서는 이전 연구들이 영어에 초점을 맞춰 조사한 놀람의 독서 시간에 대한 선형성을 보완해서, 7개의 언어(덴마크어, 네덜란드어, 영어, 독일어, 일본어, 중국어, 러시아어)의 시선 추적 말뭉치를 분석하는 것으로 연장한다."
    3. "우리는 일부 언어에서 초선형성을 관찰할 수 있었으나, 결과는 놀람을 추정하기 위해 어떤 언어 모델을 사용했느냐에 따라 크게 영향을 받는다."

###### Adversarial Text Generation by Search and Learning (https://aclanthology.org/2023.findings-emnlp.1053/)
- Anthology ID: 2023.findings-emnlp.1053 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구에서는 텍스트 공격 방법을 사용하여 자연어 처리 모델의 강건성을 평가하는 것이 중요하다는 것이 밝혀졌습니다. 그러나 대부분의 기존 텍스트 공격 방법은 단어 수준에서 대체 단어를 생성하기 위해 휴리스틱 대체 전략 또는 언어 모델만을 사용합니다. 공격 성공률을 높이는 맹목적 추구는 생성된 적대적인 텍스트의 품질을 보장하기 어렵게 합니다.
    2. 이 연구는 블랙 박스 텍스트 공격을 비지도 텍스트 생성 문제로 처리하고, 검색과 학습을 통한 Adversarial Text Generation by Search and Learning (ATGSL)를 위한 검색 및 학습 프레임워크를 제안합니다. 이를 위해 세 가지 적대적 공격 방법(ATGSL-SA, ATGSL-BM, ATGSL-FUSION)을 개발합니다.
    3. 우리는 우선 휴리스틱 검색 공격 알고리즘 (ATGSL-SA)과 언어 동의어집을 적용하여 의미적 유사성이 높은 적대적 샘플을 생성합니다. 그 후 이 과정을 거치고 검색 노이즈를 완화하면서 검색 결과로부터 조건부 생성 모델을 학습시킵니다. 또한 텍스트 생성기를 기반으로 효율적인 ATGSL-BM 공격 알고리즘을 설계합니다. 더 나아가 ATGSL-SA와 ATGSL-BM의 장점을 통합하여 공격 효과를 높이는 하이브리드 공격 방법 (ATGSL-FUSION)을 제안합니다. 제안된 공격 알고리즘은 공격 효율성과 적대적 텍스트 품질 측면에서 가장 진보된 방법보다 크게 우수합니다.

###### Measuring Pointwise 𝒱-Usable Information In-Context-ly (https://aclanthology.org/2023.findings-emnlp.1054/)
- Anthology ID: 2023.findings-emnlp.1054 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "인-컨텍스트 학습 (ICL)은 대규모 언어 모델의 발전과 함께 인기있는 새로운 학습 패러다임이다. 본 연구에서는 최근 제안된 hardness metric인 pointwise 𝒱-usable information (PVI)를 인-컨텍스트 버전으로 적용한다. 인-컨텍스트 PVI는 원래 PVI에 비해 더 효율적으로 동작하며 몇 개의 예시만을 필요로 하고 fine-tuning이 필요하지 않는다."
    2. "우리는 인-컨텍스트 PVI의 신뢰성을 평가하기 위해 포괄적인 실험 분석을 수행하였다. 결과로써, 인-컨텍스트 PVI 추정치가 원래 PVI와 유사한 특성을 가짐을 보였다. 특히 인-컨텍스트 환경에서 인-컨텍스트 PVI 추정치는 다양한 예시 선택 및 샷 수에 걸쳐 일관성을 유지한다는 것을 보여준다."
    3. "또한, 우리는 인-컨텍스트 PVI를 활용하여 어려운 문제를 식별하는 방법을 보여준다. 우리의 연구는 인-컨텍스트 PVI의 잠재력을 강조하며 ICL의 능력에 대한 새로운 통찰력을 제시한다."

###### SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities (https://aclanthology.org/2023.findings-emnlp.1055/)
- Anthology ID: 2023.findings-emnlp.1055 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Multi-modal large language models은 AGI 달성을 위한 중요한 단계로 간주되고, Cascade 패러다임으로 동작하는 현재의 음성-언어 모델들은 inter-modal 지식 전달을 방해한다. 
    2. 본 논문에서는 SpeechGPT라는 큰 규모의 다중 모달 언어 모델을 제안하며, 이 모델은 다중 모달 콘텐츠를 인식하고 생성할 수 있는 내재적인 교차 모달 대화 능력을 갖춘다. 
    3. 실험 결과는 SpeechGPT가 교차 모달 인간 지시를 따라갈 수 있는 능력을 갖추고, 하나의 모델로 여러 모달리티를 다룰 수 있는 잠재력을 강조한다.

###### Unleashing the Multilingual Encoder Potential: Boosting Zero-Shot Performance via Probability Calibration (https://aclanthology.org/2023.findings-emnlp.1056/)
- Anthology ID: 2023.findings-emnlp.1056 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습된 다국어 인코더 모델은 크로스-언어 작업이나 언어 분석을 할 수 있는데, 라벨 단어를 예측하여 모델 매개변수를 갱신할 필요 없이 입력 예시를 클로즈 스타일로 바꾸면 된다.
    2. 그러나 이 방법의 성능은 사전 학습 단계에서 빈도가 높은 라벨 단어를 예측하는 모델의 편향으로 인해 제한된다.
    3. 우리는 이 문제를 해결하기 위해 모델이 예측하는 라벨 단어의 확률을 수정하는 보정 기법을 사용하였고, 이러한 보정 기법을 적용한 다국어 인코더는 다양한 작업에서 상당한 성능 향상을 보였다.

###### A Thorough Examination on Zero-shot Dense Retrieval (https://aclanthology.org/2023.findings-emnlp.1057/)
- Anthology ID: 2023.findings-emnlp.1057 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 강력한 pre-trained language models (PLM)를 기반으로 한 dense retrieval (DR)은 벤치마크 데이터셋에서 우수한 성능을 보여주었으나, zero-shot retrieval 설정에서는 전통적인 sparse retrieval 모델 (예: BM25)보다 경쟁력이 부족하다는 것이 밝혀져 있다.
    2. 이 연구에서는 DR 모델의 zero-shot 능력에 대한 철저한 분석을 제시한다. 출처 트레이닝 세트와 관련된 여러 핵심 요소의 영향, 대상 데이터셋으로부터의 잠재적 편향, 그리고 기존의 zero-shot DR 모델들을 분석하고 비교한다.
    3. 이 연구 결과는 zero-shot DR 모델을 이해하고 발전시키기 위한 중요한 증거를 제시한다.

###### Contrastive Pre-training for Personalized Expert Finding (https://aclanthology.org/2023.findings-emnlp.1058/)
- Anthology ID: 2023.findings-emnlp.1058 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Community Question Answering (CQA)에서는 전문가를 신속하게 찾아 특정 질문에 답변할 수 있는 능력이 중요하다. 따라서 질문 텍스트 기사에 따라 전문가와 질문의 정확한 표현을 학습하는 것이 필수적이다.
    2. 이 논문에서는 미세 조정(fine-tuning) 방식으로 사전 교육(pre-training)된 모델을 사용하여 CQA를 위한 Contrastive Pre-training framework for Expert Finding (CPEF)을 제안한다.
    3. 실험 결과, CPEF 방법론은 다양한 실제 데이터셋에서 우수한 성능을 달성할 수 있음을 보여준다.

###### Mitigating Intrinsic Named Entity-Related Hallucinations of Abstractive Text Summarization (https://aclanthology.org/2023.findings-emnlp.1059/)
- Anthology ID: 2023.findings-emnlp.1059 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 추상적 텍스트 요약은 중요하면서도 도전적인 과제이다. 이 논문은 최근 연구 결과, 추상적 요약은 여전히 다양한 형태의 환각(hallucination)에 직면하고 있으며, 그 중 상당 부분은 named entity와 관련이 있다는 것을 보여준다.
    2. 데이터에 내재된 확실한 원인은 복잡하며 학습 조건 역시 다양하다. 이 논문은 데이터가 제기하는 다양한 학습 조건을 해결하기 위해 두 가지 entity-alignment 학습 방법을 제안한다.
    3. 실험 결과, 우리의 방법은 사용된 기준 모델과 비교하여 자동 평가 점수를 향상시켰다. 인간 평가도 우리의 방법이 사용된 기준 모델과 비교하여 내재적 named entity와 관련된 환각을 상당히 감소시킨다는 것을 보여준다.

###### Towards Informative Few-Shot Prompt with Maximum Information Gain for In-Context Learning (https://aclanthology.org/2023.findings-emnlp.1060/)
- Anthology ID: 2023.findings-emnlp.1060 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대용량 언어 모델은 적은 수의 샘플을 기반으로 새로운 downstream 태스크에서 사례 기반 학습을 수행할 수 있는 능력을 가지고 있지만, 이러한 학습 패러다임은 입력 분포, 샘플의 순서, 프롬프 형식과 같은 요인들에 의해 유발되는 variance 때문에 불안정하다.
    2. 이 논문은 이러한 요인들을 일정하게 유지해도, 랜덤으로 선택된 샘플은 여전히 높은 variance를 보인다는 것을 보여준다. 따라서 우리는 주어진 예제 후 예측을 통해 얻은 정보 이득을 측정하여 정보 이득이 최대인 샘플을 샘플링하도록 제안한다.
    3. 또한, 우리는 템플릿 편향의 존재를 확인하였으며, 이는 샘플링 과정에서 정보 이득의 공정한 평가를 방해할 수 있다. 이 편향을 완화하기 위해 Calibration Before Sampling 전략을 제안한다. 실험 결과는 우리의 제안 방법이 여섯 개의 분류 작업에서 세 가지 LLM 모델을 사용하여 평균 상대 개선율 14.3%를 제공할 수 있음을 보여준다.

