# app/preprocess/preprocess_image_for_predict.py
import torch
from torchvision import transforms

def preprocess_image_for_predict(img):
    img = img.resize((10, 10))  # 모델 입력 크기에 맞게 조정
    img_tensor = transforms.ToTensor()(img)  # (C, H, W) 형식으로 변환
    return img_tensor  # 변환된 텐서 반환
