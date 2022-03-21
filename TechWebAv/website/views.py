from flask import Blueprint, url_for, redirect,  render_template, request, flash
from flask_login import login_required, current_user
from . import database
from .tables import Articles
from .tables import Commentaires
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

@login_required
@views.route("/supprimeArticle/<articleid>")
def supprimeArticle(articleid):
    article = Articles.query.filter_by(id=articleid).first()
    commentaires = Commentaires.query.filter_by(articlesducommentaire_id=articleid).all()
    if current_user.id == article.usagers_id:
        flash("Article supprime")
        for commentaires in commentaires:
            database.session.delete(commentaires)
        database.session.delete(article)
        database.session.commit()
    return redirect(url_for("views.home"))

@login_required
@views.route("/creeCommentaire/<article_id>", methods=['POST'])
def creeCommentaire(article_id):
    commentaire = request.form.get("textCommentaire")
    if request.method == "POST":
        commentaire = Commentaires(usagers_id=current_user.id, textCommentaires=commentaire,
                                   articlesducommentaire_id=article_id)
        database.session.add(commentaire)
        database.session.commit()
    return redirect(url_for("views.home"))

@login_required
@views.route("/supprimerCommentaire/<commentaires_id>")
def supprimerCommentaire(commentaires_id):
    commentaire = Commentaires.query.filter_by(id=commentaires_id).first()
    if current_user.id == commentaire.usagers_id:
        flash("Article supprime")
        database.session.delete(commentaire)
        database.session.commit()
    return redirect(url_for("views.home"))