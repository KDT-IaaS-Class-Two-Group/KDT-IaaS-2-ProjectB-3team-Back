from flask import Blueprint
from .image_routes import image_bp  # image_routes 추가

# 라우트 블루프린트 생성
main = Blueprint('main', __name__)

@main.route('/')
def home():
    print("hello world")  # 요청이 들어올 때 메시지 출력
    return "<h1>Welcome to the Flask app!</h1>"

# Blueprint를 통해 라우트 등록
def register_routes(app):
    app.register_blueprint(main)
    app.register_blueprint(image_bp)  # image_routes 추가
