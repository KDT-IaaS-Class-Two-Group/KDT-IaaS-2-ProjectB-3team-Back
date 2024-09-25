import io
from app.models.yolov5_model import YOLOv5Model
from .preprocessing import preprocess_image  # preprocessing.py에서 import

# YOLOv5 모델 초기화

def process_image(file):
    # 이미지를 전처리하여 저장
    processed_image_path = preprocess_image(file)

    # YOLOv5 모델에 전달하여 예측 수행 (여기서는 예시로 처리된 이미지 경로 반환)
    return {'processed_image': processed_image_path}
