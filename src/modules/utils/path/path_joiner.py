from pathlib import Path

# 경로 조합 모듈
somePathModule = lambda *args: Path(*args).as_posix()
