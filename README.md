# 🎓 Dong-A University CSE

> 동아대학교 컴퓨터공학과에서 수강한 전공 과목과 교내 스터디의 실습 코드를 학기별로 정리한 저장소입니다.

2026학년도 1학기의 C 기초 문제 풀이와 Python 프로그래밍 수업을 시작으로, 강의 실습·과제·프로젝트의 학습 과정을 기록합니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **University** | 동아대학교 |
| **Major** | 컴퓨터공학과 |
| **Period** | 2026 ~ |
| **Current Record** | 1학년 1학기 |
| **Languages** | C, Python |
| **Activities** | 전공 수업, 학회 기초 스터디 |
| **Status** | 🚧 In Progress |

<br>

## 🗂️ Repository Structure

```text
donga-univ-cse/
├── 1-1/
│   ├── c-cpp-beginner-study/
│   │   ├── README.md
│   │   └── 10 BOJ solutions
│   └── python-programming/
│       ├── README.md
│       ├── week-02/ ... week-13/
│       └── week-14/
│           ├── README.md
│           └── brick-breaker.py
├── 1-2/
│   ├── coding-basics-and-problem-solving/
│   └── linux-system/
└── README.md
```

<br>

## 📖 Semester Records

### 1학년 1학기

| Activity | Type | Contents | Record |
| :-- | :-- | :-- | :-- |
| **C/C++ Beginner Study** | 동아대학교 소프트웨어대학 학회 MLP 스터디 | C 문법과 BOJ 입출력·조건문·반복문 문제 풀이 | [상세 보기](1-1/c-cpp-beginner-study) |
| **Python Programming** | 전공선택 | Python 기초부터 GUI, 파일 입출력, 객체지향과 Pygame 프로젝트까지 학습 | [상세 보기](1-1/python-programming) |

### 1학년 2학기

| Course | Main Area | Record |
| :-- | :-- | :-- |
| **Linux System** | Linux | [과목 폴더](1-2/linux-system) |
| **코딩의기초와문제해결** | C 언어 | [과목 폴더](1-2/coding-basics-and-problem-solving) |

수업이 시작되면 과목별 실습 코드와 학습 내용을 추가할 예정입니다.

<br>

## 💻 C/C++ Beginner Study

MLP는 동아대학교 소프트웨어대학 학회입니다. 학회에서 진행한 기초 스터디를 통해 표준 입출력부터 조건문과 반복문까지 학습하고, 같은 개념을 BOJ 문제에 적용했습니다.

주요 학습 내용:

- `printf`, `scanf`를 이용한 표준 입출력
- 산술 연산과 나머지 연산
- `if`, `else if`를 이용한 조건 분기
- `for` 반복문과 중첩 출력
- 문자 배열을 이용한 간단한 입력 검증

풀이 파일은 `문제번호-영문-주제.c` 형식으로 정리해 문제 번호와 내용을 함께 확인할 수 있습니다.

<br>

## 🐍 Python Programming

Python의 입출력과 자료형에서 시작해 조건문, 반복문, 리스트, 문자열, 함수, 모듈, 파일 입출력과 객체지향 프로그래밍을 단계적으로 실습했습니다.

| Week | Topic | Examples |
| :--: | :-- | :-- |
| 02 | 출력 형식, 진법과 연산 | 별 모양 출력, 진법 변환, 지폐 계산 |
| 03 | 연산자와 조건문 | 비트 시프트, 성적 판정 |
| 04 | `for`·`while` 반복문 | 누적 합, 구구단, 종료 조건 |
| 05 | 리스트와 반복문 응용 | 리스트 연산, 숫자 맞히기, 주차 보고서 |
| 06 | 리스트와 딕셔너리 | 입력값 합산, 역순 리스트, 딕셔너리 순회 |
| 07 | 문자열 처리 | 문자 치환과 입력 종류 판별 |
| 09 | Tkinter GUI | 메뉴, 위젯과 이미지 뷰어 |
| 10 | 함수와 모듈 | 반환값, 계산 함수와 사용자 모듈 |
| 11 | 파일 입출력 | 읽기, 쓰기, 복사와 문자 암호화 |
| 13 | 객체지향 프로그래밍 | 클래스, 생성자, 클래스 변수와 상속 |
| 14 | Pygame 프로젝트 | [벽돌깨기 게임](1-1/python-programming/week-14) |

<br>

## 🛠️ Tech Stack

| Category | Stack |
| :-- | :-- |
| **Languages** | C, Python 3 |
| **GUI & Game** | Tkinter, Pygame |
| **Tools** | Visual Studio Code, Git, GitHub |
| **Practice** | Baekjoon Online Judge |

<br>

## 🎯 What I Learned

- 문법에서 배운 개념을 작은 문제와 프로그램으로 구현하는 방법
- 조건문과 반복문을 조합해 입력을 처리하고 원하는 출력을 만드는 방법
- 여러 파일로 기능을 나누고 Python 모듈을 불러오는 방법
- GUI 이벤트와 게임 루프처럼 순차 실행과 다른 프로그램 흐름
- 학기·과목·주차 기준으로 학습 기록을 관리하는 방법

<br>

## 📌 Notes

- 학습 당시 작성한 구현은 진행 과정을 보여 주기 위해 최대한 보존했습니다.
- 일부 Tkinter 실습은 별도 이미지가 필요하고, 파일 입출력 실습은 실행 환경에 맞는 입력 파일과 경로가 필요합니다.
- GUI와 Pygame 프로그램은 그래픽 창을 사용할 수 있는 데스크톱 환경에서 실행해야 합니다.
