# Korean Three-Line Summarizations of Papers 301-400 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing
###### BiasX: “Thinking Slow” in Toxic Content Moderation with Explanations of Implied Social Biases (https://aclanthology.org/2023.emnlp-main.300/)
- Anthology ID: 2023.emnlp-main.300 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 독성 주석기나 컨텐츠 모더레이터들은 결정을 내릴 때 종종 mental shortcuts을 사용한다. 이는 미묘한 독성이 놓칠 수 있고, 독성이 있어 보이지만 실제로는 무해한 컨텐츠가 과도하게 감지될 수 있다는 의미한다.
    2. BiasX라는 프레임워크를 소개하는데, 이는 뉘앙스적인 (비)독성 컨텐츠를 인식하기 위해 free-text 설명으로 컨텐츠 모더레이션 설정을 강화한다.
    3. 전체적으로 설명의 품질이 매우 중요하며, 기계 생성 설명은 전문가가 작성한 인간의 설명에 비해 도움이 적다는 것을 보여준다. 우리의 결과는 자유로운 텍스트 설명을 사용하여 좀더 사려깊은 독성 모더레이션을 유도하는 것의 잠재력을 보여준다.

###### Text encoders bottleneck compositionality in contrastive vision-language models (https://aclanthology.org/2023.emnlp-main.301/)
- Anthology ID: 2023.emnlp-main.301 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 CLIP 모델은 보다 복합적인 입력에 대해서는 감지가 약하다는 문제점이 있고, 어떤 텍스트 인코더가 다른 것보다 훨씬 더 잘 작동한다는 것을 발견했다. 
    2. 텍스트만으로 복구 가능성을 평가하는 것이 다중 모달 매칭 성능을 예측하는 유용한 지표라는 것을 발견했는데, 이는 새로 수집하고 배포한 평가 기준인 ControlledImCaps에 대해 증명되었다. 
    3. 본 논문에서는 CompPrompts라는 기존에 없던 데이터셋과 코드를 함께 제공한다.

###### Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs Through a Global Prompt Hacking Competition (https://aclanthology.org/2023.emnlp-main.302/)
- Anthology ID: 2023.emnlp-main.302 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "대화형 챗봇과 작문 어시스턴트와 같은 대화형 환경에서는 대규모 언어 모델 (LLM)이 점점 더 많이 사용됩니다. 그러나 이런 배포는 보안 위협이 있으며, 기존 명령을 무시하고 악의적인 명령을 따르도록 조작됩니다. 이 논문은 prompt hacking에 대한 대규모 자원 및 양적 연구의 결핍을 해결하기 위해 전세계적인 prompt hacking 대회를 진행하였습니다."
    2. "우리는 세 가지 최첨단 LLM에 대해 60만 개 이상의 적대적인 프롬프트를 모집했으며, 현재 LLM은 prompt hacking을 통해 실제로 수정될 수 있다는 것을 확인했습니다."
    3. "또한 우리는 적대적인 프롬프트 유형들에 대한 종합적인 체계를 제시하였습니다."

###### MMNMT: Modularizing Multilingual Neural Machine Translation with Flexibly Assembled MoE and Dense Blocks (https://aclanthology.org/2023.emnlp-main.303/)
- Anthology ID: 2023.emnlp-main.303 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현재 널리 사용되는 다중 언어 신경 기계 번역에서 Mixture-of-Experts (MoE) 기반의 희소 아키텍처는 계산 오버헤드를 sublinear하게 증가시키면서 모델 용량을 크게 향상시킬 수 있지만, 낮은 자원언어 번역에서 과적합될 수 있다고 알려져 있다.
    2. 본 논문에서는 밀집 모듈과 MoE 기반 희소 모듈을 유연하게 조합하여 최상의 효과를 얻을 수 있는 모듈화 MNMT 프레임워크를 제안한다.
    3. 실험 결과, 제안한 모듈화 MNMT 프레임워크는 고/저 자원 언어 번역 및 제로샷 번역에서 MoE 및 밀집 모델보다 뛰어난 성능을 보이며, 다양한 방법들을 조합하고 오프더셀프 모델을 재활용하여 다중 언어 신경 기계 번역을 가능케 한다.

###### Localizing Active Objects from Egocentric Vision with Symbolic World Knowledge (https://aclanthology.org/2023.emnlp-main.304/)
- Anthology ID: 2023.emnlp-main.304 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. AI 에이전트가 과제를 해결하거나 인간을 가상으로 지원하기 위해서는, 자기 중심적 시점에서의 과제 지시를 적극적으로 이해하는 능력이 중요합니다. 이를 위한 중요한 단계 중 하나는 사람들에게 무엇을/어디를 어떻게 지시해야 하는지 정확히 알려주지 않고도, 사람의 행동/환경과 관련된 주요 활동 객체를 지역화하고 추적하는 것입니다.
    2. 기존 연구들은 이 문제를 순수한 비전 관점에서 다루었으나, 텍스트 모달리티(즉, 과제 지시)와 시각 모달리티와의 상호작용이 어느 정도 유용할 수 있는지 조사하였습니다.
    3. 우리는 구문 지지 모델이 활동적인 객체를 정확하게 지역화하는 능력을 향상시키기 위해 (1) '변화하는 객체'의 역할을 학습하고 그것들을 지시에서 정확하게 추출하는 방법, (2) 물체의 전/후 상태를 고려하는 방법, 그리고 (3) 기술적인 지식으로 객체를 더 견고하게 인식하는 방법을 제안합니다.

###### Introducing Rhetorical Parallelism Detection: A New Task with Datasets, Metrics, and Baselines (https://aclanthology.org/2023.emnlp-main.305/)
- Anthology ID: 2023.emnlp-main.305 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 말하거나 쓰는 피닉스는 내용 뿐만 아니라 스타일도 포함한다. 병렬 구조는 일반적인 스타일 도구로, 같은 시퀀스의 언어적 특징을 가진 구문의 병렬 배치이다. 병렬 구문을 자동으로 감지하는 과제를 소개하고, 강한 기준으로 측정했을 때 0.40과 0.43의 F1 스코어를 달성했다.
    
    2. 우리는 이 과제에 대한 공식적인 정의를 제시하고, 새로운 라틴어 데이터셋과 중국어 데이터셋을 구축했다.
    
    3. 또한, 기준 시스템과 병렬 구조를 포착하기 위한 새로운 시퀀스 라벨링 체계를 생성하여 이 과제에 대한 성능 평가를 수행했다.

###### Prompting is not a substitute for probability measurements in large language models (https://aclanthology.org/2023.emnlp-main.306/)
- Anthology ID: 2023.emnlp-main.306 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인간 언어 모델의 언어 지식을 평가하기 위해 Metalinguistic Prompting과 직접 확률 측정을 비교한 결과, Metalinguistic Prompting은 표현에서 직접 파생된 양보다 상대적으로 성능이 떨어진다는 것을 발견했다.
    2. 또한, Prompt Query가 다음 단어 확률의 직접 측정과 차이가 나갈수록 일관성이 떨어진다는 것을 알 수 있었다.
    3. 이 연구 결과는 Metalinguistic Prompting에 의존하는 부정적인 결과가 특정 언어 일반화가 부족한 것으로 결론지을 수 없음을 시사하며, 확률 분포에 제한이 있는 닫힌 API로의 전환으로 상실되는 가치를 강조한다.

###### Parameter-Efficient Language Model Tuning with Active Learning in Low-Resource Settings (https://aclanthology.org/2023.emnlp-main.307/)
- Anthology ID: 2023.emnlp-main.307 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 학습 언어 모델(PLMs)은 특히 저자원 도메인과 언어에서 효과적인 세밀 조정 기술에 대한 수요를 촉발시켰다. 기존의 active learning(AL) 알고리즘은 labeling 비용을 최소화하기 위해 라벨 복잡성을 최소화하는 데 유용하다. 
    2. 본 연구에서는 text classification을 위한 낮은 리소스 설정에서 AL과 adapter-based PEFT의 상호작용을 연구하였다. PEFT가 낮은 리소스 설정에서 full-fine tuning(FFT)보다 우수하며, 이 이점이 AL 설정에서도 유지됨을 입증하였다.
    3. PEFT와 FFT의 특성을 통해 forgetting dynamics와 instance-level representations을 조사해보았는데, PEFT가 FFT와 비교하여 초기 및 중간 레이어의 더 안정된 표현을 생성함을 발견하였다. 이 연구는 저자원 설정에서 AL과 PEFT의 상호작용의 잠재력을 강조하며 효율적이고 효과적인 fine-tuning의 진보에 길을 열었다.

###### Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks (https://aclanthology.org/2023.emnlp-main.308/)
- Anthology ID: 2023.emnlp-main.308 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 자동 수집 말뭉치로 사전 훈련 된 모델에서 데이터 오염이 일반화되어 어려움이 발생하고 있다.
    2. 공개 데이터는 공개 키로 암호화되어야 하며, 파생 배포를 금지하는 라이선스를 갖춰야 한다.
    3. 데이터 오염을 방지하기 위해 훈련 제외 콘트롤을 요구하고, 인터넷에 솔루션이 함께 나온 데이터를 피하고, 웹 페이지 컨텍스트와 함께 데이터를 공개해야 한다.

###### CoLT5: Faster Long-Range Transformers with Conditional Computation (https://aclanthology.org/2023.emnlp-main.309/)
- Anthology ID: 2023.emnlp-main.309 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Transformer 모델은 연산 복잡도가 큰 문제로 인해 긴 문서를 처리하는 데에 비용이 많이 든다. 그러나 긴 문서에는 모든 토큰이 동일한 중요성을 가지지 않으며, 이를 고려한 조건부 계산을 수행하는 CoLT5 모델을 제안한다. 
    2. CoLT5는 중요한 토큰에 더 많은 리소스를 할당하여 LongT5보다 더 빠른 학습과 추론 속도로 더 강력한 성능을 달성한다. SCROLLS 벤치마크에서 강력한 성과를 보여주며, 매우 긴 입력에도 효과적이고 계산 가능한 성과를 보인다.
    3. CoLT5는 긴 문서 처리를 효율적으로 수행할 수 있는 모델로서 최신 기술을 압도하는 성능을 보여준다.

###### DiSTRICT: Dialogue State Tracking with Retriever Driven In-Context Tuning (https://aclanthology.org/2023.emnlp-main.310/)
- Anthology ID: 2023.emnlp-main.310 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 상태 추적(Dialogue State Tracking)은 과업지향 대화 시스템에서 사용자 의도를 파악하기 위해 대화에서 미리 정의된 슬롯 값들을 결정하는 중요한 구성 요소이다. 기존의 접근 방식은 손으로 만들어진 템플릿과 추가적인 슬롯 정보를 사용하여 대화 문맥에서 슬롯 값을 얻기 위해 대규모 사전훈련 언어 모델을 세밀하게 조정하는 방법을 사용한다.
    2. 이 논문에서는 손으로 만들어진 템플릿 없이 모델을 세밀하게 조정하기 위해 주어진 대화에 대해 매우 관련성 높은 훈련 예제를 검색하는 DiSTRICT라는 일반화 가능한 in-context 튜닝 방법을 제안한다.
    3. MultiWOZ 벤치마크 데이터셋을 사용한 실험 결과, DiSTRICT은 훨씬 작은 모델을 사용하면서 기존 접근 방식보다 다양한 제로샷 및 퓨샷 설정에서 성능이 향상되어, 자원이 제한 있는 실제 환경에서 중요한 장점을 제공한다.

###### Cross-Cultural Analysis of Human Values, Morals, and Biases in Folk Tales (https://aclanthology.org/2023.emnlp-main.311/)
- Anthology ID: 2023.emnlp-main.311 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 말담은 아이들의 인생에 큰 영향을 주고 도덕과 가치를 가르친다. 그러나 현재의 말담 연구는 대부분 유럽의 이야기에 국한되어 있다. 
    2. 본 연구에서는 6개 대륙에서 27개 문화에서 유래한 1,900개 넘는 말담을 모아 분석하였다. 
    3. 다양한 렉시콘과 상관 분석을 사용하여 말담에서 문화에 따라 인간의 가치, 도덕, 성차별이 어떻게 표현되는지 조사하였다.

###### Non-Programmers Can Label Programs Indirectly via Active Examples: A Case Study with Text-to-SQL (https://aclanthology.org/2023.emnlp-main.312/)
- Anthology ID: 2023.emnlp-main.312 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 비 프로그래머들이 복잡한 프로그램으로 자연어 발화를 주석으로 달 수 있을까? 우리는 APEL이라는 프레임워크를 소개하여 비 프로그래머들이 시맨틱 파서로부터 생성된 후보 프로그램들 중에서 선택할 수 있도록 한다.
    2. APEL은 후보 프로그램들의 입력-출력 예제를 살펴보고 간접적으로 선택하도록 요청하여 비 프로그래머들이 프로그램을 이해하지 못해도 정확한 프로그램을 선택할 수 있도록 한다.
    3. APEL을 사용하여 SPIDER라는 텍스트-SQL 데이터셋을 다시 주석으로 달도록 인간 비 프로그래머를 모집하였고, 이 방법은 원본 전문가 주석과 같은 정확성을 달성하며 원본 주석에서 많은 섬세한 오류를 노출시켰다.

###### LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers (https://aclanthology.org/2023.emnlp-main.313/)
- Anthology ID: 2023.emnlp-main.313 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델이 논리 추론 작업을 더 효과적으로 수행하기 위해 제안된 많은 prompting 기반 전략들은 여전히 부족한 면이 있어서 예상치 못한 방식으로 성능이 떨어지는 경우가 많다.
    2. 본 논문에서는 LINC(LINC: Logical Inference via Neurosymbolic Computation)라고 부르는 모듈식 신경 기호 프로그래밍으로 이러한 작업을 다시 구성하는 것의 타당성을 조사한다.
    3. LINC를 사용하여 ProofWriter와 FOLIO에서 성능 향상을 확인하였으며, 작은 규모의 StarCoder+ 모델에 LINC를 추가한 경우에는 GPT-3.5 및 GPT-4보다 성능이 우수하다는 것을 보여준다.

###### Non-autoregressive Streaming Transformer for Simultaneous Translation (https://aclanthology.org/2023.emnlp-main.314/)
- Anthology ID: 2023.emnlp-main.314 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. SiMT 모델은 대기 시간과 번역 품질 사이의 균형을 유지하기 위해 훈련되지만, 낮은 대기 시간을 유지하면서 높은 품질을 달성하기 위한 훈련은 종종 공격적인 예측의 경향을 가지게 된다. 
    2. 이러한 문제는 대부분의 기존 SiMT 모델에서 사용되는 autoregressive 구조에서 기인한다고 주장한다.
    3. 이 논문에서는 이러한 문제를 해결하기 위해 단방향 인코더와 non-autoregressive 디코더로 구성된 non-autoregressive streaming Transformer (NAST)를 제안한다.

###### ViSoBERT: A Pre-Trained Language Model for Vietnamese Social Media Text Processing (https://aclanthology.org/2023.emnlp-main.315/)
- Anthology ID: 2023.emnlp-main.315 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 영어와 중국어는 resource-rich 언어로 알려져 있지만 베트남어에는 pre-trained 모델이 제한적이다. 하지만 이 논문에서는 대규모 베트남 소셜미디어 텍스트에 대해 pre-trained된 ViSoBERT 모델을 제안하고 다양한 베트남 소셜미디어 태스크에서 이 모델이 이전 최고 성능 모델들을 능가하는 것을 보였다.
    2. 작성한 ViSoBERT 모델은 감정인식, 혐오발언 판별, 감성분석, 스팸 리뷰 감지, 혐오발언 범위 감지 등 베트남 소셜미디어 텍스트로 구성된 다섯 가지 중요한 자연어 downstream 태스크에서 사용되었다.
    3. ViSoBERT는 훨씬 적은 파라미터를 가지고 이전 모델들을 능가하여 베트남 소셜미디어 태스크에서 우수한 성능을 보여주고 있다.

###### RAPL: A Relation-Aware Prototype Learning Approach for Few-Shot Document-Level Relation Extraction (https://aclanthology.org/2023.emnlp-main.316/)
- Anthology ID: 2023.emnlp-main.316 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소수의 레이블된 문서만 사용 가능한 상황에서 문서 수준의 의미 관계를 식별하는 방법은 어떠한가? 이 논문은 실제 상황에서 도전적인 데이터 부족 문제를 해결하기 위한 얼마 되지 않는 문서 수준의 의미 관계 추출(FSDLRE)에 대해 다룬다.
    2. 기존의 방법은 관계 원형(protoype)을 구성하기 위해 해당 관계를 갖는 모든 entity pair들의 표현을 집계하는데, 이러한 entity pair들은 다른 관계도 가질 수 있기 때문에 원형이 혼란스러울 수 있다는 문제가 있다.
    3. 본 논문에서는 관계 의미를 강화하기 위해 관계 설명과 실제 NOTA(NONE-OF-THE-ABOVE) 인스턴스를 지능적으로 활용하여 관계 원형을 개선하고 과제별 NOTA 원형을 생성하는 FSDLRE용 관계 인식 원형 학습 방법을 제안한다.

###### GeoLM: Empowering Language Models for Geospatially Grounded Language Understanding (https://aclanthology.org/2023.emnlp-main.317/)
- Anthology ID: 2023.emnlp-main.317 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사람들은 기사를 읽을 때 지리적 추론에 의해 무의식적으로 참여한다. 우리는 텍스트에서 장소 이름과 그들의 공간적 관계를 인식하고, 그들을 지구상의 실제 위치와 연관시킨다. 이 논문은 지리적 정보를 활용하여 언어 모델의 지리적 이해를 강화하는 GeoLM을 소개한다.
    2. GeoLM은 언어 모델을 사용하여 언어적 맥락을 활용하는 데에 그치지 않고, OpenStreetMap과 같은 대용량의 지리 데이터베이스에서 유용한 지리적 정보를 활용한다.
    3. 실제 실험에서 GeoLM은 지명 인식, 지명 링킹, 관계 추출 및 지리 개체 유형 분류와 같은 다양한 과제에서 유망한 성능을 보여주었다.

###### Cross-Modal Conceptualization in Bottleneck Models (https://aclanthology.org/2023.emnlp-main.318/)
- Anthology ID: 2023.emnlp-main.318 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Concept Bottleneck Models (CBMs)는 훈련 예시 (예: X-선 영상)가 고수준 개념 (예: 이상 종류)으로 주석이 달려 있으며, 이러한 개념을 기반으로 먼저 개념을 예측한 다음 레이블을 예측하여 분류를 수행한다고 가정한다. 그러나 CBM을 사용하는 주요 도전 과제는 레이블과 관련하여 예측력이 있는 개념을 정의하고 훈련 예시에 이러한 개념을 주석으로 달아야 한다는 요구 사항이다."
    2. 우리의 접근 방식에서는 보다 중간 정도의 가정을 채택하고 대신 이미지와 함께 오는 텍스트 설명 (예: 방사선학 보고서)를 사용하여 개념의 유도를 안내한다. 
    3. 실험을 통해 근사적 생성된 설명을 가진 합성 이미지에서부터 실제 의료 영상 데이터셋에 이르기까지 여러 데이터셋에서 Crossmodal Learning이 해석 가능한 개념의 유도를 촉진하는 것을 보여주며, 분리(disentanglement)을 용이하게 한다.

###### LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models (https://aclanthology.org/2023.emnlp-main.319/)
- Anthology ID: 2023.emnlp-main.319 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델(GPT-4, ChatGPT 등)의 성공으로 인해 과제별 데이터나 지시어 데이터를 사용하여 오픈 액세스 언어 모델을 fine-tuning하는 다양한 비용 효율적이고 접근 가능한 대안들이 개발되었다. 
    2. 이 논문은 어댑터 기반 PEFT(Parameter-Efficient Fine-Tuning) 방법을 연구하기 위해 사용하기 쉬운 LLM-Adapters 프레임워크를 제안한다. 
    3. 실제 실험에서 어댑터 유형, 위치, 하이퍼파라미터에 대한 영향을 평가하고, 산술 연상과 상식 연상이라는 두 가지 추론 작업에서 어댑터의 효과를 평가하여 작은 규모의 LLMs에서도 강력한 LLMs와 비교 가능한 성능을 제공함을 보였다.

###### DREAM: Deployment of Recombination and Ensembles in Argument Mining (https://aclanthology.org/2023.emnlp-main.320/)
- Anthology ID: 2023.emnlp-main.320 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Argument Mining (AM)에는 종합적인 나아가 검은 상자의 관점이 적용되었는데, 이 연구는 독립된 새로운 해결책 대신 현재 구성품을 기반으로 성능을 높이는 해결책을 제시한다. 
    2. DREAM 프레임워크를 통해 AM의 구성 요소들을 자동적으로 조합함으로써 정확도를 향상시킨다. 
    3. 성능 벤치마크를 통해 DREAM과 함께 사용된 시스템은 AM 벤치마크로 측정된 정확도에서 이전 최고 단일 시스템보다 우수한 성능을 보인다.

###### MILDSum: A Novel Benchmark Dataset for Multilingual Summarization of Indian Legal Case Judgments (https://aclanthology.org/2023.emnlp-main.321/)
- Anthology ID: 2023.emnlp-main.321 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 법적 사건 판결문의 자동 요약은 많은 나라에서 독립적인 연구에 많은 연구 노력을 투입한 실제적으로 중요한 문제이다.
    2. 이 논문은 인도의 법정 환경에서 영어로 작성된 법적 사건 판결문을 가장 많이 사용되는 인도어인 힌디어로 크로스-언어적으로 요약하는 도전적인 노력을 제안한다.
    3. 저자들은 인도 주요 법원의 영어로 된 3,122건의 사건 판결문과 영어와 힌디어로 된 요약문으로 구성된 첫 번째 고품질의 법적 코퍼스를 구축하고 해당 코퍼스에서 여러 다양한 요약 접근 방식의 성능을 평가하여 법적 도메인에서 크로스-언어적 요약 연구의 필요성을 보여준다.

###### Query Rewriting in Retrieval-Augmented Large Language Models (https://aclanthology.org/2023.emnlp-main.322/)
- Anthology ID: 2023.emnlp-main.322 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대규모 언어 모델(Large Language Models, LLMs)은 "검색해서 읽기(retrieve-then-read)" 파이프라인에서 강력한 블랙박스 리더로 작동하며, 지식 기반 태스크에서 현저한 진전을 이뤄내고 있다. 이 논문은 이전의 retrieve-then-read 대신에 query rewriting 관점에서 retrieval-augmented LLMs를 위한 Rewrite-Retrieve-Read 프레임워크를 소개한다. 
    2. 이 전략은 검색 대상으로 사용될 쿼리의 적응에 주안점을 둔 것으로, 검색 대상과 입력 텍스트 사이에 불가피한 간극이 존재하기 때문이다. 
    3. LLM을 사용해 쿼리를 생성하고, 웹 검색 엔진을 사용해 맥락을 검색한 후, 검색 대상 모듈에 대한 쿼리 조정을 위해 훈련 가능한 Rewriter 스킴을 제안한다. 실험 결과, 이 프레임워크는 일관된 성능 향상을 보여주며, retrieval-augmented LLM에 대한 효과적이고 확장 가능한 새로운 프레임워크를 제공한다는 것을 입증한다.

###### PromptMix: A Class Boundary Augmentation Method for Large Language Model Distillation (https://aclanthology.org/2023.emnlp-main.323/)
- Anthology ID: 2023.emnlp-main.323 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 데이터 증강은 훈련 데이터가 한정적인 경우 텍스트 분류 문제를 해결하기 위해 널리 사용되는 기술인데, 이 논문은 큰 언어 모델(GPT3)을 사용하여 더 유용한 증강 데이터를 생성하는 방법을 제안한다. 
    2. 제안된 메소드인 PromptMix는 어려운 경계 예제를 생성하고, 생성된 데이터의 정확성을 향상시키기 위해 LLM 분류기를 사용하여 라벨을 다시 지정한다. 
    3. 실험 결과, PromptMix는 2-shot 설정에서 여러 5-shot 데이터 증강 방법보다 성능이 우수하며, 큰 언어 모델의 지식을 작은 분류기로 전달하는 데 도움이 된다는 것을 보였다.

###### COHESENTIA: A Novel Benchmark of Incremental versus Holistic Assessment of Coherence in Generated Texts (https://aclanthology.org/2023.emnlp-main.324/)
- Anthology ID: 2023.emnlp-main.324 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "일관성(coherence)은 텍스트의 작은 단위들(문장, 명제) 간의 관계를 의미하며, 텍스트를 논리적으로 일관되고 의미 있는 것으로 만드는 언어적인 개념이다. 전통적인 기계 번역을 위한 구문, 단어 정렬과 같은 일관성 측정 방법과는 달리, 이 논문에서는 CoheSentia라는 새로운 benchmark를 소개하여 자동 생성된 텍스트의 일관성 평가에 관한 명시적인 연구를 진행하였다." 
    2. "우리의 benchmark는 500개의 자동 생성된 단락과 인간의 주관적인 일관성 점수로 구성되어 있으며, 문장별로 일관성을 평가하는 점수와 해당 지점에서의 비일관성 원인을 상세히 표시하는 점수를 제공한다." 
    3. "실험 결과, 일관성 감지를 위해 fine-tuned 된 표준 LMs는 다양한 일관성 요소에 대해 다양한 성능을 보여주었으며, 이러한 모델들은 신뢰할 수 있는 일관성 평가 방법 개발의 필요성을 강조한다."

###### QUDeval: The Evaluation of Questions Under Discussion Discourse Parsing (https://aclanthology.org/2023.emnlp-main.325/)
- Anthology ID: 2023.emnlp-main.325 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Questions Under Discussion (QUD)은 지속적인 질문과 그에 대한 답변을 통해 담론이 진행되는 다재다능한 언어적 구조이다. 이 논문에서는 문헌과 답변 문장을 제공받아 QUD의 언어적 제약을 만족하고 이전 문맥의 앵커 문장에 기반한 질문을 생성하는 복잡한 문제를 소개한다.
    2. 이 논문에서는 QUD 파싱의 자동 평가를 위한 첫 번째 프레임워크를 소개하며, QUD의 이론적 제약을 구체적인 프로토콜로 구현한다. 
    3. 이 논문은 QUDeval이라는 fine-tuned 시스템과 LLM으로부터 생성된 2,190개의 QUD 질문에 대한 세밀한 평가 데이터셋을 제안하며, 기존의 평가 메트릭은 파서의 품질을 부정확하게 추정한다는 것을 보여준다.

