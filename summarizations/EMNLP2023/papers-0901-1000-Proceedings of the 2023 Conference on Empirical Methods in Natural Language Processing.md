# Korean Three-Line Summarizations of Papers 901-1000 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### Bridging Continuous and Discrete Spaces: Interpretable Sentence Representation Learning via Compositional Operations (https://aclanthology.org/2023.emnlp-main.900/)
- Anthology ID: 2023.emnlp-main.900 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 문장 임베딩 모델은 문장의 의미 유사도와 같은 유용한 속성을 캡처하기 위해 문장을 벡터 표현으로 인코딩하지만, 문장의 구성적 의미는 문장 유사도 외에도 문장 융합 또는 차이와 같은 구성 작업을 통해 해석될 수 있다. 
    2. 이 연구에서는 구성적인 문장 의미가 임베딩 공간에서 구성적인 작업으로 직접 반영될 수 있는지 조사한다. 
    3. 우리는 문장 임베딩 공간에서 구성적인 문장 작업을 지원하는 해석 가능한 문장 임베딩을 학습하기 위한 end-to-end 프레임워크인 InterSent를 제안한다.

###### Outlier Dimensions Encode Task Specific Knowledge (https://aclanthology.org/2023.emnlp-main.901/)
- Anthology ID: 2023.emnlp-main.901 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large Language Model, LLM)의 표현은 소수의 차원이 지나치게 높은 분산으로 지배된다고 알려져 있다. 
    2. 우리는 fine-tuning이 outlier dimensions에 어떤 영향을 미치는지 조사하였고, 1) pre-training에서 발생한 outlier dimensions가 fine-tuned 모델에서도 지속되며 2) 단일 outlier dimension이 downstream tasks을 최소 오류율로 완료할 수 있음을 보였다. 
    3. 우리의 결과는 outlier dimensions이 중요한 task-specific knowledge를 인코딩할 수도 있으며, downstream 모델의 결정에는 단일 outlier dimension의 표현 값이 영향을 미칠 수 있다는 것을 시사한다.

###### Hi-ArG: Exploring the Integration of Hierarchical Argumentation Graphs in Language Pretraining (https://aclanthology.org/2023.emnlp-main.902/)
- Anthology ID: 2023.emnlp-main.902 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 그래프는 지식을 저장하고 표현하는 구조이며, 최근의 연구들은 이를 언어 모델의 다양한 응용에 도움을 주는 능력에 대해 논의하고 있다.
    2. 해당 논문에서는 텍스트-그래프 멀티모달 모델 GreaseArG와 그래프 정보를 사용한 새로운 pre-training 프레임워크를 소개하며, 그래프를 활용하는 두 가지 접근 방식을 제안한다.
    3. 실험 결과, GreaseArG는 동일 규모의 언어 모델보다 이러한 태스크에서 뛰어난 성능을 보이며, 그래프 정보를 추가적인 pre-training 동안 사용하는 것은 기본 언어 모델의 성능을 개선할 수 있다는 것을 보여준다.

###### Biomedical Named Entity Recognition via Dictionary-based Synonym Generalization (https://aclanthology.org/2023.emnlp-main.903/)
- Anthology ID: 2023.emnlp-main.903 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 바이오 의학 자연어 처리에서 생체명 개체 인식은 핵심 과제 중 하나이다. 이 논문은 개체 인식을 위해 사전 기반 접근 방법을 제안하며, 이러한 방법은 주어진 사전을 기반으로 개체를 추출한다. 그러나 기존의 사전 기반 접근 방법은 주어진 사전에 나열되지 않은 동의어를 식별하는 데 어려움이 있다. 
    
    2. 본 연구에서는 입력 텍스트에 포함된 의학 개념을 스팬 기반 예측을 사용하여 인식하기 위한 SynGen 프레임워크를 제안한다. 이 방법은 동의어 일반화 오류를 최소화하기 위해 (1) 동의어 거리 조절자와 (2) 노이즈 개입 조절자라는 두 가지 규제항을 도입한다. 
    
    3. 실험 결과를 통해 SynGen이 이전의 사전 기반 모델보다 뛰어난 성능을 보여주고, 동의어 일반화 오류의 한계를 상세히 분석하였다.

###### GNAT: A General Narrative Alignment Tool (https://aclanthology.org/2023.emnlp-main.904/)
- Anthology ID: 2023.emnlp-main.904 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 알고리즘적 시퀀스 정렬은 문서 쌍 사이에서 공유되는 유사한 세그먼트를 식별하며, 많은 NLP 태스크에서 기본적인 역할을 한다. 하지만 번역이나 서술의 서로 먼 버전과 같은 내러티브 사이의 유사성을 인식하는 것은 어렵다. 특히 요약본과 축약본은 원래 소설보다 훨씬 짧은 길이이기 때문이다.
    2. 우리는 생물 정보학에서의 Smith-Waterman 알고리즘과 현대적인 텍스트 유사성 메트릭을 결합하는 일반적인 내러티브 정렬 접근법을 개발했다. 우리는 정렬 점수의 배경이 Gumbel 분포에 맞아 매칭의 유의성에 대한 엄격한 p-값을 정의할 수 있도록 한다.
    3. 우리는 요약과 책 정렬, 번역된 책 정렬, 짧은 이야기 정렬, 그리고 표절 감지라는 서로 다른 길이의 문서를 가진 네 개의 문제 도메인에서 일반적인 내러티브 정렬 도구(GNAT)를 적용하고 평가하여 우리의 방법의 성능과 효과를 입증하였다.

###### Self-Ensemble of N-best Generation Hypotheses by Lexically Constrained Decoding (https://aclanthology.org/2023.emnlp-main.905/)
- Anthology ID: 2023.emnlp-main.905 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 생성을 개선하기 위해 N-best 가설을 앙상블하는 방법을 제안하였다. 기존의 연구들은 N-best 후보들을 명시적으로 재정렬하여 생성 품질을 향상시키는데 성공하였다. 하지만 이러한 연구들은 더 높은 품질의 가설이 존재한다고 가정한다. 
    2. 우리는 이 가정을 보다 실용적으로 확장하여 N-best 내에서 부분적으로 더 높은 품질의 가설이 존재하지만 전체 문장은 완벽하지 않을 수 있다고 가정했다. 
    3. 이 논문에서는 이러한 높은 품질의 조각들을 결합하여 단일 최고 품질의 문장보다 더 높은 품질의 출력을 얻을 수 있다고 제안하고, 이를 위해 N-best 가설을 얻고 토큰 수준의 품질 평가를 수행하였다. 그리고 최종 출력에 포함되어야 할 토큰과 포함되지 말아야 할 토큰을 디코딩 과정에서 어휘 제약으로 적용하였다.

###### UniChart: A Universal Vision-language Pretrained Model for Chart Comprehension and Reasoning (https://aclanthology.org/2023.emnlp-main.906/)
- Anthology ID: 2023.emnlp-main.906 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 차트는 복잡한 데이터를 시각적으로 표현하고 해석하는 데 널리 사용되지만, 자연어를 사용한 차트 기반 데이터 분석을 위한 기존 방법들은 차트 구조를 명시적으로 모델링하지 않고 언어나 시각-언어 태스크에 대해 사전 학습에 의존하고 있다.
    2. 이 논문에서는 다양한 주제와 시각 스타일을 포함하는 큰 규모의 차트 코퍼스를 구축하고, 차트 이해와 추론을 위한 사전 훈련 모델 UniChart를 제안한다.
    3. UniChart는 차트의 관련 텍스트, 데이터 및 시각 요소를 인코딩하고, 차트에 기반한 텍스트 생성을 위해 차트-기반 텍스트 디코더를 사용한다. 사전 훈련된 UniChart는 다양한 하위 태스크에서 최고의 성능을 보이며, 이전 방법보다 뛰어난 일반화 능력을 가지고 있다.

###### Merging Experts into One: Improving Computational Efficiency of Mixture of Experts (https://aclanthology.org/2023.emnlp-main.907/)
- Anthology ID: 2023.emnlp-main.907 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델의 크기를 확장하면 NLP 태스크에서 혁신적인 발전이 있을 수 있지만, 이는 컴퓨팅 비용이 증가하는 대가와 함께 온다. 
    2. 이 논문에서는 여러 개의 전문가 중에서 하나의 전문가를 활성화하여 계산 비용을 줄이는 Sparse Mixture of Experts (MoE) 방법을 제안한다. 
    3. 토큰 수준의 MEO의 효율성과 성능을 향상시키는 토큰 수준 어텐션 블록을 제안하며, 그러한 방법이 GLUE 벤치마크에서 최적의 성적을 보여주었다.

###### Distance-Based Propagation for Efficient Knowledge Graph Reasoning (https://aclanthology.org/2023.emnlp-main.908/)
- Anthology ID: 2023.emnlp-main.908 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 그래프 완성은 (KGs)지식 그래프에서 보이지 않는 엣지를 예측하여 새로운 사실을 발견하는 것을 목표로 한다. 
    2. 최근에는 경로 정보를 집계하는 방법들이 제안되어 이 문제를 해결하고 있다. 그러나, 이러한 방법들은 효율성 문제로 시달리고 있다.
    3. 본 논문에서는 태그넷(TAGNet)을 소개하여 효율적인 정보 전파를 가능하게 한다. 다양한 KG 데이터셋에서 성능을 가져가면서 전달된 메시지 수를 90%까지 줄일 수 있음을 실험으로 입증하였다.

###### What to Read in a Contract? Party-Specific Summarization of Legal Obligations, Entitlements, and Prohibitions (https://aclanthology.org/2023.emnlp-main.909/)
- Anthology ID: 2023.emnlp-main.909 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 법적 계약서의 핵심 의무, 권리, 금지사항을 검토하고 이해하는 것은 계약서의 길이와 도메인 특수성으로 인해 지루한 작업일 수 있다.
    2. 이 논문에서는 당사자별 추출 요약(party-specific extractive summarization)을 통해 계약서의 의무와 권리를 빠르게 검토하고 이해를 돕는 새로운 작업을 제안한다.
    3. 이를 위해 임차계약서에서 추출된 의무, 권리 및 금지사항에 대한 파티별로 구성된 데이터셋을 사용하여 파티별 계약 요약을 생성한다.

###### Enhancing Computation Efficiency in Large Language Models through Weight and Activation Quantization (https://aclanthology.org/2023.emnlp-main.910/)
- Anthology ID: 2023.emnlp-main.910 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large Language Models)은 자연어 처리 태스크에서 뛰어난 성능을 보이지만, 많은 파라미터와 연산량으로 인해 배포가 제한되는 경우가 많다.
    2. 본 논문은 4-bit weight와 8-bit activation(W4A8) 양자화를 통해 계산 효율성을 향상시키는 후처리 양자화(post-training quantization)에 초점을 맞추고 있다.
    3. AQAS와 SLAC 두 가지 혁신적인 방법을 제시하여 가중치와 활성화의 결합 효과를 고려하고, 보정 시퀀스 길이를 목표 작업에 맞추어 PTQ를 향상시키는 것을 보여준다.

###### CP-BCS: Binary Code Summarization Guided by Control Flow Graph and Pseudo Code (https://aclanthology.org/2023.emnlp-main.911/)
- Anthology ID: 2023.emnlp-main.911 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 바이너리 함수에 대한 요약문을 자동으로 생성하는 것은 매우 가치있는 작업이지만, 저수준 언어 (어셈블리 코드)의 실행 동작과 의미를 인간이 읽을 수 있는 자연어로 번역하는 것은 어려운 작업이다.
    2. 기존의 어셈블리 코드 이해 작업은 주로 함수 이름을 생성하는 것에 초점을 맞추어 왔지만, 여전히 혼동을 줄 수 있는 다양한 약어들을 포함하고 있어 이를 극복하기 위해 바이너리 함수에 대한 완전한 요약 생성에 초점을 맞춘다.
    3. CP-BCS라고 불리는 제안된 프레임워크는 제어 흐름 그래프와 의사 코드를 활용하여 전문가 지식을 통해 바이너리 함수의 실행 동작과 논리 의미를 포괄적으로 학습하고 이를 개선할 수 있다는 결과를 보여준다.

###### Assessing Step-by-Step Reasoning against Lexical Negation: A Case Study on Syllogism (https://aclanthology.org/2023.emnlp-main.912/)
- Anthology ID: 2023.emnlp-main.912 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 CoT (chain-of-thought) 프롬프팅과 같은 단계별 추론 지시에 기초하여, 이러한 모델이 CoT 스타일 추론을 얼마나 강력하게 수행하는지 알아보는 것이 중요하다.
    2. 이 연구에서는 언어 모델의 단계별 추론 능력을 부정이라는 어려운 언어 현상에 초점을 맞춰 조사한다. 이를 위해 가상의 개체를 기준으로 많은 조절된 설정을 도입하여 모델의 논리적 추론 능력을 평가한다.
    3. 우리는 몇몇 최신 LLM들이 CoT 스타일 추론을 수행할 때 어휘적 부정 (예: possible→impossible)에 대해 강력하지 못하며, 결과는 각 LLM 패밀리마다 독특한 한계를 강조한다.

