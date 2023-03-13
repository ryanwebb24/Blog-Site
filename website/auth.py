"""Creates the blueprints for the authentication relates to logging in then runs the html file associated,
    currently implemented with login, logout, and sign up"""

from flask import Blueprint, redirect, render_template, url_for

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/sign-up")
def signup():
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for(("views.home")))
