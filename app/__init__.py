# app/__init__.py
from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_bootstrap4 import BE
from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)
    
    app.register_blueprint(auth)  # Registrando el blueprint
    
    return app