###### Chain-of-Thought Tuning: Masked Language Models can also Think Step By Step in Natural Language Understanding (https://aclanthology.org/2023.emnlp-main.913/)
- Anthology ID: 2023.emnlp-main.913 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Chain-of-Thought (CoT)은 Large Language Models (LLMs)가 복잡한 작업을 중간 단계의 자연어형식으로 멀티스텝 추론을 통해 단계적으로 풀 수 있도록 안내하는 기술이다. CoT는 LLMs이 단계별로 생각할 수 있게 한다. 하지만, 많은 Natural Language Understanding (NLU) 태스크에서도 단계별 생각이 필요하지만, LLMs는 소규모 Masked Language Models (MLMs)보다 성능이 낮다. 이 논문에서는 LLMs에서 MLMs로 CoT를 이전시키기 위해 prompt tuning에 기반한 two-step 추론 프레임워크인 Chain-of-Thought Tuning (CoTT)을 제안한다.
    2. CoT를 바탕으로 한 CoTT의 two-step 프레임워크는 MLMs가 작업 분해를 구현할 수 있게 해주고, prompt tuning을 통해 중간 단계가 자연어 형식으로 사용될 수 있다. 이를 통해 CoT의 성공을 MLMs을 통해 NLU 태스크로 확장할 수 있다.
    3. CoTT의 효과를 검증하기 위해 계층적 분류(hierarchical classification)와 관계 추출(relation extraction) 두 가지 NLU 태스크에서 실험을 수행하였으며, 결과는 CoTT가 기준 모델보다 우수한 성능을 달성하며 최첨단 수준의 성능을 보여준다.

###### Large Language Models are Complex Table Parsers (https://aclanthology.org/2023.emnlp-main.914/)
- Anthology ID: 2023.emnlp-main.914 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. GPT-3.5 기반의 일반적인 QA 작업에 중점을 둔 QA 연구들이 복잡한 테이블 QA의 독특한 도전 요소들을 간과하고 있다. 
    2. 이 논문에서는 복잡한 테이블 QA에 대응하기 위해 GPT-3.5를 활용하여 테이블을 튜플 형태로 재구성하고 대화형 프롬프트 디자인을 적용하는 방식을 제안한다. 
    3. 실험 결과, 우리의 접근 방식은 HiTAB와 AIT-QA라는 복잡한 테이블 QA 데이터셋에서 이전 연구에 비해 우월한 성능을 보여주며 SOTA 성능을 기록하였다.

###### R2H: Building Multimodal Navigation Helpers that Respond to Help Requests (https://aclanthology.org/2023.emnlp-main.915/)
- Anthology ID: 2023.emnlp-main.915 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인공지능 네비게이션 도우미 에이전트는 환경 인식과 대화 능력을 통해 사용자를 알 수 없는 지역에서 안내하는 데에 매우 중요하다. 이 연구에서는 기존의 다중 모달 대화 지향 임베디드 데이터셋을 활용하여 도움 요청에 응답할 수 있는 네비게이션 도우미 에이전트 개발을 촉진하기 위한 새로운 벤치마크인 R2H를 소개한다. 
    2. 이 R2H 벤치마크에는 대화 히스토리를 기반으로 정보성 있는 응답을 생성하는 능력을 평가하는 "Respond to Dialog History (RDH)"와 작업 수행자와의 일관된 협력 과정에서 응답의 효과성과 효율성을 평가하는 "Respond during Interaction (RdI)"라는 두 가지 작업이 포함되어 있다.
    3. 또한, "SeeRee"라고 명명된 시각적 정보를 볼 수 있고 응답할 수 있는 혁신적인 task-oriented 다중 모달 응답 생성 모델을 fine-tuning하거나, 제로샷 방식으로 다중 모달 대형 언어 모델을 사용하여 네비게이션 도우미 에이전트를 구축하는 두 가지 접근 방식에 대해 탐구했다. 이를 자동 벤치마크와 인간 평가를 기반으로 분석하였다.

###### Speech-enriched Memory for Inference-time Adaptation of ASR Models to Word Dictionaries (https://aclanthology.org/2023.emnlp-main.916/)
- Anthology ID: 2023.emnlp-main.916 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대부분의 시험에서 ASR 모델의 성능은 탁월하지만 희귀 단어에서는 만족스럽지 않다.
    2. 우리는 새로운 추론 알고리즘을 제안하여 특정 도메인의 용어와 일치시켜 ASR 모델의 예측을 개선한다.
    3. 우리의 실험에서는 희귀 단어 인식을 크게 개선할 수 있는 것으로 나타났다.

###### Generative Table Pre-training Empowers Models for Tabular Prediction (https://aclanthology.org/2023.emnlp-main.917/)
- Anthology ID: 2023.emnlp-main.917 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 table pre-training의 주제에는 상당한 연구 관심이 집중되고 있지만, table pre-training을 이용하여 태블라 예측의 성능을 향상시키는 방법은 여전히 열린 과제이다.
    2. 우리는 TapTap을 제안하여 table pre-training을 활용하고 처음으로 모델을 강화시켜 태블라 예측을 수행하는데 사용한다. 
    3. TapTap은 대량의 실제 세계 태블라 데이터로 사전 훈련을 수행한 후, 고품질의 합성 테이블을 생성하여 태블라 데이터와 관련된 다양한 응용 분야에서 사용할 수 있다.

###### Learning to Describe for Predicting Zero-shot Drug-Drug Interactions (https://aclanthology.org/2023.emnlp-main.918/)
- Anthology ID: 2023.emnlp-main.918 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 음용된 약의 상호작용(adverse drug-drug interactions, DDIs)은 동시 투약의 효과를 약화시켜 건강 관리에 큰 도전을 제기한다. 
    2. 기존 DDI 예측 방법은 새로운 약의 경계를 초과하는 경우 상호작용을 잡아내지 못할 수 있다. 
    3. 이 논문에서는 새로운 약에 대한 정확한 DDI 예측을 위해 DrugBank, PubChem과 같은 온라인 데이터베이스에서 얻은 텍스트 정보를 기반으로 TextDDI 접근법을 제안한다.

###### A Simple Baseline for Knowledge-Based Visual Question Answering (https://aclanthology.org/2023.emnlp-main.919/)
- Anthology ID: 2023.emnlp-main.919 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 연구들은 외부 데이터베이스와 LLM을 통해 명시적 지식과 암묵적 지식을 효과적으로 활용하여 외부 지식이 필요한 질문에 대답하는 것의 중요성을 강조하고 있다. 그러나 이러한 접근 방식은 복잡한 파이프라인으로 구성되어 GPT-3 API에 많이 의존한다는 단점이 있다.
    2. 본 논문의 주요 기여는 간단하고 재현성이 높은 파이프라인을 제안하는 것이다. 이 파이프라인은 질문에 관련된 캡션을 문맥 정보로 사용하는 효율적인 in-context learning에 기반한다.
    3. 우리의 방법은 훈련 과정이 필요 없으며 외부 데이터베이스나 API에 접근할 필요가 없지만, OK-VQA와 A-OK-VQA 데이터셋에서 최첨단 정확도를 달성한다.

###### Unveiling the Essence of Poetry: Introducing a Comprehensive Dataset and Benchmark for Poem Summarization (https://aclanthology.org/2023.emnlp-main.920/)
- Anthology ID: 2023.emnlp-main.920 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 처리 분야의 연구는 창의적인 언어 생성에서 상당한 발전이 있었지만, 언어 모델이 창의적인 언어의 의도된 의미를 해석할 수 있는지에 대한 질문은 여전히 답이 없다.
    2. 시는 깊은 의미를 지니고 있기 때문에, 시의 요약은 단순한 문장의 의미만을 고려한다면 의도와 메시지를 잃어버릴 수 있기 때문에 도전적인 작업이다.
    3. 이 논문에서는 'Poem Summarization'이라는 자연어 이해 분야의 새로운 작업을 제안하고, 이 작업을 위한 첫 번째 데이터셋 'PoemSum'을 소개하며, 최신의 요약 모델들의 성능을 벤치마킹하고 그 한계점에 대해 관찰 결과를 제시한다.

###### Privacy Implications of Retrieval-Based Language Models (https://aclanthology.org/2023.emnlp-main.921/)
- Anthology ID: 2023.emnlp-main.921 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 검색 기반 언어 모델은 외부 데이터 스토어에서 검색된 텍스트를 통합함으로써 인터프리터블성, 사실성 및 적응성이 향상되었다. 그러나, 검색 기반 언어 모델이 개인 데이터 유출에 어떤 영향을 미치는지에 대해서는 여전히 불명확하다.  
    2. 이 논문에서는 개인 정보가 중요한 도메인에서 유용성과 개인정보 보호 사이의 균형을 찾기 위해 최적의 설계와 훈련 절차를 탐색하기 위한 개인 정보 유출의 초기 연구를 제시한다. 
    3. 실험 결과, kNN-LM은 개인 데이터 스토어로부터 개인 정보가 유출될 가능성이 파라메터 모델보다 크다는 것을 발견했으며, 개인 정보가 텍스트에서 명확하게 탐지될 때는 간단한 살균 단계만으로 위험성을 제거할 수 있다는 것을 알아냈다.

###### IMTLab: An Open-Source Platform for Building, Evaluating, and Diagnosing Interactive Machine Translation Systems (https://aclanthology.org/2023.emnlp-main.922/)
- Anthology ID: 2023.emnlp-main.922 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. IMTLab은 최신 모델을 이용하여 IMT 시스템을 빠르게 구축하고, 시스템의 약점을 진단할 수 있는 오픈 소스의 end-to-end 대화형 기계 번역(IMT) 시스템 플랫폼이다. 
    2. IMTLab은 전체 대화형 번역 과정을 인간이 참여하는 task-oriented 대화로 다루며, 고품질 및 오류없는 번역을 위해 인간의 개입을 명시적으로 포함할 수 있다. 
    3. 시뮬레이션 및 수동 실험을 통해 IMTLab을 활용하여 다른 IMT 시스템을 체계적으로 평가해 본 결과, BiTIIMT이 더 나은 대화 경험과 함께 수정 비용을 비슷하게 달성하는 반면, prefix-constrained decoding 방법이 end-to-end 평가에서 가장 낮은 편집 비용을 얻는다는 것을 알 수 있었다.

###### Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents (https://aclanthology.org/2023.emnlp-main.923/)
- Anthology ID: 2023.emnlp-main.923 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 LLM(대형 언어 모델)은 정보 검색(IR)에서 대체로 생성 기능을 활용하였으나, 본 논문에서는 기존 IR 벤치마크에서 최신 지식을 검색할 수 있는 능력을 검증하기 위한 새로운 테스트 세트인 NovelEval을 수집하였다.
    2. 또한, 실제 응용에서 효율성을 향상시키기 위해 ChatGPT의 순열 증류 방법을 사용하여 작고 특화된 모델로 ChatGPT의 순위 지정 능력을 전달하는 가능성을 탐구하였다.
    3. 만들어진 440M 순위 지정 모델은 3B 지도 모델보다 BEIR 벤치마크에서 우월한 결과를 보여주었다.

###### DiNeR: A Large Realistic Dataset for Evaluating Compositional Generalization (https://aclanthology.org/2023.emnlp-main.924/)
- Anthology ID: 2023.emnlp-main.924 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 구성적 일반화 데이터셋은 합성 생성으로 인해 자연어 다양성이 부족한 문제가 있다.
    2. 이 논문에서는 DiNeR(DIsh NamE Recognition) 과제를 제시하여 식품, 동작, 맛의 다양한 조합으로 이루어진 음식 이름을 인식하는 모델을 만들기 위한 중국어 데이터셋을 만들었다. 
    3. 이 작업은 구성적 일반화에 대한 힘든 과제와 이를 해결하기 위한 기준선 방법 및 음식 이름 인식의 문맥에서 구성적 일반화에 대한 통찰력을 제공한다.

###### Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions? (https://aclanthology.org/2023.emnlp-main.925/)
- Anthology ID: 2023.emnlp-main.925 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 훈련된 비전 및 언어 모델은 시각적인 정보만으로 답변이 불가능하고 지식에 기반한 정보를 요구하는 질문에 대답할 수 있는 능력을 가지고 있는지 여전히 분명하지 않다.
    2. 이 연구에서는 공통 감각적 지식으로만 대답할 수 없는 정보 탐색을 위한 시각적인 질문에 대한 데이터셋인 InfoSeek를 소개한다.
    3. InfoSeek를 사용하여 다양한 사전 훈련된 시각적 질문 응답 모델을 분석하고, 성능을 향상시키기 위해 정확한 시각적 엔티티 인식을 활용하는 방법을 보여준다.

###### EDeR: Towards Understanding Dependency Relations Between Events (https://aclanthology.org/2023.emnlp-main.926/)
- Anthology ID: 2023.emnlp-main.926 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 관계 추출은 NLP와 IR에서 중요한 작업인데, 이전 연구는 이벤트 간의 계층, 시간 및 인과관계에 초점을 맞추었다. 그러나 이들은 문법과 의미론에서 이벤트가 독립적이라고 가정하기 때문에 이벤트 간의 상호 의존성을 인식하지 못한다.
    2. 이를 해결하기 위해 우리는 인간 주석으로 된 Event Dependency Relation 데이터셋 (EDeR)을 소개한다. 이 데이터셋은 OntoNotes 데이터셋의 문서 샘플에 주석을 달아 구성되어 있다.
    3. 우리는 EDeR의 이벤트 의존성 관계 예측을 위한 기준선 접근 방법을 조사하고, 이벤트 의존성 관계를 인식하는 것이 의미역 라벨링 및 공조참조 해결과 같은 중요한 NLP 작업에 도움이 될 수 있음을 보여준다.

