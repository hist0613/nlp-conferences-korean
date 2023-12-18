# Korean Three-Line Summarizations of Papers 1387-1486 in Findings of the Association for Computational Linguistics: EMNLP 2023
###### LEXTREME: A Multi-Lingual and Multi-Task Benchmark for the Legal Domain (https://aclanthology.org/2023.findings-emnlp.200/)
- Anthology ID: 2023.findings-emnlp.200 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 transformer 아키텍처의 현저한 발전에 힘입어, 법적인 NLP 분야가 급속히 성장하고 있다. 이러한 발전을 측정하기 위해서는 정성적이고 도전적인 벤치마크가 필수적이다. 그러나 과거의 노력들은 주로 뉴스나 위키백과와 같은 일반적인 NLP 모델을 위한 벤치마크를 제작해왔는데, 법률 영역처럼 독특한 어휘와 복잡한 문장 구조가 있는 특정 도메인에는 적합하지 않을 수 있다.
    2. 우리는 법적인 NLP 문헌을 조사하고 24개 언어를 포함하는 11 개의 데이터셋을 선택하여 LEXTREME을 만들었다. 모델을 공정하게 비교하기 위해 데이터셋 통합 점수와 언어 통합 점수 두 개의 점수를 제안했다. 최상의 베이스라인도 수준 높은 결과를 달성하지 못하며, ChatGPT도 많은 과제에서 어려움을 겪는다는 결과를 보여준다.
    3. 연구원들과 실무자들이 쉽게 사용할 수 있도록, 우리는 LEXTREME을 huggingface에서 공개하고 모델을 평가하기 위한 필요한 코드와 함께 공개 리더보드를 제공한다. 또한 모든 실험 결과를 위한 public Weights and Biases 프로젝트도 제공한다.

###### Three Questions Concerning the Use of Large Language Models to Facilitate Mathematics Learning (https://aclanthology.org/2023.findings-emnlp.201/)
- Anthology ID: 2023.findings-emnlp.201 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)의 탁월한 언어 이해 및 생성 능력을 통해 교육 응용 분야에서 활용이 탐구되었지만, 수학 학습을 돕기 위한 LLM의 교육적 능력에 대한 연구는 거의 이루어지지 않았다.
    2. 이 포지션 논문에서는 적응형 피드백을 통해 학생의 수학 문제 해결 능력을 향상시키기 위해 LLM을 활용하는 과제와 관련된 도전 과제에 대해 논의한다.
    3. LLM은 잘못된 이유 구조를 생성할 수 있을 뿐만 아니라, 질문의 의미를 오해하고 학생의 답을 고치려고 할 때 주어진 질문의 이유를 이해하는데 어려움을 겪을 수 있다. 이를 고려하여 세 개의 연구 질문을 제시한다.

###### Simultaneous Machine Translation with Tailored Reference (https://aclanthology.org/2023.findings-emnlp.202/)
- Anthology ID: 2023.findings-emnlp.202 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Simultaneous machine translation (SiMT)은 전체 소스 문장을 읽으며 번역을 생성합니다. 그러나 기존의 SiMT 모델은 일정 지연 시간에서 사용 가능한 소스 정보의 다양성을 고려하지 않고 동일한 참조(reference)로 학습됩니다."
    2. "저희는 저희가 제안하는 새로운 방법을 통해 학습 시간에 따라 다른 참조(reference)를 제공하여 다양한 Latency에서 학습된 SiMT 모델에 맞춤형 참조를 제공하는 것을 제안합니다."
    3. "저희의 방법은 새로운 참조를 도입하고, tailor라는 reinforcement learning에 의해 유도된 참조를 통해 ground-truth를 수정하여 학습하는 것을 포함하고 있습니다. 실험 결과 무엇보다도 저희의 방법은 현재 SiMT 접근법의 다양한 문제에서 최고 수준의 성능을 달성합니다."

###### Dynamic Voting for Efficient Reasoning in Large Language Models (https://aclanthology.org/2023.findings-emnlp.203/)
- Anthology ID: 2023.findings-emnlp.203 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Self-consistency와 같은 다중 경로 투표 방법은 사실적인 오류와 시각적 생성에 의한 reasoning 오류를 완화하는데 사용되었지만, 각 문제에 대해 많은 reasoning 경로를 생성하기 때문에 많은 계산 자원이 필요합니다.
    2. 이 논문에서는 Dynamic Voting이라는 새로운 다중 경로 투표 기술을 제안하여, 대형 언어 모델이 확신을 가지고 풀 수 있는 문제에 대해 이른 퇴장 (early exiting)을 적용하여 이성적인 경로 수를 효과적으로 줄이고 정확성을 유지합니다.
    3. Dynamic Voting은 산술, 상식, 기호적 추론 작업에서의 실험적 평가 결과, 적은 양의 reasoning 경로를 사용하여 비슷한 정확성을 달성하는 것을 보여줍니다. 또한, 임계값 선택에서 강한 강건성을 보여주며, 다른 투표 기술, 다양한 모델, 다양한 프롬프트와 결합할 때 우수한 일반화 능력을 보입니다.

###### On Surgical Fine-tuning for Language Encoders (https://aclanthology.org/2023.findings-emnlp.204/)
- Anthology ID: 2023.findings-emnlp.204 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 방식으로 pre-trained 언어 인코더 모형을 새로운 태스크에 적용하는 경우, 전체 레이어를 fine-tuning 하는 것이 일반적이나, 우리는 일부 레이어만 fine-tuning 해도 비슷하거나 더 나은 성능을 얻을 수 있는 것을 보여준다.
    2. 바로 이를 위해, 우리는 고효율적인 메트릭로서 Fisher 정보 행렬의 대각 성분을 사용하여 selective fine-tuning을 위한 후보 레이어를 선택하는 방법을 제안한다.
    3. GLUE와 SuperGLUE의 실험 결과를 통해, 우리는 이 메트릭이 강력한 downstream 성능을 얻기 위한 레이어 선택에 유용하게 사용될 수 있음을 보여준다. 또한, FIM 점수의 강건성을 보여 줌으로써 최적화 과정 동안 일관되게 레이어를 순위 지정할 수 있다는 것을 확인한다.

###### AutoPlan: Automatic Planning of Interactive Decision-Making Tasks With Large Language Models (https://aclanthology.org/2023.findings-emnlp.205/)
- Anthology ID: 2023.findings-emnlp.205 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델은 매우 유망하며 구체화된 환경에서의 의사결정에 사용될 수 있다. 하지만, 이러한 모델들은 실제 환경에서의 규칙과 사전 훈련된 지식 사이의 오류로 인해 복잡한 의사결정 과제에서 종종 실패한다.
    2. 기존 방법들은 보통 비용이 많이 드는 기울기 계산이나 시간이 많이 걸리는 문맥 내 예시를 요구한다. 하지만, 이 논문에서는 AutoPlan이라는 방법을 제안하여 LLM 기반 에이전트가 상호작용적인 의사결정 과제를 수행하는 데 도움을 줄 수 있다.
    3. AutoPlan은 경험 수집과 반영을 통해 LLM 프롬프트에 작업 해결 계획을 추가하고 최적화한다. 실험 결과, AutoPlan은 인간이 작성한 예시를 사용하지 않음에도 불구하고 ALFWorld에서의 성공률은 베이스라인과 비슷하게 유지하며 HotpotQA에서는 8% 더 좋은 결과를 보였다.

###### Measuring Faithful and Plausible Visual Grounding in VQA (https://aclanthology.org/2023.findings-emnlp.206/)
- Anthology ID: 2023.findings-emnlp.206 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Visual Question Answering (VQA) 시스템에서 시각적 링크 (VG)에 대한 메트릭은 시스템이 주어진 질문에 대한 답을 추론할 때 관련 이미지 부분에 얼마나 의존하는지를 측정하는 것을 목표로 한다. VG의 부족은 최신 VQA 시스템에 공통적인 문제이며 그 결과로 무관한 이미지 부분에 과도하게 의존하거나 시각적 모달리티를 무시하는 경우가 발생할 수 있다."
    2. "우리는 시스템의 VG 특성을 양적으로 평가하지 않은 대부분의 시스템에서 VG 메트릭을 측정하여 이러한 결점을 보완하고 모델 평가 및 분석에 또 다른 가치 있는 차원을 추가하는 것이 도움이 될 것이라고 생각합니다."
    3. "우리는 질문과 관련된 객체를 식별하고 관련 객체에 포함된 정보를 사용하여 답을 생성하는지 여부를 캡처하는 새로운 VG 메트릭을 제안합니다. 이 메트릭은 "신뢰성 (faithful)"과 "합리성 (plausible)" 모두를 고려한 시각적 링크의 적합성을 쉽게 판단할 수 있으며, 대부분의 VQA 모델 설계에 대해 선명하게 설명하고 다양한 VQA 아키텍처에 대한 여러 참조 시스템을 평가합니다."

###### Improving Zero-shot Reader by Reducing Distractions from Irrelevant Documents in Open-Domain Question Answering (https://aclanthology.org/2023.findings-emnlp.207/)
- Anthology ID: 2023.findings-emnlp.207 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델 (LLM)은 오픈 도메인 질문 응답 (ODQA)에서 제로샷 접근 방식을 가능하게 했지만, 리트리버와 비교했을 때 리더는 제한적인 발전을 보여주고 있다.
    2. 이 연구는 계산 비용과 레이블이 달린 데이터의 필요성 등에 대응할 수 있는 제로샷 리더의 타당성을 조사한다.
    3. 우리는 LLM이 검색된 문서 중에서 관련 없는 문서로 인해 주의가 산만해지고, 제로샷 리더로 사용되었을 때 생성된 답변의 자신감 때문에 문제가 발생함을 발견했다. 이 문제를 해결하기 위해 부정에 기반한 지시와 적절한 답변 선택을 위한 점수 조정을 통해 이러한 문서의 영향을 완화시켰다. 실험 결과는 우리의 접근 방법이 다양한 시나리오에서 산만함을 처리하고 제로샷 리더의 성능을 향상시키는 것을 성공적으로 보여준다. 또한, 훈련 없이도 보편적인 전이 가능성을 보여주는 지도 리더에 비해 제로샷 리더는 보완적인 전이성을 보여주고 있다.

###### Can you Summarize my learnings? Towards Perspective-based Educational Dialogue Summarization (https://aclanthology.org/2023.findings-emnlp.208/)
- Anthology ID: 2023.findings-emnlp.208 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 가상 교사(VT)의 활용이 증가함에 따라 효율적이고 맞춤형으로 상호작용하는 AI 기반 학습 경험이 가능해졌다. 그러나 VT와 학생 간 대화를 요약하는 접근은 관점에 따라 다양화되어야 한다.
    2. 이 논문에서는 교사와 학생, 일반적 관점 세 가지로 교육 대화를 요약하는 Multi-modal Perspective based Dialogue Summarization (MM-PerSumm) 작업과 데이터셋 CIMA-Summ을 소개한다. 또한, IP-Summ 모델을 제안하여 이미지와 관점 기반 인코더를 활용하여 다양한 관점에서 대화를 요약한다.
    3. 마지막으로, IP-Summ 모델의 성능을 자세히 분석하여 최적의 모델링을 위한 측면을 강조한다.

###### Adaptive Textual Label Noise Learning based on Pre-trained Models (https://aclanthology.org/2023.findings-emnlp.209/)
- Anthology ID: 2023.findings-emnlp.209 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현실 세계에서의 레이블 오차는 예측할 수 없으며 다양한 종류의 오차의 혼합일 수 있다. 
    2. 이에 대응하기 위해 사전 훈련된 모델을 기반으로 한 적응적 텍스트 레이블 오차 학습 프레임워크를 개발하였다. 
    3. 여러 가지 일반화 전략을 통합하여, 잘못 레이블이 지정된 인스턴스들을 점진적으로 수정하여 노이즈를 잘 활용할 수 있도록 하는 방법을 제안한다.

###### Towards Informative Open-ended Text Generation with Dynamic Knowledge Triples (https://aclanthology.org/2023.findings-emnlp.210/)
- Anthology ID: 2023.findings-emnlp.210 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델은 텍스트 생성에서 놀랄만한 능력을 보여주지만, 생성된 텍스트가 주어진 프롬프트에 과도하게 집중되어 인간처럼 충분한 배경과 세부 정보를 제공하지 못하는 문제가 있다.
    2. 이 논문에서는 지식 그래프를 활용하여 모델이 더 맥락에 맞는 엔티티와 세부 사실을 생성하도록 하는 동적 지식 안내형 정보성 텍스트 생성 접근 방식을 제안한다.
    3. 실험 결과, 제안된 접근 방식이 기준 모델보다 더 정보성 있는 텍스트를 생성할 수 있다는 것을 보여주고 있다.

###### Novel Relation Detection: Discovering Unknown Relation Types via Multi-Strategy Self-Supervised Learning (https://aclanthology.org/2023.findings-emnlp.211/)
- Anthology ID: 2023.findings-emnlp.211 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 관계 추출 방법은 미리 정의된 관계 유형만 인식할 수 있어, 새로운 관계 유형이나 범위를 벗어난 유형들이 모델에 계속적으로 도전하는 현실 세계에서는 제한적이다.
    2. 본 논문에서는 이러한 도전적인 문제를 Novel Relation Detection (NRD)으로 정의하고, 알려진 관계의 학습 샘플을 기반으로 잠재적인 새로운 관계 유형을 발견하는 것을 목표로 한다.
    3. 실험 결과는 우리의 방법이 두 데이터셋에서 이전 최신 기법을 크게 능가하는 효과적인 NRD 방법임을 보여준다.