###### PRCA: Fitting Black-Box Large Language Models for Retrieval Question Answering via Pluggable Reward-Driven Contextual Adapter (https://aclanthology.org/2023.emnlp-main.326/)
- Anthology ID: 2023.emnlp-main.326 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Retrieval Question Answering (ReQA) 작업에서는 retriever와 generator로 구성된 retrieval-augmented framework이 사용된다. generator는 retriever가 검색한 문서를 기반으로 답변을 생성한다. 그러나 대부분의 Large Language Models (LLMs)은 예산 제약으로 인해 fine-tuning하기에 너무 크고, 일부 LLMs는 API를 통해서만 접근 가능하다. 이 문제에 대해 개선하고 ReQA 성능을 향상시키기 위해 우리는 trainable한 Pluggable Reward-Driven Contextual Adapter (PRCA)를 제안한다.
    2. PRCA는 retriever와 generator 사이에 Pluggable한 방식으로 위치하며, 강화학습 기반 reward를 최대화하는 token-autoregressive 전략으로 retrieved 정보를 개선한다. 실험을 통해 PRCA의 효과를 입증하고, 기존의 framework에 black-box LLMs을 효과적으로 적용하여 ReQA 성능을 최대 20% 향상시킬 수 있음을 보여준다.
    3. 이 논문은 LLMs 시대에 PRCA가 가지는 상당한 잠재력을 보여줌으로써, 기존의 framework에 black-box LLMs을 효과적으로 적용함으로써 ReQA 성능을 향상시키는 가능성을 보여준다.

###### Exploring Chain of Thought Style Prompting for Text-to-SQL (https://aclanthology.org/2023.emnlp-main.327/)
- Anthology ID: 2023.emnlp-main.327 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근에는 대용량 언어 모델 (LLM)의 문맥 학습이 여러 가지 작업에 대한 우수한 퓨샷 성능으로 인해 많은 관심을 받고 있다. 그러나 텍스트- SQL 파싱에서의 성능은 여전히 크게 향상될 여지가 있다. 
    2. 이 논문에서는 텍스트- SQL 파싱에 대한 LLM의 성능을 향상시키기 위한 핵심적인 측면은 다단계 추론 능력임을 가정한다. 그러므로 우리는 LLM의 추론 능력을 최적화하기 위해 chain-of-thought (CoT) 스타일 프롬프팅을 체계적으로 연구한다.
    3. 우리의 실험은 텍스트- SQL 파싱에는 최소-최대 프롬프팅과 같은 반복적인 프롬프팅이 필요하지 않을 수 있으며, 상세한 추론 단계를 사용하는 것은 오류 전파 문제가 더 많이 발생할 수 있다는 것을 보여준다. 이러한 결과를 바탕으로 우리는 텍스트- SQL 파싱을 위한 새로운 CoT 스타일 프롬프팅 방법을 제안한다.

###### Efficient Algorithms for Recognizing Weighted Tree-Adjoining Languages (https://aclanthology.org/2023.emnlp-main.328/)
- Anthology ID: 2023.emnlp-main.328 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 트리-결합 언어의 클래스는 컨텍스트-자유 문법 (CFG) 또는 pushdown 자동기계 (PDA)가 다른 CFG 또는 PDA를 제어하는 다양한 이중 형식을 사용하여 특성화될 수 있다.
    2. 이 논문에서는 위의 이중 형식들의 반지름-가중친 버전을 정의하고, 그들의 문자합 (문자 파생을 위한 가중치)과 전체합 (모든 파생의 가중치)을 계산하기 위한 새로운 알고리즘을 설계한다.
    3. 또한, TAG, LIG, PAA 및 EPDA에 대한 문자합과 전체합 알고리즘을 즉시 얻는다. (Vijay-Shanker and Weir (1989) 알고리즘에 비해 LIG의 경우 약 O(N|𝒩|) 시간적 효율성 및 O(𝛤) 공간적 효율성을 가지며, EPDA의 경우 Alonso et al. (2001) 알고리즘에 비해 O(𝛤^2) 및 O(|𝛤|3) 이상의 공간적 및 시간적 효율성을 갖는다.)

###### Harnessing Black-Box Control to Boost Commonsense in LM’s Generation (https://aclanthology.org/2023.emnlp-main.329/)
- Anthology ID: 2023.emnlp-main.329 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. GPT-3와 같은 대형 언어 모델은 일관성 있고 문맥에 적절한 텍스트를 생성할 수 있다. 그러나 생성된 출력물은 때때로 상식이 부족한 문제가 여전히 존재한다.
    2. 이 논문에서는 기존 Pre-Trained Language Model (PTLM)을 공통적 의미론적 특성을 더 잘 반영하도록 유도하는 계산 효율적인 프레임워크를 제안한다.
    3. 구축한 판단기를 가이드로 삼아 PTLM을 향상시키고, GPT-2, Flan-T5, Alpaca 기반 언어 모델에 적용하는 실험 결과, 가장 상식적인 출력이 나왔다고 보여진다.

###### Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback (https://aclanthology.org/2023.emnlp-main.330/)
- Anthology ID: 2023.emnlp-main.330 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실제 예측 시스템은 신뢰할 수 있는 확신 점수를 제공해야 하며, 답변에 대한 신뢰도는 정확한 답변의 가능성을 나타내어 신뢰도가 낮은 예측의 경우 전문가에게 이관할 수 있어야 한다.
    2. 최근 연구에 따르면, 관찰되는 현상에 대해 RLHF-LMs는 확지확율이 매우 나쁘게 보인다고 제안되었다. 이를 고려하여 우리는 RLHF-LMs에서 신뢰점수를 추출하는 다양한 방법을 평가한다.
    3. 우리의 연구에서는 ChatGPT, GPT-4, Claude와 같은 RLHF-LMs에 대해 TriviaQA, SciQ, TruthfulQA 벤치마크에서 출력 토큰으로 출력되는 신뢰 점수가 종종 기존의 조건부 확률과 비교하여 예상된 보정 오차를 상대적으로 50% 줄일 수 있음을 발견했다.

###### Representative Demonstration Selection for In-Context Learning with Two-Stage Determinantal Point Process (https://aclanthology.org/2023.emnlp-main.331/)
- Anthology ID: 2023.emnlp-main.331 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. In-Context Learning은 다양한 task에 효과적이지만, 시연 선택에 따라 그 효율이 크게 달라지고 있다. 기존 방법은 각 테스트 인스턴스마다 다른 시연을 선택하는데, 이는 시간 소모가 많고 실제 상황에서 제약사항이 있다. 이 논문은 특정 task에서 다양한 테스트 인스턴스를 효과적으로 유발할 수 있는 대표적인 in-context 시연의 부분집합을 선택하는 도전에 대해 다룬다. 
    2. 우리는 이 대표적인 부분집합이 높은 품질과 다양성을 갖추어야 한다고 제안한다. 실험 결과, 이러한 기준을 충족하는 시연은 모델의 성능을 향상시킬 수 있다는 것을 확인하였다. 
    3. 이를 위해, 우리는 품질과 다양성을 모두 고려한 두 단계의 Determinantal Point Process (DPP) 방법을 도입하여 대표적인 in-context 시연을 선택한다. 실험을 통해 우리의 제안 방법의 효과를 확인하였고, 더 실용적이고 효과적인 In-Context Learning을 위한 기반을 마련했다.

###### The Effect of Scaling, Retrieval Augmentation and Form on the Factual Consistency of Language Models (https://aclanthology.org/2023.emnlp-main.332/)
- Anthology ID: 2023.emnlp-main.332 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델은 사실 기반 지식에 자연스런 인터페이스를 제공하지만, 의미적으로 동일한 질문에 일관성 없는 답변을 하는 경향이 있다.
    2. 이 연구에서는 이러한 일관성의 원인을 파악하고, 두 가지 개선 전략인 up-scaling과 LM에 패시지 검색 데이터베이스를 추가하는 것의 효과를 평가한다.
    3. LLaMA 및 Atlas 모델에 대한 결과는 두 전략 모두 일관성을 감소시키지만, 검색 강화가 더 효율적임을 보여준다는 것을 보여준다. 또한, Atlas의 다양한 구성 요소들이 일관성에 어떤 기여를 하는지도 고려하고 분리한다.

###### ViPE: Visualise Pretty-much Everything (https://aclanthology.org/2023.emnlp-main.333/)
- Anthology ID: 2023.emnlp-main.333 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 비유적 표현과 비문법적 표현은 인간의 의사소통에서 깊이 통합되어 있다. 
    2. 이 연구에서는 이미지에 이러한 표현을 시각화하여 문화적인 생각을 전달하고 유감미 넘치는 감정을 불러일으킬 수 있는 "ViPE"를 소개한다.
    3. ViPE는 대규모로 훈련된 가사 데이터셋을 기반으로한 경량이고 강력한 언어 모델로, 인간 주석이나 이미지에 의존하지 않는다. ViPE는 임의의 텍스트를 시각적으로 표현 가능한 설명으로 변환하여 의미 있는 고품질 이미지 생성을 가능하게 한다.

###### Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models (https://aclanthology.org/2023.emnlp-main.334/)
- Anthology ID: 2023.emnlp-main.334 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문서 수준의 관계 추출 (DocRE)은 긴 맥락에서 관계를 추출하는 것으로, 세밀한 구조적 이해와 해석 가능한 문서 표현을 이루는 데 있어 중요한 도전과제이다.
    2. 이 논문은 대형 언어 모델 (LLM)인 ChatGPT와 같은 대형 모델의 in-context 학습 능력에서 영감을 받아 최소한의 인간 노력으로 DocRE를 자동 주석 처리하는 방법을 제안한다.
    3. 이를 위해, 사전에 정의된 다양한 세밀한 관계 유형과 LLM의 불규칙한 생성으로 인해 vanilla in-context 학습을 DocRE에 사용하기 어렵기 때문에, LLM과 자연어 추론 (NLI) 모듈을 통합하여 관계 삼중체를 생성하는 방법을 제안하고 이를 통해 문서 수준의 관계 데이터셋을 확장한다.

###### Navigating the Grey Area: How Expressions of Uncertainty and Overconfidence Affect Language Models (https://aclanthology.org/2023.emnlp-main.335/)
- Anthology ID: 2023.emnlp-main.335 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 실제 지식과 사실을 포함하는 실제 작업에 대한 LMs의 증가된 배치는 LMs가 무엇을 알고 있는지와 해당 지식에 대한 태도가 입력에서의 언어 사용에 어떻게 영향을 받는지 이해하는 것이 중요하다. 
    2. 우리는 epistemic marker의 여러 종류와 그들이 모델에 어떻게 영향을 주는지, 그리고 모델의 실패에 기여하는지를 연구한다. 
    3. 우리는 epistemic marker를 prompt로 삽입하고, LMs가 epistemic marker에 매우 민감하다는 것을 알게 되었다. 놀랍게도, 높은 확신의 표현은 정확성이 낮은 표현에 비해 7% 감소시키고, 사실을 나타내는 동사는 성능을 저하시키고, 증거를 나타내는 단어는 성능을 향상시킨다.

###### Elaborative Simplification as Implicit Questions Under Discussion (https://aclanthology.org/2023.emnlp-main.336/)
- Anthology ID: 2023.emnlp-main.336 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 텍스트 간소화는 복잡한 문장을 단순화된 문장으로 번역하는 단일 언어 번역 작업으로 간주되는 경우가 많다. 이 논문은 새로운 정보가 단순화된 텍스트에 추가되는 갈라놓는 단순화(elaborative simplification)를 고려해야 한다고 제안한다. 
    2. Question Under Discussion (QUD) 프레임워크로부터 갈라놓는 단순화를 바라보면, 작가들은 암묵적 질문에 대한 명시적 답변으로 갈라놓는다. 
    3. 이 논문에서는 ELABQUD 데이터셋을 소개하고, QUD 모델링을 통해 단순화의 품질을 향상시킬 수 있음을 보여준다.

###### EntSUMv2: Dataset, Models and Evaluation for More Abstractive Entity-Centric Summarization (https://aclanthology.org/2023.emnlp-main.337/)
- Anthology ID: 2023.emnlp-main.337 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Entity-centric summarization은 특정 entity에 대한 document의 요약을 생성하는 controllable summarization 형태로, 관련 어플리케이션에서 중요하다. 
    2. ENTSUMV2는 원래의 entity-centric ENTSUM 요약 dataset의 발전된 버전이다. 
    3. 이 논문에서는 supervised fine-tuning이나 large-scale instruction tuning을 사용하는 다양한 abstractive summarization 접근 방법으로 이 dataset에 대해 실험을 진행하고 당면 시스템들의 성능을 세밀하게 평가하고 향후 개선 방향을 제시한다.

