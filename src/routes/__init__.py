from flask import jsonify
from src.modules.utils.blueprint.bp_list import bp_list


main_bp = bp_list.MAIN

main_bp.add_url_rule('/api/ml', view_func=lambda: jsonify({"route": "http://localhost:8000/"}), methods=['POST'])

# @main_bp.route('/api/ml', methods=['POST'])
# def handle_ml_request():
#     # JSON 응답 생성
#     return jsonify({"message": "Hello World"})