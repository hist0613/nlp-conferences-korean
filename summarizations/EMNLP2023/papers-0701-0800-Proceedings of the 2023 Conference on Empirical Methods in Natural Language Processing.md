# Korean Three-Line Summarizations of Papers 701-800 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### Interventional Rationalization (https://aclanthology.org/2023.emnlp-main.700/)
- Anthology ID: 2023.emnlp-main.700 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "선택적인 서술은 신경망의 해석성을 향상시키기 위해 입력의 부분집합 (rationales) 을 선택하여 예측 결과를 설명하는 것이다. 기존 방법들은 아직도 데이터의 연관성(spurious correlations)에 의존하여 서술을 구성하고 예측을 한다는 문제가 있다."
    2. "본 연구에서는 인과 이론에 영감을 받아 인과 서술을 발견하기 위해 interventional rationalization (Inter-RAT)를 개발한다. 구조적인 인과 모델을 사용하여 입력, 서술, 결과 간의 인과관계를 분석하고, 인과관계에서 confounder를 식별하여 입력과 서술, 서술과 결과 간의 spurious correlations을 발견한다."
    3. "또한, 인과적 수식 개입 방법을 제안하여 들어오는 방향의 역방향 조정을 통해 입력과 서술 사이의 spurious correlations을 제거한다. 이를 통해 우리는 선택된 서술과 결과 사이의 연관성을 제거하면서 서술의 희소성 제약의 한계를 분석하고 이 연관성을 제거한다."

###### Don’t Take This Out of Context!: On the Need for Contextual Models and Evaluations for Stylistic Rewriting (https://aclanthology.org/2023.emnlp-main.701/)
- Anthology ID: 2023.emnlp-main.701 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 문체적 텍스트 재작 방법과 평가 메트릭은 문장 수준에서 작동하기 때문에 텍스트의 넓은 문맥을 무시하면 일반적이고 모호하며 일관성 없는 재작을 선호할 수 있다. 
    2. 이 논문에서는 문장이 나타나기 전의 텍스트 문맥을 문체적 텍스트 재작의 재작과 평가 단계에 통합하는 방법을 조사하고, 원래 문장과 문맥적 일관성을 결합한 새로운 평가 메트릭인 CtxSimFit를 소개한다. 
    3. 비문맥적과 문맥적 재작을 호의하는 것을 비교적으로 실험한 결과, 인간은 문맥적 재작을 비문맥적인 재작보다 훨씬 적합하고 자연스러워 평가하여, 기존의 문장 수준 자동 평가 메트릭 (ROUGE, SBERT 등)은 인간에 의한 선호와 상관 관계가 낮음을 보였다.

###### Axiomatic Preference Modeling for Longform Question Answering (https://aclanthology.org/2023.emnlp-main.702/)
- Anthology ID: 2023.emnlp-main.702 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT나 GPT-4와 같은 대형 언어 모델의 놀라운 능력은, 인간의 선호도를 보상 모델에 인코딩하여 강화학습하고자 하는 과정에서 부분적으로 유래한다.
    2. 이 논문에서는 인간의 선호도에 대한 가이드라인을 식별하고 이를 유지하기 위해 다양한 선호 신호를 생성하기 위한 공리적인 프레임워크를 개발한다.
    3. 이 프레임워크를 사용하여 긴 형식의 질문에 대한 답변의 점수를 매기기 위한 모델을 훈련시켰고, 이 모델은 GPT-4보다 더 자주 인간의 선호도와 일치하는 결과를 나타냈다.

###### Countering Misinformation via Emotional Response Generation (https://aclanthology.org/2023.emnlp-main.703/)
- Anthology ID: 2023.emnlp-main.703 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회적 보정은 소셜미디어 플랫폼(SMP)에서의 거짓 정보 확산에 대한 신뢰성 있는 방법이다. 
    2. 기존의 작업에서 거짓 정보를 사회적 보정하는 데 사실 확인자가 간접적으로 참여하지만 소셜 미디어 커뮤니케이션에서 흔히 사용되는 스타일과 기법과 통합된 참여는 시도한 적이 없다. 
    3. 이 논문에서는 VerMouth라는 첫 번째 대형 데이터 세트를 제시하고, 이 데이터 세트를 사용하여 훈련 된 모델이 출력 품질과 일반화 능력 측면에서 상당한 개선을 보여주는 포괄적인 실험을 제공한다.

###### Seq2seq is All You Need for Coreference Resolution (https://aclanthology.org/2023.emnlp-main.704/)
- Anthology ID: 2023.emnlp-main.704 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 coreference resolution 작업에서는 task-specific 모델이 최고의 성능을 내기 위해 필수적이라고 주장한다. 그러나 이 연구에서는 그런 모델이 필요하지 않다는 설득력 있는 증거를 제시한다.
    2. 연구자들은 사전 학습된 seq2seq transformer 모델을 finetuning하여 coreference 주석을 인코딩하는 태그된 시퀀스로 입력 문서를 매핑하는 방법을 사용한다. 이렇게 간단한 모델이 문헌에서 최고의 coreference 시스템에 근접하거나 그보다 우수한 성능을 보여준다.
    3. 더 간단한 seq2seq 모델 버전을 고려하여 태그된 구간만 생성하는 방법도 높은 성능을 보이며, 모델 크기, 감독 비율, 시퀀스 표현 선택 등이 성능에 중요한 영향을 미침을 분석 결과로 보여준다.

###### Integrating Language Models into Direct Speech Translation: An Inference-Time Solution to Control Gender Inflection (https://aclanthology.org/2023.emnlp-main.705/)
- Anthology ID: 2023.emnlp-main.705 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 스피치 번역 시스템은 말하는 사람을 지칭하는 단어를 번역할 때 기본 남성 성적인 것이나 오해를 일으킬 수 있는 음성 특성에 의존해서는 안 된다. 대신 스피커의 선호에 따라 성별을 할당해야 한다.
    2. 기존의 해결책들은 효과적이지만, 성별으로 라벨링된 ST 데이터에서 전용 모델을 재훈련해야 하는 등 실제적으로 적용하기 어렵다.
    3. 본 논문에서는 ST에서 스피커와 관련된 성별 변형을 제어하기 위한 첫 번째 추론 시점 솔루션을 제안한다. 실험결과, 해당 솔루션은 기본 모델 및 훈련 시 최적화 전략에 비해 여성형에 대해 최대 31.0점 및 1.6점의 성별 정확도 향상을 보였다. 음성 특성이 해당 성별과 충돌하는 어려운 상황에서는 훨씬 큰 향상 (최대 32.0 및 3.4)이 있었다.

###### StoryAnalogy: Deriving Story-level Analogies from Large Language Models to Unlock Analogical Understanding (https://aclanthology.org/2023.emnlp-main.706/)
- Anthology ID: 2023.emnlp-main.706 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인류 추론에 있어서 서사 간 유추는 중요하다. 이 논문에서는 사람들이 유추를 인식하고 생성하는 능력을 평가하기 위해, StoryAnalogy라는 대규모 스토리 수준의 유추 말뭉치를 구축하였다.
    2. 제안한 평가는 유추 식별과 생성의 첫번째 평가로서, 문장 임베딩 모델에게 어려운 성과를 보였다. ChatGPT와 LLaMa와 같은 최신 규모의 언어 모델도 식별 성능에서 인간의 성능을 따라잡지 못하였다.
    3. 또한, StoryAnalogy의 데이터가 LLMs에서 유추 생성의 품질을 향상시킬 수 있다는 것을 관찰했으며, fine-tuned FlanT5-xxl 모델은 zero-shot ChatGPT와 비교 가능한 성능을 보였다.

###### Beyond Detection: A Defend-and-Summarize Strategy for Robust and Interpretable Rumor Analysis on Social Media (https://aclanthology.org/2023.emnlp-main.707/)
- Anthology ID: 2023.emnlp-main.707 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어의 영향력이 증가함에 따라 가짜 뉴스에 노출될 가능성이 높아지고 있다. 이 논문에서는 텍스트 콘텐츠와 전파 경로를 분석하여 소셜 미디어에서 가짜 뉴스를 탐지하는 방법을 제안한다. 
    2. 기존의 탐지 모델들은 응답 레벨에서 흔히 관측되는 악의적인 공격을 고려하지 않고 있으며, 해석 가능성도 떨어진다. 
    3. 이 논문에서 제안하는 DAS 프레임워크는 비슷한 의견을 공유하는 응답을 걸러내고 추출 및 요약 방식으로 각 대화 스레드의 응답 게시물을 요약하여 다중 관점의 예측 설명을 제공한다.

###### Crystal: Introspective Reasoners Reinforced with Self-Feedback (https://aclanthology.org/2023.emnlp-main.708/)
- Anthology ID: 2023.emnlp-main.708 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이전의 관점의 연속성(chain-of-thought) 및 그 변형과 같은 기존의 공통 감성 추론 방법은 공통 감성 추론에 필요한 "introspective"한 지식을 포착하기에 부족하며, 생성과 활용 사이의 상호 적응을 설명하는 데 어려움이 있다. 
    2. 이 논문에서는 **Crystal**이라는 새로운 방법을 제안하여 감성 추론에 필요한 introspection과 knowledge-grounded 추론 모드를 상호 점검하고 조정한다. 
    3. 실험 결과는 Crystal이 표준 감독 지도 기법 및 chain-of-thought 초집악 방식보다 우수한 성능을 보이며 공통 감성 추론 과정의 투명성을 향상시킨다는 것을 보여준다.

###### DiffS2UT: A Semantic Preserving Diffusion Model for Textless Direct Speech-to-Speech Translation (https://aclanthology.org/2023.emnlp-main.709/)
- Anthology ID: 2023.emnlp-main.709 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. diffusion generative models가 이미지 생성에서 큰 성공을 거두었지만, 특히 번역과 같은 음성 생성 작업에 효과적으로 적용하는 것은 어려운 문제이다.
    2. 저밀도 음성 데이터의 경우, 변환된 이산적인 음성 단위 sequence는 대응되는 텍스트 전사보다 훨씬 더 긴데, 이는 기존 자기 회귀 모델에 큰 도전 과제를 제기한다.
    3. 이 논문에서는 연속적인 음성 표현 공간에서 정확한 확산 과정을 적용하고, 이산적인 음성 단위 공간에서 역확산 과정을 적용하여 새로운 확산 모델을 제안한다.

###### BioFEG: Generate Latent Features for Biomedical Entity Linking (https://aclanthology.org/2023.emnlp-main.710/)
- Anthology ID: 2023.emnlp-main.710 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 생물의학 텍스트 처리에서 필수적인 과제인 생물의학 entity linking은 많은 경우에 드문 생물 기관들이라는 특성으로 인해 어렵다. 이러한 미처 개념하지 않은 entity들을 이해하는 데 제한이 있어 전통적인 생물의학 entity linking 모델들은 여러 종류의 링킹 오류가 발생한다.
    2. 본 논문에서는 BioFEG라는 새로운 latent feature generation 프레임워크를 제안한다. 이 프레임워크는 도메인 지식을 활용하여 생성적 적대 신경망을 훈련시켜 미처 개념하지 않은 entity들에 대한 latent 시맨틱 feature를 생성한다. 이러한 feature를 활용하여 모델은 드문 entity가 관련된 모호한 언급에 대해 보다 정확한 링킹 결정을 내릴 수 있게 된다.
    3. 두 개의 벤치마크 데이터셋에서의 실험을 통해 우리가 제안한 프레임워크의 우수성을 입증하였다.

###### TRIGO: Benchmarking Formal Mathematical Proof Reduction for Generative Language Models (https://aclanthology.org/2023.emnlp-main.711/)
- Anthology ID: 2023.emnlp-main.711 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 언어 생성 모델의 추론 능력을 탐구하기 위해 자동 정리 증명 (ATP)이 매력적인 도메인이 되었다. 그러나, 기존 ATP 벤치마크는 주로 상징적 추론에 초점을 맞추었고, 복잡한 숫자 조합 추론을 포함하지 않았다.
    2. 이 논문에서는 TRIGO라는 ATP 벤치마크를 제안한다. 이 벤치마크는 모델이 단계별로 증명을 하여 삼각함수 표현식을 간소화하는 능력을 요구하며, 또한 공식의 추론 능력과 숫자 항들을 조작, 그룹화, 인수분해하는 능력을 평가한다.
    3. 우리는 웹에서 삼각함수 표현식과 그 간소화된 형태를 수집하고, 이를 수동으로 간소화하는 과정을 주석 처리하고, "Lean" 공식 언어 시스템으로 번역한다. 또한, 주석 처리된 샘플에서 추가적인 예제를 자동으로 생성하여 데이터셋을 확장한다.

