# Korean Three-Line Summarizations of Papers 1109-1186 in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track
###### Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track (https://aclanthology.org/2023.emnlp-industry.0/)
- Anthology ID: 2023.emnlp-industry.0 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors:  
- Summary: 
    요약문을 생성할 수 없습니다.

###### BeautifulPrompt: Towards Automatic Prompt Engineering for Text-to-Image Synthesis (https://aclanthology.org/2023.emnlp-industry.1/)
- Anthology ID: 2023.emnlp-industry.1 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 텍스트-이미지 합성에서 Diffusion 기반 딥 생성 모델 (예 : Stable Diffusion)은 놀라운 결과를 보여주었지만, 현재의 텍스트-이미지 모델은 실제 응용 프로그램에 만족스러운 결과를 얻기 위해 사람들에 의한 여러 번의 문구 작업이 필요하다.
    2. 우리는 간단한 원시 설명에서 고품질 프롬프트를 생성하는 깊은 생성 모델인 BeautifulPrompt를 제안하며, 이를 통해 확산 기반 모델이 더 아름다운 이미지를 생성할 수 있다.
    3. 시각 AI 피드백과 강화 학습을 활용하여 모델을 세밀하게 조정하여 더 아름다운 이미지를 생성할 수 있는 프롬프트를 생성하고, 이를 클라우드 내 AI 플랫폼에 통합하여 더 나은 텍스트-이미지 생성 서비스를 제공하는 것을 보여준다.

###### Enhancing Language Model with Unit Test Techniques for Efficient Regular Expression Generation (https://aclanthology.org/2023.emnlp-industry.2/)
- Anthology ID: 2023.emnlp-industry.2 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 generative language models을 사용하여 시맨틱 기반의 정규 표현식을 생성하는 연구가 진행되었으나, 이러한 접근 방식은 기능적인 정확성에 문제가 있어 실제 적용에서의 한계가 있다.
    2. 이 논문에서는 Unit-Test Driven Reinforcement Learning (UTD-RL)라는 새로운 방법을 제안하는데, 기존 방법과는 다르게 기능적인 정확성을 중요한 측면으로 고려하고 정책 기울기 기술을 사용하여 가중 피드백으로 변환한다.
    3. 실험 결과, 제안된 방법은 정규 표현식 생성에서 효과적이며, 그 결과는 규제 시나리오에서도 적용되어 관련 인원들의 작업 부하를 크게 줄일 수 있다.

###### A Comparative Analysis of Task-Agnostic Distillation Methods for Compressing Transformer Language Models (https://aclanthology.org/2023.emnlp-industry.3/)
- Anthology ID: 2023.emnlp-industry.3 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 NLP에서 상위 성능을 보이는 대형 언어 모델은 실제 개발에서 추론 비용 때문에 비효율적이다. 
    2. 본 연구에서는 Transformer 언어 모델의 과제-비구조(distillation)에 대한 대표적인 방법들을 재생산, 비교 및 분석하였다. 
    3. 결과적으로, MiniLMv2를 기반으로 한 MHA 전이는 일반적으로 가장 효과적이며, HS 전이는 sophisicated한 레이어 매핑 전략 아래에서 경쟁력 있는 베이스라인을 형성하는 것을 보였다.

###### Towards Effective Automatic Debt Collection with Persona Awareness (https://aclanthology.org/2023.emnlp-industry.4/)
- Anthology ID: 2023.emnlp-industry.4 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 채권자의 퍼스널리티를 이해하는 것은 채권자가 채무자와 공감하며 효과적인 수금 전략을 개발하는 데 중요하다.
    2. 본 연구는 채무자의 퍼스널리티의 중요성을 종합적으로 조사하고, 자동 채권 수금 에이전트에 대한 성공적인 상용 실천 사례를 제시한다.
    3. 퍼스널리티에 대한 대화 데이터셋을 구축하여 효과적인 에이전트를 구현한 결과, 수입률이 3.31% 증가하고 약 100,000위안의 추가 수금을 달성했다.

###### Gatekeeper to save COGS and improve efficiency of Text Prediction (https://aclanthology.org/2023.emnlp-industry.5/)
- Anthology ID: 2023.emnlp-industry.5 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 텍스트 예측 작업에서는 사용자가 제안을 수락할 때까지 거의 모든 문자마다 큰 언어 모델을 호출하는데, 이는 모델의 실행 비용을 높이고 정확하지 않은 예측까지 네트워크와 계산 비용을 발생시킨다. 
    2. 따라서 클라이언트 응용 프로그램 수준에서 잘못된 예측을 방지하기 위해 모델 게이트키퍼를 제안한다. 이를 통해 모델 호출 비용을 절약하고 잘못된 예측을 사용자에게 보여주지 않음으로써 사용자 경험을 향상시킬 수 있다.
    3. 모델 게이트키퍼의 사용으로 텍스트 예측 모델의 효율성이 약 73% 향상되고, COGS(임원 지출, 비용, 수익)를 약 46.6% 절약할 수 있었다.

###### Efficient Transformer Knowledge Distillation: A Performance Review (https://aclanthology.org/2023.emnlp-industry.6/)
- Anthology ID: 2023.emnlp-industry.6 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 사전 훈련된 transformer 언어 모델들이 최고 수준의 성능을 보이며, 모델 압축과 효율적인 어텐션 메커니즘에 대한 연구가 이루어졌다. 이 논문에서는 지식 증류를 통한 모델 압축에 대한 평가를 제시하고, 효율적인 어텐션 transformer의 압축에 따른 성능 향상을 연구한다. 
    2. 실험 결과, 훈련된 효율적인 어텐션 transformer는 원래 모델의 성능을 상당 부분 보존할 수 있으며, 추론 시간을 최대 57.8%까지 줄일 수 있다는 것을 발견했다.
    3. 지식 증류는 대부분의 모델과 대부분의 태스크에서 효과적인 방법으로 나타났으며, 저비용으로 높은 성능을 가진 효율적인 어텐션 모델을 얻는데 효과적인 방법으로 나타났다.

###### CDD: A Large Scale Dataset for Legal Intelligence Research (https://aclanthology.org/2023.emnlp-industry.7/)
- Anthology ID: 2023.emnlp-industry.7 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 인공지능의 중요한 응용 분야로 법률 지능이 많은 연구자들의 관심을 끌고 있다. 이 논문에서는 법정 판결 예측을 지원하는 연구를 위한 대규모 법정 토론 데이터셋(총 30,481건의 법정 사건)을 제안한다.
    2. 실제 법정 트라이얼에서 판사, 원고, 피고자들 간의 대화를 포함하는 이 데이터셋은 텍스트 요약, 대화 생성, 텍스트 분류 등 여러 다운스트림 태스크에 적용될 수 있다.
    3. 경험 있는 판사들에게 적절한 레이블을 설계하도록 초대한 후, 법학 학생들에게 정의된 레이블에 따라 주석을 달도록 요청하여 데이터셋을 구축했으며, 이를 통해 법률 지능 분야의 연구가 발전될 수 있다는 점과 그에 따른 성능 벤치마크 결과를 제공한다.

###### MUST&P-SRL: Multi-lingual and Unified Syllabification in Text and Phonetic Domains for Speech Representation Learning (https://aclanthology.org/2023.emnlp-industry.8/)
- Anthology ID: 2023.emnlp-industry.8 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 이 논문에서는 Montreal Forced Aligner (MFA)라는 강제 정렬 도구와 호환될 수 있는 언어적 특징 추출 방법론을 제시한다. 
    2. 텍스트와 음성적 도메인 양쪽에서, 우리의 방법론은 텍스트에서 음성적 문자를 추출하고 강세 기호와 통합된 자동 음절화를 중점적으로 한다.
    3. 우리는 영어, 프랑스어 및 스페인어 등 여러 언어의 단어를 자동 음절화하는 우리의 접근법의 효과를 연구를 통해 입증하였고, 또한 CMU ARCTIC 데이터셋의 전사에 이 기법을 적용하여 스피치 표현 학습, 스피치 유닛 탐색 및 스피치 관련 분야에서의 스피치 요소의 분리에 유용한 주석을 생성하였다.

###### Personalized Dense Retrieval on Global Index for Voice-enabled Conversational Systems (https://aclanthology.org/2023.emnlp-industry.9/)
- Anthology ID: 2023.emnlp-industry.9 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 음성 제어 AI 대화 시스템은 음운 변이와 모호한 개체 해결에 대한 노이즈에 영향을 받는데, 이러한 오류 모드에서 회복하기 위해 개인화된 개체 해결 (ER)과/또는 쿼리 재작성 (QR)이 사용된다. 
    2. 이 논문에서는 개인화된 인덱스에 대한 제약 없이 음성 노이즈와 모호성에 강한 개인화된 개체 검색 시스템을 제안한다. 
    3. 이를 위해 개인의 청취 선호도를 조건화한 상황적 쿼리 임베딩을 사용하여 개체 검색에 사용되며, 기준선에 비해 엔티티 검색 작업에서 91%의 성능 향상을 보였다.

###### Text2Topic: Multi-Label Text Classification System for Efficient Topic Detection in User Generated Content with Zero-Shot Capabilities (https://aclanthology.org/2023.emnlp-industry.10/)
- Anthology ID: 2023.emnlp-industry.10 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. Multi-label 텍스트 분류는 산업에서 매우 중요한 작업인데, 이 논문에서는 Bi-Encoder Transformer 아키텍처를 사용해 높은 분류 성능을 달성하며 zero-shot 예측과 도메인 특화 텍스트 임베딩, 대용량 배치 추론 등 여러 기능을 제공한다.
    2. Text2Topic은 Booking.com의 3개 주요 데이터 소스에서 약 120,000개의 텍스트를 사용하여 약 1.6백만 개의 텍스트-토픽 쌍 주석을 수집하였고, 이를 통해 다른 기법들과 비교했을 때 정확하고 포괄적인 결과를 달성했으며 실제 시스템에 배포되어 사용된다.
    3. 어떠한 모델링 선택지를 했는지, 어떤 테스트와 생산 단계 결정 사항이 있었는지 상세하게 정리되어 있다.

