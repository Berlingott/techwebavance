from flask import Blueprint, url_for, redirect,  render_template, request, flash
from flask_login import login_required, current_user
from . import database
from .tables import Articles
views = Blueprint("views", __name__)

@views.route("/Accueil")
@views.route("/")
def home():
    articles = Articles.query.all()
    return render_template("Accueil.html", usager=current_user, articles=articles)


@views.route("/Publier", methods=['GET', 'POST'])
@login_required #doit etre connecte pour acceder a l accueil
def creationArticle():
    if request.method == "POST":
        textarticle = request.form.get('textArticle')

        if not textarticle:
            flash('Vous devez ecrire un article!', category='error')
        else:
            flash(('Article publie'), category='success')
            articles = Articles(usagers_id=current_user.id, textArticle=textarticle)
            database.session.add(articles)
            database.session.commit()
            return redirect(url_for('views.home'))

    return render_template('Publier.html', usager=current_user)

