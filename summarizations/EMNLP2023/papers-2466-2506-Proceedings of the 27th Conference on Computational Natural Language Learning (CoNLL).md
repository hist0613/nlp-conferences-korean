# Korean Three-Line Summarizations of Papers 2466-2506 in Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL)
###### Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) (https://aclanthology.org/2023.conll-1.0/)
- Anthology ID: 2023.conll-1.0 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors:  
- Summary: 
    요약문을 생성할 수 없습니다.

###### Can Language Models Be Tricked by Language Illusions? Easier with Syntax, Harder with Semantics (https://aclanthology.org/2023.conll-1.1/)
- Anthology ID: 2023.conll-1.1 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 언어 모델은 인간과 유사한 문법적 판단 작업에서 상당한 중복이 있다고 주장되었다. 그러나 인간이 언어 처리에서 일관적인 오류를 만들 때, 우리는 언어 모델이 인지 모델처럼 행동하고 인간의 행동을 모방할 것으로 기대해야 할까? 이 논문에서는 "언어 환각"에 관련된 미묘한 판단에 대해 언어 모델의 동작을 조사하여 이 질문에 대답한다.
    2. 언어 모델의 확률은 비교 환각이나 depth-charge 환각과 같은 심층적인 의미 이해를 요구하지만, NPI 환각의 경우에는 인간의 판단과 더 일치하는 경향이 있다. 어떤 언어 모델 또는 메트릭도 일관된 결과를 제공하지 않는다.
    3. 결국, 우리는 언어 모델이 인간의 언어 처리의 인지 모델로 쓸 수 있는 한계가 있으며, 복잡한 언어 자료에서 섬세하고 중요한 정보를 인식하는 능력도 한정되어 있다는 것을 보여준다.

###### ToMChallenges: A Principle-Guided Dataset and Diverse Evaluation Tasks for Exploring Theory of Mind (https://aclanthology.org/2023.conll-1.2/)
- Anthology ID: 2023.conll-1.2 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. "Theory of Mind (ToM), 즉 다른 사람의 정신 상태를 이해하는 능력은 다양한 실용적인 응용분야에 필수적이다. 그러나 대형 언어 모델 (LLM)의 ToM 작업 수행 능력에 대한 논란이 있다. 이 논문에서는 ToMChallenges라는 다양한 과제 세트가 포함된 Sally-Anne, Smarties 테스트에 기반한 ToM 평가를 위한 데이터셋을 제안한다."
    2. "우리는 davinci, turbo, gpt-4 세 가지 모델을 테스트해본 결과, LLM은 프롬프트와 작업에 따라 불일치하는 행동을 보이며 ToM 작업을 안정적으로 수행하는 것은 여전히 어려운 도전임을 보여준다."
    3. "또한, 우리의 논문은 LLM에서 ToM을 평가하는 데 대한 인식을 높이고, LLM의 능력을 더 잘 평가할 수 있는 ToM 과제와 프롬프트를 설계하기 위해 더 많은 논의를 이끌기 위한 것이다."

###### The Zipfian Challenge: Learning the statistical fingerprint of natural languages (https://aclanthology.org/2023.conll-1.3/)
- Anthology ID: 2023.conll-1.3 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 논문은 사람의 언어가 다른 소통 시스템과 기본적으로 다른 점을 구분해내는 것에 대한 "Zipfian Challenge"를 표준 분류 과제로 접근하는 것을 제안한다.
    2. 다양한 글쓰기 시스템과 언어, 심볼적이고 비복잡한 시스템 등을 포함한 텍스트 자료로 구성된 말뭉치를 사용하여 이진 분류 알고리즘을 훈련하고 테스트한다.
    3. 결과적으로 사람의 언어는 큰 단위 종류, 높은 엔트로피와 인접 단위의 반복 횟수가 적은 통계적 특징을 가지며, 이 특징은 다른 심볼적이고 비심볼적인 시스템과 구분하기 위해 사용될 수 있다.

###### On the Effects of Structural Modeling for Neural Semantic Parsing (https://aclanthology.org/2023.conll-1.4/)
- Anthology ID: 2023.conll-1.4 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 시멘틱 파싱은 자연어 문장을 논리 형식 또는 프로그래밍 언어와 같은 사전 정의된 형식 언어로 매핑하는 작업이다. 이 논문에서는 시멘틱 파싱과 관련하여 자연어와 형식 언어를 시퀀스로 처리하는 시멘틱 파서들의 구조 모델링 기법들을 평가하고, 구조 선택에 대한 메트릭을 제안하여 특정 데이터셋과 도메인에 대한 문법 설계의 자동화를 촉진할 수 있다고 주장하고 있다.
    2. 구조를 고려하는 시멘틱 파서들은 자연어와 형식 언어의 구조를 모델링하고, 모델의 소스와 타깃 측에 대한 구조 선택이 중요하다는 것을 밝혀냈다.
    3. 특정 데이터셋과 일반화 수준에 따라 구조가 설계되어야 하며, 소스와 타깃 측의 구조 선택보다는 양쪽을 조합하는 선택이 중요하다는 것을 발견하였다.

