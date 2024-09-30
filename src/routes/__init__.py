from flask import jsonify
from src.modules.utils.blueprint.bp_list import bp_list
from src.modules.utils.path.path_joiner import path_joiner
from src.modules.utils.env.env_loader import env_loader
from src.static.env.env_list_static import EnvList

main_bp = bp_list.MAIN

# main_bp.add_url_rule(path_joiner(env_loader(EnvList.MAIN_URL.value), env_loader(EnvList.EP_API.value), env_loader(EnvList.EP_ML.value)),
#     view_func=lambda: jsonify({"route": path_joiner("api","ml")}), methods=['POST'])

# main_bp.add_url_rule(path_joiner(env_loader(EnvList.MAIN_URL.value), env_loader(EnvList.EP_API.value), env_loader(EnvList.EP_ML.value)),view_func=lambda: jsonify({"route": path_joiner("api","ml")}), methods=['POST'])

main_bp.add_url_rule(
    "/api/ml",
    view_func=lambda: jsonify({"route": "http://localhost:8000"}),
    methods=["POST"]
)
