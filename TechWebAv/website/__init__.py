from flask import Flask  # Importation de toutes les librairies necessaire au projet
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from os import path
import sqlite3
from flask_migrate import Migrate
database = SQLAlchemy()
DB_NAME = "BlogDB.db"


def initialisation_database(app):
    #if not path.exists("website/" + DB_NAME):#verifie si daatabase existe, sinon la cree
        database.create_all(app=app)
        print ("Database operationelle")


def create_app():  # Initialisation de l'application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "berlingotestlaclefmaisavecun0alafin"
    app.config['FLASK_ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/berlingott/Desktop/BlogDB.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .tables import Usagers

    database.init_app(app)

    from .views import views  # importation de nos fichiers cree, le point est parce qu'ils font partie du projet
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    initialisation_database(app)
    gestionaireLogin = LoginManager()
    gestionaireLogin.login_view = "auth.login"#si une personne nest pas connecte, redirection a la page de login
    gestionaireLogin.init_app(app)



    @gestionaireLogin.user_loader #retourner le id de la base de donnee
    def load_user(id):
        return Usagers.query.get(int(id))


    return app  # On retourne l'application

