# metrics_controller.py
from flask import jsonify, request
from flask_login import login_required, current_user
from app.models.metrics.metrics import Metric
import pandas as pd

@login_required
def get_metrics():
    start = request.args.get("start_date")
    end = request.args.get("end_date")
    order_by = request.args.get("order_by")
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("page_size", 100))

    data, total = Metric.load_data(start, end, order_by, page, page_size)
    df = pd.DataFrame(data)

    if not current_user.has_role("admin"):
        df = df.drop(columns=["cost_micros"], errors="ignore")

    return {
        "data": df.to_dict(orient="records"),
        "total": total,
        "page": page,
        "page_size": page_size
    }
