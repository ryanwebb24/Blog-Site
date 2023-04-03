"""Creates the blueprints for the authentication relates to logging in then runs the html file associated,
    currently implemented with login, logout, and sign up"""

from flask import Blueprint, redirect, render_template, url_for, request

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET','POST'])
def login():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    return render_template("login.html")


@auth.route("/sign-up", methods=['GET','POST'])
def signup():
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for(("views.home")))
