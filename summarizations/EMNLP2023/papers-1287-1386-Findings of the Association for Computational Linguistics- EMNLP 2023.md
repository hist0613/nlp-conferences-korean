# Korean Three-Line Summarizations of Papers 1287-1386 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### MenatQA: A New Dataset for Testing the Temporal Comprehension and Reasoning Abilities of Large Language Models (https://aclanthology.org/2023.findings-emnlp.100/)
- Anthology ID: 2023.findings-emnlp.100 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 큰 언어 모델 (LLMs)은 많은 자연어 처리 (NLP) 작업에서 거의 포화 상태의 성능을 보였다. 그 결과, 사람들은 LLMs가 시간 이해와 추론과 같은 능력도 능숙하게 습득했다고 믿는 것이 자연스럽다. 그러나, LLMs의 시간 감수성에 대한 연구는 충분히 강조되지 않았다.
    2. 이 논문에서는 LLMs의 시간 이해와 추론 능력을 평가하는 Multiple Sensitive Factors Time QA (MenatQA)를 구성한다. 이는 세 가지 시간적 요인 (범위 요인, 순서 요인, 반사실적 요인)을 포함하며, 총 2,853개의 샘플로 구성된다.
    3. 실험 결과, 현재 주요 LLMs는 다양한 매개변수 크기 (수십억에서 수천억까지)의 작은 시간 추론 모델에 비해 다른 정도로 시간적 추론에 뒤쳐지는 것으로 나타났다. 특히, LLMs는 시간적 편향에 취약하며 질문에서 제공된 시간적 정보에 크게 의존한다.

###### What Makes Chain-of-Thought Prompting Effective? A Counterfactual Study (https://aclanthology.org/2023.findings-emnlp.101/)
- Anthology ID: 2023.findings-emnlp.101 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 체인오브소울트 프롬프팅(CoT)의 효과는 널리 인정되었지만, 그 성공의 기반 메커니즘, 왜 다양한 태스크에서 잘 동작하는지에 대해서는 여전히 알려지지 않은 문제이다.
    2. 이 논문의 연구에서는 카운터펙처얼 프롬프팅 접근 방법을 사용하여 few-shot 프롬프트에서 사용되는 예제 요소들을 체계적으로 조작하고, 모델 동작에 미치는 영향을 테스트함으로써 이를 조사한다.
    3. 세 가지 서로 다른 대용량 언어 모델로 수행한 실험 결과는 몇 가지 핵심적인 결과를 보여준다.

###### Perceptual Structure in the absence of grounding: the impact of abstractedness and subjectivity in color language for LLMs (https://aclanthology.org/2023.findings-emnlp.102/)
- Anthology ID: 2023.findings-emnlp.102 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 이해에 대한 그라운딩이 활발히 연구되고 있다. 이 연구에서는 인지적 중요성과 색상 모델과 언어 모델 간의 특성 공간의 상당한 일치를 보여주는 색상 인지와 색상 언어를 연구하기 위한 적합한 테스트 베드로 인식된다.
    2. 이 논문에서는 대규모의 색상과 설명을 수집하여 (1) 임베딩 공간과 색상 공간 간의 매핑을 학습한 inter-space 정렬과 (2) 색상 설명 간에 비교하는 intra-space 정렬을 비교하는 경험적 분석을 수행한다. 
    3. 결과는 모노렉스믹이고 실용적인 색상 설명의 경우 색상 공간 정렬이 유지되지만 주관성과 추상성과 같은 실제 언어 사용 요소가 포함된 예에서는 정렬이 상당히 감소하는 것을 보여주므로 그라운딩이 해당 경우에 필요할 수 있다는 것을 시사한다.

###### A Dataset for Investigating the Impact of Context for Offensive Language Detection in Tweets (https://aclanthology.org/2023.findings-emnlp.103/)
- Anthology ID: 2023.findings-emnlp.103 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 온라인 상에서의 욕설 탐지는 자연어처리에서 중요한 주제이다. 이 논문에서는 트위터의 답글 트윗에서 욕설 탐지를 위한 문맥의 중요성을 조사하였다.
    2. 욕설이 흔히 사용되는 트위터에서, 특정 트윗에 작성된 원본 트윗을 답글로 추가함으로써 문맥적 정보를 풍부하게 만든 터키어 트윗 데이터셋을 수집하였다.
    3. 이 데이터셋은 인간의 주석자에 의해 수작업으로 라벨링되어 공개되었으며, 문맥 정보의 유무에 따른 다양한 머신러닝 모델의 성능을 비교하였다. 그 결과, 특정 모델의 macro-averaged F1-score을 약간 향상시키긴 했지만, 일반적으로 문맥 정보는 모델 성능 향상에 크게 기여하지는 않았다.

###### Remember what you did so you know what to do next (https://aclanthology.org/2023.findings-emnlp.104/)
- Anthology ID: 2023.findings-emnlp.104 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 6B parameter GPT-J 언어 모델을 사용하여 초등학교 과학 실험을 위한 텍스트 게임 시뮬레이터인 ScienceWorld에서 30가지 목표를 달성하기 위한 계획을 작성하는 방법을 탐구한다. 
    2. 마르코프 가정을 사용하여 모델은 강화학습에 기반한 최신 방법을 1.4배 능가하는 성능을 보인다. 
    3. 실험 결과를 통해 30가지 작업에 대한 성능이 크게 다르므로 작업 평균화가 중요한 성능 문제를 가려낼 수 있다는 것을 보여준다.

###### An Empirical Study of Multimodal Model Merging (https://aclanthology.org/2023.findings-emnlp.105/)
- Anthology ID: 2023.findings-emnlp.105 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 모델 병합 기술을 통해 여러 가지 다른 작업에서 학습된 다수의 모델을 하나로 결합하여 멀티태스크 솔루션을 생성하는 방법이 주로 유사한 작업과 초기화로 학습된 모델들에 대해 성공적으로 적용되었다. 
    2. 본 논문에서는 이 개념을 모델들이 다른 모달리티에서 학습된 변형기들을 병합하는 다중 모달리티 설정에 적용하고자 한다. 
    3. 실험 결과, 초기화, 병합 메커니즘, 모델 아키텍처 등이 모델 병합 이후의 성능에 영향을 미친다는 것을 확인하였고, 또한 병합될 가중치 사이의 거리를 측정하고 병합 결과를 평가하는 두 가지 메트릭을 제안하였다. 이를 통해 모델 병합을 통해 모달리티-방지 구조의 성능을 매칭하는 효과적인 학습 방법을 발견하였고, VQA에서 3%, COCO 검색에서 7%, NLVR2에서 25%, Flickr30k에서 14%, ADE20k에서 3%의 성능 향상을 보였다.

###### Learning to Abstract with Nonparametric Variational Information Bottleneck (https://aclanthology.org/2023.findings-emnlp.106/)
- Anthology ID: 2023.findings-emnlp.106 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 글자, 서브 단어, 단어, 문장 수준의 학습된 표현은 각각 다른 NLP 작업과 언어 현상 이해에 기여하였지만, 텍스트 임베딩 학습은 토큰화에 특화되어 있고 추상화 수준별로 다른 모델을 훈련해야 하는 비용이 크다.
    2. 우리는 하나의 모델 내에서 서로 다른 계층에서 다른 수준의 추상화를 압축하는 학습 가능한 언어 표현 모델인 Nonparametric Variational Information Bottleneck (NVIB)을 Transformer self-attention 계층에 적용한다.
    3. 우리는 모델 내의 계층이 추상화 수준을 증가시키며, 그 표현이 언어적인 특성을 더 잘 반영한다는 것을 발견하였으며, NVIB 압축은 적대적 왜곡에 대해 더 견고한 모델을 얻을 수 있다고 보여준다.

###### Global Structure Knowledge-Guided Relation Extraction Method for Visually-Rich Document (https://aclanthology.org/2023.findings-emnlp.107/)
- Anthology ID: 2023.findings-emnlp.107 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시각적 관계 추출(VRE)은 시각적으로 풍부한 문서 내의 entity 간 관계를 발견하는 강력한 수단이다. 
    2. 기존 방법들은 entity feature를 조작하여 pairwise 관계를 찾는 데 초점을 두었으나, 서로 다른 entity 쌍을 연결하는 더 근본적인 구조적 정보를 소홀히 한다. 
    3. GOSE는 초기 단계에서 문서의 스캔 이미지에서 추출된 entity 쌍에 대해 사전적인 관계 예측을 생성한 다음, 반복적인 예측에서 전역 구조적 지식을 포착하고 entity의 표현에 통합하여 모델의 성능을 향상시키는 프레임워크를 제안한다.

###### Learning to Compose Representations of Different Encoder Layers towards Improving Compositional Generalization (https://aclanthology.org/2023.findings-emnlp.108/)
- Anthology ID: 2023.findings-emnlp.108 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 seq2seq 모델들은 compositional generalization (CG)에 어려움을 겪는다는 것이 알려져왔다. 이 논문에서는 CG가 어려운 이유 중 하나가 인코더의 최상위 레이어의 표현이 혼재되어 있다는 점을 제시하고 있다.
    2. 이전에 식별되었던 표현의 혼재 문제만으로는 충분하지 않다고 본다. 또한, 다른 디코더 레이어에 전달되는 소스 키(key)와 값(value)의 표현도 혼재되어 있는 것으로 가정한다.
    3. 이 논문에서는 CompoSition이라는 seq2seq 모델의 확장을 제안하는데, 이 모델은 다른 태스크에 대해 다른 인코더 레이어의 표현을 동적으로 합성하여 특정 키와 값이 다른 디코더 레이어로 전달되도록 한다. 이 제안의 효과를 실험적으로 입증하였다.

###### SelectNoise: Unsupervised Noise Injection to Enable Zero-Shot Machine Translation for Extremely Low-resource Languages (https://aclanthology.org/2023.findings-emnlp.109/)
- Anthology ID: 2023.findings-emnlp.109 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 극히 적은 자원으로 주어진 언어에서 영어로의 기계 번역 작업에 초점을 맞추고 있다. 평행 데이터의 부재와 큰 다국어 사전 훈련 모델에서의 대표성 부족, 한정된 단일 언어 데이터가 ELRL 언어에 대한 MT 시스템 개발을 저해한다. 
    2. 그러나 많은 ELRL 언어는 방언의 변이, 지리적 근접성, 언어 구조와 같은 요인으로 인해 고자원 언어와 어휘적 유사성을 가진다. 이러한 특성을 활용하여 ELRL 언어에 대한 MT 작업을 가능하게 하는데 HRL 언어로부터의 cross-lingual 신호 향상을 위해 새로운 비지도식 접근 방법인 SelectNoise를 제안한다.
    3. 제안된 모델은 FLORES-200 벤치마크의 12개 ELRL 언어에 대해 zero-shot 설정에서 두 언어 패밀리를 거쳐 평가되었으며, 강력한 기준에 비해 더 나은 성능을 보여주었다. 그리고 supervised noise injection 모델과 품질이 비슷하다는 결과를 얻었다.

###### Breaking Boundaries in Retrieval Systems: Unsupervised Domain Adaptation with Denoise-Finetuning (https://aclanthology.org/2023.findings-emnlp.110/)
- Anthology ID: 2023.findings-emnlp.110 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Dense retrieval 모델들은 탁월한 효과를 보여주었지만, 풍부한 레이블 데이터에 의존하고 다른 도메인에 적용할 때 문제점이 있다.
    2. 기존의 도메인 적응 방법들은 가짜 쿼리를 생성하는 생성 모델을 사용하여 dense retrieval 모델의 성능을 향상시키기 위해 가짜 데이터셋을 생성했다. 
    3. 그러나 이러한 접근법은 일반적으로 적응되지 않은 rerank 모델을 사용하므로, 정확하지 않은 레이블을 얻을 수 있다. 이 논문에서는 rerank 모델을 target 도메인에 적응시키는 것의 중요성을 입증하고, 이를 통해 더 정확한 레이블을 얻어 dense retrieval 모델의 전체적인 성능을 향상시키는 방법을 소개한다.

###### Exploring the Cognitive Knowledge Structure of Large Language Models: An Educational Diagnostic Assessment Approach (https://aclanthology.org/2023.findings-emnlp.111/)
- Anthology ID: 2023.findings-emnlp.111 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구는 LLMs의 학습 능력을 테스트하고 다양한 도메인에서 뛰어난 능력을 나타내었으나, LLMs의 지식 구조에 대한 인식은 부족하다. 
    2. 이 논문에서는 교육적 진단 평가 방법을 사용하여 LLMs의 지식 구조를 평가하고 인식 능력을 파악한다.
    3. LLMs의 지식을 조명함으로써 연구자들은 더욤 정보화되고 효과적인 LLMs의 개발과 활용을 진전시킬 수 있다.

###### Simpler neural networks prefer subregular languages (https://aclanthology.org/2023.findings-emnlp.112/)
- Anthology ID: 2023.findings-emnlp.112 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LSTMs는 L0 정규화의 연속적 완화를 적용함으로써 희소성을 유도하는데 이를 통해 LSTMs가 학습하고 표현하기 쉬운 형식 언어의 패턴에 관심이 있다.
    2. 다양한 테스트에서 우리는 희소한 LSTMs가 정반 정규 언어보다 소규칙(subregular) 언어를 선호한다는 것을 발견했으며, LSTMs에서의 이러한 편향은 희소성 압력이 커질수록 강해진다.
    3. 또한, 소규칙 언어로 훈련된 LSTMs는 비-0 매개변수가 더 적다. 이러한 LSTMs의 소규칙 편향은 적절한 설명 언어의 간단함 편향 아래에서 발생하는 인간의 음운학에서의 소규칙 언어 편향과 관련되어 있다고 추측한다.

