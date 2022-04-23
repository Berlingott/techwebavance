from flask import Flask  # Importation de toutes les librairies necessaire au projet
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def initialisation_database(app):
    # if not path.exists("website/" + DB_NAME):#verifie si database existe, sinon la cree
    database.create_all(app=app)

    print ("Database operationelle")


# initialisation de l application et de la base de donnee

def create_app():  # Initialisation de l'application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "CeciEstUneClefSecrete"
    app.config['FLASK_ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/DBdb2.db"  # chemin ou sera enregistré la base de donnee windows
    #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////./DBdb2.db"  # chemin ou sera enregistré la base de donnee linux
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .tables import Usagers, Articles, Commentaires, articleReactionAssociation, Balises, Reactions

    database.init_app(app)

    from .views import views  # importation de nos fichiers cree, le point est parce qu'ils font partie du projet
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    initialisation_database(app)
    gestionaireLogin = LoginManager()
    gestionaireLogin.login_view = "auth.login"  # si une personne nest pas connecte, redirection a la page de login
    gestionaireLogin.init_app(app)

    # gestionnaire de connexion
    @gestionaireLogin.user_loader  # retourner le id de la base de donnee
    def load_user(id):
        return Usagers.query.get(int(id))

    return app  # On retourne l'application
