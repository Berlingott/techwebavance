from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/Accueil")
@views.route("/")
@login_required #doit etre connecte pour acceder a l accueil
def home():
    return render_template("Accueil.html", usager=current_user)

@views.route("/creeArticle", methods=['GET', 'POST'])
@login_required
def creationArticle():
    if request.method == "POST":
        text = request.form.get('textArticle')

        if not text:
            flash('Vous devez ecrire un article!', category='error')
        else:
            flash(('Article publie'), category='success')

    return render_template('creationArticle.html', usager=current_user)