from flask import Flask  # Importation de toutes les librairies necessaire au projet
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():  # Initialisation de l'application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "berlingotestlaclefmaisavecun0alafin"

    from .views import views  # importation de nos fichiers cree, le point est parce qu'ils font partie du projet
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app  # On retourne l'application