###### Humans and language models diverge when predicting repeating text (https://aclanthology.org/2023.conll-1.5/)
- Anthology ID: 2023.conll-1.5 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 다음 단어 예측을 학습한 언어 모델은 단어 예측과 읽기 속도에 있어 인간의 행동을 정확하게 모델링한다고 알려져 왔지만, 본 연구에서는 인간과 언어 모델의 성능이 다른 경우를 소개한다. 
    2. 반복되는 텍스트 구간을 가진 5개의 자극에 대한 인간의 다음 단어 예측 데이터셋을 수집하였고, 처음에는 인간과 GPT-2 언어 모델의 예측이 강하게 일치하지만, 기억력 (또는 문맥 학습)이 작용하기 시작하면 성능이 빠르게 차이가 나기 시작한다.
    3. 이 차이의 원인은 중간 레이어의 특정 어텐션 헤드에서 추적되었으며, 이러한 어텐션 헤드에 거듭 제곱 법칙의 최근성 바이어스를 추가하면 모델이 인간과 유사한 성능을 보인다. 이 연구는 언어 모델을 인간의 행동에 더 가깝게 만들기 위한 미래 연구를 촉진할 것을 기대한다.

###### Investigating the Nature of Disagreements on Mid-Scale Ratings: A Case Study on the Abstractness-Concreteness Continuum (https://aclanthology.org/2023.conll-1.6/)
- Anthology ID: 2023.conll-1.6 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 인간들은 척도에 대해 강한 합의를 보이지만 (예: 고양이는 매우 구체적으로 평가된다), 중간 단어에 대한 판단은 더 많은 불일치를 보인다. 그러나 수집된 평가 기준은 학문 분야 전반에 걸쳐 적용된다. 
    2. 이 연구는 구체성 평가에 초점을 맞추고, (i) 상관 관계와 감독 분류를 구현하여 중간 단어의 중요한 다중 모달 특성을 식별하고, (ii) 하드 클러스터링을 적용하여 평가자 간 체계적인 불일치 패턴을 식별한다. 
    3. 결과는 중간 척도 대상 단어를 세밀 조정하거나 거르기를 권장한다.

###### ArchBERT: Bi-Modal Understanding of Neural Architectures and Natural Languages (https://aclanthology.org/2023.conll-1.7/)
- Anthology ID: 2023.conll-1.7 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근 몇 년 동안 멀티모달 언어 모델 구축이 트렌드인데, 이미지, 비디오, 음성 등의 추가적인 모달리티를 자연어와 함께 학습한다. 
    2. 그러나 다양한 모달리티로 이루어진 멀티모달 언어 모델은 신경망 아키텍처와 자연어 간의 연결을 위한 기존 솔루션이 없다.
    3. 이 논문에서는 신경망 아키텍처와 자연어의 학습 및 이해를 위한 이중 학습 모델인 ArchBERT를 제안하며, 이를 통해 뉴럴 아키텍처나 간단한 텍스트 쿼리를 통한 AutoML 접근 방법을 개선하는데 도움을 줄 수 있다는 가치를 제시한다.

###### A Comparative Study on Textual Saliency of Styles from Eye Tracking, Annotations, and Language Models (https://aclanthology.org/2023.conll-1.8/)
- Anthology ID: 2023.conll-1.8 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근의 자연어 처리 파이프라인에서는 시선 추적 데이터와 같은 인간 언어 처리의 암묵적인 측정치를 통합하는 데에 대한 관심이 커지고 있다. 
    2. 이 논문은 언어 처리 데이터가 인간들의 언어 이해에 대한 독특한 통찰력을 포함하고 있으며 언어 모델에 의해 활용될 수 있다고 주장한다. 
    3. EyeStyliency라는 이름의 눈 추적 데이터셋을 소개하고, 이 데이터가 인간 주석 방법과 모델 기반의 중요도 점수와 어떻게 일치하는지 조사한다.

###### PROPRES: Investigating the Projectivity of Presupposition with Various Triggers and Environments (https://aclanthology.org/2023.conll-1.9/)
- Anthology ID: 2023.conll-1.9 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 발화의 사전추론은 다른 유추(entailment)와는 다르게 projectivity를 가지고 있는데, 여태까지는 이를 고려하지 않은 기존 자연언어 이해 연구들이 존재한다.
    2. 이 논문에서는 새로운 데이터셋인 PROPRES를 도입하며, 6가지 trigrer와 5가지 환경을 포함한 12,000개의 문장 쌍을 사용하여 모델의 성능을 평가한다.
    3. 사람들의 판단의 변동성과 언어학적인 항목의 조합을 고려하는 유용성 평가를 통해 DeBERTa 모델은 projectivity를 완전히 포착하지 못한다는 것을 보여준다.

###### A Minimal Approach for Natural Language Action Space in Text-based Games (https://aclanthology.org/2023.conll-1.10/)
- Anthology ID: 2023.conll-1.10 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. Text-based games에서는 language models (LMs)와 knowledge graphs (KGs)를 사용하여 대화형 환경을 다루는데, 이러한 기술이 필요한지 혹은 과도하게 사용되었는지에 대해 불분명하다.
    2. 본 논문에서는 action space를 탐색하는 문제에 다시 초점을 맞추고, admissible한 액션들을 활용하는 minimal한 𝜖-admissible exploration을 제안한다.
    3. 본 연구는 Jericho의 10개 게임을 기준으로, KG나 LM을 사용하지 않고 오로지 게임 관측 정보만을 활용해 텍스트 명령을 생성하는 text-based actor-critic (TAC) 에이전트를 제시한다. 이 방법은 강력한 베이스라인 및 최신 기법을 뛰어넘는 성능을 보여주며, 지수적으로 큰 액션 공간을 효과적으로 탐색하기 위해 더 가벼운 모델 디자인과 환경 내 정보의 새로운 관점을 강조한다.

