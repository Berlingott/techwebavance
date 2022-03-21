import datetime

from sqlalchemy.sql import func
from flask_login import (
    LoginManager, UserMixin, current_user,
    login_required, login_user, logout_user
)
from . import database
from sqlalchemy import Table, Column, Integer, String, MetaData



#articleReactionassociation = Table('articleReactionassociation' Base.metadata,    #relation
#Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False, primary_key=True),
#Column(database.Integer, database.ForeignKey('Articles.id', ondelete='CASCADE'), nullable=False, primary_key=True),
#Column(database.Integer, database.ForeignKey('Reactions.id', ondelete='CASCADE'), nullable=False, primary_key=True)
#)

class Commentaires(database.Model):
    #clef
    __tablename__ = 'Commentaires'
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    usagers_id = Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False)
    articlesducommentaire_id = Column(database.Integer, database.ForeignKey('Articles.id', ondelete='CASCADE'), nullable=False)
    #attributs
    textCommentaires =Column(database.String(254))
    datePublication = Column(database.DateTime(timezone=True), default=func.now())
    #backrefs

class Balises:
    __tablename__ = 'Balises'
    #clef
    id = Column(database.Integer, primary_key=True, autoincrement=True)

class Reactions:
    __tablename__ = 'Reactions'
    #clef
    id = Column(database.Integer, primary_key=True, autoincrement=True)
   # articleReaction = database.relationship("articleReaction", backref='articleReaction')


class Usagers(database.Model, UserMixin):
    #clef
    __tablename__ = 'Usagers'
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    #attributs
    nom = Column(database.String(100))
    username = Column(database.String(100), unique=True)
    password = Column(database.String(100))
    email = Column(database.String(100), unique=True)
    #backrefs
    articles = database.relationship("Articles", backref='usagers')
   # articleReaction = database.relationship("articleReaction", backref='articleReaction')

class Articles(database.Model):
    #clef
    __tablename__ = 'Articles'
    id = Column(database.Integer, primary_key=True, autoincrement=True)
    #attributs
    usagers_id = Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False)
    textArticle = Column(database.String(254))
    datePublication = Column(database.DateTime(timezone=True), default=func.now())
    #backrefs
    commentaires = database.relationship("Commentaires", backref='Articles')
   # articleReaction = database.relationship("articleReaction", backref='articleReaction')
