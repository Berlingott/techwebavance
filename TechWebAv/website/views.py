from flask import Flask,Blueprint, url_for, redirect, render_template, request, flash
from flask_login import login_required, current_user


from . import database
from .tables import Articles, Usagers
from .tables import Commentaires
from .tables import Reactions
from .tables import articleReactionAssociation

views = Blueprint("views", __name__)


@views.route("/Accueil")
@views.route("/")
def home():
    articles = Articles.query.all()
    return render_template("Accueil.html", usager=current_user, articles=articles)


@views.route("/Publier", methods=['GET', 'POST'])
@login_required  # doit etre connecte pour acceder a l accueil
def creationArticle():
    if current_user.role == "admin" or current_user.role == "autheur":
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


@views.route("/supprimeArticle/<articleid>")
@login_required
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


@views.route("/creeCommentaire/<article_id>", methods=['POST'])
@login_required
def creeCommentaire(article_id):
    commentaire = request.form.get("textCommentaire")
    if request.method == "POST":
        commentaire = Commentaires(usagers_id=current_user.id, textCommentaires=commentaire,
                                   articlesducommentaire_id=article_id)
        database.session.add(commentaire)
        database.session.commit()
    return redirect(url_for("views.home"))


@views.route("/supprimerCommentaire/<commentaires_id>")
@login_required
def supprimerCommentaire(commentaires_id):
    commentaire = Commentaires.query.filter_by(id=commentaires_id).first()
    if current_user.id == commentaire.usagers_id:
        flash("Article supprime")
        database.session.delete(commentaire)
        database.session.commit()
    return redirect(url_for("views.home"))


@views.route("/aimerArticles/<articles_id>", methods=['GET'])
@login_required
def aimerArticles(articles_id):
    article = Articles.query.filter_by(id=articles_id).first()
    jaime = articleReactionAssociation.query.filter_by(article_id=articles_id, usagers_id=current_user.id).first()
    reaction = Reactions.query.filter_by(nomDeLaReaction="aime").first()
    if article:
        if jaime:

            database.session.delete(jaime)
            database.session.commit()
        else:
            relation = articleReactionAssociation(usagers_id=current_user.id, article_id=article.id,
                                                  reaction_id=reaction.id)
            database.session.add(relation)
            database.session.commit()
    return redirect(url_for("views.home"))


@views.route("/publieoubrouillon/<articles_id>", methods=['GET'])
@login_required
def publieoubrouillon(articles_id):
    if current_user.role == "admin" or current_user.role == "autheur":
        article = Articles.query.filter_by(id=articles_id).first()

        if article:
            if article.status == "publie":
                article.status = "brouillon"
            else:
                article.status = "publie"
            database.session.commit()
    return redirect(url_for("views.home"))


# ------Partie Admin---


@views.route("/adminrechercheusager")
@login_required
def adminrechercheusager():
    if current_user.role == "admin":
        return render_template('adminRechercheUser.html', usager=current_user)

    return redirect(url_for("views.home"))


@views.route("/adminrechercheuseager", methods=['POST'])
@login_required  # doit etre connecte pour acceder a l accueil
def adminrechercheuseagerSoumis():
    if current_user.role == "admin":
        rechercheutilisateur = request.form.get('adminrechercheuseagerSoumis')
        if rechercheutilisateur:
            resultat = Usagers.query.filter_by(username=rechercheutilisateur).first()
            return render_template('ModCompte.html', usager=current_user, resultat=resultat)
    return redirect(url_for('views.home'))


@views.route("/api/article", methods=['GET'])
@login_required
def listerTousLesItems():
    articles = Articles.query.all()
    return render_template("apiBase.html",  articles=articles)


@views.route("/api/article/<articles_id>", methods=['GET'])
def listerUnItem(articles_id):
    article = Articles.query.filter_by(id=articles_id)
    return render_template("apiBase.html",  articles=article)


@views.route("/api/article/", methods=['PUT'])
def ajouterUnItem():
    tmp = request.get_json(force=True)
    usagers_id = tmp['usagers_id']
    textArticle = tmp['textArticle']

    article = Articles(usagers_id=usagers_id,textArticle=textArticle)
    database.session.add(article)
    database.session.commit()
    articlecree = Articles.query.order_by(Articles.id.desc()).first().id
    #return render_template("apiBase.html",  articles_id=articlecree)
    return redirect(("/api/articlecree/"+str(articlecree)))



@views.route("/api/articlecree/<articles_id>", methods=['GET'])
def itemCree(articles_id):
    article = Articles.query.filter_by(id=articles_id)
    return render_template("apiArticleCree.html",  articles=article)


@views.route("/api/article/", methods=['POST'])
def modifierUnItem():
    tmp = request.get_json(force=True)
    textArticleapi = tmp['textArticle']
    articleIdapi = tmp['article_id']

    article = Articles.query.filter_by(id=articleIdapi).first()
    article.textArticle=textArticleapi

    database.session.commit()

    return redirect(("/api/articlemod/"+str(articleIdapi)))


@views.route("/api/articlemod/<articles_id>", methods=['GET'])
def itemMod(articles_id):
    article = Articles.query.filter_by(id=articles_id)
    return render_template("apiArticlemod.html",  articles=article)

@views.route("/api/article/<articles_id>", methods=['DELETE'])
def supprimerUnItem(articles_id):

    article = Articles.query.filter_by(id=articles_id).first()
    commentaires = Commentaires.query.filter_by(articlesducommentaire_id=articles_id).all()
    for commentaires in commentaires:
        database.session.delete(commentaires)

    database.session.delete(article)
    database.session.commit()
    return ('', 204)
