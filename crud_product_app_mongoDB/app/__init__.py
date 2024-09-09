# app/__init__.py

from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize PyMongo
    mongo.init_app(app)

    # Register Blueprints for routes
    from app.routes import product_bp
    app.register_blueprint(product_bp)

    # Register error handlers
    from app.errors import register_error_handlers
    register_error_handlers(app)

    return app