###### Physician Detection of Clinical Harm in Machine Translation: Quality Estimation Aids in Reliance and Backtranslation Identifies Critical Errors (https://aclanthology.org/2023.emnlp-main.712/)
- Anthology ID: 2023.emnlp-main.712 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기계 번역(MT)의 실용 적인 사용에서 사용자들은 출력에 얼마나 의존해야 하는지를 결정하기 위한 번역 품질에 대한 정보가 부족하다. 
    2. 품질 평가 연구의 진전은 MT 품질을 자동으로 평가할 수 있는 기법을 제공하지만, 이러한 기법들은 어느 특정한 사용 환경 외부에서 사람의 판단과 비교하여 평가되는 경우가 주로다.
    3. 이 논문에서는 비상실에서의 응급실 퇴원 지시서를 사용하여 품질 평가 피드백을 실제 고위험 의료 환경에서 인간 연구로 평가한다. 품질 평가를 기반으로 한 적절한 의존 및 backtranslation은 QE만으로는 감지할 수 없는 임상적으로 더 위험한 오류를 의사들이 감지하는 데 도움이 된다.

###### Vicarious Offense and Noise Audit of Offensive Speech Classifiers: Unifying Human and Machine Disagreement on What is Offensive (https://aclanthology.org/2023.emnlp-main.713/)
- Anthology ID: 2023.emnlp-main.713 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 욕설 감지는 콘텐츠 모더레이션의 중요한 요소이지만, 욕설에 대한 판단은 주관적일 수 있다. 이 논문은 실제 사회 웹 정치적 담론에서 머신과 인간 모더레이터가 어떻게 욕설에 대해 의견 차이를 가지는지 조사한다.
    2. 연구 결과, 모더레이터(인간 및 머신) 간의 의견 차이가 크며, 정치적 성향을 기반으로 다른 인간 판정자가 어떻게 응답할지 예측하는 것은 어렵다는 것을 보여준다.
    3. 자연스러운 노이즈의 조합으로 모더레이션 결과가 크게 다르며, 정치적 성향과 민감한 문제는 일인칭 및 간접적인 욕설에 모두 영향을 미친다.

###### Generating Summaries with Controllable Readability Levels (https://aclanthology.org/2023.emnlp-main.714/)
- Anthology ID: 2023.emnlp-main.714 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 읽기 가능성은 텍스트를 이해하기 쉬운 정도를 나타내며, 텍스트의 복잡성, 주제 및 독자의 배경 지식 등 여러 요인이 영향을 미친다. 
    2. 이 논문에서는 세밀한 제어를 통해 특정 읽기 가능성 수준에서 요약을 생성하는 기술을 연구한다. 
    3. CNN/DM 데이터셋을 기반으로 한 실험 결과, 우리의 생성 방법은 다양한 읽기 가능성 메트릭과 인간 판단을 통해 읽기 가능성 제어를 크게 개선시키며, 요약에서 제어 가능한 읽기 가능성에 대한 강력한 기준을 제시한다.

###### mAggretriever: A Simple yet Effective Approach to Zero-Shot Multilingual Dense Retrieval (https://aclanthology.org/2023.emnlp-main.715/)
- Anthology ID: 2023.emnlp-main.715 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 정보 검색(MLIR)은 인간 주석이 필요하여 데이터 생성이 많은 노력을 요구하는 난해한 작업이다. 이 논문에서는 mAggretriever를 소개하는데, 이 모델은 사전 훈련된 다국어 transformer (mBERT와 XLM-R)의 의미적 및 어휘적 특징을 효과적으로 활용하여 밀집 검색(dense retrieval)을 수행한다. 
    2. mAggretriever는 근사 마스킹 언어 모델 예측을 사용하여 어휘적 특징을 계산하는데, 이를 통해 훈련 및 추론 효율성을 향상시킨다. 이를 통해 mAggretriever는 영어 훈련 데이터에만 fine-tuning 된 경우에도 대규모 MLIR 훈련 데이터로 추가 훈련을 받은 기존 최첨단 다국어 밀집 검색 모델보다 우수한 성능을 보인다. 
    3. 추가적으로, 이 논문에서는 mAggretriever의 코드를 url에서 확인할 수 있다.

###### CodeFusion: A Pre-trained Diffusion Model for Code Generation (https://aclanthology.org/2023.emnlp-main.716/)
- Anthology ID: 2023.emnlp-main.716 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 마치 마지막 한 줄만 수정 가능한 개발자처럼, 이 논문에서는 자연어로부터의 코드 생성 모델에서 이전 토큰을 다시 고려하기 어렵다는 한계를 극복하기 위해 CodeFusion을 제안한다.
    2. CodeFusion은 완전한 프로그램을 반복적으로 노이즈를 제거하며 생성하기 때문에 이전에 생성된 토큰을 쉽게 재고려할 수 있으며, Bash, Python, Microsoft Excel 조건부 서식 (CF) 규칙에 대한 자연어에서 코드로의 생성 작업에서 우수한 성능을 보인다.
    3. CodeFusion은 자연어와의 조화를 잘 유지하여, top-1 정확성은 상위 방법들과 비슷하지만, top-3 및 top-5 정확성에서 상위 방법들보다 우수한 성능을 보인다.

###### CESAR: Automatic Induction of Compositional Instructions for Multi-turn Dialogs (https://aclanthology.org/2023.emnlp-main.717/)
- Anthology ID: 2023.emnlp-main.717 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Instruction-based multitasking(지시 중심의 다중작업)은 다중 턴 대화 애플리케이션에서 대형 언어 모델의 성공에 중요한 역할을 한다. 그러나 공개적으로 사용 가능한 대형 언어 모델은 ChatGPT와 같은 최신 모델에 비해 복잡한 지시 사항과 여러 제약 조건을 가진 경우 성능이 떨어진다.
    2. 본 논문에서는 복잡한 지시사항을 포함하는 대규모 집합을 사용하여 이러한 격차를 좁히는 것이 중요하다는 가설을 세운다. 다중 턴 대화 애플리케이션에 초점을 맞추어, CESAR라고 불리는 새로운 프레임워크를 제안한다.
    3. CESAR를 InstructDial과 함께 사용하여 구성적인 지시(language)를 포함하는 복합 작업(composite tasks)을 도출하는 방법을 개발하였다. 이에 따라 InstructDial++이라는 새로운 벤치마크가 생성되었으며, 이를 활용하여 63개 데이터셋, 86개 기본 작업 및 68개의 복합 작업을 포함하였다.

###### VECHR: A Dataset for Explainable and Robust Classification of Vulnerability Type in the European Court of Human Rights (https://aclanthology.org/2023.emnlp-main.718/)
- Anthology ID: 2023.emnlp-main.718 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 취약성을 인식하는 것은 필요한 지원을 제공하기 위해 개인을 권한을 부여하는 데 중요하다. 하지만 취약성의 개념은 ECtHR에서는 알려져 있지 않으며, NLP 연구가 이에 대하여 다루지 않았다.
    2. 따라서, 우리는 VECHR이라는 새로운 전문가 주석이 달린 다중 라벨 데이터셋을 제안하여 취약성 유형 분류와 설명 근거를 포함하여 ECtHR에서의 연구를 가능하게 한다.
    3. 우리의 결과는 예측 성능과 모델과 전문가 간의 제한된 일치로 인해 작업의 난이도를 보여준다. 또한, 모델의 out-of-domain 데이터 처리에 대한 강건성을 분석하고 전체적으로 제한된 성능을 관찰한다.

###### ACQUIRED: A Dataset for Answering Counterfactual Questions In Real-Life Videos (https://aclanthology.org/2023.emnlp-main.719/)
- Anthology ID: 2023.emnlp-main.719 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다중모달 카운터팩트럴 추론은 AI 시스템에게 중요하지만 도전적인 능력이다. 이는 비전과 언어 입력을 기반으로 가상의 상황의 결과를 예측하는 것을 의미하며, 이를 통해 AI 모델은 실패로부터 학습하고 가정적인 시나리오를 탐색할 수 있다.
    2. 그러나 실제 세계의 다양한 시나리오와 추론 차원에서 모델의 일반화 능력을 신뢰할 수 있는 벤치마크로 삼기 어렵게 만드는 합성 환경이나 특정 유형의 이벤트에 대한 접근만 가능한 몇 개의 데이터셋만 존재한다.
    3. 이 논문에서는 ACQUIRED라는 비디오 질의응답 데이터셋을 개발하여 실제 다양성에 초점을 맞추고, 물리적, 사회적, 시적 등 세 가지 추론 차원을 포괄적으로 평가할 수 있는 신뢰할 수 있는 벤치마크를 제공한다.

###### From Parse-Execute to Parse-Execute-Refine: Improving Semantic Parser for Complex Question Answering over Knowledge Base (https://aclanthology.org/2023.emnlp-main.720/)
- Anthology ID: 2023.emnlp-main.720 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실행 가능한 논리 형식으로 질문을 파싱하는 것은 지식 기반 질문-답변(KBQA)에서 탁월한 결과를 보여주었지만, 복잡한 KBQA는 복잡한 다단계 추론을 수행해야 하는 더 어려운 작업입니다. 
    2. 이 논문에서는 간단한 파싱-실행-개선 패러다임을 통해 의미 파서의 추론 능력을 풀어낼 수 있는 방법을 탐구합니다. 
    3. 제안된 PER-KBQA는 복잡한 추론 작업의 능력을 크게 향상시킬 수 있는 것을 벤치마크 데이터셋 상의 실험을 통해 보여줍니다.

###### Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model (https://aclanthology.org/2023.emnlp-main.721/)
- Anthology ID: 2023.emnlp-main.721 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델은 다양한 하위 응용 프로그램에서 효과적이나 종종 문제가되는 텍스트를 생성한다. 
    2. 우리는 보상 증강 디코딩(Reward-Augmented Decoding, RAD)을 소개하여 언어 모델이 특정 속성을 가진 텍스트를 생성하도록 유도하는 텍스트 생성 절차를 제안한다.
    3. 우리의 실험 결과는 RAD가 생성 절차만 변경하는 기존 방법들보다 우수한 성능을 보이고 언어 모델 재학습이 필요한 최신 방법들과도 성능이 일치함을 보여준다. 또한 RAD가 매우 큰 언어 모델에서 효과적이며 최소한의 컴퓨팅 오버헤드를 유발하는 것을 검증한다.

###### CORE: A Few-Shot Company Relation Classification Dataset for Robust Domain Adaptation. (https://aclanthology.org/2023.emnlp-main.722/)
- Anthology ID: 2023.emnlp-main.722 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. CORE는 회사 관계와 비즈니스 엔티티에 초점을 맞춘 few-shot relation classification (RC)을 위한 데이터셋으로, 회사 Wikipedia 페이지에서 추출한 12가지 관계 유형의 4,708개 인스턴스와 해당 텍스트 증거를 포함하고 있다. 
    2. CORE 데이터셋은 회사 이름과 비즈니스 엔티티로 인해 다양한 정보가 연결되기 때문에 few-shot RC 모델에 대한 도전을 제공한다. 
    3. CORE 데이터셋에 대한 실험 결과, 기존 도메인에서 훈련된 모델은 CORE에 적응하기 어려워 성능 차이가 크다는 것을 확인했다. 또한 CORE에 훈련된 모델은 영역 일반화에 대한 중요성을 강조하면서 가짜 관련 동사와 같은 표면적인 단서에 의존하지 않고 문맥적 뉘앙스에 집중할 수 있게 해준다는 것을 발견했다.

###### Models See Hallucinations: Evaluating the Factuality in Video Captioning (https://aclanthology.org/2023.emnlp-main.723/)
- Anthology ID: 2023.emnlp-main.723 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 비디오 캡션은 비디오에 대한 자연어로 이벤트를 설명하는 것을 목표로 하지만, 모델이 생성하는 문장들 중 56%가 사실적 오류를 포함하고, 기존 평가 메트릭은 인간의 사실성 주석과 거의 상관관계가 없음을 발견했다.
    2. 우리는 비디오 캡션에서 사실성의 인식이 중요한 문제임을 보여주기 위해 인간 평가와 사실성 주석을 바탕으로 비디오 캡션의 사실성을 재평가하기 위한 약한 지도학습 모델 기반 메트릭인 FactVC를 제안하였다.
    3. FactVC는 이전 메트릭보다 비디오 캡션의 사실성 평가에서 뛰어난 성능을 보였다.

###### Back Transcription as a Method for Evaluating Robustness of Natural Language Understanding Models to Speech Recognition Errors (https://aclanthology.org/2023.emnlp-main.724/)
- Anthology ID: 2023.emnlp-main.724 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 말하는 대화 시스템에서, 음성 인식 시스템의 성능이 자연어 이해 모델의 성능을 저하시킬 수 있다. 
    2. 본 논문에서는 음성 인식 오류가 NLU 모델의 성능에 미치는 영향을 조사하기 위한 방법을 제안한다. 
    3. 제안된 방법은 역전사 절차와 NLU 모델의 성능에 영향을 주는 오류들을 세분화하는 기술을 결합한 것이다.

