from flask import Blueprint

bp_user_db = Blueprint('db_user', __name__)

from . import dashboard