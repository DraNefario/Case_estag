import pandas as pd
from app.models.db import db
from app.models.user.user import User
from werkzeug.security import generate_password_hash

def init_user(app):
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