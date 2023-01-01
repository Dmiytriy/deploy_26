from flask import Flask
from db import db
from views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_app:flask_app_password@pg/flask_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main_bp)

    return app

a = 1