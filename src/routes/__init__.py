from flask import jsonify
from src.modules.utils.blueprint.bp_list import bp_list
from src.modules.utils.path.path_joiner import path_joiner
from src.modules.utils.env.env_loader import env_loader
from src.static.env.env_list_static import EnvList
from src.static.utils.symbols.forward_slash_static import forward_slash
from src.static.routes.__init__static import env_values_for_join

bp_list.MAIN.add_url_rule(
    path_joiner(forward_slash, *[env_loader(value) for value in env_values_for_join]),
    view_func=lambda: jsonify({"route": env_loader(EnvList.ML_MAIN_URL.value)}),
    methods=["POST"]
)
