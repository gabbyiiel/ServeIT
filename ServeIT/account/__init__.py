from flask import Blueprint

bp_acc = Blueprint('acc', __name__)

from . import account