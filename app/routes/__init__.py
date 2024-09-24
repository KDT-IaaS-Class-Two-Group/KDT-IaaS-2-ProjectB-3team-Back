from flask import Blueprint

# 라우트 블루프린트 생성
main = Blueprint('main', __name__)

@main.route('/')
def home():
    print("hello world")  # 요청이 들어올 때 메시지 출력
    return "<h1>Welcome to the Flask app!</h1>"