###### Deep Metric Learning to Hierarchically Rank - An Application in Product Retrieval (https://aclanthology.org/2023.emnlp-industry.11/)
- Anthology ID: 2023.emnlp-industry.11 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대부분의 전자상거래 검색 엔진은 고객 행동 신호를 사용하여 어휘적 일치를 보완하고 검색 관련성을 향상시키는데, 하지만 고객 행동 데이터가 희소한 새로운 상점에서는 문제가 발생한다. 이 논문에서는 상점 간의 중복 및 거의 중복 제품을 식별하는 모델을 개발하였다. 
    2. 제안된 모델은 세계적으로 제품 카탈로그를 유니파이하거나 제품 메타데이터를 개선하거나 검색 관련성을 향상하기 위해 거의 중복 제품을 활용할 수 있다.
    3. 제안된 방법은 다국어로 통합된 검색 및 순위 결합 방법을 통해 제품 유사도 계층 구조를 포착하고 우수한 성과를 보여준다는 점을 실험을 통해 확인하였다.

###### A Pretrained Language Model for Cyber Threat Intelligence (https://aclanthology.org/2023.emnlp-industry.12/)
- Anthology ID: 2023.emnlp-industry.12 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. CTI-BERT는 사이버보안 도메인에서의 CTI 추출 정확도를 개선하여 잠재적인 사이버 위협에 대한 조직의 방어 능력을 향상시킬 수 있는 새로운 BERT 모델을 제안한다.
    2. 이 논문에서는 사이버보안 도메인의 다양한 NLP 과제에 대한 도메인 말뭉치 수집, 훈련 방법 및 효과에 대한 자세한 정보를 제공한다.
    3. 실험 결과, CTI-BERT는 일반 도메인 및 보안 도메인 모델들보다 사이버보안 응용 프로그램에서 우수한 성능을 보이며, 훈련 데이터와 방법론이 모델 성능에 큰 영향을 미친다는 것을 보여준다.

###### SAMP: A Model Inference Toolkit of Post-Training Quantization for Text Processing via Self-Adaptive Mixed-Precision (https://aclanthology.org/2023.emnlp-industry.13/)
- Anthology ID: 2023.emnlp-industry.13 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. FasterTransformer와 TurboTransformers와 같은 최신 산업용 추론 엔진은 반정밀도 부동 소수점 (FP16) 및 8비트 정수 (INT8) 양자화가 모델 추론 속도를 크게 향상시킬 수 있다는 것을 검증하였다. 
    2. 그러나 기존의 INT8 양자화 방법은 너무 복잡하여 부적절한 사용으로 인해 모델 성능에 큰 손상을 유발한다. 
    3. 본 논문에서는 SAMP (Self-Adaptive Mixed-Precision)이라는 기술을 제안하여 혼합 정밀도 아키텍처를 통해 양자화 비율을 자동으로 제어하여 모델 정확성과 효율성을 균형있게 조절할 수 있도록 사용자가 모델을 쉽게 양자화할 수 있는 도구를 개발한다.

###### KD-Boost: Boosting Real-Time Semantic Matching in E-commerce with Knowledge Distillation (https://aclanthology.org/2023.emnlp-industry.14/)
- Anthology ID: 2023.emnlp-industry.14 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 웹 및 제품 검색에서 실시간 의미 일치가 중요한데, Transformer 기반 모델은 쿼리를 임베딩 공간으로 인코딩하여 의미적으로 유사한 엔티티들을 가까운 거리로 표현하는 데 높은 효과를 보여주었다.
    2. 그러나 대규모 Transformer 모델의 계산 복잡성으로 인해 실시간 일치에 제한이 있다. 이 논문에서는 실시간 의미 일치를 위한 새로운 지식 증류 알고리즘인 KD-Boost를 제안한다.
    3. KD-Boost는 선생님 모델로부터의 soft label과 직접적인 감사, 사용자 행동, 분류 기반 데이터로부터 파생된 쌍별 쿼리-제품 및 쿼리-쿼리 신호를 활용하여 낮은 대기 시간의 정확한 학생 모델을 훈련시킨다. KD-Boost를 사용한 모의 온라인 A/B 테스트에서는 6.31%의 쿼리 대 쿼리 일치 증가, 2.76%의 제품 커버리지 증가, 그리고 2.19%의 관련성 개선이 있었다.

###### Multi-teacher Distillation for Multilingual Spelling Correction (https://aclanthology.org/2023.emnlp-industry.15/)
- Anthology ID: 2023.emnlp-industry.15 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 현대의 검색 인터페이스에서 맞춤법 교정은 특히 모바일 기기와 음성 인식 인터페이스 시대에 중요한 단계이다. 전 세계에서 서비스가 배포되는 경우, 모든 언어에서 스펠링 오류를 잡고 수정해야 하는 중요한 과제로 거듭난다.
    2. 이 논문에서는 multi-teacher distillation을 사용하여 이 도전에 대처한다. 방법론은 각 언어/로캘에 대해 단일 언어 선생님 모델을 훈련시키고, 이러한 개별 모델을 모든 언어/로캘을 대상으로 하는 단일 다국어 학생 모델로 축약한다.
    3. 오픈 소스 데이터와 전 세계 검색 서비스의 고객 데이터를 사용한 실험에서, 우리는 효과적인 맞춤법 교정 모델을 얻을 수 있으며, 배포된 서비스의 엄격한 대기 시간 요구 사항을 충족시킬 수 있음을 보여준다.

###### Does Named Entity Recognition Truly Not Scale Up to Real-world Product Attribute Extraction? (https://aclanthology.org/2023.emnlp-industry.16/)
- Anthology ID: 2023.emnlp-industry.16 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 속성-값 추출 작업(AVE)의 주요 과제는 실제 전자 상거래 사이트에서 다양한 속성에 대한 대규모 제품에 확장 가능한 것이다. 최근 연구자들은 대상 속성을 추가로 입력하여 해당 속성의 값을 추출하는 질문-응답(QA) 기반 접근 방식을 도입하여, 전통적인 명명된 개체 인식(NER) 기반 접근 방식과 비교하여 이점을 확인하였다.
    2. 이 연구에서는 QA 기반 접근 방법을 평가하기 위해, BERT 기반 QA 모델을 판단 기준으로 세운 약한 BiLSTM 기반 NER 베이스라인과만 비교하였기 때문에 NER 기반 접근 방식의 확장 가능성을 논한다.
    3. 실제 데이터셋을 사용한 실험 결과, 공정한 설정에서 BERT 기반 NER 모델은 정확성 측면에서 BERT 기반 QA 모델과 어울릴 정도로 동등하며, 같은 제품 텍스트를 여러 번 처리하여 여러 대상 속성을 처리하는 QA 모델에 비해 추론 속도가 빠르다.

###### Investigating Table-to-Text Generation Capabilities of Large Language Models in Real-World Information Seeking Scenarios (https://aclanthology.org/2023.emnlp-industry.17/)
- Anthology ID: 2023.emnlp-industry.17 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 다양한 산업에서 널리 사용되는 표 형식의 데이터는 사용자가 정보를 찾고 조작하는 데 시간과 노력이 많이 필요하다. 
    2. 하지만 대용량 언어 모델 (LLM)의 발전은 사용자의 효율성을 향상시킬 수 있는 엄청난 잠재력을 보여주었으나, 표 정보 탐색에서의 LLM 활용은 아직 탐구되지 않고 있다.
    3. 이 논문에서는 실제 정보 탐색 시나리오에서 다양한 LLM의 표-텍스트 능력을 조사하고, GPT-4를 포함한 다른 LLM과의 성능 차이를 밝히고 있다.

###### TMID: A Comprehensive Real-world Dataset for Trademark Infringement Detection in E-Commerce (https://aclanthology.org/2023.emnlp-industry.18/)
- Anthology ID: 2023.emnlp-industry.18 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 상표권 침해를 탐지하기 위한 새로운 데이터셋인 TMID가 소개되었으며, 이는 Alipay와 같은 세계 최대의 전자상거래와 디지털 결제 플랫폼에서 직접 수집된 실제 데이터이다.
    2. 이 데이터셋은 법적 추론 작업으로, 문맥과 법적 규칙을 이해하는 것을 요구하는데, 법률 전문가들의 주석과 함께 상인 및 상표 관련 문맥 정보의 철저한 수집을 제공한다.
    3. 통계적 분석을 수행하여 데이터 품질을 보장하며, 이 데이터셋을 활용한 실험을 통해 이의 가치와 주요 도전 과제를 강조한다.

###### Joint Dialogue Topic Segmentation and Categorization: A Case Study on Clinical Spoken Conversations (https://aclanthology.org/2023.emnlp-industry.19/)
- Anthology ID: 2023.emnlp-industry.19 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 자연어 처리 기술을 이용하여 임상 대화를 처리하는 것은 의료진과 환자의 건강관리 업무의 효율성을 향상시키는 데 효과적이다.
    2. 일반화된 모델이 도메인 특정 응용 프로그램에 즉시 적용되지 않는다. 이는 분할 세분화와 주제 정의의 다양성, 다양한 주석이 된 코퍼스의 부족으로 인해 발생한다.
    3. 이 논문에서는 대화 분할과 주제 분류를 위해 공통 모델을 도입하고 당뇨병 관리를 위한 의료 후속 전화에 대한 사례 연구를 진행한다. 성능과 견고성에 대한 데이터와 모델 관점에서 통찰력을 제공한다.

###### AdapterDistillation: Non-Destructive Task Composition with Knowledge Distillation (https://aclanthology.org/2023.emnlp-industry.20/)
- Anthology ID: 2023.emnlp-industry.20 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근에는 "어댑터"라고 불리는 각 transformer layer에 일부 작업 특정 파라미터들을 추가하여 여러 작업의 지식을 활용하는 것이 큰 관심을 받고 있다. 그러나 지식 합성을 구현하기 위해 추가적인 퓨전 레이어를 추가하는 것은 추론 시간을 증가시키고 일부 응용 프로그램에서는 확장성이 없다. 이런 문제를 피하기 위해 우리는 AdapterDistillation이라고 불리는 두 단계의 지식 전달 알고리즘을 제안한다.
    2. 첫 번째 단계에서는 로컬 데이터를 사용하여 학생 어댑터를 훈련하여 작업별 지식을 추출한다. 두 번째 단계에서는 기존의 교사 어댑터로부터 학생 어댑터로 지식을 전달하여 추론을 도와준다.
    3. 작업 지향적 대화 시스템에서 자주 사용되는 질문 검색 작업에 대한 실험 결과, AdapterDistillation의 효율성이 입증되었다. 정확도, 리소스 소비 및 추론 시간 측면에서 AdapterDistillation이 기존 알고리즘보다 우수한 성능을 보여준다.

