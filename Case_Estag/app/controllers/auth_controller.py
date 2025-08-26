from flask import Blueprint, render_template, request, redirect, url_for
from app.models.db import db
from app.models.user.user import User

from flask_login import login_user, logout_user, login_required

auth_ = Blueprint('auth', __name__, template_folder="templates")

@auth_.route('/inicio')
def inicio():
    return render_template("inicio.html")

@auth_.route("/validate_user", methods=["POST"])
def validated_user():
    username = request.form["username"]
    senha = request.form["senha"]
    user = User.query.filter_by(username=username).first()

    if user and user.verificar_senha(senha):
        login_user(user, remember=False)  
        return redirect(url_for("user_.home"))

    return render_template("inicio.html", erro="Usuário ou senha inválidos")


@auth_.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.inicio"))