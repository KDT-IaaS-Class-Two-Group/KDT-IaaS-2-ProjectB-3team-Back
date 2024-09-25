# app/routes/image_routes.py
from flask import Blueprint, request, jsonify
from app.services.image_service import process_image

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    print(file)
    
    # 이미지 처리 및 결과 얻기
    result = process_image(file)
    
    print(result)
    
    return jsonify({'result': result})