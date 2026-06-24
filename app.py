from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
from dashboard import dashboard_bp  
import os
from datetime import datetime
import calendar
from collections import defaultdict

app = Flask(__name__)  
app.secret_key = "mysecret3453453"

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/process_login", methods=['POST'])
def process_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin":
            session['user'] = username
            print("Login successful")
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    expenses = session.get("expenses", [])

    for e in expenses:
        e["date_obj"] = datetime.strptime(e["date"], "%Y-%m-%d")

    return render_template("dashboard.html", expenses=expenses)

@app.route("/calendar")
def calendar_view():

    expenses = session.get("expenses", [])
    today = datetime.now()

    # Start from URL values if present
    month = int(request.args.get("month", today.month))
    year = int(request.args.get("year", today.year))

    move = request.args.get("move")

    if move == "prev":
        month -= 1
        if month == 0:
            month = 12
            year -= 1

    elif move == "next":
        month += 1
        if month == 13:
            month = 1
            year += 1

    elif move == "current":
        month = today.month
        year = today.year

    # STEP 3: ONLY apply manual override if NO move
    else:
        if request.args.get("month") and request.args.get("year"):
            month = int(request.args.get("month"))
            year = int(request.args.get("year"))

    cal = calendar.monthcalendar(year, month)

    day_totals = defaultdict(float)

    for e in expenses:
        expense_date = datetime.strptime(e["date"], "%Y-%m-%d")

        if expense_date.month == month and expense_date.year == year:
            day_totals[expense_date.day] += float(e["amount"])

    return render_template(
        "calendar.html",
        calendar_data=cal,
        day_totals=day_totals,
        month_name=calendar.month_name[month],
        month=month,
        year=year
    )

@app.route("/manager")
def manager():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('manager.html')

@app.route("/editor")
def editor():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('editor.html')

@app.route("/logout")
def logout():
    session.pop("user", None) 
    session.pop("expenses", None) 
    session.pop("total", None)  
    return redirect(url_for("login"))



@app.route("/addexpense", methods=['GET', 'POST'])
def add_expense():
    data = session.get("expenses", [])
    new_expense = {
        "id": len(data) + 1,    
        "date": request.form["date"],
        "category": request.form["category"],
        "amount": request.form["amount"]
    }

    data.append(new_expense)
    session["expenses"] = data
    session["total"] = sum(float(e["amount"]) for e in data)   
    return redirect(url_for("dashboard"))
    

@app.route("/deleteexpense/<int:expense_id>", methods=['GET', 'POST'])
def delete_expense(expense_id):
    data = session.get("expenses", [])
    current_expense = next((e for e in data if e["id"] == expense_id), None)    

    data.remove(current_expense)
    session["expenses"] = data
    session["total"] = sum(float(e["amount"]) for e in data)   
    
    return redirect(url_for("dashboard"))

@app.route("/edit/<int:expense_id>")
def edit_expense(expense_id):

    expenses = session.get("expenses", [])

    expense_to_edit = None

    for expense in expenses:
        if expense["id"] == expense_id:
            expense_to_edit = expense
            break

    return render_template(
        "editor.html",
        expense=expense_to_edit
    )
@app.route("/update/<int:expense_id>", methods=["POST"])
def update_expense(expense_id):

    expenses = session.get("expenses", [])

    for expense in expenses:

        if expense["id"] == expense_id:

            expense["date"] = request.form["date"]
            expense["category"] = request.form["category"]
            expense["amount"] = request.form["amount"]

            break

    session["expenses"] = expenses

    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    session["total"] = total

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


