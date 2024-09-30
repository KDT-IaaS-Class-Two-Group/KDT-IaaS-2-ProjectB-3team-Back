from pathlib import Path

# 경로 조합 모듈
path_joiner = lambda *args: Path(*args).as_posix()
