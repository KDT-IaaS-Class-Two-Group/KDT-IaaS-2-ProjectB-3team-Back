# app/routes/image_routes.py
from flask import Blueprint, request, jsonify
import torch
from PIL import Image
from app.models.train_model import RGBClassifier  # 모델 위치에 맞게 수정
from app.preprocess.preprocess_image_for_predict import preprocess_image_for_predict  # 경로 수정

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # 이미지 처리 및 결과 얻기
    result = predict_image(file)  # process_image(file) 대신 predict_image(file)로 수정
    
    return jsonify({'result': result})

def predict_image(image_file):
    model = RGBClassifier()
    model.load_state_dict(torch.load('app/models/rgb_classifier.pth', weights_only=True))  # 모델 경로 수정
    model.eval()

    img = Image.open(image_file).convert('RGB')  # 파일 객체를 사용하여 이미지 열기
    img_tensor = preprocess_image_for_predict(img)  # 이미지 객체를 전달
    img_tensor = img_tensor.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)

    label_map = {0: 'R', 1: 'G', 2: 'B'}
    return label_map[predicted.item()]  # 예측한 클래스 반환
