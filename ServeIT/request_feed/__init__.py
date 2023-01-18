from flask import Blueprint

bp_reqfeed= Blueprint('bp_reqfeed', __name__)

from . import feed