###### Cabbage Sweeter than Cake? Analysing the Potential of Large Language Models for Learning Conceptual Spaces (https://aclanthology.org/2023.emnlp-main.725/)
- Anthology ID: 2023.emnlp-main.725 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Conceptual Spaces" 이론은 개념의 의미를 나타내는 인식-언어 인지 프레임워크로, 실제 체감적인 특징들과 대응되는 품질 차원들의 집합으로 구성된다. 이 논문에서는 대형 언어 모델(Large Language Models, LLMs)이 개념 공간을 배우는 데에 활용될 수 있는 가능성을 탐구한다.
    2. 실험 결과, LLMs는 어느 정도 의미 있는 표현을 학습하는 데에 사용될 수 있음을 보여준다. 그러나 BERT 계열의 세밀하게 조정된 모델은 GPT-3 모델보다 작은 크기에도 불구하고 일치하거나 더 나은 성능을 발휘할 수 있다.
    3. 이러한 결과는 큰 규모의 모델보다 작은 모델이 문제에 특화된 표현을 더 잘 학습한다는 점에서 흥미로운 결과를 제시한다.

###### Can Language Models Understand Physical Concepts? (https://aclanthology.org/2023.emnlp-main.726/)
- Anthology ID: 2023.emnlp-main.726 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델(LMs)이 상호작용과 실체 세계에서 중요한 전제조건인 물리 개념을 이해할 수 있는지 알 수 없다. 
    2. 이 연구에서는 객체의 형태와 재료와 같은 시각적 개념과 물리적 상호작용을 통해 습득한 개념과 같은 조건을 다루는 벤치마크 VEC를 설계한다.
    3. CLIP 및 BLIP과 같은 시각적으로 향상된 LMs는 체감개념에 대한 인간 수준의 이해력을 얻는 반면, 일부 기본 개념은 스케일 업에서 적용되지 않는다. VEC에 VLMs의 체감지식을 전달하는 증류 방법을 제안하고, 스케일 업 매개변수와 비교할 수 있는 성능 향상을 달성한다.

###### SPT: Learning to Selectively Insert Prompts for Better Prompt Tuning (https://aclanthology.org/2023.emnlp-main.727/)
- Anthology ID: 2023.emnlp-main.727 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 프롬프트 튜닝 방법은 최적의 프롬프트 레이어를 수동으로 선택하는데 제한이 있었고, 프롬프트 튜닝의 잠재력을 활용하지 못했다. 본 연구에서는 학습 가능한 확률 게이트로 제어되는 프롬프트를 중간 레이어에 삽입함으로써 적절한 프롬프트 레이어를 선택하는 Selective Prompt Tuning (SPT) 프레임워크를 제안한다.
    2. 또한 SPT-DARTS라는 새로운 이중 최적화 프레임워크를 제안하여 학습 가능한 게이트를 더 잘 최적화하고 학습된 프롬프트 레이어 설정의 최종 프롬프트 튜닝 성능을 개선할 수 있다.
    3. 실험 결과, SPT 프레임워크는 전체 데이터와 소량 데이터 상황에서 이전의 최고 성능 모델인 PETuning과 비교하여 더 나은 성능을 보여준다.

###### Once Upon a Time in Graph: Relative-Time Pretraining for Complex Temporal Reasoning (https://aclanthology.org/2023.emnlp-main.728/)
- Anthology ID: 2023.emnlp-main.728 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리의 물리적 세계는 시간이 지남에 따라 지속적으로 변화하며, 사전 훈련된 언어 모델이 텍스트의 시간적 맥락을 이해하고 추론하는 데 어려움을 겪는다. 
    2. 이 연구에서는 시간과 지식의 관련성이 다른 지식 간의 시간 의존성을 추론하는 다운스트림 태스크를 위해 강화시키는 기존 방법들의 한계를 극복하기 위해 그래프 구조를 활용한다.
    3. 실험 결과 RemeMo는 다양한 설정에서 여러 시간적 질문-답변 데이터셋에서 기준선인 T5보다 우수한 성능을 보였으며, 추가 분석 결과 RemeMo가 장거리 복잡한 시간적 종속성을 모델링하는 데 특히 효과적인 것으로 나타났다.

###### Expository Text Generation: Imitate, Retrieve, Paraphrase (https://aclanthology.org/2023.emnlp-main.729/)
- Anthology ID: 2023.emnlp-main.729 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 설명서 문서는 복잡한 정보를 독자에게 전달하는 중요한 도구이지만, 손으로 설명서 텍스트를 작성하는 것은 콘텐츠 계획, 다양한 출처에서 사실 확보, 사실을 명확하게 종합적으로 결합하는 능력이 필요하기 때문에 어려운 과정이다.
    2. 우리는 이러한 부담을 줄이기 위해, 지식 소스를 지능적으로 탐색하여 토픽에 대한 정확하고 스타일 일관성 있는 설명서 텍스트를 자동으로 생성하기 위한 "설명서 텍스트 생성" 과제를 제안한다.
    3. 우리는 retrieval-augmented 모델의 한계를 극복하고, 콘텐츠 계획, 사실 확보 및 문장 재구성을 반복하는 IRP라는 프레임워크를 개발하여 이 과제를 해결한다. 우리는 새롭게 수집한 세 가지 다양한 데이터셋에서의 실험을 통해, IRP가 독자에게 정확한 정보를 제공하는 사실적이고 조직화된 설명서 텍스트를 생성한다는 것을 보여준다.

###### Large-scale similarity search with Optimal Transport (https://aclanthology.org/2023.emnlp-main.730/)
- Anthology ID: 2023.emnlp-main.730 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Wasserstein 거리(Wasserstein distance)는 확률 분포를 비교하기 위한 강력한 도구로 NLP에서 문서 분류 및 검색에 널리 사용된다." 
    2. "WMD는 다양한 NLP 작업에서 우수한 성능을 보이지만, 계산 비용이 크고 대규모 분포 비교에 적합하지 않다는 한계점이 있다." 
    3. "본 연구에서는 Wasserstein 거리를 기반으로 하는 간단하고 효과적인 최근접 이웃 검색 방법을 제안하였으며, 해당 근사 방법은 기존의 Wasserstein 거리와 비교 가능한 성능을 가지고 있으며 기존 방법보다 3개 차원 빠르게 계산할 수 있다는 것을 실험을 통해 입증하였다."

###### Enhancing Textbooks with Visuals from the Web for Improved Learning (https://aclanthology.org/2023.emnlp-main.731/)
- Anthology ID: 2023.emnlp-main.731 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 교과서는 고품질 교육을 학생에게 전달하는 주요 매체 중 하나이다. 그러나 많은 교과서는 학생 학습을 지원하기 위한 흥미로운 시각 자료가 부족하다.
    2. 본 논문에서는 비전-언어 모델의 효과성을 조사하여 웹에서 교과서를 자동으로 이미지로 향상하는 방법을 제시한다.
    3. 수학, 과학, 사회과학 및 비즈니스 분야의 e-교과서 데이터셋을 수집하고, 웹 이미지를 교과서에 적절하게 할당하는 일치 최적화 문제로 설정하여 그 효과를 검증하였다.

###### Continual Event Extraction with Semantic Confusion Rectification (https://aclanthology.org/2023.emnlp-main.732/)
- Anthology ID: 2023.emnlp-main.732 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 개설학습 추출에서 annotation의 갱신으로 인해 semantic confusion이 생기고 event type들 사이의 불균형 문제가 악화되는 것을 관찰하였다.
    2. 우리는 semantic confusion을 완화하기 위해 문장마다 가짜 라벨을 만들고 이전 모델로부터 transfer learning을 통해 pivotal knowledge를 전달하는 새로운 모델을 제안한다.
    3. 실험 결과, 우리의 모델은 기존 모델들보다 뛰어나며 불균형 데이터에 효과적이다.

###### An Empirical Study of Translation Hypothesis Ensembling with Large Language Models (https://aclanthology.org/2023.emnlp-main.733/)
- Anthology ID: 2023.emnlp-main.733 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델 (LLM)은 종종 생산된 결과물이 신뢰성이 없거나 환각하는 경우가 있는데, 이 논문에서는 가설 앙상블링이 LLM 기반 기계 번역의 품질을 어떻게 개선하는지 조사한다.
    2. 우리는 ChatGPT, LLaMA, Alpaca와 같은 LLM에서 생성된 가설에 대한 여러 기법을 실험하며 다양한 차원에서 포괄적인 연구를 제공한다. 
    3. 결과는 MBR 디코딩이 매우 효과적인 방법이며, 적은 수의 샘플을 사용하여 번역 품질을 개선할 수 있으며, 단순 샘플링 온도와 가설 다양성 간의 관계에 대한 instruction tuning이 강력한 영향을 미친다는 것을 보여준다.

###### FedTherapist: Mental Health Monitoring with User-Generated Linguistic Expressions on Smartphones via Federated Learning (https://aclanthology.org/2023.emnlp-main.734/)
- Anthology ID: 2023.emnlp-main.734 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 정신과 의사들은 환자의 언어 사용을 통해 정신질환을 진단하지만, 기존의 정신 건강 모니터링 시스템은 데이터 프라이버시로 인해 활동, 앱 사용 및 위치와 같은 대체 기능을 사용한다.
    2. 우리는 FedTherapist라는 모바일 정신 건강 모니터링 시스템을 제안한다. 이 시스템은 연합 학습을 통해 연속적인 음성과 키보드 입력을 개인 정보 보호 방식으로 활용한다.
    3. 우리는 여러 모델 디자인을 탐색하고, on-device 언어 모델 훈련의 복잡성을 극복하기 위해 FedTherapist의 성능과 부하를 비교하여지루하고 소음이 많은 텍스트를 효과적으로 활용하기 위한 Context-Aware Language Learning (CALL) 방법론을 제안한다.

###### Visually-Situated Natural Language Understanding with Contrastive Reading Model and Frozen Large Language Models (https://aclanthology.org/2023.emnlp-main.735/)
- Anthology ID: 2023.emnlp-main.735 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 대형 언어 모델(Large Language Models, LLMs)의 발전으로 시각적 영역에 대한 응용 프로그램의 연구가 급증했으나 텍스트가 풍부한 이미지에서의 성능은 여전히 개선이 필요하다.
    2. 이 논문에서는 Cream이라는 새로운 신경 아키텍처를 제안하여 기존 방법에서 자주 간과되는 복잡한 세부사항을 포착하여 LLMs의 언어-이미지 이해 능력을 향상시킨다.
    3. Cream은 시각 및 보조 인코더를 결합하여 이미지 내에서 시각적으로 배치된 맥락 내의 언어 정보를 보다 효과적으로 이해하며, 시각과 언어 이해 사이의 격차를 줄여 더 정교한 문서 인텔리전스 어시스턴트의 개발을 도모한다.

###### Continual Learning for Multilingual Neural Machine Translation via Dual Importance-based Model Division (https://aclanthology.org/2023.emnlp-main.736/)
- Anthology ID: 2023.emnlp-main.736 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 신경망 기계 번역(MNMT)의 지속적인 목표는 이전 훈련 데이터에 접근하지 않고도 모델을 지속적으로 새로운 언어 쌍을 지원하거나 기존 언어 쌍을 개선하는 것이다.
    2. 기존 방법들은 기존과 새로운 언어 쌍 사이에서 타협을 통해 catastrophic forgetting을 방지하는 데 초점을 두지만, 이는 두 가지 번역 작업에 대해 최적의 성능을 보여주지 않는다.
    3. 이 논문에서는 이 문제를 완화하기 위해 모델 파라미터를 두 부분으로 나눌 수 있는 이중 중요도 기반 모델 분할 방법을 제안한다. 이를 통해 기존 번역 작업에 대한 책임을지는 Fine-tuned된 모델을 만들고 새로운 훈련 데이터로 새로운 번역 작업에 대한 external 파라미터를 추가하고 이를 재조정한다.

###### SimCSE++: Improving Contrastive Learning for Sentence Embeddings from Two Perspectives (https://aclanthology.org/2023.emnlp-main.737/)
- Anthology ID: 2023.emnlp-main.737 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 드롭아웃 잡음을 다루고 특징 결함을 해결하기 위해 조금 더 나은 대조 학습을 제안한다.
    2. 먼저, 이 논문은 부정적인 짝에서의 드롭아웃 잡음이 모델 성능에 영향을 미치는 것을 확인하고, 이러한 잡음을 다루기 위한 간단하고 효과적인 방법을 제안한다.
    3. 두 번째로, 특징 결함의 현재 솔루션에서의 랭크 병목현상을 파악하고, 이 문제를 해결하기 위해 차원별 대조 학습 목적을 제안한다.

