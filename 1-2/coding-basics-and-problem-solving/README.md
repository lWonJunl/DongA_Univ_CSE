# 💻 코딩의기초와문제해결

> 1학년 2학기 코딩의기초와문제해결 과목에서 작성할 C 언어 실습, 문제 풀이와 과제를 정리하는 공간입니다.

현재는 수강 전이므로 구체적인 진도나 프로젝트를 미리 단정하지 않고, 실제 수업 자료를 일관되게 관리하기 위한 기준만 마련했습니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **Semester** | 1학년 2학기 |
| **Course** | 코딩의기초와문제해결 |
| **Language** | C |
| **Source Extension** | `.c` |
| **Status** | 🗓️ 수강 예정 |

<br>

## 🧩 자료별 파일 형식

| 학습 자료 | 형식 | 용도 |
| :-- | :-- | :-- |
| C 소스 코드 | `.c` | 강의 예제, 실습, 문제 풀이와 과제 |
| 개념 및 풀이 설명 | `.md` | 문제 정의, 접근 방법과 실행 방법 기록 |
| 입력 예시 | `.txt` | 프로그램 테스트에 사용하는 입력값 |
| 헤더 파일 | `.h` | 여러 소스가 공유하는 선언이 생길 때 사용 |

실행 파일은 운영체제와 컴파일러에 따라 다시 만들 수 있으므로 저장소에 포함하지 않고 소스와 설명을 중심으로 관리합니다.

<br>

## 🗂️ 예정 구조

수업 자료가 생기면 실제 강의 구성에 맞춰 필요한 폴더만 추가합니다.

```text
coding-basics-and-problem-solving/
├── week-01/
│   └── example.c
├── assignments/
│   └── assignment-01/
│       ├── README.md
│       └── main.c
├── projects/
│   └── project-name/
│       ├── README.md
│       └── main.c
└── README.md
```

강의가 주차제가 아니거나 별도의 명명 규칙을 제공하면 과목 기준을 우선합니다.

<br>

## 🏷️ 파일명 규칙

| Type | Pattern | Example |
| :-- | :-- | :-- |
| 강의 예제 | `example-topic.c` | `example-standard-input.c` |
| 실습 | `practice-topic.c` | `practice-conditional.c` |
| 과제 | `assignment-number-topic.c` | `assignment-01-calculator.c` |
| 문제 풀이 | `problem-number-topic.c` | `problem-01-digit-sum.c` |

교재나 온라인 저지의 문제 번호가 있으면 번호를 유지해 원문을 쉽게 찾을 수 있도록 합니다.

<br>

## ▶️ 기본 실행 방법

GCC를 사용하는 경우 다음과 같이 컴파일하고 실행합니다.

```bash
gcc main.c -o main
./main
```

Windows PowerShell에서는 생성된 실행 파일을 다음과 같이 실행할 수 있습니다.

```powershell
.\main.exe
```

실제 과제에 추가 컴파일 옵션이나 여러 소스 파일이 필요하면 해당 프로젝트 README에 별도로 기록합니다.

<br>

## 📌 정리 원칙

- 코드만 저장하지 않고 입력 조건, 출력 결과와 핵심 아이디어를 함께 기록합니다.
- 수업에서 제공한 예제와 직접 작성한 과제를 파일명으로 구분합니다.
- 실행에 외부 입력 파일이 필요하면 파일 형식과 준비 방법을 README에 설명합니다.
- 컴파일 과정에서 필요한 명령과 환경 차이를 프로젝트별로 기록합니다.
- 수업에서 다루지 않은 내용을 학습 완료 항목처럼 작성하지 않습니다.

<br>

## 🔗 Navigation

- [1학년 2학기](../README.md)
- [저장소 대표 README](../../README.md)
