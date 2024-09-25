import os
from PIL import Image
import numpy as np
import json

def preprocess_image(file, output_size=(10, 10), save_dir='uploads/processed'):
    # 이미지 읽기
    img = Image.open(file)
    
    # 이미지 크기 조정
    img = img.resize(output_size)
    
    # 이미지 데이터를 numpy 배열로 변환
    img_array = np.array(img)

    # 정규화 (0-255 범위를 0-1로 조정)
    img_array = img_array / 255.0

    # 저장할 디렉토리 생성
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    # 파일 이름 생성
    file_name = os.path.splitext(os.path.basename(file.name))[0] + '.json'
    output_path = os.path.join(save_dir, file_name)
    
    # numpy 배열을 json 파일로 저장
    with open(output_path, 'w') as f:
        json.dump(img_array.tolist(), f)  # numpy 배열을 리스트로 변환 후 저장

    return output_path
