from pathlib import PurePosixPath

# 경로 조합
path_joiner = lambda *args: str(PurePosixPath(*args))