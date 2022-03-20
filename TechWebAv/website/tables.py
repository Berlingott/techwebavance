import datetime

from sqlalchemy.sql import func
from flask_login import (
    LoginManager, UserMixin, current_user,
    login_required, login_user, logout_user
)
from . import database
from sqlalchemy import Table, Column, Integer, String, MetaData


class Usagers(database.Model, UserMixin):
    __tablename__ = 'Usagers'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    nom = database.Column(database.String(100))
    username = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(100))
    email = database.Column(database.String(100), unique=True)
    articles = database.relationship("Articles", backref='usagers')


class Articles(database.Model):
    __tablename__ = 'Articles'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    usagers_id = database.Column(database.Integer, database.ForeignKey('Usagers.id', ondelete='CASCADE'), nullable=False)
    textArticle = database.Column(database.String(254))
    datePublication = database.Column(database.DateTime(timezone=True), default=func.now())