###### Simple Hardware-Efficient PCFGs with Independent Left and Right Productions (https://aclanthology.org/2023.findings-emnlp.113/)
- Anthology ID: 2023.findings-emnlp.113 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수천 개의 nonterminal에 대한 밀집 PCFG 스케일링은 규칙 확률 텐서의 저차원 파라미터화를 통해 비슷한 규모의 HMM보다 효과적임이 입증되었으나, 이 방식으로 크기를 확장한 PCFG는 여전히 언어 모델로서 성능이 안 좋고 HMM보다 성능이 나쁘다.
    2. 본 논문에서는 독립적인 좌우 생성 (independent left and right productions) 을 강하게 가정한 SimplePCFG를 소개하며, 저차원 방식보다 확장성이 효과적이라는 것을 발견했다.
    3. 또한 SimplePCFG의 확장성을 향상시키기 위해 FlashInside라는 하드웨어 I/O-aware한 inside algorithm 구현을 도입하였으며, 여러 grammar induction 벤치마크에서 extensive한 실험을 통해 SimplePCFG의 효과를 검증하였다.

###### R3 Prompting: Review, Rephrase and Resolve for Chain-of-Thought Reasoning in Large Language Models under Noisy Context (https://aclanthology.org/2023.findings-emnlp.114/)
- Anthology ID: 2023.findings-emnlp.114 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Chain-of-Thought (CoT) prompting을 통해 Large Language Models (LLMs)은 다양한 추론 태스크에서 놀라운 성능을 달성했지만, 대부분의 태스크는 노이즈가 없는 문맥에서 평가되었고, 노이즈가 있는 문맥에서 LLMs가 부정확한 결과를 생성하는 문제는 완전히 조사되지 않았다.
    2. 기존 연구는 트리거 문장(trigger sentences)을 사용하여 LLMs가 관련 정보에 집중하도록 유도하지만, 트리거는 최종 정답 예측에 제한적인 영향을 미친다.
    3. 이 논문에서는 noise가 있는 문맥에서 CoT 추론을 위한 R3 prompting이라는 새로운 프롬프팅 방법을 제안한다. R3 prompting은 LLMs와 상호작용을 통해 핵심 문장 추출, 변수 선언 및 정답 예측을 수행하며, 이는 검토, 다시 구문화 및 해결 등의 사고과정에 해당한다. R3 prompting은 노이즈가 있는 문맥에서 다섯 가지 추론 태스크에서 기존 CoT prompting 방법보다 큰 성능 향상을 보였다.

###### Quality Estimation-Assisted Automatic Post-Editing (https://aclanthology.org/2023.findings-emnlp.115/)
- Anthology ID: 2023.findings-emnlp.115 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자동 텍스트 수정(APE) 시스템은 기계 번역(MT) 출력물의 과다 수정 문제가 있다. 단어 수준의 품질 평가(QE) 시스템은 과다 수정을 방지하는 방법을 제공할 수 있지만, 기존의 APE와 QE 조합 전략을 사용하여 상당한 성능 향상이 관측되지 않았다.
    2. 이 논문에서는 APE를 개선하기 위해 APE와 QE 작업에 대한 모델의 공동 훈련을 제안한다. 제안된 접근 방식은 다중 작업 학습(MTL) 방법론을 활용하며, 훈련 중 양쪽 작업을 '협상 게임'으로 다루면서 상당한 향상을 보여준다.
    3. 또한, 다양한 기존 조합 전략을 조사하고, 제안된 접근 방식이 '먼' 언어 쌍인 영어-마라티어에 대해 최첨단 성능을 달성하는 것을 보여준다. QE 비지도 APE 시스템에 대해 영어-마라티어에서 1.09 TER 및 1.37 BLEU 포인트 개선을 관찰하고, 영어-독일어에서는 0.46 TER 및 0.62 BLEU 포인트를 관찰한다.

###### Adapter Pruning using Tropical Characterization (https://aclanthology.org/2023.findings-emnlp.116/)
- Anthology ID: 2023.findings-emnlp.116 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 어댑터는 사전 훈련된 언어 모델의 레이어 사이에 학습 가능한 모듈을 삽입하는 파라미터 효율적인 전이 학습 접근법이다. 그러나 어댑터 파라미터의 최적 개수를 분석하는 연구가 부족하다. 
    2. 따라서, 우리는 훈련 가능한 모듈의 tropical 특성을 연구하여 어댑터 가중치를 자르는 접근법을 제안한다.
    3. 실험 결과는 tropical geometry가 magnitude-based 기준과 비교했을 때 더 관련성이 높은 파라미터를 자를 수 있음을 보여주며, 합친 방법이 다양한 작업에서 가장 잘 작동한다.

###### Self-Supervised Rule Learning to Link Text Segments to Relational Elements of Structured Knowledge (https://aclanthology.org/2023.findings-emnlp.117/)
- Anthology ID: 2023.findings-emnlp.117 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 우리는 지식 베이스 질문 응답 시스템에서 관계 연결을 수행하기 위해 해석 가능한 규칙인 지식을 자기학습하는 신경 기호적 접근 방식을 제안한다.
    2. 학습 중에 학습된 가중치는 관계 연결을 수행하는 데 필요한 매핑 역할을 효과적으로 수행한다.
    3. 마스킹 된 훈련 전략을 사용하여 규칙을 자기학습하는 데 있어 이 작업의 차별화된 측면은 문장의 논리 형태에 적용된다. 이는 구조화된 지식 원본에서 확장된 문맥 정보를 추출하고 이를 기반으로 견고하고 인간이 읽을 수 있는 규칙을 구축하는 기회를 제공한다.

###### TaTA: A Multilingual Table-to-Text Dataset for African Languages (https://aclanthology.org/2023.findings-emnlp.118/)
- Anthology ID: 2023.findings-emnlp.118 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 data-to-text generation 데이터셋은 대부분 영어로 제한되어 있다. 이 연구에서는 이러한 데이터 부족 문제를 해결하기 위해 아프리카어에 초점을 맞춘 첫 번째 대규모 다국어 table-to-text 데이터셋인 TaTA를 생성하였다.
    2. TaTA는 계통학적 및 보건 조사 프로그램에 의한 이중언어 보고서의 테이블과 관련 텍스트를 전문 번역을 통해 9개 언어로 병렬화하여 구축되었다.
    3. 인간 평가를 통해 TaTA는 현재의 모델에 대해 어렵고, mT5-XXL 기반 모델에 의한 출력 중 이해 가능하고 소스 데이터에 귀속되는 결과는 절반에 불과함을 보여주었다. 이 결과는 가) 평가 메트릭의 검증 필요성과 나) 도메인 특정 메트릭의 중요성을 강조한다.

###### Explain-then-translate: an analysis on improving program translation with self-generated explanations (https://aclanthology.org/2023.findings-emnlp.119/)
- Anthology ID: 2023.findings-emnlp.119 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구는 언어 모델을 사용하여 코드 간 변환을 위한 중간 단계로 자체 생성된 자연어 설명의 사용을 탐색한다. MultiPL-E 데이터셋에서 생성된 3가지 유형의 설명과 19개 프로그래밍 언어를 대상으로 실험한 결과, 설명은 제로샷 경우에 특히 효과적이며, 성능을 평균 12% 향상시킨다. 자연어 설명은 어려운 프로그램에서 특히 두드러진 효과를 보였다.
    2. 자연어 설명을 사용한 실험 결과, 제로샷 경우에 특히 수행 성능이 향상되었으며, 설명이 어려운 프로그램에 특히 도움이 된다는 것을 확인하였다.
    3. 19개 언어로 된 데이터셋, 코드 및 기준 솔루션을 공개한다.

###### Can Brain Signals Reveal Inner Alignment with Human Languages? (https://aclanthology.org/2023.findings-emnlp.120/)
- Anthology ID: 2023.findings-emnlp.120 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "뇌 신호 (예: 뇌파)와 인간 언어는 다양한 하향 작업에 독립적으로 널리 연구되었지만, 그들 간의 관계 와 의존성을 잘 알려진 바가 없다." 
    2. "우리는 MTAM이라는 다중 모달 트랜스포머 (Multimodal Transformer Alignment Model)을 소개하여 이 두 매체 간의 조정된 표현을 관찰하는 것을 목표로 한다."
    3. "우리의 방법은 감성 분석 및 관계 감지와 같은 하향 응용 프로그램에서 ZuCo 및 K-EmoCon 두 데이터 세트에 대해 새로운 최첨단 결과를 달성했다. 또한, 우리는 그 결과의 해석과 함께 코드를 공개적으로 제공한다."

###### DemoSG: Demonstration-enhanced Schema-guided Generation for Low-resource Event Extraction (https://aclanthology.org/2023.findings-emnlp.121/)
- Anthology ID: 2023.findings-emnlp.121 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 이벤트 추출 (EE) 방법들은 대규모의 주석이 달린 데이터가 필요한 높은 리소스 시나리오에 초점을 맞추고 있어서, 저자금 도메인에는 적용하기 어렵다. 이러한 제한된 리소스로 EE를 더 효과적으로 다루기 위해, 저작 리서스를 활용한 스키마 가이드 생성 (DemoSG) 모델을 제안한다.
    2. 우리는 EE를 설명에 기반한 학습 패러다임으로 제안하여 주석이 달린 데이터를 활용하여 추출 프로세스를 설명하고, 모델의 효과적인 학습을 돕도록 한다.
    3. 또한, 우리는 스키마 기반 프롬프트에 따라 자연어 생성 작업으로 EE를 정의하여, 저자원 시나리오에서 라벨 의미론을 활용하고 지식 전이를 촉진한다. 우리는 세 개의 데이터셋에서 도메인 내 및 도메인 적응 저자원 시나리오에서의 확장적인 실험을 수행하고, DemoSG의 강건성을 연구한다. 결과는 DemoSG가 저자원 시나리오에서 현재 방법들보다 큰 성능 향상을 보인다.

###### GLGR: Question-aware Global-to-Local Graph Reasoning for Multi-party Dialogue Reading Comprehension (https://aclanthology.org/2023.findings-emnlp.122/)
- Anthology ID: 2023.findings-emnlp.122 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다자간 대화 읽기 이해(MDRC)에서 그래프 추론은 다양한 정보(clue)를 통합하는데 기여한다. 하지만 기존의 접근 방식은 질문을 그래프 추론에 적용하지 않고, 발화문의 지역적 의미 구조를 무시한다.
    2. 이 논문에서는 질문을 고려한 전역부터지역 그래프 추론 방법을 제안한다. 전통적인 상대말-발화문 그래프에 질문 노드를 추가하여 종합적인 전역 그래프 추론을 가능하게 한다. 또한, 각 발화문에 대해 의미 역할 그래프를 구성하여 의미적 관계에 의거한 지역 그래프 추론을 수행한다.
    3. 실험 결과, 제안된 방법은 BERT와 ELECTRA 기준에 비해 매우 큰 개선을 보여주며, 모울웨니와 FriendsQA에서 각각 73.6%와 77.2%의 F1 점수를 얻어 다른 사전 훈련 언어 모델을 백본으로 사용하는 최신 기법들을 능가한다.

###### Towards Mitigating LLM Hallucination via Self Reflection (https://aclanthology.org/2023.findings-emnlp.123/)
- Anthology ID: 2023.findings-emnlp.123 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델(LLMs)은 질의응답(QA)과 같은 생성 및 지식 집약적 작업에 대한 가능성을 보였으나, 모델이 사실과 일치하지 않거나 의미없는 정보를 생성하는 "환각(hallucination)" 문제가 여전히 해결되지 않고 있다.
    2. 본 논문에서는 의학 분야에서 널리 사용되는 LLM과 데이터셋을 사용하여 환각 현상을 분석하였는데, 목표는 일반적으로 문제가 되는 답변들을 식별하고 이해하는 것이다.
    3. 이를 해결하기 위해, 우리는 지식 습득과 답변 생성을 접목한 대화식 자기 반성 방법론을 제안한다. 이를 통해 우리의 접근 방식은 점진적으로 사실성, 일관성 및 함의를 향상시키며, 점점 더 정확하고 정확한 답변을 생성한다는 것을 실험 결과로 입증하였다.

###### Making Body Movement in Sign Language Corpus Accessible for Linguists and Machines with Three-Dimensional Normalization of MediaPipe (https://aclanthology.org/2023.findings-emnlp.124/)
- Anthology ID: 2023.findings-emnlp.124 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수화 동영상 자료에서 movement를 확인하는 데에는, 수동 주석이나 컴퓨터 기반 방법이 사용된다. 하지만 전자는 feature의 사전 정의에 의존하고, 후자는 기술적인 지식을 요한다.
    2. 이 논문에서는 2차원 이미지에서 한정적인 depth 좌표 근사치로 body pose를 감지하는 MediaPipe 및 OpenPose와 같은 방법을 제안한다.
    3. 논문에서 제안하는 새로운 3차원 정규화 방법을 사용하여 2차원 자세 데이터의 잠재적인 한계를 해결하였고, 이를 통해 deep learning 기반 접근법에서 좋은 성능을 보여주었다.

###### XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (https://aclanthology.org/2023.findings-emnlp.125/)
- Anthology ID: 2023.findings-emnlp.125 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 데이터 부족은 다국어 NLP 시스템 개발에 있어 중요한 문제입니다. 그러나 NLP 연구가 특히 사용자 요구를 충족시키지 못하는 언어들에 대해서는 소량의 데이터를 주석으로 붙이는 것이 가능합니다.
    2. 이 논문에서는 XTREME-UP라는 벤치마크를 제안하며 일반적으로 유용한 작업인 사용자 중심(task-centric) 작업에 초점을 맞추고 있습니다. XTREME-UP은 OCR, 자동 완성, 의미 분석, 음성 인식, 기계 번역 등 9가지 주요한 사용자 중심 기술 부문에 걸쳐 88개의 언더 리프레젠티드 언어들을 평가합니다.
    3. 이를 위해 XTREME-UP은 텍스트만을 고려한 모델링 시나리오, 멀티모달(비전, 오디오, 텍스트) 모델링 시나리오, 지도 학습 매개변수 조정, 문맥 학습 등 여러 가지 모델링 시나리오를 평가하는 방법론을 제공하고 있습니다.

###### DiffuVST: Narrating Fictional Scenes with Global-History-Guided Denoising Models (https://aclanthology.org/2023.findings-emnlp.126/)
- Anthology ID: 2023.findings-emnlp.126 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 AI 기반 이미지 합성의 진보로 인해, 추상성과 다양성을 갖춘 시각적인 장면들이 많이 생성되었으며, 이에 따라 시각적인 스토리텔링(VST)은 더욱 도전적인 작업이 되었고, 실제 장면 이상으로 요구되고 있다.
    2. 기존 VST 기술은 보통 자가회귀 디코더를 사용하는데, 많은 progress를 보이지만 추적 속도가 낮고 가상 장면에는 적합하지 않다.
    3. 이 논문에서는 시각적 설명의 생성을 단일 조건부 노이즈 제거 과정으로 모델링하는 획기적인 확산 기반 시스템인 DiffuVST를 제안한다. 추론 시에 확률적이고 비자기 회귀적인 특성을 가진 DiffuVST는 더 효율적으로 다양한 내러티브를 생성할 수 있다.

###### DiFair: A Benchmark for Disentangled Assessment of Gender Knowledge and Bias (https://aclanthology.org/2023.findings-emnlp.127/)
- Anthology ID: 2023.findings-emnlp.127 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습 언어 모델의 성별 편향을 완화하기 위해 많은 균형 조정 기술이 제안되었지만, 이는 모델의 예측에서 성별 중립성을 얼마나 검증하는지를 평가하는 기존 데이터셋에 의존한다. 이 논문에서는 이러한 평가 프로토콜이 유용한 성별 지식에 대한 부작용을 고려하지 못한다고 지적하고, 유용한 성별 지식이 유지되는지를 확인할 수 있는 통합 메트릭인 "gender invariance score"를 도입한다.
    2. "DiFair"라는 수동으로 제작된 데이터셋을 기반으로, 사전 학습 언어 모델과 균형 조정 기술에 대한 벤치마크로 사용된다. 실험 결과는 기존의 성별 편향 문제를 확인하면서도, 균형 조정 기술이 성별 편향 문제를 개선하지만 이로 인해 모델의 유용한 성별 지식이 감소하는 경향을 보여준다.
    3. 따라서 이 논문은 성별 편향을 해결하는 한편, 모델의 유용한 성별 지식을 유지할 수 있는 방법을 제시한다.

###### Transformer-Based Language Model Surprisal Predicts Human Reading Times Best with About Two Billion Training Tokens (https://aclanthology.org/2023.findings-emnlp.128/)
- Anthology ID: 2023.findings-emnlp.128 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 심리언어학적 연구들은 언어 모델의 품질과 예상치의 능력 사이에 모순된 결론을 내놓았다. 이 논문은 역사적으로 높은 양의 훈련 데이터와 모델 용량의 큰 격차 때문에 이러한 다양성이 생기는 것이라고 제안한다.
    2. 이 연구에서는 훈련 데이터와 모델 용량이 체계적으로 다른 Transformer 기반 언어 모델별로 예상치 측정치가 인간의 읽기 시간을 예측하는 능력을 평가하여 이러한 결과들을 통합한다.
    3. 결과적으로, 현대적인 모델 용량을 가진 대부분의 변형체들은 약 20억 개의 훈련 토큰을 본 후에 가장 적합한 예측치를 제공하며, 그 이후에는 인간의 기대치와 일치하지 않게 되는 것으로 나타났다. 또한, 새롭게 훈련된 작은 모델 변형체들은 수렴시 '포인트'로 반영되며, 언어 모델의 내재적인 크기가 인간의 읽기 시간과 일치하는데 필요한 요소임을 보여준다.

###### ExplainCPE: A Free-text Explanation Benchmark of Chinese Pharmacist Examination (https://aclanthology.org/2023.findings-emnlp.129/)
- Anthology ID: 2023.findings-emnlp.129 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구들은 언어모델의 유용성을 탐구하고 있지만, 중요한 문제는 이 모델들의 해석 가능성이다. 기존 설명 데이터셋은 영어와 일반적인 도메인에 한정되어 있어 언어 다양성의 부족과 의료와 같은 특수 도메인의 부족으로 인해 한계가 있다. 이를 해결하기 위해 "ExplainCPE"라는 의학 분야에 특화된 도전적인 데이터셋을 제안한다.
    2. 중국에서 의약사 시험에 대한 7K개 이상의 문제로 구성된 ExplainCPE는 언어모델이 생성하는 설명을 평가하는 목적으로 만들어졌다.
    3. 전체 결과를 보면, GPT-4만이 약사 시험을 75.7%의 정확도로 통과하고, ChatGPT와 같은 다른 모델들은 실패한다. 더 상세한 분석 결과, 언어모델이 생성한 설명의 한계와 의료 텍스트의 이해와 계산적 추론에 대한 한계가 드러난다. 따라서 ExplainCPE는 의료 분야에서 언어모델의 해석 가능성을 개선하고 평가하는 방향으로 한 발 더 나아간다.

###### CLASS: A Design Framework for Building Intelligent Tutoring Systems Based on Learning Science principles (https://aclanthology.org/2023.findings-emnlp.130/)
- Anthology ID: 2023.findings-emnlp.130 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. CLASS 프레임워크는 고성능의 Large Language Model (LLM)을 통해 고급 지능형 학습 시스템 (ITS)을 구축하는 데 사용하는 설계 도구이다. 이 프레임워크는 학습자에게 튜터처럼 단계별 가이드를 제공하고 학습자와 자연어 상호작용을 도와주는 두 가지 주요 기능을 제공한다.
    2. CLASS 프레임워크를 사용하여 개발된 SPOCK은 대학 수준의 생물학 컨텐츠에 중점을 둔 ITS로, 학습자에게 질문을 관리 가능한 하위 문제로 나누고 학습자에게 격려하는 답변을 제공하는 능력을 강조하여 전문가로부터 긍정적인 평가를 받았다.
    3. CLASS 프레임워크는 연속된 수정 및 개선을 가능하게 하며 사용자 피드백을 통합할 수 있어 ITS의 내부 의사 결정 과정에 대한 통찰력을 제공한다.

###### Normal-Abnormal Decoupling Memory for Medical Report Generation (https://aclanthology.org/2023.findings-emnlp.131/)
- Anthology ID: 2023.findings-emnlp.131 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 의료 보고서의 자동 생성은 임상 자동화에서 중요한 역할을 한다. 라디올로지 이미지는 자연 이미지와 달리 높은 유사성을 보이는 동시에 의료 데이터는 데이터 편향과 복잡한 노이즈에 취약하므로, 기존 방법들이 미세한 시각적 정보를 포착하는 데 어려움을 겪는다.
    2. 이 논문에서는 비정상적인 패턴 메모리를 활용하는 새로운 정상/비정상 의미 해체 네트워크를 소개하여 시각적 추출을 최적화한다. 정상/비정상 의미를 독립적으로 학습하여 시각적 네트워크의 최적화에 영향을 미치지 않도록 한다.
    3. 이 방법은 잡음이 있는 정상 의미와 보고서의 영향을 완화하며, 비정상 패턴 메모리를 위한 새로운 인코더를 개발하여 이미지의 비정상 패턴을 포착하고 내장하는 네트워크의 능력을 개선한다. 이 접근법은 MIMIC-CXR 벤치마크에서 우수한 성능을 나타내며 현재의 최고 성능 방법을 능가한다.

###### mmT5: Modular Multilingual Pre-Training Solves Source Language Hallucinations (https://aclanthology.org/2023.findings-emnlp.132/)
- Anthology ID: 2023.findings-emnlp.132 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 sequence-to-sequence 모델은 언어 처리 범위가 넓어질수록 성능이 저하되며, few-shot 설정에서 올바른 목표 언어의 텍스트를 일관되게 생성하지 못한다. 
    2. 이 논문에서는 mmT5라는 모듈식 다국어 sequence-to-sequence 모델을 제안한다. 
    3. mmT5는 pre-training 중 언어별 모듈을 사용하여 언어-일반 정보를 분리하며, fine-tuning 과정에서 발생하는 representation drift를 완화시키기 위한 전략을 개발하여 40개 이상의 언어에서 대표적인 자연어 이해와 생성 과제에서 mT5과 비교했을 때 월등한 성능 향상을 보인다.

###### ImageNetVC: Zero- and Few-Shot Visual Commonsense Evaluation on 1000 ImageNet Categories (https://aclanthology.org/2023.findings-emnlp.133/)
- Anthology ID: 2023.findings-emnlp.133 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근, 대형 언어 모델 (LLM)은 일반적인 인터페이스로 사용되고 있는데, 이는 포괄적인 시각적 지식에 대한 중요한 요구 사항을 발생시킨다.
    2. 이 연구에서는 시각적 commonsense 지식을 제대로 활용할 수 있는 현재의 LLM과 그의 시각적 augmented 상대방 (VaLM)의 실력이 어느 정도인지 조사한다.
    3. ImageNetVC를 활용하여 1,000개의 ImageNet 카테고리를 대상으로 zero- 및 few-shot 시각적 commonsense 평가를 위한 인간 주석 데이터셋을 구축한다.

###### MultiCoNER v2: a Large Multilingual dataset for Fine-grained and Noisy Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.134/)
- Anthology ID: 2023.findings-emnlp.134 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. MULTICONER V2는 12개 언어에서 33개 entity 클래스를 다루는 fine-grained Named Entity Recognition(NER) 데이터셋으로, movie titles과 같은 복잡한 entity를 포함하는 fine-grained 클래스를 효과적으로 처리하고, typing mistakes나 OCR 오류로 인한 노이즈로 인한 성능 하락을 대비한다.
    2. MULTICONER V2의 특징으로는 fine-grained taxonomy의 어려움과 entity 오염이 성능에 미치는 영향이 크다는 점이 있다. entity 오염으로 인해 비엔티티 오염에 비해 성능이 9% 하락하는 것을 확인할 수 있다.
    3. MULTICONER V2 데이터셋은 Wikipedia와 Wikidata 같은 오픈 리소스를 사용하여 공개되어 있으며, XLM-RoBERTa 기준 평가 결과는 이 데이터셋의 독특한 어려움을 강조하고 있다.

###### A Query-Parallel Machine Reading Comprehension Framework for Low-resource NER (https://aclanthology.org/2023.findings-emnlp.135/)
- Anthology ID: 2023.findings-emnlp.135 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 명명된 개체 인식(NER)은 자연어 처리에서 중요한 작업이다. 현재의 MRC(Machine Reading Comprehension)-기반 NER 기술은 한 번에 하나의 유형의 개체만 추출할 수 있으며 주로 resource-rich한 상황에 적용된다. 이로 인해 추론 단계에서 효율적이지 못하며, low-resource한 상황에서의 활용 가능성도 제한된다.
    2. 우리는 여러 개의 유형의 개체를 동시에 추출할 수 있는 query-parallel MRC 기반 접근법을 제안한다. 이는 resource-rich와 resource-limited 상황 모두에 적용 가능하다.
    3. 우리는 query-parallel encoder를 제안하며, 이는 query-segmented attention 메커니즘을 사용하여 query의 의미를 독립적으로 분리하고, 쿼리-컨텍스트 상호작용을 단방향 흐름으로 모델링한다. 이는 새로운 개체 유형에 대한 일반화나 새로운 도메인으로의 전이를 보다 쉽게 가능하게 한다.

###### BiSPN: Generating Entity Set and Relation Set Coherently in One Pass (https://aclanthology.org/2023.findings-emnlp.136/)
- Anthology ID: 2023.findings-emnlp.136 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Set Prediction Networks (SPNs)는 인스턴스간 상호작용을 모델링하여 named entity recognition과 관계 트리플 추출 작업에서 최고의 성능을 달성했다. 그러나 SPNs를 통해 entity와 relation triple을 동시에 추출하는 방법은 아직 연구되지 않은 문제이다. 이 논문에서는 Bipartite Set Prediction Network (BiSPN)을 제안하여 병렬로 entity set과 relation set을 효율적으로 생성할 수 있는 새로운 모델을 소개한다.
    2. BiSPN은 coherence 유지를 위한 새로운 bipartite consistency loss와 entity-relation linking loss를 훈련 중에 적용하여 도전적인 과제를 극복한다.
    3. 바이오의학/임상 데이터셋과 일반 도메인 데이터셋에서의 실험 결과, BiSPN은 지식 중심 scene에서 새로운 state-of-the-art 성능을 달성하며, 일반 도메인에서도 경쟁력 있는 성능을 보여준다. 이때, 두 단계의 joint extraction 방법보다 효율적이다.

###### MEEP: Is this Engaging? Prompting Large Language Models for Dialogue Evaluation in Multilingual Settings (https://aclanthology.org/2023.findings-emnlp.137/)
- Anthology ID: 2023.findings-emnlp.137 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 언어에서 대화 시 평가를 위해 대화 기록을 사용한 실시간 평가 기준이 필요한데, 기존의 자동화된 평가 메트릭은 대화 기록을 고려하지 않거나 특정 데이터셋에 한정돼 있으며 사람의 평가와 상관성이 제한적이었다.
    2. 저자들은 대규모 언어 모델(Large Language Models, LLMs)을 활용하여 멋있는(engaging) 대화의 평가를 위한 프롬프트 시스템을 제안한다.
    3. 저자들은 선별된 프롬프트 요소와 LLMs를 사용함으로써 다국어 대화에서 engagingness 평가에서 기존 방법들보다 뛰어난 성능을 보였다.