###### It Ain’t Over: A Multi-aspect Diverse Math Word Problem Dataset (https://aclanthology.org/2023.emnlp-main.927/)
- Anthology ID: 2023.emnlp-main.927 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 수학 워드 프로블럼은 자연어 이해와 논리적 추론이 필요한 복잡한 작업이다. 이전 연구들은 다양한 MWP 데이터셋을 제공했지만, 문제 유형, 어휘 사용 패턴, 언어, 중간 솔루션에 대한 주석 등 다양성이 부족하다.
    2. 이 논문은 DMath (다양한 수학 워드 프로블렘)이라는 새로운 데이터셋을 소개하여, 문제 유형, 어휘 사용 패턴, 언어, 중간 솔루션 등에서 다양성을 제공한다.
    3. 실험 결과, DMath 데이터셋은 대형 언어 모델의 능력을 평가하기 위한 새로운 기회를 제공하며, 예를 들어 GPT-4는 DMath 데이터셋에서 약 75%의 정확도만을 달성한다고 보여주었다.

###### Dr ChatGPT tell me what I want to hear: How different prompts impact health answer correctness (https://aclanthology.org/2023.emnlp-main.928/)
- Anthology ID: 2023.emnlp-main.928 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 ChatGPT가 건강 정보 탐색에 사용될 때 다른 프롬프트가 모델의 동작에 미치는 중요한 영향을 조사한다. 특히, 건강과 같이 부정확한 답변이 심각한 결과를 초래할 수 있는 도메인에서, ChatGPT와 같은 큰 언어 모델(LLMs)에 대한 모델 동작을 이해하는 것이 매우 중요하다.
    2. TREC Misinformation 데이터셋을 사용하여, 우리는 ChatGPT를 실증적으로 평가하여 그 효과성을 보여주고, 프롬프트에 포함된 지식이 답변의 정확성을 해치는 모델 편향을 밝힌다.
    3. 이 연구는 생성형 대형 언어 모델에 기반한 보다 견고하고 투명한 질문-답변 시스템 개발에 중요한 영향을 미친다. 프롬프트, raw 결과 파일 및 수동 분석은 https://github.com/ielab/drchatgpt-health_prompting 에서 공개되어 있다.

###### kNN-LM Does Not Improve Open-ended Text Generation (https://aclanthology.org/2023.emnlp-main.929/)
- Anthology ID: 2023.emnlp-main.929 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문에서는 interpolation 기반의 retrieval-augmented language model (LM)의 생성 품질을 연구한다. 
    2. 이러한 방법들은 kNN-LM을 포함하여 언어 모델의 다음 단어에 대한 예측 분포와 주어진 접두사에 대한 가장 관련성이 높은 retrieval들로 구성된 분포를 보간한다.
    3. 우리는 automatic evaluation metrics (예: MAUVE)와 human evaluation을 통해 측정한 대로 open-ended 생성 품질에서 상응하는 개선이 없다는 것을 발견하였으며, 추가적으로 base LM에 비해 perplexity이 증가하고 retrieval 분포의 엔트로피도 증가되는 등의 문제를 발견하였다.

###### Towards A Unified View of Sparse Feed-Forward Network in Pretraining Large Language Model (https://aclanthology.org/2023.emnlp-main.930/)
- Anthology ID: 2023.emnlp-main.930 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 스케일업을 위해 S-FFN(Mixture-of-Experts와 같은)은 입력에 의존하여 일부 FFN 파라미터만 활성화함으로써 훈련 및 추론 비용을 유지하면서 일반화 성능을 향상시킵니다.
    2. 본 논문에서는 이러한 S-FFN의 주요 구조 선택 가능성인 메모리 블록 크기와 메모리 블록 선택 방법을 분석하고, 효과와 효율성에 대한 통찰을 제공합니다.
    3. 평균된 숨은 상태로 블록을 선택하는 Avg-K 선택 방법이 기존 MoE 구조보다 낮은 혼돈도(perplexity)를 달성하는 것을 발견했습니다.

###### Exploring the Impact of Model Scaling on Parameter-Efficient Tuning (https://aclanthology.org/2023.emnlp-main.931/)
- Anthology ID: 2023.emnlp-main.931 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Parameter-efficient tuning (PET) 메소드는 훈련에 필요한 파라미터를 최소화하여 매우 큰 pre-trained language models (PLMs) 을 효과적으로 구동하는데 도움이 된다. 하지만 작은 PLM의 경우, PET 메소드 간에 성능 차이가 난다. 모델의 규모가 커질수록, 성능 차이는 크게 줄어든다."
    2. "우리는 규모 확장이 PET 메소드의 디자인 차이에 미치는 영향을 완화시키는지에 대해 탐구하기 위해 더 유연한 Arbitrary PET (APET) 메소드를 도입한다. 우리의 조사 결과, 모델 규모가 튜닝 파라미터의 위치에 미치는 영향을 완화시키고, 적은 수의 튜닝 파라미터를 최적화함으로써 전체 파라미터 fine-tuning과 성능을 비교 가능한 수준의 성능을 달성할 수 있도록 한다."
    3. "놀랍게도, 우리는 튜닝 방법이 각기 다른 작업에서 무작위 추측 성능을 능가하는데 필요한 튜닝 파라미터의 수가 비슷하다는 것을 관찰했다. 이 연구 결과는 모델 규모가 PET에 미치는 영향을 이해하는 데 도움이 되며, 서로 다른 규모의 PLM에 대해 더 효과적이고 효율적인 PET 메소드를 설계하는 데 도움이 된다."

###### STAIR: Learning Sparse Text and Image Representation in Grounded Tokens (https://aclanthology.org/2023.emnlp-main.932/)
- Anthology ID: 2023.emnlp-main.932 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이미지 및 텍스트 검색은 비전 및 언어 분야에서 다양한 실제 응용 프로그램을 가진 핵심 작업 중 하나이다. 이 논문에서는 CLIP 모델을 확장하여 텍스트와 이미지를 sparse한 토큰 공간으로 매핑하는 sparse semantic representation을 구축한다. 이 모델은 dense representation보다 더 강력하며, 기존의 정보 검색 시스템과 쉽게 통합할 수 있을 뿐만 아니라, COCO-5k 텍스트 → 이미지 및 이미지 → 텍스트 검색에서 이전의 CLIP 모델보다 상당한 성능 향상을 이룩한다.
    2. 기존의 텍스트 벡터 임베딩은 dense한 표현 영역에서 유사성을 측정하는 반면, 이 논문에서 제안하는 sparse한 semantic representation은 토큰 공간에서 이미지와 텍스트를 매핑하여 사용한다. 이렇게 구성된 STAIR 모델은 dense한 표현보다 더 나은 성능을 보여주며, 서로 다른 작업에서도 더 우수한 결과를 달성한다.
    3. STAIR 모델은 이미지넷 제로샷 및 선형 프로빙과 같은 작업에서 CLIP보다 더 나은 성능을 보였으며, 이러한 sparse한 표현은 기존의 정보 검색 시스템에 쉽게 통합할 수 있다.

###### Crossing the Threshold: Idiomatic Machine Translation through Retrieval Augmentation and Loss Weighting (https://aclanthology.org/2023.emnlp-main.933/)
- Anthology ID: 2023.emnlp-main.933 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Idioms은 일상 언어에서 흔하지만, 그 의미가 부분들의 의미로부터 유도되지 않기 때문에 번역자에게 도전이 된다. 그러나 기계 번역 시스템은 여전히 Idiomatic 표현을 번역하는 것에 어려움을 겪고 있다. 
    2. 이 논문에서는 Idiomatic 번역과 관련된 문제들을 간단한 방식으로 설명함으로써 Machine Translation 모델들이 Idiomatic 번역을 올바르게 수행하기 위한 기준점(tipping point)을 발견하였다.
    3. 이 논문에서는 Idiomatic 표현을 포함한 데이터셋을 만들고, 훈련시에 이 데이터를 활용하는 기법을 제안하여 기존의 번역 모델의 정확성을 상당히 향상시킬 수 있는 것을 확인하였다.

###### CoRec: An Easy Approach for Coordination Recognition (https://aclanthology.org/2023.emnlp-main.934/)
- Anthology ID: 2023.emnlp-main.934 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 방법들은 문장에서 협조어를 식별하고 협조 경계를 인식하기 위해 문법 파서에 의존하지만, 최신 문법 파서는 긴 복잡한 문장에서 특히 에러가 날 가능성이 높고 느리다. 
    2. 이 논문에서는 COordination RECognizer (CoRec)라는 pipeline 모델을 제안하여 문제를 효과적으로 해결한다. 
    3. 다양한 도메인의 데이터셋에서의 실험 결과는 제안된 방법의 효과적이고 효율적임을 보여주며, 추가 실험 결과는 CoRec이 downstream task에 긍정적인 영향을 주어 최신 Open IE 모델의 성과를 향상시킨다는 것을 보여준다.

###### A linear time approximation of Wasserstein distance with word embedding selection (https://aclanthology.org/2023.emnlp-main.935/)
- Anthology ID: 2023.emnlp-main.935 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Wasserstein distance는 문서 간의 중복성을 측정하는 강력한 도구이지만, cubic time을 필요로 하기 때문에 계산 비용이 큰 문제입니다."
    2. "논문에서는 feature selection과 tree approximation 접근법을 결합하여 고차원 문제를 처리하는 방법을 제안합니다."
    3. "실험 결과, 제안된 방법을 사용하여 문서 분류 작업에서 높은 성능을 달성하였습니다."

###### Exchange-of-Thought: Enhancing Large Language Model Capabilities through Cross-Model Communication (https://aclanthology.org/2023.emnlp-main.936/)
- Anthology ID: 2023.emnlp-main.936 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 Large Language Models (LLMs)는 복잡한 추론 태스크에서 Chain-of-Thought 기술을 통해 중요한 발전을 이루어왔으나, 그들의 추론은 종종 내재적인 이해력으로 제한되어 외부적인 통찰력이 부족하다. 
    2. 이를 해결하기 위해 우리는 문제 해결 도중에 모델 간의 교류를 가능케 하는 Exchange-of-Thought(EoT)라는 새로운 프레임워크를 제안한다. 
    3. 우리는 이 논문에서 각 패러다임에 따른 EoT의 커뮤니케이션 동적 및 양적 측면을 자세히 알아보며, 잘못된 추론 체인의 위험을 상쇄하기 위해 믿을 만한 신뢰도 평가 메카니즘을 구현한다.

###### Conversation Understanding using Relational Temporal Graph Neural Networks with Auxiliary Cross-Modality Interaction (https://aclanthology.org/2023.emnlp-main.937/)
- Anthology ID: 2023.emnlp-main.937 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 감정 인식은 인간 대화 이해에 중요한 작업이다. 언어, 음성 및 얼굴 표정과 같은 다중 모달 데이터 개념과 함께 더 도전적인 과제가 된다. 
    2. 기존 접근 방식은 대화에서 각 문장에 대한 감정 레이블을 예측하기 위해 전역 및 로컬 context 정보를 사용하고 있다. 
    3. 이 논문에서는 CORECT라는 새로운 신경망 프레임워크를 제안하여 대화 수준의 다중 모달 상호작용과 문장 수준의 시간적 종속성을 효과적으로 포착한다.

###### Connecting degree and polarity: An artificial language learning study (https://aclanthology.org/2023.emnlp-main.938/)
- Anthology ID: 2023.emnlp-main.938 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "우리는 사전 훈련된 언어 모델들에서 새로운 언어적 일반화 현상을 조사했습니다. 저향(adverbs)으로 표현되는 정도 수정자들 (예: 조금, 매우, 굉장히) 에 초점을 맞춰서, 수정자의 정도가 문장의 극성 감지 민감도와 관련이 있는지를 테스트하고자 했습니다."
    2. "이 연결을 조사하기 위해, 우리는 심리언어학의 인공언어학 파라다임을 신경 언어 모델에 적용했습니다. 우리의 실험 결과는, BERT가 예전부터 관찰된 언어들과 일치하게 일반화한다는 것을 시사합니다. 즉, 낮은 정도의 수정자는 긍정 극성을 선호한다는 주요한 언어적 연구들과 일치합니다."
    3. "고로, 이 연구는 사전 훈련된 언어 모델들이 단어의 정도 의미와 극성 민감도를 연결짓는 기존 언어적 관찰들을 일반화하는 경향을 갖는다는 것을 보여줍니다."

