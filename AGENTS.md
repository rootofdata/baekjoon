# AGENTS.md

백준(BOJ) 문제 풀이 및 코딩테스트 대비 알고리즘 학습 저장소. 범용 코딩 에이전트를 위한 안내 문서.

## 명령어

- 실행(.py): `python "python_solutions/<파일>.py"` — 예제 입력을 표준 입력으로 전달
- 실행(.ipynb): Jupyter 또는 VS Code에서 셀 단위 실행
- 설치/의존성: 없음. Python 3 표준 라이브러리만 사용
- 테스트: 별도 프레임워크 없음. 정답 검증은 BOJ 온라인 채점으로 수행

## 구조

- `greedy/` `implementation/` `dfs_bfs/` `sorting/` `search/` `shortestpath/` `dinamic/`(DP) — 알고리즘 유형별
- `baekjoon_solutions/` — 문제 번호별 `.ipynb`
- `python_solutions/` — 문제 번호별 `.py`
- `06 이후 알고리즘/` — 백준 단계별 학습
- `scratch/` — 연습장

## 컨벤션

- 파일명: `<문제번호> <문제제목>.ipynb`, 한글 제목 그대로 사용
- 진행 상태 접두어 `(미해결)`·`(공부중)` 은 파일명 앞에 유지. 해결 시 제거하되 임의 변경 금지

## 주의

- 한글 파일명은 NFC로 통일 (자소 분리 방지)
- 노트북의 문제 이미지 attachment·셀 출력을 함부로 삭제하지 말 것
- `__pycache__/`, `.ipynb_checkpoints/`, `.DS_Store` 커밋 금지
- CLAUDE.md와 이 문서의 내용은 동일하게 유지할 것