###### Ask Language Model to Clean Your Noisy Translation Data (https://aclanthology.org/2023.findings-emnlp.212/)
- Anthology ID: 2023.findings-emnlp.212 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 신경 기계 번역(NMT)에서 TTransformer 모델들은 높은 성능을 보여주고 있으나, 소음이 섞인 입력에 대한 취약성이 있어 실제 구현에서 깨끗한 출력을 생성하는 것은 중요한 도전 과제이다. 
    2. 우리는 MTNT 데이터셋의 대상 문장에서 노이즈를 제거하여 소음 평가에 더 적합한 벤치마크로 만들기 위해 힘들게 검토하였다. 
    3. 우리의 실험은 언어 모델의 기능을 활용하여 노이즈 제거에 그들의 놀라운 능력을 관찰하였으며, 이를 통해 NMT 모델의 견고성 평가에 효과적인 C-MTNT 데이터셋을 구축하였고, LLM이 이 작업에 효과적으로 수행된다는 결론을 도출하였다.

###### Multi-User MultiWOZ: Task-Oriented Dialogues among Multiple Users (https://aclanthology.org/2023.findings-emnlp.213/)
- Anthology ID: 2023.findings-emnlp.213 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화 시스템은 이제 더 많은 사용자들과 동시에 협력적으로 결정을 내리는 대화를 수행하는 것이 기대된다. 이를 위해, 저자들은 두 명의 사용자와 한 명의 에이전트 간의 대화를 포함하는 Multi-User MultiWOZ 데이터셋을 공개하였다.
    2. 이 데이터셋은 여러 사용자가 공동으로 작업을 진행하는 상황에서의 대화 동역학을 반영하고 있다.
    3. 이 데이터를 기반으로 저자들은 multi-user 대화에서 prediction된 쿼리를 사용하여 대화 상태 추적을 효과적으로 개선하는 방법을 제안하였다. 이 방법은 기존의 single-user 대화에 훈련된 대화 시스템을 수정하지 않고도 적용 가능하며, 새로운 도메인에도 일반화될 수 있다.

###### Extractive Summarization via ChatGPT for Faithful Summary Generation (https://aclanthology.org/2023.findings-emnlp.214/)
- Anthology ID: 2023.findings-emnlp.214 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 요약 추출은 긴 문서를 직접 문장을 추출하여 짧은 버전으로 요약하는 자연어 처리의 중요한 과제이다. 이 논문은 ChatGPT의 요약 추출 성능을 보다 폭넓은 benchmark 데이터셋에서 전통적인 fine-tuning 방법과 비교하여 평가하였다. 실험 결과, ChatGPT는 ROUGE 점수 측면에서 기존의 지도학습 시스템에 비해 성능이 떨어지는 반면, LLM 기반 평가 메트릭을 기반으로 한 높은 성능을 보였다고 밝혔다.
    2. 또한, in-context learning과 chain-of-thought reasoning의 효과를 조사하여 성능을 향상시키는 방법을 탐구하였다. 이에 따라, ChatGPT를 extract-then-generate 파이프라인에 적용하는 것은 요약의 충실성 측면에서 abstractive 기준에 비해 상당한 성능 향상을 이끌어 냈다.
    3. 이러한 관찰결과는 두 단계 접근법을 사용하여 ChatGPT의 신뢰성 있는 요약 능력을 향상시키는 잠재적인 방향을 제시하였다.

###### MAPO: Boosting Large Language Model Performance with Model-Adaptive Prompt Optimization (https://aclanthology.org/2023.findings-emnlp.215/)
- Anthology ID: 2023.findings-emnlp.215 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Prompt engineering"은 대규모 언어 모델 (LLM) 을 활용하는 효과적인 방법이지만, 기존 연구들은 특정 LLM보다는 특정 작업에 적합한 prompt의 중요성을 강조한다.
    2. 본 연구에서는 서로 다른 LLM에 대한 다른 prompt의 사용이 NLP의 다양한 하위 작업에서 능력을 강화하는데 중요하다는 사실을 정량적으로 보였다. 
    3. 제안된 MAPO (model-adaptive prompt optimizer) 방법은 각 특정 LLM의 하위 작업에 대해 원래의 prompt를 최적화하는데 효과적이며, 다양한 하위 작업에서 큰 향상을 이끌었다.

###### PsyCoT: Psychological Questionnaire as Powerful Chain-of-Thought for Personality Detection (https://aclanthology.org/2023.findings-emnlp.216/)
- Anthology ID: 2023.findings-emnlp.216 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 대형 언어 모델 (LLMs)의 발전은 ChatGPT와 같은 다양한 NLP 작업에서 놀라운 zero-shot 성능을 나타내었다. 그러나 글로 작성된 텍스트에서 개인의 성격을 식별하는 인식 작업에서의 LLM의 잠재력은 아직 충분히 탐구되지 않았다.
    2. 우리는 심리 질문지에서 영감을 받아 심리학자들에 의해 개별 성격 특성을 평가하기 위해 신중하게 설계된 질문 항목들을 체인 오브 스로트 (CoT, 사고의 연결) 프로세스의 집합으로 간주 할 수 있다고 주장한다.
    3. 이에 대응하여 우리는 PsyCoT라는 새로운 성격 인식 방법을 제안하며, 이는 다중 턴 형식의 대화 방식으로 심리 질문지를 완료하는 개인의 방법을 모방한다. 우리는 텍스트 분석을 전문으로 하는 AI 어시스턴트로서 LLM을 사용한다. 우리는 어시스턴트에게 각 턴마다 개별 항목을 평가하도록 하고, 평가 결과를 이용하여 결론적인 성격 선호도를 도출한다.

###### Harnessing the power of LLMs: Evaluating human-AI text co-creation through the lens of news headline generation (https://aclanthology.org/2023.findings-emnlp.217/)
- Anthology ID: 2023.findings-emnlp.217 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLM 기술을 활용하여 텍스트 작성에 인간이 어떻게 최상의 결과를 얻고, 이 모델과 상호작용하는 것이 글 작성 과정에 소유감과 신뢰감에 어떤 영향을 미치는지 알아보기 위해, LLM 보조 뉴스 제목 생성을 통해 일반적인 인간-인공지능 상호작용 방식을 비교해보았다.
    2. LLM 자체만으로도 만족스러운 뉴스 제목을 생성할 수 있지만, 잘못된 모델 출력을 수정하기 위해서는 평균적으로 인간의 개입이 필요했다.
    3. 인터랙션 방법 중에서도, 모델 출력을 안내하고 선택하는 것이 시간과 노력에 비해 가장 많은 이점을 제공했다. 또한, AI 협력은 자유롭게 편집하는 것과 비교하여 참가자들의 통제감에 해를 끼치지 않았다.

###### NERetrieve: Dataset for Next Generation Named Entity Recognition and Retrieval (https://aclanthology.org/2023.findings-emnlp.218/)
- Anthology ID: 2023.findings-emnlp.218 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트에서 entity를 인식하는 것은 정보 탐색 시나리오에서 중요한 필요로 여겨지며, Named Entity Recognition (NER)은 널리 채택된 NLP 태스크와 해당 기술의 가장 성공적인 예라고 볼 수 있다. 
    2. 큰 언어 모델의 최근 발전은 전용 모델로 처리되던 NER 작업에도 효과적인 솔루션을 제공하며, 전용 모델의 능력을 맞추거나 능가하는 경우도 많다. 그러나 NER은 여전히 해결된 문제로 보기에는 이르지 않다.
    3. 이 논문에서는 NER 작업의 세 가지 변형을 제시하고, 이를 지원하는 데이터셋을 제공한다. 더 세분화되고 서로교차하는 entity 유형으로 나아가는 것, entity 유형 레이블을 기반으로 미리 학습되지 않은 유형의 인식 및 추출을 하는 것, 검색 설정에서 인식 설정으로 전환하는 것이다. 이러한 모든 변형은 아직 해결되지 않은 문제들이다.

###### SWEET - Weakly Supervised Person Name Extraction for Fighting Human Trafficking (https://aclanthology.org/2023.findings-emnlp.219/)
- Anthology ID: 2023.findings-emnlp.219 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구에서는 SWEET(Supervise Weakly for Entity Extraction to fight Trafficking)이라는 엔터티 추출을 위한 약한 감독 파이프라인을 제안한다.
    2. SWEET은 노이즈가 있는 에스코트 광고에서 사람 이름을 추출하기 위해 규칙 일치와 대규모 언어 모델을 결합한 방법이다.
    3. SWEET은 라벨링 함수를 통해 다중 약한 라벨을 얻고 효과적으로 집계하여 이전의 감독형 성능 지표를 9% F1 점수로 능가하며 벤치마크 데이터에 더 잘 일반화된다.

###### Watermarking LLMs with Weight Quantization (https://aclanthology.org/2023.findings-emnlp.220/)
- Anthology ID: 2023.findings-emnlp.220 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델의 남용은 언어 모델을 빠르게 배포하면서 높은 위험을 드러내고 있다. 이 논문은 대화스러운 양자화 과정에서 워터마크를 추가하는 새로운 전산수법을 제안한다.
    2. 이 워터마크는 모델이 fp32 모드에서 사용될 때 동작하고, int8로 양자화될 때는 숨겨져 있는다. 이를 통해 사용자들은 모델을 그 자체로 추론할 수 있지만, 모델의 추가 지도학습 없이는 워터마크를 삭제할 수 없다.
    3. GPT-Neo와 LLaMA를 포함한 오픈소스 대규모 언어 모델에 워터마크를 성공적으로 심었다. 이 방법이 대규모 언어 모델 응용 분야에서 모델 가중치 보호를 위한 잠재적인 방향을 제공할 수 있기를 희망한다.

###### Disentangling Extraction and Reasoning in Multi-hop Spatial Reasoning (https://aclanthology.org/2023.findings-emnlp.221/)
- Anthology ID: 2023.findings-emnlp.221 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트를 통한 공간 추론은 직접적인 공간 정보를 추출하는 데에 그치는 것이 아니라 해당 정보에 대한 추론과 암묵적인 공간 관계를 유추하는 것도 필요하기 때문에 어려운 문제이다.
    2. 본 논문에서는 이러한 도전을 극복하기 위해 정보 추출과 추론을 분리(disentangle)하는 다양한 모델을 설계하고, 해당 모델들을 명시적으로 디자인하지 않은 최신기술(SOTA) 베이스라인과 비교한다.
    3. 실험 결과는 분리(disentangling)의 유효성을 일관되게 입증하여, 실제 데이터 도메인 내에서 모델의 일반화 능력을 향상시킬 수 있는지 보여주었다.

###### PsyAttention: Psychological Attention Model for Personality Detection (https://aclanthology.org/2023.findings-emnlp.222/)
- Anthology ID: 2023.findings-emnlp.222 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 개성 탐지 작업은 BigFive 및 MBTI와 같은 다양한 개성 모델의 심리학적 특징을 포함하려고 했다. 그러나 이러한 특징들을 결합해서 사용할 때, 서로 다른 계산 표준을 갖고 있는 기능들 사이의 간섭이 발생할 수 있어 노이즈를 도입하고 성능을 저하시킬 수 있다.
    2. 이 논문에서는 PsyAttention을 제안하여 다른 심리학적 모델을 개성 탐지에 적용하고, 이를 효과적으로 인코딩하여 특징의 수를 85% 줄일 수 있다.
    3. BigFive와 MBTI 모델에 대한 실험에서, PsyAttention은 각각 65.66%와 86.30%의 평균 정확도를 달성하여 최신 기법보다 우수한 성능을 보여주었다.

###### RoAST: Robustifying Language Models via Adversarial Perturbation with Selective Training (https://aclanthology.org/2023.findings-emnlp.223/)
- Anthology ID: 2023.findings-emnlp.223 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(LM)을 fine-tuning 하는 것은 많은 NLP 태스크에서 표준이 되었지만, 여전히 adversarial robustness와 모델 calibration과 같은 robustness 문제에 취약하다.
    2. 본 논문에서는 adversarial perturbation을 fine-tuning 도중에 도입하고, 불필요한 편차를 최소화하기 위해 모델 파라미터를 상대적 중요성에 따라 선택적으로 업데이트하여, LMs의 다양한 관점에서의 robustness를 향상시키는 간단하면서도 효과적인 fine-tuning 기술인 RoAST를 제안한다.
    3. RoAST는 모델 robustness에 대한 네 가지 대표적인 관점을 통합하여 fine-tuned LMs를 평가하고, 여섯 가지 다른 유형의 LMs에서 최신 fine-tuning 방법과 비교해서 그 효과성을 입증하였으며, 실제 응용에서의 유용성을 시사한다.

###### The Law and NLP: Bridging Disciplinary Disconnects (https://aclanthology.org/2023.findings-emnlp.224/)
- Anthology ID: 2023.findings-emnlp.224 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 법적 실무는 언어의 구조에 근본이 있지만 법적 실무자들과 학자들은 자연어 처리(NLP) 도구를 도입하는 데서 느림이 있다. 동시에, 법체계가 접근성에 따른 위기를 겪고 있는데, NLP를 통해 이 부분을 일부 완화할 수 있다. 이 논문에서는 법적 실무 중 NLP의 필요성과 NLP 연구자의 초점 사이의 괴리가 NLP의 천천히 채용되는 데 영향을 미친다고 주장한다. 
    2. 법적 실무에서 가장 인기 있는 NLP 태스크 중 일부는 법적 실무자의 요구사항을 충족시키지 못하는 것으로 나타났다. 
    3. 법률 NLP 연구의 최근 동향을 검토한 결과, 법률 NLP 커뮤니티와 법률 학계 간에는 제한적인 중첩이 있으며, 연구를 할 수 있는 여러 가지 법적 NLP 작업을 소개하여 이러한 괴리를 벌릴 수 있는 흥미로운 연구 분야를 강조하고 있다.

