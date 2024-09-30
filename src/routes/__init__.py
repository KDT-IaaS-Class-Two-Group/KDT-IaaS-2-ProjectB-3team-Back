from flask import jsonify
from src.modules.utils.blueprint.bp_list import bp_list
from src.modules.utils.path.path_joiner import path_joiner


main_bp = bp_list.MAIN

main_bp.add_url_rule(path_joiner("/api","ml"), view_func=lambda: jsonify({"route": path_joiner("api","ml")}), methods=['POST'])