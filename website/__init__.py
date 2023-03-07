"""This file initializes the blog site"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    """Initializes the app and creates basic url pathways for the other files"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "basicpassword"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