###### Symbolization, Prompt, and Classification: A Framework for Implicit Speaker Identification in Novels (https://aclanthology.org/2023.findings-emnlp.225/)
- Anthology ID: 2023.findings-emnlp.225 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 새로운 대화에서 발화자 식별은 다중 발화자 오디오북 생성 및 소설을 대본으로 변환하는 등 다양한 하위 작업에 적용될 수 있는데, 기존 최첨단 방법은 "Tom said, '...'"과 같은 명시적인 이야기 패턴에만 제한되어 있어서 장거리 맥락을 완전히 이해하고 복잡한 경우를 처리할 수 없다.
    2. 이를 위해 우리는 SPC라는 프레임워크를 제안하는데, 이는 상징화(symbolization), 프롬프트(prompt), 분류(classification)를 통해 장르에서 은암적인 발화자를 식별한다.
    3. 실험 결과, SPC는 웹 소설 모음에서 4.8% 정확도의 큰 향상을 보여 이전 방법들보다 발화자 식별 오류를 47% 줄일 수 있으며, 새로운 ChatGPT보다 뛰어나다. 또한 SPC는 장거리 맥락 의미 이해가 필요한 은암적 발화자 식별의 경우에 더 정확하다.

###### Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models (https://aclanthology.org/2023.findings-emnlp.226/)
- Anthology ID: 2023.findings-emnlp.226 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 고정된 prompt로는 open-domain 자연어를 처리하고 사용자의 특이한 절차에 적응하는 것이 어렵습니다. 이 논문에서는 HELPER라는 화면이 있는 에이전트를 소개합니다. HELPER는 대화의 문맥에 맞는 prompt 예제를 사용하여 뉴메모리 기반 언어 모델(Language Model)에 질의합니다.
    2. HELPER는 사용자의 언어와 행동 계획을 기록하여 향후 추론을 지원하고 사용자의 언어와 루틴에 맞춤화합니다. HELPER는 TEACh 벤치마크에서 Execution from Dialog History (EDH) 및 Trajectory from Dialogue (TfD)에서 새로운 최고 성능을 달성하였고 이전에 기록된 최고 기록에 비해 1.7배 성능 향상을 이끌어냈습니다.
    3. 개발된 모델, 코드 및 비디오 결과는 https://helper-agent-llm.github.io에서 확인할 수 있습니다.

###### ACT-SQL: In-Context Learning for Text-to-SQL with Automatically-Generated Chain-of-Thought (https://aclanthology.org/2023.findings-emnlp.227/)
- Anthology ID: 2023.findings-emnlp.227 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근에는 대형 언어 모델(LLM)이 다양한 도메인과 태스크에서 강력한 능력을 갖추었다. 이 연구에서는 텍스트-SQL 태스크에서 프롬프트 설계 문제를 연구하고, LLM의 추론 능력을 개선한다. 
    2. 우리는 스키마 링크와 비슷한 방법으로 연결된 상태습관 (chain-of-thought) 프롬프트를 설계하고, ACT-SQL이라는 방법을 제안하여 자동으로 상태습관을 생성한다. 이로써 수작업 레이블링이 필요하지 않아 비용 절감효과를 얻을 수 있다. 
    3. 실험 결과, 우리의 ACT-SQL 접근 방식은 LLM의 성능을 향상시키고, 기존의 상황인식 학습 접근 방식 중에서도 Spider dev 세트에서 최고 성능을 달성하였다.

###### Manifold-Preserving Transformers are Effective for Short-Long Range Encoding (https://aclanthology.org/2023.findings-emnlp.228/)
- Anthology ID: 2023.findings-emnlp.228 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다양한 학습 작업에서 Multi-head self-attention 기반 Transformer 모델은 매우 유망하게 나타났으나, 이 모델들은 계층별 문맥 정보를 보존하지 못한다. TransJect는 이 문제를 해결하기 위해 layer 간 토큰 간 거리 보존의 이론적 한계를 보장하면서 토큰 표현을 다른 manifold로 변환하여 Euclidean 거리를 보존한다.
    2. 다양한 벤치마크 짧은 및 긴 시퀀스 분류 작업에서 TransJect는 Transformers의 변형들보다 각각 최대 6.8%와 5.9%의 성능 향상을 보여준다. 또한 TransJect는 언어 모델링 작업에서 Transformer보다 79% 우수한 성능을 보인다.
    3. TransJect는 다양한 attention head들이 무작위하고 비정렬적으로 학습하는 문제를 해결하기 위해 전문가들의 조합을 이용하여 규제할 수 있으며, 이러한 전문가들은 입력 시퀀스로부터 다른 희소 표현을 학습한다. TransJect는 엔트로피가 매우 낮고 깊이를 더욱 효율적으로 확장할 수 있다.

###### ASPIRO: Any-shot Structured Parsing-error-Induced ReprOmpting for Consistent Data-to-Text Generation (https://aclanthology.org/2023.findings-emnlp.229/)
- Anthology ID: 2023.findings-emnlp.229 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ASPIRO는 구조화된 데이터를 zero to few-shot 환경에서 짧은 템플릿 문장으로 변환하는 기법을 제안한다. 이전 방법과 다르게, ASPIRO는 큰 언어 모델에게 엔티티에 대해 고려하지 않는 템플릿을 직접 생성하도록 유도한다.
    2. ASPIRO는 알고리즘적 파싱 체크와 LLM 재프롬프팅을 활용하여 실시간으로 템플릿 생성 문제를 해결하는 방법을 제시한다.
    3. ASPIRO는 DART 데이터셋에서 RDF 트리플의 문장화 과정에서 파싱 오류를 평균 66% 줄이며, Rel2Text 데이터셋에서 BLEU 50.62, METEOR 45.16, BLEURT 0.82, NUBIA 0.87, PARENT 0.8962의 성능을 보이며 최신 사전 훈련 언어 모델과 경쟁한다.

###### Detecting Syntactic Change with Pre-trained Transformer Models (https://aclanthology.org/2023.findings-emnlp.230/)
- Anthology ID: 2023.findings-emnlp.230 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 연구에서는 Transformer 기반 언어 모델이 19세기 초과 20세기 후반의 영어 사이의 구문적 차이를 찾을 수 있는 능력을 조사한다. 이를 위해 BERT 모델을 fine-tuning하여 문맥 정보를 가린 뒤, 구문 정보만을 사용하여 이 두 시기의 텍스트를 구분할 수 있다는 것을 보여준다. 
    2. 또한, fine-tuned BERT 모델을 사용하여 구체적인 구문 변화 및 새로운 품사가 도입된 단어를 식별하는 방법을 제안한다. 이를 위해 자동적인 품사 태거와 BERT의 사전학습된 표현을 활용하여 특정 말뭉치에 대한 품사 태거를 학습시킨다. 
    3. 최종적으로, 이 방법을 사용하여 구문적 변화의 역사적인 발전인 진행형 문법의 등장을 확인하는데 사용한다.

###### A Word Sense Distribution-based approach for Semantic Change Prediction (https://aclanthology.org/2023.findings-emnlp.231/)
- Anthology ID: 2023.findings-emnlp.231 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 단어의 의미 변화를 예측하는 것은 시간에 민감한 NLP 애플리케이션에서 중요한 작업이다. 각 맥락에 따라 모호한 단어들의 의미를 구분하는 WSD 방법과 의미 변화 감지 사이에 관계가 있는데, 우리는 두 개의 시간 단위로 수집된 코퍼스에서 대상 단어의 의미가 변화했는지를 예측할 수 있는지 조사한다.
    2. 사전 훈련된 정적 sense embedding을 사용하여 대상 단어의 각 인스턴스에 sense id를 자동으로 부여한다.
    3. 다른 발산 또는 거리 측정 기법을 사용하여 주어진 두 코퍼스 간 대상 단어의 의미 변화를 양적으로 측정한다. 실험 결과, 단어의 의미 변화를 정확하게 예측하는 데에 단어 sense 분포를 사용할 수 있다는 것을 확인하였다.

###### Gold: A Global and Local-aware Denoising Framework for Commonsense Knowledge Graph Noise Detection (https://aclanthology.org/2023.findings-emnlp.232/)
- Anthology ID: 2023.findings-emnlp.232 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 일반 상식 그래프(Commonsense Knowledge Graphs)를 사람의 주석을 통해 구축하는 것은 비용이 많이 들 수 있다. 그 결과, 더 많은 의미적인 범위를 가진 CSKG를 구축하기 위해 여러 자동 방법이 제안되고 있다.
    2. 이 논문에서는 CSKG의 노이즈를 감지하기 위해 Entity Semantic Information, Global Rules, Local Structural Information을 활용하는 Noise detection framework인 Gold를 제안한다.
    3. 실험 결과, Gold는 합성된 노이즈가 있는 CSKG 벤치마크에서 모든 기준 성능을 능가하며, CSKG의 노이즈를 제거하는 것이 Zero-shot commonsense question answering task에도 효과적임을 보여준다.

###### Improving Conversational Recommendation Systems via Bias Analysis and Language-Model-Enhanced Data Augmentation (https://aclanthology.org/2023.findings-emnlp.233/)
- Anthology ID: 2023.findings-emnlp.233 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대화형 추천 시스템은 언어 모델링 기술의 발전에 따라 주목을 받으면서 빠르게 성장하는 연구 분야이다. 그러나 현재의 대화형 추천은 상대적으로 새로운 분야이며 제한된 기여로 인해 여러 가지 도전에 직면하고 있다. 
    2. 본 연구에서는 CRS 모델 개발을 위한 벤치마크 데이터셋을 탐구하고, 다중 턴 상호작용에서 나타나는 피드백 루프로 인해 발생하는 선택 편향과 다양한 인기 편향 변형 등의 잠재적인 편향 문제를 다룬다. 
    3. 언어 모델과 데이터 확장 기법을 사용하는 데이터 증강 접근 방식을 제안하고, ReDial 및 TG-ReDial 벤치마크 데이터셋에서의 실험을 통해 CRS 기술의 성능을 향상시키고 새롭게 정의된 다양한 편향 문제를 해결하는 데 도움이 되는 결과를 제시한다.

###### Exploring Graph Pre-training for Aspect-based Sentiment Analysis (https://aclanthology.org/2023.findings-emnlp.234/)
- Anthology ID: 2023.findings-emnlp.234 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존 연구들은 감성 요소를 생성적으로 추출하여 복잡한 모델링을 피하기 위해 해왔는데, 이러한 방식은 감성 요소간의 관계를 고려하지 않아서 중요한 문제를 놓치고 있다. 
    2. 따라서, 이 논문에서는 그래프 기반 pre-training을 활용하여 감성 요소 간의 관계를 더 잘 파악할 수 있는 모델을 개발하였다.
    3. 실험 결과는 우리의 방법이 뛰어나며, 우리의 동기에 대한 올바른 이해를 검증한다.

###### DemaFormer: Damped Exponential Moving Average Transformer with Energy-Based Modeling for Temporal Language Grounding (https://aclanthology.org/2023.findings-emnlp.235/)
- Anthology ID: 2023.findings-emnlp.235 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 시간 언어 지원은 비디오 순간을 자연어 질의와 의미적으로 대응시키는 것을 목표로 한다. 최근 연구들은 어텐션 메커니즘을 사용하여 비디오 순간과 텍스트 질의 사이의 관계를 학습한다. 그러나 단순한 어텐션은 이러한 관계를 적절하게 파악하지 못하여 목표 비디오 순간을 다른 순간들과 구분하기 어려운 분포를 생성할 수 있다.
    2. 이 문제를 해결하기 위해, 우리는 에너지 기반 모델 프레임워크를 제안하여 순간-질의 분포를 명시적으로 학습한다.
    3. 또한, 우리는 exponential moving average와 학습 가능한 감쇠 인자를 사용하는 새로운 Transformer 기반 아키텍처인 DemaFormer를 제안하여 순간-질의 입력을 효과적으로 인코딩한다. 4개의 공개 데이터셋에서 수행한 포괄적 실험을 통해 우리의 방법이 최신 기준선에 비해 우수함을 보였다.

###### Test-time Augmentation for Factual Probing (https://aclanthology.org/2023.findings-emnlp.236/)
- Anthology ID: 2023.findings-emnlp.236 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사실적 파악은 언어 모델이 특정 세계 지식 사실을 "알고 있는지" 테스트하는 방법으로, prompt의 작은 변경이 모델 출력에 큰 변화를 일으키는 문제가 있다. 
    2. 기존 연구는 텍스트 마이닝이나 세밀한 조정을 통해 이 문제를 완화시키려고 했으나, 이런 접근 방식은 관련성에 특화되어 있고 본연의 종족을 보이지 않아 새로운 관계 유형에는 일반화하지 못한다. 
    3. 본 논문은 시험 시간 증강 (TTA)을 사용하여 prompt 변동에 대한 민감도를 줄이는 관계 비의 방법으로 제안한다. 실험 결과, TTA를 사용하면 모델 신뢰도가 예측 정확성을 더 잘 반영하는 개선이 보여진다. 몇몇 모델에서는 예측 정확도가 향상되지만, 다른 모델에서는 TTA가 저하를 일으킨다. TTA에 대한 해석 분석은 높은 품질의 prompt 변이 생성의 어려움을 주요 도전 요소로 확인했다.