###### Structural Ambiguity and its Disambiguation in Language Model Based Parsers: the Case of Dutch Clause Relativization (https://aclanthology.org/2023.conll-1.11/)
- Anthology ID: 2023.conll-1.11 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 논문은 네덜란드어 관계 절의 구조적 모호함에 대해 다룬다. '지지를 통한 모호함 해소' 작업을 통해, 이전 문장의 존재가 관계 절의 모호함을 해소하는 방법을 연구한다. 이 방법을 두 개의 구문 분석 구조에 적용하여 현대 신경망 구문 분석기의 구문 분석과 언어 모델 구성 요소를 분석한다.
    2. 결과는 proof nets을 기반으로 한 neurosymbolic 구문 분석기가 universal dependencies를 기반으로 한 접근 방식보다 데이터 편향 보정에 더 개방적이지만, 두 가지 설정 모두 유사한 초기 데이터 편향에 문제가 있다.
    3. (이 외에는 다른 특별한 내용이 없는 것 같으므로 더이상 추가로 요약하지 않겠습니다.)

###### On the utility of enhancing BERT syntactic bias with Token Reordering Pretraining (https://aclanthology.org/2023.conll-1.12/)
- Anthology ID: 2023.conll-1.12 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근에는 자기 지도 학습 언어 모델이 사전 훈련에 대한 기본 선택 사항이 되었지만, Token Reordering (TOR) 사전 훈련 목표는 토큰 예측 이상으로 깊게 연구되지 않았다.
    2. 이 연구에서는 일부 토큰 입력이 주어졌을 때 두 토큰이 인접한지 여부를 예측하는 새로운 TOR 사전 훈련 목표를 설계하였다.
    3. 결과적으로 TOR는 GLUE 언어 이해 벤치마크에서 MLM에 대비해 경쟁력이 있으며, 특히 구문 종속적인 데이터셋에서는 몇몇 샷 학습 설정에서 약간 우위에 있다.

###### Quirk or Palmer: A Comparative Study of Modal Verb Frameworks with Annotated Datasets (https://aclanthology.org/2023.conll-1.13/)
- Anthology ID: 2023.conll-1.13 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 일상 대화에서 사용되는 모달 동사는 발화자의 관점을 전달하는 데에 널리 사용되지만, 그 사용 방법과 문맥에 따라 의미가 크게 달라질 수 있다. 그러나 모달 동사의 의미 분류에 대해서는 언어학자들 간에 합의가 없다. 
    2. 본 논문에서는 MoVerb 데이터셋을 소개하는데, 이 데이터셋에는 사회적 대화에서 하나 이상의 문장을 포함한 4,540개의 발화에 대한 27,240개의 모달 동사 의미 주석이 포함되어 있다. 
    3. MoVerb 데이터셋을 사용하여 RoBERTa 기반 분류기를 훈련시키고, Quirk와 Palmer 프레임워크에 대해 각각 82.2와 78.3의 F1 스코어를 달성하여 모달 동사의 의미 모호성 해결이 쉬운 작업이 아님을 보여주었다.

###### Quantifying Information of Tokens for Simple and Flexible Simultaneous Machine Translation (https://aclanthology.org/2023.conll-1.14/)
- Anthology ID: 2023.conll-1.14 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. Simultaneous Translation (ST)은 전체 소스 입력이 아닌 일부 소스 입력만으로 번역하는 것으로 번역 품질의 저하 가능성이 있다. 이전 접근 방식은 번역 품질과 응답 지연 시간의 균형을 맞추기 위해 합리적인 정책을 가진 오프라인 모델을 활용하는 것이 더 효과적이라는 것을 보였다.
    2. 그러나 오프라인 모델 사용은 부분 소스 입력으로 훈련되지 않았기 때문에 분포 변화를 일으키며, 언제 번역을 수행할지 알려주는 추가 모듈을 통해 개선할 수 있다.
    3. 본 논문에서는 소스와 대상 정보를 모델링하여 오프라인 모델이 번역에 충분한 정보를 가지고 있는지 판단하는 정보 양자 (IQ)를 제안한다. IQ는 정보를 양자화함으로써 Simultaneous Translation을 위한 적합한 정책을 구성하는 데 도움이 되며, 품질과 지연 시간 사이의 균형을 자연스럽게 제어할 수 있다. 여러 언어 쌍에서의 실험 결과, 제안한 모델이 기준 모델보다 우수한 성능을 보였다.

###### Enhancing Code-mixed Text Generation Using Synthetic Data Filtering in Neural Machine Translation (https://aclanthology.org/2023.conll-1.15/)
- Anthology ID: 2023.conll-1.15 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 코드믹싱은 다중 언어 사회에서 흔히 사용되는 의사소통 현상이지만, 데이터의 품질이 NLP 시스템에 큰 제약을 둔다. 이 논문에서는 인간의 판단을 활용하여 고품질의 코드믹싱 문장을 생성하는 신경 기계 번역 방법을 제안한다.
    2. 인견 판단을 기반으로 필터를 훈련시켜 합성된 코드믹싱 문장에서 자연스러운 코드믹싱 문장을 식별하는 여러 프레러럴 코퍼스를 생성한다. 이를 활용하여 다중 언어 인코더-디코더 모델을 학습시키고, 더 나은 코드믹싱 생성 결과를 얻을 수 있다.
    3. 힌디어-영어 뿐만 아니라, 저자원 언어인 텔루구어의 코드믹싱 문장 생성에도 효과적이다.

