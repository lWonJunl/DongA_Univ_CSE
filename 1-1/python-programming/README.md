# 🐍 Python Programming

> 2026학년도 1학기에 수강한 Python Programming 전공선택 과목의 주차별 실습, 보고서와 최종 프로젝트를 정리했습니다.

출력과 자료형에서 시작해 조건문, 반복문, 컬렉션, 문자열, 함수, 파일 입출력과 객체지향 프로그래밍을 학습했습니다. 후반부에는 Tkinter로 GUI 이벤트를 다루고 Pygame 벽돌깨기 게임을 구현했습니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **Type** | 전공선택 과목 |
| **Period** | 2026학년도 1학기 |
| **Language** | Python 3 |
| **Recorded Weeks** | 11개 주차 |
| **Source Files** | 58개 |
| **GUI** | Tkinter |
| **Final Project** | Pygame 벽돌깨기 |

<br>

## 🧭 Course Progression

```text
출력·변수·자료형
        ↓
연산자·조건문·반복문
        ↓
리스트·딕셔너리·문자열
        ↓
함수·모듈·파일 입출력
        ↓
클래스·생성자·상속
        ↓
Tkinter GUI와 Pygame 게임
```

<br>

## 📅 Weekly Records

| Week | Topic | Main Practice | Files |
| :--: | :-- | :-- | --: |
| [02](week-02) | 출력과 데이터 표현 | 출력 서식, 진법 변환, 지폐 단위 계산 | 4 |
| [03](week-03) | 연산자와 조건문 | 비트 연산, 시프트, 점수별 학점 판정 | 3 |
| [04](week-04) | 반복문 기초 | 누적 합, 구구단, 반복 종료 조건 | 9 |
| [05](week-05) | 반복문과 리스트 응용 | 리스트 메서드, 반복문 재작성, 10문제 보고서 | 18 |
| [06](week-06) | 리스트와 딕셔너리 | 입력값 합산, 역순 저장, 딕셔너리 순회 | 4 |
| [07](week-07) | 문자열 | 위치별 문자 변환과 문자열 종류 판별 | 2 |
| [09](week-09) | Tkinter GUI | 메뉴 바, 위젯과 이미지 뷰어 | 3 |
| [10](week-10) | 함수와 모듈 | 복수 반환값, 계산 함수와 사용자 모듈 | 5 |
| [11](week-11) | 파일 입출력 | 파일 읽기·쓰기·복사와 문자 암호화 | 5 |
| [13](week-13) | 객체지향 | 클래스, 생성자, 클래스 변수와 상속 | 4 |
| [14](week-14) | Pygame 프로젝트 | 패들·공·벽돌의 충돌과 게임 상태 구현 | 1 |

<br>

## 📖 Learning by Stage

### 1. Python 기초 문법

2~3주차에는 출력 서식, 이스케이프 문자와 변수 사용법을 익혔습니다. 입력한 값을 여러 진법으로 변환하고 비트 시프트 결과를 출력하면서 정수 표현과 연산자의 동작을 확인했습니다.

대표 실습:

- [별 모양 출력](week-02/self-03-01-star-pattern.py)
- [진법 변환](week-02/self-03-02-base-converter.py)
- [지폐 단위 계산](week-02/self-04-01-banknote-counter.py)
- [학점 판정](week-03/code-05-07-grade-calculator.py)

### 2. 제어문과 컬렉션

4~7주차에는 `for`, `while`, `break`, `continue`를 이용해 반복 흐름을 제어했습니다. 같은 구구단을 서로 다른 반복문으로 다시 작성하고, 리스트·딕셔너리와 문자열 데이터를 순회했습니다.

대표 실습:

- [전체 구구단](week-04/code-06-08-multiplication-tables.py)
- [종료 조건이 있는 덧셈](week-04/code-06-12-sentinel-addition.py)
- [리스트 메서드](week-05/list-methods.py)
- [딕셔너리 기초](week-06/dictionary-basics.py)
- [문자 위치별 치환](week-07/self-08-01-character-mask.py)

### 3. GUI, 함수와 파일

9~11주차에는 Tkinter 위젯의 이벤트 처리, 함수의 반환값과 사용자 모듈을 학습했습니다. 텍스트 파일을 읽고 쓰거나 복사하고, 문자 코드를 이동하는 방식으로 간단한 암호화·복호화 과정도 구현했습니다.

대표 실습:

