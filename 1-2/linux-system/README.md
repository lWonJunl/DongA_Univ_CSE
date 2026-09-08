# 🐧 LinuxSystem

> 2026학년도 2학기에 수강하는 LinuxSystem 전공선택 과목의 수업 기록입니다.

1주차 2차시에는 관리자 권한으로 명령을 실행하는 `sudo`와 다른 사용자로 전환하는 `su`를 기록했습니다.

<br>

## 📂 Overview

| Item | Description |
| :-- | :-- |
| **Type** | 전공선택 |
| **Period** | 2026학년도 2학기 |
| **Environment** | Ubuntu WSL 26.04 LTS |
| **Recorded Classes** | 1개 |
| **Recorded Commands** | 2개 |

<br>

## 🧭 Course Progression

```text
사용자 권한 관리
├── sudo: 다른 사용자의 권한으로 명령 실행
└── su: 다른 사용자로 전환
```

<br>

## 📅 Weekly Records

| Week | Topic | Main Practice | Files |
| :--: | :-- | :-- | --: |
| [01-02](Week01-Day02.md) | 사용자 권한과 전환 | `sudo`, `su` | 1 |

<br>

## 📖 Learning by Stage

### 1. 사용자 권한과 전환

`sudo`는 기본적으로 `root` 권한으로 명령을 실행하며, `-u 사용자`를 사용하면 지정한 사용자의 권한으로 실행합니다. `-k`는 저장된 인증 정보를 무효화합니다.

`su [사용자명]`은 다른 사용자로 전환하며, 사용자명을 생략하면 기본적으로 `root` 사용자로 전환합니다.

대표 기록:

- [`sudo` 명령어](Week01-Day02.md#1-sudo)
- [`su` 명령어](Week01-Day02.md#2-su)

<br>

## ▶️ Running the Examples

```bash
sudo 명령
sudo -u 사용자 명령
sudo -k
su 사용자명
su
```

<br>

## ⚠️ Environment Notes

- 사용자 계정과 권한 설정에 따라 `sudo`, `su`의 실행 결과가 달라질 수 있습니다.

<br>

## 🏷️ File Naming

| Pattern | Meaning |
| :-- | :-- |
| 주차와 차시가 포함된 `.md` 파일 | 수업 기록 문서 |

<br>

## 🔗 Navigation

- [1학년 2학기](../README.md)
- [저장소 대표 README](../../README.md)