###### Towards Better Evaluation of Instruction-Following: A Case-Study in Summarization (https://aclanthology.org/2023.conll-1.16/)
- Anthology ID: 2023.conll-1.16 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근의 발전에도 불구하고, 대형 언어 모델이 사용자 지시를 얼마나 잘 따르는지 평가하는 것은 여전히 열려 있는 문제이다.
    2. 언어 모델의 평가 방법은 prompt 기반 접근법에 대한 연구가 늘어났으나, 이러한 방법들의 정확성에 대한 연구는 제한적이다.
    3. 우리는 grounded query-based 요약을 통해 언어 모델의 지시 따르기 능력을 정확하게 측정하는 다양한 메트릭의 메타-평가를 수행하였다.

###### Syntactic Inductive Bias in Transformer Language Models: Especially Helpful for Low-Resource Languages? (https://aclanthology.org/2023.conll-1.17/)
- Anthology ID: 2023.conll-1.17 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. BERT와 같은 Transformer 기반 언어 모델의 구문 인지 편향은 많은 데이터를 필요로 하지 않고 훈련을 강화시킬 수 있을 것이라는 이론에 기반하여 개발되었다. 하지만 이러한 방법들은 영어와 같은 high-resource 언어에서 주로 테스트되었다. 
    2. 따라서 본 연구에서는 이러한 방법들이 low-resource 언어의 데이터 부족 문제를 보완할 수 있는지 조사하였고, low-resource 언어에서의 효과가 더 크다는 가설을 세웠다.
    3. 우리는 Uyghur, Wolof, Maltese, Coptic, 그리고 Ancient Greek이라는 다섯 가지의 low-resource 언어를 실험 대상으로 하였고, 이러한 구문 인지 편향 방법들이 low-resource 환경에서 일정하지 않은 결과를 도출하며, 대부분의 경우에 놀랍도록 적은 혜택을 제공한다는 사실을 발견하였다.

###### Attribution and Alignment: Effects of Local Context Repetition on Utterance Production and Comprehension in Dialogue (https://aclanthology.org/2023.conll-1.18/)
- Anthology ID: 2023.conll-1.18 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 현대 대화 시스템의 기반으로 자주 사용되는 언어 모델은 대량의 작성된 유창한 언어로 사전 학습된다. 하지만 대화에서는 반복이 중요한 요소이다. 이 연구에서는 (a) 언어 모델이 대화에서 인간과 유사한 수준의 반복을 생성하는지, (b) 이해과정에서 어휘 재사용과 관련된 처리 메커니즘에 대해 평가한다. 
    2. 우리는 모델 생성과 이해 행동의 공동 분석이 인지적 영감을 받은 대화 생성 시스템의 개발에 도움을 줄 수 있다고 믿는다. 
    3. 사람들은 로컬하게 반복하고 파트너에게 특정 반복을 사용하며, 이는 인간 사용자가 선호하며 대화에서 더 성공적인 커뮤니케이션으로 이어진다.

###### The Validity of Evaluation Results: Assessing Concurrence Across Compositionality Benchmarks (https://aclanthology.org/2023.conll-1.19/)
- Anthology ID: 2023.conll-1.19 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근 NLP 모델은 많은 데이터셋을 통해 성능을 평가하였지만, 특정 데이터셋 설계 선택이 모델 능력에 대한 결론에 어떤 영향을 미치는지에 대한 의문이 남아있다.
    2. 이 연구에서 우리는 합성성 일반화의 도메인에서 6가지 모델링 접근 방식을 4개 데이터셋에 걸쳐 조사하였고, 8가지 합성 분할 전략에 따라서도 성능을 평가하였다. 결과는 다음과 같다: i) 합성 일반화를 평가하기 위해 설계된 데이터셋은 각기 다른 모델링 접근 방식에 대해 다르게 선호하는 경향이 있었다. ii) 사람이 생성한 데이터셋은 인공적인 데이터셋 보다 서로 더 일치하였다. iii) 데이터셋의 원본이 같은지 여부가 구성적 합성의 해석을 유지하는지 여부보다 모델 순위에 더 많은 예측력을 가지고 있었다. iv) 데이터셋 내의 특정 어휘 항목이 측정 일관성에 영향을 미치는 것으로 나타났다.
    3. 전체적으로, 우리의 결과는 인기 있는 평가 데이터셋이 의도한 바를 측정하는지 여부를 평가하는 데에는 아직 많은 작업이 남아있고, 보다 엄격한 기준을 제시함으로써 평가 세트의 타당성을 확립하는 것이 이 분야에 도움이 될 수 있다는 것을 시사한다.

###### Mind the instructions: a holistic evaluation of consistency and interactions in prompt-based learning (https://aclanthology.org/2023.conll-1.20/)
- Anthology ID: 2023.conll-1.20 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 현재 NLP에서 사전 학습 언어 모델을 작업에 적응하는 가장 좋은 방법을 찾는 것은 큰 도전이다. 이 논문은 in-context-learning(ICL)이나 instruction tuning(IT)을 통해 작업에 적응된 모델들이 어떤 상황에서는 강건하고, 다른 상황에서는 그렇지 않은 이유에 대해 상세한 분석을 제시한다.
    2. 먼저, TT 모델에서 알려진 문제인 입력 분포와 레이블 사이의 의미 없는 상관관계는 prompted 모델에서는 거의 문제가 되지 않는다는 것을 보여준다.
    3. 그런 다음, prompting 설정에서 예측에 영향을 미치는 다양한 요소들을 체계적으로 ganz리적으로 평가한다. 이들 요소의 모든 가능한 조합을 테스트하고, 다양한 크기의 일반 LLM과 instruction-tuned LLM에서 결과를 통계적으로 분석하여 가장 영향력이 크거나 상호작용하는 요소들, 그리고 가장 안정적인 요소들을 보여준다.

