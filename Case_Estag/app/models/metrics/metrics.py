from sqlalchemy import select
from app.models.db import db

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(120))
    campaign_id = db.Column(db.String(120))
    cost_micros = db.Column(db.Float)
    clicks = db.Column(db.Integer)
    conversions = db.Column(db.Float)
    impressions = db.Column(db.Integer)
    interactions = db.Column(db.Integer)
    date = db.Column(db.Date)

    @staticmethod
    def load_data(start=None, end=None, order_by=None, page=1, page_size=100):
        stmt = select(Metric)

        if start and start.lower() != "null":
            stmt = stmt.where(Metric.date >= start)
        if end and end.lower() != "null":
            stmt = stmt.where(Metric.date <= end)

        if order_by and hasattr(Metric, order_by):
            stmt = stmt.order_by(getattr(Metric, order_by))

        stmt = stmt.offset((page - 1) * page_size).limit(page_size)

        rows = db.session.execute(stmt).scalars().all()

        count_stmt = select(db.func.count()).select_from(Metric)
        if start and start.lower() != "null":
            count_stmt = count_stmt.where(Metric.date >= start)
        if end and end.lower() != "null":
            count_stmt = count_stmt.where(Metric.date <= end)
        total = db.session.execute(count_stmt).scalar()

        data = [row.__dict__ for row in rows]
        for row in data:
            row.pop("_sa_instance_state", None)

        return data, total