###### Exploring the Impact of Corpus Diversity on Financial Pretrained Language Models (https://aclanthology.org/2023.findings-emnlp.138/)
- Anthology ID: 2023.findings-emnlp.138 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 다양한 도메인 특화 사전 훈련 언어 모델(PLMs)이 제안되었으며, 생물의학, 과학 및 임상 분야와 같은 특수 영역에서 범용 PLM보다 우수한 성능을 보였다.
    2. 하지만 금융 데이터 분석의 경제적 영향이 크기 때문에 금융 PLMs에 대한 연구가 진행 중이며, 금융 PLMs는 충분히 다양한 금융 데이터로 사전 훈련되지 않았다는 문제점을 발견하였다. 
    3. 이 문제를 해결하기 위해 우리는 다양한 금융 말뭉치를 수집하고 이러한 다양한 데이터셋으로 Financial Language Model (FiLM)을 훈련시켰다. 실험 결과에서 FiLM은 기존 금융 PLMs뿐만 아니라 일반적인 도메인 PLMs보다 우수한 성능을 보인다는 것을 확인하였으며, 이 개선은 본문에서 제시한 방법을 통해 본문 그룹에 대해서도 달성될 수 있음을 입증하였다.

###### LLMDet: A Third Party Large Language Models Generated Text Detection Tool (https://aclanthology.org/2023.findings-emnlp.139/)
- Anthology ID: 2023.findings-emnlp.139 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델 (LLMs) 에서 생성된 텍스트는 고품질 인간 작성 텍스트에 근접하여, 거짓 정보 전파 및 학문적 부도에 잘못 사용될 수 있는 우려가 있습니다. 따라서 주어진 텍스트의 출처를 정확하게 식별할 수 있는 매우 실용적인 감지 도구가 긴급히 필요합니다. 
    2. 기존의 감지 도구들은 일반적으로 LLMs에 대한 액세스에 의존하며, 기계 생성 텍스트와 인간 작성 텍스트만 감지할 수 있으며, 미세한 추적, 중개 판단 및 신속한 감지의 요구 사항을 충족하지 못합니다. 
    3. 따라서 우리는 특정 LLMs (예: GPT-2, OPT, LLaMA 등) 을 통해 텍스트 출처를 파악할 수 있는 모델별, 안전하고 효율적이며 확장 가능한 감지 도구인 LLMDet을 제안합니다. LLMDet은 주요한 n-gram의 다음 토큰 확률을 기록하여 각 LLM의 Proxy Perplexity를 계산하는 기능을 가지고 있습니다. LLM의 Proxy Perplexities를 공동으로 분석함으로써 생성된 텍스트의 출처를 판단할 수 있습니다. 실험 결과, LLMDet은 높은 탐지 성능을 보여주며, 속도와 보안을 보장하며 인간 작성 텍스트를 인식하는 데 약 5배 빠르게 동작합니다. 추가로, LLMDet은 손쉽게 새로운 오픈 소스 모델에 대한 감지 기능을 확장할 수 있습니다. (https://github.com/TrustedLLM/LLMDet에서 오픈 소스 도구를 제공할 예정입니다.)

###### RECAP: Towards Precise Radiology Report Generation via Dynamic Disease Progression Reasoning (https://aclanthology.org/2023.findings-emnlp.140/)
- Anthology ID: 2023.findings-emnlp.140 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 방사선학 보고서 생성의 자동화는 방사선과사의 작업 부담을 크게 줄일 수 있다. 이전 연구는 예전부터 주로 문제점을 정확하게 파악하는 것에 중점을 두었으나, 환자의 현재 상태를 평가하는데 중요한 시간 정보를 무시하고 있다.
    2. 이 논문에서는, 두 개의 연속 방사선 사진을 기반으로 관찰과 진행 상황 (공간-시간 정보) 을 예측한 다음, 이를 토대로 보고서를 생성하는 RECAP을 제안한다.
    3. RECAP은 질병 진행 그래프와 동적 진행 추론 메커니즘을 고안하여 관찰과 진행의 속성을 정확하게 선택하는 방사선 보고서를 생성한다.

###### Causal Intervention for Abstractive Related Work Generation (https://aclanthology.org/2023.findings-emnlp.141/)
- Anthology ID: 2023.findings-emnlp.141 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Abstractive related work generation"은 독자들이 현재 연구를 이해하는 데 도움이 되는 일관성 있는 관련 작업을 생성하는 데에 관심이 증가하고 있다. 그러나 대부분의 기존 모델은 관련 작업 생성 중에 내재적인 인과 관계를 무시하여 잘못된 상관관계를 유발하고 이로 인해 모델의 생성 품질과 일반성이 저하된다.
    2. 이 연구에서는 인과적 개입이 이러한 한계를 해결하고 생성된 관련 작업의 품질과 일관성을 개선할 수 있다고 주장한다. 이를 위해 우리는 효과적으로 생성 과정에서 원인-결과 사이의 관계를 포착하기 위한 새로운 Causal Intervention Module for Related Work Generation (CaM)을 제안한다.
    3. CaM을 Transformer와 융합하여 end-to-end 관련 작업 생성 프레임워크를 얻을 수 있으며, 두 개의 실제 데이터셋에서 수행한 실험 결과, CaM은 효과적으로 모델이 인과 관계를 학습하고 더 높은 품질과 일관성의 관련 작업을 생성할 수 있도록한다.

###### G-SPEED: General SParse Efficient Editing MoDel (https://aclanthology.org/2023.findings-emnlp.142/)
- Anthology ID: 2023.findings-emnlp.142 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 인간의 지시를 이해하고 기대한 내용을 출력하여 작업 효율성을 크게 향상시킬 수 있다. 
    2. 본 논문에서는 General SParse Efficient Editing MoDel (G-SPEED)을 제안하여 최소한의 계산 비용으로 다양한 편집 요구를 충족시킬 수 있다. 
    3. 실험 결과는 G-SPEED가 175B 개의 파라미터를 갖는 대형 모델보다 우수한 성능을 보인다는 것을 보여준다.

###### Attack Prompt Generation for Red Teaming and Defending Large Language Models (https://aclanthology.org/2023.findings-emnlp.143/)
- Anthology ID: 2023.findings-emnlp.143 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 유해한 콘텐츠를 생성할 수 있는 red teaming 공격에 취약한데, 이전 연구는 수작업이나 자동 방법을 통해 공격 prompt를 구성하는 데 제한이 있다. 
    2. 이 논문에서는 지속가능한 공격 prompt를 경제적으로 생성하기 위해 수작업 방법과 자동 방법을 결합한 통합 접근법을 제안한다.
    3. 새롭게 제안된 공격 프레임워크와 방어 프레임워크를 통해 LLM의 안전성을 향상시키고, SAP라는 다양한 크기의 공격 prompt 데이터셋을 제공하여 더 많은 LLM의 안전성 평가와 개선을 용이하게 한다.

###### Smart “Chef”: Verifying the Effect of Role-based Paraphrasing for Aspect Term Extraction (https://aclanthology.org/2023.findings-emnlp.144/)
- Anthology ID: 2023.findings-emnlp.144 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "우리는 문장으로부터 Aspect Term을 자동으로 추출하는 ATE(Apsect Term Extraction) 작업에 접근한다. PLN 기반 추출기들이 많은 향상을 이루었다. 하지만 ATE corpora에는 많은 비정보적이고 낮은 품질의 문맥들이 포함되어 있다."
    2. "우리는 문맥 지향적인 품질 향상 방법을 탐구한다. 특히, 우리는 가상 전문가들의 관점에서 문장을 자동으로 다시 작성하는 방법을 제안한다. 이를 기반으로 우리는 훈련된 추출기를 사용하여 테스트 중에 paraphrased된 문장 위에서 ATE를 수행한다."
    3. "실험 결과, 우리의 접근 방식은 "al di la"와 같은 눈에 띄지 않는 aspect term들을 효과적으로 재호출할 수 있었으며, 이는 정확도를 떨어뜨리기는 하지만 기존 문장에서 얻은 예측을 확장하는 데 사용될 수 있다는 것이 입증되었다."

###### Multi-Defendant Legal Judgment Prediction via Hierarchical Reasoning (https://aclanthology.org/2023.findings-emnlp.145/)
- Anthology ID: 2023.findings-emnlp.145 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "다수의 피고인을 포함하는 형사 사실 설명은 일반적으로 복잡한 상호작용을 나타내며, 단일 피고인 사건에 대한 판례 예측 (LJP) 방법이 이를 제대로 처리하기 어렵다." 
    2. "이 문제를 해결하기 위해, 우리는 다수의 피고인 LJP 작업을 제안하며, 이 작업은 다수의 피고인 사건의 판결 결과 (예 : 법조, 혐의, 형벌 조건)를 자동으로 예측하는 것을 목표로 한다." 
    3. "Hierarchical Reasoning Network (HRN)이라는 다수의 피고인 LJP 방법을 도입하여 각 피고인의 범죄 관계, 판결 환경, 법조, 혐의, 형벌 조건을 결정하기 위해 계층적 추론 체인을 따르는 HRN 방법을 소개한다."

###### Interpreting Indirect Answers to Yes-No Questions in Multiple Languages (https://aclanthology.org/2023.findings-emnlp.146/)
- Anthology ID: 2023.findings-emnlp.146 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Yes-no 질문은 "예" 또는 "아니오"로 대답을 기대하지만, 사람들은 종종 극단적인 키워드를 건너뛰고 긴 설명으로 대답한다. 이 논문에서는 이 문제에 초점을 맞추고 8개 언어의 새로운 벤치마크를 발표한다.
    2. 우리는 훈련 데이터를 수집하기 위해 distant supervision 접근법을 제시하고, 극단적인 키워드를 포함하는 직접적인 대답이 간접적인 대답을 해석하는 모델 훈련에 유용하다는 것을 보여준다.
    3. 우리는 단일 언어의 fine-tuning이 관심 언어에 대해 distant supervision을 통해 훈련 데이터를 얻을 수 있는 경우에 유용하다는 것을 보여주며, cross-lingual fine-tuning은 항상 유익하다는 것을 보여준다.

###### Generalizing Few-Shot Named Entity Recognizers to Unseen Domains with Type-Related Features (https://aclanthology.org/2023.findings-emnlp.147/)
- Anthology ID: 2023.findings-emnlp.147 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 적은 데이터로 인식하는 NER 방법들은 낮은 자원 도메인에서 entity를 식별하는 데에 큰 진전을 보였으나, Out-of-Domain (OOD) 예제에는 여전히 어려움을 겪는다. 
    2. 이 논문에서는 OOD 예제에 대한 모델의 일반화를 위해 데이터 증강 기법을 사용하며, 도메인 간 지식 전이를 강화하는 프레임워크인 PLTR을 제안한다. 
    3. PLTR은 상호 정보 기준으로 entity type 관련 feature (TRF)를 추출하고, 각 OOD 예제에 대해 해당 TRF를 선택하여 고유한 프롬프트를 생성하여 모델의 능력을 향상시킨다.

###### Intervention-Based Alignment of Code Search with Execution Feedback (https://aclanthology.org/2023.findings-emnlp.148/)
- Anthology ID: 2023.findings-emnlp.148 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 코드 검색에서의 기본적인 목표 중 하나는 주어진 자연어 질의에 대해 기능적으로 정확한 코드를 검색하는 것입니다. 그러나 기존의 코드 검색 훈련 데이터는 정확성을 주장하기 위해 테스트 케이스를 실행하는 것이 필요하며, 이러한 실행 피드백을 긍정적인 것으로 인식합니다. 그러나 이 정규화는 모델의 검색 결정을 실제 정확성과 일치시키지 못할 수 있습니다.
    2. 이러한 제한을 해결하기 위해, 우리는 CIRL(Code Intervention-based Reinforcement Learning)을 제안합니다. 이는 훈련 코드를 개입시켜 모델의 결정을 왜곡시키고, 그 후 강화 학습을 통해 실행 피드백으로 이를 수정합니다. CIRL의 첫 번째 기술적 기여는 실제 실행 없이 개입으로부터 실행 피드백을 유발하는 것입니다.
    3. 두 번째로, CIRL은 단순한 어휘적 변경을 넘어 추상 구문 트리를 사용하여 구조적 개입을 도입합니다. 다양한 데이터셋에서의 실험적 결과는 CIRL이 기존 방법과 비교하여 효과적임을 보여줍니다.

###### Enhancing Neural Machine Translation with Semantic Units (https://aclanthology.org/2023.findings-emnlp.149/)
- Anthology ID: 2023.findings-emnlp.149 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 NMT 모델은 기본적으로 서브워드와 단어를 모델의 입력과 이해에 사용하지만, 실제 의미를 표현하는 데 필수적인 완전한 단어와 구문은 종종 의미 단위로 사용된다. 
    2. 이 논문에서는 문장 내의 의미 단위의 총 의미를 모델링하고, 이를 활용하여 문장을 이해하기 위한 새로운 관점을 제공하는 Semantic Units for Machine Translation (SU4MT) 방법을 제안한다. 
    3. 실험 결과에서는 우리의 방법이 의미 단위 수준의 정보를 효과적으로 모델링하고, 강력한 기준 모델보다 성능이 우수함을 보여준다.

###### DRAFT: Dense Retrieval Augmented Few-shot Topic classifier Framework (https://aclanthology.org/2023.findings-emnlp.150/)
- Anthology ID: 2023.findings-emnlp.150 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 정보의 증가로 인해 임의의 주제를 분류하는 수요가 점점 중요해지고 있다. DRAFT는 몇 개의 예시를 사용하여 특정 주제의 분류기를 훈련시키기 위해 설계된 간단한 프레임워크이다.
    2. DRAFT는 특정 주제와 관련된 여러 개의 질문을 효과적으로 처리하는 Multi-query retrieval (MQR) 알고리즘을 사용하여 Customized 데이터셋을 구축한다.
    3. DRAFT는 InstructGPT 175B와 같은 in-context learning을 사용하는 베이스라인과 비교했을 때, 177배 더 적은 파라미터를 가지면서도 few-shot 주제 분류 작업에서 경쟁력 있는 또는 우수한 성능을 보여주며 그 효과를 입증한다.

###### A Framework for Exploring Player Perceptions of LLM-Generated Dialogue in Commercial Video Games (https://aclanthology.org/2023.findings-emnlp.151/)
- Anthology ID: 2023.findings-emnlp.151 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템에 사용되는 LLM으로 생성된 대화를 포함한 비디오 게임의 플레이어 경험을 평가하는 것은 여전히 큰 도전이다. 이 논문에서는 역할극 비디오 게임에서 자주 사용되는 task-oriented 대화를 제어하는 대화 관리 시스템에 대한 동적 평가 프레임워크를 제안한다.
    2. *Disco Elysium: The Final Cut*이라는 역할 극 게임에서 대화를 추출하여 이를 데이터셋으로 사용하고, GPT-4를 사용하여 게임 상태를 표현하는 코드로 기반된 대화를 생성한다.
    3. 플레이어들에게 선호도 판단 및 자유양식 피드백을 통해 LLM 생성 결과를 게임 디자이너의 글과 비교 평가하였고, 전반적으로 게임 디자이너의 글이 더 선호되었다고 밝혔다.

###### Generative Calibration for In-context Learning (https://aclanthology.org/2023.findings-emnlp.152/)
- Anthology ID: 2023.findings-emnlp.152 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large Language Model, LLM)의 한 가지 흥미로운 특징인 in-context learning은 몇 가지 학습 예제만으로도 과연솔버를 속속들이 제작할 수 있게 해줍니다. 그러나 이는 다양한 프롬프트 설정에 민감하며 학습 예제의 선택이나 순서와 같은 설정에 따라 성능이 다릅니다.
    2. 저자들은 이 겂체의 모순이 LLM의 종속 변수 분포를 데이터 분포로 이동시키는 일종의 label shift 때문이라고 처음으로 이론적으로 및 경험적으로 밝혀냅니다. 이해를 통해 Monte-Carlo 샘플링을 통해 추정된 프롬프트 생성을 통해 라벨의 마진을 조정하여 예측 분포를 보정할 수 있게 됩니다.
    3. 저자들의 제안은 generative calibration이라는 방법으로, 12가지 텍스트 분류 작업과 774M에서 33B로 스케일이 조정된 12개의 LLM에서 철저한 실험을 수행하여 제안된 방법이 일반적으로 ICL 및 최첨단 보정 방법보다 약 27%까지 macro-F1에서 향상되었다고 보여줍니다. 또한, 제안된 방법은 다양한 프롬프트 설정에 대해서도 안정적입니다.