###### Med-HALT: Medical Domain Hallucination Test for Large Language Models (https://aclanthology.org/2023.conll-1.21/)
- Anthology ID: 2023.conll-1.21 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 연구 논문은 대형 언어 모델(LLM)에서 발생하는 환각에 초점을 맞추고 있으며, 특히 의료 분야에서의 환각 문제를 다룹니다.
    2. Med-HALT (의료 분야 환각 테스트)라는 새로운 벤치마크와 데이터셋을 제안하여 환각을 평가하고 줄이는 데에 목적이 있습니다.
    3. Med-HALT는 다양한 국가에서 수행된 의료 검사를 기반으로 한 다양한 테스트 모달리티를 포함하고 있으며, LLM의 문제 해결 및 정보 검색 능력을 평가하는 데 사용됩니다.

###### Revising with a Backward Glance: Regressions and Skips during Reading as Cognitive Signals for Revision Policies in Incremental Processing (https://aclanthology.org/2023.conll-1.22/)
- Anthology ID: 2023.conll-1.22 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. NLP에서 incremental processors는 언어 입력의 접두사에 기반하여 출력을 단계적으로 생성한다. 하지만 모델이 왜 수정을 하는지에 대해서는 잘 알려져 있지 않다. 
    2. 수정이 필요한 시점을 감지하는 정책은 효율성을 향상시킬 수 있다. 하지만 수정 정책을 훈련시키기 위한 적절한 신호를 찾는 것은 여전히 문제이다. 
    3. 이 연구에서는 인간의 독해 시간에 따른 회귀(regressions)와 스킵(skips)이 수정을 위한 신호로 사용될 수 있는지 조사하였으며, 다양한 언어에 대해 BiLSTM 및 Transformer 모델에 일관된 결과를 얻었다.

###### ChiSCor: A Corpus of Freely-Told Fantasy Stories by Dutch Children for Computational Linguistics and Cognitive Science (https://aclanthology.org/2023.conll-1.23/)
- Anthology ID: 2023.conll-1.23 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 논문에서는 자연적인 맥락에서 어린이들이 자유롭게 이야기하는 619개의 판타지 이야기를 포함한 새로운 코퍼스인 ChiSCor를 소개한다.
    2. ChiSCor는 어린이의 인지와 언어를 이해하기 위한 계산 도구로 해당 이야기들을 연구하기 위해 구성되었다.
    3. ChiSCor는 언어와 인지의 발전에 따른 어린이의 캐릭터 시각화 방식을 연구하는데 유용하며, Zipf의 법칙에도 잘 부합된다는 사실과 함께 언어 처리를 위한 설명 벡터를 학습하기에 충분히 풍부하다는 것을 보여주고 있다.

###### HNC: Leveraging Hard Negative Captions towards Models with Fine-Grained Visual-Linguistic Comprehension Capabilities (https://aclanthology.org/2023.conll-1.24/)
- Anthology ID: 2023.conll-1.24 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이미지-텍스트 매칭(ITM)은 비전과 언어에서 대량 말뭉치로부터 일반화된 표현을 학습하기 위한 방법 중 하나이다. 하지만 웹에서 수집한 이미지-텍스트 쌍 간의 약한 연관성으로 인해 모델들은 이 모달리티의 결합된 의미를 세밀하게 이해하지 못한다.
    2. 따라서 우리는 세밀한 교차 모달 이해를 달성하기 위해 ITM 학습에 사용되는 traiing set을 위한 어려운 부정적인 캡션이 포함된 HNC라는 자동 생성된 데이터셋을 제안한다.
    3. 우리의 결과는 HNC에서의 학습이 임상적인 작업에서 미스매치 감지의 제로샷 능력을 향상시키고, 잡음이 있는 시각적 입력 시나리오에서 강력한 성능을 발휘함을 보여준다. 또한 HNC 모델이 세밀 조정을 위한 비교적 좋은 초기화를 제공한다는 것을 보여준다.

###### Theory of Mind in Large Language Models: Examining Performance of 11 State-of-the-Art models vs. Children Aged 7-10 on Advanced Tests (https://aclanthology.org/2023.conll-1.25/)
- Anthology ID: 2023.conll-1.25 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 큰 언어 모델 (LLMs)에는 Theory of Mind (ToM)과 같은 의도와 믿음에 대한 추론 능력을 어느 정도 부여해야 할까요? 이 논문에서는 (i) 대세인 잘못된 믿음 패러다임 외에도 ToM과 관련된 능력을 11개의 베이스-LLMs와 인스트럭션 튜닝 된 LLMs로 테스트하고, (ii) 표준화된 테스트의 새로운 버전을 사용하여 LLMs의 강건성을 평가하고, (iii) 폐쇄적 질문 외에도 개방형 질문 점수화를 위한 프롬프트와 점수화를 수행하며, (iv) 동일한 태스크에서 7-10세 어린이와 LLM의 실적을 벤치마킹합니다.
    2. GPT 계열의 인스트럭션 튜닝 LLMs이 다른 모델보다 우수한 성능을 보이며, 종종 어린이보다 뛰어납니다. 베이스 LLMs는 대부분 특화된 프롬프트로도 ToM 태스크를 해결할 수 없습니다.
    3. 우리는 언어와 ToM의 상호 연결된 진화와 발달이 인스트럭션 튜닝이 추가되는 이유를 설명하는 데 도움이 될 수 있다고 제안합니다. 상대방과 맥락을 고려한 협력적인 커뮤니케이션을 보상하는 것입니다. LLMs에서 ToM에 대한 세심한 관점을 주장합니다.