###### PROMINET: Prototype-based Multi-View Network for Interpretable Email Response Prediction (https://aclanthology.org/2023.emnlp-industry.21/)
- Anthology ID: 2023.emnlp-industry.21 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. "이메일은 비즈니스 커뮤니케이션에서 널리 사용되는 도구이며, 이메일 마케팅은 기업에게 비용 효과적인 전략으로 부상하고 있다. 그러나 이전 연구들은 이메일 마케팅 성과에 영향을 미치는 요소들을 조사해 왔지만, 이메일 콘텐츠와 메타데이터를 고려한 이메일 반응 행동을 이해하는 데 제한된 연구가 있었다."
    2. 이 연구는 이메일 데이터에서 의미론적 및 구조적 정보를 포함하는 프로토타입 기반 멀티뷰 네트워크 (PROMINET)를 제안한다. PROMINET 모델은 프로토타입 학습을 활용하여 해석 가능한 이메일 응답 예측을 가능하게 한다. 모델은 문서, 문장 또는 구문과 같은 다양한 정밀도 수준에서 학습된 의미론적 및 구조적 인스턴스를 훈련 데이터의 관찰된 샘플과 매핑한다.
    3. 실험 결과 PROMINET 모델은 기준 모델에 비해 F1 점수에서 약 3%의 성능 향상을 보이며, 해석 가능한 모델과 비교 가능한 성능을 유지하면서 다양한 정밀도 수준의 프로토타입을 통해 해석 가능성을 제공한다. 학습된 프로토타입은 이메일 텍스트 편집을 향상시키고 효과적인 이메일 응답 가능성을 향상시키기 위한 제안 생성의 잠재력도 보여준다. 이 연구는 이메일 상호작용에서 발신자-수신자 커뮤니케이션과 고객 참여를 향상시키는 데 기여한다."

###### Retrieval-Enhanced Dual Encoder Training for Product Matching (https://aclanthology.org/2023.emnlp-industry.22/)
- Anthology ID: 2023.emnlp-industry.22 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 판매자가 상품을 올렸을 때 적절한 상품과 매칭하는 것은 전자상거래 플랫폼에게 중요한 과제이며, 대규모 환경에서 효율적으로 실행되어야 한다.
    2. 최근에는 두 개의 인코더를 사용하는 방식이 높은 성능과 계산 효율성으로 인해 상품 매칭에서 일반적인 접근법이 되었다.
    3. 본 논문에서는 두 단계의 훈련을 제안하며, 첫 번째 단계에서는 더 정보가 많은 훈련 데이터를 식별하는 데에 드우며, 두 번째 단계에서는 효과적인 데이터로 학습하여 더 나은 인코더 모델을 만든다.

###### WordArt Designer: User-Driven Artistic Typography Synthesis using Large Language Models (https://aclanthology.org/2023.emnlp-industry.23/)
- Anthology ID: 2023.emnlp-industry.23 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. WordArt Designer는 사용자 중심의 예술적 타이포그래피 합성을 위한 프레임워크이다. Large Language Model (LLM)과 네 가지 핵심 모듈로 구성되어 있다.
    2. LLM 엔진은 사용자 입력을 해석하고 다른 모듈에 대한 작업 가능한 프롬프트를 생성하여 추상적인 개념을 구체적인 디자인으로 변환한다.
    3. SemTypo 모듈은 읽기 가능성과 예술적 변환 사이의 균형을 고려하여 의미적 개념을 활용하여 폰트 디자인을 최적화한다. StyTypo 모듈은 SemTypo 모듈이 제공한 의미적 레이아웃을 기반으로 부드럽고 정제된 이미지를 생성한다. TexTypo 모듈은 텍스처 렌더링을 통해 디자인의 미적인 요소를 강화하여 창의적인 텍스처 폰트를 생성한다.

###### Lattice Path Edit Distance: A Romanization-aware Edit Distance for Extracting Misspelling-Correction Pairs from Japanese Search Query Logs (https://aclanthology.org/2023.emnlp-industry.24/)
- Anthology ID: 2023.emnlp-industry.24 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 검색 쿼리 로그로부터 스펠링 교정 모델의 학습 데이터인 오탈자-정정 짝을 추출하는 데 성공한 것은 편집 거리의 영향이다. 그러나 이는 일본어에 적용하기 어렵다. 
    2. 일본어에서 오탈자는 주로 로마자 기반의 입력 방법 때문에 올바른 스펠링과 다름이 많기 때문이다.
    3. 이 문제를 해결하기 위해 로마자 라티스 경로 편집 거리를 소개하고, 로마자 라티스를 활용하여 입력 문자열의 모든 로마자 형태를 효율적으로 고려한다.

###### Learning Multilingual Sentence Representations with Cross-lingual Consistency Regularization (https://aclanthology.org/2023.emnlp-industry.25/)
- Anthology ID: 2023.emnlp-industry.25 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 다국어 문장 표현은 다국어 신경 기계 번역(NMT) 시스템을 더 많은 언어로 확장하기 위한 중요한 요소이다.
    2. 이 논문에서는 223개 언어를 지원하는 MuSR(Multilingual Sentence Representation) 모델을 소개한다. 수십억 개의 영어 중심 병렬 문장 데이터를 활용하여 transformer encoder와 auxiliary transformer decoder를 훈련시킨다.
    3. 실험 결과는 MuSR이 148개 독립적인 다국어 문장 인코더로 구성된 LASER3보다 우수한 성능을 보여준다.

###### Unveiling Identity Biases in Toxicity Detection : A Game-Focused Dataset and Reactivity Analysis Approach (https://aclanthology.org/2023.emnlp-industry.26/)
- Anthology ID: 2023.emnlp-industry.26 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 주로 성별이나 인종적 편향에 초점을 둔 기존 bias benchmarking 데이터셋은 게임 채팅의 독성 감지를 위해 만들어진 모델에는 적합하지 않은 문제였으며, 이러한 과민한 용어를 강조하기 위한 데이터셋과 방법을 제안한다.
    2. 우리는 reactivity analysis와 모델의 성능을 활용하여 과민한 용어를 강조하는 데이터셋과 방법을 개발하였다.
    3. 우리의 실험 결과, 독성 모델들이 이미 어려움을 겪는 그룹의 존재를 알리지 못하게 하거나 성숙한/정상적인 대화를 할 수 없게 하는 공동체의 정체성과 관련된 용어를 자동으로 독성으로 분류하는 경우가 많다는 것을 발견하였다.

###### ORANGE: Text-video Retrieval via Watch-time-aware Heterogeneous Graph Contrastive Learning (https://aclanthology.org/2023.emnlp-industry.27/)
- Anthology ID: 2023.emnlp-industry.27 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. TikTok과 YouTube와 같은 산업용 비디오 공유 플랫폼에서 짧은 영상 데이터가 폭발적으로 증가함에 따라, 텍스트-비디오 검색 기술은 점점 중요해지고 있다.
    2. 기존의 텍스트-비디오 검색 작업은 질문과 비디오 자체의 내용 정보(질문의 텍스트 정보 및 비디오의 복합 정보)를 활용하는 정보성 표현 및 매칭 메커니즘에 초점을 맞추고 있다. 
    3. 하지만 현실적인 상황에서는 간단하고 모호한 질문과 저화질 비디오가 많아서 내용 기반 검색이 효과적이지 못하다. 이 논문은 이러한 다양한 검색 요구를 수용하고 사용자 만족도를 향상시키기 위해 새로운 텍스트-비디오 검색 방법인 ORANGE를 소개한다.

###### Compute-Efficient Churn Reduction for Conversational Agents (https://aclanthology.org/2023.emnlp-industry.28/)
- Anthology ID: 2023.emnlp-industry.28 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. "모델의 변동(churn)은 같은 데이터와 하이퍼파라미터를 사용하더라도 재학습 시 다른 예측 결과가 나타날 때 발생한다. 이러한 변동을 줄이는 것은 사용자가 동일한 쿼리에 대해 일관된 결과를 기대하는 산업용 대화 시스템에서 중요하다."
    2. "우리는 추가적인 자원을 요구하지 않으면서도 변동을 완화하는 계산 효율적인 방법을 제안한다. 이 방법은 '함수 호출 서명'을 기반으로 의미 파싱을 짝지움으로써 가벼운 데이터 전처리 단계를 수행하고, Jensen-Shannon Divergence를 기반으로 한 추가적인 손실을 통해 유사성을 촉진한다."
    3. "우리는 학술(평균 3.93%의 변동 감소 메트릭 개선), 시뮬레이션된 잡음 데이터(8.09%), 산업(5.28%) 환경에서 우리의 방법의 효과를 검증하였다."

###### Empower Large Language Model to Perform Better on Industrial Domain-Specific Question Answering (https://aclanthology.org/2023.emnlp-industry.29/)
- Anthology ID: 2023.emnlp-industry.29 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대형 언어 모델 (LLM)은 개방형 도메인 작업에서 높은 성능을 보여주었으나, 실제 산업 분야에서 도메인 특정 지식 부족으로 평균적인 성능을 보인다. 
    2. 이 논문에서는 Microsoft 제품과 고객이 마주치는 IT 기술 문제를 중심으로 한 MSQA라는 벤치마크 QA 데이터셋을 제공한다. 
    3. 이 데이터셋은 일반 LLM에서는 제대로 다루지 않는 산업 클라우드 특정 QA 지식을 포함하고 있어서 LLM의 도메인 특정 능력을 향상시키고자 하는 방법을 평가하는 데 적합하다.
    
    주어진 paper에서는 Microsoft 제품과 IT 기술 문제를 다루는 산업 분야에 대한 벤치마크 데이터셋인 MSQA를 제공하고, 이 데이터셋을 활용하여 LLM의 도메인 특정 능력을 향상시키는 방법을 제안하고 실험 결과를 보여준다.

