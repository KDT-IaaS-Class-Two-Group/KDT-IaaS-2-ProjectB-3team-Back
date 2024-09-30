from ..utils.generator.bp_generator import generate_blueprint
from flask import jsonify
from app.utils.blueprint.bp_list import bp_list


main_bp = bp_list

# main_bp.add_url_rule('/', view_func=lambda: "<h1>ㅎ_ㅇ</h1>")

@main_bp.route('/')
def home():
    return "<h1>ㅎ_ㅇ</h1>"



@main_bp.route('/api/ml', methods=['POST'])
def handle_ml_request():
    # JSON 응답 생성
    return jsonify({"message": "Hello World"})