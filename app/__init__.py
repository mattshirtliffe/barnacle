from flask import Flask


from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

db = SQLAlchemy()
from app.models import Lead, User


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.routes.landing import landing
    app.register_blueprint(landing)

    from app.routes.auth import auth
    app.register_blueprint(auth)


    return app