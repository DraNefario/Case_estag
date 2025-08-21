from models.db import db

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(120))
    campaign_id = db.Column(db.String(120))
    cost_micros = db.Column(db.Float)
    clicks = db.Column(db.Integer)
    conversions = db.Column(db.Float)
    impressions = db.Column(db.Float)
    interactions = db.Column(db.Float)
    date = db.Column(db.Date)