###### Prompting with Pseudo-Code Instructions (https://aclanthology.org/2023.emnlp-main.939/)
- Anthology ID: 2023.emnlp-main.939 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 자연어 지시를 사용하여 대용량 언어 모델의 능력을 효과적으로 활용하는 방법으로 주목받고 있다. 그러나 자연어의 내재된 모호성 때문에, 퍼즈도 코드와 같이 모호성이 적은 지시를 사용하면 성능을 향상시킬 수 있는 가능성이 있다.
    2. 이 논문에서는 퍼즈도 코드 지시로 프롬프팅하는 것이 사전 훈련된 언어 모델의 성능을 향상시키는 데 도움이 되는지 탐구한다. 다양한 분류, QA, 생성 언어 작업에 대한 132가지 다른 작업의 퍼즈도 코드 프롬프트 데이터셋을 수동으로 생성하고, 이러한 프롬프트를 자연어 프롬프트와 함께 사용하여 BLOOM, CodeGen 두 언어 모델 계열에서 성능을 연구했다.
    3. 실험 결과, 퍼즈도 코드 지시를 사용하면 분류 작업에서 F1 점수의 평균 증가율이 7-16 포인트이고, 모든 작업에서 ROUGE-L 점수를 12-38% 향상시켰다. 코드 코멘트, 독스트링, 퍼즈도 코드에 인코딩된 구조적 단서가 모두 성능 향상에 기여한다는 설명적 실험 연구도 포함되어 있다.

###### CRAB: Assessing the Strength of Causal Relationships Between Real-world Events (https://aclanthology.org/2023.emnlp-main.940/)
- Anthology ID: 2023.emnlp-main.940 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문에서는 사건의 원인과 결과에 대해 추론하는 것을 이해하기 위해서는 복잡한 인과관계의 네트워크를 이해할 수 있는지 알 수 없다.
    2. CRAB라는 causal reasoning 평가 벤치마크 데이터셋을 소개하여 여러 언어 모델의 성능을 측정한다.
    3. 실험 결과, 모델들은 단순한 선형 인과관계 체인보다 복잡한 인과구조에서는 인과 추론에 대해 더 부족한 성능을 보였다.

###### NORMSAGE: Multi-Lingual Multi-Cultural Norm Discovery from Conversations On-the-Fly (https://aclanthology.org/2023.emnlp-main.941/)
- Anthology ID: 2023.emnlp-main.941 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회문화적 시나리오에서 사용 가능한 행동에 대해 이해하고 추론하기 위해서는 규범에 대한 지식이 필요합니다. 규범에 대한 대부분의 컴퓨터 연구는 한 문화를 중심으로 진행되며, 비대화식 환경에서 수동으로 구축된 데이터셋을 사용합니다.
    2. 우리는 NormSage라는 새로운 프레임워크를 제안하여 다중 언어 대화에서 문화 특정 규범을 자동으로 추출합니다. NormSage는 대화에서 후보 규범을 직접 추출하고, 정확성과 관련성을 확인하기 위해 설명 가능한 자체 검증을 제공하는데 GPT-3 프롬프팅을 사용합니다.
    3. 포괄적인 실험 결과는 NormSage가 다중 언어 대화 (영어와 중국어)에서 고품질 문화 지각 규범을 추출하기 위한 접근 방식의 잠재력을 보여줍니다. 또한, 우리의 관련성 검증은 텍스트 설명과 함께 대화에 대한 규범 준수 및 위반을 평가하는 데 확장될 수 있습니다. NormSage는 생성된 설명이 사람이 작성한 품질과 일치하는 94.6%의 AUC를 달성합니다.

###### A State-Vector Framework for Dataset Effects (https://aclanthology.org/2023.emnlp-main.942/)
- Anthology ID: 2023.emnlp-main.942 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 DNN 기반 시스템의 성공은 훈련에 사용된 고품질 데이터셋의 영향이 크다. 그러나 데이터셋의 영향과 데이터셋 간 상호작용에 대한 연구는 아직 충분히 이루어지지 않았다.
    2. 우리는 상태 벡터 프레임워크를 제안하여 데이터셋의 영향을 체계적으로 연구할 수 있게 한다. 이 프레임워크는 이상적인 프로빙 테스트 결과를 기반으로 벡터 공간을 형성한다.
    3. 우리는 일부 자주 사용되는 언어 이해 데이터셋의 중요한 영향이 특정한 언어적 요소에 집중되어 있는 것을 보여준다. 또한 "spill-over" 효과를 관찰하였는데, 이는 의도한 작업과는 관련이 없어 보이는 차원에서 모델에 영향을 미칠 수 있다.

###### Challenges in Context-Aware Neural Machine Translation (https://aclanthology.org/2023.emnlp-main.943/)
- Anthology ID: 2023.emnlp-main.943 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문맥 지속적인 신경 기계 번역에 대한 이해는 문장 수준의 문맥 이상의 정보를 활용하여 문장 간 의사소통 종속성을 해결하고 문서 수준의 번역 품질을 향상시키는 패러다임을 가능하게 했지만, 대부분의 연구는 문장 수준의 시스템보다 크게 개선되고 있다고 단언할 수 없다.
    2. 이 연구에서는 문헌 수준의 번역에 관련된 여러 핵심적인 문제들을 조사하고 제시한다. 이로 인한 문제점이 의사소통 현상, 문맥 사용, 모델 구조 및 문서 수준 평가와 관련되어 있다.
    3. 이러한 문제를 해결하기 위해, 우리는 문서 수준 번역에 대해 더 실제적인 설정을 제안하며, 이를 위해 중국어-영어 소설의 새로운 데이터셋을 수집하여 향후 연구를 촉진한다.

###### Task-Adaptive Tokenization: Enhancing Long-Form Text Generation Efficacy in Mental Health and Beyond (https://aclanthology.org/2023.emnlp-main.944/)
- Anthology ID: 2023.emnlp-main.944 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 downstream task의 세부 사항에 맞게 생성 파이프라인을 조정하고, 정신건강 분야에서의 긴형식 생성을 향상시키기 위해 과제적응적 토큰화(task-adaptive tokenization)를 제안한다.
    2. 우리의 과제적응적 토큰화 접근법은 인지과학의 통찰에서 영감을 받아, 과제별 데이터를 기반으로 최적화된 샘플링 확률로 여러 결과에서 가변적인 세그멘테이션을 샘플링한다.
    3. 중국어와 영어의 심리학적 질문 응답 과제에서의 광범위한 실험을 통해, 우리의 과제적응적 토큰화 접근법이 성능 향상에 유의미한 기여를 하며 최대 60% 적은 토큰을 사용한다는 것을 알아냈다. 매우 큰 언어 모델과 함께 이러한 토큰화 접근법을 사용할 때 유망한 결과를 얻을 수 있다는 사전 실험 결과가 있다.

###### FACTIFY3M: A benchmark for multimodal fact verification with explainability through 5W Question-Answering (https://aclanthology.org/2023.emnlp-main.945/)
- Anthology ID: 2023.emnlp-main.945 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어 플랫폼에서 매일 32억 장의 이미지와 72만 시간의 비디오가 공유되는 상황에서, 다중형식의 가짜 뉴스를 대규모로 탐지하기 위해서는 효율적인 사실 검증이 필요하다.
    2. 이 논문은 FACTIFY 3M이라는 데이터셋을 소개하는데, 이는 다중형식 가짜 뉴스 데이터셋을 통해 사실 검증 도메인의 영역을 넓히고, 5W 질문-답변 개념을 통해 설명 가능성을 제공한다.
    3. 이 데이터셋의 주요 특징은 텍스트 단언문, ChatGPT로 생성된 패러프레이즈 된 단언문, 연관된 이미지, 안정적인 확산 생성 추가 이미지, 픽셀-레벨 이미지 히트맵, 5W 질문-답변 쌍, 그리고 가짜 뉴스 이야기 등이다.

###### Building Multi-domain Dialog State Trackers from Single-domain Dialogs (https://aclanthology.org/2023.emnlp-main.946/)
- Anthology ID: 2023.emnlp-main.946 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 multi-domain 대화 상태 추적(DST) 모델은 다양한 도메인의 대화에 기반을 두고 있어 도메인 관계를 정의하고 데이터를 수집하는 데 많은 수동 노력이 필요하다. 이를 대응하는 것은 도메인 조합이 없는 대화로부터 multi-domain DST 모델을 구축할 수 있도록 한 divide-and-conquer(DAC) DST 패러다임과 multi-domain 대화 합성 프레임워크를 제안한다. 
    2. DAC 패러다임은 multi-domain 대화를 DST를 위해 여러 개의 단일 도메인 대화로 분할하여, 모델이 보이지 않은 도메인 조합을 가진 대화에 대해 더 일반화할 수 있도록 한다. 
    3. 대화 합성 프레임워크는 여러 개의 관련이 있는 단일 도메인 대화를 하나의 multi-domain 대화로 병합하고, 도메인 간 관계를 모방하기 위해 대화를 수정한다. 이러한 합성된 대화는 DST 모델이 도메인 간 지식 전달을 포착하는 데 도움을 준다.

###### Specialist or Generalist? Instruction Tuning for Specific NLP Tasks (https://aclanthology.org/2023.emnlp-main.947/)
- Anthology ID: 2023.emnlp-main.947 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델 (LLM)이 다양한 자연어 처리 (NLP) 작업을 동시에 수행할 수 있는 잠재력이 광범위한 연구의 주제이다. 
    2. 본 논문에서는 일반화된 가이드라인 튜닝을 통합하는 것이 전문가 모델 구축에 기여할 수 있는지를 조사한다. 
    3. 실험 결과, 일반화된 가이드라인 튜닝이 특화된 작업의 성능을 꾸준히 향상시키는데 효과적이며, 특히 작업 특정 학습 데이터가 제한된 경우에 더욱 두드러진다. 그러나 사실적인 지식을 필요로 하는 작업에서는 시각화된 정보를 포함한 일반화 데이터가 모델의 성능에 부정적인 영향을 미치는 것으로 나타났다.

###### Making Large Language Models Better Data Creators (https://aclanthology.org/2023.emnlp-main.948/)
- Anthology ID: 2023.emnlp-main.948 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(LLMs)은 NLP 분야에서 성능을 크게 향상시켰지만, 비용, 응답 속도, 제어 능력 또는 개인 정보 보호 및 보안 문제로 인해 실전 응용에는 여전히 어려움이 있다. 이 논문에서는 LLM을 사용하여 데이터 생성하는 통합 파이프라인을 제안하며, 이는 단일 포맷 예제만으로도 다양한 작업에 적용 가능하다.
    2. 실험에서는 지시를 따르는 LLM이 비용 효율적인 데이터 생성자로 작용하며, 이러한 데이터로 훈련된 모델이 분포 밖 평가에서 (최대 17.5%까지) 인간이 레이블링한 데이터보다 더 나은 성능을 보이는 동시에 분포 내 작업에서 비슷한 성능을 유지한다.
    3. 이러한 결과는 실제 세계에서 배포되는 NLP 시스템의 탄탄성에 중요한 시사점을 제공한다.

###### Hallucination Detection for Generative Large Language Models by Bayesian Sequential Estimation (https://aclanthology.org/2023.emnlp-main.949/)
- Anthology ID: 2023.emnlp-main.949 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Big Language Models (LLMs)은 자연어 생성 분야에서 현저한 발전을 이루었으나, LLMs의 부정확하거나 비실제적인 컨텐츠 생성 ("hallucinations") 경향은 여전히 큰 도전 과제이다.
    2. 현재의 환각 탐지 방법은 많은 양의 관련 자료 검색이 필요하여 응답 시간이 증가하는 문제가 있다.
    3. 우리는 통계적 의사 결정 이론과 베이지안 순차분석을 활용하여 환각 탐지 과정에서 비용과 이익 사이의 트레이드 오프를 최적화하는 독특한 프레임워크를 소개한다.
    
    1. "Automatic MCQ generation"은 교사들의 학생 평가 시간을 크게 줄임으로써 중요한 교육 수단이 될 수 있지만, 기존 MCQ 평가 메트릭은 생성된 MCQ가 교육적인 가치를 지니는지 판단할 수 없기 때문에 제한적이다.
    2. 이 논문에서는 "지식 종속 가능성(KDA)"라고 불리는 새로운 평가 메트릭을 제안하여 MCQ의 대답 가능성과 대상 사실의 학생 지식 평가 능력을 측정한다. 
    3. 실험 결과 KDA_disc와 KDA_cont는 "KDA"와 "실제 강의실 세트에서의 사용성"과 강한 상관관계를 가지며, n-gram 기반 유사성 메트릭과 함께 사용할 때 다양한 MCQ 품질 지표에 대해 강한 예측력을 보인다.
    
    1. 최근의 deep모델은 NLP 태스크에서 뛰어난 성능을 보이지만 특정 패턴에 의존하므로 robustness가 한계가 있다. 
    2. 이 논문에서는 Contrastive Learning과 counterfactual augmentation을 활용하여 강건성(robustness)을 높이기 위한 방법을 제안한다.
    3. 기존의 augmentation 방법과는 달리 여러 개의 counterfactual을 합성하여 예측 분포를 통해 인과 관계를 신뢰할 수 있으며, 이를 통해 counterfactual의 강건성, 도메인 간 일반화, 희소 데이터 일반화의 세 가지 측면에서 큰 개선을 얻었다.

