from flask import Blueprint

bp = Blueprint('collection', __name__, url_prefix='/collection')

from . import routes