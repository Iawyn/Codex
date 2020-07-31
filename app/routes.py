from app import app
from app import db
from flask import render_template, request
from flask_login import LoginManager
from . import Bootstrap

@app.route('/')
@app.route('/home' ,methods=['GET', 'POST'])
def index():
    print(f"Flask ENV is set to: '{app.config['ENV']}")
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('accountPage.html')

#db test route
@app.route('/testDB')
def testdb():
    return 'done!'