###### Chain of Thought with Explicit Evidence Reasoning for Few-shot Relation Extraction (https://aclanthology.org/2023.findings-emnlp.153/)
- Anthology ID: 2023.findings-emnlp.153 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 희소 학습 데이터로 관계 추출 문제를 해결하기 위해 CoT-ER (chain-of-thought with explicit evidence reasoning) 알고리즘을 제안한다. 
    2. CoT-ER은 대규모 언어 모델을 사용하여 task-specific하고 concept-level한 지식으로 증거를 생성하고 관계 추출에 명시적으로 사용한다. 
    3. 실험 결과, CoT-ER은 훈련 데이터 0%인 상황에서 Fully-Supervised (훈련 데이터 100%)로 비교했을 때 FewRel1.0과 FewRel2.0 데이터셋에서 경쟁력 있는 성능을 보여준다.

###### AdaTranS: Adapting with Boundary-based Shrinking for End-to-End Speech Translation (https://aclanthology.org/2023.findings-emnlp.154/)
- Anthology ID: 2023.findings-emnlp.154 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. End-to-end 음성 번역에서 데이터 부족 문제를 완화하기 위해 음성인식과 기계 번역 데이터에 대한 사전 훈련이 중요한 기술로 간주되고 있다. 그러나 음성과 텍스트 사이의 모달리티 갭으로 인해 사전 훈련 모델로부터 효율적으로 지식을 상속하는 것이 어렵다. 
    2. 이 논문에서는 end-to-end ST를 위한 AdaTranS를 제안한다. 이 모델은 단어 경계를 예측하여 음성과 텍스트 피처 간의 길이 불일치 문제를 완화하기 위해 새로운 shrinking 메커니즘을 사용하여 음성 피처를 적응시킨다. 
    3. MUST-C 데이터셋에서의 실험 결과, AdaTranS가 다른 shrinking 기반 방법보다 더 나은 성능, 더 빠른 추론 속도 및 더 낮은 메모리 사용량을 보였다. 추가적인 정렬 손실을 적용하면 성능을 더욱 개선할 수 있다는 실험 결과도 제시되었다.

###### No offence, Bert - I insult only humans! Multilingual sentence-level attack on toxicity detection networks (https://aclanthology.org/2023.findings-emnlp.155/)
- Anthology ID: 2023.findings-emnlp.155 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 black-box toxicity detector 모델에 대한 간단하면서도 효과적인 문장 수준 공격을 소개한다. 혐오 메시지 뒤에 몇 개의 긍정적인 단어나 문장을 추가하여 신경망의 예측을 변경하고 독성 감지 시스템의 체크를 통과할 수 있다.
    2. 이 접근 방식은 세 가지 다른 언어 군으로부터 일곱 개의 언어에서 작동함을 보여준다.
    3. 또한, 위에서 언급한 공격에 대한 방어 메커니즘을 설명하고 그 제한점에 대해 논의한다.

###### Manipulating the Perceived Personality Traits of Language Models (https://aclanthology.org/2023.findings-emnlp.156/)
- Anthology ID: 2023.findings-emnlp.156 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 대규모 언어 모델로부터 생성된 텍스트가 "Big Five"라는 성격 특성에 일관된지 여부를 조사한다. 예를 들어, GPT2와 같은 언어 모델은 파티에 가라고 하면 일관된 방식으로 응답할 것인가? 
    2. 우리는 또한 BERT와 GPT2와 같은 언어 모델이 다른 유형의 맥락(성격 설명이나 성격 특성에 대한 진단 질문에 대한 답변)에 노출되었을 때, 해당 맥락에서 성격 특징을 일관되게 인식하고 반영한다는 것을 보여준다.
    3. 이러한 행동은 일관적으로 특정 방식으로 조작될 수 있는 능력(의도한 성격 특성 변경과 실현된 변경 사이의 상관관계가 0.84까지 나타남)을 보여주며, 대화 시스템과 같은 응용 프로그램에서 페르소나(personas)를 제어하는 도구로 사용될 수 있다.

###### WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia (https://aclanthology.org/2023.findings-emnlp.157/)
- Anthology ID: 2023.findings-emnlp.157 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 반복 및 지연시간이 적은 대화능과 conversationality를 갖춘 거의 존스회할 일이 없는 최초의 few-shot LLM 기반 챗봇을 제시한다. 
    2. WikiChat은 영어 위키피디아에 기반을 둔데, LLM에서 응답을 생성하고, 기존에 있는 grounded facts만 보존하며, 긍정적이고 사실적인 응답을 형성하기 위해 전체 말뭉치에서 추가적인 정보를 검색한다. 
    3. LLM은 7B-parameter LLaMA 모델로 변환되며, 다양한 면에서 향상된 대화 시간, 비용, 개인정보 보호, 연구 및 배포가 가능하도록 한다.

###### Automated Few-Shot Classification with Instruction-Finetuned Language Models (https://aclanthology.org/2023.findings-emnlp.158/)
- Anthology ID: 2023.findings-emnlp.158 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최신 few-shot learning 접근법 중 하나인 로드맵(complement data samples)을 사용하는 언어 모델은 성공적이지만, 각 작업마다 로드맵을 수작업으로 설계하기 위해서는 도메인 지식과 상당한 추측이 필요하다.
    2. 이 논문에서는 AuT-Few라는 새로운 방법을 제안하여 수작업으로 만든 로드맵을 필요로하지 않게 한다. AuT-Few는 로드맵 검색 모듈과 교차 검증을 통한 두 가지 다른 의미를 가진 클래스 설명 생성 및 선택 메커니즘으로 구성되어 있다.
    3. 12개 데이터셋과 8개의 분류 작업에서 실험을 진행한 결과, AuT-Few가 현재 최첨단 few-shot learning 방법을 능가하는 성과를 보였고, 또한 RAFT few-shot benchmark에서 가장 우수한 순위를 달성하였다. 이러한 결과는 수작업으로 만든 로드맵을 사용하지 않은 새로운 작업에 대해서도 유효하다.

###### Meta-Learning of Prompt Generation for Lightweight Prompt Engineering on Language-Model-as-a-Service (https://aclanthology.org/2023.findings-emnlp.159/)
- Anthology ID: 2023.findings-emnlp.159 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 다양한 회사들이 Language-Model-as-a-Service (LMaaS)로 대형 언어 모델의 기능을 제공하고 있다. 하지만 자동 프롬프트 엔지니어링 기법이 고비용 연산이 필요한 이유때문에 이러한 기능을 제공하지 않는다.
    2. 이 논문에서는 LMaaS를 위한 경량 자동 프롬프트 생성 방법인 MetaL-Prompt을 제안한다. 이는 메타-러닝 접근 방식을 사용하여 특정 작업에 대한 추가적인 훈련 없이 언어 모델이 보다 강력한 학습을 할 수 있도록 한다. 또한, 기존 방법에 비해 계산 비용을 크게 절감시킨다.
    3. MetaL-Prompt을 QA 데이터셋에 대해 평가한 결과, 최첨단 기법인 P-tuning과 비교하여 평균 F1 점수 기준으로 최대 19.4%의 성능 향상을 보였으며, 계산 비용도 크게 줄일 수 있다.

###### Beneath Surface Similarity: Large Language Models Make Reasonable Scientific Analogies after Structure Abduction (https://aclanthology.org/2023.findings-emnlp.160/)
- Anthology ID: 2023.findings-emnlp.160 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 연구들은 단어 유추에 주목했지만, 본 연구는 대형 언어 모델이 이 유추의 기반인 구조를 간과하는 경향이 있다고 제안하며, 인간의 유추적 사고와 유사한 능력을 측정하는 대비 유추 (analogy structure abduction) 작업을 소개한다.
    2. SCAR라는 벤치마크를 통해 대비 유추를 평가하는데 사용되는 13개의 다양한 분야에서 400개의 과학적 대비를 포함시키고, 이 작업을 지원한다.
    3. ChatGPT와 GPT-4와 같은 대형 언어 모델들이 이 작업에서 여전히 도전을 겪고 있으며, 그 능력을 향상시키기 위한 미래 탐구의 필요성을 강조한다.

###### HiCL: Hierarchical Contrastive Learning of Unsupervised Sentence Embeddings (https://aclanthology.org/2023.findings-emnlp.161/)
- Anthology ID: 2023.findings-emnlp.161 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 지역 세그먼트-level과 전체 sequence-level 관계를 고려한 계층적 대조 학습 프레임워크인 HiCL을 제안한다. 기존의 방법들은 전체 시퀀스를 대조하기 위해 전체를 인코딩하므로 지역 표현 학습을 소홀히하고 짧은 텍스트에 대한 일반화에 어려움이 있었다. 
    2. HiCL은 시퀀스를 여러 세그먼트로 나누고 지역 및 전역 대조 학습을 활용하여 세그먼트 수준과 시퀀스 수준의 관계를 모델링하여 효과를 향상시킨다. 
    3. 또한, HiCL은 transformers의 입력 토큰에 대한 이차 시간 복잡도를 고려하여 먼저 짧은 세그먼트를 인코딩하고 이를 집계하여 시퀀스 표현을 얻는 방식으로 훈련 효율성을 향상시킨다. 실험 결과, HiCL은 STS 태스크에서 이전에 최고 성능을 보인 SNCSE 모델을 향상시키며, BERTlarge에서 평균적으로 +0.2%의 상승과 RoBERTalarge에서 +0.44%의 상승을 관찰하였다.

###### Density-Aware Prototypical Network for Few-Shot Relation Classification (https://aclanthology.org/2023.findings-emnlp.162/)
- Anthology ID: 2023.findings-emnlp.162 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근들어, few-shot relation classification은 많은 연구 관심을 불러일으켰지만, 훨씬 어려운 NOTA(none-of-the-above) 문제에 대해서는 더욱 탐구가 필요하다.
    2. 기존 연구들은 NOTA를 추가 클래스로 취급하고 이미 알려진 관계와 동일하게 처리하였으나, 이 방법은 NOTA 인스턴스들이 알려진 인스턴스와는 달리 이상치로 분포되어 있음을 고려하지 않는다.
    3. 이 논문에서는 unique training objectives를 설계하여 알려진 인스턴스와 NOTA 인스턴스를 분리하고 이상치로 취급함으로써 이상적인 인스턴스 분포를 달성하는 density-aware prototypical network (D-Proto)를 제안한다.

