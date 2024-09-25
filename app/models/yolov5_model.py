# app/models/yolov5_model.py
import torch

class YOLOv5Model:
    def __init__(self):
        # YOLOv5s 모델 로드
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def predict(self, image):
        # 이미지에서 예측 수행
        results = self.model(image)
        return results.pandas().xyxy[0].to_dict(orient="records")
