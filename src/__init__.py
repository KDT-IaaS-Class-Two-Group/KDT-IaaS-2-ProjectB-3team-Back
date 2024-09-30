from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from src.routes.modules.register_routes import register_routes
from src.modules.utils.blueprint.bp_list import bp_list

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)

    register_routes(app, *bp_list.get_blueprints().values())

    return app