###### Improved Training of Deep Text Clustering (https://aclanthology.org/2023.findings-emnlp.163/)
- Anthology ID: 2023.findings-emnlp.163 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 전통적인 깊은 클러스터링 최적화 방법은 클러스터링 센터, 상호 정보, 거리 메트릭과 같은 정보를 활용하여 암묵적인 일반화 레이블을 구성하여 딥 모델을 최적화한다. 그러나, 클러스터링 정확성의 한계로 인해 생성된 일반화 레이블은 클러스터링 과정에서 다양한 정도의 오류를 가지며, 클러스터링 과정에 큰 간섭을 일으킨다.
    2. 이 논문에서는 샘플 간의 상관관계를 사용하여 경험적 위험 최소화의 관점에서 일반적인 딥 클러스터링 최적화 방법을 제안한다.
    3. 두 가지 전통적인 딥 클러스터링 방법에 대한 실험은 이 방법의 필요성과 효과를 입증한다.

###### RegaVAE: A Retrieval-Augmented Gaussian Mixture Variational Auto-Encoder for Language Modeling (https://aclanthology.org/2023.findings-emnlp.164/)
- Anthology ID: 2023.findings-emnlp.164 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 업데이트되지 않은 정보와 환각(hallucination)과 같은 언어 모델의 문제를 해결하기 위해, retrieval-augmented 언어 모델이 유망한 성과를 보이지만, 현재의 연구에서는 두 가지 주요 문제점이 있다.
    2. 우리는 유용한 검색된 정보는 현재의 소스 텍스트뿐만 아니라 미래의 타겟 텍스트까지 고려해야 한다고 주장합니다. 또한, 우리는 문맥 길이에 제한을 받고 노이즈에 영향을 받기 쉬운 명시적인 원시 텍스트 대신, 압축된 잠재 공간에서 유도된 잠재 변수를 사용하는 방법이 더 효율적이라고 제안합니다.
    3. RegaVAE는 VAE(변이형 오토 인코더)를 기반으로 구성된 retrieval-augmented 언어 모델로, 텍스트 말뭉치를 잠재 공간에 인코딩하며, 소스 텍스트와 타겟 텍스트에서 현재와 미래의 정보를 포착합니다. 또한, 우리는 VAE를 사용하여 잠재 공간을 초기화하고, 가우시안 사전 분포를 가우시안 혼합 분포로 확장하여 확률적인 검색 생성 패러다임을 채택합니다. 이론적 분석은 RegaVAE의 최적화 가능한 상한을 제공하며, 다양한 데이터셋에서의 실험 결과는 텍스트 생성 품질과 환각 제거에서 상당한 개선을 보여줍니다.

###### RefGPT: Dialogue Generation of GPT, by GPT, and for GPT (https://aclanthology.org/2023.findings-emnlp.165/)
- Anthology ID: 2023.findings-emnlp.165 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLM)은 높은 품질의 지시 데이터를 세밀 조정하여 다양한 NLP 작업을 수행할 수 있는 능력을 갖추었다. 그러나 고품질의 인간이 작성한 대화 데이터, 특히 다중 턴 대화의 수집은 대부분의 사람들에게는 비용이 많이 들고 어렵다. 
    2. 이 논문에서는 모델 환시 (model hallucination)로 인한 사실적 오류를 걱정하지 않고 거대하고 진실하고 맞춤형 대화를 생성하기 위한 RefGPT라는 방법을 제안한다. 
    3. RefGPT는 LLM을 이용한 대화 생성에서 모델 환시 문제를 해결하기 위해 모델이 자체 지식이 아닌 주어진 참고 자료를 활용하도록 제한하고, 이전 연구에서 무시된 각 발언에 대한 상세한 제어기능을 추가한다.

###### INA: An Integrative Approach for Enhancing Negotiation Strategies with Reward-Based Dialogue Agent (https://aclanthology.org/2023.findings-emnlp.166/)
- Anthology ID: 2023.findings-emnlp.166 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 온라인 마켓플레이스를 위해 디자인된 새로운 협상 에이전트를 제안한다. 
    2. 이 에이전트는 가격뿐만 아니라 거래 번들에서 아이템의 추가나 제거와 같은 다른 요소들에 대해서도 협상할 수 있는 능력을 가지고 있다. 
    3. 제안된 방법은 협상 능력을 크게 향상시키며, 인수 또는 배제 등 거래 번들을 동적으로 조정할 수 있는 능력을 보여준다.

###### Large Language Models are Better Reasoners with Self-Verification (https://aclanthology.org/2023.findings-emnlp.167/)
- Anthology ID: 2023.findings-emnlp.167 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 문장 사슬 (CoT) 프롬프팅을 통해 GPT-3와 같은 대규모 언어 모델이 산술, 상식, 논리 추론과 같은 여러 NLP 태스크에서 강력한 추론 능력을 보여주고 있다.
    2. 그러나, CoT를 사용한 언어 모델은 다단계 프롬프팅과 다중 토큰 예측이 필요하여 개인 실수에 민감하고 오류가 누적될 수 있다.
    3. 따라서 이 논문에서는 셀프-검증(self-verification) 기술을 제안하여 언어 모델이 스스로 답을 검증하고 가장 높은 점수의 후보 답을 선택할 수 있도록 한다. 실험 결과는 이 방법이 산술, 상식, 논리 추론 데이터셋에서 추론 성능을 향상시킬 수 있다는 것을 보여준다.

###### Multi-Granularity Information Interaction Framework for Incomplete Utterance Rewriting (https://aclanthology.org/2023.findings-emnlp.168/)
- Anthology ID: 2023.findings-emnlp.168 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 Incomplete Utterance Rewriting (IUR) 접근법은 불완전한 발화를 수정하는데 필요한 단어들의 출처를 파악하지 못하고, 관련 없는 발화에서 단어들을 도입한다.
    2. 우리는 multi-granularity의 의미 정보를 포착하기 위해 context selection, edit matrix construction, relevance merging을 포함한 새로운 효과적인 multi-task 정보 상호작용 프레임워크를 제안한다.
    3. 우리의 접근법은 관련 있는 발화를 가져오고 중요한 단어를 파악하는 이점을 갖고 있어 기존의 최첨단 모델들을 이 분야에서 능가한다.

###### Accuracy is not enough: Evaluating Personalization in Summarizers (https://aclanthology.org/2023.findings-emnlp.169/)
- Anthology ID: 2023.findings-emnlp.169 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 요약 모델은 ROUGE, BLEU, METEOR, BERTScore, PYRAMID, readability 등 다양한 지표를 사용해 정확도와 품질을 평가한다. 그러나 독자의 취향에 따라 요약의 중요성은 주관적이므로 주어진 문서에 대한 "적합한" 요약은 존재하지 않을 수 있다.
    2. 따라서 많은 경우 요약 모델이 사용자 프로필에 맞게 개인화되어야 하는데, 현재로서는 요약 모델의 개인화 정도를 평가하는 방법이 없다.
    3. 이 논문에서는 기존의 정확도 측정 방법이 어떤 요약 모델의 개인화 정도를 평가할 수 없음을 증명하고, 개인화 정도를 자동으로 측정하기 위한 새로운 측정 지표인 EGISES를 제안한다. 이를 Microsoft Research에서 공개한 PENS 데이터셋을 사용해 실험하고, 개인화를 명시적으로 학습한 모델과 개인화를 구현한 모델을 포함한 총 10개의 최신 요약 모델의 개인화 정도를 분석한다. 마지막으로 개인화를 고려하는 새로운 정확도 측정 방법인 P-Accuracy를 제안하고, 메타평가를 통해 이 측정 방법의 강건성과 신뢰성을 검증한다.

###### For Generated Text, Is NLI-Neutral Text the Best Text? (https://aclanthology.org/2023.findings-emnlp.170/)
- Anthology ID: 2023.findings-emnlp.170 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 추론(NLI)을 텍스트 생성 파이프라인에 통합하는 방법을 탐구한다. 그들은 사전 훈련된 NLI 모델을 사용하여 생성된 문장이 prompt와 이전 텍스트와 동등하거나 모순되거나 중립인지를 판단하는 데 사용한다.
    2. 이 논문은 GPT-3가 만드는 오류들의 예측에 NLI 작업이 도움이 된다는 것을 보여준다. 이 결과를 사용하여 GPT-J에 대한 NLI 기반 생성 절차를 개발한다.
    3. 실험 결과, Laugaveglur (nucleus sampling randomness parameter) 값이 높을 때는 NLI를 entailment (동등성)을 최대화하는 전략을 사용하는 것이 텍스트 생성을 개선시키는 반면, 낮을 때는 contradiction (모순성)을 최대화하는 전략이 효과적이라는 것을 보여준다. 하지만, 매개변수 값에 관계없이 neutral (중립) 클래스를 최대화하는 NLI 전략이 가장 높은 품질의 생성된 텍스트를 제공한다. (vanilla generations 보다 유의미하게 우수)

###### Combining Counting Processes and Classification Improves a Stopping Rule for Technology Assisted Review (https://aclanthology.org/2023.findings-emnlp.171/)
- Anthology ID: 2023.findings-emnlp.171 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 Technology Assisted Review (TAR) stopping rule은 수작업으로 문서의 관련성을 평가하는 비용을 줄이기 위해 검토해야 할 문서의 수를 최소화하기 위해 개발되었다. 
    2. 이 연구에서는 추가적인 주석 없이 훈련할 수 있는 텍스트 분류기로부터 유도된 정보를 사용하여 효과적인 stopping rule을 확장하였다. 
    3. 다양한 데이터셋 (CLEF e-Health, TREC Total Recall, TREC Legal and RCV1)에서 시행한 실험 결과, 제안된 접근 방식이 성능을 일관되게 향상시키고 다른 대안적인 방법보다 우수한 결과를 보여주었다.

###### Complexity-Guided Curriculum Learning for Text Graphs (https://aclanthology.org/2023.findings-emnlp.172/)
- Anthology ID: 2023.findings-emnlp.172 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 커리큘럼 학습은 훈련 과정을 점진적으로 세분화하여 다양한 예시에 노출함으로써 일반화 능력을 향상시키는 체계적인 학습 방법을 제공한다. 본 논문에서는 텍스트 그래프 데이터와 함께 학습하기 위해 텍스트 및 그래프 복잡성 형식에 대한 기존 지식을 기반으로 하는 커리큘럼 학습 방법을 소개한다.
    2. 제안된 모델은 더 많은 데이터를 이용하고, 더 적은 데이터를 사용한다. 훈련 과정에서 일관적으로 텍스트를 그래프 복잡성 지수보다 선호하며, 텍스트와 그래프 복잡성 지수에서 나온 최적의 커리큘럼은 동일한 효과를 가져온다. 이 모델은 GNN 모델과 데이터셋에 걸쳐 전송 가능한 커리큘럼을 학습한다.
    3. 또한, 노드 수준(지역)과 그래프 수준(전역) 복잡성 지수뿐만 아니라 얕은 및 전통적인 텍스트 복잡성 지수가 효과적인 커리큘럼 학습에 중요한 역할을 한다는 것을 발견하였다.

###### CoVariance-based Causal Debiasing for Entity and Relation Extraction (https://aclanthology.org/2023.findings-emnlp.173/)
- Anthology ID: 2023.findings-emnlp.173 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. entity 및 relation 추출 과제는 명명된 entity를 인식하고 동시에 relation을 추출하는 것을 목표로 한다. 그러나 데이터 선택 편향 및 분포 편향과 같은 다양한 데이터 편향의 문제로 전이성, 견고성 및 일반화에 대한 모델의 위험이 증가하고 있다.
    2. 우리는 인과 관점에서 위의 문제들을 해결하는 것을 목표로 한다. 우리는 feature representations를 최적화하고 일반적인 debiasing을 수행하기 위해  ̲covariance and  ̲variance  ̲optimization (OVO)이라는 새로운 인과적 프레임워크를 제안한다.
    3. OVO를 entity 및 relation 추출 작업에 적용한 결과, 두 개의 널리 사용되는 데이터셋에서 세 가지 강력한 기준에 효과적이며 일반화할 수 있음을 보여준다. 또한 미세한 분석 결과, OVO가 long-tail 분포의 영향을 완화하는 능력을 갖고 있다는 것을 보여준다.

###### Multi-label and Multi-target Sampling of Machine Annotation for Computational Stance Detection (https://aclanthology.org/2023.findings-emnlp.174/)
- Anthology ID: 2023.findings-emnlp.174 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 수동 레이블링을 통한 데이터 수집은 데이터 기반 방법의 도메인 특화된 지도를 제공하며, 합리적인 성능을 얻기 위해서는 잘 주석이 된 자원들의 상당량이 필요하다.
    2. 이 논문에서는 대용량 언어 모델을 활용하여 자동 주석 작업에 대한 유효성을 조사하였다. 
    3. 우리의 방법을 채택한 실험 결과들은 성능과 학습 효과를 크게 향상시킬 수 있음을 보여주었다.

###### In What Languages are Generative Language Models the Most Formal? Analyzing Formality Distribution across Languages (https://aclanthology.org/2023.findings-emnlp.175/)
- Anthology ID: 2023.findings-emnlp.175 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다국어 생성 언어 모델 (LM)은 여러 언어에서 많은 숙련도를 보여주고 있다. 그러나 이러한 모델의 예측에는 어떤 문화적 편향이 생기는지는 여전히 알려지지 않았다.
    2. 이 논문에서는 문화적인 영향을 받는 언어 속성 중 하나인 "정형성(formality)"을 분석한다.
    3. 다양한 모델과 언어들 간에 다양한 행동을 관찰하며, 생성된 텍스트의 정형성에 대한 다국어 LMs의 영향을 측정한다.

