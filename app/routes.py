import os
import secrets
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash
from PIL import Image
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from .forms import LoginForm, RegisterForm, UpdateAccountForm
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
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('accountPage.html', title='Account'
                            , image_file=image_file)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn    


@app.route("/editProfile", methods=['GET', 'POST'])
@login_required
def EditAccount():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('EditAccount'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('editProfile.html', title='editProfile',
                           image_file=image_file, form=form)    