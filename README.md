## 1. 프로젝트 개요

- **프로젝트명**: Lempel-Ziv Algorithm
- **개발 기간**: [2025.11.06]
- **수행 방식**: 정보이론 및 부호화 개론 강의 과제
- **담당 범위:** 난수 소스 생성, LZ78 Encoder/Decoder 구현 및 성능 분석
- **기술 스택**: Python

---

## 2. 클라이언트 요구사항 및 나의 역할

### 💼 클라이언트 개요

> 본 프로젝트는 정보이론에서 다루는 Lempel-Ziv 78 (LZ78) 압축 알고리즘을 직접 구현하고, random binary source에 대해 압축 결과와 압축률을 분석하는 것을 목적으로 하였다. 
이론으로만 학습하던 dictionary 기반 압축 알고리즘을 실제 코드로 구현하여, dictionary 생성 과정과 decodability를 검증하였다.
> 

### 📌 요구사항 요약

- 확률 q를 갖는 Bernoulli binary source 생성
- LZ78 Encoder/Decoder 알고리즘 구현
- Encoding 결과의 복원 정확성 검증
- 압축률 계산 및 출력

### 👨‍💻 담당 역할

- Bern(q) 기반 random source 생성 함수 구현
- LZ78 Encoder/Decoder 구현
- 코드 길이 기반 압축률 계산 및 분석

---

## 3. 기술 스택 및 아키텍처

| 항목 | 사용 기술 / 개념 |
| --- | --- |
| 구현 언어 | Python |
| 난수 생성 | import random
random.random() |
| 압축 방식 | import math
math.log2() |
| 검증 | Encoder→Decoder round trip |

### 📐 아키텍처 특징

- Source Generator
    - Bern(q) 확률을 갖는 길이 10^5 binary sequence generator
- LZ78 Encoder
    - dictionary 점진적으로 확장
    - (index, symbol) 쌍으로 output stream 구성
- LZ78 Decoder
    - 동일한 dictionary 재구성
    - prefix + symbol 결합을 통해 원본 복원

---

## 4. 주요 기능

| 기능 | 설명 |
| --- | --- |
| 랜덤 소스 생성 | Bern(q) Binary sequence |
| LZ78 Encoding | Dictionary-based prefix matching |
| LZ78 Decoding | Dictionary 재구성 복원 |
| 무손실 검증 | W→X→Y→W’ , W=W’ |
| 압축률 계산 | Rc=c(logc+1)/n |

---

## 5. 문제 해결 및 기술적 도전

### ✅ 문제 사례 1: LZ78 Encoding 시 prefix index 처리 오류

> 기존 prefix가 dictionary에 존재할 때와 존재하지 않을 때, 출력해야 할 index 값을 구분하지 않으면 decoder에서 dictionary가 어긋나는 문제가 발생하였다.
→ 해결 방법: 현재 word가 dictionary에 존재하는지 여부를 chk 플래그로 명확히 구분하여, 최초 등장 prefix는 (0,symbol), 기존 prefix 확장은 (index + 1, symbol) 형태로 출력하도록 수정하였다. 이는 decoder에서 동일한 dictionary를 정확히 재현할 수 있도록 하였다.
> 

### ✅ 문제 사례 2: 입력 종료 시 남은 prefix 처리 문제

> 입력 비트열의 마지막에서 prefix가 dictionary에 이미 존재한 상태로 종료되면, encoder가 이를 출력하지 않아 일부 비트가 손실되는 문제가 발생하였다
> 
> 
> → 해결 방법: 루프 종료 후 word가 empty(””)이지 않을 경우, (dictionary.index(word) + 1, ‘’) 형태로 마지막 entry가 출력될 수 있도록 하였다. 
> 

---

## 6. 협업 및 커뮤니케이션

- 개인 과제 형태로 수행
- 이론 강의 자료 기반으로 설계
- 결과 검증은 직접 구현한 decoder와 비교하여 수행

---

## 7. 개발 결과 및 회고

### 📈 결과

- encoder–decoder round-trip 검증 통과
- dictionary 크기 증가에 따른 압축률 계산 및 보고서 작성

### 🤔 회고

- LZ78은 단순해 보이지만, index 정의와 사전 동기화가 정확하지 않으면 즉시 복원이 깨진다는 점을 체감했다.
- 이론에서 보던 (index, symbol) 표현이 실제 구현에서는 off-by-one 오류로 이어지기 쉬웠다.
