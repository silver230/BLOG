from flask import Flask
from . import main
from flask import render_template,redirect, request, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import User,
from .. import db


app = Flask(__name__)