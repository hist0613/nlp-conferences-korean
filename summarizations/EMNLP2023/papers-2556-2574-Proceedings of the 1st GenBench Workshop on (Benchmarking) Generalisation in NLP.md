# Korean Three-Line Summarizations of Papers 2556-2574 in Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP
###### Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP (https://aclanthology.org/2023.genbench-1.0/)
- Anthology ID: 2023.genbench-1.0 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    요약문을 생성할 수 없습니다.

###### 90% F1 Score in Relation Triple Extraction: Is it Real? (https://aclanthology.org/2023.genbench-1.1/)
- Anthology ID: 2023.genbench-1.1 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 지식 베이스 구축을 위한 텍스트에서 관계적인 triple을 추출하는 것은 중요한 과제이다. 기존의 모델들은 실제적인 실험 환경과 비현실적인 데이터셋에서 평가되어 왔다. 이 논문에서는 실제적인 환경에서 최신 모델들을 벤치마크로 평가하는 연구를 제시한다.
    2. 이 논문은 기존 모델들은 zero triple을 가지는 문장을 무시하여 작업을 단순화하였고, 이로 인해 실제적인 실험 환경에서 성능이 상당히 저하되는 것을 보였다.
    3. 이 논문에서는 더 실제적인 환경에서의 성능 향상을 위해, 간단한 BERT 기반 분류기를 활용하는 두 단계의 모델링 접근법을 제안한다. 이는 실제적인 실험 환경에서 전반적인 성능 향상을 이끌어냈다.

###### GenCodeSearchNet: A Benchmark Test Suite for Evaluating Generalization in Programming Language Understanding (https://aclanthology.org/2023.genbench-1.2/)
- Anthology ID: 2023.genbench-1.2 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 언어 모델들은 소프트웨어 개발자들에게 생산성을 높일 수 있는 가치있는 도구로 사용될 수 있다. 그러나 기존의 훈련 데이터는 주로 인기 있는 프로그래밍 언어에 초점을 맞추고 있어서 저-resource 프로그래밍 언어들을 간과한다. 
    2. 우리는 Hupkes et.,al.에 의해 제안된 NLP 일반화 탐색법에 영감을 받아, 언어 모델의 프로그래밍 언어 이해 일반화 능력을 체계적으로 평가하기 위한 벤치마크 데이터셋인 GenCodeSearchNet (GeCS)을 제안한다. 
    3. R은 컴퓨터 과학 분야에서 벗어난 연구자들에게 널리 사용되는 인기있는 프로그래밍 언어이지만, 그 동안 크게 다루어지지 않은 언어로, 이를 중점적으로 다루는 Manuelly curated subset인 StatCodeSearch를 도입한다.

###### Adapt and Decompose: Efficient Generalization of Text-to-SQL via Domain Adapted Least-To-Most Prompting (https://aclanthology.org/2023.genbench-1.3/)
- Anthology ID: 2023.genbench-1.3 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. Text-to-SQL 문장 파싱의 cross-domain과 cross-compositional generalization은 어려운 작업이다. 기존 모델들은 테스트할 Natural Language (NL) 쿼리마다 추론 시간에 적은 수의 exemplar를 training set에서 추출하여 실행 시 prompt를 합성하는 방식을 사용한다. 그러나 우리는 오프라인 샘플링을 통해 학습 데이터에서 최소한의 few-shot을 선택하는 알고리즘을 개발하여 매번 expensive 한 exemplar 검색 시간을 피하고, 다양한 exemplar로 구성된 고정된 Generic Prompt (GP)을 합성함으로써 NL 테스트 쿼리에 대한 완전한 커버리지를 제공한다.
    2. 우리는 또한 대상 데이터베이스 도메인에 맞게 GP를 자동으로 적응시키는 DA-GP를 추가로 개발하여 cross-domain generalization을 더 잘 다룰 수 있다. 그리고 cross-compositional generalization을 다루기 위해 Least-To-Most-Prompting (LTMP-DA-GP)를 분해하는 방법을 사용한다.
    3. 우리의 접근 방식은 Text-to-SQL 작업의 일반화 능력을 평가하기 위해 설계된 KaggleDBQA 데이터셋에서 우수한 성능을 보여준다. 또한 KaggleDBQA의 다양한 LLMs와 데이터베이스에서 GP 대비 LTMP-DA-GP의 일관된 성능 향상을 보여주며, prompt 기반의 적응과 분해 방식의 효과와 모델에 구애받지 않는 이점을 강조한다.