###### A Block Metropolis-Hastings Sampler for Controllable Energy-based Text Generation (https://aclanthology.org/2023.conll-1.26/)
- Anthology ID: 2023.conll-1.26 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 최근의 연구는 에너지 기반 언어 모델링이 임의의 판별기를 유연하게 통합할 수 있는 효과적인 텍스트 생성 프레임워크임을 입증했습니다.
    2. 그러나 전체 정규화를 수행하는 에너지 기반 언어 모델은 추론에 Metropolis-Hastings (MH)와 같은 근사 기법을 필요로 합니다.
    3. 이 논문에서는 대조적으로, 한 번의 단계에서 전체 시퀀스를 다시 작성하는 새로운 MH 샘플러를 개발하여, 더 효율적이고 정확한 대상 분포 샘플링이 가능해집니다.

###### How Fragile is Relation Extraction under Entity Replacements? (https://aclanthology.org/2023.conll-1.27/)
- Anthology ID: 2023.conll-1.27 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. Relation Extraction (RE)은 텍스트 컨텍스트에서 엔티티 간의 관계를 추출하는 것을 목표로 한다. 하지만 기존의 모델은 텍스트 컨텍스트 대신 엔티티 이름 패턴을 기억하여 예측하기 때문에, 문장에 있는 관계가 무시된다고 밝혀졌다.
    2. 본 논문에서는 대체된 엔티티에 대한 복원력 있는 RE 모델의 필요성을 제기하고, TACRED 데이터셋에서 상태-of-the-art RE 모델의 자리에 랜덤하고 타입 제한 조건이 있는 엔티티를 대체하여 실험을 진행하였다.
    3. 실험 결과, 상태-of-the-art RE 모델이 엔티티 대체에 대해 30%~50% F1 score 하락을 보였으며, 이는 엔티티 대체에 강건한 효과적인 RE 모델 개발을 위해 더 많은 노력이 필요하다는 것을 시사한다.

###### JaSPICE: Automatic Evaluation Metric Using Predicate-Argument Structures for Image Captioning Models (https://aclanthology.org/2023.conll-1.28/)
- Anthology ID: 2023.conll-1.28 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이미지 캡션 생성은 BLEU와 METEOR과 같은 자동 평가 메트릭에 많이 의존하는데, n-gram 기반 메트릭은 인간 평가와 상관관계가 낮다고 보고되어, 영어를 위한 SPICE와 같은 대체 메트릭이 제안되었다.
    2. 이 연구에서는 일본어 자막을 scene graph를 기반으로 평가하는 자동 평가 메트릭인 JaSPICE를 제안한다. 제안된 방법은 의존성과 술어-인자 구조를 통해 scene graph를 생성하고, 동의어를 활용하여 그래프를 확장한다.
    3. STAIR Captions와 PFN-PIC에서 학습한 10개의 이미지 캡션 모델을 실험에 활용하고, 103,170개의 인간 평가를 포함하는 Shichimi 데이터셋을 구축하여, 우리의 평가 메트릭이 인간 평가와 상관관계에서 기준 메트릭보다 우수한 성능을 보였다.

###### MuLER: Detailed and Scalable Reference-based Evaluation (https://aclanthology.org/2023.conll-1.29/)
- Anthology ID: 2023.conll-1.29 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. MuLER은 기계번역 (MT)을 비롯한 텍스트 생성의 참조 기반 평가 메트릭을 세밀한 분석 도구로 변환하는 새로운 방법론을 제안한다. MuLER은 선택한 메트릭이 특정 오류 유형 (예: 위치 이름 번역 오류)에 얼마나 엄격한지를 정량화하여 세부적인 오류 분석이 가능하게 한다.
    2. MT 평가뿐만 아니라 요약 등 다른 작업에서 MuLER의 유용성을 보여주기 위해 합성 및 자연적인 환경에서 실험을 수행하였다. 2014-2020년 WMT의 모든 제출물을 분석한 결과, 일관된 트렌드를 발견했는데, 명사와 동사가 가장 빈번한 POS 태그 중 하나지만 번역하기 가장 어렵다는 것이다.
    3. 요약 작업을 통한 초기 실험 결과도 유사한 트렌드를 보여주었다.

###### The Impact of Familiarity on Naming Variation: A Study on Object Naming in Mandarin Chinese (https://aclanthology.org/2023.conll-1.30/)
- Anthology ID: 2023.conll-1.30 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 동일한 객체 또는 개체에 대해 다른 화자는 종종 다른 이름을 사용하며, 이러한 이름의 변동은 잘 이해되지 않는다.
    2. 우리는 중국어에 대한 언어 및 비전 데이터셋을 만들어보고, 주어진 객체에 대한 익숙함과 주제 간의 명명 변동의 정도와의 관계를 조사한다.
    3. 우리는 익숙함이 두 가지 경쟁적인 방식으로 명명 변동에 영향을 미친다고 제안하는데, 익숙함은 어휘를 확장시켜 변동을 높일 수도 있고, 일반적인 이름으로 수렴을 촉진하여 변동을 줄일 수도 있다.

