#__init__.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
from app.utils.create_db import create_db
from werkzeug.security import generate_password_hash
from app.models.db import db, instance
from app.models.user.user import User

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "0000"
    app.config['SQLALCHEMY_DATABASE_URI'] = instance
    db.init_app(app)

    create_db(app)  

    with app.app_context():
        users = pd.read_csv("data/users.csv")

        for _, row in users.iterrows():

            if not User.query.filter_by(username=row["username"]).first():
                user = User(
                    username=row["username"],
                    password_hash=generate_password_hash(row["password"]),
                    role=row["role"]
                )
                db.session.add(user)

        db.session.commit()
        print("Usuários importados com sucesso!")

    return app
