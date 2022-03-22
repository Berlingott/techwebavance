import datetime

from sqlalchemy.sql import func
from flask_login import (
    LoginManager, UserMixin, current_user,
    login_required, login_user, logout_user
)
from . import database
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
from sqlalchemy.event import listens_for
from sqlalchemy.pool import Pool
from sqlalchemy import event, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base



class articleReactionAssociation(database.Model):
    __tablename__ = 'articleReactionAssociation'
    id = Column(database.Integer, primary_key=True, autoincrement=True, unique=True)
    usagers_id = Column(database.Integer, database.ForeignKey('Usagers.id'))
    article_id = Column(database.Integer, database.ForeignKey('Articles.id'))
    reaction_id = Column(database.Integer, database.ForeignKey('Reactions.id'))


class Commentaires(database.Model):
    # clef
    __tablename__ = 'Commentaires'
    #
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    usagers_id = Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False)
    articlesducommentaire_id = Column(database.Integer, database.ForeignKey('Articles.id', ondelete='CASCADE'),
                                      nullable=False)
    # attributs
    textCommentaires = Column(database.String(254))
    datePublication = Column(database.DateTime(timezone=True), default=func.now())
    # backrefs


class Balises(database.Model):
    __tablename__ = 'Balises'
    # clef
    id = Column(database.Integer, primary_key=True, autoincrement=True)


class Reactions(database.Model):
    __tablename__ = 'Reactions'
    # clef
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    #attributs
    nomDeLaReaction = Column(database.String(20), unique=True)
    #backrefs
    articleReactionAssociationReactions = database.relationship("articleReactionAssociation", backref='Reactions')

class Usagers(database.Model, UserMixin):
    # clef
    __tablename__ = 'Usagers'
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    # attributs
    nom = Column(database.String(100))
    username = Column(database.String(100), unique=True)
    password = Column(database.String(100))
    email = Column(database.String(100), unique=True)
    role = Column(database.String(10), default="lecteur")
    # backrefs
    articles = database.relationship("Articles", backref='usagers')
    articleReactionAssociationUsager = database.relationship("articleReactionAssociation", backref='usagers')


class Articles(database.Model):
    # clef
    __tablename__ = 'Articles'
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    # attributs
    usagers_id = Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False)
    textArticle = Column(database.String(254))
    datePublication = Column(database.DateTime(timezone=True), default=func.now())
    status = Column(database.String(20), default="brouillon")
    # backrefs
    commentaires = database.relationship("Commentaires", backref='Articles')
    articleReactionAssociationArticle = database.relationship("articleReactionAssociation", backref='Articles')



def insert_data_reaction(target, connection, **kw):
    connection.execute(target.insert(), {'nomDeLaReaction':"aime"})

event.listen(Reactions.__table__, 'after_create', insert_data_reaction)