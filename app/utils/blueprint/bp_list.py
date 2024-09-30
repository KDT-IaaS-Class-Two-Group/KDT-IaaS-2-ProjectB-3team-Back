from app.static.utils.blueprint.bp_list_static import Blueprints
from app.utils.generator.bp_generator import generate_blueprint

bp_list = {
    Blueprints.MAIN.name: generate_blueprint(Blueprints.MAIN.value),
    Blueprints.IMAGE.name: generate_blueprint(Blueprints.IMAGE.value)
}