###### Enhancing Extreme Multi-Label Text Classification: Addressing Challenges in Model, Data, and Evaluation (https://aclanthology.org/2023.emnlp-industry.30/)
- Anthology ID: 2023.emnlp-industry.30 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. Extreme multi-label text classification은 산업에서 흔한 작업이지만, 일반적인 SciBERT 기반 분류 모델의 한계, 데이터 부족 문제, 시간이 소요되는 평가와 같은 기계 학습 측면에서 많은 도전을 겪는다.
    2. 우리는 두 가지 혁신적인 접근 방식을 제시하여 이러한 문제를 완화하고자 한다. 먼저, 대규모 레이블을 효율적으로 처리하고 새로운 레이블을 수용할 수 있는 레이블 순위 모델을 제안한다.
    3. 또한, 분류 시스템의 업데이트 과정에서 새로운 레이블의 데이터 부족 문제를 해결하기 위한 액티브 러닝 기반 파이프라인을 제안하고, ChatGPT를 통해 모델 평가를 보조하는 방식을 소개한다. 실험 결과는 이러한 기술들이 extreme multi-label text classification 작업을 향상시키는 데 효과적임을 보여준다.

###### Query-aware Multi-modal based Ranking Relevance in Video Search (https://aclanthology.org/2023.emnlp-industry.31/)
- Anthology ID: 2023.emnlp-industry.31 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 비디오 검색에서 중요도 순위 시스템은 스트리밍 플랫폼에서 중요한 역할을 한다. 
    2. 이 논문에서는 텍스트 모달리티에 초점을 맞춘 relevance ranking 방법들이 비디오 내에 존재하는 cross-modal 정보를 완전히 활용하지 못한다는 문제점이 있다고 분석하였다. 
    3. 이를 해결하기 위해, 우리는 query 정보를 정렬 타겟으로 활용하는 모델인 QUALITY를 제안하고, 이를 relevance ranking 모델에 통합하여 다중 모달 지식을 활용하고 순위 최적화 방법을 향상시켰다.

###### Coordinated Replay Sample Selection for Continual Federated Learning (https://aclanthology.org/2023.emnlp-industry.32/)
- Anthology ID: 2023.emnlp-industry.32 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 지속적 페더레이티드 학습(CFL)은 페더레이티드 학습(FL)과 계속적 학습(CL)을 결합한 것으로, 여러 클라이언트 장치에서 중앙 모델을 학습하되 데이터를 공유하지 않는 구조를 가진다.
    2. 이 논문에서는 줄줄이 새로운 데이터가 들어올 때 기존 데이터를 잊는 것이 주요 과제로 제시되고 있다.
    3. 지난 연구에서는 단순한 재생 샘플 선택 전략만 CFL에 적용되었으며, 클라이언트 간 협력을 통한 더 나은 샘플 선택은 고려되지 않았다. 이 논문에서는 샘플 선택 목적을 최적화하기 위해 그래디언트 기반의 재생 샘플 선택 방법과 데이터를 공유하지 않으면서 클라이언트 간 그래디언트 기반의 재생 샘플 선택을 조정하는 알고리즘을 제안하고 있다.

###### Building Real-World Meeting Summarization Systems using Large Language Models: A Practical Perspective (https://aclanthology.org/2023.emnlp-industry.33/)
- Anthology ID: 2023.emnlp-industry.33 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 본 논문은 대규모 언어 모델(Large Language Model; LLM)을 사용하여 현실 세계에서 회의 요약 시스템을 효과적으로 구축하는 방법을 연구한다.
    2. 대다수의 상용 LLM은 일반적으로 더 나은 성능을 보이지만, 작은 오픈 소스 모델인 LLaMA-2 (7B 및 13B)는 제로샷 시나리오에서도 대형 상용 모델과 비교 가능한 성능을 달성할 수 있다.
    3. 성능과 연관된 비용 및 개인 정보 보호 문제를 균형있게 고려할 때, LLaMA-2-7B 모델이 산업용으로 더 유망하다. 총론적으로, 이 논문은 실제 비즈니스 회의 요약에 LLM을 사용하는 데 대한 실용적인 통찰력을 제공하며, 성능과 비용 사이의 트레이드오프에 대한 양면의 조명을 한다.

###### Creator Context for Tweet Recommendation (https://aclanthology.org/2023.emnlp-industry.34/)
- Anthology ID: 2023.emnlp-industry.34 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 트윗을 논할 때 사람들은 주로 그 내용에 대한 언급뿐 아니라 트윗의 작성자에 관해서도 언급한다. 다시 말해, 트윗의 해석을 작성자의 맥락에 근거하여 해독하는 것이 트윗의 진짜 의도와 중요성을 파악하는 데 중요한 역할을 한다.
    2. 이 논문에서는 트윗 이해를 발전시키기 위해 작성자의 맥락을 어떻게 사용해야 하는지에 대한 질문에 대답하려고 한다. 특히, 다양한 유형의 작성자 맥락의 유용성을 조사하고 트윗 모델에 작성자 맥락을 통합하기 위한 다양한 모델 구조를 검토한다.
    3. 우리는 트윗 이해 모델을 실용적인 사례인 뉴스 기사에 관련 트윗을 추천하는 데에 적용하여 평가한다. 이 경우는 이미 인기있는 뉴스 앱에 존재하며, 기자들에게 유용한 보조 도구 역할도 할 수 있다. 우리는 작성자 맥락이 트윗 이해에 필수적이며, 응용 프로그램 지표를 크게 개선시킬 수 있다는 것을 발견했다. 그러나 모든 작성자 맥락이 동일하지는 않다는 것도 관찰되었다. 작성자 맥락은 시간에 민감하고 노이즈가 될 수 있다. 신중한 작성자 맥락 선택과 모델 구조 설계는 작성자 맥락의 효과적인 활용에 중요한 역할을 한다.

###### AdaBERT-CTC: Leveraging BERT-CTC for Text-Only Domain Adaptation in ASR (https://aclanthology.org/2023.emnlp-industry.35/)
- Anthology ID: 2023.emnlp-industry.35 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. E2E 자동 음성 인식(ASR) 모델은 가상 어시스턴트, 자막, 딕테이션 시스템 등 상업적 응용분야에서 점점 인기를 끌고 있다. 그러나 E2E 모델은 여전히 명사나 도메인 특정 용어와 같은 도메인 외 단어를 인식하는 데 어려움을 겪고 있다. 
    2. 본 논문에서는 텍스트 데이터만을 활용하는 도메인 적응 기술인 AdaBERT-CTC를 소개한다. 우리의 방법은 사전 학습된 self-supervised 텍스트 인코더 모델을 fine-tuning하여 텍스트만으로 적응을 가능하게 한다. 
    3. 또한, 우리의 방법은 사전 학습 모델에 bottleneck 어댑터를 추가함으로써 파라미터를 효율적으로 관리할 수 있다. 이를 통해 파라미터 증가량이 5% 미만이며 추론 시 최소한의 계산 비용만 발생한다. 여러 도메인 외, 공개 데이터셋을 기반으로 실험 결과, 우리의 접근 방식이 기본 BERT-CTC 모델 대비 14%까지 상대적인 단어 오류율 개선을 얻을 수 있음을 보여주었다.

###### Conversing with databases: Practical Natural Language Querying (https://aclanthology.org/2023.emnlp-industry.36/)
- Anthology ID: 2023.emnlp-industry.36 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 본 논문에서는 DataQue라는 하이브리드 NLQ 시스템을 개발하여 대화식 DB 질의를 수행한다. 이 시스템은 고객의 다양한 실제적인 문제를 해결하기 위해 설계되었으며, 사용자 질문에 포함된 다양한 복잡한 implicit 조건, 용어와 약어, 사용자 정의 계산, SQL이 아닌 연산 등을 처리할 수 있다.
    2. DataQue는 텍스트를 SQL로 번역하기 위해 10-15개의 모델 기반 및 규칙 기반 컴포넌트로 구성된 처리 파이프라인을 사용하여 처리를 정확하게 제어할 수 있다.
    3. 이 시스템은 빠른 시간 내에 파이프라인에 이를 수 있도록 하고, 요구 사항이 높은 사용자에게 확실한 파싱 결과를 제공하는 등 다양한 실제적인 문제를 해결할 수 있는 기능을 제공한다.

###### AART: AI-Assisted Red-Teaming with Diverse Data Generation for New LLM-powered Applications (https://aclanthology.org/2023.emnlp-industry.37/)
- Anthology ID: 2023.emnlp-industry.37 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대규모 언어 모델에 적용되는 공격적인 테스트는 그들의 안전한 전개를 위해 중요하다. 이 논문은 LLM(대규모 언어 모델)이 새로운 하위 응용 프로그램에서 안전성을 테스트하기 위해 적대적인 평가 데이터셋을 자동으로 생성하는 AI 보조 접근법을 소개한다.
    2. 이 논문에서는 AART (AI 보조 레드팀)라고 불리는 자동 팀테스팅 시스템을 소개하고 있다. 이 시스템은 인간의 노력을 크게 줄이고 적대적인 테스트를 신제품 개발 초기에 통합할 수 있는 재사용 가능하고 맞춤 설정 가능한 데이터 생성 및 증강 파이프라인을 제공한다.
    3. AART는 다양한 문화적 지역과 응용 프로그램 시나리오에 특정한 민감하고 해로운 개념들을 포함하는 평가 데이터셋을 생성하며, AI 보조 레시피를 사용하여 새로운 응용 프로그램 문맥에서 다양성을 정의, 범위화 및 우선순위를 지정한다.

###### Speakerly: A Voice-based Writing Assistant for Text Composition (https://aclanthology.org/2023.emnlp-industry.38/)
- Anthology ID: 2023.emnlp-industry.38 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. Speakerly는 email, 인스턴트 메시지, 노트 등 다양한 사용 사례에서 사용자가 텍스트를 작성하는 데 도움을 주는 새로운 실시간 음성 기반 작성 지원 시스템을 제공한다.
    2. 사용자는 지시나 딕테이션을 통해 시스템과 상호 작용하고, 시스템은 잘 정리되고 일관성 있는 문서를 생성한다.
    3. 작은 task-specific 모델과 미리 학습된 언어 모델을 조합하여 시스템은 빠르고 효과적인 텍스트 작성을 지원하며, 더 나은 사용성을 위해 다양한 입력 모드를 지원한다.

