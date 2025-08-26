#__init__.py
from flask import Flask, render_template, request, jsonify
from app.utils.create_db import create_db
from app.models.db import db, instance
from app.controllers.init_user import init_user
from app.controllers.init_metrics import init_metrics
from app.utils.decorators import *

from app.models.user.user import User
from app.controllers.metrics_controller import get_metrics

from flask_login import LoginManager
login_manager = LoginManager()

from app.controllers.auth_controller import auth_
from app.controllers.user_controller import user_

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "0000"
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    create_db(app)  

    init_user(app)
    init_metrics(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.inicio"  

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    app.register_blueprint(auth_, url_prefix='/')
    app.register_blueprint(user_, url_prefix='/')

    

    @app.route('/')
    def index():
        return render_template("inicio.html")

    return app
