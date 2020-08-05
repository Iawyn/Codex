from . import app, db, login_manager, bcrypt
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from .models import User 
from .forms import LoginForm, RegisterForm
import email_validator
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():  #if block has been submited
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')#generate a 80 chracter long encrypted password 
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>' + form.username.data + ' ' +  form.email.data + ' ' + form.password.data + ' ' + '</h1>'
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return '<h1>Niaceuu </h1>'
        #return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            #return redirect(next_page) if next_page else redirect(url_for('home'))
            return '<h1>Niceu</h1>'
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='SignIn', form=form)