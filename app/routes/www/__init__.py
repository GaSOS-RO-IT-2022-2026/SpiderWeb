from flask import Blueprint

www = Blueprint("www", __name__)

from .views import *