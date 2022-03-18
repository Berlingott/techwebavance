from sqlalchemy.sql import func
from flask_login import (
    LoginManager, UserMixin, current_user,
    login_required, login_user, logout_user
)
from . import database
from sqlalchemy import Table, Column, Integer, String, MetaData


class Usagers(database.Model, UserMixin):
    id = database.Column(database.INTEGER, primary_key=True, autoincrement=True)
    nom = database.Column(database.String(100))
    username = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(100))
    email = database.Column(database.String(100), unique=True)