###### Guideline Learning for In-Context Information Extraction (https://aclanthology.org/2023.emnlp-main.950/)
- Anthology ID: 2023.emnlp-main.950 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델은 단지 지시사항과 몇 가지 입출력 예시에 의해 조건이 주어짐으로써 새로운 작업을 수행할 수 있으며, 어떠한 파라미터도 최적화하지 않습니다. 이를 In-Context Learning (ICL)이라고 합니다.
    2. 그러나 In-Context Information Extraction (IE)의 성능은 일반적으로 최신의 지도학습 전문 모델보다 뒤쳐지는 편입니다. 이는 작업 설명의 불명확함이 주요한 원인입니다.
    3. 이 논문에서는 In-Context IE를 위한 Guideline Learning (GL) 프레임워크를 제안하여 몇 가지 오류 사례를 기반으로 가이드라인을 자동으로 생성하고, 추론 중에 도움이 되는 가이드라인을 검색해 더 나은 ICL을 실현합니다. 또한, GL의 효율성을 향상하기 위해 자기 일관성 기반의 액티브 러닝 방법을 제안합니다. 실험 결과이벤트 추출과 관계 추출에서 GL은 In-Context IE의 성능을 크게 향상시킬 수 있습니다.

###### Open Information Extraction via Chunks (https://aclanthology.org/2023.emnlp-main.951/)
- Anthology ID: 2023.emnlp-main.951 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 OIE 시스템들은 문장을 토큰으로 나누고 토큰 범위를 튜플 관계와 인자로 인식한다. 이 논문에서는 문장을 청크(Chunk) 시퀀스로 인식하고, 청크 범위를 튜플의 관계와 인자로 인식하는 방법인 Sentence as Chunk sequence (SaC) 를 제안한다.
    2. 청크로 나누는 것이 토큰으로 나누는 것보다 OIE에 더 적합한 속성을 가지고 있다고 주장하며, CoNLL 청크, OIA 간단한 구 묶음, 명사구, 그리고 SpanOIE의 범위로 나누는 네 가지 옵션을 평가한다.
    3. 또한 SaC 위에 간단한 end-to-end BERT 기반 모델인 Chunk-OIE를 제안하여 문장 청크화와 튜플 추출을 수행하는데, 해당 모델은 다양한 OIE 데이터셋에서 최고 성능을 보이며, SaC가 OIE 작업에 이점을 제공함을 나타낸다.

###### Rethinking Word-Level Auto-Completion in Computer-Aided Translation (https://aclanthology.org/2023.emnlp-main.952/)
- Anthology ID: 2023.emnlp-main.952 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 컴퓨터 지원 번역에서 단어 수준 자동 완성(WLAC)은 중요한 역할을 한다. 기존 연구들은 복잡한 모델 구조를 설계하는데 초점을 두었지만 이 논문은 다른 관점에서 접근하여 어떤 종류의 단어가 좋은 자동 완성인지에 대한 기준을 제시한다.
    2. 우리는 이 기준에 만족하지 못하는 기존의 WLAC 모델들이 많다는 것을 발견하였고, 이를 개선하기 위한 효과적인 방법을 제안한다.
    3. 실험을 통해 우리의 접근 방식이 WMT2022의 WLAC 공유 작업에 제출된 최고 성능 시스템보다 우수한 성능을 발휘하는 것을 보여주었다.

###### Automatic Transcription of Handwritten Old Occitan Language (https://aclanthology.org/2023.emnlp-main.953/)
- Anthology ID: 2023.emnlp-main.953 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 신경망 기반 접근법은 고자원 언어나 표준화된/기계로 작성된 텍스트에 대한 Handwritten Text Recognition (HTR)에서 유망한 결과를 보여주었으나, 낮은 자원 언어에 적용하는 것은 효과가 제한되는 문제점을 가지고 있다.
    2. 우리는 Transformer 아키텍처를 활용하여 Old Occitan 언어의 손글씨 텍스트를 인식하는 혁신적인 HTR 접근법을 제안한다.
    3. 제한된 데이터를 고려하여, 우리는 텍스트와 이미지 데이터에 대한 복잡한 데이터 증강 기법을 개발하고, Swin 이미지 인코더와 BERT 텍스트 디코더를 결합하여 모델을 구성한다. 실험 결과, 우리의 접근법은 Old Occitan HTR의 최신 기술 모델, TrOCR과 Google Cloud Vision과 같은 상용 애플리케이션을 포함하여 다른 모델들보다 우수한 성능을 보인다.

###### CorefPrompt: Prompt-based Event Coreference Resolution by Measuring Event Type and Argument Compatibilities (https://aclanthology.org/2023.emnlp-main.954/)
- Anthology ID: 2023.emnlp-main.954 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "이벤트 핵심 참조 (ECR)는 동일한 현실 세계 이벤트를 가리키는 이벤트 언급을 클러스터로 그루핑하는 것을 목표로 한다."
    2. "기존 방법들은 '인코딩 먼저, 그리고 스코어링' 프레임워크를 채택하여 핵심 참조 판단이 이벤트 인코딩에 의존하는 문제가 있다."
    3. "우리는 CorefPrompt 라는 기법을 제안하여 ECR을 클로즈 스타일의 MLM (Masked Language Model) 과제로 변환하고, 단일 템플릿 내에서 동시적으로 이벤트 모델링과 핵심 참조 구분을 수행할 수 있도록 한다."

###### Anaphor Assisted Document-Level Relation Extraction (https://aclanthology.org/2023.emnlp-main.955/)
- Anthology ID: 2023.emnlp-main.955 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다문장 문서 내에서 분산된 entity 간의 관계를 식별하는 문제에는 기존 방법들이 다양한 entity 사이의 내부 구조와 외부 상호작용을 모델링하기 위해 이질적인 문서 그래프를 구축하는 것에 초점을 맞추고 있다.
    2. 하지만 기존 방법들은 추론에 중요한 역할을 하는 anaphor를 무시하고, 문서나 문장을 중간 노드로 활용하여 문장간 entity 상호작용을 암묵적으로 이루고 있다. 
    3. 우리는 이러한 문제를 해결하기 위해 Anaphor-Assisted (AA) framework를 제안하였으며, 널리 사용되는 데이터셋에서 실험 결과 우리의 모델이 새로운 state-of-the-art 성능을 달성한다는 것을 보였다.

###### FinEntity: Entity-level Sentiment Classification for Financial Texts (https://aclanthology.org/2023.emnlp-main.956/)
- Anthology ID: 2023.emnlp-main.956 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 금융 도메인에서는 특정 금융 엔티티에 대한 감성 분석을 정확하게 수행하는 것이 중요하다. 이를 위한 공개 데이터셋은 현재로서는 알려진바가 없다.
    2. 이 논문에서는 금융 뉴스에서 금융 엔티티 범위와 그들의 감성 (긍정, 중립, 부정)을 주석으로 달아놓은 entity-level 감성 분류 데이터셋인 "FinEntity"를 소개한다. 
    3. 추가로, "FinEntity"를 기반으로 BERT, FinBERT, ChatGPT 등 여러 사전 훈련된 모델들을 entity-level 감성 분류에서 벤치마크하였다.

###### All Things Considered: Detecting Partisan Events from News Media with Cross-Article Comparison (https://aclanthology.org/2023.emnlp-main.957/)
- Anthology ID: 2023.emnlp-main.957 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대중 의견은 뉴스 매체가 제공하는 정보에 의해 형성되며, 이 정보 또한 매체의 이념적 기호에 의해 형성될 수 있다. 본 논문은 동일한 이야기에 대한 여러 기사를 비교하여 이념적 기사의 기울기를 예측하는 잠재 변수 기반의 프레임워크를 개발하여 매체의 이념적 이벤트의 포함 또는 생략에 의해 의도된 영향을 조사한다. 
    2. 실험을 통해 이념적 이벤트 선택의 존재를 검증하고, 기사의 일치와 문서 간 비교가 경쟁적인 기준에 비해 이념적 이벤트와 기사의 이념을 더 잘 탐지한다는 것을 보였다.
    3. 우리의 결과는 객관성과 비정치성의 강한 규범을 가진 주류 매체에서도 존재하는 고수준의 미디어 편향을 드러낸다.

###### Rationale-Enhanced Language Models are Better Continual Relation Learners (https://aclanthology.org/2023.emnlp-main.958/)
- Anthology ID: 2023.emnlp-main.958 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 연속적인 관계 추출(CRE)은 새롭게 나타나는 관계들의 시퀀스를 학습할 때 치명적인 잊어버림(catastrophic forgetting) 문제를 해결하기 위한 것인데, 최근 연구에서는 치명적인 잊어버림이 미래의 유사한 관계에 대해 모델이 강건하지 못하다는 것을 발견하였다.
    2. 이 문제를 해결하기 위해 우리는 대규모 언어 모델에서 생성된 관계 분류 결과의 설명을 CRE 작업에 도입한다. 특히, 현재 관계를 강건하게 학습하기 위해 다중 작업 원리 튜닝 전략을 제안하며, 또한 유사한 관계를 구별하기 위해 대조적인 원리 재생 모듈을 사용한다.
    3. 두 개의 표준 벤치마크에서의 실험 결과에서 우리의 방법이 최신 CRE 모델보다 우수한 성능을 보였다.

###### BanglaAbuseMeme: A Dataset for Bengali Abusive Meme Classification (https://aclanthology.org/2023.emnlp-main.959/)
- Anthology ID: 2023.emnlp-main.959 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어 플랫폼의 사용 증가로 인해 온라인 학대 문제도 급증하고 있다. 
    2. 이 논문은 낮은 자원 환경에서 폭력적인 밈 (Meme)을 탐지하고 표시하기 위한 모델을 개발하는 것이 중요하다고 강조하고 있다. 
    3. 텍스트와 시각 정보를 모두 활용하는 multimodal 모델이 단일 모달 모델보다 우수한 성능을 보이며, 제안된 모델 중 가장 우수한 성능을 보이는 모델은 macro F1 점수가 70.51이다.

###### ScanDL: A Diffusion Model for Generating Synthetic Scanpaths on Texts (https://aclanthology.org/2023.emnlp-main.960/)
- Anthology ID: 2023.emnlp-main.960 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 독서 중의 눈 움직임은 인간의 언어 처리에 대한 인지 메커니즘을 연구하는 심리 언어학 연구에서 중요한 역할을 한다. 얼마 전까지는 인과관계 모델로 눈 움직임 데이터를 생성했지만, 최근 데이터 기반의 기계 학습 기반 기법이 더 적합하다고 입증되었다.
    2. 해당 논문에서는 이산적인 시퀀스-투-시퀀스 확산 모델인 ScanDL을 제안하여 텍스트에 대한 합성 스캔 패스를 생성한다. 사전 훈련된 단어 표현을 활용하여 자극 텍스트와 고정 시퀀스를 함께 임베딩함으로써 두 입력 간의 다중 모달 상호작용을 포착한다. 
    3. 데이터셋 내부 및 데이터셋 간의 평가를 통해 ScanDL이 최고의 스캔 패스 생성 방법보다 우수한 성과를 보여준다는것을 보였고, 인간과 유사한 독서 행동을 나타내는 능력이 있다는 것을 보여주는 심리 언어학적 분석도 수행한다.

###### From Values to Opinions: Predicting Human Behaviors and Stances Using Value-Injected Large Language Models (https://aclanthology.org/2023.emnlp-main.961/)
- Anthology ID: 2023.emnlp-main.961 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현실적인 시나리오에서 사람들의 의견을 예측할 수 있다면, 정치나 마케팅 등 다양한 분야에서 도움이 될 수 있다. 그러나 유럽 사회조사처럼 대규모 설문조사를 실시하는 것은 막대한 비용이 발생할 수 있다. 
    2. 이를 대비하기 위해, 우리는 핵심 인간 가치가 개인의 결정과 행동에 미치는 영향에 대한 이전 연구를 활용하여, 가치 주입된 대형 언어 모델을 사용하여 의견과 행동을 예측하는 것을 제안한다.  
    3. 실험 결과, 가치 주입된 언어 모델은 기준 모델보다 훨씬 우수한 예측 결과를 보이며, 의견과 행동을 예측하는 데에 가치 주입된 언어 모델을 사용하는 것이 기준 접근법보다 좋을 수 있다는 결과를 제시한다.

###### Analyzing Film Adaptation through Narrative Alignment (https://aclanthology.org/2023.emnlp-main.962/)
- Anthology ID: 2023.emnlp-main.962 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소설은 종종 영화로 채택되지만 두 가지 미디어 간의 차이로 인해 영화 스크립트에서는 소스 텍스트를 일부 삭제해야 하는 경우가 많다.
    2. 이 연구에서는 Smith-Waterman 로컬 정렬 알고리즘과 SBERT 임베딩 거리를 결합하여 장면과 책 단위 사이의 텍스트 유사성을 측정하는 Narrative Alignments를 구성함으로써 이 스크린 어댑테이션 프로세스를 연구한다.
    3. 우리는 이러한 정렬을 사용하여 40개의 영화 어댑테이션을 자동 분석하여 (i) 어댑테이션의 충실성, (ii) 대화의 중요성, (iii) 서술 순서의 보존, 및 (iv) Bechdel 테스트를 반영하는 성별 표현 문제들에 대한 통찰을 얻었다.

