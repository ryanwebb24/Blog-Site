"""Creates the blueprint for each url path that the user takes and calls the html file. So far only implemented home"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")
