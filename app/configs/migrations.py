from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    #import here all our models


    Migrate(app, app.db)