###### Inverse Scaling Can Become U-Shaped (https://aclanthology.org/2023.emnlp-main.963/)
- Anthology ID: 2023.emnlp-main.963 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델의 규모를 키우면 downstream task의 성능도 향상되지만, 일부 task에서는 모델 규모가 커짐에 따라 성능이 떨어졌을 때 이는 사람의 선호와 일치하지 않는 행동을 독려할 수 있다는 것을 나타낸다.
    2. 이 연구에서는 역 비례하는 성능을 보이는 task들을 자세히 살펴보았다. 연구에서는 540B 파라미터를 가진 모델을 사용하여 훈련 시간도 Inverse Scaling Prize에서 평가한 것보다 다섯 배 더 길게 훈련했다. 결과적으로 역 비례하는 task 중 4개만이 남았고, 6개의 task는 U자형 비례로 성능이 일정 규모까지 하락한 후 다시 증가하는 형태였다.
    3. 이러한 U자형 비례는 McKenzie et al. (2023)에서 관찰된 역 비례하는 경향이 더 큰 모델에 대해서는 계속 유지되지 않을 수도 있다는 것을 시사한다. 이는 충분히 큰 모델만이 방해 task를 피할 수 있는 영향으로 해석된다.

###### Nearest Neighbor Machine Translation is Meta-Optimizer on Output Projection Layer (https://aclanthology.org/2023.emnlp-main.964/)
- Anthology ID: 2023.emnlp-main.964 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Nearest Neighbor Machine Translation (kNN-MT)"은 사전 훈련된 Neural Machine Translation(NMT) 모델과 도메인 특정 토큰 검색을 통합하여 도메인 적응 작업에서 큰 성공을 거두었지만, 그 이유는 철저히 조사되지 않았다. 
    2. 이 논문에서는 kNN-MT의 작동 메커니즘에 대한 새로운 통찰력을 제공하여, NMT의 출력 projection 레이어에서 경사 하강법을 암묵적으로 수행하는 효율적인 기술로서의 특수한 경우임을 보여준다.
    3. 또한, 여러 도메인 실험과 단어 수준 분석을 통해 kNN-MT와 전체 모델 fine-tuning 간의 성능 차이를 조사하고 찾아낸 결과를 소개한다.

###### Variance Matters: Detecting Semantic Differences without Corpus/Word Alignment (https://aclanthology.org/2023.emnlp-main.965/)
- Anthology ID: 2023.emnlp-main.965 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 본 논문에서, 우리는 두 개의 corpus에 나오는 단어들 사이의 의미적 차이를 발견하기 위한 방법을 제안한다.
    2. 제안된 방법들은 이전 방법들과 달리 단어와/또는 corpus 간의 정렬을 필요로 하지 않는다.
    3. 이 방법들은 이전의 최고 성능 시스템과 견줄 만한 결과를 보여주며, 문서 크기의 불균형에도 강인하며, 드물게 나타나는 단어들의 의미적 차이를 탐지하고, 두 corpus 비교에서 한 corpus에 의미가 빠진 단어들을 찾는 데 효과적이다.

###### MolCA: Molecular Graph-Language Modeling with Cross-Modal Projector and Uni-Modal Adapter (https://aclanthology.org/2023.emnlp-main.966/)
- Anthology ID: 2023.emnlp-main.966 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델 (LM)은 다양한 1D 텍스트 관련 작업에서 인상적인 분자 이해 능력을 보여주었지만, 인간 전문가의 핵심 능력인 2D 그래프 인지를 내재적으로 부족하고 있다. 이런 갭을 메우기 위해 MolCA를 제안한다. MolCA는 크로스모달 프로젝터와 유니모달 어댑터를 사용하여 LM (Galactica)가 텍스트 및 그래프 기반의 분자 내용을 이해할 수 있게 한다.
    2. MolCA는 그래프 인코더의 표현 공간과 LM의 텍스트 공간을 연결하는 Q-포머로 구현된 크로스모달 프로젝터를 사용한다.
    3. 이전 연구들은 크로스모달 대조 학습을 통해 LM과 그래프 인코더를 결합하였으나, MolCA는 LM의 개방형 텍스트 생성 능력을 보존하며 2D 그래프 정보를 보완하여 더욱 효과적으로 작동한다.

###### A Training-Free Debiasing Framework with Counterfactual Reasoning for Conversational Emotion Detection (https://aclanthology.org/2023.emnlp-main.967/)
- Anthology ID: 2023.emnlp-main.967 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 이야기에서 기분 인식 (ERC) 데이터셋에는 레이블 편향, 확률이 높은 클래스에 편향되는 문제와 특정 중립 단어나 발화자와 클래스 간의 과도한 상관관계로 인한 불공정한 예측이 존재한다.
    2. 이 논문에서는 ERC에서 발생하는 이러한 데이터셋 편향을 해결하기 위해 훈련 과정 없이 예측할 때 작동하는 Training-Free Debiasing (TFD) 프레임워크를 제안한다.
    3. TFD는 데이터를 균형화하거나 모델 구조를 수정하지 않고, 간단하고 실험적으로 견고한 원소 별 뺄셈 연산을 사용하여 모델에서 편향을 제거하는 방법이다.

###### Self-ICL: Zero-Shot In-Context Learning with Self-Generated Demonstrations (https://aclanthology.org/2023.emnlp-main.968/)
- Anthology ID: 2023.emnlp-main.968 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델은 몇 개의 입출력 데모로도 목표 작업에 대해 놀랄만한 in-context learning (ICL) 능력을 보여주었다. 이 논문에서는 training 코퍼스에서 대표적인 데모를 선택하기 위해 다양한 방법이 제안되었지만, 실제 사용자들은 대개 데모 풀에 접근할 수 없는 상황이므로, Self-ICL이라는 간단한 프레임워크를 소개하여 zero-shot ICL을 수행하는 LMs의 내재적 능력을 활용한다. 
    2. Self-ICL은 테스트 입력을 받은 후, 모델을 가짜 입력을 생성하도록 유도하고, zero-shot prompting을 통해 가짜 입력에 대한 가짜 라벨을 예측한다. 마지막으로, 가짜 입력-라벨 쌍을 데모로 사용하여 테스트 입력에 대한 ICL을 수행한다. 
    3. BIG-Bench Hard 태스크 23개에 대한 평가 결과, Self-ICL은 평균 정확도와 head-to-head 비교에서 zero-shot 기준을 능가했다. 또한, zero-shot chain-of-thought와 함께 Self-ICL을 사용하면 실제 데모를 사용한 결과와 비교 가능한 성과를 얻을 수 있다.

###### Learning Knowledge-Enhanced Contextual Language Representations for Domain Natural Language Understanding (https://aclanthology.org/2023.emnlp-main.969/)
- Anthology ID: 2023.emnlp-main.969 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지식 향상된 사전 훈련 언어 모델 (KEPLM)은 대규모 지식 그래프 (KG)에서 지식 사실을 주입하여 다양한 하위 NLP 태스크의 성능을 향상시킬 수 있다. 그러나 관계형 트리플로 KEPLM을 사전 훈련시키는 기존 방법은 충분한 도메인 그래프 의미 부족으로 인해 도메인 체계에 적응하기 어렵다.
    2. 이 논문에서는 엔티티 사이의 암묵적인 그래프 구조를 포착하여 다양한 폐쇄 도메인에 대한 지식 강화 언어 표현 학습 프레임워크인 KANGAROO를 제안한다.
    3. 실험에서 KANGAROO는 폐쇄 도메인에서 다양한 지식 고려 NLP 태스크에서 다양한 KEPLM 훈련 패러다임보다 우수한 성능을 보였다.

###### ScdNER: Span-Based Consistency-Aware Document-Level Named Entity Recognition (https://aclanthology.org/2023.emnlp-main.970/)
- Anthology ID: 2023.emnlp-main.970 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문서 수준의 NER (Named Entity Recognition) 접근 방식은 정확하고 일관된 예측을 위해 단어 기반의 key-value memory를 통해 전역 정보를 사용한다.
    2. 그러나 단어 수준에서 전역 정보를 사용할 경우 동일한 단어가 다른 토큰 시퀀스에서 나타나고 다른 레이블을 가지는 경우에는 잡음을 도입할 수 있다.
    3. 이 논문에서는 적응적인 스팬 수준의 전역 특징 퓨전을 통해 더 정확하고 일관된 예측을 위한 두 단계로 구성된 문서 수준의 NER 모델인 ScdNER를 제안한다.

###### MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions (https://aclanthology.org/2023.emnlp-main.971/)
- Anthology ID: 2023.emnlp-main.971 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델 (LLM)에 저장된 정보는 빠르게 날아감으로써 처음부터 다시 훈련하는 것은 종종 불가능하다. 따라서 모델 가중치를 업데이트하여 새로운 사실을 주입하는 기술이 등장했다.
    2. 기존의 평가 패러다임은 수정 된 사실의 회수만 검증하기 때문에 매우 제한적이다. 그러나 한 가지 사실을 변경하면 모델의 관련된 믿음에도 변화가 발생해야 한다. 
    3. 이 논문에서는 사실이 수정된 경우 답이 변경되어야하는 문제를 평가하는 MQuAKE (Multi-hop Question Answering for Knowledge Editing) 벤치마크를 제안한다. MeLLo라는 간단한 메모리 기반 접근 방식을 제안하여 이전 모델 편집자보다 큰 폭으로 성능이 향상됨을 보여준다.

###### Stance Detection on Social Media with Background Knowledge (https://aclanthology.org/2023.emnlp-main.972/)
- Anthology ID: 2023.emnlp-main.972 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어 플랫폼에서 대중 의견을 배우기 위해 특정 대상/주제에 대한 사용자의 입장을 파악하는 것은 중요한 방법이다. 
    2. 기존 연구들은 맥락에서 대상에 대한 입장을 결정하기 위해 맥락에서 대상에 대한 입장 정보를 학습하는 데 초점을 맞추었다. 
    3. 본 논문에서는 대상의 배경 지식을 고려하여 더 나은 입장 검출을 수행하는 새로운 접근 방식을 제안한다. 실험 결과로는 KASD가 대상 내/외 제약에서 최고 수준의 성능을 달성한다는 것을 보여준다.

###### Vision-Enhanced Semantic Entity Recognition in Document Images via Visually-Asymmetric Consistency Learning (https://aclanthology.org/2023.emnlp-main.973/)
- Anthology ID: 2023.emnlp-main.973 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 시각적 요소인 폰트, 배경, 색상, 바운딩 박스 위치 및 크기 등이 사전에 정의된 카테고리에 속하는 의미 있는 엔티티를 식별하는 것은 어려운 작업이다.
    2. 기존 모델은 강한 교차 모달 감독 신호로 시각 인코더를 훈련시키나, 이는 비문자적 특징을 캡처하는 능력에 제약을 가지고 성능이 좋지 않다.
    3. 이 논문에서는 색상 우선순위를 포함시켜 세밀한 시각 및 레이아웃 특징을 더 잘 포착할 수 있는 새로운 VANCL(Visually-Asymmetric coNsistenCy Learning) 접근 방식을 제안하고, 실험 결과를 통해 우리의 방법의 효과를 입증한다.

###### NormDial: A Comparable Bilingual Synthetic Dialog Dataset for Modeling Social Norm Adherence and Violation (https://aclanthology.org/2023.emnlp-main.974/)
- Anthology ID: 2023.emnlp-main.974 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회적 규범은 대인간 의사소통에 근본적으로 영향을 미친다. 이 연구에서는 사회적 규범 준수와 위반의 턴별 어노테이션을 가진 중국과 미국 문화에 대한 고품질의 dyadic 대화 데이터셋인 NormDial을 제안한다.
    2. 우리의 데이터셋은 사회적 규범 준수 감지 작업을 소개하며, 전문가 어노테이션된 사회적 규범을 가지고 사람-모델 협업 파이프라인을 통해 중국어와 영어로 합성적으로 생성된다.
    3. 인간 평가와 기존의 대규모 언어 모델의 성능 평가를 통해 우리의 생성 대화가 고품질임을 보여주며, 이 작업에 대한 기존 대규모 언어 모델의 성능을 평가한다. 우리의 연구 결과는 언어와 문화를 아우르는 대화 맥락에서 사회적 규범의 세밀한면을 이해하기 위한 새로운 방향을 제시한다.

###### ClimateBERT-NetZero: Detecting and Assessing Net Zero and Reduction Targets (https://aclanthology.org/2023.emnlp-main.975/)
- Anthology ID: 2023.emnlp-main.975 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 지속가능한 약속에 대한 정보를 평가하는 것은 어렵기 때문에, 우리는 기업과 국가의 순수제로 및 감축목표를 자동으로 탐지하기 위한 도구를 개발했다.
    2. 전문가 주석이 달린 3.5K개의 텍스트 샘플로 데이터셋을 구축하고, ClimateBERT-NetZero라는 자연어 분류기를 훈련시켜 순수제로 및 감축목표를 포함하는 텍스트를 감지하는 모델을 공개하였다.
    3. 이 모델을 활용하여 기존의 질의응답(Q&A) 모델과 결합하여 순수제로 및 감축목표의 목표분석에 사용할 수 있으며, 분기별 소득 통화 대화 내용에서 통신 패턴이 시간에 따라 어떻게 변화하는지 분석하는 데 활용할 수 있다는 것을 보여준다.