###### PSST! Prosodic Speech Segmentation with Transformers (https://aclanthology.org/2023.conll-1.31/)
- Anthology ID: 2023.conll-1.31 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 우리는 비번역화된 대화형 영어 음성에서 주곡선 구분을 감지하기 위한 모델을 개발하고 조사한다. 
    2. 이 모델은 Transformer 기반 음성-텍스트(STT) 모델을 fine-tuning하여, 음성 인식 작업과 Intonation Unit (IU) 경계 식별을 통합한 것이다. 
    3. 우리는 모델이 다양한 사투리와 전사 프로토콜을 대표하는 분포 외의 데이터에서도 강건한 성능을 보이며, 프로소딕 구조를 알리는데 일반적으로 이해되는 음향적 정보만이 아니라 오디오에서 추론된 어휘 및 구문 정보에 의존하는 것을 확인하였다.

###### Alignment via Mutual Information (https://aclanthology.org/2023.conll-1.32/)
- Anthology ID: 2023.conll-1.32 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 많은 언어 학습 태스크들은 두 모드 간의 데이터 상응관계를 추론하는 것을 요구한다. 종종 이러한 상응관계는 다대다 및 문맥 종속적이다.
    2. 저자들은 문맥 종속적이고 다대다 매핑을 위해 정보 이론적 접근방법을 설명한다. 저자들은 먼저 마스킹된 순서 모델을 학습하여 (소스, 타겟) 순서의 빠진 구간에 대한 분포를 배치한다. 그런 다음 이 모델을 사용하여 문맥에 조건부로 소스와 타겟 구간 간의 점별 상호정보를 계산한다.
    3. 제안된 이 방법은 구조화된 방법과 신경망 기반 기준을 모두 능가하는 성능을 보여주며, 조건부 상호정보는 일반적인 도메인에서 상응관계 문제를 형식화하는 효과적인 프레임워크를 제공한다는 것을 보여준다.

###### Challenging the “One Single Vector per Token” Assumption (https://aclanthology.org/2023.conll-1.33/)
- Anthology ID: 2023.conll-1.33 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 논문은 각 토큰이 하나의 벡터로 표현되어야 한다는 네트워크 내의 전체적인 가정에 대해 의문을 제기한다.
    2. 실험 결과, 의존 문법 분석에서 각 토큰을 벡터의 시퀀스로 표현하는 것이 더 나은 성능을 보인다는 것을 보여준다.
    3. 이 결과는 순환 신경망에서 토큰을 처리하는 방식에 대한 추가적인 연구가 필요하다는 것을 시사한다.

###### Strategies to Improve Low-Resource Agglutinative Languages Morphological Inflection (https://aclanthology.org/2023.conll-1.34/)
- Anthology ID: 2023.conll-1.34 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 형태학적 변형은 형태학 분야에서 중요한 과제로, 보통은 시퀀스 변환 작업으로 간주된다. 최근 몇 년간 많은 연구자들의 관심을 받아 상당한 진전을 이루었으며, 고-저자원 언어에 대해 인상적인 성능을 달성하였다. 그러나 훈련 데이터셋의 인스턴스 분포가 변경되거나, 새로운 lemma나 특징 레이블이 예측되는 상황에서 모델의 정확도는 떨어진다.
    2. 접착어(agglutinative) 언어에서는 형태학적 변형 시 새로운 단어를 생성하면서 음운 사상(phonological phenomena)이 관여하며, 이는 원형(lemma)과 접미사 사이의 음절 패턴을 변경시킬 수 있다.
    3. 이 논문에서는 저자원 접착어 언어에 적용할 수 있는 4가지 전략을 제안한다. 이를 통해 모델의 일반화 능력을 향상시킬 수 있는데, 이는 합성어의 음절과 피처 레이블의 순서를 학습하거나, 원형 내에서 공통 부분 문자열을 인식하여 단어로 복사하는 등의 방식을 포함한다. 실험결과, 제안된 모델이 다른 베이스라인 모델보다 우수한 성능을 보였다.

###### Exploring Transformers as Compact, Data-efficient Language Models (https://aclanthology.org/2023.conll-1.35/)
- Anthology ID: 2023.conll-1.35 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 대부분의 트랜스포머 모델은 매우 크기 때문에 한정된 컴퓨팅 자원을 가진 사람들은 이 모델들을 사용할 수 없다.
    2. 이 논문에서는 5.7백만 개의 파라미터로도 트랜스포머 모델을 축소시킬 수 있으며, 대부분의 downstream 능력을 유지할 수 있다는 것을 보여준다.
    3. 또한, 5백만 단어의 pretraining 데이터로 훈련된 트랜스포머 모델도 상당한 결과를 유지할 수 있으며, 복잡한 모델 압축 방법이 항상 훨씬 우수한 것은 아니라는 것을 보여준다.

