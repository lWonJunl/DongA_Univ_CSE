# 📘 1학년 1학기

> 2026학년도 1학년 1학기에 진행한 전공 수업과 동아대학교 소프트웨어대학 학회 MLP 활동을 정리한 학습 기록입니다.

C 언어로 프로그래밍 문제 해결의 기초를 익히고, Python Programming 수업에서 문법부터 GUI·파일 입출력·객체지향 프로그래밍까지 학습했습니다. 마지막에는 Pygame을 이용해 벽돌깨기 게임을 구현했습니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **Semester** | 2026학년도 1학년 1학기 |
| **Course** | Python Programming |
| **Academic Activity** | 동아대학교 소프트웨어대학 학회 MLP |
| **Languages** | C, Python |
| **Source Files** | C 10개, Python 58개 |
| **Final Project** | Pygame 벽돌깨기 |

<br>

## 📚 Activities

### C/C++ Beginner Study

| Item | Description |
| :-- | :-- |
| **Organization** | 동아대학교 소프트웨어대학 학회 MLP |
| **Activity** | C/C++ 기초 스터디 |
| **Language Used** | C |
| **Practice** | Baekjoon Online Judge 10문제 |
| **Record** | [문제 풀이와 학습 내용](c-cpp-beginner-study) |

표준 입출력과 산술 연산에서 시작해 조건문, 반복문과 문자열 길이 검사를 BOJ 문제에 적용했습니다. 문제 번호를 파일명에 유지해 원문과 풀이를 쉽게 연결할 수 있도록 정리했습니다.

### Python Programming

| Item | Description |
| :-- | :-- |
| **Type** | 전공선택 과목 |
| **Language** | Python 3 |
| **Recorded Weeks** | 2~7주차, 9~11주차, 13~14주차 |
| **Practice** | 강의 예제, 자기주도 실습, 주차 보고서 |
| **Record** | [주차별 수업 기록](python-programming) |

출력과 자료형부터 조건문, 반복문, 리스트, 문자열, 함수와 모듈을 순서대로 익혔습니다. 이후 Tkinter GUI, 파일 입출력과 클래스·상속을 실습하고 Pygame 프로젝트로 학습 내용을 확장했습니다.

<br>

## 🗂️ Repository Structure

```text
1-1/
├── c-cpp-beginner-study/
│   ├── README.md
│   └── 10 BOJ solutions
├── python-programming/
│   ├── README.md
│   ├── week-02/ ... week-13/
│   └── week-14/
│       ├── README.md
│       └── brick-breaker.py
└── README.md
```

<br>

## 🧭 Learning Path

```text
C 표준 입출력과 연산
          ↓
조건문·반복문을 BOJ 문제에 적용
          ↓
Python 자료형과 제어문 학습
          ↓
리스트·문자열·함수와 모듈 활용
          ↓
파일 입출력과 객체지향 프로그래밍
          ↓
Tkinter GUI와 Pygame 프로젝트
```

<br>

## 💡 Semester Highlights

### 문제 해결 기초

- 입력 조건을 읽고 필요한 변수와 자료형을 선택했습니다.
- 조건을 여러 경우로 나누고 반복 범위를 코드로 표현했습니다.
- BOJ의 정해진 입출력 형식에 맞춰 불필요한 문구 없이 결과를 출력했습니다.

### Python 응용

- 같은 구구단 출력을 `for`와 `while`로 각각 구현하며 반복 구조를 비교했습니다.
- 리스트와 딕셔너리로 여러 값을 저장하고 순회·검색·정렬했습니다.
- 함수를 별도 모듈로 분리하고 다른 파일에서 불러와 사용했습니다.
- 파일 읽기·쓰기와 간단한 문자 암호화 흐름을 실습했습니다.

### 프로젝트

- 키보드 이벤트와 프레임 단위 갱신을 이용해 패들을 조작했습니다.
- 공, 패들, 벽돌 사이의 충돌을 사각형 영역으로 판정했습니다.
- 점수, 목숨, 남은 벽돌과 승패 상태를 하나의 게임 루프에서 관리했습니다.

<br>

## 📌 Record Notes

- 교재 예제 번호가 있는 파일은 번호를 보존하고 핵심 내용을 영문 파일명에 추가했습니다.
- C/C++ 스터디 폴더에는 현재 C로 작성한 풀이만 포함되어 있습니다.
- Tkinter 이미지 실습과 파일 입출력 실습 일부는 별도 이미지·텍스트 파일이 필요합니다.
- 학습 당시 코드의 흐름은 기록 목적으로 보존하고, 폴더 이동으로 깨지는 import와 절대 경로만 현재 구조에 맞게 조정했습니다.

<br>

## 🔗 Navigation

- [저장소 대표 README](../README.md)
- [C/C++ Beginner Study](c-cpp-beginner-study)
- [Python Programming](python-programming)
- [Pygame 벽돌깨기](python-programming/week-14)