###### MaXM: Towards Multilingual Visual Question Answering (https://aclanthology.org/2023.findings-emnlp.176/)
- Anthology ID: 2023.findings-emnlp.176 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 Visual Question Answering (VQA)은 영어로 주로 연구되었으며, 다른 언어로의 mVQA에는 많은 자원이 필요하다. 본 논문에서는 데이터 및 모델링 측면에서 mVQA의 scalable 한 솔루션을 제안한다.
    2. 기존 방식인 질문-답변 수집에 필요한 인력을 줄이기 위해 번역 기반의 프레임워크를 mVQA 데이터 생성에 제안하였다.
    3. Crossmodal-3600 데이터셋의 다국어 캡션을 활용하여 효율적인 주석 프로토콜을 개발하고, MaXM이라는 7개 언어의 VQA 벤치마크를 생성하였다.

###### Efficient Latent Variable Modeling for Knowledge-Grounded Dialogue Generation (https://aclanthology.org/2023.findings-emnlp.177/)
- Anthology ID: 2023.findings-emnlp.177 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "지식 기반 대화 생성은 대화적 맥락을 기반으로 적절한 외부 지식을 검색하고 이를 기반으로 대답을 생성하는 것을 요구한다. 기존의 방법은 지식 검색 모듈과 응답 생성 모듈을 따로 훈련시켜왔으나, 특히 개방형 대화에서는 중간 라벨을 얻는 것이 비용이 많이 든다. 이 논문에서는 중간 변수 모델링을 통해 이러한 라벨 필요성을 줄이는 효율적인 알고리즘을 제안한다."
    2. "우리의 알고리즘은 복잡한 검색 모델을 직접 학습시키는 대신, 일반적인 모델을 사용하여 질의 생성 모델을 적용하며, 질의 생성 모델과 응답 생성 모델을 동시에 학습한다. 또한, 적절한 훈련 목적 함수와 수정된 증거의 하한을 사용하여 학습을 안정적으로 수행한다."
    3. "다양한 지식 기반 대화 데이터셋에서의 실험 결과, 우리의 방법은 주석된 지식을 사용하지 않고도 지식 기반 대화 작업에서 지도 학습 알고리즘보다 훨씬 성능이 우수하며 효율적이고 확장 가능함을 보였다."

###### Ask To The Point: Open-Domain Entity-Centric Question Generation (https://aclanthology.org/2023.findings-emnlp.178/)
- Anthology ID: 2023.findings-emnlp.178 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "엔티티 중심의 질문 생성" (ECQG) 이라는 새로운 작업을 소개한다. 이 작업은 주제별 학습, 도움을 받은독서, 사실 검증과 같은 실제 응용 프로그램에서 동기를 얻었다. 이 작업은 엔티티의 관점에서 질문을 생성하는 것을 목표로 한다. 
    2. 이 작업을 해결하기 위해 요약된 PLM 기반 프레임워크 GenCONE을 제시하며, 이 프레임워크는 두 개의 새로운 모듈인 콘텐츠 초점화 기능과 질문 검증을 제공한다. 
    3. 우리는 또한 SQuAD에서 대규모의 오픈 도메인 데이터셋을 구축하여 이 작업을 지원한다. 우리의 um이우는 GenCONE이 다양한 기준선보다 유의미하고 일관되게 우수한 결과를 보여주며, 두 모듈은 높은 품질의 질문을 생성하는 데 효과적이고 보완적임을 보여준다.

###### Self-prompted Chain-of-Thought on Large Language Models for Open-domain Multi-hop Reasoning (https://aclanthology.org/2023.findings-emnlp.179/)
- Anthology ID: 2023.findings-emnlp.179 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 개방 도메인 질의응답 (ODQA)에서는 대부분의 질문이 상식에 따른 단일 점프 추론(single-hop reasoning)을 필요로 한다. 이 논문에서는 더 확장된 개방 도메인 다중 점프 추론 (ODMR)을 소개하고, 개방 도메인에서 명시적인 추론 과정을 거친 다중 점프 질문에 대한 답을 찾는 과제를 제시한다.
    2. 이 논문에서는 Self-prompted Chain-of-Thought (SP-CoT)라는 자동화된 프레임워크를 제안하는데, 이는 LLMs (large language models)의 고성능 CoT 생성을 위해 사용되는 LLMs에 의해 만들어진다. SP-CoT은 고품질 ODMR 데이터셋의 자동 생성 파이프라인, 문맥 내 CoT 선택을 위한 적응형 샘플러, 그리고 문맥 학습을 통한 자기 프롬프팅 추론을 도입한다.
    3. 실험 결과, SP-CoT는 4개의 다중 점프 질의응답 벤치마크에서 SOTA 방법들을 대폭 초월하며, 큰 규모의 LLMs에서는 거의 2배의 zero-shot 성능 향상을 보인다. 추가적인 분석에서는 SP-CoT이 MuSiQue-Ans 데이터셋에서는 중간 답변의 약 50%를 회상하여 직접적이고 간결한 중간 추론 단계를 도출하는 뛰어난 능력을 보인다.

###### CASE: Commonsense-Augmented Score with an Expanded Answer Space (https://aclanthology.org/2023.findings-emnlp.180/)
- Anthology ID: 2023.findings-emnlp.180 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLM은 학습 과정에서 얻은 지식 덕분에 NLP 태스크에서 인상적인 zero-shot 성능을 보여주었다. 하지만 multiple-choice QA 태스크에서 사용되는 LM 확률은 각 선택지의 타당성을 나타내는 불완전한 지표로 사용되는데, 이 기본 점수의 주요한 한계는 모든 단어를 동등하게 다룬다는 것이다.
    2. 이 논문에서는 단어의 중요도 가중치를 부여하여 개별 단어가 입력 내의 다른 단어와의 의미적 관계에 기반하여 중요도를 결정하는 CASE라는 설명 추가 점수를 제안한다.
    3. 또한 선택지와 개념적으로 유사한 다양한 응답을 생성함으로써 응답 공간을 확장하고, 이를 기존 방법과 결합하면 5가지 공통 감각 기준에서 강력한 기준 모델을 능가하는 결과를 얻을 수 있음을 실험을 통해 보여주었다.

###### GRENADE: Graph-Centric Language Model for Self-Supervised Representation Learning on Text-Attributed Graphs (https://aclanthology.org/2023.findings-emnlp.181/)
- Anthology ID: 2023.findings-emnlp.181 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 downstream tasks를 위해 표현 학습을 위한 self-supervised 방법이 많은 연구 주목을 받고 있습니다. 그러나, 기존 방법들은 구조적 컨텍스트 정보의 완전한 범위를 포착하기 어렵거나 과제별 훈련 레이블에 의존하는 등 실제 상황에서의 효과성과 일반성을 크게 저해합니다. 
    2. 우리는 텍스트 속성 그래프에서의 self-supervised 표현 학습 문제를 해결하기 위해 새로운 GRENADE (Graph-Centric Language model)를 개발했습니다. 
    3. GRENADE는 사전 훈련된 언어 모델과 그래프 신경망의 시너지를 활용하여 그래프 중심의 비교 및 지식 조정을 통해 정보성 텍스트 의미론과 구조적 컨텍스트 정보를 효과적으로 포착합니다. 실험 결과, GRENADE는 최첨단 방법들에 비해 우수성을 보여주었습니다.

###### Sources of Hallucination by Large Language Models on Inference Tasks (https://aclanthology.org/2023.findings-emnlp.182/)
- Anthology ID: 2023.findings-emnlp.182 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델 (LLM)은 질문 답변 및 요약과 같은 응용 작업에 필요한 자연어 추론 (NLI)의 능력을 가질 수 있는 것으로 주장되며, 우리는 이들을 향한 통제된 실험을 통해 그들의 행동을 조사한 설명과 함께 시범을 제시한다.
    2. 우리는 사전 훈련에서 비롯된 두 가지 편향성을 확립하고, 이것들이 생성형 LLMs의 환각의 주요 원인임을 보여준다. 첫째, 문장 수준에서의 암기: 우리는 모델이 훈련 데이터에서 가설 이행을 표시할 때, 무관하게 전제가 무엇이든 잘못된 NLI 테스트 샘플을 잘못된 것으로 분류함을 보여준다. 둘째, 말뭉치 수준에서 학습된 통계적 패턴: 훈련 데이터에서 전제 술어가 가설 술어보다 덜 빈번한 경우에도 유사한 효과가 나타나며, 이는 이전 연구에서 유추되는 편향이다.
    3. 우리는 이러한 편향에 부합하지 않는 NLI 테스트 샘플에서 LLMs의 성능이 부적합한 것으로 안 내고, 이들을 미래 LLM 평가에 유용한 검증 자료로 제시한다.

###### Efficient Long-Range Transformers: You Need to Attend More, but Not Necessarily at Every Layer (https://aclanthology.org/2023.findings-emnlp.183/)
- Anthology ID: 2023.findings-emnlp.183 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 학습된 transformer 모델들은 다양한 자연어 처리 태스크에서 놀라운 성능을 보여주고 있으나, full attention 메커니즘은 계산 비용이 높기 때문에 긴 시퀀스를 다루는 작업에는 적합하지 않다.
    2. 본 논문에서는 MASFormer라는 transformer variant를 제안하여 full attention을 몇 개의 레이어에서만 사용하고 나머지 레이어에서는 sparse attention을 사용하여 계산 비용을 줄이면서도 복잡한 dependency를 캡처할 수 있다.
    3. 실험 결과, 1.3B parameter로 이루어진 MASFormer 모델은 full attention을 사용하는 vanilla transformer와 비교하여 연산 비용을 현저히 줄이면서 경쟁력 있는 성능을 보이고, 긴 시퀀스 데이터를 이용한 계속적인 training의 효과와 시퀀스 길이가 downstream generation 성능에 어떤 영향을 미치는지도 조사하였다.

###### Prompting ChatGPT in MNER: Enhanced Multimodal Named Entity Recognition with Auxiliary Refined Knowledge (https://aclanthology.org/2023.findings-emnlp.184/)
- Anthology ID: 2023.findings-emnlp.184 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어에서의 다중모달 Named Entity Recognition (MNER)은 이미지 기반 단서를 포함하여 텍스트 엔티티 예측을 향상하는 것을 목표로 한다. 기존 연구들은 적절한 이미지 정보의 활용을 극대화하거나 명시적인 지식 베이스에서 외부 지식을 통합하는 데 주로 초점을 맞추고 있다. 
    2. 그러나 이러한 방법들은 모델에 외부 지식 제공의 필요성을 간과하거나 검색된 지식에서 과도한 중복 문제에 부딪힌다. 
    3. 본 논문에서는 ChatGPT를 암묵적인 지식 베이스로 활용하고, 보조적인 효율적인 엔티티 예측을 위해 직관적으로 보조 지식을 생성할 수 있도록 하는 PGIM - 2단계 프레임워크를 제시한다.

###### Understanding HTML with Large Language Models (https://aclanthology.org/2023.findings-emnlp.185/)
- Anthology ID: 2023.findings-emnlp.185 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large language models, LLMs)은 다양한 자연어 처리 작업에서 뛰어난 성능을 보여주었지만, HTML 이해 능력인 웹페이지의 원시 HTML 구문 분석, 웹 기반 작업 자동화, 크롤링 및 브라우저 지원 검색과 같은 응용 분야는 아직 완전히 탐구되지 않았다.
    2. 본 논문은 HTML 이해를 위한 모델과 세 가지 작업에 대한 심층 분석을 제시한다: (i) HTML 요소의 의미론적 분류, (ii) HTML 입력에 대한 설명 생성 및 (iii) HTML 페이지의 자동 웹 탐색.
    3. 기존 연구들은 HTML 이해를 위해 전용 아키텍처와 학습 절차를 개발해왔지만, 우리는 표준 자연어 말뭉치로 사전 학습된 LLMs가 HTML 이해 작업에 대하여 놀라울 정도로 전이 학습이 잘 되는 것을 보여준다.

###### The PEACE-Reviews dataset: Modeling Cognitive Appraisals in Emotion Text Analysis (https://aclanthology.org/2023.findings-emnlp.186/)
- Anthology ID: 2023.findings-emnlp.186 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인식 평가는 감정을 해석하는데 중요한 역할을 한다. 이 연구는 다양한 형태의 인식 평가와 기쁨, 분노와 같은 특정 감정과의 상호작용을 고객 상황에서 알아보는 영역이다.
    2. PEACE-Reviews 데이터셋은 고객의 개인적인 제품이나 서비스와의 상호작용 중 인식 경험과 감정을 다룬 주관적인 기록들의 독특한 컴필레이션으로, 구매에 대한 평가와 결과적인 감정에 대한 참가자들의 심리적 특성과 평가적 피드백을 깊이 분석한다.
    3. PEACE-Reviews 데이터셋은 감정, 인식, 개인 특성 및 인구 통계 데이터를 포함하며, 자서전적 이야기를 기반으로 특정 기능을 예측하는 초기 모델을 소개한다.

###### UReader: Universal OCR-free Visually-situated Language Understanding with Multimodal Large Language Model (https://aclanthology.org/2023.findings-emnlp.187/)
- Anthology ID: 2023.findings-emnlp.187 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 문서, 웹사이트, 사진 등에서 중요한 정보를 전달하는 텍스트는 우리의 시각적 세계에서 널리 사용된다. 본 논문에서는 Multimodal Large Language Model (MLMM)을 기반으로 한 OCR-free 시각적 언어 이해 모델인 UReader를 제안한다. 
    2. MLLM의 얕은 텍스트 인식 능력을 활용하여 이전의 작업들에 비해 파라미터의 1.2%만을 finetuning하며 훈련 비용이 훨씬 낮다. 
    3. 업데이트되지 않은 단일 모델로 10가지 시각적 언어 이해 작업 중 8가지에서 최첨단 성능을 달성하였다.

