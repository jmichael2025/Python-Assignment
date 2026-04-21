from flask import Flask, render_template  
app = Flask(__name__)  

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/calendar")
def calendar():
    return render_template('calendar.html') 

@app.route("/manager")
def manager():
    return render_template('manager.html')

@app.route("/editor")
def editor():
    return render_template('editor.html')

if __name__ =="__main__":  
    app.run()