###### Methodological Insights in Detecting Subtle Semantic Shifts with Contextualized and Static Language Models (https://aclanthology.org/2023.findings-emnlp.237/)
- Anthology ID: 2023.findings-emnlp.237 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 네덜란드어와 영어의 다른 정치적 신념을 가진 사회 공동체 사이의 미묘한 의미 변화를 자동으로 탐지하는 연구를 수행한다.
    2. 우리는 정적 모델과 문맥화된 언어 모델을 사용하는 방법을 비교하는 방법론적 연구를 수행한다. 
    3. 우리의 결과는 정적 모델을 사용하는 방법과 우리의 마스크 토큰 예측 방법은 정치적으로 부담스러운 용어의 함의 차이를 감지할 수 있으며, 문맥화된 표현의 거리를 측정하는 방법은 심지어 극단적인 변화의 합성 시나리오에서도 명확한 신호를 제공하지 않는다는 것을 보여준다.

###### Disfluent Cues for Enhanced Speech Understanding in Large Language Models (https://aclanthology.org/2023.findings-emnlp.238/)
- Anthology ID: 2023.findings-emnlp.238 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연스러운 대화에서 입다듬지 않는(disfluent) 내용을 제거하는 것이 보통의 방법이지만, 이 논문에서는 이러한 disfluencies가 단순한 노이즈 이상의 정보적인 표식 역할을 할 수 있다고 가정한다.
    2. 이 연구에서는 다양한 유형의 대화 수정 (speech repairs)이 포함된 disfluent 질의를 포함하여 읽기 이해 작업에 대해 사전 학습된 모델을 사용한다.
    3. 연구 결과, 특정 disfluencies는 모델 성능을 향상시킬 수 있는데, 특히 문맥 기반의 조절으로 인한 disfluencies가 그렇다는 것을 보여준다. 그러나 대규모 언어 모델은 의사 결정을 포함한 수정이나 어휘 또는 구문 오류의 수정에 어려움이 있어 발전 가능성이 있는 중요한 영역이라고 제안한다.

###### Watermarking PLMs on Classification Tasks by Combining Contrastive Learning with Weight Perturbation (https://aclanthology.org/2023.findings-emnlp.239/)
- Anthology ID: 2023.findings-emnlp.239 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "대규모 사전 훈련 언어 모델(PLM)은 비용이 많이 드는 훈련으로 인해 저작권보호에 대한 중요성이 있는 가치 있는 지적 재산이 되었다. 이에따라, 지적 재산을 보호하기 위해 개발된 PLM 워터마킹 방법이 중요하지만 미개발된 기술이다." 
    2. "이 연구에서는 특정 입력에 의해 트리거 될 수 있는 백도어를 포함하여 PLM 워터마킹의 실현 가능성을 조사한다. 워터마킹 단계에서 대조 학습을 사용하여 특정 입력의 표현을 다른 입력에서 분리하고, 후속 학습 후에 특정 레이블과 연결시킬 수 있게 한다." 
    3. "다양한 데이터셋에서 수행된 광범위한 실험 결과 워터마크를 다운스트림 작업에 대한 어떠한 지식 없이도 견고하게 추출할 수 있으며, 성공률이 높다는 것을 보여준다."

###### BanLemma: A Word Formation Dependent Rule and Dictionary Based Bangla Lemmatizer (https://aclanthology.org/2023.findings-emnlp.240/)
- Anthology ID: 2023.findings-emnlp.240 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 레마타이제이션은 자연어처리와 언어학에서 중요하며, 데이터 밀도를 줄이고 문맥적 의미를 이해하는 데 도움이 된다. 그러나 방글라 텍스트의 인플렉션과 형태론적인 풍부함으로 인해 레마타이제이션은 복잡한 도전 과제가 된다.
    2. 우리는 방글라에 대한 레마타이저를 설계하기 위해 언어학적 규칙을 제안하고 규칙과 사전을 이용한다. 이 시스템은 주어진 문장 내에서 단어의 품사 클래스에 기반하여 단어를 레마타이즈하는 것을 목표로 한다. 
    3. 우리의 룰은 인플렉션된 단어의 단어 형성을 관찰하기 위해 다양한 도메인, 원본 및 시간대의 방글라 텍스트 크러포스를 분석한다. 이를 통해 우리의 레마타이저는 훈련된 언어학자들이 수작업으로 주석을 단 테스트 데이터셋에서 96.36%의 정확도를 달성하고 이전에 발표된 세 개의 방글라 레마타이제이션 데이터셋에서 경쟁력 있는 성능을 보여준다.

###### Exploring the Sensitivity of LLMs’ Decision-Making Capabilities: Insights from Prompt Variations and Hyperparameters (https://aclanthology.org/2023.findings-emnlp.241/)
- Anthology ID: 2023.findings-emnlp.241 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. LLM의 의사결정 능력은 하이퍼파라미터와 prompt의 변화에 민감하다는 점을 고려하지 않은 이전 연구들이 있다. 
    2. 이 논문에서는 세 가지 다른 성능을 갖는 OpenAI 언어 모델을 사용하여 prompt와 온도 설정에 따른 LLM의 의사결정 능력 변동을 분석하였다. 
    3. 단순한 prompt 조정에 따라 언어 모델은 사람과 유사한 탐사와 활용의 균형을 나타낸다는 점을 발견하였다.

###### Search Augmented Instruction Learning (https://aclanthology.org/2023.findings-emnlp.242/)
- Anthology ID: 2023.findings-emnlp.242 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델들은 instruction fine-tuning을 통해 크게 발전해왔으나, 여전히 투명성과 최신 지식과 정보 활용 능력이 부족하다. 
    2. 본 논문에서는 in-house와 외부 검색 엔진들이 생성한 복잡한 검색 결과에 기반하여 언어 생성과 지시 따르기 능력을 더 높이는 search-augmented instruction learning (SAIL)을 제안한다. 
    3. 실험 결과, fine-tuned SAIL-7B 모델은 강력한 지시 따르기 능력을 가지며, 개방형 질문 답변과 사실 확인처럼 투명성이 중요한 작업에서 유의미한 개선을 보인다.

###### “Kelly is a Warm Person, Joseph is a Role Model”: Gender Biases in LLM-Generated Reference Letters (https://aclanthology.org/2023.findings-emnlp.243/)
- Anthology ID: 2023.findings-emnlp.243 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근의 대형 언어 모델은 권장서와 같은 전문 문서를 작성하는 데 도움이되는 효과적인 도구로 등장했습니다. 그러나 이 응용 프로그램은 편의성을 제공하는 한편 이전에 없던 공정성 문제를 도입합니다. 모델 생성된 추천서에 잠재된 편견이 있다면, 정성적인 검토 없이 사용하면 여성 지원자의 합격률을 감소시키는 등 사회적인 문제를 초래할 수 있습니다.
    2. 우리는 이 긴급한 문제를 감안하여 실세계 사용 사례에서의 공정성 문제와 관련된 피해를 포괄적으로 연구하는 것이 절실하고 필요하다고 생각합니다.
    3. 이 논문에서는 LLM이 생성한 추천서에서 성별 편견을 비판적으로 조사합니다. 우리는 사회과학 연구 결과로부터 영감을 받아 언어 스타일의 편견과 어휘 내용의 편견 이라는 2가지 차원을 통해 편견을 명백히 보이는 평가 방법을 설계합니다. 또한, 편식 편견(hallucination bias)을 분석하여 편견의 전파 정도를 조사하고, ChatGPT와 Alpaca라는 두 가지 인기 있는 LLM에서 평가를 수행하여 LLM이 생성한 추천서에서 심각한 성별 편견을 발견합니다. 이 연구 결과는 검토 없이 LLM을 이용하는 것에 대한 경고뿐만 아니라 LLM이 생성한 전문 문서에서의 숨겨진 편견과 피해를 철저히 연구하는 중요성을 명확히 합니다.

###### TextMixer: Mixing Multiple Inputs for Privacy-Preserving Inference (https://aclanthology.org/2023.findings-emnlp.244/)
- Anthology ID: 2023.findings-emnlp.244 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(PLM)은 클라우드 서비스로 배포되어 사용자가 텍스트 데이터를 업로드하고 원격으로 추론을 수행할 수 있게 한다. 그러나 사용자의 개인 텍스트는 민감한 정보를 포함하고 있으며, 이를 서비스 제공자와 직접 공유하면 심각한 개인정보 유출에 이어질 수 있다. 본 연구에서는 추론 단계에서 평문 유출을 방지하는 혁신적인 개인 정보 보호 추론 프레임워크인 MixPi를 소개한다.
    2. MixPi는 사용자의 개인 입력을 여러 다른 입력과 혼합하여 의미적 연결을 혼란시켜 잠재적인 개인 정보 공격자를 방지하는 것을 목표로 한다. 이를 위해 우리의 접근 방식은 (1) 혼합, 표현 및 위치와 같은 세 가지 다른 차원에서 입력을 암호화하는 혁신적인 암호화 모듈인 Privacy Mixer를 제안한다. (2) 혼합된 표현을 처리하고 여러 예측을 얻기 위해 사전 훈련된 다중 입력 다중 출력 네트워크를 채택한다. (3) 사용자만이 여러 예측 중에서 실제 출력을 해독할 수 있도록 Privacy Demixer를 사용한다.
    3. 또한, 혼합에 필요한 합성 입력을 자동으로 생성하는 다양한 방법을 탐색한다. 토큰 및 문장 분류 작업에 대한 실험 결과는 MixPi가 성능과 개인 정보 보호 측면에서 기존의 비공개 방법을 크게 능가한다는 것을 보여준다.

###### FinePrompt: Unveiling the Role of Finetuned Inductive Bias on Compositional Reasoning in GPT-4 (https://aclanthology.org/2023.findings-emnlp.245/)
- Anthology ID: 2023.findings-emnlp.245 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 처리에서 텍스트 간의 구성적 추론은 오랫동안 과제였는데, GPT-4와 같은 큰 언어 모델이 등장하면서 chain-of-thought (CoT)와 같은 프롬프팅 기법이 제안되었다. 그러나 이러한 프롬프팅은 발견하고 검증하는 데 상당한 인력이 필요하다.
    2. 우리의 연구는 GPT-4의 구성적 추론 능력을 향상시키는 방법으로 사후조정된 모델로부터 작업별 귀납적 편향을 프롬프트로 전달하는 것을 제안한다.
    3. 다중 점프 질문 응답과 텍스트에서의 수치 추론에 대한 실험 결과, 우리의 프롬프트 방식은 복잡한 추론 작업에 대해 기존의 프롬프트와 경쟁력 있는 제로샷 및 퓨샷 성능을 보여주며, 이전 패러다임의 검증된 편향을 채택하는 것의 중요성을 강조한다.

###### Teacher Perception of Automatically Extracted Grammar Concepts for L2 Language Learning (https://aclanthology.org/2023.findings-emnlp.246/)
- Anthology ID: 2023.findings-emnlp.246 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 언어 교육에서의 한 도전은 구문, 의미, 또는 음운론에 관한 규칙을 의미 있는 방식으로 조직하는 것이다. 이 논문에서는 교육자가 규칙을 생성하는 데 도움을 주기 위해 문법 설명을 자동으로 추출하고 시각화하는 방법을 제안한다.
    2. 인도의 칸나다어와 마라티어라는 두 개의 언어를 가르치기 위해 이 방법을 적용하고, 영어와 달리 잘 개발된 학습 자료가 없는 이 언어들에 대한 매우 의미 있는 자료를 자동으로 추출할 수 있다는 것을 보여준다.
    3. 북미의 언어 교육자들에게 수동 평가를 받아서 추출된 자료의 유용성을 평가한 결과, 이 자료는 수업 준비와 학습자 평가에 사용될 수 있는 잠재력을 가지고 있다고 평가받았다.

###### Allies: Prompting Large Language Model with Beam Search (https://aclanthology.org/2023.findings-emnlp.247/)
- Anthology ID: 2023.findings-emnlp.247 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(LLM)의 발전으로 인해, LLM 응용 분야의 연구는 점점 인기를 끌고, LLM API 호출을 쌓아 복잡한 작업을 수행하는 파이프라인을 구축하는 아이디어가 실현되었다.
    2. 그러나 이러한 방법은 정보 범위가 제한되고 잘못 대처하는 한계가 있다. 본 논문에서는 ALLIES라는 참신한 방법을 제안한다. 
    3. ALLIES는 입력 쿼리를 기반으로 LLM을 사용하여 원본 쿼리와 관련된 새로운 쿼리를 반복적으로 생성하여 반복적인 추론 과정을 가능하게 한다.
    
    ***code: https://github.com/microsoft/SimXNS/tree/main/ALLIES***

###### Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning (https://aclanthology.org/2023.findings-emnlp.248/)
- Anthology ID: 2023.findings-emnlp.248 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 인간과 유사한 추론 능력을 보이지만 복잡한 논리적 문제에 여전히 어려움을 겪습니다. 이 논문에서는 LLM과 심볼릭 풀러 (symbolic solver)를 통합하는 새로운 Logic-LM 프레임워크를 소개합니다. 
    2. 우리의 방법은 먼저 LLM을 사용하여 자연어 문제를 심볼릭한 수식으로 변환합니다. 그런 다음 심볼릭 풀러가 변환된 문제에 대한 추론을 수행합니다. 
    3. 우리는 논리 지식을 활용하는 Logic-LM이 LLM만 사용하는 것보다 평균적으로 39.2%의 성능 향상을 보이며,  chain-of-thought prompting을 사용하는 LLM보다도 18.4%의 성능 향상을 보인다는 실험 결과를 보여줍니다.