###### Are ChatGPT and GPT-4 General-Purpose Solvers for Financial Text Analytics? A Study on Several Typical Tasks (https://aclanthology.org/2023.emnlp-industry.39/)
- Anthology ID: 2023.emnlp-industry.39 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근의 대규모 언어 모델들은 ChatGPT와 GPT-4와 같이 일반화 능력이 뛰어난 모델로서, 적은 수정 없이 다양한 NLP 태스크에서 최고 수준의 성능을 보여주고 있다. 이러한 모델들이 금융 도메인에서 얼마나 효과적인지 알아보는 것은 다양한 금융 텍스트 분석 작업에 중요한 영향을 줄 수 있다.
    2. 본 논문에서는 5개 범주의 태스크에서 비교 실험을 통해 8개 벤치마크 데이터셋을 사용하여 금융 텍스트 분석 문제에서의 성능을 계량한 경험적 연구를 수행한다.
    3. 또한, 저자들은 모델을 최신 fine-tuned 접근법과 최근 출시된 도메인 특정 pretrained 모델들과 비교하여 현재 모델들의 강점과 한계를 보고하며, 이를 통해 기존 모델들의 금융 도메인 역량을 이해하고 더 나은 성능을 도모할 수 있기를 희망한다.

###### CL-QR: Cross-Lingual Enhanced Query Reformulation for Multi-lingual Conversational AI Agents (https://aclanthology.org/2023.emnlp-industry.40/)
- Anthology ID: 2023.emnlp-industry.40 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. Alexa, Google 어시스턴트, Siri와 같은 대화형 AI 에이전트의 인기 증가로 정확한 음성 언어 이해를 필요로 하고 있다. 
    2. 하지만 QR(Query Reformulation)은 언어 리소스 부족으로 non-English 사용자에게 고품질의 QR을 제공하는 것이 여전히 어려운 과제로 남아있다. 
    3. 이 논문에서는 영어의 풍부한 리포매퓰레이션 리소스를 활용하여 non-English QR 성능을 개선하기 위한 클로싱귤 QR(CL-QR) 프레임워크를 제안한다.

###### Improving Contextual Query Rewrite for Conversational AI Agents through User-preference Feedback Learning (https://aclanthology.org/2023.emnlp-industry.41/)
- Anthology ID: 2023.emnlp-industry.41 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. Conversational AI 에이전트에서는 Contextual query rewriting (CQR)이 중요한 구성 요소로 작용하여 이전 사용자-에이전트 대화의 문맥 정보를 활용하여 현재 사용자 의도를 더 잘 이해할 수 있도록 한다.
    2. 기존 CQR 방법은 사용자 피드백을 활용하여 사용자 선호도에 맞춘 쿼리 재작성을 학습할 수 있는 기회를 놓치는 경향이 있다.
    3. 본 논문에서는 Preference Aligned Contextual Query Rewriting (PA-CQR) 프레임워크를 제안하고, 다양한 최신 피드백 학습 알고리즘의 CQR 작업에 대한 효과를 조사하였다. 또한, 대규모 CQR 학습에 Dynamic Direct Preference Optimization (Dynamic DPO) 알고리즘을 적용하도록 개선된 알고리즘을 제안하였다.

###### Scaling Neural ITN for Numbers and Temporal Expressions in Tamil: Findings for an Agglutinative Low-resource Language (https://aclanthology.org/2023.emnlp-industry.42/)
- Anthology ID: 2023.emnlp-industry.42 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. ITN 작업은 방언, 전사 오류 등으로 인해 단어의 철자 변형으로 인해 ITN 항목을 식별하는 데 어려움이 있다.
    2. 타밀어는 음운 형태론적 변형인 Punarchi로 인해 문장에서 인접한 단어 사이의 단어 경계가 모호해진다.
    3. 실험 결과, 부트스트래핑과 데이터 증강을 통해 추가 데이터를 사용하는 s2s 모델이 최적의 성능을 보이며, fully-supervised 설정 대비 20.1%의 향상을 보고한다.

###### EELBERT: Tiny Models through Dynamic Embeddings (https://aclanthology.org/2023.emnlp-industry.43/)
- Anthology ID: 2023.emnlp-industry.43 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. EELBERT는 transformer 기반 모델 (예: BERT)을 압축하는 방법으로, downstream 태스크 정확도에 미치는 영향이 최소화되도록 설계되었다.
    2. 이 방법은 모델 크기를 크게 줄여주기 위해 모델의 입력 임베딩 레이어를 동적인 계산으로 대체하여 성취된다. 
    3. 실험 결과, EELBERT 모델은 전통적인 BERT 모델과 비교하여 미미한 성능 하락만을 보이며, 최소한의 크기로 GLUE 점수를 달성할 수 있는 UNO-EELBERT 모델을 개발하였다.

###### Gold Standard Bangla OCR Dataset: An In-Depth Look at Data Preprocessing and Annotation Processes (https://aclanthology.org/2023.emnlp-industry.44/)
- Anthology ID: 2023.emnlp-industry.44 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 본 연구 논문은 방글라 문자 인식(OCR) 시스템의 개선을 위해 방글라 텍스트 구조의 복잡성, 다양한 필체 스타일 및 종합 데이터셋의 부족에 대한 도전에 대처하기 위한 것이 목적이다. 
    2. 최근 딥러닝과 OCR 기술의 발전을 활용하여, 다양한 종류의 라벨이 달린 방글라 텍스트 이미지 데이터셋을 활용하여 방글라 OCR의 성능을 크게 향상시킬 것으로 기대된다.
    3. 이 연구는 400만 개가 넘는 인간 주석 이미지로 구성된 가장 광범위한 방글라 문자 및 단어 골드 표준 말뭉치를 소개하며, 이 데이터셋을 공개함으로써 방글라 OCR 및 관련 분야의 추가 연구 및 개발을 용이하게 할 것이다.

###### PILLOW: Enhancing Efficient Instruction Fine-tuning via Prompt Matching (https://aclanthology.org/2023.emnlp-industry.45/)
- Anthology ID: 2023.emnlp-industry.45 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 기존의 instruction tuning 기술은 대규모 언어 모델을 다양한 태스크에 적응시키는 데 사용되었지만, 계산 리소스가 많이 필요하여 개인이나 소규모 기관에서 실제로 사용하기 어려웠다.
    2. 최근에는 리소스 부담을 줄인 LoRA (Low-Rank Adaptation)이라는 대안이 등장했지만, LoRA의 성능을 만족시키기는 어려운 문제가 있다.
    3. 이 논문에서는 PILLOW라는 방법을 제안하여 제한된 리소스 환경에서 reinforcement learning을 통해 LLM의 in-context learning 능력을 활용하여 LoRA의 성능을 향상시키는 것을 목표로 한다.

###### Welcome to the Real World: Efficient, Incremental and Scalable Key Point Analysis (https://aclanthology.org/2023.emnlp-industry.46/)
- Anthology ID: 2023.emnlp-industry.46 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. "Key Point Analysis (KPA)는 의견 집합에서 주요 요점을 추출하고 그 보편성을 정량화하는 요약 프레임워크로, 이는 논쟁, 사용자 리뷰, 설문 응답과 같은 다양한 유형의 데이터에 성공적으로 적용되었다."
    2. 그러나 KPA 시스템을 실제로 구현하는데 필요한 실용적인 도전과제에 대한 주목은 아직 그리 높지 않다.
    3. 이 논문은 우리 조직 내의 여러 팀에 정기적으로 서비스되는 KPA 시스템을 발표하며 시스템 구축 중 마주친 주요 도전과제, 아키텍처 및 알고리즘적 개선사항에 대해 논의한다.

###### Automatic Linking of Judgements to UK Supreme Court Hearings (https://aclanthology.org/2023.emnlp-industry.47/)
- Anthology ID: 2023.emnlp-industry.47 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 영국에서 가장 중요한 법적 자료 중 하나는 국가의 최고 법원에서 판결된 사건에 대한 특판과 법정 속기 및 녹화 영상이다.
    2. 이 연구에서는 법적 논의에서 중요한 인용구들에 대한 연구를 위해 텍스트 판결서의 세그먼트를 영상의 시간부분과 연결하는 자동 도구를 구축하는데 초점을 맞췄다. 
    3. 우리는 AI 생성 기술을 사용하여 관련 링크를 검색하고, GPT 텍스트 임베딩을 우리 데이터셋에 맞게 사용하면 링킹 시스템의 최고 정확도를 달성할 수 있다는 것을 보였다.

###### Automatic Marketing Theme and Commodity Construction System for E-commerce (https://aclanthology.org/2023.emnlp-industry.48/)
- Anthology ID: 2023.emnlp-industry.48 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 소비자들의 쇼핑 필요성이 집중될 때 특정 마케팅 테마 아래의 상품 모음에 더 관심이 있다. 따라서 마케팅 테마와 해당 상품 모음을 탐지하면 고객이 쇼핑 비용을 절약하고 추천 시스템의 사용자 클릭 및 구매를 개선할 수 있다.
    2. 기존 시스템은 전문가들이 마케팅 테마를 작성하고 관련 상품을 선택하도록 요구하지만 대량 생산, 신속성 및 저온 표시와 같은 문제가 있다.
    3. 이 논문에서는 우리는 자동 마케팅 테마 및 상품 구축 시스템을 제안하여 마케팅 테마를 자동으로 생성하고 관련 상품을 선택할 수 있으며, 추천 시스템에서 테마의 온라인 효과성을 향상시킬 수 있다는 것을 보여준다.

