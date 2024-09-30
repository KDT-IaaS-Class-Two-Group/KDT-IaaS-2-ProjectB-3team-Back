from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.modules.register_routes import register_routes
from app.utils.generator.bp_generator import generate_blueprint



def create_app():
    
    main_bp = generate_blueprint("main")
    image_bp = generate_blueprint("image_bp")
    
    # .env 파일 로드
    load_dotenv()

    # Flask 앱 인스턴스 생성
    app = Flask(__name__)

    # Flask 앱의 설정값을 .env 파일이나 config.py에서 불러오기
    app.config.from_object('config.Config')

    # 필요한 플러그인 초기화 (예: CORS)
    CORS(app)

    # 라우트 블루프린트 등록
    register_routes(app, main_bp, image_bp)  # main과 image_routes를 함께 등록

    return app