###### SciRepEval: A Multi-Format Benchmark for Scientific Document Representations (https://aclanthology.org/2023.emnlp-main.338/)
- Anthology ID: 2023.emnlp-main.338 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 과학 문서 표현 평가 기준은 관련된 다양한 작업들의 다양성을 포착하지 못한다. 그래서 이 논문에서는 과학 문서 표현 모델의 일반화 능력을 개선하기 위한 첫 번째 종합적인 평가 기준인 SciRepEval을 소개한다. 이 평가 기준을 사용하여 SPECTER와 SciNCL과 같은 최신 모델의 일반화 능력을 연구하고 개선함을 보여준다.
    2. SPECTER2라는 다양한 형식들을 위한 멀티 포맷 모델 패밀리를 발표하고, 이 모델은 과학 문서 표현의 성능을 개선한다. 
    3. 이 논문에서는 문서에 대한 여러 개의 임베딩을 학습하는 새로운 접근 방식을 제시하고, 이를 통해 기존의 단일 임베딩 기반 최신 방법보다 더 뛰어난 성능을 보여준다.

###### A Diachronic Perspective on User Trust in AI under Uncertainty (https://aclanthology.org/2023.emnlp-main.339/)
- Anthology ID: 2023.emnlp-main.339 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인간-인공지능 협업에서 사용자들은 AI 시스템에 대한 "mental model"을 형성하게 되는데, 이는 시스템의 정확성과 예측 설명, 예측에 대한 신뢰도 등을 고려하여 형성된다. 그러나 현대의 NLP 시스템은 자주 confidence calibration이 이루어지지 않으며, 자신의 예측에 대해 자신감을 가지고 있는 경우가 많아 신뢰를 깎아내리게 된다. 
    2. 이 연구에서는 사용자들에게 NLP 시스템의 정확성에 대한 베팅을 시도하게 하고, 이를 통해 신뢰의 변화와 그 회복에 대해 연구한다.
    3. 몇 개의 불확실한 예측이 사용자의 신뢰를 상실시키고, 이후 시간이 지나도 회복이 어려움을 발견했으며, 신뢰를 회복하기 위해서는 확신을 가지고 잘못된 예측보다는 불확실한 상태에서 정확한 예측을 하는 것이 더 바람직함을 발견했다.

###### CT-GAT: Cross-Task Generative Adversarial Attack based on Transferability (https://aclanthology.org/2023.emnlp-main.340/)
- Anthology ID: 2023.emnlp-main.340 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존 전이 기반 방법들은 치료 모델을 사용하기 때문에 세부 정보가 없거나 실용적이지 않아 현실적인 상황에서 구현하는 것이 어렵다.
    2. 여기서는 다른 작업에 걸쳐 전이 가능한 특징을 추출하여 직접적으로 적대적인 예시를 구축하는 새로운 방법을 제안한다.
    3. 실험 결과, 작은 비용으로 우리의 방법이 우수한 공격 성능을 달성한다는 것을 보여준다.

###### Improving Long Document Topic Segmentation Models With Enhanced Coherence Modeling (https://aclanthology.org/2023.emnlp-main.341/)
- Anthology ID: 2023.emnlp-main.341 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 주제 분할은 구조화된 문서를 얻고 정보 검색과 같은 하위 작업의 성능을 향상시키기 위해 중요하다. 이 논문에서는 Topic-aware Sentence Structure Prediction (TSSP)와 Contrastive Semantic Similarity Learning (CSSL)을 제안하여 지도 모델이 논리적 구조와 의미적 유사성 측면에서 일관성을 파악할 수 있도록 모델의 능력을 강화하였다.
    2. TSSP는 모델이 무질서한 문서에서 문장 간 원래 관계를 학습함으로써 구조적 정보를 이해하도록 하는 작업이다. 이러한 불규칙한 문서는 주제와 문장 수준에서 원본 문서를 동시에 파괴하여 생성된다.
    3. 실험 결과, 우리의 방법을 활용한 Longformer가 이전의 최첨단 기법에 비해 크게 우수한 성능을 보였다. 우리의 방법은 WIKI-727K 데이터셋에서 이전 기법의 F1를 3.42 (73.74 → 77.16) 개선시켰으며, WikiSection에서는 Pk를 1.11 점 (15.0 → 13.89) 감소시켰다. 또한 두 개의 서로 다른 도메인 데이터셋에서는 평균 상대 Pk 감소율이 8.38%로 우리의 방법의 강건성을 입증하였다.

###### Dialogue Chain-of-Thought Distillation for Commonsense-aware Conversational Agents (https://aclanthology.org/2023.emnlp-main.342/)
- Anthology ID: 2023.emnlp-main.342 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 인류와 유사한 챗봇을 만들기 위해서는 대화 속 암시적인 정보를 효과적으로 이해하고 응답하기 위해 상식적 추론이 필요하다. 그러나 대화 속에서 핵심 증거를 식별하고 통합하는 일은 대규모 언어 모델에게도 어려운 작업이다. 이 논문에서는 이러한 다중 호핑 추론을 위해 지식 전달 기법을 제안한다. 
    2. 불안정한 선생님 역할을 하는 LLMs (대규모 언어 모델)로부터 일관된 지식을 추출하기 위한 지식 전달 프레임워크를 제안한다. 이를 통해 신뢰할 수 있는 CoT (대화주제의 연속성) 이유를 통해 대답을 생성할 수 있는 DOCTOR라고 하는 도구를 제공한다. 
    3. 실험 결과, DOCTOR를 통해 대화 에이전트의 응답 품질을 크게 향상시킬 수 있음을 보여준다.

###### Information Value: Measuring Utterance Predictability as Distance from Plausible Alternatives (https://aclanthology.org/2023.emnlp-main.343/)
- Anthology ID: 2023.emnlp-main.343 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 다른 가능성의 합리적 대안에 상대하여 언어 표현의 예측 가능성을 측정하는 정보 가치라는 지표를 제시한다.
    2. 우리는 신경 네트워크를 사용하여 정보 가치를 해석 가능한 방법으로 추정하는 방법을 도입하고, 그들의 심리학적 예측 능력을 활용하여 인간의 이해 행동을 이끌어내는 예측 가능성의 차원을 조사한다. 
    3. 정보 가치는 토큰 수준의 놀람(aggregates of token-level surprisal)보다 작성 및 말하기 다이얼로그에서 발화의 수용 가능성을 더 강력하게 예측하며, 눈 추적 독서 시간을 예측하기 위해 놀람과 보완적인 역할을 한다.

###### Generating Commonsense Counterfactuals for Stable Relation Extraction (https://aclanthology.org/2023.emnlp-main.344/)
- Anthology ID: 2023.emnlp-main.344 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대조적 확장 데이터 연구는 대개의 자연어 처리 과제에서 큰 성과를 이뤄냈다. 그러나 세부관계 추출 과제에서는 발생하는 두 가지 주요 문제가 있다. 첫째, 인과적 개념을 불변적으로 제한된 entity에서 정확하게 식별하기 어렵다. 둘째, 생활 상식(sense) 제약을 무시한다. 
    2. 이러한 문제를 해결하기 위해 우리는 안정적인 관계 추출을 위해 생성된 상식적 대조 사례에 대한 새로운 프레임워크를 제안한다. 구체적으로, 인과적인 용어를 정확하게 식별하기 위해 개입(인터벤션) 기반 전략을 도입하고, 구문 분석기를 사용하여 보정한다. 생활 상식 제약을 충족하기 위해 우리는 지식 베이스인 WordNet을 도입하고 하향식 관계 확장 알고리즘을 설계하여 entity 간의 생활 상식적 관계를 발견한다.
    3. 저희는 저자들이 저런 문제를 고려하여, 전래 추출 모델을 안정화하는 접근법을 소개함으로써, 다양한 평가, 심지어 자원이 적거나 타 도메인의 데이터, 공격적인 공격 등 실제 환경에서 안정성을 향상시킬 수 있음을 실험 결과를 통해 입증하였습니다.

###### C-STS: Conditional Semantic Textual Similarity (https://aclanthology.org/2023.emnlp-main.345/)
- Anthology ID: 2023.emnlp-main.345 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Semantic textual similarity (STS)는 NLP의 중요한 태스크인데, 문장 간의 유사성을 측정한다. 그러나 이 태스크는 특정 관점에 의존하여 문장의 유사성이 달라질 수 있는 모호한 문제다. 이 논문에서는 관련된 측면을 자연어로 명시하는 새로운 조건부 STS(C-STS)를 제안해서 STS의 주관성과 모호성을 해결하고 다양한 조건에서 문장의 세밀한 유사성을 평가할 수 있게 한다.
    2. C-STS는 약 20,000개의 다양한 도메인에서 문장 쌍을 포함하고 있으며, GPT-4, Flan, SimCSE와 같은 최첨단 모델들에 대한 실험을 통해 낮은 상관관계 점수를 얻는 등 어려움을 겪는 것을 보여준다.
    3. 이를 통해 저자들은 C-STS에서 세마틱 유사성과 자연어 이해에 대한 모델의 종합적인 평가를 제공할 것을 독려하고 있다.

###### Cross-lingual Transfer Can Worsen Bias in Sentiment Analysis (https://aclanthology.org/2023.emnlp-main.346/)
- Anthology ID: 2023.emnlp-main.346 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 감성 분석 시스템에서는 인종적 편견 문제가 있으며, 이러한 시스템에서는 transfer learning을 통해 다른 언어로 훈련된 pre-trained 모델을 사용한다.
    2. 이 연구에서는 다국어 transfer의 경우 성별이나 인종적 편견이 더욱 심화되는 경향이 있다는 것을 발견했다.
    3. 이에 따라 본 연구에서는 해당 분야의 추가 연구를 위해 사용된 sentiment 모델과 중간 체크포인트를 공개한다.

###### Rumor Detection on Social Media with Crowd Intelligence and ChatGPT-Assisted Networks (https://aclanthology.org/2023.emnlp-main.347/)
- Anthology ID: 2023.emnlp-main.347 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어를 통한 광범위한 정보 전파 시대에서 소문 탐지의 과제는 신뢰할 수 있는 정보 환경을 구성하는 데 중요한 역할을 한다. 
    2. 기존 소문 탐지 연구는 텍스트 인코딩 시퀀스의 한계, 도메인 지식 커버리지 및 지식 그래프 기반 방법을 통한 효과적인 정보 추출 및 의미 구조 정보의 부족이라는 여러 가지 도전에 직면하고 있다. 
    3. 이 논문에서는 소문 분류를 위해 인공지능 기반 크라우드 소스와 ChatGPT-Assisted Network(CICAN)을 제안한다. 이를 통해 순차적 및 계층적 특징을 포착하는 크라우드 소스 기반 의미 기능 학습 모듈과 지식 향상을 위해 ChatGPT를 활용하는 지식 기반 의미 구조 규모 모듈이 설계되었다.

###### Grounding Visual Illusions in Language: Do Vision-Language Models Perceive Illusions Like Humans? (https://aclanthology.org/2023.emnlp-main.348/)
- Anthology ID: 2023.emnlp-main.348 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Vision-Language Models (VLMs)은 인간의 세계 이해를 모사하는 인간들에 의해 수집된 방대한 양의 데이터를 기반으로 학습되었습니다. 그러나, 시각적 환각으로 알려진 대로, 인간의 현실 인식은 항상 실제 세계와 일치하지 않을 수 있습니다. 이로 인해 주요한 질문이 제기됩니다. VLMs는 인간과 같은 환각을 가지고 있는 걸까요? 아니면 실제 세계를 충실히 학습하는 건가요?
    2. 이 질문에 답하기 위해, 우리는 다섯 가지 유형의 시각적 환각을 포함하는 데이터셋을 구축하고 최신 VLMs에서 시각적 환각을 조사하기 위해 네 가지 작업을 정의했습니다.
    3. 우리의 연구 결과는 전반적으로 정렬이 낮지만, 더 큰 모델일수록 인간의 인식에 더 가깝고 시각적 환각에 더 취약하다는 것을 보여줍니다. 우리의 데이터셋과 초기 결과는 인간과 기계가 공유된 시각적 세계에 대해 인간과 기계를 더 잘 조화시킬 수 있는 미래의 계산 모델을 위한 기반을 마련할 것입니다.

###### Analysing State-Backed Propaganda Websites: a New Dataset and Linguistic Study (https://aclanthology.org/2023.emnlp-main.349/)
- Anthology ID: 2023.emnlp-main.349 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 논문은 Reliable Recent News (rrn.world)와 WarOnFakes (waronfakes.com)라는 두 사이트를 분석하여 국가 지원을 받은 가짜 뉴스에 대한 연구를 수행한다.
    2. 이들 사이트는 아랍어, 중국어, 영어, 프랑스어, 독일어, 스페인어로 콘텐츠를 발행하고 있으며, 이에 대한 다국어 데이터셋을 사용하여 토픽 클러스터링을 수행한다.
    3. 이 논문의 주요 기여는 가짜 뉴스 탐지를 위한 NLP 도구의 훈련에 필요한 고유한 데이터셋을 마련하고, 가짜뉴스 네트워크에 대한 연구를 가능하게 한다.

