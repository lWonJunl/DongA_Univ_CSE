# Pygame 벽돌깨기

공과 패들의 움직임, 충돌 판정, 점수와 게임 상태를 직접 제어해 완성한 Python Programming 과목의 최종 게임 프로젝트입니다.

## 주요 기능

- 방향키로 패들을 움직이고 화면 경계를 벗어나지 않도록 제한합니다.
- 공과 벽, 패들, 벽돌 사이의 충돌을 `pygame.Rect`로 판정합니다.
- 패들에 맞은 위치에 따라 공의 좌우 반사각이 달라집니다.
- 일반 벽돌과 보너스 벽돌에 서로 다른 점수를 적용합니다.
- 공을 놓치면 목숨을 차감하고 공과 패들의 위치를 초기화합니다.
- 모든 벽돌을 제거하거나 목숨을 모두 사용하면 승리·종료 화면을 표시합니다.

## 기술

`Python` · `Pygame` · `Collision Detection` · `Game Loop` · `State Management`

## 실행 방법

```bash
pip install pygame
python "brick out game(w.chatGPT).py"
```

## 관련 파일

- [Python 소스](<brick out game(w.chatGPT).py>)

## 배운 점

이벤트 처리, 프레임 단위 갱신, 객체의 위치와 충돌, 점수·목숨·승패 상태가 하나의 게임 루프 안에서 어떻게 연결되는지 경험했습니다. 개발 과정에는 생성형 AI를 보조 도구로 활용하고 코드를 직접 검토했습니다.
