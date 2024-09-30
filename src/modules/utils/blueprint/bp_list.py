from app.static.utils.blueprint.bp_list_static import Blueprints
from app.utils.generator.bp_generator import generate_blueprint

class BlueprintContainer:
    def __init__(self):
        
        # 블루프린트 생성 및 저장
        self.MAIN = generate_blueprint(Blueprints.MAIN.value)
        self.IMAGE = generate_blueprint(Blueprints.IMAGE.value)
        
        
    def get_blueprints(self):
        # 클래스 속성을 반복하여 블루프린트 목록을 반환
        return {name: getattr(self, name) for name in self.__dict__ if not name.startswith('__')}


# bp_list 변수에 저장
bp_list = BlueprintContainer()