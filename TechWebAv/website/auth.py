from flask import request, Blueprint, render_template, redirect, url_for, request, flash
from . import database

auth = Blueprint("auth", __name__)
from .tables import Usagers
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nom = request.form.get("nom")
        password = request.form.get("password")
        passwordconfirmation = request.form.get("passwordconfirmation")
        username = request.form.get("username")
        email = request.form.get("email")
        usager_existe = Usagers.query.filter_by(username=username).first()
        email_existe = Usagers.query.filter_by(email=email).first()
        if email_existe or usager_existe:  # todo inverser logique pour defaut non correct par securite
            flash('informations already used!', 'error')
        elif password != passwordconfirmation:
            flash('Les mots de passe ne correspondent pas', 'error')  # todo regex de courriel
        else:
            nouvel_utilisateur = Usagers(email=email, username=username,
                                         password=generate_password_hash(password, method='sha256'), nom=nom)
            database.session.add(nouvel_utilisateur)
            database.session.commit()
            login_user(nouvel_utilisateur, remember=True)
            flash('Account Created!')
            return redirect(url_for('views.home'))

    return render_template("signup.html", usager=current_user)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get("password")
        email = request.form.get("email")

        usager = Usagers.query.filter_by(email=email).first()
        if usager:
            if check_password_hash(usager.password, password):
                flash('Connexion reussi', 'success')
                login_user(usager, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Email ou mot de passe incorrect', 'error')
        else:
            flash('Email ou mot de passe incorrect', 'error')

    return render_template("login.html", usager=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