###### SiMFy: A Simple Yet Effective Approach for Temporal Knowledge Graph Reasoning (https://aclanthology.org/2023.findings-emnlp.249/)
- Anthology ID: 2023.findings-emnlp.249 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 Temporal Knowledge Graph (TKG) reasoning 작업은 그래프 신경망과 순환 신경망을 사용하여 지식 그래프의 구조적 정보와 시간적 정보를 모델링하였으나, 훈련 효율성이 낮고 일반화 능력이 부족한 문제가 있다.
    2. 이 논문은 이러한 복잡한 모델 구조의 필요성을 고찰하고, multilayer perceptron (MLP)과 고정 빈도 전략을 사용하여 간단하고 효과적인 접근법인 SiMFy를 제안한다.
    3. 실험 결과에서 SiMFy는 빠른 수렴 속도와 더 좋은 일반화 능력, 훈련 과정에서의 시간 소비 감소, 그리고 KG의 구조적 의존성을 더 잘 포착하는 능력을 보여주었다. 이러한 결과는 복잡한 모델을 간단한 대칭 모델로 대체하는 것도 실현 가능한 전략임을 보여준다.

###### Understanding Translationese in Cross-Lingual Summarization (https://aclanthology.org/2023.findings-emnlp.250/)
- Anthology ID: 2023.findings-emnlp.250 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Cross-lingual 요약에서 번역어가 학습 및 성능에 영향을 끼친다는 것을 확인하고, 기존 데이터셋 구축 방법에 따라 번역어 정도가 다르게 나타남을 밝혀냈다.
    2. 번역어가 테스트 세트의 문서나 요약에 영향을 미쳐 인간의 판단과 자동 평가 간의 차이를 야기할 수 있음을 발견했다.
    3. 트레이닝 세트에 번역어가 포함되면 실제 응용 프로그램에서 모델 성능에 해로울 수 있음을 확인했으며, 특정한 학습 전략 아래에서 저자원 언어에 대한 CLS 시스템 구축에 매우 유용한 기계 번역 문서임을 밝혔다.

###### The Truth, The Whole Truth, and Nothing but the Truth: A New Benchmark Dataset for Hebrew Text Credibility Assessment (https://aclanthology.org/2023.findings-emnlp.251/)
- Anthology ID: 2023.findings-emnlp.251 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정보 과잉의 시대에서는 사실과 허구를 구별하는 것이 이전보다 더 중요하다. 이 논문에서는 이스라엘 공공 인물과 정치인들의 발언의 신뢰성을 평가하기 위한 새로운 공개 데이터셋 HeTrue를 소개한다.
    2. 우리는 이 데이터셋을 활용하여 텍스트만을 기반으로 발언의 신뢰성을 예측할 수 있는지 검증한 결과, 발언 텍스트만 사용하는 방법과 메타데이터, 맥락, 증거와 같은 추가 데이터를 사용하는 방법을 비교하였다.
    3. 실험 결과, 발언과 맥락을 통합하는 모델이 단순히 발언 텍스트만을 기반으로 하는 모델보다 성능이 향상되었으며, 증거도 통합한 최고 모델은 48.3의 F1 Score를 달성하여 HeTrue가 어려운 벤치마크임을 보여주었다.

###### IndiSocialFT: Multilingual Word Representation for Indian languages in code-mixed environment (https://aclanthology.org/2023.findings-emnlp.252/)
- Anthology ID: 2023.findings-emnlp.252 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인도어 사용자들의 수가 증가함에 따라, 인도어 기술을 개발하는 것이 필요하다고 한다.
    2. 이 논문은 원어, 음역, 다국어, 코드 혼용 및 소셜 미디어 관련 특성을 포함한 다양한 텍스트 특징에 대한 일반화된 표현 벡터를 제안한다.
    3. 제안된 임베딩은 대부분의 경우와 언어에서 기준선을 뛰어넘어 다양한 NLP 응용에 적합함을 보여주었다.

###### Adaptive Hinge Balance Loss for Document-Level Relation Extraction (https://aclanthology.org/2023.findings-emnlp.253/)
- Anthology ID: 2023.findings-emnlp.253 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 다중 문장에서 개체 간 관계를 예측하는 문서 수준 관계 추출은 개체 쌍 간의 관계 여부를 결정하기 위해 multi-label 분류 임계값을 선택하는 것이 일반적이다. 하지만 문서 수준 작업에서는 대부분의 개체 쌍이 어떤 관계도 표현하지 않아 양성 및 음성 클래스 간에 매우 불균형한 분포가 발생한다.
    2. 본 논문에서는 관계의 예측 점수와 분류 임계값 간의 거리를 활용하여 쉬운 음성 데이터를 가중치를 줄이는 방법을 제안한다. 즉, 소수의 양성 관계인 어려운/잘못된 분류 관계에 더욱 집중하여 그들의 난이도를 측정하는 새로운 Adaptive Hinge Balance Loss를 제안하고 있다.
    3. Re-DocRED에서의 실험 결과를 통해 우리의 접근법이 다른 균형 조절 방법보다 우수함을 보였다고 한다.
    
    논문 링크: https://github.com/Jize-W/HingeABL

###### Answer-state Recurrent Relational Network (AsRRN) for Constructed Response Assessment and Feedback Grouping (https://aclanthology.org/2023.findings-emnlp.254/)
- Anthology ID: 2023.findings-emnlp.254 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. NLP에서 새로운 유형인 constructed response (CR) 질문에 대응하는 Answer-state Recurrent Relational Network (AsRRN)를 개발하여, college STEM에서 일반적인 multiple questions per context 구조를 다루었다.
    2. AsRRN은 계산 그래프에서 특정 종속성을 위한 relation 벡터를 학습하며, contrastive loss를 통해 더 좋은 표현 학습과 학생 피드백을 지원한다.
    3. AsRRN은 LLMs 기반의 분류기, CR 질문을 위한 이전 relational network, 그리고 GPT-3.5를 이용한 few-shot learning을 능가하는 성능을 보였다.

###### Low-Resource Comparative Opinion Quintuple Extraction by Data Augmentation with Prompting (https://aclanthology.org/2023.findings-emnlp.255/)
- Anthology ID: 2023.findings-emnlp.255 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Comparative Opinion Quintuple Extraction (COQE)는 비교 문장에서 주체, 대상, 공유 가능한 측면, 비교 의견, 선호도를 예측하는 것을 목표로 한다. 기존의 COQE 방법은 오류 전파 문제로 실패한다.
    2. 이 논문에서는 데이터 증강 기법에 기반한 저자원 비교 의견 퀸텀 추출 방법인 DAP(Dataset Augmentation with Prompting)을 소개한다.
    3. Camera, Car, Ele의 세 가지 데이터셋을 사용한 실험 결과 우리의 접근법이 대폭 개선되며 최고 성능을 달성한다는 것을 보여준다.

###### A New Benchmark and Reverse Validation Method for Passage-level Hallucination Detection (https://aclanthology.org/2023.findings-emnlp.256/)
- Anthology ID: 2023.findings-emnlp.256 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델은 현실 세계에서 사람들과 효과적으로 협업할 수 있지만, 잘못된 텍스트나 검증되지 않은 정보를 만들어 내는 오류가 발생할 수 있다.
    2. 본 논문에서는 제로 리소스 방식으로 사실적인 오류를 자동으로 감지하기 위해 역 검증을 기반으로 한 자가 점검 방법을 제안한다.
    3. 실험 결과는 제안된 방법이 베이스 라인보다 우수한 성능을 보이며, 토큰과 시간이 적게 든다는 것을 보여준다. 또한, LLM이 포착하지 못한 몇 가지 오류 케이스를 수동으로 분석하여 제로 리소스 방법의 공통적인 한계를 밝힌다.

###### Speculative Decoding: Exploiting Speculative Execution for Accelerating Seq2seq Generation (https://aclanthology.org/2023.findings-emnlp.257/)
- Anthology ID: 2023.findings-emnlp.257 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Speculative Decoding (SpecDec)를 제안하여 예상 실행의 개념을 활용하여 autoregressive (AR) decoding을 가속화하는 방법을 공식적으로 연구하였습니다. 
    2. SpecDec는 Spec-Drafter와 Spec-Verification이라는 두 가지 혁신을 가지고 있으며, 이를 통해 Transformer 아키텍처에서 약 5배의 속도 향상을 달성할 수 있습니다. 
    3. 뿐만 아니라 SpecDec의 추가적인 장점들을 보여주며, 실제 응용 프로그램에서 생성 모델의 가속화를 위한 실용적인 가치를 확인할 수 있습니다.

###### APP: Adaptive Prototypical Pseudo-Labeling for Few-shot OOD Detection (https://aclanthology.org/2023.findings-emnlp.258/)
- Anthology ID: 2023.findings-emnlp.258 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "사용자 쿼리에서 out-of-domain (OOD) 의도를 감지하는 것은 task-oriented 대화 시스템에 있어서 필수적이다. 이 논문에서는 대부분의 라벨링된 in-domain (IND) 의도가 있는 가정이 아닌, 실제로 IND 데이터가 적고 IND와 OOD에 속할 수 있는 대량의 라벨 되지 않은 혼합 데이터가 있는 few-shot OOD 설정에 초점을 맞춘다."
    2. "우리는 한정된 IND 데이터를 사용하여 구별력 높은 표현을 학습하고, 라벨 되지 않은 혼합 데이터를 활용하는 few-shot OOD 감지를 위한 adaptive prototypical pseudo-labeling (APP) 메소드를 제안한다. 이 방법은 한정된 IND 데이터를 사용하고 IND 데이터를 이용한 low-resource OOD 감지를 돕는 prototypical OOD 감지 프레임워크(ProtoOOD)와 고품질의 pseudo OOD와 IND 라벨을 생성하기 위한 adaptive pseudo-labeling 방법을 포함한다."
    3. "영구 실험과 분석을 통해 우리의 방법이 few-shot OOD 감지에 효과적임을 입증하였다."

###### 2INER: Instructive and In-Context Learning on Few-Shot Named Entity Recognition (https://aclanthology.org/2023.findings-emnlp.259/)
- Anthology ID: 2023.findings-emnlp.259 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Pre-training 지식을 활용하여 down-stream few-shot task에서 강력한 기법인 Prompt-based learning이 등장했으나, NER 태스크를 위한 새로운 text-to-text 프레임워크 2INER를 제안한다.
    2. 우리의 접근 방식은 InstructionNER를 기반으로 instruction finetuning을 사용하여 모델이 과제별 지침을 효과적으로 이해하고 처리할 수 있게 한다. 
    3. 우리는 Type Extracting이라는 새로운 보조 작업을 소개하여 문장의 전체 의미적 맥락에서 entity 유형을 모델이 더 잘 이해하도록 한다. 결과적으로 우리의 방법은 존재하는 Few-Shot NER 방법을 능가하며 최첨단 표준 NER 알고리즘과 경쟁력을 유지한다.

###### Generative Emotion Cause Triplet Extraction in Conversations with Commonsense Knowledge (https://aclanthology.org/2023.findings-emnlp.260/)
- Anthology ID: 2023.findings-emnlp.260 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ECTEC (Emotion Cause Triplet Extraction in Conversations)는 대화에서 감정 발화, 감정 범주 및 원인 발화를 동시에 추출하는 것을 목표로 한다. 
    2. 기존 연구들은 ECTEC 작업을 여러 하위 작업으로 분해하고 이를 파이프라인 방식으로 해결한다.
    3. 이 논문에서는 SHARK라는 commonSense knowledge-enHanced generAtive fRameworK를 제안하였다. 이는 ECTEC 작업을 인덱스 생성 문제로 정의하고 시퀀스 투 시퀀스 모델을 사용하여 감정-원인-범주 세트를 자동으로 생성한다.

###### Proto-lm: A Prototypical Network-Based Framework for Built-in Interpretability in Large Language Models (https://aclanthology.org/2023.findings-emnlp.261/)
- Anthology ID: 2023.findings-emnlp.261 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델 (LLMs)은 자연어 처리 (NLP) 분야를 크게 발전시켰으나, 해석 가능성의 부족은 주요한 문제점이다. 
    2. 기존 방법들은 추론 시간 이후에 적용되는 후처리(post hoc) 방식으로 저수준 피처에 초점을 맞추고 상위 수준의 텍스트 단위의 설명 가능성을 갖지 못한다.
    3. 이 연구에서는 proto-lm이라는 프로토타입 네트워크 기반의 화이트 박스 프레임워크를 소개하는데, 이는 경쟁력 있는 성능을 유지하면서 fine-tuning 단계에서 바로 해석 가능한 임베딩을 학습할 수 있게 한다.

###### GROVE: A Retrieval-augmented Complex Story Generation Framework with A Forest of Evidence (https://aclanthology.org/2023.findings-emnlp.262/)
- Anthology ID: 2023.findings-emnlp.262 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 조건부 이야기 생성은 복잡한 플롯을 가진 이야기를 만드는 사람-기계 상호작용에서 중요하며, 기존 방법은 세부적인 프롬프트에 의존하여 창의적인 플롯을 억제한다. 
    2. 이 논문에서는 인간이 작성한 예시 이야기에서 정보를 활용하여 다양한 플롯을 생성하는 "GROVE"라는 프레임워크를 제안한다.
    3. 이 프레임워크는 타깃 조건에 대한 검색 저장소를 구축하여 LLMs를 자극하는데 활용하며, "asking-why" 프롬프팅 체계를 설계하여 이야기의 배경에 대한 정보를 공급한다.