###### Controllable Contrastive Generation for Multilingual Biomedical Entity Linking (https://aclanthology.org/2023.emnlp-main.350/)
- Anthology ID: 2023.emnlp-main.350 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 다국어 바이오메디컬 entity linking(MBEL)은 생명과학 텍스트의 언어별 언급을 표준화된 개념(예: Unified Medical Language System)에 연결하는 것을 목표로 한다.
    2. Con2GEN은 MBEL을 판별적 분류기가 아닌 시퀀스-투-시퀀스 생성 과제로 정의함으로써 소스 언급과 타깃 entity 사이의 공유 종속성을 더 잘 활용한다.
    3. Con2GEN은 가능한 많은 언어와 유형의 UMLS 개념과 일치시켜 교차 정보의 모호성 해소를 용이하게 한다. 실험 결과, 이 모델은 12개 다양한 언어를 포함한 XL-BEL 및 Mantra GSC 데이터셋에서 몇 가지 최신 기술과 비교하여 유망한 성능 향상을 달성한다.

###### HyperRouter: Towards Efficient Training and Inference of Sparse Mixture of Experts (https://aclanthology.org/2023.emnlp-main.351/)
- Anthology ID: 2023.emnlp-main.351 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Sparse Mixture-of-Experts는 대규모 언어 모델의 효율적인 학습을 가능하게 해주는데, 최근 연구에서 모든 전문가가 결국 유사한 표현을 학습하는 문제를 완화하기 위해 router를 고정시키면 경쟁력있는 성능을 얻을 수 있다고 밝혀졌다.
    2. 하지만 이 전략은 두 가지 주요한 제한이 있는데, 첫째, 무작위 router에서 유도된 정책이 최적화가 되지 못할 수 있고, 둘째, 학습과 평가 과정에서 많은 자원을 필요로 하여 효율성의 한계가 발생할 수 있다.
    3. 이 논문에서는 HyperRouter를 소개하는데, 이는 고정된 하이퍼네트워크와 학습 가능한 임베딩을 통해 동적으로 router의 매개변수를 생성하여 더 나은 라우팅 정책을 학습하면서 라우터를 학습하고 고정시키는 균형을 이룬다. 다양한 태스크를 통해 수행된 실험은 HyperRouter의 우수한 성능과 효율성을 보여주었다.

###### MediaHG: Rethinking Eye-catchy Features in Social Media Headline Generation (https://aclanthology.org/2023.emnlp-main.352/)
- Anthology ID: 2023.emnlp-main.352 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 소셜 미디어 플랫폼에서의 매력적인 블로그 제목은 독자의 관심을 끌고 더 많은 클릭을 유도할 수 있습니다. 그러나 좋은 제목은 주요 내용을 압축하는 것뿐만 아니라 웹 사이트의 사용자와 목적에 의해 결정되는 도메인 플랫폼 특징으로도 눈에 띄어야 합니다. 
    2. 이 연구에서는 콘텐츠와 문맥적 특징을 균형있게 고려하는 headline generation 모델인 MediaHG (Social Media Headline Generation)을 제안합니다. 
    3. REDBook (중국 소셜 미디어 플랫폼)에서 수집된 70k개의 핫 포스트의 콘텐츠와 제목을 사용하여 실험 결과는 headline generation 태스크의 개선을 보여줍니다.

###### Fine-tuned LLMs Know More, Hallucinate Less with Few-Shot Sequence-to-Sequence Semantic Parsing over Wikidata (https://aclanthology.org/2023.emnlp-main.353/)
- Anthology ID: 2023.emnlp-main.353 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 큰 언어 모델(Large Language Models)은 많은 질문에 정확한 답을 할 수 있지만, 가끔 옳지 않은 답도 낼 수 있다. 본 논문에서는 Wikidata를 활용하여 언어 모델의 사실성을 향상시키기 위한 WikiWebQuestions라는 높은 품질의 질문-답변 벤치마크를 제안한다. 
    2. 이 논문에서는 Wikidata에 대한 few-shot sequence-to-sequence semantic parser를 제안한다. SPARQL을 수정하여 고유한 도메인과 속성명을 사용하고, entity linker의 결과나 쿼리 내의 언급을 활용하여 parser를 훈련시킨다. 
    3. 그 결과, 우리의 방법은 WikiWebQuestions의 dev와 test 세트에서 각각 76%와 65%의 답변 정확도를 보이며, QALD-7 Wikidata 데이터셋에서는 F1 score에서 최신 기법보다 3.6% 더 우수한 성능을 보인다.

###### ZEROTOP: Zero-Shot Task-Oriented Semantic Parsing using Large Language Models (https://aclanthology.org/2023.emnlp-main.354/)
- Anthology ID: 2023.emnlp-main.354 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이 연구에서는 대규모 언어 모델 (LLM) 을 사용하여 zero-shot 의미 파싱을 탐구한다. 의미 파싱은 자연어 발화를 과제에 특화된 의미 표현으로 매핑하는 작업을 의미한다. 
    2. 우리는 LLM이 제로샷 환경에서 도메인 특화 파싱 작업에 직접적으로 일반화될 수 없다는 문제를 해결하기 위해 ZEROTOP이라는 제로샷 과제 지향 파싱 방법을 제안한다. 
    3. 실험 결과, QA 기반 분해와 fine-tuned LLM을 결합한 우리의 접근법은 MTOP 데이터셋에서 약 16%의 발화를 zero-shot으로 파싱할 수 있다는 것을 보여준다.

###### Efficient Grammatical Error Correction Via Multi-Task Training and Optimized Training Schedule (https://aclanthology.org/2023.emnlp-main.355/)
- Anthology ID: 2023.emnlp-main.355 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 네트워크 문법 오류 수정(GEC)에서의 진전은 주석이 달려 있는 훈련 데이터의 부족으로 어려움을 겪고 있다. 이 논문에서는 사용 가능한 데이터를 보다 효율적으로 활용하는 두 가지 방법을 제안한다.
    2. 우선, 원래 문장과 수정된 문장 사이의 매핑을 활용한 보조 작업을 제안하고, 시퀀스-투-시퀀스 문제로 정의하여 멀티태스크 학습을 수행한다.
    3. 또한, 훈련에 사용되는 데이터셋의 순서와 개별 인스턴스의 순서는 최종 성능에 중요한 영향을 미친다는 것을 발견하고, 최적의 훈련 일정을 찾기 위해 연구한다. 이 두 가지 아이디어는 크기가 작은 모델로도 최신 기술을 개선하는 결과를 도출하여 T5-XXL(110B 파라미터)을 기반으로 한 최고의 모델을 BART 기반 모델로 능가한다.

###### The BLA Benchmark: Investigating Basic Language Abilities of Pre-Trained Multimodal Models (https://aclanthology.org/2023.emnlp-main.356/)
- Anthology ID: 2023.emnlp-main.356 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사전 학습된 언어와 시각 모델들의 하향 작업 성능이 인지모형에 기반한 이미지-텍스트 상호작용을 제대로 이해하는 것인지에 대한 의문이 남아있습니다.
    2. 이 연구에서는 유치원 아이들도 일반적으로 이해할 수 있는 능력인 능동-수동태, 연결어 및 관계절을 얼마나 잘 처리하는지 알아보기 위해 다양한 기존 모델과 새로운 벤치마크인 BLA를 사용하여 평가하였습니다.
    3. 실험 결과, 대부분의 모델들은 구체적인 구문을 사용하여 세밀하게 조정하거나 문맥 학습 환경에서 약간의 향상만을 보였지만, 생성 모델인 BLIP2는 희망적인 결과를 보여주어 BLA를 평가 벤치마크로 사용하고 모델의 기본 언어 능력을 향상시킬 수 있는 가능성을 열었습니다.

###### RainProof: An Umbrella to Shield Text Generator from Out-Of-Distribution Data (https://aclanthology.org/2023.emnlp-main.357/)
- Anthology ID: 2023.emnlp-main.357 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 번역부터 챗봇까지 NLP 모델의 적절한 기능과 보안을 보장하기 위해 효과적인 제어 메커니즘을 구현하는 것이 중요하다. 이 논문은 OOD(Out-Of-Distribution) 감지를 위해 블랙박스 프레임워크에서 soft-probabilities을 활용하는 방법에 초점을 맞추었다.
    2. 기존의 OOD 감지 방법들은 대부분 인코더의 hidden features에 의존하는 데 반해, 이 논문은 내부 상태에는 접근하지 못하지만 soft-predictions에 접근할 수 있는 블랙박스 프레임워크에서 soft-probabilities를 활용한다.
    3. 실험 결과, RAINPROOF는 전통적인 OOD 감지 방법보다 태스크 특정 성능 측정과 더 일치하는 OOD 감지 방법을 제공한다는 것을 보여주고 있다.

###### KEPL: Knowledge Enhanced Prompt Learning for Chinese Hypernym-Hyponym Extraction (https://aclanthology.org/2023.emnlp-main.358/)
- Anthology ID: 2023.emnlp-main.358 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. "Hypernym-hyponym ('is-a') 관계를 모델링하는 것은 분류, 자연어 추론 및 관계 추출과 같은 많은 자연어 처리 (NLP) 작업에서 매우 중요합니다. 기존의 is-a 관계 추출 연구는 대부분 영어 환경에서 이루어지고 있으며, 언어 표현의 유연성과 고품질의 중국어 주석 데이터셋의 부족으로 인해 중국어 비구조화된 텍스트에서 이러한 관계를 정확하게 식별하는 것은 여전히 도전과제입니다."
    2. 이 문제를 해결하기 위해, 우리는 중국어 hypernym-hyponym 관계 추출을 위한 지식 향상 프롬프트 학습 (KEPL) 방법을 제안합니다. 우리의 모델은 Hearst와 같은 패턴을 사전 지식으로 활용하며, Dynamic Adaptor Architecture를 이용하여 텍스트에 대한 매칭 패턴을 선택하여 모델은 동시에 패턴과 텍스트를 임베딩합니다.
    3. 또한, 우리는 중국 hypernym-hyponym 관계 추출 데이터셋을 만들었으며, 이는 baike, 뉴스 및 We-media와 같은 세 가지 대표적인 시나리오를 포함하고 있습니다. 데이터셋에서의 실험 결과는 우리가 제안한 모델의 효율성과 효과성을 입증하였습니다.

###### Ditto: A Simple and Efficient Approach to Improve Sentence Embeddings (https://aclanthology.org/2023.emnlp-main.359/)
- Anthology ID: 2023.emnlp-main.359 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기존의 pre-trained 언어 모델, 예를 들어 BERT에서 fine-tuning 없이 문장 표현에서의 간극 문제를 진단하는 연구가 이전에 이루어졌으며, 
    2. 우리의 분석 결과 BERT의 문장 임베딩은 아무런 정보가 없는 단어에 편향(bias)되어 있으며 이는 문맥 의미 유사도 작업에서의 성능을 제한한다. 
    3. 이러한 편향 문제를 해결하기 위해 우리는 단순하고 효율적인 비지도 학습 방법인 Diagonal Attention Pooling (Ditto)을 제안한다. Ditto는 pre-trained 모델에서 단어의 중요성을 모델 기반으로 가중치를 부여하고 가중치가 부여된 단어 표현의 평균을 문장 임베딩으로 계산하는 방법이다. Ditto는 매개변수를 추가하지 않고 학습을 요구하지 않으므로 다양한 pre-trained 모델에서 쉽게 적용될 수 있다. 실험 결과, Ditto는 anisotropy 문제를 완화시키고 STS 벤치마크에서 다양한 pre-trained 모델의 성능을 향상시킬 수 있다.

###### Preserving Knowledge Invariance: Rethinking Robustness Evaluation of Open Information Extraction (https://aclanthology.org/2023.emnlp-main.360/)
- Anthology ID: 2023.emnlp-main.360 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. NLP 모델들이 정보 추출과 같은 실제 세계에서도 성공적으로 적용될 수 있는데, 이를 위해 robustness가 필요하다. 하지만 이전 평가 벤치마크들은 주로 pairwise matching 정확성을 검증하는 데에 초점을 맞추어 왔고, robustness를 중요하게 평가하지 않았다.
    2. 이 논문에서는 open information extraction 모델들의 robustness를 실제 세계에서의 평가를 시뮬레이션하는 첫번째 벤치마크를 제시한다. 신택스와 의미적 분포가 다양하게 변할 수 있는 같은 의미를 가진 구조화된 지식을 포함하는 문장들로 이루어진 크리크로 구성된 대규모 테스트베드를 설계하고 주석을 달았다.
    3. 이 대규모 테스트베드를 이용하여 실제로 발표된 모델 및 대표적인 대형 언어 모델에 대한 실험을 수행한 결과, 기존의 성공적인 모델들이 최대 23.43 F1 스코어 감소와 같은 실망스러운 저하를 보였다.

