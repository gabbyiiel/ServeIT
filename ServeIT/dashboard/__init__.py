from flask import Blueprint

bp_dashboard = Blueprint('bp_dashboard', __name__)

from . import dashboard