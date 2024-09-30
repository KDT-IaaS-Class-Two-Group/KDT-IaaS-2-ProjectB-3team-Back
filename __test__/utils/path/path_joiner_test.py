from src.modules.utils.path.path_joiner import somePathModule
# from ....app.modules.utils.path.path_joiner import somePathModule

def test_somePathModule():
    # 테스트 케이스 1: 기본 경로 조합
    result = somePathModule("api", "ml")
    assert result == "api/ml"

    # 테스트 케이스 2: 절대 경로 조합
    result = somePathModule("app", "modules", "utils")
    assert result == "app/modules/utils"

    # 테스트 케이스 3: 빈 인자
    result = somePathModule()
    assert result == ""

    # 테스트 케이스 4: 슬래시가 포함된 인자
    result = somePathModule("api/", "/ml")
    assert result == "api/ml"