- [Tkinter 메뉴 바](week-09/code-10-04-menu-bar.py)
- [Tkinter 위젯](week-09/widgets-demo.py)
- [사용자 모듈 호출](week-10/module-usage.py)
- [파일 존재 확인 후 읽기](week-11/code-11-06-read-file-if-exists.py)
- [파일 암호화와 복호화](week-11/code-11-09-file-encryption.py)

### 4. 객체지향과 게임 프로젝트

13주차에는 자동차 클래스를 예제로 인스턴스 변수, 클래스 변수, 생성자와 상속을 비교했습니다. 14주차에는 Pygame의 이벤트 루프와 충돌 판정을 이용해 최종 프로젝트를 구현했습니다.

대표 실습:

- [클래스 변수](week-13/code-12-05-class-variables.py)
- [생성자 매개변수](week-13/self-12-01-parameterized-car.py)
- [클래스 상속](week-13/self-12-02-inheritance.py)
- [Pygame 벽돌깨기](week-14)

<br>

## 📝 Week 05 Report

5주차 보고서는 조건문과 반복문을 작은 문제에 적용한 10개의 독립 실습으로 구성되어 있습니다.

| No. | Topic | File |
| :--: | :-- | :-- |
| 01 | 음수 여부 판정 | [Python](week-05/report/report-01-negative-number.py) |
| 02 | 게임 점수에 따른 수준 판정 | [Python](week-05/report/report-02-game-score-level.py) |
| 03 | 두 정수의 일치 여부 | [Python](week-05/report/report-03-number-equality.py) |
| 04 | 윤년 판정 | [Python](week-05/report/report-04-leap-year.py) |
| 05 | 두 사람의 주사위 게임 | [Python](week-05/report/report-05-dice-game.py) |
| 06 | `#` 문자 반복 출력 | [Python](week-05/report/report-06-hash-pattern.py) |
| 07 | 입력받은 단의 구구단 | [Python](week-05/report/report-07-multiplication-table.py) |
| 08 | 숫자 맞히기 | [Python](week-05/report/report-08-number-guessing.py) |
| 09 | 무작위 덧셈 퀴즈 | [Python](week-05/report/report-09-addition-quiz.py) |
| 10 | 첫 모음 이전의 문자열 출력 | [Python](week-05/report/report-10-before-first-vowel.py) |

<br>

## 🧱 Final Project

[Pygame 벽돌깨기](week-14)는 키보드 입력, 프레임별 위치 갱신, 사각형 충돌 판정과 상태 관리를 하나의 게임 루프로 연결한 프로젝트입니다.

구현한 요소:

- 방향키를 이용한 패들 이동과 화면 경계 제한
- 공과 벽·패들·벽돌의 충돌 처리
- 일반 벽돌과 보너스 벽돌의 점수 구분
- 목숨 차감과 공·패들 위치 초기화
- 남은 벽돌 수에 따른 승리 및 게임 종료 처리

<br>

## ▶️ Running the Examples

대부분의 콘솔 실습은 원하는 주차 폴더에서 Python으로 실행할 수 있습니다.

```bash
cd week-04
python code-06-08-multiplication-tables.py
```

벽돌깨기 프로젝트는 Pygame 설치가 필요합니다.

```bash
pip install pygame
python week-14/brick-breaker.py
```

<br>

## ⚠️ Environment Notes

- `week-09`의 이미지 뷰어는 코드에서 참조하는 GIF 이미지 폴더가 별도로 필요합니다.
- `week-11` 예제는 입력 텍스트 파일 또는 운영체제별 파일 경로를 사용하므로 실행 환경에 맞는 자료를 준비해야 합니다.
- Tkinter와 Pygame 예제는 그래픽 창을 표시할 수 있는 데스크톱 환경에서 실행해야 합니다.
- 강의 당시 작성한 코드의 흐름을 보존했으므로 일부 실습은 사용자 입력이나 보조 파일 없이는 끝까지 실행되지 않습니다.

<br>

## 🏷️ File Naming

| Pattern | Meaning |
| :-- | :-- |
| `lecture.py` | 해당 주차의 강의 예제 모음 |
| `code-XX-XX-topic.py` | 교재 예제 번호와 핵심 주제 |
| `self-XX-XX-topic.py` | 자기주도 실습 번호와 핵심 주제 |
| `report-XX-topic.py` | 보고서의 문제 순서와 내용 |

<br>

## 🔗 Navigation

- [1학년 1학기](../README.md)
- [Pygame 벽돌깨기](week-14)
- [저장소 대표 README](../../README.md)
