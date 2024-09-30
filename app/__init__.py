from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from ..app.routes.image_routes import image_bp  # image_routes 추가
from app.routes import register_routes  # 라우트 등록 함수 가져오기

def create_app():
    # .env 파일 로드
    load_dotenv()

    # Flask 앱 인스턴스 생성
    app = Flask(__name__)

    # Flask 앱의 설정값을 .env 파일이나 config.py에서 불러오기
    app.config.from_object('config.Config')

    # 필요한 플러그인 초기화 (예: CORS)
    CORS(app)

    # 라우트 블루프린트 등록
    register_routes(app, main, image_bp)  # main과 image_routes를 함께 등록

    return app
