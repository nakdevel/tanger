'''
Created on 5 de mar. de 2016

@author: jr
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from ..config import config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    return app