###### Unlearn What You Want to Forget: Efficient Unlearning for LLMs (https://aclanthology.org/2023.emnlp-main.738/)
- Anthology ID: 2023.emnlp-main.738 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델들은 텍스트 데이터의 사전 학습과 기억을 통해 큰 발전을 이루고 있으나, 이 과정은 개인 정보 보호 문제 및 데이터 보호 규정 위반에 취약할 수 있다.
    2. 이 논문에서는 데이터 제거 후 모델 전체를 재학습하지 않으면서 개별 사용자와 관련된 데이터를 모델에서 쉽게 제거할 수 있는 효율적인 unlearning 프레임워크를 제안한다.
    3. 실험 결과는 제안된 방법이 최신 기준보다 효과적임을 보여 주었다.

###### Simplicity Level Estimate (SLE): A Learned Reference-Less Metric for Sentence Simplification (https://aclanthology.org/2023.emnlp-main.739/)
- Anthology ID: 2023.emnlp-main.739 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문장 단순화에 대한 자동 평가는 여전히 어려운 문제이다. 대부분의 인기 있는 평가 메트릭은 단순화로부터 파생된 단어들과 유사한 단어들만 비교하기 때문에 단순성을 평가하기에는 제한적이다. 
    2. 우리는 "SLE"라는 새로운 학습된 평가 메트릭을 제안하여 간결성에 중점을 두었으며, 인간의 판단과의 상관관계 측면에서 거의 대부분의 기존 메트릭보다 우수한 성능을 보인다. 
    3. 이를 통해 우리는 실제 사용되지 않은 도메인에 대한 성능을 테스트하는 것이 어려운 단순화 작업에 대한 자동 평가의 한계를 극복할 수 있다는 것을 보여준다.

###### Precedent-Enhanced Legal Judgment Prediction with LLM and Domain-Model Collaboration (https://aclanthology.org/2023.emnlp-main.740/)
- Anthology ID: 2023.emnlp-main.740 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 법적 판단 예측은 법적 AI에서 점점 중요해지고 있는 과제로, 사건 사실 설명에 대한 판단을 예측하는 것이다. 이 연구에서는 이전과 같은 사실을 가진 선행 사례들이 국가 법제에서 추후 사건의 판단에 기초가 되기 때문에 선행 사례들의 활용 가능성을 탐구하는 것이 가치가 있다고 말한다.
    2. LLMs (large language models)과 domain-specific models을 사용하여 LJP 과제를 해결하기 위해 PLJP(precedent-enhanced LJP) 프레임워크를 제안한다. domain models은 후보 라벨을 제공하고 적절한 선행 사례를 효율적으로 찾아내는 역할을 하고, large models은 선행 사례를 고려하여 최종 판단을 내린다.
    3. 실제 데이터셋에서의 실험을 통해 PLJP의 효과를 입증하였고, LLM과 도메인 모델의 협력이 가능한 다른 수직 도메인으로 일반화할 수 있는 유망한 방향성을 보여준다.

###### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (https://aclanthology.org/2023.emnlp-main.741/)
- Anthology ID: 2023.emnlp-main.741 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델에서 생성된 장문 텍스트의 사실성을 평가하는 것은 어렵다. 따라서 이 논문에서는 생성된 결과를 일련의 원자적 사실들로 나누고, 신뢰할 수 있는 지식 출처에 의해 지원되는 원자적 사실의 백분율을 계산하는 새로운 평가 척도인 FACTSCORE를 제안한다.
    2. 큰 규모의 언어 모델-InstructGPT, ChatGPT 그리고 retrieval-augmented PerplexityAI-에서 생성된 사람 전기기록들을 FACTSCORE로 평가하여 분석한 결과 ChatGPT는 58%에 불과하다는 것을 보여주었다. 또한, 인간 평가 비용을 절감하기 위해 retrieval과 강한 언어 모델을 사용하여 FACTSCORE를 추정하는 자동 모델을 제시하였다.
    3. 이 자동 메트릭을 사용하여 최근 13개의 언어 모델 6,500개의 생성 결과를 평가하였고, 인간 평가비용은 26,000달러가 소요될 뻔한 상황에서 GPT-4와 ChatGPT가 다른 공개 모델보다 사실적이며, Vicuna와 Alpaca가 가장 좋은 공개 모델임을 발견하였다. FACTSCORE는 pip install factscore로 사용 가능하다.

###### Calc-X and Calcformers: Empowering Arithmetical Chain-of-Thought through Interaction with Symbolic Systems (https://aclanthology.org/2023.emnlp-main.742/)
- Anthology ID: 2023.emnlp-main.742 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 언어 모델들은 많은 태스크에서 높은 성능을 보이지만, 산술 연산이 필요한 태스크에서 사실적인 오류를 낼 가능성이 높다. 
    2. 본 논문에서는 "Calc-X"라는 새로운 데이터셋을 만들어 계산기의 적절한 사용법을 언어 모델에게 가르치는 방법을 제안한다.
    3. Calc-X를 사용하여 오픈소스 계산기 사용 모델을 훈련시키고, 기존 언어 모델과 비교하여 정확도를 거의 2배 향상시킬 수 있었다는 결과를 보였다.

###### CoF-CoT: Enhancing Large Language Models with Coarse-to-Fine Chain-of-Thought Prompting for Multi-domain NLU Tasks (https://aclanthology.org/2023.emnlp-main.743/)
- Anthology ID: 2023.emnlp-main.743 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Chain-of-Thought" 프롬프팅은 추론 태스크에서 인기가 있지만, 자연어 이해(NLU)에서의 큰 언어 모델에 적용은 미개척되어 있다.
    2. LLM(대형 언어 모델)의 다단계 추론을 기반으로 하는 "Coarse-to-Fine Chain-of-Thought(CoF-CoT)" 접근 방식을 제안한다. 이 방식은 NLU 태스크를 여러 추론 단계로 분해하여 LLM이 다양한 단위에서 필수적인 개념을 학습하고 활용할 수 있도록 한다.
    3. 또한, 우리는 의미론적 기반의 Abstract Meaning Representation(AMR) 구조적 지식을 중간 단계로 활용하여 발언의 뉘앙스와 다양한 구조, 그리고 그들 사이의 연결을 파악한다. 이러한 접근법은 제로샷 및 퓨샷 다중 도메인 설정에서 LLM이 다중 단계 NLU 태스크에 적응하는 데 효과적으로 작용함을 입증하였다.

###### When Language Models Fall in Love: Animacy Processing in Transformer Language Models (https://aclanthology.org/2023.emnlp-main.744/)
- Anthology ID: 2023.emnlp-main.744 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 생물학적 속성을 텍스트에서 학습한 언어 모델들은 일상 속에서 발생하는 보다 일반적인 생명체에 대해서는 사람과 유사한 방식으로 동작한다. 
    2. 그러나 이 모델들은 적절하지 않은 문맥에서의 생명체에 대한 처리에서 사람보다는 성능이 떨어진다.
    3. 이 연구는 텍스트만을 통해 생물학적 속성을 학습하는 언어모델들도 세밀한 문맥 정보로부터 어떻게 배울 수 있는지를 보여준다.

###### Improving Unsupervised Relation Extraction by Augmenting Diverse Sentence Pairs (https://aclanthology.org/2023.emnlp-main.745/)
- Anthology ID: 2023.emnlp-main.745 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 무지도 관계 추출(Unsupervised relation extraction, URE)은 수동 주석이나 사전에 기존 지식 베이스를 필요로 하지 않고 원시 텍스트에서 이름이 명시된 개체 간의 관계를 추출하는 것을 목표로 한다.
    2. URE 연구에서는 대조적 학습 전략에 많은 관심을 기울였지만, 다양한 양의 대조적 쌍과 적절한 손실 함수 탐색이 무시된 경우가 많다.
    3. 이 논문에서는 문장 내 다양한 쌍의 증강과 문장 간 쌍 추출을 통해 양의 쌍의 다양성을 증가시키고 대조적 학습의 식별력을 강화하는 AugURE을 제안하였다. 또한, 관계 표현 학습에 있어서 기존의 노이즈-대조적 추정(NCE) 손실의 한계를 확인하고 문장 쌍에 대한 마진 손실을 적용하는 것을 제안한다. NYT-FB와 TACRED 데이터셋에서의 실험 결과, 제안된 관계 표현 학습과 간단한 K-Means 군집화는 최고의 성능을 달성하였다.

###### Paraphrase Types for Generation and Detection (https://aclanthology.org/2023.emnlp-main.746/)
- Anthology ID: 2023.emnlp-main.746 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현재 paraphrase 생성 및 탐지 방법은 언어의 복잡한 특성을 무시하고 단일한 유사도 점수에 의존한다. 이 논문은 paraphrase 유형을 고려하여 이러한 결함을 보완하기 위해 두 가지 새로운 과제를 제안한다.
    2. 현재 기술들은 이진 분류(scenario), 즉 paraphrased or not의 경우에는 잘 수행하지만, 미세한 paraphrase 유형을 포함하는 것은 상당한 도전이다.
    3. paraphrase 유형을 파악하는 것은 paraphrase 모델 개발 및 미래의 과제 해결을 위한 새로운 패러다임을 열 수 있다고 생각된다.

###### Target-to-Source Augmentation for Aspect Sentiment Triplet Extraction (https://aclanthology.org/2023.emnlp-main.747/)
- Anthology ID: 2023.emnlp-main.747 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Aspect Sentiment Triplet Extraction (ASTE)은 사용자가 작성한 리뷰에서 관점 수준의 의견과 감정을 추출하는 sentiment analysis의 중요한 과제이다. ASTE의 세밀성으로 인해 주석 작업 비용이 높아지고, 주석된 데이터의 부족으로 기존 방법의 성능이 제한되었다. 이 논문에서는 데이터 증강을 활용하여 이 문제를 해결한다."
    2. "기존의 증강 방법들은 휴리스틱 규칙이나 언어 모델을 사용하여 기존 샘플의 입력 문장을 수정하는 방식인데, ASTE와 같은 세밀한 작업에 이러한 방법을 적용하는 것은 다양한 증강된 샘플을 생성하면서 수정된 문장과 원래 레이블 간의 일치를 유지하는 것에 어려움이 있다."
    3. "따라서 이 논문에서는 ASTE를 위한 타겟-소스 증강 방법을 제안한다. 저희 방법은 레이블과 문법적 템플릿을 혼합하여 새로운 문장을 직접 생성할 수 있는 generator를 학습하는 데 초점을 맞춘다. 이 generator를 사용하여 다양한 증강 샘플을 생성할 수 있으며, 생성된 문장의 품질을 보장하기 위해 순조성과 일치성 판별기를 도입하여 생성된 문장에 피드백을 제공하고 이를 강화 학습 프레임워크를 통해 generator를 최적화한다. 실험 결과, 우리의 방법은 기존 ASTE 모델의 성능을 크게 향상시킨다."

###### PAC-tuning: Fine-tuning Pre-trained Language Models with PAC-driven Perturbed Gradient Descent (https://aclanthology.org/2023.emnlp-main.748/)
- Anthology ID: 2023.emnlp-main.748 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 학습된 언어 모델(PLM)을 downstream 태스크에 fine-tuning하는 것은 대규모 최적화 문제이며, 훈련 알고리즘의 선택은 훈련된 모델의 일반화 성능에 큰 영향을 미친다. PAC-tuning은 두 단계로 구성되어 있으며, PAC-Bayes training을 기반으로 하여 적절한 모수 분포를 학습한다. PAC-tuning은 파라미터에 학습된 분산의 노이즈를 주입하여 gradient를 수정하고, perturbed gradient descent(PGD)의 변형을 사용하여 모델을 훈련시킨다. 
    2. 과거에는 몇 개의 훈련 데이터로 큰 모델에 적용할 때 PAC-Bayes bound가 엄격하지 않을 수 있어서 few-shot scenario에서 PAC-Bayes training이 어려웠다. 
    3. 5개의 GLUE 벤치마크 태스크를 통해 실험한 결과, PAC-tuning은 fine-tuning 과제에 대한 도전에 성공하고 강력한 베이스라인 방법들을 큰 폭으로 능가하며, 현재 Adam optimizer로 훈련하는 경우에도 PAC training을 적용할 수 있는 잠재력을 더욱 확인시켜준다.

###### Emergence of Abstract State Representations in Embodied Sequence Modeling (https://aclanthology.org/2023.emnlp-main.749/)
- Anthology ID: 2023.emnlp-main.749 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. sequence modeling을 통한 결정은 언어 모델의 성공을 모방하기 위해 사용되며, 이 논문에서는 Embodied agent의 행동을 예측하는 Token으로 모델링한다. 하지만 이러한 모델이 환경 상태 정보를 나타내는 내부 표현을 형성하는지 여전히 불분명하다.
    2. 이 논문에서는 BabyAI 환경에서 언어에 의존한 탐색 과제를 수행하는 Sequence 모델 Transformer를 구축하여, 추상적인 상태 표현의 출현을 조사한다.
    3. 실험 결과 중간 환경 레이아웃이 훈련된 모델의 내부 활성화로부터 상당히 재구성될 수 있으며, 언어 명령이 재구성 정확도에 영향을 준다는 것을 보여준다. 이러한 결과는 Sequence 모델링을 통해 상태 표현의 많은 주요 특징이 출현할 수 있다는 것을 시사하며, 복잡한 결정을 내리는 영역에 Sequence 모델링을 적용하는 의사결정을 낙관적으로 지지한다.

