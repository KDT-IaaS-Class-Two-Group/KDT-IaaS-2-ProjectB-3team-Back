import subprocess
import sys

# 워크 스페이스에서 실행해야 합니다.
def install_requirements():
    try:
        # requirements.txt 파일에서 패키지 설치
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("모든 패키지가 성공적으로 설치되었습니다.")
    except subprocess.CalledProcessError as e:
        print("패키지 설치 중 오류가 발생했습니다.")
        print(e)

if __name__ == "__main__":
    install_requirements()
