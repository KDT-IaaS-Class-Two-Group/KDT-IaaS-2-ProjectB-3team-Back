# test_example.py

# 테스트할 함수
def add(a, b):
    return a + b

# 테스트 함수
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0