###### Accelerating Toeplitz Neural Network with Constant-time Inference Complexity (https://aclanthology.org/2023.emnlp-main.750/)
- Anthology ID: 2023.emnlp-main.750 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Toeplitz Neural Networks (TNN)는 많은 sequence modeling 태스크에서 뛰어난 성능을 보이는 것으로 알려져 있으며, 일반적으로 사용되는 Transformer-based 모델보다 우수한 결과를 제공하면서 log-linear space-time 복잡성을 가진다. 하지만, State Space Models (SSM)은 언어 모델링에서 TNN에 비해 성능이 낮지만 일정한 추론 복잡성을 가진다.
    2. 본 논문에서는 TNN과 SSM의 장점을 결합하기 위해 TNN을 SSM으로 변환하여 추론 중에 SSM과 같은 일정한 추론 복잡성을 가지도록 한다.
    3. 이를 위해 변환 과정을 최적화 문제로 정의하고 클로즈드폼 솔루션을 제공한다. 또한, 대상 방정식을 Vandermonde 선형 시스템 문제로 변환하고 Discrete Fourier Transform (DFT)를 사용하여 효율적으로 해결하는 방법을 보여준다. 이 방법은 훈련을 필요로하지 않으며 수치적 안정성을 유지한다. 또한, LongConv-based 모델에도 적용할 수 있다.

###### Dissecting Recall of Factual Associations in Auto-Regressive Language Models (https://aclanthology.org/2023.emnlp-main.751/)
- Anthology ID: 2023.emnlp-main.751 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformer 기반 언어 모델에서는 사실적인 지식을 파라미터로 포함시킬 수 있다. 이전 연구들은 사실적인 연관성이 어디에 저장되어 있는지를 살펴봤지만, 추론 중에 내부적으로 어떻게 검색되는지에 대해서는 거의 알려져있지 않다.
    2. 이 논문에서는 정보 전달을 통해 이 질문에 대한 답을 예측하기 위해 모델이 subject와 relation에 대한 정보를 어떻게 집계하는지를 조사한다.
    3. 연구 결과, 지식이 LMs 내부적으로 어떻게 저장되고 추출되는지에 대한 종합적인 관점을 도입하여 지식의 지역화 및 편집에 대한 미래 연구를 용이하게 한다.

###### StereoMap: Quantifying the Awareness of Human-like Stereotypes in Large Language Models (https://aclanthology.org/2023.emnlp-main.752/)
- Anthology ID: 2023.emnlp-main.752 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델은 훈련 데이터에 존재하는 유해한 연관성을 부여하고 유지시킵니다. 이 논문에서는 StereoMap이라는 이론적인 기반을 제안하여 이들이 사회적 집단에 대해 어떻게 인식하는지 알아낼 수 있습니다.
    2. StereoMap은 사회적인 차원인 온기(Warmth)와 능력(Competence)을 사용하여 LLM의 인식을 매핑합니다.
    3. 결과적으로, LLM은 사회적인 집단에 대해 다양한 인식을 갖고 있으며, 온기와 능력의 차원에서 혼합적인 평가로 특징 짓습니다. 또한, LLM의 판단에 영향을 미치는 기저 요인을 밝히기 위해 그들의 추론을 분석한 결과, LLM은 사회적 불평등에 대한 인식을 보여주며, 이를 지원하기 위해 통계 데이터와 연구 결과를 인용합니다.

###### Select, Prompt, Filter: Distilling Large Language Models for Summarizing Conversations (https://aclanthology.org/2023.emnlp-main.753/)
- Anthology ID: 2023.emnlp-main.753 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT와 같은 큰 언어 모델은 텍스트 요약과 같은 특정 자연어 생성 작업이나 특정 도메인에서 사용하기에 비용이 많이 들 수 있다. 
    2. 작은 언어 모델을 특정 작업에 맞게 세밀하게 fine-tuning하는 것은 유망한 대안이다. 그러나 이를 위한 고품질의 훈련 데이터를 구하는 것은 매우 비용이 많이 든다. 
    3. 이 논문에서는 지식 축약(KD)을 통해 약한 지도 데이터를 생성하고, 이를 통해 ChatGPT를 축약하고 작은 언어 모델에 대해 요약 작업을 성공적으로 수행할 수 있음을 보였다.

###### Human Raters Cannot Distinguish English Translations from Original English Texts (https://aclanthology.org/2023.emnlp-main.754/)
- Anthology ID: 2023.emnlp-main.754 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Translationese"는 번역된 텍스트에만 나타나는 언어적 특징을 말하는데, translationese를 구분하기 위한 자동 분류기들은 높은 정확성을 가지고 있으나 사람들의 정확성은 잘 연구되지 않았다. 
    2. 이 연구에서는 사람들이 텍스트를 원문인지 번역된 영어인지 어떻게 판별하는지와 그 과정에서 어떤 특징들을 고려하는지를 알아보기 위해 원문과 번역된 영어 텍스트에 대한 인간 평가를 수행하였다.
    3. 결과적으로, 판별자의 모국어나 텍스트의 원본 언어에 상관없이 사람들은 번역되었는지 원문인지를 구별하지 못하며 의견이 일치하지 않는다는 결론이 나왔다. 이 연구 결과는 번역 연구와 번역ese 분류기의 평가에 중요한 통찰력을 제공한다.

###### Impressions: Visual Semiotics and Aesthetic Impact Understanding (https://aclanthology.org/2023.emnlp-main.755/)
- Anthology ID: 2023.emnlp-main.755 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "아름다움과 미적 영향은 다를까요? 시각적 중요성은 효과적인 커뮤니케이션 능력의 반영일까요?"  Impression이라는 새로운 데이터셋을 통해 이미지의 의미 구성에 스타일이 주제뿐만 아니라 의미를 형성하는 데에도 중요한 역할을 한다는 주장을 제시한다. 기존의 이미지 캡셔닝 데이터셋은 최신 아키텍처가 이미지의 인상이나 해석을 모델링할 수 있는 능력을 갖출 수 있도록 설계되지 않았다는 점을 인정하며, 이를 보완하기 위해 이미지 분석 기술에 영감을 받은 주석 작업을 설계하여 1,440개의 이미지-캡션 쌍과 4,320개의 고유한 주석을 수집한다.
    2. 기존의 다중모달 이미지 캡셔닝과 조건부 생성 모델들은 실제 인간의 응답을 시뮬레이션하는 데 어려움을 겪는다는 것을 보여준다.
    3. 그러나 이 데이터셋은 미세 조정(fine-tuning) 및 피우-샷(few-shot) 적응을 통해 이들의 이미지의 인상과 미적 평가를 모델링하는 능력을 크게 향상시킨다.

###### DNA: Denoised Neighborhood Aggregation for Fine-grained Category Discovery (https://aclanthology.org/2023.emnlp-main.756/)
- Anthology ID: 2023.emnlp-main.756 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 가늠성 레이블 데이터로부터 미세한 범주를 발견하는 것은 미세한 분석 요구와 높은 주석 비용 사이의 격차를 좁히는 것이다. 
    2. 이 논문에서는 semantic structure를 임베딩 공간으로 인코딩하기 위해 노이즈를 제거한 이웃 집합(DNA)이라는 자기-지도적인 프레임워크를 제안한다. 
    3. 실험 결과로, 우리의 방법은 더 정확한 이웃을 검색하고, 다른 모델들보다 더 나은 결과를 보여준다.

###### Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models (https://aclanthology.org/2023.emnlp-main.757/)
- Anthology ID: 2023.emnlp-main.757 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. prompt 기반 학습은 few-shot 설정에서 특히 NLP 태스크에서 최고의 성능을 보이는데, 이에 대한 공격으로는 backdoor attacks가 있다. 이 논문에서는 prompt를 트리거로 사용하여 외부 트리거를 필요로 하지 않는 새로운 백도어 공격 방법인 ProAttack을 제안한다.
    2. ProAttack은 훼손된 샘플의 정확한 라벨링을 보장하며, 트리거로 인한 이상한 문장 표현을 최소화하여 백도어 공격의 은밀성을 향상시킨다.
    3. ProAttack은 풍부한 리소스와 few-shot 텍스트 분류 과제에서 다양한 실험을 통해 합리적인 성능을 보여주었다. 특히, rich-resource 설정에서는 외부 트리거 없이도 clean-label 백도어 공격 벤치마크에서 최고의 공격 성공률을 달성했다.

###### UPRISE: Universal Prompt Retrieval for Improving Zero-Shot Evaluation (https://aclanthology.org/2023.emnlp-main.758/)
- Anthology ID: 2023.emnlp-main.758 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델은 인상적인 능력을 갖고 있지만, 모델 특화 fine-tuning이나 태스크 특정 prompt engineering의 필요성으로 일반화에 어려움을 겪을 수 있다.
    2. 우리는 다양한 태스크에서 튜닝되었지만 보이지 않는 태스크 유형에 대해 테스트되는 경량이고 다용도의 retrieves를 자동으로 제공하는 UPRISE (Universal Prompt Retrieval for Improving zero-Shot Evaluation)를 제안한다. 
    3. 우리는 또한 UPRISE가 ChatGPT에서 환각 문제를 완화하는 것을 실험으로 보여주며, 가장 강력한 LLM을 개선할 잠재력을 암시한다.

###### KRLS: Improving End-to-End Response Generation in Task Oriented Dialog with Reinforced Keywords Learning (https://aclanthology.org/2023.emnlp-main.759/)
- Anthology ID: 2023.emnlp-main.759 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 과제 지향적 대화(TOD)에서 강화학습(Reinforcement Learning) 알고리즘은 과제 관련 메트릭에 대한 응답을 직접 최적화하기 위해 모델을 훈련시킨다. 그러나 강화학습은 자동회귀적인 시퀀스 생성 과정이 느리기 때문에 탐색을 수행해야 하는데 이는 시간이 많이 소요된다. 우리는 오프라인 환경에서 TOD 성능을 향상할 수 있는 더 효율적인 RL 기반 알고리즘을 개발하였다.
    2. 우리는 훈련된 언어 모델(LM)을 사용하여 더 빠른 생성 절차를 사용하며, 강화학습을 위한 세부적인 보상 함수를 도입하여 대화에서 각 생성된 토큰의 중요성과 의미적 유사성을 측정함으로써 모델이 핵심 정보를 학습하도록 돕는다.
    3. MultiWoZ 데이터셋에서의 실험 결과, 새로운 훈련 알고리즘인 KRLS(Keywords Reinforcement Learning with Next-word Sampling)는 자동회귀 생성을 사용하는 표준 RL 알고리즘과 비교하여 훈련 시간을 15% 줄이면서 엔드투엔드 응답 생성 과제에서 최고 성능을 달성한다.

###### Large Language Models Only Pass Primary School Exams in Indonesia: A Comprehensive Test on IndoMMLU (https://aclanthology.org/2023.emnlp-main.760/)
- Anthology ID: 2023.emnlp-main.760 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(Large Language Models, LLMs)은 주로 대규모 멀티리굴 텍스트로 사전학습되지만, 이들의 추론 능력과 현실 세계 지식은 주로 영어 데이터셋을 기반으로 평가된다.
    2. 이 연구에서는 인도네시아 언어와 문화 분야에서의 LLM 능력을 평가하기 위해 IndoMMLU라는 첫 번째 멀티태스크 언어 이해 기준을 제안한다.
    3. "GPT-3.5는 오직 인도네시아 초등학교 수준에만 통과할 뿐, 인도네시아의 지역 언어와 문화에 대한 제한적인 지식을 갖고 있다."

###### Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs (https://aclanthology.org/2023.emnlp-main.761/)
- Anthology ID: 2023.emnlp-main.761 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Self-Consistency 기법은 LLM에서 출력되는 결과의 정확성을 향상시킬 수 있는 대표적인 방법이다. 그러나 기존 Self-Consistency 기법은 질문마다 일정한 수의 샘플을 생성하는 반면, 더 나은 방법은 현재까지 생성된 샘플들 간의 일치 정도에 따라 사용 가능한 예산을 비균등하게 분배하는 것이다.
    2. 본 논문에서는 Lightweight stopping criterion을 사용하여 동적으로 각 질문마다 샘플의 수를 조절하는 비용 효율적이고 모델에 구애 받지 않는 기법인 Adaptive-Consistency를 소개한다. 
    3. 3개의 LLM과 17개의 추론 및 코드 생성 데이터셋에서의 실험 결과 Adaptive-Consistency는 평균적으로 정확도 하락이 0.1% 미만이면서 샘플 예산을 최대 7.9배로 감소시키는 것을 보여준다.

