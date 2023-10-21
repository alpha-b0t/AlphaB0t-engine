from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBaseNoMeta
from config import AppConfig
from app.views.api import api_bp

class Base(DeclarativeBaseNoMeta):
    pass

# Initialize the database
db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(api_bp)

    app_config = AppConfig()

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{app_config.DATABASE_USERNAME}:{app_config.DATABASE_PASSWORD}@localhost:{app_config.DATABASE_PORT}/{app_config.DATABASE_NAME}"
    db.init_app(app)

    return app