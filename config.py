import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 예시입니다. 얼마든지 수정 가능.
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MODEL_PATH = os.getenv('MODEL_PATH')
    DEBUG = os.getenv('FLASK_DEBUG', False)