###### KAPALM: Knowledge grAPh enhAnced Language Models for Fake News Detection (https://aclanthology.org/2023.findings-emnlp.263/)
- Anthology ID: 2023.findings-emnlp.263 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어에서의 뉴스 소비가 증가함에 따라 가짜 뉴스의 전파 또한 늘어났는데, 기존의 가짜 뉴스 탐지 방법은 외부 entity(knowledge) 정보를 활용한다.
    2. 이 논문에서는 뉴스 entity 정보 뿐만 아니라 뉴스 entity 간의 구조화된 지식까지 고려하는 방법을 제안한다.
    3. 실험 결과는 우리의 방법이 저자들의 실험 기준에 비해 더 나은 성능을 보여준다는 것을 보여준다. 또한, few-shot 시나리오에서도 경쟁력을 가지고 있다.

###### Comparing the Evaluation and Production of Loophole Behavior in Humans and Large Language Models (https://aclanthology.org/2023.findings-emnlp.264/)
- Anthology ID: 2023.findings-emnlp.264 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "법, 전통, 일상생활에서 loopholes는 흔하게 일어난다. 파고드는 이들은 다른 사람의 의도된 의미나 목표를 이해하나, 다른 해석을 택한다. AI 연구는 지금까지 artificial intelligence가 loopholes를 활용하는 것처럼 보였으나, 이는 아마 인간화일 가능성이 높다. 현재 모델들, 특히 큰 Language 모델들이 loopholes를 이해하는 데 필요한 실용적 이해를 얼마나 잘 포착하는지는 여전히 불분명하다."
    2. "우리는 두 가지 loophole 행동 연구를 위해 개발된 평가 지표인 LLMs의 성능을 조사했다: 평가 (문제, 불쾌함, 유머의 평가)와 생성 (주어진 맥락에서 새로운 loopholes 찾기). 우리는 최신 LLMs와 인간들을 세밀하게 비교하고, 대다수의 모델들이 loophole 행동을 통한 결과물이 완벽한 비준수보다 문제와 불쾌함이 적다고 평가했으며 (성인들과 일치), 그러나 인간들처럼 loophole을 창의적으로 활용한 유머를 인식하는 데 어려움이 있다는 것을 발견했다."
    3. "게다가, GPT 3과 3.5 두 모델만이 자체 loophole을 생성할 수 있으며, 그 중 GPT3.5가 인간의 기준에 가장 가깝게 수행하는 것으로 나타났다."

###### InstructExcel: A Benchmark for Natural Language Instruction in Excel (https://aclanthology.org/2023.findings-emnlp.265/)
- Anthology ID: 2023.findings-emnlp.265 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large Language Models, LLMs)의 발전으로 우리는 스프레드시트를 포함한 다양한 도메인에서 복잡한 NLP 태스크를 해결할 수 있게 되었습니다. 이 연구는 LLMs가 자연어 사용자 명령을 통해 스프레드시트 특정 작업을 해결하는 코드(Excel OfficeScripts)를 생성할 수 있는지를 조사합니다.
    2. 이를 위해 우리는 Excel의 '자동화' 기능을 활용하여 사용자의 동작으로부터 OfficeScripts를 자동으로 생성하는 InstructExcel이라는 대규모 벤치마크를 소개합니다.
    3. GPT-4와 같은 최신 모델을 기준으로한 다양한 제로샷 및 퓨샷 설정에서의 실험 결과, InstructExcel이 GPT-4와 같은 최신 모델에게 어려운 벤치마크라는 것을 관찰하며, (1) GPT-4 대 GPT-3.5 사용, (2) 보다 많은 문맥 예제 제공, (3) 동적 프롬프팅은 이 벤치마크에서의 성능을 향상시키는 데 도움이 될 수 있다는 것을 알 수 있었습니다.

###### Hallucination Detection for Grounded Instruction Generation (https://aclanthology.org/2023.findings-emnlp.266/)
- Anthology ID: 2023.findings-emnlp.266 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 연구에서는 실내 환경에서 사람을 안내하기 위한 지침 생성 문제를 조사한다. 현재 모델의 주요 문제는 환각이다: 모델은 사람이 따라갈 때 실행되거나 마주칠 수 없는 동작이나 물체에 대한 참조를 생성한다.
    2. 우리는 이러한 환각된 참조를 탐지하기 위해 큰 양의 이미지 - 텍스트 쌍으로 사전 훈련된 모델을 채택하고, 합성된 환각을 포함한 지침과 올바른 지침을 구분하는 대조 손실에 대해 세부 튜닝을 한다.
    3. 우리의 최종 모델은 지시어 생성 모델에 의한 단어 확률을 사용하는 기준선 및 LSTM 및 Transformer를 기반으로 한 지도 모델을 포함하여 여러 가지 기준모델을 능가한다.

###### Definitions Matter: Guiding GPT for Multi-label Classification (https://aclanthology.org/2023.findings-emnlp.267/)
- Anthology ID: 2023.findings-emnlp.267 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델은 미세 조정(fine-tuning) 없이도 많은 자연어 태스크를 수행하는 능력으로 최근 인기를 끌고 있다. 
    2. 이 연구에서는 (1) 예시에서 정의를 생성하고 제로샷 분류에 사용하며, (2) LLM이 그 정의를 활용하는 방법을 조사하는 두 가지 새로운 아이디어에 초점을 맞추고 있다.
    3. GPT-3 모델을 사용하여 트윗의 세부적인 다중 레이블 음모론 분류에 대해 제로샷 레이블링을 통해 성능을 분석하고, 레이블의 정의형식의 최소한이면서도 의미 있는 컨텍스트를 제공하여 레이블링을 개선하는 방법을 평가한다.

###### ECHo: A Visio-Linguistic Dataset for Event Causality Inference via Human-Centric Reasoning (https://aclanthology.org/2023.findings-emnlp.268/)
- Anthology ID: 2023.findings-emnlp.268 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ECHo는 비디오-언어적 소셜 시나리오에 기반한 사건 인과 추론을 위한 진단 데이터셋으로, 인간 중심의 연역적 정보를 활용한다. 
    2. ECHo는 비디오-언어적 추론에 대한 ToM 능력을 요구하여, 현재 AI 시스템의 추론 능력을 평가하는 CoT 프레임워크를 제안한다.
    3. ECHo는 InstructGPT와 MiniGPT-4와 같은 최근의 대형 foundation model들을 사람 중심의 진단 태스크에서 검증하는 데 사용되며, 이를 통해 추론의 불완전성과 일관성의 문제를 드러내는 어려운 데이터셋임을 보여준다.
    
    (ECHo: Event Causality Inference via Human-Centric Reasoning, ToM: Theory-of-Mind, CoT: Chain-of-Thought)

###### An Empirical Study of Instruction-tuning Large Language Models in Chinese (https://aclanthology.org/2023.findings-emnlp.269/)
- Anthology ID: 2023.findings-emnlp.269 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. ChatGPT의 성공은 대형 언어 모델의 인공 일반지능 (AGI)에 대한 잠재력을 입증한다. 다음으로, 대형 언어 모델 공개로 인해 커뮤니티에서는 ChatGPT 복제 프로세스를 가속화하기 위해 'instruction-tuning'에 대한 관심이 높아졌다.
    2. 그러나 세계에서 가장 많이 사용되는 중국어에서 instruction-tuning 대한 연구는 아직 초기 단계에 있다. 따라서 이 논문은 중국어에서 instruction-tuning 대한 철저한 경험적 연구를 수행하였으며, 이는 중국어 지침에 더 효과적으로 대응할 수 있는 LLMs를 사용자 정의하는 데 유용한 결과를 제공하는 쿡북 역할을 할 수 있다.
    3.특히, LLM 기반, 매개변수 효율적인 방법, instruction 데이터 유형 등, instruction-tuning에 가장 중요한 세 가지 요소의 영향을 체계적으로 탐색했다. 또한, chain-of-thought 데이터와 인간의 가치 정렬과 같은 다른 요소들의 영향을 연구하기 위한 실험도 수행되었다.

###### Debiasing Multimodal Models via Causal Information Minimization (https://aclanthology.org/2023.findings-emnlp.270/)
- Anthology ID: 2023.findings-emnlp.270 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 다중모달 모델에 대한 편향 보정 방법은 근사적인 휴리스틱을 사용하여 편향을 나타내는데, 이러한 휴리스틱은 훈련 초기의 얕은 특징 또는 VQA와 같은 다중모달 태스크의 단일모달 특징들을 사용하는 것이 일반적이다.
    2. 이 논문에서는 다중모달 데이터에 대한 인과 그래프에서 발생하는 편향을 연구하고, 인과론적 정보 최소화를 활용하여 편향 제거를 위한 새로운 접근 방식을 제안한다. 
    3. 제안된 방법들은 데이터셋의 편향을 포착하고, 편향 제거 방법은 분포 범위를 벗어난 데이터에 대한 성능을 향상시키면서도 분포 내의 성능은 유지할 수 있다는 것을 실험 결과를 통해 확인하였다.

###### Evaluating Emotion Arcs Across Languages: Bridging the Global Divide in Sentiment Analysis (https://aclanthology.org/2023.findings-emnlp.271/)
- Anthology ID: 2023.findings-emnlp.271 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. Emotion arcs는 개인 또는 인구의 시간에 따른 감정 변화를 나타내는데 널리 사용되지만, 이를 자동으로 생성하는 것에 대한 평가에는 여전히 연구가 부족하다. 이 연구에서는 자동으로 생성된 감정 변화를 첫 번째로 체계적이고 정량적으로 평가하며, 머신러닝 모델과 Lexicon-Only 방법 두 가지 일반적인 감정 변화 생성 방법을 비교한다.
    2. 인스턴스 수백 개에서 정보를 종합하는 데 있어서는 Lexicon-Only 방법이 감정 분류에서는 좋지 않지만, 감정 변화를 생성하는 데에는 매우 정확하다는 것을 18개의 다양한 데이터셋과 9개의 언어에서 실험을 통해 보여준다.
    3. 또한 영어 감정 어휘의 자동 번역이 자원이 적은 언어에서도 높은 품질의 감정 변화를 생성하는 데 사용될 수 있다는 것을 여섯 가지 아프리카 원주민 언어, 아랍어, 스페인어 실험을 통해 보여준다.

###### Multi-step Jailbreaking Privacy Attacks on ChatGPT (https://aclanthology.org/2023.findings-emnlp.272/)
- Anthology ID: 2023.findings-emnlp.272 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대규모 언어 모델(Large Language Models, LLMs)의 빠른 발전으로 적절한 입력 프롬프트가 주어질 경우, 다양한 NLP 태스크를 잘 해결할 수 있다. 그러나 LLM에서 유해한 콘텐츠 생성을 피하기 위한 작업에도 불구하고, 인공지능 생성 콘텐츠(AIGC)를 인간의 이익을 위해 조절하는 것은 여전히 어려운 과제이다. 
    2. 강력한 LLMs이 다양한 도메인의 기존 텍스트 데이터를 처리하고 있는데 (예: GPT-3는 45TB의 텍스트로 훈련함), 이 훈련 데이터에 개인 정보가 포함되어 있는지 그리고 이러한 LLMs과 그들의 downstream 어플리케이션은 어떤 개인정보 위협을 가져올 수 있는지 의심스러울 수 있다.
    3. 이 논문에서는 OpenAI의 ChatGPT와 ChatGPT 기반으로 개선된 New Bing으로부터의 개인정보 위협을 연구하고, 어플리케이션에 통합된 LLMs가 새로운 개인정보 위협을 일으킬 수 있음을 보여준다. 이를 위해 우리는 광범위한 실험을 수행하여 주장을 뒷받침하고, LLMs의 개인정보 영향에 대해 논의한다.

###### Chain-of-Thought Embeddings for Stance Detection on Social Media (https://aclanthology.org/2023.findings-emnlp.273/)
- Anthology ID: 2023.findings-emnlp.273 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 소셜 미디어에서의 stance detection은 대형 언어 모델(LLM)에게 도전적이며, 임의 표현과 비형식적인 언어로 인해 암묵적인 stance 레이블이 포함되어 있다. COT(prompt) 기법은 stance detection 성능을 향상시키는 것으로 알려져 있으나 여전히 암묵적 stance 인식에 어려움을 겪고 있다. 
    2. 이 논문에서는 COT(reasoning chain) 임베딩을 도입하여 전통적인 RoBERTa 기반의 stance detection 파이프라인에 통합함으로써 COT의 성능을 향상시켰다. 
    3. 실험 결과, COT(reasoning chain)은 text encoder가 COT 레이블을 왜곡시킬 수 있는 미세한 오류나 착각을 통해 학습할 수 있으며, 도메인 특정 패턴에 의존하는 경우 잘못된 COT reasoning을 간과할 수 있다는 것을 보여주었다.

