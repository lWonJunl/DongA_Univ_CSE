# 💻 C/C++ Beginner Study

> 동아대학교 소프트웨어대학 학회 MLP에서 진행한 C/C++ 기초 스터디의 BOJ 문제 풀이 기록입니다.

저장소에는 C로 작성한 BOJ 문제 풀이 10개가 있으며, 파일명에는 문제 번호와 영문 주제를 함께 사용합니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **Type** | C/C++ 기초 스터디 |
| **Period** | 2026학년도 1학기 |
| **Language** | C |
| **Platform** | Baekjoon Online Judge |
| **Source Files** | 10개 |
| **Organization** | 동아대학교 소프트웨어대학 학회 MLP |

<br>

## 🧭 Course Progression

```text
기본 출력과 산술 연산
        ↓
반복 입력과 조건 분기
        ↓
반복문과 출력 패턴
        ↓
문자열 입력과 길이 검사
```

<br>

## 📝 Problem Records

| BOJ | Problem | Main Practice | File |
| :--: | :-- | :-- | :-- |
| 2557 | Hello World | `printf` 출력 | [C](2557-hello-world.c) |
| 10869 | 사칙연산 | 산술 연산과 나머지 | [C](10869-arithmetic-operations.c) |
| 10950 | A+B - 3 | 반복 입력 | [C](10950-a-plus-b-3.c) |
| 2480 | 주사위 세개 | 조건 분기 | [C](2480-three-dice.c) |
| 2525 | 오븐 시계 | 시각 계산 | [C](2525-oven-clock.c) |
| 25314 | 코딩은 체육과목 입니다 | 문자열 반복 출력 | [C](25314-long-int.c) |
| 25372 | 성택이의 은밀한 비밀번호 | `strlen` 검사 | [C](25372-password-validation.c) |
| 2739 | 구구단 | `while` 반복문 | [C](2739-multiplication-table.c) |
| 2438 | 별 찍기 - 1 | 중첩 반복문 | [C](2438-print-stars-1.c) |
| 2439 | 별 찍기 - 2 | 공백과 별 출력 | [C](2439-print-stars-2.c) |

<br>

## 📖 Learning by Stage

### 1. 기본 출력, 연산과 입력

`2557-hello-world.c`는 `printf`로 문자열을 출력합니다. `10869-arithmetic-operations.c`는 두 정수를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈과 나머지 연산 결과를 출력합니다.

대표 풀이:

- [Hello World](2557-hello-world.c)
- [사칙연산](10869-arithmetic-operations.c)
- [A+B - 3](10950-a-plus-b-3.c)

### 2. 조건문과 반복문

`2480-three-dice.c`는 세 입력값의 일치 여부에 따라 분기합니다. `2739-multiplication-table.c`, `2438-print-stars-1.c`, `2439-print-stars-2.c`는 반복문으로 곱셈식 또는 문자 패턴을 출력합니다.

대표 풀이:

- [주사위 세개](2480-three-dice.c)
- [구구단](2739-multiplication-table.c)
- [별 찍기 - 1](2438-print-stars-1.c)
- [별 찍기 - 2](2439-print-stars-2.c)

### 3. 문자열 길이 검사

`25372-password-validation.c`는 문자 배열에 입력을 받고 `strlen`으로 문자열 길이를 확인합니다.

대표 풀이:

- [성택이의 은밀한 비밀번호](25372-password-validation.c)

<br>

## ▶️ Running the Examples

GCC 환경에서 원하는 C 파일을 컴파일하고 실행합니다.

```bash
gcc 10869-arithmetic-operations.c -o solution
./solution
```

<br>

## ⚠️ Environment Notes

- Windows PowerShell에서는 생성된 실행 파일을 `.\solution.exe`로 실행합니다.
- BOJ 제출용 프로그램은 문제에서 요구한 출력만 작성합니다.

<br>

## 🏷️ File Naming

| Pattern | Meaning |
| :-- | :-- |
| `문제번호-영문-주제.c` | BOJ 문제 번호와 영문 주제를 포함한 C 소스 파일 |

<br>

## 🔗 Navigation

- [1학년 1학기](../README.md)
- [저장소 대표 README](../../README.md)
