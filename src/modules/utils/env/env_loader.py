import os
from dotenv import load_dotenv


def env_loader(envName):
    # 처음에 기본 .env 파일을 로드합니다.
    load_dotenv()  # .env 파일을 먼저 로드합니다.
    
    # ENV_MODE에 따라 적절한 .env 파일을 결정합니다.
    env_mode = os.getenv("ENV_MODE")
    env_file = ".env.development" if env_mode == "development" else ".env.production"
    
    # 환경 변수 파일을 다시 로드합니다.
    load_dotenv(env_file)
    
    # 주어진 환경 변수 이름에 해당하는 값을 반환합니다.
    return os.getenv(envName)