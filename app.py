from flask import Flask, redirect, render_template, request, session, url_for, Blueprint
from dashboard import dashboard_bp  

app = Flask(__name__)  
app.secret_key = "mysecret3453453"


@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route("/calendar")
def calendar():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('calendar.html') 

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
    return redirect(url_for("dashboard.view_dashboard"))
    

@app.route("/deleteexpense/<int:expense_id>", methods=['GET', 'POST'])
def delete_expense(expense_id):
    data = session.get("expenses", [])
    current_expense = next((e for e in data if e["id"] == expense_id), None)    

    data.remove(current_expense)
    session["expenses"] = data
    session["total"] = sum(float(e["amount"]) for e in data)   
    
    return redirect(url_for("dashboard.view_dashboard"))


@app.route("/process_login", methods=['GET', 'POST'])
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

@app.route('/expenses_chart')
def expenses_chart():
    expenses = session.get('expenses', [])
    return render_template('expenses_chart.html', expenses=expenses)

app.register_blueprint(dashboard_bp)

if __name__ =="__main__":  
    app.run(debug=True)
    