###### Using LLM for Improving Key Event Discovery: Temporal-Guided News Stream Clustering with Event Summaries (https://aclanthology.org/2023.findings-emnlp.274/)
- Anthology ID: 2023.findings-emnlp.274 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정치적 담론을 분석하기 위해서는 뉴스 스트림에서 핵심 사건과 그에 연관된 뉴스 기사를 식별하는 것이 중요하다. 
    2. 우리는 뉴스 스트림 클러스터링을 위한 일반적인 프레임워크를 제안하고, 이를 통해 중요한 뉴스 이벤트와 그에 대한 뉴스 아티클을 자동으로 추출한다.
    3. 우리의 간단하고 효과적인 프레임워크는 더 일관된 이벤트 중점 클러스터를 생성하며, 이를 통해 KeyEvents라는 11개 주제의 611개 핵심 이벤트를 가진 40,000개 문서의 데이터셋을 구축한다.

###### Descriptive Prompt Paraphrasing for Target-Oriented Multimodal Sentiment Classification (https://aclanthology.org/2023.findings-emnlp.275/)
- Anthology ID: 2023.findings-emnlp.275 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "Target-Oriented Multimodal Sentiment Classification (TMSC)"은 텍스트, 이미지 및 기타 다양한 모달리티를 포함하여 대상의 감성 극성을 함께 분류하는 작업이다. 
    2. 기존 연구들은 대상의 타입에 따라 분산 방식으로 작업을 수행하는데, 이는 대상의 감성 극성이 타입이 아니라 문맥에 의해 결정된다는 점을 고려하지 않았다.
    3. 이 논문에서는 UnifiedTMSC라는 통합 모델을 제안하여 이 문제를 해결하였고, 실제 실험결과에서도 그 효과를 입증하였다.

###### Joint Semantic and Strategy Matching for Persuasive Dialogue (https://aclanthology.org/2023.findings-emnlp.276/)
- Anthology ID: 2023.findings-emnlp.276 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 설득 대화는 대화를 통해 사용자를 설득하여 목표를 달성하는 것을 목표로 한다. 기존의 설득 모델은 주로 문장의 의미 일치에 기반하지만, 대화 전략과 같은 중요한 측면을 무시하는 경향이 있다.
    2. 대화 전략은 문장 의미에 비해 고수준 개념이며, 효과적인 설득을 위해 정보를 제공하고 보완하는 역할을 할 수 있다.
    3. 본 논문에서는 대화 의미와 전략을 함께 모델링하여 설득 모델을 구축하는 것을 제안한다. 실험 결과, 우리의 접근법은 Recall@1 측면에서 작은 데이터셋에서 5%와 큰 데이터셋에서 37%까지 최신 기준 모델에 비해 성능을 크게 개선했다. 상세 분석 결과, 자동 회귀 예측기가 최종 성능에 가장 큰 기여를 한다는 것을 보여준다.

###### Non-Autoregressive Sentence Ordering (https://aclanthology.org/2023.findings-emnlp.277/)
- Anthology ID: 2023.findings-emnlp.277 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 문장 순서 결정 방법은 순서에 맞게 문장을 예측하기 위해 반복적으로 엔코더-디코더 프레임워크를 사용한다. 그러나 이러한 방식은 디코딩 중에 단방향 종속성만을 활용하며 문장 간의 의미적 종속성을 완전히 탐구할 수 없다는 한계가 있다.
    2. 이 논문에서는 문장 간의 양방향 종속성을 탐구하고 각 위치에 대한 문장을 병렬로 예측하는 새로운 비자기 회귀적 순서 결정 네트워크인 NAON을 제안한다. 문장의 길이가 결정적이며 문장과 위치가 서로 매치되어야 하는 문장 순서 결정 과제에 비자기 회귀적 방식이 특히 적합하다고 주장한다.
    3. 실험 결과를 통해 제안한 모델의 효과를 확인하고, 기존의 자기 회귀적 접근 방식보다 우수한 성능을 나타내며 최신 기법과 경쟁력 있는 성능을 달성한다는 것을 보여준다.

###### Large Language Models are Not Yet Human-Level Evaluators for Abstractive Summarization (https://aclanthology.org/2023.findings-emnlp.278/)
- Anthology ID: 2023.findings-emnlp.278 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 언어 모델(ChatGPT, GPT-4 등)의 추론 능력이 크게 발전함에 따라, 다양한 작업에 언어 모델을 활용하는 추세가 있다. 그 중 한 분야는 복잡한 생성 작업의 대체 평가 메트릭으로 언어 모델을 사용하는 것이다.
    2. 본 논문에서는 ChatGPT와 GPT-4가 기존 자동 평가 메트릭을 능가하지만, 일관성과 신뢰성 측면에서 아직은 인간 대체 수준에 이르지 못하는 것으로 밝혀졌다. 또한, 언어 모델은 후보 시스템을 일관되게 평가하지 못하며, 차원에 따라 평가 결과가 달라진다.
    3. 언어 모델은 성능이 비슷한 후보들을 비교하는 데 어려움을 겪으며, 높은 품질의 요약문일수록 인간 평가와의 상관관계가 낮아져 신뢰성이 떨어진다. 따라서, 발전하는 요약 시스템을 평가할 때 언어 모델을 사용하면 오해를 불러일으킬 수 있다.

###### Women Wearing Lipstick: Measuring the Bias Between an Object and Its Related Gender (https://aclanthology.org/2023.findings-emnlp.279/)
- Anthology ID: 2023.findings-emnlp.279 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문에서는 이미지 캡션 시스템에서 객체가 성별 편향에 미치는 영향을 조사하였다. 그 결과, 성별 특정 객체만이 성별 편향을 강하게 가지고 있음을 보였다.
    2. 또한, 우리는 시각적 의미 기반 성별 점수를 제안하였는데, 이 점수는 편향 정도를 측정하고 어떤 이미지 캡션 시스템에도 적용될 수 있는 플러그인 역할을 할 수 있다.
    3. 실험 결과 우리는 성별 점수가 유용하게 사용될 수 있는데, 캡션과 관련된 성별 편향을 측정할 수 있기 때문에 기존의 Object Gender Co-Occ 접근법에 추가적인 메트릭으로 사용될 수 있다.

###### FREDSum: A Dialogue Summarization Corpus for French Political Debates (https://aclanthology.org/2023.findings-emnlp.280/)
- Anthology ID: 2023.findings-emnlp.280 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인코더-디코더 아키텍처의 발전으로 문서에 대한 추상적 요약 시스템의 성능이 크게 향상되었다. 그러나 최근 몇 년간 대화와 다자간 대화의 요약에 대한 관심이 증가하고 있다.
    2. 이 논문은 프랑스 정치 토론에 대한 데이터셋을 제안하여 다국어 대화 요약 연구에 필요한 리소스를 개선하는 목적으로 한다.
    3. 고품질의 전사 및 주석이 정확하고 효과적인 대화 요약 모델을 훈련하는 데 중요하며, 비영어 언어에서의 대화 요약을 지원하기 위해 다국어 리소스가 필요하다고 강조한다. 또한 최신 기법을 사용한 베이스라인 실험을 제공하고, 대화 요약 분야의 연구를 촉진할 것을 권장하며, 데이터셋을 연구 커뮤니티에 공개하여 다국어 대화 요약의 추가적인 발전을 가능하게 할 것이다.

###### Towards Zero-shot Relation Extraction in Web Mining: A Multimodal Approach with Relative XML Path (https://aclanthology.org/2023.findings-emnlp.281/)
- Anthology ID: 2023.findings-emnlp.281 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 웹 페이지의 급증과 그 구조의 복잡성이 웹 마이닝 모델에 도전을 제기한다. 현재의 방법들은 텍스트 노드들 사이의 관계를 고려하지 못하고, 이에 대한 문제를 해결하기 위해 새로운 방법인 ReXMiner를 제안한다. ReXMiner는 웹 페이지의 Document Object Model (DOM) 트리에서 가장 짧은 상대 경로를 인코딩하여 웹 페이지 내에서 key-value 쌍 추출에 더 정확하고 효율적인 신호를 제공한다.
    2. 또한 ReXMiner는 각 텍스트 노드의 인기도를 고려하여 다른 웹 페이지에서 동일한 텍스트 노드의 발생 빈도를 계산한다. 
    3. 공개적인 벤치마크 실험 결과로써, ReXMiner는 웹 마이닝의 zero-shot 관계 추출 과제에서 최신 기준선보다 우수한 성능을 보여준다.

###### Narrative Style and the Spread of Health Misinformation on Twitter (https://aclanthology.org/2023.findings-emnlp.282/)
- Anthology ID: 2023.findings-emnlp.282 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 서술적 스타일은 소셜미디어에서의 건강 정보 전달에 효과적인 방법이지만, 잘못된 정보가 온라인으로 퍼지고 그것의 부정적인 영향이 커지는 상황에서 서술적 의사소통 스타일과 건강 정보의 불규칙성이 소셜미디어에서의 사용자 참여에 어떤 영향을 미치는지 조사하는 것이 필요하다.
    2. 본 연구에서는 Twitter 컨텍스트에서의 이를 탐구하기 위해, 이전에 어노테이트된 건강 정보의 잘못된 트윗 (약 15,000개)을 사용하고 서술적 스타일의 존재 유무를 어노테이션을 통해 확인하였다. 이후 이러한 레이블을 사용하여 텍스트 분류기를 훈련시키고, 자동 서술 감지를 위해 지도 학습과 인텍스트 학습을 실험했다.
    3. 최고 모형을 사용하여 데이터 집합의 남은 부분을 레이블링 한 뒤, 서술적 스타일, 잘못된 정보 및 사용자 수준 특징과 참여 사이의 관계를 통계적으로 분석하였으며, 서술의 일반적인 언어 범주 및 건강 정보에 대한 잘못된 정보의 범주를 분석하였다.

###### HadSkip: Homotopic and Adaptive Layer Skipping of Pre-trained Language Models for Efficient Inference (https://aclanthology.org/2023.findings-emnlp.283/)
- Anthology ID: 2023.findings-emnlp.283 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(LMs)은 많은 NLP 작업에서 놀라운 성능을 보여주었지만, 투입되는 자원과 추론에 필요한 높은 계산 비용 때문에 실시간 시스템에 적용하기 어렵다. 
    2. 우리는 기존의 조기 종료 방법들과 달리, 선택된 종료층 이전의 모든 층을 순차적으로 통과해야 하는 제약을 없애고 유연성을 높여 성능을 향상시키기 위해 HadSkip이라는 새로운 레이어 스킵 방법을 제안한다. 
    3. GLUE 벤치마크에서의 실험 결과, 제안된 HadSkip이 모든 최신 기베라인에 비해 우수한 성능을 보여주었다.

###### Empowering Psychotherapy with Large Language Models: Cognitive Distortion Detection through Diagnosis of Thought Prompting (https://aclanthology.org/2023.findings-emnlp.284/)
- Anthology ID: 2023.findings-emnlp.284 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 정신 질환은 전문가의 부족과 접근성 제한으로 인해 현재 가장 중요한 공중 보건 문제 중 하나입니다. 표현력이 뛰어나고 복잡한 추론과 분석을 수행하는 고급 전문성이 필요합니다. 
    2. 우리는 대규모 언어 모델 시대에 인공지능을 통한 심리치료 지원을 개발하기에 적절한 시기라고 생각합니다. 우리는 인식 왜곡(cognitive distortion) 검출 작업을 연구하고, DoT (Diagnosis of Thought) prompting을 제안합니다.
    3. DoT은 환자의 언어를 세 단계로 진단하여 주제 평가, 대조적 추론, 기질 분석을 수행합니다. 이를 통해 전문가들의 지원을 위한 진단 이유를 생성합니다. 실험 결과, DoT은 ChatGPT에 비해 인지 왜곡 감지에서 큰 향상을 보여주며, 인간 전문가가 승인한 고품질 이유를 생성합니다.

###### Measuring the Knowledge Acquisition-Utilization Gap in Pretrained Language Models (https://aclanthology.org/2023.findings-emnlp.285/)
- Anthology ID: 2023.findings-emnlp.285 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델(PLM)이 많은 지식을 습득하는 것을 보여주었으나, 이 파라미터 기반 지식 중 얼마나 실제로 다운스트림 태스크 수행에 활용될 수 있는지는 여전히 불분명하다.
    2. 우리는 PLM에서 파라미터의 지식을 추출하고, 이 추출된 지식을 기반으로 다운스트림 태스크를 구성하는 체계적인 프레임워크를 제안한다.
    3. 우리의 연구 결과는 PLMs의 습득된 지식과 활용된 지식 사이에 차이가 있음을 보여주며, 분포 변화에서의 지식 활용에서 제한된 강건성을 보여주고, 큰 모델일수록 확보된 지식의 차이를 줄이지만 활용된 지식의 차이는 여전하다.

###### Non-compositional Expression Generation Based on Curriculum Learning and Continual Learning (https://aclanthology.org/2023.findings-emnlp.286/)
- Anthology ID: 2023.findings-emnlp.286 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "비구성 표현은 NLP 시스템에 있어서 한계가 있는데, 현재의 신경망 모델, 특히 대규모 사전 훈련 언어 모델에서도 어렵다."
    2. 이 논문은 비구성 표현 생성 과제에서 동적 커리큘럼 학습 프레임워크를 제안하고, 잊혀짐 문제를 완화하기 위해 지속적 학습 방법을 적용한다.
    3. 이러한 방법을 통해 비구성 표현 생성 작업에서 모델의 성능을 점진적으로 개선할 수 있으며, 관용구 생성 및 은유 생성에 대한 실험에서도 유효성을 확인하였다.

