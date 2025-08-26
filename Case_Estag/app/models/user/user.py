from flask_login import UserMixin
from app.models.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(200))
    role = db.Column(db.String(200))

    def verificar_senha(self, senha):
        return check_password_hash(self.password_hash, senha)
    
    def has_role(self, role):
        return self.role == role