###### Leap-of-Thought: Accelerating Transformers via Dynamic Token Routing (https://aclanthology.org/2023.emnlp-main.976/)
- Anthology ID: 2023.emnlp-main.976 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformers의 계산 효율성은 자원이 제한된 환경이나 실시간 응용 프로그램에서의 배포를 방해하는 오랜 문제였다. 
    2. 본 논문에서는 그 문제를 완화하기 위해 계산 효율성에 큰 기여를 하는 sequence length에 초점을 맞추어 덜 중요한 토큰들을 점진적으로 제거하는 Leap-of-Thought (LoT)이라는 새로운 토큰 축소 방법을 소개한다. 
    3. 이를 통해 LoT은 25배 더 빠른 추론 시간을 달성하면서도 정확도의 큰 손실 없이 모든 토큰에 접근할 수 있는 특징을 갖추게 된다.

###### Reinforcement Replaces Supervision: Query focused Summarization using Deep Reinforcement Learning (https://aclanthology.org/2023.emnlp-main.977/)
- Anthology ID: 2023.emnlp-main.977 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Query-focused Summarization (QfS)는 질의에 기반하여 문서에서 요약을 생성하는 시스템을 다룬다. 우리는 강화학습 (RL)이 자연어생성 문제에 있어 지도학습 (SL)보다 강한 성능을 선보인다는 점에 착안하여, QfS 작업에 RL 기반 접근법을 사용한다. 또한, Transformer에서 RL을 사용할 때 발생할 수 있는 Teacher Forcing의 충돌도 해결한다."
    2. "우리는 ROUGE, BLEU, 의미 유사성을 기반으로 학습된 다중 Policy Gradient 네트워크를 개발하였으며, 이는 벤치마크 데이터셋 (ELI5)에서 ROUGE-L 메트릭에 대한 State-of-the-Art 접근법보다 10 포인트의 개선을 이끌어냈다."
    3. "또한, 우리는 기존에 DebatePedia에 특화된 베이스라인과 비교될 수 있는 결과를 도출하는 제로샷 환경에서도 우리의 접근법의 성능을 보여주었다. 이를 위해 새로운 패시지 임베딩 방법과 함께 더 나은 의미 유사성 보상을 제안하였으며, 마지막으로 QfS와 Long-form Question Answering 연구를 위한 골드 스탠다드 테스트 데이터셋도 기여하였다."

###### Fair Text Classification with Wasserstein Independence (https://aclanthology.org/2023.emnlp-main.978/)
- Anthology ID: 2023.emnlp-main.978 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 그룹 공정은 텍스트 분류에서 중요한 연구 주제로, 여성 대 남성과 같은 민감한 그룹 간의 공정한 대우를 달성하는 것은 여전히 도전과제이다.
    2. 이 논문에서는 모델 아키텍처에 무관한 신경망 텍스트 분류에서 편견을 완화하기 위한 새로운 방법을 제시한다.
    3. 우리의 접근 방식은 민감한 속성에 대한 주석을 훈련 및 테스트 데이터에서 요구하지 않는다는 점에서 기존 방법에 비해 현실적인 시나리오에 더 적합하며, 공정성-정확성 trade-off 관점에서 기존 방법과 비교해서 유사하거나 더 나은 결과를 보여준다.

###### TacoPrompt: A Collaborative Multi-Task Prompt Learning Method for Self-Supervised Taxonomy Completion (https://aclanthology.org/2023.emnlp-main.979/)
- Anthology ID: 2023.emnlp-main.979 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 주제 분류를 위한 새로운 방법인 TacoPrompt는 기존의 overfitting 문제와 subtask 결과에 대한 영향을 고려하지 않는 문제를 해결하기 위해 collaborative multi-task prompt learning을 제안한다. 
    2. TacoPrompt은 prompt learning 기법을 사용하여 불균형한 학습 샘플에서 non-leaf attachment 능력을 효과적으로 학습하고, 결과 문맥을 설계하여 최종 예측과 subtask 결과 간의 관계를 강화하여 multi-task 학습을 개선한다. 
    3. 실험 결과, TacoPrompt는 세 가지 데이터셋에서 최신 주제 분류 성능을 달성하였으며, 코드는 https://github.com/cyclexu/TacoPrompt에서 확인할 수 있다.

###### An Attribution Method for Siamese Encoders (https://aclanthology.org/2023.emnlp-main.980/)
- Anthology ID: 2023.emnlp-main.980 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 시아미즈 인코더 모델인 ST와 같은 모델들이 입력에 어떤 측면에 집중하는지에 대해 잘 알려져 있지 않다. 그 이유는 ST들이 단일 입력을 처리하는 것이 아닌 두 입력을 비교하기 때문에 각각의 특성에 대해 예측을 할 수 없기 때문이다. 
    2. 이 논문은 다중 입력을 가진 모델에 대해 통합 그래디언트의 원리를 일반화하여 시아미즈 인코더에 대한 로컬 어트리뷰션 방법을 유도한다. 이 방법은 특성 쌍에 대한 어트리뷰션 형태이며, ST의 경우 토큰-토큰 행렬로 축소될 수 있다.
    3. 이 방법은 통합된 자코비안의 도입과 통합 그래디언트의 유리한 형식적 특성을 계승하며, 모델의 전체 계산 그래프를 고려하며 실제 예측에 수렴될 것임이 보장된다. 실험 결과 ST의 경우 일부 토큰 쌍이 예측을 지배할 수 있으며, ST는 주로 명사와 동사에 집중하고 있다는 것을 나타낸다. 그러나 정확한 예측을 위해서는 대부분의 토큰과 품사에도 주의를 기울여야 한다.

###### Global Voices, Local Biases: Socio-Cultural Prejudices across Languages (https://aclanthology.org/2023.emnlp-main.981/)
- Anthology ID: 2023.emnlp-main.981 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인간 편향은 문화, 언어, 사회적 경계를 가로지르며 널리 퍼져 있다. 이 연구에서는 Word Embedding Association Test (WEAT)를 24개 언어로 확장하여 언어 모델의 편향에 대한 보다 포괄적인 연구를 진행하고, 각 언어의 문화적인 컨텍스트를 살피면서 그 영향에 대해 조사한다.
    2. 특히 우리는 독다발성, 장애주의 등 다양한 편향 차원에 대한 연구를 진행하며 인도의 언어 풍경에 대해 자세한 지역 편향 분석도 수행한다.
    3. 더불어 임베딩 방법의 광범위한 비교를 통해 이러한 사회적 편향의 중요성과 새로운 차원을 강조하며, 보다 공정한 언어 모델을 위해 이러한 문제를 해결해야 함을 강조한다.

###### Graph vs. Sequence: An Empirical Study on Knowledge Forms for Knowledge-Grounded Dialogue (https://aclanthology.org/2023.emnlp-main.982/)
- Anthology ID: 2023.emnlp-main.982 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Knowledge-grounded dialogue"는 대화 기록과 외부 지식 소스를 기반으로 정보를 제공하는 작업이다. 이 작업에서는 주로 annotated knowledge graph와 website에 있는 지식 텍스트 두 가지 형태의 지식이 사용된다. 이 논문에서는 이러한 두 가지 지식 형태의 장단점과 상호 효과, 그리고 지식의 few-shot 성능에 관한 실험과 연구를 통해 기본 원칙과 결정 요소를 구분하기 위해 핵심적인 세 가지 질문에 답을 찾으려고 한다. 
    2. 적절한 지식 형태의 선택, 지식과 모델 선택 사이의 상호작용 정도, 그리고 지식의 few-shot 성능 등의 주요 질문에 대한 근거를 통해 미래 연구의 방향과 표준에 대한 결론적인 해결책과 합리적인 제안을 제시한다.
    3. 실험 결과에 기반한 통계적인 증거와 함께, 미래 연구의 방향과 표준에 대한 결론적인 해결책과 합리적인 제안을 제시한다.

###### Are Compressed Language Models Less Subgroup Robust? (https://aclanthology.org/2023.emnlp-main.983/)
- Anthology ID: 2023.emnlp-main.983 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델의 추론 비용을 줄이기 위해 모델 압축은 점점 더 사용되고 있으나, 데이터셋의 레이블과 속성에 의해 정의된 소수의 하위 그룹에 대한 강인성은 잘 알려져 있지 않다.
    2. 이 논문에서는 18가지 다른 압축 방법과 설정이 BERT 언어 모델의 하위 그룹 강인성에 미치는 영향을 조사한다.
    3. 우리는 최악의 그룹 성능이 모델 크기만큼이 아니라 사용된 압축 방법에 따라 달라짐을 보여주며, 모델 압축이 항상 소수 그룹 성능을 악화시키지는 않는다는 것을 발견했다.

###### Length Does Matter: Summary Length can Bias Summarization Metrics (https://aclanthology.org/2023.emnlp-main.984/)
- Anthology ID: 2023.emnlp-main.984 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 요약 작업에 대한 메트릭 개발은 복잡하고 종종 주관적인 작업이다. 하지만 기존의 요약 메트릭은 생성된 요약의 길이에 편향성이 존재한다는 것을 밝혀냈다.
    2. 많은 메트릭이 긴 요약을 선호하며 다른 요인들을 고려해도 긴 요약을 더 선호한다는 실험 결과를 보였다.
    3. 이 문제를 해결하기 위해 베이지안 정규화 기술을 도입하여 이러한 편향성을 줄일 수 있다고 보여주었다. 이러한 방식은 요약의 일관성 측면에서 인간의 직감과 대부분의 메트릭 사이의 조화를 크게 향상시킨다.

###### NL2TL: Transforming Natural Languages to Temporal Logics using Large Language Models (https://aclanthology.org/2023.emnlp-main.985/)
- Anthology ID: 2023.emnlp-main.985 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 공학 응용 프로그램에서 시스템에 대한 복잡한 상위 명세를 엄격하게 지정하기 위해 Temporal Logic (TL)을 사용할 수 있다. 그러나 자연어 (NL)와 TL 간의 번역은 데이터셋의 부족과 다양한 응용 분야에서의 일반화 가능한 모델의 부재로 인해 소홀히 여겨진다.
    2. 이 논문에서는 LLMs (Large Language Models)를 여러 단계에서 사용하여 NL에서 TL로의 정확하고 일반화 가능한 변환 프레임워크를 제안한다. 
    3. LLMs와 인간 주석을 조합하여 NL-TL 쌍 데이터셋을 생성하는 프레임워크를 개발하고, 23K 개의 NL-TL 쌍 데이터셋을 게시한다. 그리고 더 나은 일반화 성능을 위해 T5 모델을 미세 조정한다.

###### Reformulating NLP tasks to Capture Longitudinal Manifestation of Language Disorders in People with Dementia. (https://aclanthology.org/2023.emnlp-main.986/)
- Anthology ID: 2023.emnlp-main.986 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 치매는 의사소통을 방해하는 언어 장애와 관련이 있다. 이 연구에서는 중간 크기의 사전 학습 언어 모델을 사용하여 자연어 처리 작업과 관련된 언어 패턴에 집중하도록 강제하며 언어 장애 패턴을 자동으로 학습한다. 
    2. 실험 결과, 문맥 정보를 포함하고 언어 패턴을 향상시키는 NLP 작업은 성능에 이점을 제공한다는 것을 보여준다. 
    3. 제안된 디지털 언어 장애 표지자는 치매 환자들의 언어를 강하고 신뢰할 수 있게 특성화하여 기존의 언어 접근법보다 우수한 성능을 보여준다.

###### Elevating Code-mixed Text Handling through Auditory Information of Words (https://aclanthology.org/2023.emnlp-main.987/)
- Anthology ID: 2023.emnlp-main.987 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 코드 혼합 데이터의 인기 증가와 함께 이러한 유형의 데이터를 처리하는 방법에 대한 필요성이 높아지고 있는다. 그러나 현재의 언어 모델은 주로 단어의 의미적 표현에 초점을 두고 청각적 음성 특징을 무시하므로, 코드 혼합 텍스트의 철자 변화를 처리하기 어렵다.
    2. 본 논문에서는 SOUNDEX의 단어 청각 정보를 활용하여 코드 혼합 텍스트 데이터를 처리하는 언어 모델을 효과적으로 생성하는 접근 방식을 제안한다. 이 접근 방식은 SOUNDEX 표현 (SAMLM)을 포함하는 마스크된 언어 모델링을 기반으로하며, 사전 훈련 모델에 입력 데이터를 제공하는 새로운 방법을 포함한다.
    3. 실험 결과, 우리의 새로운 언어 모델링 접근 방식 (SAMLM)은 코드 혼합 분류 작업에서 적대적 공격에 대한 강도가 향상되었으며, 코드 혼합 작업에 대한 인기 있는 기준보다 더 좋은 분류 결과를 제공한다.

