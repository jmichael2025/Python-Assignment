from flask import Flask, redirect, render_template, request, session, url_for  

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
    session.pop("user", None)  # Remove from session
    return redirect(url_for("login"))


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
if __name__ =="__main__":  
    app.run(debug=True)
    
