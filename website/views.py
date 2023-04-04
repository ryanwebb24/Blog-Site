"""Creates the blueprint for each url path that the user takes and calls the html file. So far only implemented home"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", name=current_user.username)