###### Information Extraction from Legal Wills: How Well Does GPT-4 Do? (https://aclanthology.org/2023.findings-emnlp.287/)
- Anthology ID: 2023.findings-emnlp.287 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 이 논문은 법적 유언에서의 정보 추출 (IE)를 위한 수동으로 주석이 달린 데이터셋을 제시하고, 데이터셋에서 진행된 관련 "in-context learning" 실험을 소개한다. 
    2. 이 데이터셋은 entity, entity 간의 이진 관계, n-ary events (e.g., bequest) 등을 포함하며, 이는 미국의 두 주에서 추출된 45개의 법적 유언으로 구성되어 있다. 
    3. 이 데이터셋은 법률 도메인에서의 하향식 작업에 기반이 될 수 있으며, 대형 언어 모델 (LLMs)의 이 IE 작업에 대한 성능을 평가하는 데에도 활용될 수 있다.

###### Transparency at the Source: Evaluating and Interpreting Language Models With Access to the True Distribution (https://aclanthology.org/2023.findings-emnlp.288/)
- Anthology ID: 2023.findings-emnlp.288 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 인공적인 언어와 비슷한 데이터를 사용하여 신경 언어 모델을 훈련하고 평가하고 해석하기 위한 세팅을 제안한다.
    2. 많은 자연어 코퍼스에서 파생된 상당한 확률적 문법을 사용해서 데이터를 생성하고 이를 통해 훈련과정을 완전히 제어할 수 있다.
    3. 우리의 결과는 신경 언어 모델의 아키텍처와 훈련 목표가 perplexity의 하한에 대해 얼마나 잘 근사할 수 있는지에 대한 놀라운 차이를 보여준다.

###### Continual Generalized Intent Discovery: Marching Towards Dynamic and Open-world Intent Recognition (https://aclanthology.org/2023.findings-emnlp.289/)
- Anthology ID: 2023.findings-emnlp.289 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 일반적인 대화 시스템에서 사용자는 주제 외의 쿼리를 입력할 수 있다. GID 작업은 OOD(Out-of-Domain) 쿼리에서 OOD intents를 발견하고 이를 IND(In-Domain) 분류기에 확장하는 것을 목표로 한다. 
    2. 하지만 GID는 OOD 학습의 일부분만 고려하며, 이전 단계의 데이터를 모두 사용하여 공동 학습해야 하기 때문에 실제 응용에 제한이 있다.
    3. 이 논문에서는 Continuous Generalized Intent Discovery (CGID)라는 새로운 과제를 소개하고, 동적인 OOD 데이터 스트림에서 OOD intents를 지속적으로 발견하고 거의 이전 데이터 없이 분류기에 점진적으로 추가하는 것을 목표로 한다.

###### Frugal Prompting for Dialog Models (https://aclanthology.org/2023.findings-emnlp.290/)
- Anthology ID: 2023.findings-emnlp.290 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 대형 언어 모델(Large Language Model, LLM)을 자연어처리 태스크에 사용하는 경우가 많아지고 있으며, 이로 인해 연구자들은 문제에 접근하는 방식을 바꿔가고 있다. 이 연구는 LLM을 사용하여 대화 시스템을 구축하는 다양한 접근 방식과 대화 기록의 효율적인 표현에 대해 분석하여 LLM의 상호작용 능력을 이해하는 데 기여한다.
    2. 연구에서는 지침, 예시, 현재 질의, 추가적인 맥락 등의 다양한 prompt 요소를 고려하여 다른 대화 시스템을 구축하는 방법을 실험하였다. 또한, 대화 기록의 표현을 분석하여 유용한 정보 밀도가 최적인 방법을 찾았다.
    3. 연구 결과를 기반으로, 대화 기록 정보를 보다 간결하게 제공하면서 성능을 유지하고 모델의 추론-API 비용을 줄일 수 있는 방법을 제안하였다. 이 연구는 LLM을 효과적으로 대화 시스템 구축에 활용하는 데 도움이 되는 내용을 제시한다.

###### The Interpreter Understands Your Meaning: End-to-end Spoken Language Understanding Aided by Speech Translation (https://aclanthology.org/2023.findings-emnlp.291/)
- Anthology ID: 2023.findings-emnlp.291 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 현재의 대형 사전 훈련 언어 모델을 사용하여도, 다양한 언어의 경우에도 엔드 투 엔드 음성 언어 이해 (SLU)를 실현하는 것은 여전히 어렵다. 음성 모델에는 낮은 수준의 음향 프레임에서 작동하는 것이 원하는 상위 의미와 다른 언어 간의 연결을 포착할 수 있도록 하므로 기계 번역은 문자 기반으로 강력한 사전 훈련 목표로서 확립되어 있다.
    2. 우리는 특히 다국어 SLU 작업에서 음성 번역 (ST) 작업을 통해 엔드 투 엔드 SLU를 사전 훈련할 수 있는 좋은 방법임을 보여준다. ST를 도입함으로써 우리의 모델은 SLURP, MINDS-14, NMSQA 벤치마크를 사용한 단일 및 다국어 의도 분류 및 음성 질문 답변에서 기준 모델보다 더 좋은 성능을 달성한다.
    3. 우리의 방법의 효과를 검증하기 위해, 우리는 음성 요약 및 영어에서 프랑스어 또는 스페인어로의 저자원/제로샷 전이를 위한 합성 및 실제 원본에서 새로운 벤치마크 데이터셋을 생성하였으며, 더 나은 후속 성능을 위해 ST 사전 훈련 작업에 대한 지식을 보존하는 가치를 보여주고자 한다.

###### MacLaSa: Multi-Aspect Controllable Text Generation via Efficient Sampling from Compact Latent Space (https://aclanthology.org/2023.findings-emnlp.292/)
- Anthology ID: 2023.findings-emnlp.292 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 기존의 multi-aspect controllable text generation 방법들은 디코딩 단계에서 비싼 반복과 탐색을 요구했거나, 각각의 속성을 위해 별도의 컨트롤러를 훈련시키는 문제점이 있어서 다양한 속성 간의 불일치로 인해 텍스트의 품질이 저하된다.
    2. 이 논문에서는 MacLaSa라는 새로운 multi-aspect 제어 방식을 제안하는데, 이 방식은 여러 속성에 대한 압축된 잠재 공간을 추정하고 빠른 샘플러를 사용하여 효율적인 샘플링을 수행한다.
    3. 실험 결과로는 MacLaSa가 속성의 관련성과 텍스트의 품질 모두에서 강력한 기준을 능가하면서도 높은 추론 속도를 유지한다는 것을 보여준다.

###### HPE: Answering Complex Questions over Text by Hybrid Question Parsing and Execution (https://aclanthology.org/2023.findings-emnlp.293/)
- Anthology ID: 2023.findings-emnlp.293 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. "텍스트 기반 질문 응답 시스템의 우세한 패러다임은 자연어 질문에 능숙하게 대응하지만 복잡한 질문에는 한계가 있다. 이에 대조적으로, 구조화된 데이터 소스 (ex. 관계형 데이터베이스, 지식 그래프) 상에서 의미 파싱 접근방식의 널리 사용으로 자연어 질문을 논리적 형태로 변환하고 질의 엔진으로 실행하는 것이 이루어진다."
    2. "우리는 신경망 모델과 심볼릭 방법의 간다한 점을 결합하기 위해 텍스트 기반 질문 파싱 및 실행 프레임워크를 제안한다."
    3. "제안된 프레임워크는 질문 파싱과 하이브리드 실행으로 구성되어 있으며, 해석 가능성을 높이고 심볼릭 연산의 이점을 유지하면서 기본 구성 요소를 해결하기 위해 신경망 판독기를 사용한다."

###### Length-Adaptive Distillation: Customizing Small Language Model for Dynamic Token Pruning (https://aclanthology.org/2023.findings-emnlp.294/)
- Anthology ID: 2023.findings-emnlp.294 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 사전 훈련된 언어 모델의 성능을 향상시키기 위해 모델 압축과 동적 계산 방법이 연구되었으나, 이 두 가지 방법은 따로 개발되어 동적 계산에 최적화된 모델을 만들기 어렵다. 
    2. 길이 적응적 지식 증류 (Length-Adaptive Distillation)라는 이름의 새로운 방법을 제안하여 동적 토큰 가지치기에 적합한 작은 언어 모델을 만드는데 집중한다. 
    3. 실험적 결과는 우리의 방법이 동적 토큰 가지치기에 최적화된 작은 언어 모델을 만들고 속도 및 성능의 균형을 향상시킬 수 있음을 보여준다.

###### Toxicity, Morality, and Speech Act Guided Stance Detection (https://aclanthology.org/2023.findings-emnlp.295/)
- Anthology ID: 2023.findings-emnlp.295 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 본 논문은 소셜 미디어 플랫폼에서 논의되는 다양한 사회 문제에 대한 대중의 태도를 판단하는 작업에 초점을 맞추고 있다. 그러나 트위터와 같은 플랫폼은 종종 극단적인 견해로 오인정보나 가짜 뉴스를 퍼뜨리는 데 사용되며, 톡실한 대화는 부정적인 영향을 퍼뜨려 사회 문제 해결을 지연시킨다.
    2. 이전 연구들은 대개의 경우 트윗의 태도를 캡처하는 데 도움이 될 수 있는 톡실성, 도덕성, 이사회 특징을 무시하거나, 대상에 걸친 태도를 감지할 수 있는 효율적인 아키텍처를 잊고 있는 것으로 나타났다.
    3. 따라서 우리의 연구에서는 톡실성, 도덕성, 이사회 특징을 공유하는 공유 피쳐를 사용하여 트윗의 태도를 정확하게 감지하기 위해 감정, 도덕성, 톡실성과 같은 보조 작업을 활용하는 다중 작업 모델 TWISTED를 제안한다.

###### Reasoning about Ambiguous Definite Descriptions (https://aclanthology.org/2023.findings-emnlp.296/)
- Anthology ID: 2023.findings-emnlp.296 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 자연어 추론은 언어모델의 복잡한 언어이해 과제를 해결하는 데에 점점 더 중요한 역할을 하고 있으며, 추론 기능을 통해 문맥 의존적인 모호함을 해결하는 것이 흥미로운 사례로 등장하고 있다.
    2. 우리는 문맥을 이해하기 위해 명시적 추론을 얼마나 잘 활용할 수 있는지 평가하기 위해 모호한 정확한 표현을 사용하는 것을 제안하고 이를 위한 첫 번째 벤치마크 데이터셋을 제작하고 공개한다.
    3. 우리의 방법은 문제의 모호함을 해결하는 데 필요한 모든 정보를 포함하고 있으므로 모델은 추론 외에 다른 것을 요구하지 않아도 성능이 잘 나온다. 최근의 언어 모델에 대해서도 이는 도전적인 과제임을 확인했다.

###### A Framework for Bidirectional Decoding: Case Study in Morphological Inflection (https://aclanthology.org/2023.findings-emnlp.297/)
- Anthology ID: 2023.findings-emnlp.297 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 텍스트 시퀀스에 대한 sequence-to-sequence 작업에서, 기존의 좌에서 우로 생성하는 Transformer 기반 모델 대신 외부에서 내부로 시퀀스를 생성하는 디코딩 프레임워크를 제안한다. 
    2. 이러한 방식은 이전의 양방향 디코더보다 더 원칙적이라고 주장하며, 모델 아키텍처를 지원하고, 잠재적인 순서 변수를 고려하는 동적 프로그래밍 알고리즘과 같은 여러 훈련 방법을 포함한다.
    3. 제안된 모델은 최신의 SOTA 성능을 보여주며, 특히 긴 시퀀스에 대해서 우수한 성능을 보이고, 어간과 접사로 이루어진 단어의 분리점을 암묵적으로 학습하며, 고유한 레마가 적은 데이터셋에서 기준선에 비해 더 나은 성능을 보인다.

###### Text-guided 3D Human Generation from 2D Collections (https://aclanthology.org/2023.findings-emnlp.298/)
- Anthology ID: 2023.findings-emnlp.298 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 3D 인간 모델링은 게임, 영화, 애니메이션에서 적극적인 상호작용을 위해 폭넓게 사용되고 있다. 이 논문에서는 텍스트에 의해 동작하는 3D 인간 생성 모델을 제안한다. 
    2. 이 모델은 두 가지 목표가 있다. 3D 인간의 처리가 정확해야 하며, 의상은 주어진 텍스트로 제어되어야 한다. 
    3. Cross-modal attention을 사용하는 CCH 모델을 도입하여 3D 인간의 렌더링과 패션 의미를 결합하여 모델링하였으며, 실험 결과는 우수한 성능을 보인다.

###### Statistically Profiling Biases in Natural Language Reasoning Datasets and Models (https://aclanthology.org/2023.findings-emnlp.299/)
- Anthology ID: 2023.findings-emnlp.299 
- Volume: Findings of the Association for Computational Linguistics: EMNLP 2023 
- Authors: Houda Bouamor | Juan Pino | Kalika Bali 
- Summary: 
    1. 최근 연구에서는 많은 자연어 이해 및 추론 데이터셋이 NLP 모델에 의해 활용되는 통계적 단서를 가지고 있으며, 이로 인해 그들의 능력이 과대평가되고 있다는 것을 보여준다. 
    2. 기존 방법들은 이러한 편향을 식별하고 모델의 약점을 평가하는 데 제한이 있다. 
    3. 이 논문에서는 추가 테스트 케이스를 필요로하지 않으면서도 다중 선택 NLU 데이터셋에서 잠재적인 편향을 자동으로 식별할 수 있는 경량, 일반적인 통계 프로파일링 프레임워크(ICQ)를 소개한다.

