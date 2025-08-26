#user_controller.py
from flask import Blueprint, request, render_template, redirect, url_for
from app.models.user.user import User
from app.utils.decorators import *
from app.models.db import *
from app.controllers.metrics_controller import get_metrics
from app.controllers.metrics_controller import get_metrics as get_metrics_func

from flask_login import login_required



user_ = Blueprint("user_",__name__, template_folder="templates")
user_.add_url_rule("/get_metrics", "get_metrics", get_metrics_func, methods=["GET"])
user_.route("/get_metrics", methods=["GET"])


@user_.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@login_required
def metrics_route():
    return get_metrics()



@user_.route('/home')
@login_required
def home():
    return render_template('home.html')