###### Why Should This Article Be Deleted? Transparent Stance Detection in Multilingual Wikipedia Editor Discussions (https://aclanthology.org/2023.emnlp-main.361/)
- Anthology ID: 2023.emnlp-main.361 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인 플랫폼의 콘텐츠 중재는 일반적으로 비투명하다. 하지만 위키피디아에서는 이러한 토의가 공개적으로 이루어지며, 편집자들은 콘텐츠 중재 정책을 사용하여 중재 결정을 설명할 것을 권장받는다.
    2. 본 논문에서는 위키피디아 편집자들의 토의와 그들의 이유를 포함한 독창적인 다국어 데이터셋을 구축한다. 이 데이터셋은 각 편집 결정에 대한 편집자의 입장 (유지, 삭제, 통합, 코멘트)과 명시된 이유, 그리고 콘텐츠 중재 정책을 포함한다.
    3. 우리는 입장과 해당 이유 (정책)를 고도의 정확도로 공동으로 예측할 수 있음을 보여주며, 이는 결정 과정에 투명성을 추가한다는 것을 보여준다. 또한 우리는 공동 예측 모델과 다국어 콘텐츠 중재 데이터셋을 공개하여 자동화된 투명한 콘텐츠 중재에 대한 추가 연구를 위해 제공한다.

###### Fast and Robust Early-Exiting Framework for Autoregressive Language Models with Synchronized Parallel Decoding (https://aclanthology.org/2023.emnlp-main.362/)
- Anthology ID: 2023.emnlp-main.362 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Autoregressive 언어 모델의 높은 추론 지연 문제를 해결하기 위해 이전 연구에서는 후속 토큰 생성의 복잡성을 기반으로 각 토큰에 대한 적응형 계산 경로를 할당하는 초기 종료 (early-exiting) 프레임워크를 제안했으나, 상태 복사 메커니즘 또는 많은 종료 경로로 인한 성능 저하 및 종료 신뢰 임계값에 대한 민감성과 같은 몇 가지 단점이 관찰되었다.
    2. 이에 우리는 Fast and Robust Early-Exiting (FREE) 프레임워크를 제안하여 얕은-깊은 모듈과 동기화 병렬 디코딩을 통합하였다.
    3. 우리의 프레임워크는 현재 토큰의 디코딩 과정을 이전에 조기 종료된 토큰과 동기화하여 빠른 추론을 가능하게 한다. 또한 병렬 디코딩을 통해 얕은 모델과 깊은 모델의 예측을 관찰할 수 있으므로, Beta 혼합 모형을 활용하여 적절한 신뢰 임계값을 결정하는 새로운 적응형 임계값 추정기를 제시한다. 우리는 다양한 생성 태스크에서 우리가 제안한 프레임워크의 우수성을 실험적으로 입증하였다.

###### End-to-end Task-oriented Dialogue: A Survey of Tasks, Methods, and Future Directions (https://aclanthology.org/2023.emnlp-main.363/)
- Anthology ID: 2023.emnlp-main.363 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. end-to-end task-oriented dialogue (EToD)은 모듈식 학습 없이 단계별로 대화 응답을 생성할 수 있어서 점점 더 인기를 끌고 있다. 
    2. 이 논문에서는 EToD 연구의 존재하는 접근 방식과 최근 동향을 요약하여 통합적인 관점을 제시한다.
    3. 이 논문은 EToD 연구 분야에서 폭발적인 발전을 위한 잠재적인 고간과 도전과제를 논의하며, 업계 연구자들이 최근 연구 동향에 직접 접근할 수 있는 공개 웹사이트를 구축한다.

###### Answering Questions by Meta-Reasoning over Multiple Chains of Thought (https://aclanthology.org/2023.emnlp-main.364/)
- Anthology ID: 2023.emnlp-main.364 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 현대적인 다중 점프 질문 답변 시스템은 종종 일련의 추론 단계, 즉 chain-of-thought (CoT)로 질문을 분석한 후 최종 답변을 도출한다. 그러나 종종 여러 개의 체인을 샘플링하여 최종 답변을 투표 기법으로 집계하고 중간 단계는 버린다.
    2. 본 논문에서는 Multi-Chain Reasoning (MCR)이라는 접근법을 소개하는데, 이는 대규모 언어 모델에게 각각의 추론 체인에 대해 메타 추론을 수행하고 답변을 평균낼 대신 그들의 답변을 집계하는 것이다.
    3. MCR은 다양한 추론 체인을 검토하고 정보를 혼합하며 설명을 생성하고 답변을 예측하기 위해 가장 관련 있는 사실을 선택하므로 성능이 강력한 기준에 비해 우수하다. 또한 MCR 설명은 고품질을 갖추어 사람이 답을 검증할 수 있도록 한다.

###### INSTRUCTSCORE: Towards Explainable Text Generation Evaluation with Automatic Feedback (https://aclanthology.org/2023.emnlp-main.365/)
- Anthology ID: 2023.emnlp-main.365 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 학습된 언어 생성 metric은 인간 판단과 높은 상관관계를 보이지만, 이들 metric은 판단의 명확한 설명을 제공하지 않으며 생성된 텍스트의 결함과 점수를 연결시키지 않는다.
    2. 이 한계를 해결하기 위해, 우리는 INSTRUCTSCORE라는 텍스트 생성을 위한 detailed explanation을 제공하는 평가 metric을 제시한다.
    3. LLaMA를 기반으로 하여 인간의 명시적 지시와 GPT-4의 내재적 지식을 동원하여 text evaluation metric을 fine-tuning하고, 생성된 텍스트에 대한 점수와 사람이 읽을 수 있는 진단 보고서를 생성한다.

###### Multi-level Contrastive Learning for Script-based Character Understanding (https://aclanthology.org/2023.emnlp-main.366/)
- Anthology ID: 2023.emnlp-main.366 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 스크립트에서의 캐릭터 이해 시나리오를 다루는데에 있어서, 우리는 캐릭터의 성격과 정체성을 그들의 발언으로부터 학습하는 것을 목표로 한다.
    2. 이 논문에서는 이러한 시나리오에서의 여러 가지 도전과제들을 분석하고, 캐릭터들의 전역 정보를 세밀하게 포착하기 위한 다중 수준 대비 학습 프레임워크를 제안한다.
    3. 실험 결과에서 우리의 방법이 성능을 상당히 향상시키는 것을 보여주며, 이 방법이 도전과제들에 대응하는 데에 효과적임을 깊이 있는 분석을 통해 보여준다.

###### CHEF in the Language Kitchen: A Generative Data Augmentation Leveraging Korean Morpheme Ingredients (https://aclanthology.org/2023.emnlp-main.367/)
- Anthology ID: 2023.emnlp-main.367 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 한국어 형태학적 변이는 자연어처리(NLP)에서 독특한 기회와 도전을 제공하며, 형태소 기반 문장 구성에 대한 고급 이해가 필요하다.
    2. 우리는 이를 고려하여 모포(blender)와 라벨 판별자를 사용하는 CHEF라는 방법을 제안하여 형태소와 기능 형태소의 조합을 통해 문장의 형태학적 변형을 재현한다.
    3. 우리의 제안 방법은 외부 데이터 사용 없이 한국어 다중 분류 데이터셋에서 모델 성능을 향상시키며, 대규모 언어 모델을 이용한 다른 augmentation 기법과 비슷한 결과를 보이는 것을 실험을 통해 확인하였다.

###### Automatic Debate Evaluation with Argumentation Semantics and Natural Language Argument Graph Networks (https://aclanthology.org/2023.emnlp-main.368/)
- Anthology ID: 2023.emnlp-main.368 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 전문적인 논쟁 및 토론에 대한 주석이 달린 데이터 부족으로 인해 보다 복잡한 자연어 처리 작업에 접근하는 것이 현실적으로 어려워졌다.
    2. 이 논문에서는 논쟁 이론, 변환기 기반 아키텍처, 신경 그래프 네트워크와 같은 개념들을 결합하여 이러한 토론에서 승리 자세를 자동으로 예측하는 혼합 메소드를 제안한다.
    3. 우리는 미 탐색된 자연어 논증의 자동 분석에 대한 새로운 기초를 마련할 만한 유망한 결과를 얻었다.

###### Transfer-Free Data-Efficient Multilingual Slot Labeling (https://aclanthology.org/2023.emnlp-main.369/)
- Anthology ID: 2023.emnlp-main.369 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 슬롯 라벨링은 태스크 지향 대화 시스템에서 중요한 구성 요소이나, 언어, 태스크, 도메인에 특화된다. 이 논문은 흔히 비현실적인 가정에서 벗어나서 영어로 된 주석 데이터를 전혀 사용하지 않고, 대상 언어로 직접 다양한 언어를 포함한 데이터효율적인 슬롯 라벨러를 구축하는 방법을 제시한다.
    2. 이 논문에서는 슬롯 라벨링을 위해 표준 다국어 문장 인코더를 유효한 슬롯 라벨러로 변환하는 데에 두 단계의 접근법을 제안한다. 첫 단계에서는 소수의 주석된 예제만을 가지고 문장 인코더를 과제 특정 스팬 인코더로 변환한다. 두 번째 단계에서는 슬롯 라벨을 토큰 분류에서 데이터 부담이 적은 스팬 분류로 재구성한다.
    3. 실험 결과는 이 방법의 효과와 강건성을 확인하였고, 최도의 어려운 전이 없는 푸샷 설정에서 특히 효과적이며, 태스크 지향 대화 시스템을 위한 데이터 효율적인 다국어 슬롯 라벨러를 빠르게 구축할 수 있는 길을 열어준다.

###### Towards Interpretable Mental Health Analysis with Large Language Models (https://aclanthology.org/2023.emnlp-main.370/)
- Anthology ID: 2023.emnlp-main.370 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT와 같은 대규모 언어 모델은 자동 정신 건강 분석에서 강력한 능력을 보이지만, 기존 연구는 불충분한 평가, 프롬프트 전략의 부재 및 LLM 설명 가능성 탐구 무시 같은 여러 제한 사항을 갖고 있다.
    2. 우리는 5가지 작업에 걸쳐 11개 데이터셋에서 LLM의 정신 건강 분석 및 감정 추론 능력을 포괄적으로 평가한다. 또한 LLM에게 각각의 결정에 대한 설명을 생성하도록 지시하여 해석 가능한 정신 건강 분석에 대한 연구를 진행한다. 생성된 설명의 품질을 평가하기 위해 엄격한 인간 평가를 전달하며, 이를 바탕으로 163개의 인간 평가된 설명을 가진 새로운 데이터셋을 구축한다.
    3. 결과에 따르면, ChatGPT는 맥락에서의 학습 능력이 강하지만, 여전히 고급 작업 특화 방법과는 상당한 차이가 있다. 감정적 단서와 전문가가 작성한 부족한 샷 예제를 통해 신중한 프롬프트 엔지니어링은 정신 건강 분석 성능을 효과적으로 향상시킬 수도 있다. 게다가, ChatGPT는 인간의 성능과 유사한 설명을 생성하여, 설명 가능한 정신 건강 분석에서 큰 잠재력을 보여준다.

###### Learning to Rank Generation with Pairwise Partial Rewards (https://aclanthology.org/2023.emnlp-main.371/)
- Anthology ID: 2023.emnlp-main.371 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. supervised maximum likelihood estimation 접근 방식의 한계를 극복하기 위해 강화학습을 조건부 텍스트 생성에 사용하는 것을 연구했다.
    2. 이러한 방식은 대규모 행동 공간과 지연된 보상이라는 어려움을 여전히 겪고 있다.
    3. 우리는 중간 상태에서 취한 중간 행동에 대한 부분적인 보상을 제공하는 방법을 제안하여 더 원하는 시퀀스를 생성하는 행동을 우선적으로 선택할 수 있도록 했다.

###### GreedyCAS: Unsupervised Scientific Abstract Segmentation with Normalized Mutual Information (https://aclanthology.org/2023.emnlp-main.372/)
- Anthology ID: 2023.emnlp-main.372 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 과학 논문의 요약문은 일반적으로 전제 (배경 및 관찰)와 결론을 모두 포함한다. 하지만 구조화되지 않은 요약문에서는 결론 정보가 명시적으로 표시되지 않기 때문에 과학적 요약문에서 결론을 자동으로 분할하는 것은 어려운 작업이다.
    2. 본 연구에서는 Abstract segmentation에 Normalized Mutual Information (NMI)을 사용하는 방법을 제시한다. 우리는 각각의 요약문을 문장의 순환 주기로 간주하고, 선행 전제와 강한 의미적으로 연결되는 결론을 가정하여 두 세그먼트 간의 NMI 점수를 탐욕적으로 최적화하여 두 개의 분할 경계를 배치한다.
    3. 구조화되지 않은 요약문에서는 제안한 비지도 학습 방법인 GreedyCAS가 모든 평가 메트릭에서 가장 우수한 성능을 보였으며, 구조화된 요약문에서는 GreedyCAS가 Pk를 기준으로 모든 베이스라인 방법을 능가하였다. NMI의 강한 상관관계는 abstract segmentation에 대한 NMI의 효과를 보여준다.

###### Spoiler Detection as Semantic Text Matching (https://aclanthology.org/2023.emnlp-main.373/)
- Anthology ID: 2023.emnlp-main.373 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인에서 TV 쇼에 대한 토론에 참여하는 것은 스포일러를 피하기 위해 오랜 기간 동안 관련 콘텐츠를 소비하지 않아야 하는 경우가 많다. 
    2. 기존 스포일러 탐지 연구는 일반적인 스포일러로부터 시청자를 보호하는 데는 유망한 결과를 보이지만, 시청 중인 동안 콘텐츠를 제한하는 문제에 대해서는 다루지 못하고 있다. 
    3. 이 논문에서는 스포일러 일치 (spoiler matching)라는 과제를 제안하며, 특정 TV 쇼가 주어졌을 때 스포일러에 에피소드 번호를 할당하는 작업으로 문제를 해결한다.