###### Bridging Information-Theoretic and Geometric Compression in Language Models (https://aclanthology.org/2023.emnlp-main.762/)
- Anthology ID: 2023.emnlp-main.762 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 언어 모델(LM)이 인간의 언어를 정확하게 모델링하기 위해서는 방대하고 무한한 정보를 상대적으로 적은 차원으로 압축해야 한다. 
    2. 이 논문에서는 (pre-trained) LMs의 압축을 geometric한 관점과 정보 이론적인 관점에서 분석하는 것을 제안한다. 
    3. 언어 데이터의 내재 기하 차원은 LMs에서의 코딩 길이를 예측하는데 중요한 역할을 한다는 것을 보이고, 언어 데이터의 높은 압축은 그 데이터에 대한 빠른 적응을 예측하는 것을 확인한다.

###### Pre-training Language Models for Comparative Reasoning (https://aclanthology.org/2023.emnlp-main.763/)
- Anthology ID: 2023.emnlp-main.763 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 비교 추론은 개체, 개념 또는 엔티티를 비교하여 결론을 도출하는 과정으로, 이는 기본적인 인지 능력이다. 본 논문에서는 비교 추론 능력을 향상시키기 위해 언어 모델을 사전 훈련하기 위한 새로운 프레임워크를 제안한다.
    2. 비교 추론이 필요한 NLP 작업에 대한 기존 방법들은 비용이 많이 드는 수동 데이터 라벨링과 다른 작업에 대한 한정적인 일반화 능력 등의 문제가 있다.
    3. 이 연구에서는 구조화된 데이터와 비구조화된 데이터를 모두 활용하여 확장 가능한 텍스트 기반 개체 비교 데이터 수집 기법을 도입하고, 비교 추론에 관한 세 가지 새로운 목표를 가진 언어 모델 사전 훈련 프레임워크를 제안한다. 이 프레임워크는 저자들의 평가를 통해 매우 좋은 성능을 보여주었으며, 특히 데이터 부족한 상황에서 비교 추론 능력을 크게 향상시켰다.

###### Improved Pseudo Data for Machine Translation Quality Estimation with Constrained Beam Search (https://aclanthology.org/2023.emnlp-main.764/)
- Anthology ID: 2023.emnlp-main.764 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기계 번역 품질 추정은 참고 번역문이 없는 경우 기계 번역의 품질을 추정하는 중요한 작업이다.  
    2. 기존의 pseudo data 솔루션은 pseudo label이 부정확하거나 실제 번역과 다른 경우 불만족스러운 결과를 가져온다.  
    3. 이 논문에서는 CBSQE를 사용하여 pseudo 데이터를 생성하고, supervised 및 unsupervised 상황에서 강력한 성능을 보였다고 주장한다.

###### Text Embeddings Reveal (Almost) As Much As Text (https://aclanthology.org/2023.emnlp-main.765/)
- Anthology ID: 2023.emnlp-main.765 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트 임베딩은 원본 텍스트에 대한 개인 정보를 얼마나 많이 노출시키는가? 우리는 밀집 텍스트 임베딩에서 원래 텍스트를 재구성하는 embedding inversion 문제를 조사했다. 
    2. 우리는 이 문제를 controlled generation으로 구체화하여 텍스트를 생성하는 방식으로 접근했고, 임베딩에 의존하는 단순한 모델보다 반복적으로 텍스트를 수정하고 재 임베딩하는 멀티 스텝 방법이 32 토큰의 텍스트 입력의 92%를 정확하게 복구할 수 있다는 것을 발견했다.
    3. 우리는 두 개의 최첨단 임베딩 모델에서 텍스트 임베딩을 디코드하는 방법을 모델에 학습시키고, 또한 우리의 모델이 임상 기록 데이터 세트에서 중요한 개인 정보 (전체 이름)를 복구할 수 있다는 것을 보여줬다.

###### AutoTrial: Prompting Language Models for Clinical Trial Design (https://aclanthology.org/2023.emnlp-main.766/)
- Anthology ID: 2023.emnlp-main.766 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 약 개발을 위해 임상시험은 중요하다. 이 논문에서는 자연어 모델을 사용하여 임상 임검 의 자격 조건을 설계하는 AutoTrial 메소드를 제안한다.
    2. AutoTrial은 (1) 이전 임상 임검의 조건을 고려하고, (2) 명시적인 사고의 체인(rational)으로 실행결과를 이해할 수 있으며, (3) 고급 지침(instruction tuning)을 통해 조건을 제어 가능하다. 
    3. 약 70,000개의 임상시험에서 수행된 실험에서, AutoTrial은 적절한 기준을 만족시키며 일관된 조건 텍스트를 생성하고 GPT-3.5 보다 약 60% 우세한 평가결과를 보였다.

###### Faster Minimum Bayes Risk Decoding with Confidence-based Pruning (https://aclanthology.org/2023.emnlp-main.767/)
- Anthology ID: 2023.emnlp-main.767 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최소 베이즈 위험 (MBR) 디코딩은 어떤 유용성 함수에 대한 모델 분포의 가장 높은 기대 효용을 가지는 가설을 출력한다. 그러나 MBR을 위한 표준 샘플링 기반 알고리즘은 beam search보다 훨씬 계산 비용이 많이 들며, 많은 수의 샘플 및 유틸리티 함수의 호출이 필요하므로 적용 범위가 제한된다. 
    2. 이 논문에서는 우리는 부트스트랩 샘플링으로 얻은 신뢰도 추정치에 따라 가장 높은 유틸리티를 가지지 않을 것으로 예상되는 가설을 제거하며, 유틸리티를 추정하는 데 사용되는 샘플 수를 점진적으로 증가시키는 MBR 알고리즘을 제안한다.
    3. chrF ++ 및 COMET을 유틸리티/평가 메트릭으로 사용하여 세 가지 언어 쌍에 대한 실험에서 우리의 접근법의 효과를 입증하였다.

###### Enhancing Generative Retrieval with Reinforcement Learning from Relevance Feedback (https://aclanthology.org/2023.emnlp-main.768/)
- Anthology ID: 2023.emnlp-main.768 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에 도입된 end-to-end generative retrieval은 문서 검색 방법에서의 중요한 변화이며, 특정 질의에 대한 응답으로 관련 문서 식별자 (docid)를 직접 생성하기 위해 differentiable search indexes를 활용한다. 
    2. 이러한 접근 방식은 두 가지 주요 도전에 직면하고 있다: (i) 토큰 수준의 확률적 최적화와 더 넓은 문서 수준의 관련성 평가 간의 불일치, (ii) 전반적인 순위 품질을 희생하고도 최상위 결과에 과도하게 초점을 맞추는 문제. 
    3. 이러한 도전을 극복하기 위해, 우리는 generative retrieval 모델을 제안하며, relevance feedback으로부터의 강화학습을 통해 토큰 수준의 docid 생성을 문서 수준의 관련성 평가와 일치시키기 위해 노력한다.

###### Multi-Source Probing for Open-Domain Conversational Understanding (https://aclanthology.org/2023.emnlp-main.769/)
- Anthology ID: 2023.emnlp-main.769 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 이해와 생성은 오픈 도메인 대화 시스템의 성공에 매우 중요합니다. 미리 학습된 생성 대화 모델은 유창한 응답 생성에서 상당한 진전을 이루었지만, 사람들은 대화의 문맥 정보를 이해하고 효과적으로 모델링하는지 판단하기 어렵습니다.
    2. 이 연구에서는 여러 가지 상황에 적용 가능한 다양한 대화 이해 기술을 수행하기 위해 다양한 소스로부터의 특징들을 종합하는 "Multi-Source Probing (MSP)" 방법을 제안합니다.
    3. 실험 결과는 오픈 도메인 대화 모델이 중간 숨겨진 상태에서 의미 정보를 인코딩할 수 있으며, 다양한 규모와 구조의 모델이 다른 대화 이해 능력을 가지고 있음을 보여줍니다.

###### Hallucination Mitigation in Natural Language Generation from Large-Scale Open-Domain Knowledge Graphs (https://aclanthology.org/2023.emnlp-main.770/)
- Anthology ID: 2023.emnlp-main.770 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이전 연구들은 지식 그래프 트리플을 위한 자연어 설명을 생성할 때, 소규모의 사람 주석이 달린 데이터셋이나 mostly star graphs와 같은 다양성이 제한된 데이터셋을 사용하였다. 이 논문은 이러한 제한적인 데이터셋 대신 대규모, 오픈 도메인 상황을 고려한 GraphNarrative 데이터셋을 제시한다.
    2. Transformer 기반 사전 훈련된 언어 모델을 세밀하게 조정하는 것이 그래프-텍스트 모델들 사이에서 최고 성능을 보였지만, 이 방법은 정보 환각이라는 문제가 있다. 즉, 생성된 텍스트에 입력 그래프에 없는 가공된 사실들이 포함될 수 있다.
    3. 이 논문에서는 GraphNarrative에서 그래프-문장 쌍을 가지고, 문장의 종속성 파스 트리를 활용하여 해당 그래프에 없는 부분을 제거하는 새로운 방법을 제안한다. 이 방법을 GraphNarrative 및 기존 데이터셋 위에서 학습한 모델을 사용하여 실험한 결과가 검증되었다.

###### Multi-Source Multi-Type Knowledge Exploration and Exploitation for Dialogue Generation (https://aclanthology.org/2023.emnlp-main.771/)
- Anthology ID: 2023.emnlp-main.771 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다양한 유형의 지식이 부족한 Open-domain multi-turn 대화 생성을 위한 과제가 있다. 기존 모델들은 특정 유형의 대화 지식을 식별하고 해당 데이터셋을 사용하여 훈련하는 것에 주로 초점을 맞추었으나, 이러한 접근 방식은 일반화 능력이 제한되고 계산 리소스 요구가 증가하는 결과를 가져온다.
    2. 이 논문에서는 여러 종류의 다양한 데이터셋을 활용하여 LLMs에서 multi-source multi-type 지식을 탐색하고 이를 대화 응답 생성에 활용하는 KnowEE라는 프레임워크를 제안한다.
    3. 자동 및 수동 평가 결과 모두, 우리의 프레임워크가 다중 소스 다중 유형 지식을 탐색하고 활용하여 일관된, 정보성 높은, 유창한 응답을 생성하는 데 효과적임을 검증한다.

###### Focus Your Attention (with Adaptive IIR Filters) (https://aclanthology.org/2023.emnlp-main.772/)
- Anthology ID: 2023.emnlp-main.772 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 어텐션에 앞서 입력 시퀀스를 처리하기 위해 동적인 Infinite Impulse Response (IIR) 필터를 사용하는 새로운 레이어를 제안한다. 상태-공간 레이어와 비교하여 파라미터 수가 적고 입력 크기와 시간 복잡도가 서브-2차 방식으로 성능 또한 우수하다.
    2. 동적 적응 필터는 입력 시퀀스의 관련 요소에 주목하도록 하며, 선형 시스템 이론에 기반하여 설계되었다.
    3. Heyna, GPT2, Mega와 같은 레이어에 비해 적은 파라미터 수로 여러 개의 장거리 시퀀스 문제에 대한 성능을 향상시켰다.

###### Identifying Statements Crucial for Awareness of Interpretive Nonsense to Prevent Communication Breakdowns (https://aclanthology.org/2023.emnlp-main.773/)
- Anthology ID: 2023.emnlp-main.773 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 원격 대화 중 청취자가 일부 발언을 놓치면 의사소통 장애가 발생하는데, "SCAINs" 라고 불리는 중요한 발언을 식별함으로써 이러한 장애를 예방하는 것을 목표로 한다.
    2. SCAINs를 식별하기 위해, 원래의 대화에서 두 개 연속 발언을 생략하고 다음 발언을 보다 구체화하는 텍스트를 생성하여 대화를 만들어내는 독특한 접근법을 채택한다. 
    3. 우리는 missing 정보를 처리하여 누락된 정보를 시뮬레이션하는 것이라는 점에서 제안한 방법의 독창성을 강조하며, 대화 데이터셋을 사용하여 SCAIN의 효과를 검증한다.

###### Multilingual Large Language Models Are Not (Yet) Code-Switchers (https://aclanthology.org/2023.emnlp-main.774/)
- Anthology ID: 2023.emnlp-main.774 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 여러 언어 대형 언어 모델인 LLM은 zero-shot이나 few-shot prompting 방법을 통해 최신 성능을 보여주었지만, 코드 스위칭 (CSW) 환경에서의 잠재력에 대한 연구는 아직 미탐한 영역이다.
    2. 본 논문에서는 다양한 multilingual LLM의 성능을 감정 분석, 기계 번역, 요약 및 단어 수준 언어 식별과 같은 네 가지 태스크를 기준으로 평가했다.
    3. 결과적으로, zero-shot이나 few-shot prompting 방법을 통해 일부 태스크에서는 promising한 결과를 보이지만, 그 크기가 훨씬 작은 fine-tuned 모델과는 비교할 때 성능이 낮았다. 현재의 multilingual LLM은 코드 스위칭 텍스트에 대한 능숙함을 내포하지 않는다고 주장하며 이 간극을 해소하기 위한 미래 연구를 촉구한다.

