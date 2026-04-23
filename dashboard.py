from flask import Blueprint, render_template, session, request, redirect, url_for
from datetime import datetime

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def view_dashboard():
    expenses = session.get('expenses', [])
    breakpoint()
    month = request.args.get("month")

    if not month:
        month = datetime.now().strftime("%Y-%m")

    
    # Filter by month
    filtered = []
    total = 0

    for e in expenses:
        if e["date"].startswith(month):
            filtered.append(e)
            total += float(e["amount"])
    

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total=total,
        current_month=month
    )


@dashboard_bp.route("/add", methods=["POST"])
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


@dashboard_bp.route("/delete", methods=["POST"])
def delete_expense():
    index = int(request.form["index"])
    data = session.get("expenses", [])

    if 0 <= index < len(data):
        data.pop(index)

    session["expenses"] = data

    return redirect(url_for("dashboard.view_dashboard"))


@dashboard_bp.route("/manager")
def manager():
    return render_template("manager.html")

