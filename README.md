# Python-Assignment

WalletWatcher Application

WalletWatcher is a lightweight personal expense tracking web application built with ** Flask, Python, html, css nad Javascript. It helps allows users to manage daily expenses, track spending hadits,and view monthly insights through a clean dashboard.
---
Features

🔐 Secure session-based user login system
📊 Dashboard for viewing expenses
➕ Add new expenses easily
✏️ Edit existing expense records
❌ Delete unwanted expenses
📅 Calendar view for monthly expense tracking
🧑‍💼 simple user session management
💾 Session-based data storage (no database required)

---

Tech Stack

Backend: Python, Flask
Frontend: HTML5, JavaScript, CSS3
Templating Engine: Jinja2
Deployment: Gunicorn (Render)

---

📁 Project Structure
WalletWatcher/
│
├── app.py
├── dashboard.py
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── calendar.html
│   ├── manager.html
│   ├── editor.html
├── static/
│   ├── css/
│   └── js/
├── requirements.txt
└── README.md

---

Installation

Clone the repository:
git clone https://github.com/jmichael2025/Python-Assignment
cd walletwatcher
Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:
pip install -r requirements.txt


▶️ Running Locally
python app.py
Then open your browser at:
http://127.0.0.1:5000


🌐 Deployment (Render)

WalletWatcher is configured to run on Render.

Start Command:
gunicorn app:app --bind 0.0.0.0:$PORT

Important Notes:
The app must bind to 0.0.0.0
The port must come from the PORT environment variable

🔑 Default Login
Username: admin
Password: admin
