from flask import Flask
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, SECRET_KEY
from config import CLOUD_NAME, API_KEY, API_SECRET
from flask_mysql_connector import MySQL
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader
from flask_ngrok import run_with_ngrok

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
    cloudinary.config(
        cloud_name = CLOUD_NAME,
        api_key = API_KEY,
        api_secret = API_SECRET,
        )
    CSRFProtect(app)
    
    
    #import blueprints
    from .auth import bp_auth
    from .dashboard import bp_dashboard
    from .account import bp_acc
    #register blueprints
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_dashboard)
    app.register_blueprint(bp_acc)
    # run_with_ngrok(app)
    return app
    