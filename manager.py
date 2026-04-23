from flask import Blueprint, render_template, session, request, redirect, url_for
from datetime import datetime

manager_bp = Blueprint("manager", __name__)


@manager_bp.route("/add", methods=["POST"])
def add_expense():
    data = session.get("expenses", [])

    new_expense = {
        "date": request.form["date"],
        "category": request.form["category"],
        "amount": request.form["amount"]
    }

    data.append(new_expense)
    session["expenses"] = data

    return redirect(url_for("dashboard.view_dashboard"))

@manager_bp.route("/delete", methods=["POST"])
def delete_expense():    
    index = int(request.form["index"])
    data = session.get("expenses", [])

    if 0 <= index < len(data):
        data.pop(index)

    session["expenses"] = data

    return redirect(url_for("dashboard.view_dashboard"))    