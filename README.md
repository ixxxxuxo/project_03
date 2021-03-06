# project_03_ML/DL for PSG(Polysomnography)
- **프로젝트 배경**
  - 수면은 인간 삶에서 1/3을 차지하는 만큼 그 중요성과 올바른 수면습관 형성이 건강에 미치는 영향이 상당하다.
  - 하지만 아직까지 수면에 대한 올바른 인식이 부족하고, 이를 관리하는것 보다 깨어 있는 시간에 효용성과 생산성을 더 중요시하는것이 현실이다.
  - 최근 기술의발전으로 일상생활에서 건강관리를 도와주는 제품/서비스의 출시가 점점 더 많아지고 있으며, 슬립테크라 불리우는 수면산업 역시 매년 성장세를 보이고 있다.
- **프로젝트 목적**
  - 본 프로젝트를 통해 일상 생활에서 마이크로부터 측정되는 소리를 바탕으로 수면의 질과양을 측정하고 분석하는 모델을 구축해 보고자 한다.
  - 나아가 이러한 모델이 고도화 되고 사용자 데이터가 축적된다면, 병원기관에서 수행하는 PSG(수면다원검사)의 판독시간을 단축하거나 사전검사와 같은 보조적수단으로 활용될 수 있다고 생각한다.
- **회고**
  - 뇌파데이터를 직접적으로 다루기 위해서는 기본적인 도메인 지식이 필요하다.
  - 건강정보를 다루는 모델구축에 있어서는 절대적으로 올바른 정답데이터의 확보가 필요하다고 생각했다.
    - 개방된 의료데이터는 접근 권한이 제약이 있거나 데이터 셋이 한정적이며, 한국인의 표준화된 데이터를 찾을 수 없었다. 
  - 이를 비지도학습을 통해 수행한 연구사례나 프로젝트를 살펴보고, 뇌파데이터가 아닌 소리로 수면패턴을 분석하는 기존서비스는 어떤 알고리즘을 활용하는지 살펴보고
  - 기존 병원기관의 수면검사 대비 수면패턴 분석결과에 얼마나 신뢰도가 높은지 서비스별로 분석해 보고자 한다.
  
