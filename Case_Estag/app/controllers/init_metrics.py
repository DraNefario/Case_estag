import pandas as pd
from app.models.db import db
from app.models.metrics.metrics import Metric


def init_metrics(app):
    with app.app_context():
        metrics = pd.read_csv("data/metrics.csv")

        data_dicts = metrics.to_dict(orient="records") 

        db.session.bulk_insert_mappings(Metric, data_dicts)
        db.session.commit()

        print(f"{len(data_dicts)} métricas importadas com sucesso!")
