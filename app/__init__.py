from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

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
    from app.routes import main
    app.register_blueprint(main)

    return app
