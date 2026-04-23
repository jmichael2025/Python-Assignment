# Python-Assignment

WalletWatcher Application

WalletWatcher is a lightweight personal expense tracking web application built with Python (Flask), JavaScript, and HTML5. It allows users to log, manage, and visualize their expenses through a simple and intuitive dashboard.
🔐 User login system (session-based authentication)
📊 Dashboard for viewing expenses
➕ Add and ❌ delete expenses
📅 Calendar view for tracking spending over time
📈 Expense chart visualization
🧑‍💼 Role-based pages (Manager / Editor views)
💾 Session-based data storage (no database required)


Tech Stack
Backend: Python, Flask
Frontend: HTML5, JavaScript, CSS
Templating: Jinja2
Server: Gunicorn (for production deployment)


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
│   └── expenses_chart.html
│
├── static/
│   ├── css/
│   └── js/
│
├── requirements.txt
└── README.md

⚙️ Installation
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