###### Evaluating Neural Language Models as Cognitive Models of Language Acquisition (https://aclanthology.org/2023.genbench-1.4/)
- Anthology ID: 2023.genbench-1.4 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. "Neural language models (LMs)는 기술적인 작업에서의 성공을 통해 언어 습득과의 차이가 명확한데도 불구하고 언어 과제에서의 과학적인 이론으로의 잠재적인 관련성을 가져왔다."
    2. "문법적 능력 평가의 주요한 벤치마크가 LMs의 요구사항을 충분히 견뎌낼 수 없을 수 있다고 주장한다."
    3. "우리는 언어의 구조적 기반을 탐구하기 위해 경험적으로 연구된 데이터셋의 사용을 주장하며, 특히 LI-Adger 데이터셋에 대한 실험 결과를 언급한다."

###### Robust Code Summarization (https://aclanthology.org/2023.genbench-1.5/)
- Anthology ID: 2023.genbench-1.5 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 이 논문은 고급 transformer 기반 언어 모델을 사용하여 코드 summarization의 복잡성을 다룬다. 텍스트적 단서에 의존하는 것이 아닌 코드의 의미를 실제로 이해하는 지 알아보기 위해 함수와 변수 이름을 변경하여 코드 summarization의 효과를 검증한다.
    2. 우리는 Python, Javascript, Java 세 가지 프로그래밍 언어로 된 코드에서 dead code, commented code와 같은 adversary를 도입하여 모델의 이해력을 더욱 구체적으로 조사한다.
    3. 최종적으로, 우리의 연구는 transformer 기반 언어 모델의 내부 작동 방식에 대한 가치 있는 통찰을 제공하여 코드를 이해하는 능력을 향상시키고 효율적인 소프트웨어 개발 및 유지보수 워크플로에 기여하고자 한다.

###### Temporal Generalizability in Multimodal Misinformation Detection (https://aclanthology.org/2023.genbench-1.6/)
- Anthology ID: 2023.genbench-1.6 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 시간적 변화가 다중모달 모델에 대한 성능에 어떤 영향을 미치는지 조사한 실험 결과, 모델 성능은 시간에 따라 점차 하락하는 것으로 나타났다. 이 연구는 시간적 변화에 대비하지 않은 전통적인 평가 전략과 비교하여, 훈련 데이터에 나타나지 않는 시간 대의 데이터에서 모델을 평가하는 것이 매크로 F1에서 비선형적이고 7-8%의 성능 저하를 초래한다는 것을 확인하였다.
    2. 시간적 변화의 일반화를 어렵게 만드는 두 가지 요인인 내용 변화와 클래스 분포 변화에 대한 조사 결과, 내용 변화가 리콜에 더 큰 영향을 미침을 발견하였다.
    3. 허위정보 탐지에서의 분류 세부 정보를 고려한 실험결과, 특정 허위정보 클래스는 내용 변화에 대해 상대적으로 안정적인 것으로 나타났으며, 미래의 연구에서는 실제 성능을 잘 반영하기 위해 허위정보의 시간적 특성을 명확히 고려해야 한다는 결론을 얻었다.

###### Robust Generalization Strategies for Morpheme Glossing in an Endangered Language Documentation Context (https://aclanthology.org/2023.genbench-1.7/)
- Anthology ID: 2023.genbench-1.7 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 리소스 제한된 환경에서는 일반화가 특히 중요하다. 우리는 지식 분리 모델의 일반화 능력을 조사하고, 보지 않은 텍스트 장르에서의 성능을 평가하여 이를 메꾸는 전략을 실험한다.
    2. Weight decay 최적화, 출력 노이즈 제거 및 반복적인 가짜 레이블링을 사용하여 분포와 다른 데이터에서의 성능 차이를 줄일 수 있는 방법을 실험한다.
    3. Mayan 언어 Uspanteko로 작성된 문장을 사용하여 수행한 실험에서, 이러한 전략을 통해 보지 않은 장르의 텍스트에서 2% 성능 향상을 달성하였다.

