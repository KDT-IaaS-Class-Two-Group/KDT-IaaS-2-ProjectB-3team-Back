# app/routes/image_routes.py
from flask import Blueprint, request, jsonify

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    print(file)
    
    
    return jsonify({'result': True})