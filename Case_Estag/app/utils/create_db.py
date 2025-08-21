#create_db.py
from flask import Flask
from app.models.db import *


def create_db(app:Flask):
    with app.app_context():
      db.drop_all()
      db.create_all()