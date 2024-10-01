from flask import Flask
from flask_cors import CORS
from src.routes.modules.register_routes import register_routes
from src.modules.utils.blueprint.bp_list import bp_list

def create_app():
    """
    Flask 애플리케이션 인스턴스를 생성하고 설정하는 함수입니다.

    1. 환경 변수 파일(.env)을 로드합니다.
    2. Flask 애플리케이션 인스턴스를 생성합니다.
    3. 설정 객체(config.Config)에서 설정을 로드합니다.
    4. CORS(Cross-Origin Resource Sharing)를 활성화하여 외부 요청을 허용합니다.
    5. 등록된 블루프린트를 사용하여 라우트를 설정합니다.

    Returns:
        app: 설정된 Flask 애플리케이션 인스턴스
    """
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)

    register_routes(app, *bp_list.get_blueprints().values())

    return app