###### Predict and Use: Harnessing Predicted Gaze to Improve Multimodal Sarcasm Detection (https://aclanthology.org/2023.emnlp-main.988/)
- Anthology ID: 2023.emnlp-main.988 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "유머는 사실적인 내용과 억양, 표정, 대화의 문맥, 언어 능력 및 인지 능력과 같은 개인적 특성에 따라 복잡한 언어 구조를 가지고 있다. 이 연구에서는 대화 형태의 다중 모달 유머 감지 성능을 향상시키기 위해 합성의 시선 데이터 활용을 제안한다."
    2. 기존의 다중 모달 대화 데이터셋인 MUStARD++에 시선 특징을 추가하여 성능을 평가하였으며, 사람을 통해 데이터 일부에 대한 시선 특징을 수집하고 나머지 데이터에 대해서는 다양한 시선 특징 예측 방법을 조사하였다.
    3. 수집된 시선 특징과 예측된 데이터를 결합하여 학습한 모델이 MUStARD++ 데이터셋에서 SoTA 성능을 달성하였으며, 유머 감지에 대한 예측 및 활용 모델은 처음으로 공개되었다.

###### Fine-grained Medical Vision-Language Representation Learning for Radiology Report Generation (https://aclanthology.org/2023.emnlp-main.989/)
- Anthology ID: 2023.emnlp-main.989 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 방사선학적 이미지를 입력으로 받아 의료 보고서 생성을 목표로 하는 방사선 보고서 생성에서 기존 연구들은 일반적으로 이미지의 시각적 표현을 추출하기 위해 사전 훈련된 비전 인코더에 의존하였습니다. 
    2. 본 연구에서는 시각과 텍스트 모달리티 간의 간극을 효과적으로 해소하기 위해 페노타입에 의존한 의료 시각-언어 표현 학습 프레임워크를 제안합니다. 
    3. 기존 방법과 달리 우리의 접근법은 이미지를 전체 보고서와 대조시키는 대신 이미지를 보고서 내의 각 문장과 대조하여 더 세부적인 표현을 학습하며, 이 학습된 세부 표현은 방사선 보고서 생성의 성능을 향상시킬 수 있습니다.

###### ViT-TTS: Visual Text-to-Speech with Scalable Diffusion Transformer (https://aclanthology.org/2023.emnlp-main.990/)
- Anthology ID: 2023.emnlp-main.990 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. TTS(Text-to-speech) 기술은 DDPM (Denoising Diffusion Probabilistic Models)의 등장으로 성능이 크게 향상되었지만, 오디오의 인지 품질은 내용, 음높이, 리듬, 에너지뿐만 아니라 물리적 환경에도 영향을 받는다. 이 연구에서는 ViT-TTS라는 첫 번째 시각적 TTS 모델을 제안하여 시각 정보를 포함하여 고 품질의 오디오를 생성함으로써 AR 및 VR의 실용적인 응용 프로그램에 새로운 기회를 제공한다.
    2. 우리는 시각-텍스트 인코더와 노이즈 제거 디코더를 강화하기 위한 자가 지도 학습 프레임워크를 도입하고, 시각적인 장면 정보를 학습하기 위해 매개변수와 용량 측면에서 확장 가능한 확산 트랜스포머 (diffusion transformer)를 활용한다.
    3. 실험 결과, ViT-TTS는 시각적 장면의 가시성에 관계없이, 단순한 시스템 및 기준선보다 우수한 신문 기록을 달성하며, 저 자원 데이터에서도 (1시간, 2시간, 5시간) 풍부한 자원 기준선과 비교 가능한 결과를 달성한다.

###### Consistency Analysis of ChatGPT (https://aclanthology.org/2023.emnlp-main.991/)
- Anthology ID: 2023.emnlp-main.991 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT의 신뢰성과 신뢰성에 대한 의심을 조사한 논문이다. ChatGPT는 언어 이해와 추론 능력이 향상되었지만, 논리적으로 일관된 예측을 자주 만들지 못한다는 결과가 나타났다.
    2. 이 논문은 특히 의미적 일관성과 부정, 대칭 및 추이성과 같은 속성에 주목하여 ChatGPT와 GPT-4의 논리적으로 일관된 행동에 대한 신뢰성을 조사한다. 
    3. 실험을 통해 prompt 설계, few-shot learning 및 큰 언어 모델 (LLM)의 사용이 일관성 문제를 해결하는 궁극적인 해결책이 아님을 확인하였다.

###### Do Differences in Values Influence Disagreements in Online Discussions? (https://aclanthology.org/2023.emnlp-main.992/)
- Anthology ID: 2023.emnlp-main.992 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인 토론에서 의견 차이는 일반적이다. 의견 차이는 일부 조건에서 협력을 촉진하고 토론의 품질을 향상시킬 수 있다. 
    2. 본 논문에서는 차이점에 따른 의견 차이를 예측하기 위해 최신 모델을 사용하고, 예측된 가치를 합산하여 가치 프로필을 만드는 방법을 제안한다. 
    3. Human-annotated agreement labels로 평가한 결과, 가치 프로필의 차이는 특정 경우에 의견 차이와 관련이 있다는 것을 발견하였고, 의견 예측에 가치 정보를 포함시키면 성능이 향상됨을 확인하였다.

###### Automated Fact-Checking in Dialogue: Are Specialized Models Needed? (https://aclanthology.org/2023.emnlp-main.993/)
- Anthology ID: 2023.emnlp-main.993 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이전 연구에서는 독립적인 주장에 대한 사실 확인 모델이 대화에서 제기된 주장에 대해 어려움을 겪는 것으로 나타났다. 이 문제에 대한 해결책으로 대화 데이터 위에 모델을 fine-tuning 하는 것이 제안되었다.
    2. 그러나 각 use case마다 별도의 모델을 만드는 것은 실용적이지 않으며, 대화를 위한 모델 fine-tuning은 일반적인 사실 확인에 대한 성능을 저하시킨다는 것을 보여주었다.
    3. 이러한 도전을 극복하기 위해, 대화를 위해 학습된 모델로 적합하게 대화를 처리하기 위해 검색 적응 및 대화형 입력 변환과 같은 기술을 제안한다. 이러한 기술을 적용한 일반적인 사실 확인 모델이 최신 대화 모델과 경쟁력을 유지하면서 독립적인 주장에 대한 성능을 유지할 수 있는 것을 보여준다.

###### A Digital Language Coherence Marker for Monitoring Dementia (https://aclanthology.org/2023.emnlp-main.994/)
- Anthology ID: 2023.emnlp-main.994 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 주관하지 않은 치매 진단 및 관리를 위해 spontaneous language를 사용하여 디지털 마커를 도출하는 방법이 급부상하고, 유망하며 비침투적인 방법이 되었다.
    2. 디지털 일관성 마커를 도입하여 치매 환자의 인지 변화를 모니터링하는 비용 효율적이고 사람이 이해할 수 있는 디지털 마커를 캡처하는 방법을 제안한다.
    3. 이 연구에서는 짧은 기록된 이야기에서 말의 논리적 일관성을 학습하기 위한 새로운 과제를 제시하고 다양한 신경 접근법을 조사한다. 이 연구는 치매와 건강한 대조군 간의 일관성 패턴을 비교하고 세 가지 임상 생체 마커와의 장기간 평가를 통해 제안된 디지털 일관성 마커의 신뢰성을 조사한다.

###### Detecting Spoilers in Movie Reviews with External Movie Knowledge and User Networks (https://aclanthology.org/2023.emnlp-main.995/)
- Anthology ID: 2023.emnlp-main.995 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 영화 리뷰 플랫폼은 영화 산업과 일반인에게 큰 영향을 주는데, 스포일러 리뷰는 사용자 경험을 크게 해치고 있다. 이전 연구들은 리뷰 내용에 초점을 맞추었지만, 실질적인 스포일러 탐지를 위해서는 영화에 관한 사실과 지식, 사용자 행동 등을 고려해야 한다.
    2. 따라서 이 논문에서는 큰 규모의 스포일러 탐지 데이터셋과 포괄적이며 최신의 영화 지식 디비를 확보하였고, 이를 이용한 스포일러 탐지 모델인 MVSD를 제안한다. MVSD는 영화에 대한 외부 지식과 사용자의 리뷰 플랫폼 활동을 고려하는 모델로, 다양한 데이터 소스와 다중 속성을 모델링하기 위해 세 가지 연결된 이질적 정보 네트워크를 구축한다.
    3. 실험 결과, MVSD는 스포일러 탐지 데이터셋에서 기술적으로 성능이 향상되었고, 외부 지식과 사용자 상호작용의 도입으로 검증 가능한 스포일러 탐지가 가능하다는 것을 보여준다.

###### Joyful: Joint Modality Fusion and Graph Contrastive Learning for Multimoda Emotion Recognition (https://aclanthology.org/2023.emnlp-main.996/)
- Anthology ID: 2023.emnlp-main.996 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다중 모달 감정인식은 인간-기계 상호작용에서 사용되는 각 발화의 감정을 여러 모달리티에서 인식하는 것을 목표로 한다. 하지만 현재의 그래프 기반 방법들은 대화에서의 전역적인 문맥적 특징과 개별 모달의 다양한 특징을 동시에 묘사하는 데 실패한다. 
    2. 이 논문에서는 Joyful이라는 다중 모달 감정인식을 위한 모달리티 퓨전과 그래프 대조 학습을 동시에 최적화하는 방법을 제안한다. 특히, 글로벌 문맥 및 개별 모달 특징 간의 깊은 상호작용과 융합을 제공하는 새로운 다중 모달 퓨전 메커니즘을 설계한다.
    3. 세 개의 벤치마크 데이터셋에서의 실험 결과는 Joyful이 모든 베이스라인과 비교하여 최고 성능을 달성했음을 보여준다. (SOTA performance)

###### HyperRank: Hyperbolic Ranking Model for Unsupervised Keyphrase Extraction (https://aclanthology.org/2023.emnlp-main.997/)
- Anthology ID: 2023.emnlp-main.997 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 웹 상의 문서 개수가 급격히 증가함에 따라, 해당 문서에서 핵심 키워드를 정확하게 추출하는 모델에 대한 수요가 증가하고 있다. 
    2. 본 논문에서는 일반적으로 후보 키워드는 복잡한 문법 및 의미 정보가 내재된 잠재적인 계층 구조를 갖고 있고, 후보 키워드와 문서 간의 관계 역시 계층 구조를 이루기 때문에, 이러한 계층 구조를 고려하는 것이 중요하다. 
    3. 기존의 모델들이 이러한 계층 구조를 간과하여 잘못된 키워드 추출 결과를 만드는 문제를 해결하기 위해, 본 논문은 HyperRank라는 새로운 하이퍼볼릭 랭킹 모델을 제안하였고, 실험 결과 이 모델이 최근의 최고 성능 모델들보다 우수한 성능을 보여준다.

###### Assessing the influence of attractor-verb distance on grammatical agreement in humans and language models (https://aclanthology.org/2023.emnlp-main.998/)
- Anthology ID: 2023.emnlp-main.998 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "주어와 동사간에 위치한 attractor noun은 복잡한 행동을 유발한다. 'The girl near the boys likes climbing.' 이 문장에서 attractor (boys)와 동사 (likes) 간의 grammatical number가 일치하지 않아 문맥상 불가능한 전이 확률을 만든다."
    2. 인공 신경망 모델과 인간의 성능을 비교해 보았고, attractor가 동사에 더 가까워지면 양측 다 실수를 더 많이 하지만, 인간은 주로 attractor의 간섭을 극복할 수 있다. 또한, attractor와 동사 사이의 거리가 반응 시간에도 선형적인 영향을 미친다는 것을 보고했다. 
    3. 이 논문에서는 adjacent words 간의 전이 확률 계산이 근접 효과 (proximity effect)에 영향을 줄 수 있다는 가설을 제시하였다. 그러나 cue-based model과 같은 전통적인 attraction 모델로 이 현상을 설명하는 것은 충분하다고 주장하며, 새로운 연구의 길을 열 수 있다고 주장한다.

###### Federated Meta-Learning for Emotion and Sentiment Aware Multi-modal Complaint Identification (https://aclanthology.org/2023.emnlp-main.999/)
- Anthology ID: 2023.emnlp-main.999 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소비자들이 구매한 상품 또는 서비스에 대한 불만을 자동으로 감지하는 것은 기업과 온라인 상인들에게 매우 중요하다. 기존의 고객 불만 식별 연구는 텍스트에만 국한되어 있으며, 리뷰와 함께 이미지를 사용하는 것이 더 나은 불만 식별을 위한 단서를 제공할 수 있다는 중요성을 강조한다.
    2. 고객의 감정상태가 불만 표현에 큰 영향을 미치기 때문에, 감정과 감성이 불만 식별에 미치는 영향도 조사되어야 한다. 
    3. 이 논문에서는 아마존 웹사이트에 게시된 제품 리뷰와 이미지의 다중 모달 불만 데이터셋을 사용하여, 감정 인식과 감성 분석을 보조 과제로 고려하는 다중 모달 다중 태스크 프레임워크를 제안하였으며, 실험 결과는 제안된 접근법이 기준과 최신 기법을 따른 경우에 비해 더 우수한 성능을 보여준다.

