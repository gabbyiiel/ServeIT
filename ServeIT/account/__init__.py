from flask import Blueprint

bp_acc = Blueprint('bp_acc', __name__)

from . import account