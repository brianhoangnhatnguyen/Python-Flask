from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
db_name = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "cookies"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    # db.init_app(app)
    #
    from .views import views
    from .auth import auth

    app.register_blueprint(views, URL_prefix="/")
    app.register_blueprint(auth, URL_prefix="/")

    return app