###### Walking a Tightrope – Evaluating Large Language Models in High-Risk Domains (https://aclanthology.org/2023.genbench-1.8/)
- Anthology ID: 2023.genbench-1.8 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 고위험 도메인에서의 언어 모델의 정확성과 안전성은 중요한 문제이다. 대형 언어 모델 (LLMs)의 ChatGPT와 같은 모델들의 고위험 도메인 내에서의 성능은 여전히 불분명하다.
    2. 우리는 고위험 도메인에서의 instruction-tuned LLM의 성능을 분석하고, 사실적인 정확성과 안전 준수를 중점적으로 평가하는 실험을 진행하였다.
    3. 고위험 도메인에서의 LLM의 한계를 강조하며, LLM의 능력을 개선하는 것뿐만 아니라 도메인 특화된 지표의 완화와 안전성 및 사실적 신뢰성 강화를 위해 인간 중심 접근법을 채택하는 것이 중요하다는 결론을 도출하였다.

###### Latent Feature-based Data Splits to Improve Generalisation Evaluation: A Hate Speech Detection Case Study (https://aclanthology.org/2023.genbench-1.9/)
- Anthology ID: 2023.genbench-1.9 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 소셜 미디어의 증가로 인해 유해 콘텐츠의 확산이 늘고 견고한 혐오 발언 탐지 시스템의 필요성도 높아졌다. 
    2. 이 논문에서는 모델의 숨은 표현(clustering of models' hidden representations)을 기반으로 기존 데이터셋을 새롭게 분할하여 특정 키워드에 대한 과적합 문제를 돋보이게 하고 모델의 잠재 공간의 blind spot에서의 실패를 확인한다.
    3. 이 연구 결과는 한 모델에서 분할을 개발하고 다른 모델에서 평가할 때에도 일반화된다. 반면 성능 저하와 관련된 데이터 분할의 표면적 속성은 명확하지 않으며, 이는 과제의 난이도가 항상 사람이 해석 가능하지는 않음을 강조한다.

###### Syntax-Guided Transformers: Elevating Compositional Generalization and Grounding in Multimodal Environments (https://aclanthology.org/2023.genbench-1.10/)
- Anthology ID: 2023.genbench-1.10 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. "합성 일반화"는 지능 모델이 새로운 조합에 대한 이해를 완화하는 능력으로, 특히 다중 모달 환경에서의 AI 연구에서 매우 중요하고 어려운 요소이다.
    2. 이 연구에서는 언어의 문법 구조를 활용하여 합성 일반화를 강화한다. 특히, 텍스트 입력 구문 분석에서 파생된 어텐션 마스킹 기술을 통해 문법적 경험을 활용하는 것이 중요하다.
    3. 우리는 의존성 파싱(dependency parsing)을 사용하는 것의 장점과 Transformer 인코더에서 가중치 공유를 활용할 때 다양한 작업에서 합성 일반화를 향상시킬 수 있다는 것을 평가하고, 이를 통해 다중 모달 연결과 매개 변수 효율적 모델링을 위한 최신 기술을 제안한다.

###### mSCAN: A Dataset for Multilingual Compositional Generalisation Evaluation (https://aclanthology.org/2023.genbench-1.11/)
- Anthology ID: 2023.genbench-1.11 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 최근에 나타난 언어 모델들은 다양한 태스크에서 놀라운 결과를 보이지만, 합성 일반화 벤치마크에서 여전히 어려움을 겪는다.
    2. 이 논문에서는 이러한 벤치마크의 평가 결과가 다른 언어로 일반화될 수 있는지에 대한 질문을 제기한다.
    3. 이 질문에 대한 초기 단계로, 저자들은 SCAN 데이터셋의 다국어 버전인 mSCAN을 소개하고, 이를 통해 몇 가지 문맥 학습 실험과 GPT3.5 및 다국어 대형 언어 모델 BLOOM을 평가한다.

###### Inductive Bias Is in the Eye of the Beholder (https://aclanthology.org/2023.genbench-1.12/)
- Anthology ID: 2023.genbench-1.12 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1.유한한 증거로부터 인식된 시스템 일반화는 귀납적 편향의 존재에 결정적으로 의지한다. 이 연구는 Kharitonov and Chaabouni (2021)의 연구에서 영감을 받아, CNN, LSTMs (with and without attention), transformers와 같은 다양한 유형의 sequence-to-sequence 신경망 모델에서 귀납적 편향을 조사한다.
    2. 하지만 중요한 점은, 이 연구에서는 그들의 연구보다 더 넓은 범위의 가능한 귀납적 편향을 고려한다.
    3. hierarchical generalization과 counting strategy를 비교하기 위해, 우리는 transformers는 hierarchical generalization을 선호하지 않고 counting strategy를 선호한다는 Kharitonov and Chaabouni (2021)의 결과와 달리, hierarchical generalization을 선호하지 않음을 발견했다.또한 다양한 조합성에 대한 편향을 조사했고, Kharitonov and Chaabouni (2021)의 테스트셋에서 교란을 제어함으로써 일반적으로 더 일관성 없는 일반화를 발견하고, 고려된 두 가지 유형의 generalization 이외의 타입으로 응답이 많이 나왔다. 그럼에도 불구하고, 우리는 모든 유형의 모델에서 원시 데이터와 기능의 조합을 기반으로 한 검증 세트에서 일관된 구성적 일반화를 관찰했으나, 훈련 세트에서 원시 요소가 다른 함수와 함께 나타날 때에만 일어난다는 결과를 관찰했다. 이 성공의 패턴은 이러한 유형의 모델들의 일반화가 그들의 훈련 데이터의 분포적 특성에 극도로 민감하다는 것을 나타낸다.

###### Blackbird Language Matrices Tasks for Generalization (https://aclanthology.org/2023.genbench-1.13/)
- Anthology ID: 2023.genbench-1.13 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 인간과 유사한 언어 능력을 가진 시스템을 개발하기 위해서는 현재 시스템의 일반화 능력과 구성 능력을 이해해야 한다. 
    2. 우리는 시각 지능 테스트에서 영감을 받아 구성적이고 구조화된 데이터를 생성하여 이를 통해 문제 해결자들이 이미지 시퀀스에서 객체와 그들의 절대적 및 상대적 특성을 분리할 수 있는지 확인한다. 
    3. 우리는 프랑스어에서 주어-동사 일치와 영어에서 동사 교체를 모델링하는 두 가지 언어 현상에 대한 데이터셋을 제안하고, 이를 활용하여 LLM이 언어적 객체와 그들의 문법적 및 의미적 특성 등을 어떻게 인코딩하고 이를 조합하여 각 문제를 올바르게 해결하는지 조사할 수 있다.

###### In-Context Learning for Text Classification with Many Labels (https://aclanthology.org/2023.genbench-1.14/)
- Anthology ID: 2023.genbench-1.14 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 다중 선택 문제(MCQ) 생성의 자동화는 교육자가 학습 평가에 소비하는 시간을 줄일 수 있는 잠재력이 있으나, 기존 평가 메트릭은 교육적 가치를 고려하지 않고 단어 유사성만을 측정한다.
    2. 이 논문에서는 Knowledge Dependent Answerability (KDA)라는 새로운 자동 평가 메트릭을 제안하여 MCQ의 대답 가능성을 측정하고 대상 사실에 대한 학생의 지식을 평가한다.
    3. KDA_disc와 KDA_cont는 실제 강의환경에서의 사용성과 강한 상관관계를 가지며, n-gram 기반 유사성 메트릭과 결합하면 다양한 MCQ 품질 지표를 강하게 예측할 수 있다.
    
    1. 최근 NLP 과제에서 딥 모델은 초인적인 정확도를 보이지만, 특정 패턴에 의존하여 강건성이 제한된다. 
    2. 이 논문에서는 대조 학습과 반사상 augmentation을 활용하여 강건성을 향상시키고자 한다.
    3. "집합적 의사 결정 (collective decisions)"을 통해 여러 개의 반사상을 합성하여 인과관계를 강건하게 감독할 수 있으며, 이로 인해 카우스와 적절한 분포를 바탕으로 향상된 결과를 얻을 수 있다.
    
    1. 많은 라벨을 가진 과제를 위해 큰 언어 모델을 사용한 "인컨텍스트 학습 (ICL)"은 제한된 문맥 창으로 인해 도전적이다.
    2. 이 논문에서는 사전 훈련된 밀집 검색 모델을 사용하여 이 제한을 우회하고 각 추론 호출마다 전체 라벨 공간의 부분적인 정보만 모델에 제공한다.
    3. 기존 모델에 비해 더 나은 성능을 나타내며, 인컨텍스트 예제 갯수와 모델 크기에 따른 성능을 분석하고, in-context 예제의 유사성, 클래스 이름의 의미적 내용, 예제와 라벨 간의 올바른 대응을 분석하였다.

###### GQG: Generalized Quantifier Generalization - A Dataset for Evaluating Quantifier Semantics Understanding in Language Models (https://aclanthology.org/2023.genbench-1.15/)
- Anthology ID: 2023.genbench-1.15 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 본 논문은 언어 모델의 일반화 능력을 평가하기 위해 다양한 양화식들로 이루어진 새로운 데이터셋을 제안한다.
    2. 이 데이터셋은 다양한 양화식을 포함하고 있으며, 이 도메인에서 의미 이해를 평가하는 새로운 프레임워크를 형성한다.
    3. 제안된 데이터셋을 사용하여 4억1000만에서 69억까지의 Pythia 모델을 테스트한 결과, 현재의 언어 모델에게 양화식 기반 작업은 도전적임을 보여준다.

###### Cross-Lingual Data Augmentation For Thai Question-Answering (https://aclanthology.org/2023.genbench-1.16/)
- Anthology ID: 2023.genbench-1.16 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. 이 논문은 낮은 자원을 가진 언어 (특히 태국어)에서 Question Answering (QA) 모델의 견고성을 향상시키기 위해 설계된 데이터 품질 관리와 함께 혁신적인 데이터 확장 프레임워크를 제시한다.
    2. 훈련 데이터의 부족과 품질이라는 어려움을 인식하여, 우리는 단일 언어 및 교차 언어 환경에서 데이터 확장 기술을 활용한다.
    3. 우리의 접근 방식은 원래 데이터셋을 확장하고 향상시켜 언어적 다양성과 견고성을 높이며, 낮은 자원 언어 환경에서 훈련 데이터를 효과적으로 증가시키고 모델의 일반화를 향상시킬 수 있는 데이터 확장 방법의 잠재력을 실험적으로 입증한다. 이는 데이터 확장 분야에 대한 유망한 방향을 제시한다.

###### On using distribution-based compositionality assessment to evaluate compositional generalisation in machine translation (https://aclanthology.org/2023.genbench-1.17/)
- Anthology ID: 2023.genbench-1.17 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. NLP와 기계 학습에 적용된 Compositional generalisation(CG)은 대부분 인공 데이터셋을 사용하여 평가되었다. 이 논문에서는 실제 자연어 태스크에서 CG를 평가하기 위한 벤치마크를 개발하고자 한다. 
    2. DBCA(Distribution-based compositionality assessment) 프레임워크를 사용하여 Europarl 번역 코퍼스를 학습 데이터와 테스트 데이터로 분할하여 CG 능력이 필요한 테스트 세트를 만든다. 
    3. 이는 자연어 compositionality 벤치마크를 자동으로 생성하는 간단하고 비용 효율적인 방법으로, 다른 데이터셋과 언어에도 적용하기 쉽다.

###### Shifted PAUQ: Distribution shift in text-to-SQL (https://aclanthology.org/2023.genbench-1.18/)
- Anthology ID: 2023.genbench-1.18 
- Volume: Proceedings of the 1st GenBench Workshop on (Benchmarking) Generalisation in NLP 
- Summary: 
    1. Semantic parsing은 대규모 사용자-컴퓨터 상호작용의 접근성 향상에 중요한 역할을 한다. Spider 데이터셋과 그 개량버전인 PAUQ는 영어와 러시아어로 된 자연어 질문과 SQL 쿼리가 포함되어 있다. 이 논문에서는 제안된 스플릿을 사용하여 text2SQL 모델을 평가하고, 컴포지셔널리티와 다국어 일반화를 측정한다.
    2. 기존 Spider와 PAUQ 데이터셋은 독립적이고 동일한 분포를 가정한다. 이 논문에서는 타겟 길이 스플릿과 다국어 i.i.d 스플릿을 제안한다.
    3. 실험 결과와 컨텍스트-프리 문법을 통한 평가를 제시하고, 스플릿 데이터는 HuggingFace hub에서 공개되어 있다.

