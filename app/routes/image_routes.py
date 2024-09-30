# app/routes/image_routes.py
from flask import request, jsonify
from app.utils.generator.bp_generator import generate_blueprint

image_bp = generate_blueprint("image_bp")

@image_bp.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    print(file)
    
    return jsonify({'result': True})