###### Tree-shape Uncertainty for Analyzing the Inherent Branching Bias of Unsupervised Parsing Models (https://aclanthology.org/2023.conll-1.36/)
- Anthology ID: 2023.conll-1.36 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 이 논문은 tree-shape uncertainty의 형식화를 제안하여, 텍스트만을 사용하여 비지도 파싱 모델의 내재적인 분기 경향(branching bias)을 분석할 수 있게 한다. 
    2. 이전 연구들은 훈련된 파서의 출력을 골드 문법 트리와 비교하여 비지도 파싱 모델의 분기 경향을 분석했지만, 이러한 접근은 텍스트가 서로 다른 문법에서 생성될 수 있다는 점을 고려하지 않고 모델이 학습한 훈련 데이터의 편향과 모델의 내재적인 편향을 명확하게 분리하지 못할 수 있다.
    3. 이를 위해, 우리는 tree-shape uncertainty를 공식화하고, 편향된 정보가 없을 것으로 예상되는 텍스트를 생성하기 위해 사용할 수 있는 충분한 조건을 도출한다. 실험에서는 이러한 편향이 없는 텍스트로 파서를 훈련시키면 기존의 비지도 파싱 모델의 분기 편향을 효과적으로 탐지할 수 있음을 보여준다.

###### Future Lens: Anticipating Subsequent Tokens from a Single Hidden State (https://aclanthology.org/2023.conll-1.37/)
- Anthology ID: 2023.conll-1.37 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 개별 입력 토큰에 대응하는 숨겨진 상태 벡터는 몇 개의 토큰을 정확하게 예측하는 데 충분한 정보를 포함한다고 추측한다.
    2. 이 논문은 단일 토큰의 숨겨진 (내부) 표현을 통해 t + 2 이상의 위치에 나타날 토큰을 신뢰성 있게 예측할 수 있는지 알아보고 있다.
    3. GPT-J-6B에서 선형 대략화와 인과적 개입 방법을 측정하여 네트워크의 개별 숨겨진 상태가 미래의 숨겨진 상태와 토큰 출력을 예측하기에 충분한 신호를 포함하는 정도를 평가한다고 한다.

###### Cross-Document Event Coreference Resolution: Instruct Humans or Instruct GPT? (https://aclanthology.org/2023.conll-1.38/)
- Anthology ID: 2023.conll-1.38 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 본 논문에서는 대형 언어 모델을 사용하여 Cross-Document Event Coreference Resolution (CDEC) 주석을 수행하고, 다양한 수준의 학습을 받은 사람 주석자와 어떻게 맞선지 평가한다.
    2. GPT-4 기반의 zero-shot 학습 결과, 대부분의 경우 사람 주석자보다 우수한 성능을 보이며 학습된 주석자와 비교 가능한 수준의 성능을 나타낸다.
    3. 그러나 GPT-4는 과도하게 자신감이 있으며, 충분한 정보가 없는 경우에도 강제적으로 주석 결정을 내릴 수 있다는 특성을 보인다.따라서 본 연구는 LLM시대에서 CDEC와 같은 복잡한 주석을 수행하는 방법에 대한 함의가 있다. 고품질 데이터를 확보하기 위해서 LLM의 장점과 학습된 인간 주석자의 강점을 결합하는 것이 가장 효율적인 방법일 것이다.

###### Implications of Annotation Artifacts in Edge Probing Test Datasets (https://aclanthology.org/2023.conll-1.39/)
- Anthology ID: 2023.conll-1.39 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. 엣지 프로빙 테스트는 LLM과 같은 문맥 인코더에서 나온 토큰 표현에 문법 지식이 인코딩되어 있는지를 확인하는 분류 작업이다. 많은 LLM 인코더가 이러한 테스트에서 높은 성능을 보여줌에 따라 언어 지식을 인코딩하는 능력에 대한 추측이 제기되었다.
    2. 그러나 많은 연구에서는 이러한 테스트가 LLM의 인코딩 능력을 측정하는 것이 아니라 분류기의 문제 학습 능력을 반영한다는 것을 주장하고 있다. 특히, LLM 대 무작위 인코더를 사용할 때 분류기의 정확도가 매우 유사한 경우가 많다.
    3. 이 논문에서는 널리 사용되는 엣지 프로빙 테스트 데이터셋에는 외움을 포함한 다양한 편향이 있다는 것을 보여준다. 이러한 편향이 제거되면 단순한 비정보 이론적 프로브라도 LLM 인코더와 무작위 인코더 사이에 유의미한 차이가 나타난다.

###### REFER: An End-to-end Rationale Extraction Framework for Explanation Regularization (https://aclanthology.org/2023.conll-1.40/)
- Anthology ID: 2023.conll-1.40 
- Volume: Proceedings of the 27th Conference on Computational Natural Language Learning (CoNLL) 
- Authors: Jing Jiang | David Reitter | Shumin Deng 
- Summary: 
    1. "인간-주석 기반 텍스트 설명은 설명 가능한 자연어 처리에서 점점 중요해지고 있다. 이 논문에서는 다음을 목표로 하는 rationale extraction을 제안한다. 이는 예측에 가장 큰 영향을 미친 입력을 강조하여 모델의 행동을 신뢰할 만한 설명을 제공함과 동시에 성능을 희생시키지 않는다."
    2. "기존 작업에서는 주로 plausibility 최적화를 위해 인간의 주석을 사용해 rationale extractor를 훈련시키고, task model은 task 예측 정확도와 faithfulness을 동시에 최적화하는 방식을 사용했다."
    3. "우리는 REFER라는 프레임워크를 제안하여 rationale extraction 과정에 back-propagation을 허용하는 differentiable rationale extractor를 사용하는 것의 효과를 분석했다. 실험 결과, REFER는 신뢰성, 타당성, 그리고 새로운 데이터에서도 downstream task 정확도 측면에서 이전 기준점들보다 크게 향상된 결과를 보여준다."

