from flask import Blueprint

wap = Blueprint('wap', __name__)

from . import views