###### Multimodal Embodied Plan Prediction Augmented with Synthetic Embodied Dialogue (https://aclanthology.org/2023.emnlp-main.374/)
- Anthology ID: 2023.emnlp-main.374 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 감각적인 작업 완료는 전체적으로 볼 때, 시뮬레이션 환경에서 요소 관점의 시각적 관찰과 자연어 지시에 기반하여 환경 동작을 예측하는 것이다.
    2. 우리는 agent의 동작이 더 해석 가능하도록 agent 동작을 추상화 된 더 높은 수준의 plan으로 예측하는 문제에 대한 변형을 제안한다.
    3. 우리는 multimodal transformer 모델이 이 문제에 대해 언어만 사용하는 모델을 능가하지만 오라클(plan)보다는 멀리 못하는 것을 보여준다.

###### GEM: Gestalt Enhanced Markup Language Model for Web Understanding via Render Tree (https://aclanthology.org/2023.emnlp-main.375/)
- Anthology ID: 2023.emnlp-main.375 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 이전의 사전 학습 언어 모델들은 텍스트를 넘어서는 인식 가능한 웹 컨텐츠에 포함된 풍부한 정보를 무시한다.
    2. 이 연구에서는 HTML 외에도 시각, 레이아웃, 스타일과 같은 렌더링된 웹의 중요한 정보를 활용하기 위해 제슈탈 심리학 이론에서 영감을 받은 GEM(Language Model)을 제안한다.
    3. 실험 결과, GEM은 웹 질문응답 및 웹 정보 추출과 같은 여러 다운스트림 작업에서 우수성을 검증한다.

###### Abstractive Open Information Extraction (https://aclanthology.org/2023.emnlp-main.376/)
- Anthology ID: 2023.emnlp-main.376 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. OpenIE는 자유로운 텍스트에서 구조화된 정보를 추출하여 다른 하위 응용 프로그램에 사용하는 전통적인 NLP 작업이다. 기존의 OpenIE는 원시 텍스트에 나타나는 관계의 표면 형태를 추출하는 것에 초점을 맞추었으며 이를 추출형 OpenIE라고 한다. 이 접근 방식의 한 가지 주요한 단점은 암묵적인 의미적 관계(추론된 관계)를 추출할 수 없어 하위 응용 프로그램의 성능에 문제가 발생한다는 것이다.
    2. 본 논문에서는 추출형 OpenIE에서 표면 형태의 관계뿐만 아니라 추론된 관계도 포함시킨 새로운 추상적 OpenIE로 OpenIE 관계를 확장한다. 이 새로운 작업을 위해 새로운 추상적 OpenIE 학습 데이터셋과 추론된 관계를 추출할 수 있는 기준선 신경망 모델의 개발이 필요하다. 또한, 추상적 OpenIE 추출을 평가하기 위한 새로운 의미 기반 메트릭의 필요성을 보여준다.
    3. 복잡한 QA의 사례 연구를 통해 추상적 OpenIE의 효과를 입증한다.

###### CoSyn: Detecting Implicit Hate Speech in Online Conversations Using a Context Synergized Hyperbolic Network (https://aclanthology.org/2023.emnlp-main.377/)
- Anthology ID: 2023.emnlp-main.377 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사회적 미디어 사용자들 간의 온라인 대화가 급증하면서 다양한 인종과 인구에 영향을 주는 혐오 발언의 증가로 이어졌다. 그러나 대부분의 연구들은 명시적인 혐오 발언을 감지하는 데 초점을 맞추고 있어 간접적이거나 암시적인 혐오 발언을 감지하는 데 작은 로부터 찾는데 집중이 되어있다.
    2. 저자들은 implicit hate speech를 감지하기 위해 사용자와 대화 상황에서의 문맥을 명확히 편입한 CoSyn이라 불리는 신경망 모델을 제안한다. CoSyn은 이러한 외부 문맥을 인코딩하는 새로운 방법을 도입하고, 그들 사이의 상호작용을 포착하여 노이즈가 있는 문맥에서 가져올 정보의 양을 독립적으로 평가하는 새로운 맥락 상호작용 메커니즘을 채택한다.
    3. 실험 결과, CoSyn은 6개의 혐오 발언 데이터셋에서 implicit hate speech를 감지하는 데에서 모든 기준 모델을 능가하며, 절대적인 개선 폭이 1.24%에서 57.8%에 이른다.

###### CLEME: Debiasing Multi-reference Evaluation for Grammatical Error Correction (https://aclanthology.org/2023.emnlp-main.378/)
- Anthology ID: 2023.emnlp-main.378 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문법 오류 교정(GEC) 시스템의 성능을 평가하는 것은 주관적인 요소가 많아 어려운 과제이다. 이 논문에서는 멀티 레퍼런스 평가 설정에서 GEC 시스템을 평가하기 위한 Chunk-LE 멀티 레퍼런스 평가(CLEME)를 제안한다. CLEME는 일관된 경계를 가진 청크 시퀀스를 구축하여 일관되지 않은 편집 경계로 인한 편향을 제거한다.
    2. CLEME를 사용하면 다중 레퍼런스가 있는 경우에도 단일 레퍼런스 평가 기준과 동일한 평가를 수행할 수 있으며, F0.5 점수를 통해 문법 오류의 경계를 파악하고 평가할 수 있다.
    3. 실험결과 CLEME는 다양한 레퍼런스 세트에서 GEC 시스템을 평가하는 데 효과적이며, 다른 레퍼런스 수와 주석 스타일에 따라 일관된 성능을 보인다는 것을 보여준다.

###### Dynamic Top-k Estimation Consolidates Disagreement between Feature Attribution Methods (https://aclanthology.org/2023.emnlp-main.379/)
- Anthology ID: 2023.emnlp-main.379 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 특징 귀속 점수는 텍스트 분류기의 예측을 사용자에게 설명하기 위해 k 개의 토큰을 강조하는 데 사용된다. 
    2. 이 논문에서는 특징 귀속 점수의 순차적 특성을 통해 보이는 최적의 k 토큰의 수를 결정하는 방법을 제안한다. 
    3. 연구 결과에 따르면, sequential properties를 활용하는 방법은 인간의 해석을 위해 특징 귀속 신호를 결합하는 데 유용하다는 것을 보여준다.

###### SentiStream: A Co-Training Framework for Adaptive Online Sentiment Analysis in Evolving Data Streams (https://aclanthology.org/2023.emnlp-main.380/)
- Anthology ID: 2023.emnlp-main.380 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 온라인 감성 분석은 소셜 미디어 모니터링, 고객 피드백 분석, 온라인 평판 관리와 같은 데이터 주도 어플리케이션에서 중요한 구성 요소로 부상했다. 
    2. 그러나 현재 방법론은 계속 진화하는 데이터 스트림을 효과적으로 다루기 어렵다. 
    3. 이 논문에서는 동적 데이터 스트림 내에서 효율적인 감성 분석을 위해 특별히 설계된 코트레이닝(co-training) 프레임워크인 sentistream을 제안한다.

###### HyperNetwork-based Decoupling to Improve Model Generalization for Few-Shot Relation Extraction (https://aclanthology.org/2023.emnlp-main.381/)
- Anthology ID: 2023.emnlp-main.381 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Few-shot relation extraction (FSRE)은 몇 개의 레이블 예제만을 사용하여 새로운 관계를 처리할 수 있는 모델을 훈련시키는 것을 목표로 한다. 
    2. 이 논문에서는 FSRE 모델의 클래스 분리를 조사한 결과, 상위 레이어가 관계에 특화된 지식을 학습하기 쉽다는 것을 발견하였다.
    3. 따라서 이 논문에서는 HyperNetwork 기반의 디커플링(Depouling) 접근법을 제안하여 FSRE 모델의 일반화 능력을 향상시키는 것을 목표로 한다.

###### Solving Hard Analogy Questions with Relation Embedding Chains (https://aclanthology.org/2023.emnlp-main.382/)
- Anthology ID: 2023.emnlp-main.382 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 단어들 간의 관련성 모델링은 어휘 의미론에서 중요한 주제이다. 일반적인 전략은 ConceptNet과 같은 지식 그래프(KG)를 활용하여 두 개념 간의 관계를 경로 집합으로 모델링하는 것이다.
    2. 그러나 KG는 고정된 관계 유형에 한정되어 있으며, 불완전하고 종종 노이즈가 있다. 또 다른 전략은 사전 훈련된 언어 모델에서 관계 임베딩을 추출하는 것이다. 그러나 이 방법은 직접적으로 관련되어 있지 않은 단어에는 적합하지 않으며 구조화된 도메인 지식을 쉽게 통합할 수 없다.
    3. 따라서, 이 논문에서는 경로로 관계를 모델링하면서 관계 임베딩을 사용하는 방법을 제안한다. 경로는 먼저 적절한 중간 단어를 식별한 다음, 정보가 있는 관계 임베딩을 얻을 수 있는 단어를 선택하여 얻는다. 우리의 제안된 표현은 어려운 유추 문제 해결에 유용하다는 것을 실험적으로 보여준다.

###### Modeling Empathic Similarity in Personal Narratives (https://aclanthology.org/2023.emnlp-main.383/)
- Anthology ID: 2023.emnlp-main.383 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 사람들 간 의미 있는 연결은 종종 개인적인 서술에서 공유된 취약성과 감정적인 경험을 통해 육성된다. 이 논문에서는 NLP 분야에서 지배적으로 연구되어온 의미론적이거나 어휘적인 유사성이 아닌 "감정 공감"을 기반으로 개인 이야기의 유사성을 판별하는 새로운 과제를 소개한다.
    2. 이 연구는 사회 심리학의 통찰력을 활용하여 이야기의 주요 사건, 감정적 경로, 전반적인 교훈 또는 결론이라는 세 가지 요소를 기반으로 감정 공감성을 구체화하는 프레임워크를 제안한다. EmpathicStories라는 데이터셋을 생성하여 감정 공감성 특징들로 주석을 달고, 이를 이용하여 이야기 쌍의 감정 공감성을 계산하기 위한 모델을 fine-tuning하였다.
    3. 실험 결과, 이 모델은 의미론적 유사성 모델보다 자동 상관 및 검색 메트릭에서 성능이 우수함을 보였다. 150명의 참가자를 대상으로 한 사용자 실험에서도, 우리의 모델을 사용한 이야기 검색 결과에 사용자들이 더 공감하였음을 확인하였다. 이 연구는 인간 간의 연결과 감정 공감을 육성하기 위해 감정 공감 모델의 활용에 강력한 함의를 지니고 있다.

###### Tree Prompting: Efficient Task Adaptation without Fine-Tuning (https://aclanthology.org/2023.emnlp-main.384/)
- Anthology ID: 2023.emnlp-main.384 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 작은 규모의 언어 모델에 대해서는 기울기 기반 fine-tuning과 비교했을 때, prompt 사용은 정확성이 낮다. 
    2. Tree Prompting은 여러 개의 prompt-LM 호출을 연결하여 문제를 해결하기 위해 prompt의 의사 결정 트리를 구축하는 접근 방식이다. 
    3. Tree Prompting은 classification 데이터셋에서 기존 방법보다 더 나은 정확성을 보여주고 fine-tuning과 경쟁력을 가진다.

###### Baize: An Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data (https://aclanthology.org/2023.emnlp-main.385/)
- Anthology ID: 2023.emnlp-main.385 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT와 같은 대화 모델은 탁월한 능력을 보여주고 다양한 분야에서 적극적으로 채용되고 있으나, 제한된 API를 통해서만 접근 가능하기 때문에 새로운 연구와 발전에는 장애물이 된다.
    2. 우리는 ChatGPT를 활용하여 자기 자신과 대화를 나누어 고품질의 멀티턴 대화 말뭉치를 자동으로 생성하는 파이프라인을 제안한다.
    3. 또한, 매개변수 효율적인 조정을 사용하여 오픈 소스인 LLaMA의 성능을 향상시키는 방식을 소개한다. 그 결과로 얻어진 Baize 모델은 잠재적인 위험을 최소화하는 경계선을 가진 멀티턴 대화에서 좋은 성능을 보여준다. 추가로, ChatGPT로부터의 피드백으로 Baize 모델의 성능을 개선하기 위한 새로운 기술인 Self-Distill with Feedback도 제안한다.

###### Empathy Intent Drives Empathy Detection (https://aclanthology.org/2023.emnlp-main.386/)
- Anthology ID: 2023.emnlp-main.386 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대화 시스템에서 공감 표현을 인식하는 것은 사용자의 필요를 이해하는 데 매우 관련이 있기 때문에 필수적이다.
    2. 본 논문에서는 8가지 공감 의도 레이블로 healthy empathy detection 데이터셋 IEMPATHIZE와 TwittEmp를 수동으로 주석을 달아 두 가지 작업에 대한 공동 훈련을 수행한다.
    3. 실험 결과를 통해 우리의 프레임워크가 두 데이터셋에서 모든 기준을 능가한다는 것을 보여준다.

