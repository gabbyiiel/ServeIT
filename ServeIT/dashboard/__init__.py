from flask import Blueprint

db_user = Blueprint('db_user', __name__)

from . import dashboard