###### Reinforced Target-driven Conversational Promotion (https://aclanthology.org/2023.emnlp-main.775/)
- Anthology ID: 2023.emnlp-main.775 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화형 어시스턴트의 제품 홍보를 위해 사용자와 적극적으로 소통하는 능력은 매우 중요하다. 그러나 기존 대화 추천 방법들은 사용자 선호도 획득에 너무 초점을 맞추고, 사용자를 지정된 아이템 수용으로 유도하기 위한 전략적 계획을 무시하기 때문에, 매력적인 응답과 함께 특정 아이템을 홍보하는 데 실패한다.
    
    2. 이 논문에서는 대화형 홍보를 위해 강화학습 기반의 타깃 중심 대화형 프로모션 (RTCP) 프레임워크를 제안한다. RTCP는 균형 잡힌 게이팅 메커니즘을 통해 단기 및 장기 계획을 통합한다. 이를 위해 지식 기반의 다중 헤드 어텐션을 사용하여 대화 액션을 예측하고 강화학습 보상에 따라 가이드한다. RTCP는 또한 액션에 기반한 프리픽스 튜닝을 사용하여 관련된 응답을 생성한다.
    
    3. 실험 결과는 우리 모델이 자동 측정 지표와 인간 평가 모두에서 최신 모델보다 우수한 성능을 보였음을 보여준다. 또한, RTCP는 전체 모델 재학습 없이 프리픽스 매개변수를 업데이트함으로써 새로운 시나리오에 빠르게 적응하는 능력을 갖추고 있다.

###### Identification of Multimodal Stance Towards Frames of Communication (https://aclanthology.org/2023.emnlp-main.776/)
- Anthology ID: 2023.emnlp-main.776 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 멀티미디어 문서에서 커뮤니케이션 프레임은 종종 나타나며, 작가가 텍스트에 이미지를 추가할 때 일어날 수 있다. 이 논문에서는 텍스트와 이미지 간의 상호작용을 통해 커뮤니케이션 프레임에 대한 작가의 태도를 자동으로 탐지하는 방법을 소개한다.
    2. 기존에는 텍스트만 처리하므로 멀티미디어 문서에 대한 태도 주석이 없는 문제로 인해 해당 방법은 적용되지 않았다.
    3. MMVax-Stance 데이터셋은 11,300개의 멀티미디어 문서와 113개의 커뮤니케이션 프레임에 대한 태도 주석을 포함하고 있으며, 이를 통해 텍스트와 이미지 간의 상호작용을 통해 커뮤니케이션 프레임에 대한 태도를 예측하는 모델을 실험하였다.

###### Unsupervised Sounding Pixel Learning (https://aclanthology.org/2023.emnlp-main.777/)
- Anthology ID: 2023.emnlp-main.777 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사운드 소스의 위치 파악은 cross-modal alignment의 어려움 때문에 어려운 과제이다. 이 논문에서는 비지도 학습 방법을 사용하여 픽셀 수준의 사운드 소스 위치 파악을 가능하게 하는 USPL(Unsupervised Sounding Pixel Learning) 접근법을 제안한다.
    2. 비지도 교차 모달 대응을 실현하기 위해 오디오-비디오 특징을 정렬하는 mask augmentation 기반의 다중 인스턴스 비교 학습을 설계한다.
    3. 시각 의미 관계 학습을 통해 인접 좌표 피쳐의 상호 픽셀 관계를 탐색하는 Unsupervised Sounding Map Refinement (SMR) 모듈을 제안한다.

###### LM vs LM: Detecting Factual Errors via Cross Examination (https://aclanthology.org/2023.emnlp-main.778/)
- Anthology ID: 2023.emnlp-main.778 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현대 언어 모델(LM)의 중요한 약점은 사실적으로 틀린 텍스트를 생성하는 경향이 있어, 사용성이 제한된다. 
    2. 이 논문에서는 법률에서의 참을 찾는 메커니즘에서 영감을 받아, 실수된 주장을 자동으로 감지하는 LM의 사실성 평가 프레임워크를 제안한다. 
    3. 실험 결과, 우리의 방법은 기존 방법들과 비교해 성능이 우수하며, 다른 LMs와의 상호작용을 통해 사실적인 오류를 포착하는 것이 가능함을 보여준다.

###### Large Language Models: The Need for Nuance in Current Debates and a Pragmatic Perspective on Understanding (https://aclanthology.org/2023.emnlp-main.779/)
- Anthology ID: 2023.emnlp-main.779 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현재의 대형 언어 모델은 문법적으로 올바르고 유창한 텍스트를 생성하는 능력에서 비할 데 없다. 하지만 이러한 모델의 능력에 대한 논의는 많이 이루어졌지만, 깊이 있는 고찰은 뒤처지고 있다. 
    2. 이 논문에서는 대형 언어 모델의 능력에 대한 비판 중 일부를 비판적으로 평가하고, LLM이 통계적 패턴뿐만 아니라 형태적이고 기능적 언어 역량을 습득할 수 있다는 것을 보여준다. 
    3. 또한, LLM의 "실제" 이해와 의도에 관한 문제를 탐구하고 인간의 언어 학습에 대해 영감을 줄 수 있는 LLM의 사회적 관점에 대해 논의한다.

###### PIEClass: Weakly-Supervised Text Classification with Prompting and Noise-Robust Iterative Ensemble Training (https://aclanthology.org/2023.emnlp-main.780/)
- Anthology ID: 2023.emnlp-main.780 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. weakly-supervised text classification은 각 target class의 label name만을 supervision으로 사용하여 classifier를 학습시키는데, 이는 인간의 주석 작업을 크게 줄여준다. 하지만 기존 방법은 keyword matching을 통해 pseudo labels을 생성하는데, 이러한 방식은 context에 따라 keyword의 의미가 다를 수 있고, 일부 텍스트는 어떤 키워드도 가지고 있지 않을 수 있기 때문에 noisy하고 부적절한 pseudo labels을 유발할 수 있는 두 가지 한계가 있다.
    2. 이 논문에서는 PIEClass라는 새로운 방법을 제안하는데, 이는 contextualized text understanding을 기반으로 한 static keyword matching을 넘어 pre-trained language models (PLM)의 zero-shot prompting을 사용하여 pseudo labels을 획득하는 module과, 서로 규제하는 두 가지 PLM fine-tuning 방법을 활용하여 iterative하게 classifier를 학습하고 pseudo labels을 업데이트하는 noise-robust ensemble training module로 구성된다.
    3. 실험 결과, PIEClass는 7개의 기준 데이터셋에서 기존 강력한 기준 모델보다 전반적으로 더 우수한 성능을 보이며, 감성 분류 작업에서는 fully-supervised classifier와 유사한 성능을 달성한다.

###### MeaeQ: Mount Model Extraction Attacks with Efficient Queries (https://aclanthology.org/2023.emnlp-main.781/)
- Anthology ID: 2023.emnlp-main.781 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 처리에서 모델 추출 공격에 대해 연구하고, 반복적으로 오픈 API를 쿼리하여 피해 모델을 도용하려는 공격자를 조사한다. 
    2. 이 논문에서는 제한된 쿼리 예산 설정에 초점을 맞추고, 공개된 비어노테이션 데이터 소스에서 무작위 샘플링이나 액티브 러닝 기반 샘플링 전략을 채택하는 방법들을 제시한다.
    3. MeaeQ라는 새로운 방법을 제안하여, 문제 도메인 특정 데이터셋이 아닌 공개 텍스트 말뭉치에서 문제와 관련된 데이터를 필터링하고, 군집 기반 데이터 축소 기술을 사용하여 공격을 위한 대표적인 데이터를 얻는다.

###### The CoT Collection: Improving Zero-shot and Few-shot Learning of Language Models via Chain-of-Thought Fine-Tuning (https://aclanthology.org/2023.emnlp-main.782/)
- Anthology ID: 2023.emnlp-main.782 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 100B 미만의 parameter를 가진 작은 Language model (LMs)은 chain-of-thought reasoning 태스크를 해결하는 데 있어서 큰 LMs보다 성능이 나쁘다. 이 논문에서는 작은 LMs에게도 step-by-step reasoning 능력을 부여하기 위해 CoT rationales를 사용하여 instruction tuning을 제안한다. 
    2. CoT Collection이라는 새로운 instruction-tuning 데이터셋을 소개하고, 이를 사용하여 Flan-T5 (3B & 11B)를 CoT fine-tuning한다면 작은 LMs도 unseen tasks에서 더 나은 CoT 능력을 갖게 된다고 보여준다.
    3. 또한, CoT Collection을 사용한 instruction tuning은 LMs가 4개의 도메인에 대한 few-shot learning 능력도 강화시키며, 문제 해결 능력에서 ChatGPT를 능가하는 결과를 얻을 수 있다.

###### Explaining Interactions Between Text Spans (https://aclanthology.org/2023.emnlp-main.783/)
- Anthology ID: 2023.emnlp-main.783 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 이해 (NLU) 과제에서는 입력의 서로 다른 부분의 토큰 범위를 능력있게 추론하는 것이 중요하다. 하지만 기존의 하이라이트 기반 설명은 인접한 토큰 또는 튜플 사이의 상호작용 뿐만 아니라 개별적으로 중요한 기능을 식별하는 데 주로 초점을 맞추고 있다. 
    2. 이 논문에서는 NLI 및 FC 두 NLU 작업에 대한 사람의 범위 상호작용 설명의 다중 주석가 데이터 세트인 SpanEx를 소개한다.
    3. 또한, 그들을 사람의 추론 과정과 비교하여 여러 개의 세팅된 대형 언어 모델의 결정 과정을 연구하고, 무지로 추출하는 새로운 커뮤니티 탐색 기반의 비지도 방식을 제시한다.

###### Predictive Chemistry Augmented with Text Retrieval (https://aclanthology.org/2023.emnlp-main.784/)
- Anthology ID: 2023.emnlp-main.784 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 화학 분야에서 예측 모델을 향상시키기 위해 자연어 설명을 사용하는 것에 초점을 맞추고 있다.
    2. 기존의 화학정보학 모델은 주로 문헌에서 수작업으로 추출된 구조화된 데이터로 훈련된다.
    3. 본 논문에서는 TextReact라는 새로운 방법을 소개하는데, 이 방법은 문헌에서 검색된 텍스트 설명을 사용하여 예측 화학에 직접 보완을 한다.

###### System Combination via Quality Estimation for Grammatical Error Correction (https://aclanthology.org/2023.emnlp-main.785/)
- Anthology ID: 2023.emnlp-main.785 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. gramatical error correction (GEC) 모델의 성능 평가를 위해 품질 추정 모형이 개발되었지만 기존 모형들은 좋은 수정과 나쁜 수정을 구별하는 데 문제가 있다. 
    2. GRECO라는 새로운 품질 추정 모델을 제안하여 수정된 문장의 품질을 더 정확하게 추정할 수 있다고 보여주었다. 
    3. GRECO를 활용하여 여러 GEC 시스템의 출력을 결합하는 방법을 제안하였고, 다양한 범용성을 가진 방법들로 성능을 높일 수 있다고 보여주었다.

###### Rethinking Negative Pairs in Code Search (https://aclanthology.org/2023.emnlp-main.786/)
- Anthology ID: 2023.emnlp-main.786 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 contrastive learning이 소프트웨어 개발의 효율성과 효과성을 위한 코드 검색 모델의 fine-tuning에서 핵심 요소로 자리잡았다. 
    2. 그러나 InfoNCE의 negative sample에 대한 문제들로 인해 representation learning이 저하될 수 있다. 
    3. 우리는 Soft-InfoNCE라는 간단하고 효과적인 손실 함수를 제안하여 이러한 문제들을 해결하였다.

###### Question Answering as Programming for Solving Time-Sensitive Questions (https://aclanthology.org/2023.emnlp-main.787/)
- Anthology ID: 2023.emnlp-main.787 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 질문-답변(QA)은 우리의 세상에 대한 지식 습득에 핵심적인 역할을 하는데, 실제로 답은 질문에 대한 시간 제약이 변경될 때 완전히 다를 수 있다. 
    2. 기존 LLMs는 표면적인 텍스트 의미에 기반한 엄밀한 추론을 수행하지 못하므로 위의 문제는 여전히 큰 도전이 될 수 있다. 
    3. 따라서 LLMs에게 직접적으로 질문에 답을 하도록 요구하는 대신, 우리는 QAaP라는 새로운 접근 방식을 제안하고자 한다. 이를 통해 LLMs의 능력을 활용하여 다양하게 표현된 텍스트를 구조화된 코드로 변환하고, 프로그래밍을 통해 여러 후보 중 가장 잘 맞는 답변을 선택하도록 한다.

