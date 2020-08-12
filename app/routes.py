from app import app
from app import db
from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from . import Bootstrap

@app.route('/')
@app.route('/home' ,methods=['GET', 'POST'])
def index():
    print(f"Flask ENV is set to: '{app.config['ENV']}")
    return render_template('index.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
@login_required
def account():
    return render_template('accountPage.html', title='Account')