###### Towards Safer Operations: An Expert-involved Dataset of High-Pressure Gas Incidents for Preventing Future Failures (https://aclanthology.org/2023.emnlp-industry.49/)
- Anthology ID: 2023.emnlp-industry.49 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 본 논문은 safety prevention을 위한 새로운 IncidentAI 데이터셋을 소개한다. 기존 코퍼스와는 달리, 이 데이터셋은 named entity recognition, cause-effect extraction, information retrieval 등 세 가지 작업으로 구성되어 있다.
    2. 이 데이터셋은 실무 경험을 가진 도메인 전문가들에 의해 주석이 달렸으며, 이를 통해 사고 예방 시나리오에서의 유용성을 검증하였다.
    3. 세 가지 작업을 위한 초기 결과는 사고 보고서를 분석하는 NLP 기술이 미래의 실패를 예방하는 데 도움이 된다는 것을 보여주며, 해당 데이터셋은 NLP 및 사고 관리 커뮤니티에서의 미래 연구를 용이하게 한다.

###### An Auxiliary Task Boosted Multi-task Learning Method for Service Account Retrieval with Limited Human Annotation (https://aclanthology.org/2023.emnlp-industry.50/)
- Anthology ID: 2023.emnlp-industry.50 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 공식 계정 및 미니 프로그램을 포함한 서비스 계정은 사용자에게 다양한 편의 서비스를 제공하며 애플리케이션의 중요한 구성 요소가 되었다. 그러나 이 작업은 인간 주석의 한계로 인해 어렵다. 
    2. 이 논문에서는 로그 데이터를 보조로 활용하여 본래 작업인 서비스 계정 검색의 성능을 향상시키는 여러 보조 작업을 도입한 새로운 접근 방식을 제안한다.
    3. 또한 Adaptive Hierarchical Fusion Module (AHF module)을 도입하여 여러 보조 작업의 임베딩을 주 작업에 유연하게 통합함으로써 모델의 효과를 향상시킨다.

###### VKIE: The Application of Key Information Extraction on Video Text (https://aclanthology.org/2023.emnlp-industry.51/)
- Anthology ID: 2023.emnlp-industry.51 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 비디오에서 구조화된 정보를 추출하는 것은 산업에서 많은 하위 응용프로그램에 대해 중요하다. 본 논문에서는 비디오의 시각적 텍스트에서 계층적인 중요 정보를 추출하는 작업을 정의한다.
    2. 이 작업을 수행하기 위해, 논문에서는 4가지 하위 작업으로 분리하여 PipVKIE와 UniVKIE라는 두 가지 구현 솔루션을 소개한다.
    3. PipVKIE는 연속적인 단계에서 4가지 하위 작업을 순차적으로 완료하며, UniVKIE는 모든 하위 작업을 하나의 백본으로 통합하여 개선된다. PipVKIE와 UniVKIE는 비전, 텍스트와 좌표로부터 다중 모달 정보를 활용하여 피쳐 표현을 수행한다. 실험 결과, 우리의 솔루션은 뛰어난 성능과 효율적인 추론 속도를 달성할 수 있다.

###### Investigating the Role and Impact of Disfluency on Summarization (https://aclanthology.org/2023.emnlp-industry.52/)
- Anthology ID: 2023.emnlp-industry.52 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 챗과 음성 통화를 모두 처리하는 컨택센터에서는 대화가 종료되면 요약문을 작성하는 것이 일반적인 관행이다. 음성 통화에서는 반복, 재시작 및 대체 등의 특징으로 불차분한 대화가 나타난다. 이러한 불차분한 요소는 하향식 자연어 이해 (NLU) 작업에서는 잡음으로 여겨진다.
    2. 이 논문에서는 챗과 음성 데이터 채널에 대한 수동 주석을 필요로하지 않으면서 완벽한 데이터로 훈련된 모델이 불차분한 데이터를 효과적으로 처리할 수 있는지 조사하는 것이 중요하다.
    3. 실험 결과, 완벽한 데이터로 훈련된 모델이 불차분한 데이터를 처리할 때 Rouge-L 점수가 최대 6.99점 하락하며 더불어 유창성, 일관성 및 관련성이 감소한다는 것을 확인했다. 이를 완화하기 위해 Fused-Fine Tuning을 조사하여 완벽한 데이터와 불차분한 데이터를 결합하여 모델을 훈련시키면 공개 및 실제 데이터셋에서 성능이 향상된다는 것을 알 수 있다.

###### InsightNet : Structured Insight Mining from Customer Feedback (https://aclanthology.org/2023.emnlp-industry.53/)
- Anthology ID: 2023.emnlp-industry.53 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 고객 리뷰에서 구조화된 Insight를 자동으로 추출하기 위해 InsightNet을 제안한다. 현재의 솔루션의 한계인 식별된 주제에 대한 구조 부재, 비표준적인 측면 이름, 풍부한 훈련 데이터의 부재 등을 극복하기 위해 설계된 이 시스템은 원시 리뷰에서 반지도학습 다중 레벨 분류법을 구축하고 의미 유사성 휴리스틱 접근법을 사용하여 레이블 데이터를 생성하며 LLM을 세밀하게 조정하여 다중 작업 Insight 추출 아키텍처를 적용한다.
    2. InsightNet은 각 주제별로 고객의 감정과 원문을 포함한 구체적인 대응 가능 주제를 식별한다.
    3. 실제 고객 리뷰 데이터에서의 평가 결과, InsightNet은 구조, 계층, 완전성 측면에서 기존 솔루션보다 우수한 성과를 내었다. 또한, InsightNet은 다중 레이블 주제 분류에서 현재 최고 성능을 보여주는 기법들과 비교하여 F1 점수가 0.85로 약 11% 향상되었다. 또한, InsightNet은 새로운 측면을 추론하고 분류하는 데에서 일반화 능력이 우수하다.

###### E2E Spoken Entity Extraction for Virtual Agents (https://aclanthology.org/2023.emnlp-industry.54/)
- Anthology ID: 2023.emnlp-industry.54 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 사람-컴퓨터 대화에서 음성으로부터 이름, 주소, 이메일과 같은 entity를 추출하는 것은 어려운 작업이다.
    2. 이 논문에서는 미세조정 된 사전 훈련된 음성 인코더가 음성을 텍스트 전사 없이 상대방이 이해할 수 있는 형태로 entity를 추출하는 데 미치는 영향을 연구한다.
    3. 1단계 접근법이 대화 내의 발화 entity를 식별하기 위해 먼저 텍스트 전사를 생성한 후 텍스트 기반 entity 추출을 수행하는 전통적인 2단계 접근법보다 우수하다는 것을 보여준다.

###### Generative Models for Product Attribute Extraction (https://aclanthology.org/2023.emnlp-industry.55/)
- Anthology ID: 2023.emnlp-industry.55 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 제품 속성 추출은 지식베이스 구축, 제품 추천 및 고객 경험 향상과 같은 응용 프로그램을 포함하는 정보 추출 및 전자 상거래의 신흥 분야이다. 
    2. 본 논문에서는 제품 속성 추출을 위한 생성 모델의 유용성을 분석하고 하드하고 소프트한 프롬프팅 방법을 사용하여 암시적인 속성값을 생성할 수 있는 능력을 시연한다.
    3. 아마존과 MAVE 데이터셋을 사용한 다양한 실험을 통해 생성 모델이 명시적인 제품 속성 추출에 대해 최신 sequence tagging 모델보다 우수한 성능을 발휘하고, 더 많은 데이터 효율성을 갖으며, 암시적인 제품 속성 추출을 수행할 수 있는 독특한 능력을 가지며, 특정 상황에서는 두 개의 문맥 예제로도 훈련된 모델과 경쟁적인 성능을 발휘하는 것을 보여준다.

###### CarExpert: Leveraging Large Language Models for In-Car Conversational Question Answering (https://aclanthology.org/2023.emnlp-industry.56/)
- Anthology ID: 2023.emnlp-industry.56 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대형 언어 모델(LLM)은 domain-specific한 태스크와 데이터에 대해 fine-tuning 없이도 자연어 명령을 잘 따라할 수 있지만, domain-specific한 질문에 대한 LLM의 활용은 심각한 한계가 있다.
    2. 이 논문에서 CarExpert라는 자동차에 관련된 대화형 질문-답변 시스템을 소개하며, LLM을 이용하여 input을 제어하고 domain-specific 문서를 추출 및 생성하는 답변 구성요소에 제공하며, 안전하고 domain-specific한 답변을 보장하도록 output을 제어한다.
    3. 포괄적인 실험적 평가 결과, CarExpert가 최첨단 LLM보다 자연스럽고 안전하며 자동차에 특화된 답변을 잘 생성하는 것을 확인할 수 있다.

###### BUSTER: a “BUSiness Transaction Entity Recognition” dataset (https://aclanthology.org/2023.emnlp-industry.57/)
- Anthology ID: 2023.emnlp-industry.57 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 자연어 처리 (NLP) 분야에서 큰 발전이 있었지만, 이러한 발전을 실제 비즈니스 상황에 적용하는 것은 어려울 수 있다. 이는 대중적인 벤치마크와 실제 데이터 간의 격차 때문이다. 
    2. 우리는 BUSTER라는 비즈니스 거래 개체 인식 데이터셋을 소개하여 산업 지향적인 연구를 지원한다. 이 데이터셋은 3779개의 수동으로 주석이 달린 금융 거래 문서로 구성되어 있다. 
    3. 우리는 일반 목적과 도메인 특정 언어 모델을 활용하여 여러 가지 벤치마크를 설정하였고, 가장 성능이 좋은 모델은 BUSTER에 추가적인 실버마감문서로서 6196개의 문서를 자동으로 주석을 달았다.

###### Multi-word Tokenization for Sequence Compression (https://aclanthology.org/2023.emnlp-industry.58/)
- Anthology ID: 2023.emnlp-industry.58 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대규모 언어 모델의 성능은 다양한 작업에 대해 매우 우수한 결과를 보여주고 있다. 하지만 이는 컴퓨터 자원을 많이 필요로 하기 때문에 산업적으로 보다 널리 사용되기 어렵다. 
    2. 본 논문에서는 Multi-Word Tokenizer (MWT)인 MWT를 제안하여, 빈도가 높은 여러 단어 표현을 단일 토큰으로 표현함으로써 단어 경계를 넘어서는 토큰화를 수행한다. 
    3. 실험 결과, MWT는 시퀀스 길이가 짧을 때에도 더 견고하여 시퀀스를 조기에 줄임으로써 큰 속도 향상을 가능하게 한다.

