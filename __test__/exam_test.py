# 테스트할 함수
def add(a, b):
    return a + b

# 테스트 함수
def test_add():
    """add 함수의 동작을 테스트합니다."""
    assert add(1, 2) == 3  # 1과 2를 더하면 3이어야 합니다.
    assert add(-1, 1) == 1  # -1과 1을 더하면 0이어야 합니다.
    assert add(0, 0) == 0   # 0과 0을 더하면 0이어야 합니다.
