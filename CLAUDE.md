# 프로젝트

백준(BOJ) 문제 풀이와 코딩테스트 대비 알고리즘 유형별 학습 저장소.

## 환경·실행

- 언어: Python 3 (표준 입력 `input()` 기반 풀이)
- 외부 패키지 의존성 없음 (표준 라이브러리 `sys`, `collections`, `heapq`, `math` 등만 사용)
- `.ipynb` 풀이: Jupyter/VS Code에서 셀 실행. 입력은 셀 안에서 직접 값을 주거나 `input()` 사용
- `.py` 풀이: `python "python_solutions/<파일>.py"` 로 실행, 표준 입력으로 예제 입력 전달
- 별도 빌드/테스트 프레임워크 없음. 검증은 BOJ 채점으로 대체

## 폴더 구조

- `greedy/`, `implementation/`, `dfs_bfs/`, `sorting/`, `search/`, `shortestpath/`, `dinamic/` — 알고리즘 유형별 학습 (`dinamic` = DP, 철자 그대로 유지)
- `baekjoon_solutions/` — 문제 번호별 풀이 노트북(`.ipynb`)
- `python_solutions/` — 문제 번호별 `.py` 풀이
- `06 이후 알고리즘/` — 백준 단계별(입출력·조건문·반복문·배열·기하 등) 풀이
- `scratch/` — 연습장

## 컨벤션

- 파일명: `<문제번호> <문제제목>.ipynb` (예: `11047 동전 0.ipynb`). 한글 제목 그대로 사용
- 진행 상태 접두어: `(미해결)`, `(공부중)` 을 파일명 앞에 붙임 (예: `(미해결)1167 트리의 지름.ipynb`). 문제를 풀면 접두어를 제거
- 새 풀이는 문제 유형에 맞는 유형별 폴더 또는 `baekjoon_solutions/`·`python_solutions/`에 배치
- 커밋 메시지: 간결한 한국어/영어, 보통 문제 단위로 추가

## 주의

- 한글 파일명이 매우 많다. 파일 생성/이동 시 자소 분리(NFD)가 아닌 **NFC로 통일**할 것 (macOS·Windows 혼용 환경에서 깨지기 쉬움)
- 진행 상태 접두어를 임의로 바꾸거나 제거하지 말 것 — 학습 진척 관리용 표식이다
- 노트북에는 문제 설명 이미지가 attachment로 포함된 경우가 있으니 셀 출력/첨부를 함부로 지우지 말 것
- `__pycache__/`, `.ipynb_checkpoints/`, `.DS_Store` 는 커밋하지 말 것