###### JarviX: A LLM No code Platform for Tabular Data Analysis and Optimization (https://aclanthology.org/2023.emnlp-industry.59/)
- Anthology ID: 2023.emnlp-industry.59 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. JarviX는 고도로 발전된 데이터 분석 프레임워크로, 대용량 언어 모델(LLM)을 활용하여 표 형식의 데이터셋에 대한 자동 가이드와 고정밀 데이터 분석을 수행하는 것을 목표로 한다. 
    2. JarviX는 최신의 LLM을 활용하여 다양한 열 유형의 중요성을 강조하며, 간결한 데이터 인사이트 요약을 생성하고 관련 분석 문의를 제안하며, 데이터를 효과적으로 시각화하고, 포괄적인 결과에 대한 설명을 제공한다. 
    3. 또한, JarviX는 예측 모델링을 위한 자동화된 기계 학습(AutoML) 파이프라인을 통합하여, 기계 구성을 최적화하는 데 특히 유리한 종합적이고 자동화된 최적화 주기를 형성한다.

###### Retrieve and Copy: Scaling ASR Personalization to Large Catalogs (https://aclanthology.org/2023.emnlp-industry.60/)
- Anthology ID: 2023.emnlp-industry.60 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 개별화된 음성인식 모델의 성능을 향상시키기 위해 주로 주의 메커니즘을 사용하는데, 기존 방법들은 효율성에 제한이 있어 실제로 사용하기 힘들다.
    2. 이 논문은 "Retrieve and Copy" 메커니즘을 제안하고, 큰 카탈로그에 확장할 때도 정확성을 유지하며 지연 시간을 개선한다.
    3. 실험 결과, 6% 더 많은 WER 감소 및 F1에서 3.6%의 절대적인 향상을 보여주었으며, 최소 20%의 추론 속도 향상을 달성할 수 있다.

###### STEER: Semantic Turn Extension-Expansion Recognition for Voice Assistants (https://aclanthology.org/2023.emnlp-industry.61/)
- Anthology ID: 2023.emnlp-industry.61 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 음성 어시스턴트 시스템에서 스티어링은 사용자가 이전 턴을 지시하거나 명확히 하기 위해 연속된 명령을 내리는 현상을 말한다. 
    2. 우리는 이전 명령을 조절하려는 사용자의 연속 턴을 예측하는 스티어링 탐지 모델 STEER을 제안한다. 
    3. STEER은 사용자 트랜스크립트만으로도 높은 정확도를 보이며, STEER+는 세마틱 파싱 트리를 활용하여 더 많은 문맥을 제공하고 모델 성능을 향상시킨다.

###### Self-Criticism: Aligning Large Language Models with their Understanding of Helpfulness, Honesty, and Harmlessness (https://aclanthology.org/2023.emnlp-industry.62/)
- Anthology ID: 2023.emnlp-industry.62 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 대화형 스타일의 언어 모델 (LLM)이 인공 일반 지능 (AGI)의 발전에 크게 기여하면서 대규모 언어 모델 (LLMs)의 중요성이 급증하고 있다. 이 논문에서는 RLHF에 비해 저렴하게 LLMs와 함께 일반화된 방식으로 유연하게 정렬하는 방법에 대해 탐구한다.
    2. 이 연구에서는 Self-Criticism라는 새로운 프레임워크를 제안하여 LLMs가 텍스트 코퍼스에서 배운 HHH 정의에 따라 스스로를 정렬할 수 있게 한다. 이 방법은 사전 분류 (IF)와 적은 양의 입력을 통한 인문 학습 (ICL)을 통해 LLMs를 조정하고, 모델이 자체 생성한 응답을 평가하고 자체 판단에 따라 "더 좋은" 응답을 생성하도록 학습한다.
    3. 실험 결과는 Self-Criticism 방법이 RLHF와 거의 동일한 인간 평가 및 다른 LLMs에 의한 평가 성과를 달성한다는 것을 보여준다.

###### InstructPTS: Instruction-Tuning LLMs for Product Title Summarization (https://aclanthology.org/2023.emnlp-industry.63/)
- Anthology ID: 2023.emnlp-industry.63 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 전자상거래 제품 카탈로그는 수십억 개의 항목을 포함하고 있으며, 대부분의 제품은 키워드를 제품 속성과 함께 포함하여 검색 성능을 향상하고 제품의 주요 측면을 강조한다. 이로 인해 소비자들이 사용하는 방식과 다른 불필요한 제목이 생성되는데, 이는 추천, 질의응답, 리뷰 요약과 같은 작업에서 문제가 될 수 있다.
    2. 이 논문은 최근 instruction-tuned LLMs에 영감을 받아 Product Title Summarization (PTS) 작업에 대한 조절 가능한 접근법인 InstructPTS를 제안한다. 새로운 instruction fine-tuning 전략을 사용하여 훈련된 이 접근법은 다양한 기준에 따라 제품 제목을 요약할 수 있다.
    3. 실제 전자상거래 카탈로그에서의 방대한 평가 결과, 단순한 fine-tuning 방법에 비해 제안된 접근법은 더 정확한 제품 이름 요약을 생성할 수 있으며, BLEU와 ROUGE 점수에서 각각 14점과 8점이상의 개선을 보였다.

###### LLM4Vis: Explainable Visualization Recommendation using ChatGPT (https://aclanthology.org/2023.emnlp-industry.64/)
- Anthology ID: 2023.emnlp-industry.64 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. "데이터 시각화는 다양한 도메인에서 통찰력을 탐색하고 전달하기 위한 강력한 도구이다. 시각화 권장은 이러한 데이터셋에 대한 시각화 선택을 자동화하기 위해 제안된 작업이다. 기계 학습 기반 접근법들은 이를 위해 개발되었으나 현재 다양한 예제 데이터와 결과에 대한 자연스러운 설명이 부족하다."
    2. "이 연구에서는 LLM4Vis라는 ChatGPT 기반의 적극적인 접근 방식을 제안하여 매우 적은 실제 예제를 사용하여 시각화 권장 작업을 수행하고 사람과 유사한 설명을 제공한다."
    3. "우리의 접근 방식은 feature description, demonstration example selection, explanation generation, demonstration example construction 및 inference 단계를 포함한다. 평가 결과, LLM4Vis가 Random Forest, Decision Tree 및 MLP와 같은 지도학습 모델에 비해 몇 개의 예제부터 모든 데이터를 사용한 경우에도 우수한 성능을 보였으며, 질적 평가에서도 생성된 설명의 효과성을 확인할 수 있었다."

###### DUBLIN: Visual Document Understanding By Language-Image Network (https://aclanthology.org/2023.emnlp-industry.65/)
- Anthology ID: 2023.emnlp-industry.65 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. OCR에 의존하지 않는 비주얼 문서 이해를 위한 픽셀 기반 모델인 DUBLIN을 제안한다. DUBLIN은 이미지와 텍스트를 픽셀로 처리하고 다양한 문서 유형과 작업을 처리할 수 있다.
    2. DUBLIN은 비주얼과 언어적 능력을 향상시키는 새로운 작업을 포함한 대규모 문서 이미지 코퍼스에서 사전 훈련된다.
    3. 우리는 DUBLIN이 DocVQA, InfoVQA, AI2D, OCR-VQA, RefExp, CORD와 같은 추출 작업에서 우수한 성능을 보이며 VisualMRC 및 텍스트 캡션 작업에서도 강력한 성능을 보인다는 것을 다양한 벤치마크를 통해 평가한다.

###### DocumentNet: Bridging the Data Gap in Document Pre-training (https://aclanthology.org/2023.emnlp-industry.66/)
- Anthology ID: 2023.emnlp-industry.66 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 최근 몇 년간 기업 AI의 다양한 응용 분야에서 중요한 역할을 하는 시각적인 문서 엔터티 검색(VDER)과 같은 문서 이해 작업은 광범위한 관심을 받았으나, 엄격한 개인정보 보호 제한과 높은 주석 비용으로 인해 이러한 작업에 대한 공개 데이터는 부족하다.
    2. 이 논문에서는 웹에서 대량의 약하게 주석이 된 데이터를 수집하여 VDER 모델의 훈련에 활용하는 방법을 제안한다. 
    3. DocumentNet이라는 수집된 데이터셋은 특정 문서 유형이나 엔터티 집합에 의존하지 않으며, 모든 VDER 작업에 적용할 수 있는 범용적인 데이터셋이다.

###### Relevance-assisted Generation for Robust Zero-shot Retrieval (https://aclanthology.org/2023.emnlp-industry.67/)
- Anthology ID: 2023.emnlp-industry.67 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. BEIR 벤치마크와 같은 zero-shot 검색 과제는 고성능 dense retriever의 out-of-domain generalization을 약점으로 보여준다.
    2. 기존의 도메인 적응 방법은 도메인별 유사도를 이용해 pseudo queries(PQ)를 생성하고 fine-tuning하는 것이다. 그러나 PQ 샘플링에 대한 키 바이어스가 있어 일반화에 부정적인 영향을 미칠 수 있다.
    3. 우리는 PQ 생성 과정을 여러 단계로 분리함으로써 그것들을 예방하는 방법을 제안한다. 실험 결과, 우리의 제안은 도메인 변화에 대해 더 강한 내성을 가지는 것으로 나타났다.

###### Too much of product information : Don’t worry, let’s look for evidence! (https://aclanthology.org/2023.emnlp-industry.68/)
- Anthology ID: 2023.emnlp-industry.68 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 제품 질문 답변 (PQA)은 쇼핑 메시지 보드, 소셜 미디어, 브랜드 웹사이트 및 매장에서 고객의 질문에 즉각적으로 응답하는 것을 목표로 한다.
    2. 이 논문에서는 제품 정보를 사용하여 고객 질문에 대답하는 방법론을 제시한다. 
    3. 이를 위해 레이블된 데이터가 쉽게 확보되지 않고, 긴 제품 정보는 질문에 대답하기 위해 다양한 텍스트 부분에 관심을 기울여야 하는 두 가지 주요 과제를 해결한다.

