from flask import Flask
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS, SECRET_KEY
from flask_mysql_connector import MySQL

mysql = MySQL()


def create_app(test_app=None):
    # instantiate Flask app
    app = Flask(__name__, instance_relative_config=True)
    # setup database
    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY,
        MYSQL_HOST = DB_HOST,
        MYSQL_DATABASE = DB_NAME,
        MYSQL_USER = DB_USER,
        MYSQL_PASSWORD = DB_PASS,
    )

    #import blueprints
    from .auth import auth
    #register blueprints
    app.register_blueprint(auth)
    return app