###### Joint Geometrical and Statistical Domain Adaptation for Cross-domain Code Vulnerability Detection (https://aclanthology.org/2023.emnlp-main.788/)
- Anthology ID: 2023.emnlp-main.788 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 코드 취약성 감지 작업에서, label-rich 소스 도메인에서 훈련된 탐지기는 타겟 도메인에서의 라벨링된 훈련 데이터의 부족으로 인해 정확한 예측을 제공하지 못한다. 
    2. 우리는 Mutual Nearest Neighbor Contrastive Learning을 도입하여 소스 도메인과 타겟 도메인을 기하학적으로 조정하고, 각 도메인의 개별적인 의미적 특징을 분리할 수 있는 새로운 크로스-도메인 코드 취약성 감지 프레임워크인 MNCRI을 제안한다. 
    3. 확장된 실험을 통해 MNCRI가 최신 크로스-도메인 코드 취약성 감지 방법들보다 훨씬 뛰어난 성능을 보여준다는 것을 입증하였다.

###### Revisiting Sparse Retrieval for Few-shot Entity Linking (https://aclanthology.org/2023.emnlp-main.789/)
- Anthology ID: 2023.emnlp-main.789 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Entity linking은 지식 베이스에서 모호한 언급과 해당 엔티티를 연결하는 것을 목표로 한다. 특정 도메인에 대한 부족한 레이블된 데이터로 인한 문제가 주요한 어려움 중 하나이다.
    2. 한정된 양의 도메인 내 레이블된 데이터만 사용 가능한 상황에서 dense retriever의 성능이 크게 저하된다고 한다.
    3. 본 논문에서는 sparse retrieval 방법을 재검토하고 ELECTRA 기반의 키워드 추출기를 제안하여 언급 문맥을 정리하고 더 좋은 질의 표현을 구성한다.

###### Controlling Pre-trained Language Models for Grade-Specific Text Simplification (https://aclanthology.org/2023.emnlp-main.790/)
- Anthology ID: 2023.emnlp-main.790 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 텍스트 단순화 시스템은 글의 내용을 보존하면서 읽기 쉽게 재작성한다. 하지만 읽는 이의 읽기 쉬움에 대한 기준은 의도된 독자에 따라 달라진다.
    2. 이 논문에서는 텍스트 간소화 시스템의 합리성과 단순성에 영향을 미치는 다양한 제어 기법의 영향을 이해하기 위해 실험을 진행하였다.
    3. 이를 바탕으로, 특정 학년 수준에 맞추기 위해 텍스트를 단순화하기 위해 필요한 편집 작업을 개별적으로 예측하는 간단한 방법을 제안하였다. 이 접근 방식은 코퍼스 수준의 탐색 기반 휴리스틱과 비교하여 단순화된 텍스트의 품질을 향상시킨다.

###### CLEVR-Implicit: A Diagnostic Dataset for Implicit Reasoning in Referring Expression Comprehension (https://aclanthology.org/2023.emnlp-main.791/)
- Anthology ID: 2023.emnlp-main.791 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 VL(Vision-Language) 모델은 다양한 교차 모달(Cross-Modal) 작업인 REC(Referring Expression Comprehension)에서 높은 성공을 거두고 있는데, 이러한 모델들은 대규모 이미지-텍스트 쌍으로 사전 훈련을 거친 뒤 후속 작업에서 성능을 미세조정한다. 하지만, 암묵적 텍스트(implicit text)가 포함된 작업에서는 어려움을 겪으며, 모델이 암묵적 텍스트와 이미지의 객체를 정확히 매핑하기 어렵다.
    2. 이 논문에서는 REC 작업을 위한 CLEVR-Implicit 데이터셋을 제안하고, VL 모델이 암묵적 텍스트를 처리하는 성능을 향상시키기 위해 "Transforming Implicit text into Explicit text (TIE)" 방법을 소개한다.
    3. 실험 결과, TIE 방법을 사용하여 VL 모델의 암묵적 텍스트 성능이 37.94% 크게 향상되었다.

###### “Are Your Explanations Reliable?” Investigating the Stability of LIME in Explaining Text Classifiers by Marrying XAI and Adversarial Attack (https://aclanthology.org/2023.emnlp-main.792/)
- Anthology ID: 2023.emnlp-main.792 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. LIME은 AI 설명가능성 (XAI) 프레임워크에서 가장 널리 인용되는 도구 중 하나이며, 핵심적인 머신러닝 응용 분야 (예: 건강관리 및 금융) 에 통합되어 있다. 하지만 텍스트 데이터의 특수한 제약으로 인해 LIME의 안정성은 아직 충분히 탐구되지 않았다.
    2. 본 논문에서는 먼저 텍스트 데이터에서 LIME의 고유한 불안정성을 평가하여 기준을 마련하고, 그런 다음 텍스트 입력을 왜곡하고 설명을 조작하는 XAIFooler라는 혁신적인 알고리즘을 제안한다. 이는 LIME의 안정성을 텍스트 왜곡 최적화 문제로 탐구한다.
    3. XAIFooler는 텍스트 의미론과 원래 예측을 보존하기 위한 제약 조건을 준수하며, 설명 유사성 측정을 위한 모든 요구 사항을 충족시키기 위해 Rank-biased Overlap (RBO)를 도입한다. 실제 텍스트 데이터셋에서의 광범위한 실험 결과, XAIFooler는 설명의 의미론적 보존성이 높은 LIME 조작 능력에서 모든 기준점을 큰 비율로 능가한다.

###### CQE: A Comprehensive Quantity Extractor (https://aclanthology.org/2023.emnlp-main.793/)
- Anthology ID: 2023.emnlp-main.793 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 수량은 금융, 비즈니스, 의학, 과학과 같은 분야에서 사실적인 정보를 설명하는 데 필수적이다. 그러나 다른 정보 추출 방법에 비해 텍스트에 포함된 양 추출 및 표현 방법을 설명하는 연구는 몇 개뿐이다.
    2. 본 논문에서는 텍스트 데이터에서 포괄적인 수량 추출 프레임워크를 제안한다. 이 프레임워크는 값과 단위의 조합, 수량의 동작 (상승 또는 하강) 및 수량에 관련된 개념을 효과적으로 탐지한다.
    3. 우리의 프레임워크는 의존성 구문 분석과 단위 사전을 사용하며, 검출된 수량의 적절한 정규화 및 표준화를 제공한다. 평가를 위한 새로운 데이터셋을 사용하여, 우리의 프레임워크가 다른 시스템보다 우수한 성능을 보이고, 발견된 수량과 관련된 개념을 탐지하는 첫 번째 시스템임을 보여준다.

###### Context Compression for Auto-regressive Transformers with Sentinel Tokens (https://aclanthology.org/2023.emnlp-main.794/)
- Anthology ID: 2023.emnlp-main.794 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformer 기반 LLMs에서 attention module의 이차 복잡성은 generation 도중에 계산량의 대부분을 차지하게 되며, 효율적인 메모리 사용과 추론 지연에 심각한 문제를 야기한다.
    2. 우리는 지정된 토큰 span의 중간 활성화를 점진적으로 압축하여 이후 context 처리 시 메모리 및 계산 비용을 줄이는 plug-and-play 접근법을 제안한다.
    3. 도메인 내 언어 모델링과 zero-shot open-ended document generation에서의 실험 결과, 우리의 방법이 효율성, n-gram 매칭 및 의미적 유사성 측면에서 sparse attention을 능가함을 보여준다.

###### A Unified View of Evaluation Metrics for Structured Prediction (https://aclanthology.org/2023.emnlp-main.795/)
- Anthology ID: 2023.emnlp-main.795 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 여러 구조적 예측 태스크 (예: 이벤트 및 관계 추출, 구문 및 의미 파싱)에 대한 다양한 평가 메트릭을 하나로 통합하는 개념적인 프레임워크를 제시한다. 
    2. 우리의 프레임워크는 이러한 태스크의 출력을 특정 데이터 유형의 객체로 표현하고, 공통 하위 구조의 매칭을 통해 메트릭을 유도한다.
    3. 우리는 이러한 프레임워크를 통해 여러 태스크에 대한 평가 메트릭을 간결하게 표현할 수 있음을 보여주며, 새로운 메트릭은 출력 구조를 기반으로 자연스럽게 유도될 수 있다고 보여준다.

###### A Deeper (Autoregressive) Approach to Non-Convergent Discourse Parsing (https://aclanthology.org/2023.emnlp-main.796/)
- Anthology ID: 2023.emnlp-main.796 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인 소셜 플랫폼은 정보 공유와 다중 참여 대화에 활기를 불어넣는 장소로 이용된다. 그러나 대부분의 대화 분석 프레임워크는 많은 온라인 플랫폼에서 흔하게 나타나는 논쟁적인 대화를 분석하기에는 적합하지 않다.
    2. Zakharov et al. (2021)에서 소개된 새로운 다중 라벨 체계를 이용하여 논쟁적인 대화 파싱을 위한 통합 모델을 제안한다. 이 모델은 이전 대화 발화를 제외한 다른 추가 입력을 요구하지 않는다.
    3. 우리는 GRN 레이어와 비대칭 손실 함수를 통해 RoBERTa backbone을 fine-tuning하여 제안한 아키텍처가 대화 파싱에서 우수한 성과를 보이는 것을 확인하였다. 이를 통해 대화의 동적 이해를 깊게 하는 도구의 개발을 촉진시킬 수 있다.

###### We are Who We Cite: Bridges of Influence Between Natural Language Processing and Other Academic Fields (https://aclanthology.org/2023.emnlp-main.797/)
- Anthology ID: 2023.emnlp-main.797 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자연어 처리(NLP)는 세계에 상당한 영향을 주려고 한다. 그러나 이에 따른 위험도 상당하다. 이러한 위험에 대처하기 위해서는 다양한 연구 분야와의 포괄적인 협력이 필요하다. 그러나 지금까지 관련 분야들과 NLP 사이의 협력 상태에 대한 연구는 거의 이루어지지 않았다.
    2. 이 논문에서는 NLP와 23개의 연구 분야간의 상호작용 정도를 측정한 결과를 제시하고 있다. NLP 논문, NLP 논문에서 다른 논문들로 향하는 인용, 다른 논문에서 NLP 논문으로의 인용을 분석한 결과를 바탕으로, NLP의 타 연구 분야와의 협력은 시간이 흐름에 따라 점점 감소하고 있다는 것을 보여주고 있다.
    3. NLP는 점점 특정 분야에 치우쳐 있고, 컴퓨터 과학 분야에서 다른 분야로의 인용이 매우 적다는 것을 알 수 있다. 이러한 결과는 NLP가 다양한 분야와의 협력을 반영해야 하는 시급성을 강조하고 있다.

###### Ties Matter: Meta-Evaluating Modern Metrics with Pairwise Accuracy and Tie Calibration (https://aclanthology.org/2023.emnlp-main.798/)
- Anthology ID: 2023.emnlp-main.798 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Kendall의 tau는 기계 번역(MT) 평가 메트릭이 개별 번역을 얼마나 잘 평가하는지 메타-평가하는 데 자주 사용되는데, 이제 문제는 묶음 (ties)를 어떻게 처리해야 하는지라는 것이다. 
    2. 기존의 변형들은 묶음을 처리하는 방식 때문에 약점을 가지고 있고, 때로는 게임이 가능하다는 문제가 있다.
    3. 우리는 묶음 예측에 대한 정확도를 고려하는 비교적 정확함 (pairwise accuracy) 버전으로 메타-평가를 제안하고, 묶음을 자동으로 도입하여 메트릭 점수 간의 공정한 비교를 가능하게 하는 tie calibration 절차를 도입한다. 이러한 수정이 메트릭 성능의 공정한 순위 평가를 제공한다는 이유와 실험적 증거를 제시한다.

###### SODA: Million-scale Dialogue Distillation with Social Commonsense Contextualization (https://aclanthology.org/2023.emnlp-main.799/)
- Anthology ID: 2023.emnlp-main.799 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회적 대화 분야에서 데이터 부족은 오랫동안 문제였다. 이 논문에서는 공개적으로 제공되는 첫 백만 단위의 고품질 사회적 대화 데이터셋인 SODA를 제안한다.
    2. SODA는 지식 그래프를 통해 사회적 상식 지식을 맥락화하여 대규모 언어 모델에서 사회적 상호작용을 포함하고 있다.
    3. SODA를 이용하여 COSMO라는 대화 모델을 학습시키고, COSMO는 이전의 최고 성능 대화 모델들보다 더 자연스럽고 일관성 있으며, 때로는 사람이 작성한 골드 응답보다 선호받는다는 것을 실험적으로 확인하였다.