###### Harnessing LLMs for Temporal Data - A Study on Explainable Financial Time Series Forecasting (https://aclanthology.org/2023.emnlp-industry.69/)
- Anthology ID: 2023.emnlp-industry.69 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 금융 시계열에 대한 기계 학습은 시장 통찰력, 리스크 관리, 전략적 의사 결정 및 정책 형성에서 혁신을 가능하게 하는 산업 연구의 활발한 분야입니다. 이 논문은 전통적인 접근 방식에서 볼 수 있는 교차 순서 추론, 다중 모달 데이터 통합 및 결과 해석과 같은 문제들을 해결하기 위해 대규모 언어 모델(Large Language Models, LLMs)을 이용한 설명 가능한 금융 시계열 예측에 대해 탐구합니다.
    2. NASDAQ-100 주식을 중점으로 공개된 역사적 주식 데이터, 회사 메타데이터 및 경제/금융 뉴스를 활용하며, zero-shot/few-shot 추론을 위해 GPT-4 및 instruction-based fine-tuning을 위해 Open LLaMA를 사용합니다.
    3. 실험 결과, LLM 기반 접근 방식이 전통적인 ARMA-GARCH 및 gradient-boosting tree 모델보다 우수한 성능을 보였으며, Open-LLaMA와 같은 공개된 LLMs의 fine-tuning을 통해 합리적이고 설명 가능한 예측을 생성할 수 있음을 보여줍니다. 단, GPT-4와 비교했을 때 성능은 약간 낮습니다.

###### ViGPTQA - State-of-the-Art LLMs for Vietnamese Question Answering: System Overview, Core Models Training, and Evaluations (https://aclanthology.org/2023.emnlp-industry.70/)
- Anthology ID: 2023.emnlp-industry.70 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. training 데이터와 benchmarking 데이터 부족 때문에 저자는 베트남어에 대한 실용적인 질의응답 시스템을 구현할 수 있는 방법을 제안한다. 이를 위해 베트남어에 적합하도록 조정된 instruction-tuned LLM (ViGPT)을 도입하고 평가한다.
    2. ViGPT는 실제 시나리오에서 탁월한 성능을 보여준다. 저자들은 인공지능과 인간이 생성한 데이터를 포함하는 새로운 벤치마크 데이터셋을 제작하여 베트남어 LLM의 포괄적인 평가 프레임워크를 제공한다.
    3. 최종적으로 저자들은 최신 기술을 달성하고 다른 다국어 LLM에 근접한 성과를 이끌어내는 instruction-tuned LLM의 필요성을 강조하며, 개인화 및 개인정보를 보호하는 베트남어 언어 처리 시스템을 지원하는 오픈 소스 모델을 제공한다.

###### An Integrated Search System for Korea Weather Data (https://aclanthology.org/2023.emnlp-industry.71/)
- Anthology ID: 2023.emnlp-industry.71 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. WeatherSearch는 대한기상청에서 배포된 통합 검색 시스템으로, 사용자가 간단한 자연어 질의로 대량의 기상 데이터베이스에서 관련 데이터를 검색할 수 있게 한다.
    2. 우리는 전문가 설문 및 인터뷰를 통해 템플릿을 만들고, 템플릿 채우기와 같은 데이터 증강 기법을 적용하여 400만 개의 데이터를 최소한의 인력으로 수집하였다.
    3. 수집한 데이터를 바탕으로 mT5를 finetune한 결과, 평균 MRR이 0.66, 평균 회수율이 0.82를 달성하였으며, 이를 통해 다른 지역에서 유사한 시스템을 설계하는 데 도움이 되기를 기대한다.

###### Adaptive Hyper-parameter Learning for Deep Semantic Retrieval (https://aclanthology.org/2023.emnlp-industry.72/)
- Anthology ID: 2023.emnlp-industry.72 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 온라인 전자상거래 응용 프로그램에서 깊은 의미적 검색은 놀라운 성과를 거두었습니다. 그러나 대부분의 방법들은 마진 손실이나 소프트맥스 손실을 활용하여 각 쿼리마다 양수 항목과 음수 항목을 구별하려고 합니다.
    2. 최근 몇 가지 방법들은 추천에서 학습 가능한 / 통계적인 메소드를 통해 각 매개 변수를 학습하여 위 문제를 완화하려고 시도했습니다.
    3. 우리는 질의(query)의 독립성과 다양성 때문에 검색 시나리오에 적합하지 않다고 주장하며, 본 논문에서는 검색 성능을 향상시키기 위해 간단하고 범용적인 하이퍼 파라미터 무선학습 방법을 제안합니다.

###### On Sample-Efficient Code Generation (https://aclanthology.org/2023.emnlp-industry.73/)
- Anthology ID: 2023.emnlp-industry.73 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 큰 언어 모델들은 코드 생성 태스크에서 실행 시간 동작을 예측하는 것에 어려움을 겪는다. 그래서 여러 개의 코드 스니펫을 생성한 다음 최적의 것을 선택하기 위해 거부 샘플링(best-of-n)에 의존하고 있다. 
    2. 이 논문에서는 샘플링 비용을 줄이면서도 생성 품질을 유지하는 것이 주요한 차별점이다. 
    3. EFFICODE라는 새로운 프레임워크를 소개하는데, 이는 모델이 해결할 수 있는 테스트 문제에 샘플링을 중점적으로 하는 방법을 제안한다.

###### Batch Prompting: Efficient Inference with Large Language Model APIs (https://aclanthology.org/2023.emnlp-industry.74/)
- Anthology ID: 2023.emnlp-industry.74 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 대규모 언어 모델(Large Language Models, LLMs)에서의 추론은 샘플의 수가 많을수록 계산 및 금전적 비용이 상승하는 문제가 있다. 본 논문에서는 배치 프롬프팅(batch prompting)이라는 간단하고 효과적인 방법을 제안하여 LLM이 한 번에 여러 개의 샘플에 대한 추론을 수행할 수 있도록 한다. 이 방법은 토큰 및 시간 비용을 줄이면서도 다운스트림 성능을 유지한다. 
    2. 테오리적으로 우리는 Few-shot In-Context Learning 설정에서, 배치당 샘플 수에 대한 추론 비용이 거의 역선형적으로 감소함을 보인다.  
    3. Common sense QA, 산술적 추론, NLI/NLU 등 10개의 데이터셋에서 배치 프롬프팅의 효과를 체계적으로 검증하였으며, LLM 추론 토큰 및 시간 비용을 크게 줄이면서도 더 나은 또는 비슷한 성능을 보여준다. 또한, 배치 프롬프팅은 LLM을 사용하는 다양한 추론 방법에 적용할 수 있다.

###### Graph Meets LLM: A Novel Approach to Collaborative Filtering for Robust Conversational Understanding (https://aclanthology.org/2023.emnlp-industry.75/)
- Anthology ID: 2023.emnlp-industry.75 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 맞춤화된 질의 재작성 시스템은 개별 사용자의 행동과 선호도를 고려하여 결함이 있는 질의를 최소화하고 강력한 대화 기능을 보장하기 위해 노력한다. 이 논문은 사용자의 역사적 색인에 포함되지 않은 새로운 사용자 상호작용에서 발생하는 결함이 있는 질의를 다루기 위해 다양한 기술을 사용하는데, 그 중 하나는 고객 피드백 상호작용 그래프로부터 유래된 "협력형 사용자 색인"을 구축하여 새로운 상호작용에 적합한 인덱스를 생성하는 것이다.
    2. 이 논문은 그래프 탐색과 Large Language Models (LLMs)를 결합하여 새로운 상호작용에 대한 적합한 인덱스 증가를 실현하는데 효과적이라는 것을 실험을 통해 입증하였다.
    3. 실제 대규모 데이터셋과 온라인 A/B 실험을 통해 우리가 제안한 방법의 효과를 입증하였다.

###### DELPHI: Data for Evaluating LLMs’ Performance in Handling Controversial Issues (https://aclanthology.org/2023.emnlp-industry.76/)
- Anthology ID: 2023.emnlp-industry.76 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 논란은 우리의 시대정신을 반영하며, 모든 토론에 중요한 측면이다. 대화 시스템으로 사용되는 대형 언어 모델이 등장함에 따라 사람들은 다양한 질문에 대한 답변을 위해 이 모델에 크게 의존하고 있다. 이에 따라 현재의 토론과 관련된 질문에 대해 이러한 모델이 어떻게 응답하는지 체계적으로 조사하는 것이 중요하다. 
    2. 하지만 현대적인 토론을 반영하는 사람이 주석을 단 데이터셋은 거의 없다. 이 연구는 Quora Question Pairs Dataset을 확장하여 논란이 있는 질문 데이터셋을 새롭게 구축한다. 
    3. 우리는 이 데이터셋의 일부를 사용하여 다양한 언어 모델을 평가하고, 이들이 논란이 있는 문제를 어떻게 다루고, 어떤 입장을 취하는지에 대해 조명한다. 이 연구는 결국 대형 언어 모델이 논란이 있는 문제와 상호작용하는 방법을 이해하는 데에 기여하며, 복잡한 사회적 토론의 이해력과 처리 능력을 향상시킬 수 있는 발전의 길을 열어준다.

###### Angel: Enterprise Search System for the Non-Profit Industry (https://aclanthology.org/2023.emnlp-industry.77/)
- Anthology ID: 2023.emnlp-industry.77 
- Volume: Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track 
- Authors: Mingxuan Wang | Imed Zitouni 
- Summary: 
    1. 비영리 산업은 펀드를 찾는 사람 (예: AMERICAN NATIONAL RED CROSS)과 펀드를 제공하는 사람 (예: BILL AND MELINDA GATES FOUNDATION)을 원인 (예: 암)과 대상 수혜 그룹 (예: 어린이)에 맞추어 정확하게 매치시키기 위한 시스템이 필요하다.
    2. 본 연구에서는 비영리 산업을 위한 "ANGEL"이라는 기업 검색 시스템을 만들었다. 이 시스템은 펀드 제공자의 미션 설명을 입력으로 받고 펀드를 찾는 사람들의 순위 목록을 반환한다.
    3. ANGEL은 ColBERT라는 신경 정보 검색 모델을 활용하며, 문법 정보와 다중 헤드 셀프 어텐션을 결합하는 문법 정보 인식 로컬 어텐션 (SLA) 및 간결한 미션 설명의 augmentation을 위한 댄스 가짜 연관 피드백 (DPRF) 기술을 사용한다.