###### Loose lips sink ships: Mitigating Length Bias in Reinforcement Learning from Human Feedback (https://aclanthology.org/2023.findings-emnlp.188/)
- Anthology ID: 2023.findings-emnlp.188 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "사람의 피드백으로부터의 강화 학습은 대규모 언어 모델을 인간과 사회적 가치와 조화롭게 만들기 위한 중요한 다리 역할을 한다." 
    2. "그러나 우리는 보상 모델이 종종 그 의도된 목적을 우회하기 위한 단축키를 찾는다는 것을 발견했다. 이로 인해 모델이 더 긴 출력을 선호하는 경향이 생기는데, 이는 이러한 출력 내에서 유용한 정보의 증가를 의미하지 않는다."
    3. "이 논문에서는 sequence length의 영향으로부터 보상 모델링을 분리하기 위해 Product-of-Experts (PoE) 기법을 적용하는 혁신적인 해결책을 제안한다. 실험 결과는 우리의 접근 방식의 효과를 검증하며, sequence length와 관계없이 언어 모델의 성능이 향상되는 것을 보여준다."

###### Filling the Image Information Gap for VQA: Prompting Large Language Models to Proactively Ask Questions (https://aclanthology.org/2023.findings-emnlp.189/)
- Anthology ID: 2023.findings-emnlp.189 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 자연어 태스크와 함께 open-domain knowledge-based 시각 질의 응답(OK-VQA)과 같은 몇 개의 시각-언어 태스크에서도 인상적인 추론 능력과 세계 지식을 유지한다. 
    2. 그러나 이미지는 LLM에게 표시되지 않으므로 연구자들은 이미지를 텍스트로 변환하여 LLM을 시각적 질문 추론 과정에 참여시킨다.
    3. 이 논문에서는 LLM이 더 많은 세부사항을 드러내기 위해 관련 질문을 주도적으로 제기하고 생성된 정보를 정제하는 필터를 포함한 프레임워크를 설계한다.

###### Take a Closer Look at Multilinguality! Improve Multilingual Pre-Training Using Monolingual Corpora Only (https://aclanthology.org/2023.findings-emnlp.190/)
- Anthology ID: 2023.findings-emnlp.190 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구에서는 병렬 코퍼스를 사용하지 않고 사전 훈련된 다국어 사전 훈련 언어 모델(mPLMs)의 현저한 언어간 능력이 밝혀졌지만, 공간 임베딩의 유사성이 그런 능력의 이유일 것으로 추측되었지만, 이는 미개척된 분야이다.
    2. 이 논문에서는 단어 기준의 정렬 특성을 조사하고, 공간 임베딩의 유사성과 일치함을 발견했다. 그러나, cross-lingual 상호작용이 부족하므로 mono-mPLMs는 높은 레이어에서 공간 임베딩의 유사성을 파괴할 가능성이 높아지며, cross-lingual 전이 능력이 제한된다.
    3. 이 문제를 해결하기 위해 병렬 문장에 의존하지 않고 mono-mPLMs의 레이어 간 cross-lingual 상호작용을 명시적으로 향상시키기 위해 토큰 수준과 의미 수준의 코드 스위치 마스크 언어 모델링을 도입한다. 이 방법을 다양한 자연어 이해 작업과 비지도 기계 번역 작업에서 평가했고, 결과는 강력한 기준 모델을 능가하며, 병렬 코퍼스로 훈련된 mPLMs와 비슷한 성능을 달성하였다.

###### LogiCoT: Logical Chain-of-Thought Instruction Tuning (https://aclanthology.org/2023.findings-emnlp.191/)
- Anthology ID: 2023.findings-emnlp.191 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Generative Pre-trained Transformer 4 (GPT-4)는 뛰어난 연속적인 추론 능력을 가지고 있다. 그러나 이전의 self-instruction tuning 기술들은 일반적인 작업에 탁월한 성능을 보였지만, 복잡한 추론 작업에 한계가 있다. 이 논문에서는 GPT-4와 함께 논리적 연속적인 추론을 가르치기 위한 LogiCoT라는 새로운 instruction-tuning 데이터셋을 소개한다."
    2. "LogiCoT는 GPT-4 모델에게 논리적인 추론을 유도하기 위한 instruction 집합이다. 이 데이터셋은 모델에게 일반적인 추론 능력을 가르치고자 하는 목적으로 수집되었으며, 복잡한 추론 작업을 처리하는 데 도움을 준다."
    3. "논문에서는 GPT-4가 연속적인 추론을 생성하기 위한 instruction을 수집하는 과정을 상세히 설명하고 있다."

###### Hiding in Plain Sight: Tweets with Hate Speech Masked by Homoglyphs (https://aclanthology.org/2023.findings-emnlp.192/)
- Anthology ID: 2023.findings-emnlp.192 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 혐오 발언에 대한 모니터링 애플리케이션을 우회하기 위해, 혐오 발언의 생산자들은 종종 문제와 비슷한 유니코드 문자인 'homoglyph'로 비속어의 한 개 이상의 글자를 대체한다. 
    2. 본 연구에서는 homoglyph가 포함된 실제 혐오 발언을 수집하는 것이 어렵기 때문에, 문자 대체 스크래핑 방법을 개발하여 Offensive Tweets with Homoglyphs (OTH) 데이터셋 (N = 90,788)을 구축하였다.
    3. 다양한 transformer 기반 혐오 발언 탐지 모델의 성능을 평가해본 결과, zero-shot 환경에서의 성능이 낮았지만 데이터 정규화를 통해 탐지 성능을 크게 향상시킬 수 있다는 것을 보여준다. 부가적으로 주석이 달린 데이터로 모델을 훈련시키면 성능이 더욱 향상되며, homoglyph를 알고 있거나 스크래핑 스크립트에서 모르는 homoglyph를 포함하는 데이터셋을 수집하고, 신경망 모델을 훈련하여 난장이된 실제 혐오 발언을 인식하는 데 사용될 수 있다.

###### Reducing Spurious Correlations in Aspect-based Sentiment Analysis with Explanation from Large Language Models (https://aclanthology.org/2023.findings-emnlp.193/)
- Anthology ID: 2023.findings-emnlp.193 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 Aspect-Based Sentiment Analysis (ABSA) 모델이 매우 유망한 결과를 보여주고 있다. 그러나 이 모델은 특정 단어와 출력 레이블 사이의 표면적인 상관관계를 학습하므로, 이 컨텍스트에서는 spurious correlation (가짜 상관관계) 문제가 발생할 수 있다. 
    2. 이 문제를 해결하기 위해, 우리는 큰 언어 모델(Large Language Models, LLMs)로부터 각 aspect의 sentiment 극성에 대한 설명을 활용하여 ABSA에서 spurious correlation을 줄이는 방법을 제안한다. 
    3. 다양한 데이터셋과 몇 가지 대표적인 ABSA 모델을 통합한 방법을 실험한 결과, 우리의 방법은 성능 향상을 이끌어내며 ABSA 모델의 성능과 일반화 능력을 향상시킬 수 있다.

###### High-quality argumentative information in low resources approaches improve counter-narrative generation (https://aclanthology.org/2023.findings-emnlp.194/)
- Anthology ID: 2023.findings-emnlp.194 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 작은 규모의 fine-tuning에도 언어 모델의 성능을 크게 향상시킬 수 있다는 것이 보여지고 있는데, 이 논문에서는 작은 학습 크기에도 hate speech 반언 생성(task)에 매우 효과적인 highly targeted fine-tuning이 어떻게 작용하는지 보여준다. 
    2. 이 작업에서는 단일 논쟁 전략에 집중하며, 해당 전략과 관련된 논쟁 분석을 함께 제공하여 소량의 예제 세트를 제공하면 전체 반언 세트를 제공하는 것과 동등한 수준의 반언을 생성해낸다. 
    3. 또한 fine-tuning에 긍정적인 영향을 미치기 위해서는 좋은 기본 모델이 필요한 것으로 나타났는데, 특히 스페인어의 경우 fine-tuning 없이 얻은 반언 대부분이 받아들일 수 없을 정도로 낮은 품질이었으며, fine-tuning으로 전체적인 품질이 개선되기는 하였지만 여전히 비만족스러운 수준이었다.

###### A Reference-free Segmentation Quality Index (SegReFree) (https://aclanthology.org/2023.findings-emnlp.195/)
- Anthology ID: 2023.findings-emnlp.195 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 처리(NLP)에서의 주제 분할은 문맥의 의미 변화시 문장들을 분할하고 구분하는 것을 의미한다. 현재 이 분할의 품질을 평가하기 위해서는 사람이나 알고리즘에 의한 분할을 실제 분할과 비교하여 평가해야 한다. 이 논문은 사람 평가자 없이도 분할 품질을 측정하기 위해 참조 없는 분할 품질 지표(SegReFree)를 제안한다. 
    2. 제안된 메트릭은 문장의 의미적 임베딩을 사용하여 변형된 군집 유효성 메트릭을 적용하여 분할 품질을 결정한다. 
    3. 기존의 참조 기반 분할 메트릭과의 비교를 통해 제안된 메트릭은 강력한 상관관계를 보이며, 해당 메트릭을 구현한 파이썬 라이브러리가 공개되었다.

###### In-context Learning for Few-shot Multimodal Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.196/)
- Anthology ID: 2023.findings-emnlp.196 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구들은 몇몇 entity category에 대한 다량의 주석이 담긴 자료가 있기 때문에 multimodal named entity recognition(MNER)에서 우수한 성능을 달성하였으나, 실제 상황에서는 사전에 모든 entity category를 나열하는 것은 불가능하다. 
    2. 본 논문에서는 소량의 labeled 예제만을 사용하여 텍스트-이미지 쌍 내의 named entity를 효과적으로 탐지하고 식별하는 FewMNER 과제를 제안한다. 
    3. 이미지 모달리티를 텍스트로 변환하여 대규모 언어 모델이 시각적 모달리티로부터 정보를 흡수하도록 하고, 텍스트와 이미지 모달리티의 유사도 순위 합의 랭킹을 사용하여 유용한 예제를 선택하여 task demonstration 환경을 구성하며, 각 entity 카테고리의 의미와 MNER 정의를 효과적인 지시사로 활용하는 프레임워크가 기준 모델들보다 우수한 성능을 보인다는 실험 결과를 제시한다.

###### On Uncertainty Calibration and Selective Generation in Probabilistic Neural Summarization: A Benchmark Study (https://aclanthology.org/2023.findings-emnlp.197/)
- Anthology ID: 2023.findings-emnlp.197 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 요약을 위한 딥 모델은 인상적인 성능을 달성하지만, 예측적 불확실성을 잘못하여 신뢰성과 신뢰성이 저하되는 현실 응용 분야에서 높은 확신을 낮은 품질의 예측에 할당한다. 
    2. 이 논문에서는 복잡한 자기회귀 요약 작업에서 다양한 최신 확률적 방법의 효과를 철저히 조사하고 평가 프로토콜을 통해 불확실성 품질을 개선한다. 
    3. 확률적 방법은 모델의 생성 및 불확실성 품질을 일관되게 향상시키며, 낮은 품질의 요약을 피하는 것에 대한 우수한 성능을 실증적으로 입증하고 있다.

###### Handshape-Aware Sign Language Recognition: Extended Datasets and Exploration of Handshape-Inclusive Methods (https://aclanthology.org/2023.findings-emnlp.198/)
- Anthology ID: 2023.findings-emnlp.198 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 수화인식 연구는 수어의 음운론적 특성을 명확히 고려하지 않고 수화 비디오를 인코딩한다. 하지만 수어에서는 손 모양이 중요한 매개변수이기 때문에, 손 모양을 고려한 수화인식에 대한 가능성을 탐구한다.
    2. PHOENIX14T 데이터셋을 손 모양 레이블로 확장하여 PHOENIX14T-HS 데이터셋을 생성한다.
    3. 단일 인코더 네트워크와 듀얼 인코더 네트워크를 활용한 손 모양 포함 수화인식의 새로운 방법론을 제안하고, CTC 손실과 프레임 수준의 크로스 엔트로피 손실을 동시에 최적화하는 학습 전략을 사용한다. 이러한 방법은 기존의 성능을 일관되게 개선한다.

###### SimCKP: Simple Contrastive Learning of Keyphrase Representations (https://aclanthology.org/2023.findings-emnlp.199/)
- Anthology ID: 2023.findings-emnlp.199 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 키워드 생성(KG)은 소스 문서가 주어졌을 때 요약하는 단어나 구를 생성하는 것을 목표로하며, 키워드 추출(KE)은 텍스트에서 이를 식별하는 것을 목표로합니다. 현재의 통합 접근 방식은 주로 토큰 수준에서 작동하는 순차 레이블링 및 최대화 기반 생성을 채택하여 전체적인 키워드를 관찰하고 점수를 매기는 데 실패합니다.
    2.  이 논문에서는 SimCKP라는 간단한 대조 학습 프레임 워크를 제안하며, 이는 두 단계로 구성됩니다. 첫 번째는 어떤 문서에도 나타나지 않는 키워드도 생성하면서 대조적인 방식으로 문맥을 고려하는 구문 수준 표현을 학습하여 키워드를 추출하는 추출기-생성기입니다. 두 번째는 생성 된 각 구문과 해당 문서의 표현을 정렬하여 점수를 조정하는 재순위 모델입니다.
    3. 다중 벤치마크 데이터셋에서의 실험 결과는 우리가 제안하는 방법의 효과를 입증하며, 최신 모델을 상당히 능가합니다.