###### Adaptive End-to-End Metric Learning for Zero-Shot Cross-Domain Slot Filling (https://aclanthology.org/2023.emnlp-main.387/)
- Anthology ID: 2023.emnlp-main.387 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 슬롯 채우기(slot filling)는 딥러닝과 대용량 주석이 달린 데이터의 가용성 덕분에 큰 발전을 이루었으나, 훈련 중 본적 없는 새로운 도메인을 다루는 것은 중요한 도전 과제이다.
    2. 기존의 메트릭 기반 접근 방식은 두 단계의 파이프라인 방식을 사용해 문제를 해결하지만, 병렬 추론과 컨텍스트-프리 이산 레이블 임베딩 때문에 계산 효율성과 일반화 능력에 한계가 있다.
    3. 본 연구에서는 전형적인 메트릭 기반 방법을 재조명하여, 도전적인 제로샷 슬롯 채우기에 대한 새로운 적응형 end-to-end 메트릭 학습 방법을 제안하였다. 컨텍스트를 고려한 소프트 레이블 표현과 슬롯 수준 대조 표현 학습을 결합하여 데이터와 레이블의 변화 문제를 효과적으로 완화하는 구조형 학습 프레임워크를 제안하였다.

###### BasahaCorpus: An Expanded Linguistic Resource for Readability Assessment in Central Philippine Languages (https://aclanthology.org/2023.emnlp-main.388/)
- Anthology ID: 2023.emnlp-main.388 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 자동 가독성 평가(Automatic Readability Assessment, ARA) 연구는 영어와 같은 고리소스 언어에서 모델의 성능을 향상시키기 위해 진행되어 왔다.
    2. 이 논문에서는 필리핀 낮은 리소스 언어에 대한 가독성 평가의 기존 코퍼스와 기준 모델을 확장하기 위한 BasahaCorpus를 소개하고 공개한다.
    3. 우리는 Hiligaynon, Minasbate, Karay-a, Rinconada와 같은 필리핀 센트럴 필리핀어 언어들로 작성된 짧은 허구 이야기의 코퍼스를 통해 ARA 모델을 훈련시킨다. 또한, 가족 트리 그룹에 속하는 언어의 배치를 활용하여 다중 언어 모델링 접근법을 제안한다.

###### ReTAG: Reasoning Aware Table to Analytic Text Generation (https://aclanthology.org/2023.emnlp-main.389/)
- Anthology ID: 2023.emnlp-main.389 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 테이블 요약 작업은 테이블이나 하이라이트된 특정 셀의 내용을 간결하고 정확하게 나타내는 텍스트를 생성하는 작업이다. 이 논문에서는 기존 모델들이 주로 테이블에 포함된 정보를 반복하는 기술적인 요약문을 생성한다는 문제를 지적하고 이에 대한 해결책으로 ReTAG라는 새로운 모델을 제안한다.
    2. ReTAG는 다양한 유형의 분석적인 추론력을 출력에 적용하기 위해 벡터 양자화를 사용하는 테이블과 추론에 민감한 모델이다. ReTAG는 기존 기준선에 비해 ToTTo와 InfoTabs에서 테이블 요약 작업을 수행하는데 있어서 PARENT metric에서 2.2%, 2.9%의 개선을 보인다.
    3. 사람 평가를 통해 ReTAG의 출력이 강력한 테이블 인식 모델에 비해 더 정확하고 분석적이라는 것을 확인할 수 있었다. ReTAG는 다중 테이블 요약 작업에서 최첨단 성능을 넘어설 수 있는 첫 번째 모델이다. 또한, 문장에 사용된 추론 카테고리를 각 데이터셋에 추출하여 기여하였다.

###### Beyond Factuality: A Comprehensive Evaluation of Large Language Models as Knowledge Generators (https://aclanthology.org/2023.emnlp-main.390/)
- Anthology ID: 2023.emnlp-main.390 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 큰 언어 모델들은 세계 지식 생성을 요청받을 때 정보 검색 기술을 능가하지만, 이러한 알고리즘을 사용하는 것의 사실 여부와 잠재적인 영향에 대한 걱정이 존재한다.
    2. 따라서 이 연구에서는 CONNER라는 종합적인 지식 평가 프레임워크를 소개하여 사실성, 관련성, 일관성, 정보성, 도움성 및 유효성 등 여섯 가지 관점에서 생성된 지식을 체계적으로 자동 평가할 것이다.
    3. 놀랍게도, 이 연구는 생성된 지식의 사실성이 낮더라도 다운스트림(Task-dependent) 작업에는 크게 영향을 미치지 않는다는 것을 밝혀냈다. 대신, 출력물의 관련성과 일관성이 사소한 사실적 오류보다 더 중요하다는 것을 보였다.

###### Compressing Context to Enhance Inference Efficiency of Large Language Models (https://aclanthology.org/2023.emnlp-main.391/)
- Anthology ID: 2023.emnlp-main.391 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근의 대형 언어 모델 (LLM)은 다양한 과제에서 장엄한 성과를 달성했으나, 긴 문서와 확장된 대화를 다루는 데 어려움을 겪고 있다.
    2. 이 논문에서는 Selective Context라는 방법을 제안하여 입력 문맥의 중복을 파악하고 제거하여 LLM의 추론 효율성을 향상시킨다.
    3. 실험 결과, Selective Context는 전체 문맥을 사용하는 경우와 비교하여 메모리 비용을 50% 감소시키며 응답 생성 시간을 32% 줄이고, 성능은 비슷한 수준을 유지한다는 것을 보여준다.

###### MoT: Memory-of-Thought Enables ChatGPT to Self-Improve (https://aclanthology.org/2023.emnlp-main.392/)
- Anthology ID: 2023.emnlp-main.392 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 최근 대형 언어 모델들은 다양한 과제에서 놀라운 성능을 보였으나, 이들을 본질적으로 개선하기 위해서는 고품질 데이터셋이나 계산적으로 비싼 fine-tuning이 필요하다. 반면에 사람은 외부 자료 없이도 스스로 사고하고 기억을 통해 쉽게 스스로를 개선할 수 있다. 
    2. 본 논문에서는 주석이 달린 데이터셋이나 매개변수 업데이트 없이 대형 언어 모델이 **MoT**라 불리는 "추억의 메모리"를 통해 스스로 개선할 수 있는 프레임워크를 제안한다.
    3. 실험 결과, MoT를 통해 ChatGPT가 산술 추론, 상식 추론, 사실적 추론, 자연어 추론과 같은 능력을 크게 향상시킬 수 있으며, 각 구성 요소가 개선에 중요한 역할을 하고 MoT가 다양한 CoT 방법과 대형 언어 모델에 일관되게 개선을 이끌어낼 수 있음을 보여준다.

###### 4 and 7-bit Labeling for Projective and Non-Projective Dependency Trees (https://aclanthology.org/2023.emnlp-main.393/)
- Anthology ID: 2023.emnlp-main.393 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 우리는 구문 분석을 시퀀스 레이블링으로 표현하는 인코딩을 소개하였다. 이 인코딩은 하나의 단어 당 4비트 레이블 시퀀스로 모든 projective 의존성 트리를 표현 할 수 있다.
    2. 우리는 이를 통해 트리에서 레이블로의 일대일 매핑을 선형 시간 안에 인코딩 및 디코딩할 수 있다는 것을 보여주었다.
    3. 실험 결과, 우리의 7비트 인코딩은 이전에 최고 성능의 시퀀스 레이블링 인코딩보다 상당한 정확도 향상을 얻는다.

###### Can You Follow Me? Testing Situational Understanding for ChatGPT (https://aclanthology.org/2023.emnlp-main.394/)
- Anthology ID: 2023.emnlp-main.394 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. ChatGPT와 같은 채팅 모델의 경우 Situational Understanding (SU)가 필요하며, 그러한 채팅 모델의 SU 능력을 테스트하기 위한 새로운 합성 환경을 제안한다.
    2. ChatGPT는 환경 상태를 올바르게 추적하는 능력이 부족하며, 이는 비지속적인 인문 학습을 반영하는 모델의 성능 저하와 관련되어 있다.
    3. ChatGPT의 대화 기술에 대한 신뢰는 위험을 동반하며, ChatGPT의 성능을 평가하기 위한 테스트 환경과 관련 코드는 공개되어 있다.

###### Towards Reliable Misinformation Mitigation: Generalization, Uncertainty, and GPT-4 (https://aclanthology.org/2023.emnlp-main.395/)
- Anthology ID: 2023.emnlp-main.395 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. Fake News에 대한 검증에 완벽한 분류가 불가능한 상황에서, 최근의 대형 언어 모델을 활용하여 정보의 진실성을 평가하기 위한 실용적인 도구를 만들기 위해 generalization, uncertainty에 초점을 맞추고 있는 연구다.
    2. 연구에서는 GPT-4가 다양한 setting과 언어에서 이전 방법보다 우수한 성능을 내는 것을 보였고, GPT-4와 RoBERTa-large가 실패 모드에서 차이점을 나타낸다는 사실을 밝혔다.
    3. 이 외에도 불확실성을 다루는 기술과 불가능한 예제를 감지하여 결과를 크게 개선하는 기술을 제안하였으며, 다양한 언어 모델, 온도, 프롬프팅, 버전 관리, 설명가능성, 웹 검색에 대한 결과를 논의하였다.

###### Advancements in Arabic Grammatical Error Detection and Correction: An Empirical Investigation (https://aclanthology.org/2023.emnlp-main.396/)
- Anthology ID: 2023.emnlp-main.396 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 문법 오류 수정은 영어에서 잘 연구된 문제이지만, 데이터 부족과 언어의 복잡성과 같은 도전 때문에 품사 풍부한 언어에서의 문법 오류 수정 연구는 제한되어 왔다.
    2. 이 논문에서는 새롭게 개발된 Transformer 기반의 사전 훈련된 시퀀스-투-시퀀스 모델을 사용하여 아랍어 문법 오류 수정 문제에 대한 최초의 결과를 제시한다.
    3. 우리는 또한 다중분류 아랍어 문법 오류 감지(GED) 작업을 정의하고, 다양한 장르를 포괄하는 세 개의 데이터셋에서 GED 정보를 보조 입력으로 사용하는 것이 GEC 성능을 개선하는 것을 보여준다.

###### HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models (https://aclanthology.org/2023.emnlp-main.397/)
- Anthology ID: 2023.emnlp-main.397 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델 (LLM)은 사실 또는 소스와 충돌하는 내용이나 검증할 수 없는 내용과 같은 환각을 생성하기 쉽다. 
    2. HalluEval 벤치마크를 통해 LLM의 환각 인식 능력을 평가하기 위해 생성 및 인간 주석이 달린 환각 샘플의 대규모 컬렉션을 도입한다. 
    3. ChatGPT는 특정 주제에서 검증할 수 없는 정보를 만들어내어 환각 콘텐츠를 생성할 가능성이 있다 (사용자 쿼리 약 19.5%). 게다가 기존 LLM은 텍스트 내의 환각을 인식하는 데 큰 어려움을 겪는다는 것이다.

###### Enabling Large Language Models to Generate Text with Citations (https://aclanthology.org/2023.emnlp-main.398/)
- Anthology ID: 2023.emnlp-main.398 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 정보 검색에 널리 사용되는 도구로 등장했지만 생성된 결과물은 환각에 빠지기 쉽다. 
    2. 이 연구의 목표는 LLMs가 주장에 대한 사실적 인정과 검증 가능성을 향상시키기 위해 사람 평가와 상업용 검색 엔진에 의존하는 기존 방법보다 더 재현성 높은 벤치마크를 제안하는 것이다.
    3. ALCE라는 벤치마크를 사용하여 LLMs의 자동 인용 평가에 대한 첫 번째 벤치마크를 수행하고 있으며, 자동 평가 메트릭을 개발하여 인간 판단과의 강한 상관관계를 보여준다.

###### Revisiting Machine Translation for Cross-lingual Classification (https://aclanthology.org/2023.emnlp-main.399/)
- Anthology ID: 2023.emnlp-main.399 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing 
- Summary: 
    1. 기계 번역(Machine Translation, MT)은 크로스-언어 분류에 널리 사용되는데, 이는 테스트 세트를 영어로 번역하고 단일 언어 모델로 추론을 실행하거나 (translate-test) 훈련 세트를 대상 언어로 번역하고 멀티 리더한 모델을 세밀 조정(translate-train)하는 방식이다. 
    2. 기존의 연구는 MT보다는 멀티링구어 모델에 집중되어 왔으나, 더 강력한 MT 시스템을 사용하고 훈련과 추론 간의 불일치를 완화함으로써 translate-test가 이전보다 훨씬 우수한 성능을 발휘할 수 있다고 보여준다. 
    3. 다만, 최적의 접근 방식은 과제에 따라 다르므로, 서로 다른 과제와 접근 방식에 영향을 미치는 여러 가지 크로스-언어 전달 차이 요인을 식별하는 것이 중요하다. 이 연구는 크로스-언어 분류를 위한 멀티링구어 모델의 지배력에 의문을 제기하며, MT 기반 베이스라인에 더 많은 주목을 촉구한다.

