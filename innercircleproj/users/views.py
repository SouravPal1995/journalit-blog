from PIL import Image
import os
import secrets
from flask import Blueprint, url_for, redirect, render_template, request, flash, current_app
from innercircleproj.users.forms import Registration, Login, UpdateUser
from innercircleproj.models import User
from innercircleproj import db
from innercircleproj import login_manager
from flask_login import login_required, login_user, logout_user, current_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('core.home'))
    form = Registration()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user = User(name, email, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congrats...You just registered')
        return redirect(url_for('user.login'))
    return render_template('register.html', form = form)

@user_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember = False)
            flash('Your are logged in')
            next = request.args.get('next')
            if next:
                return redirect(next)
            else:
                return redirect(url_for('core.home'))
        else:
            flash('Login Unsuccessful. Please check email or password')
    return render_template('login.html', form = form)

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))

def add_profile_pic(pic_file):
    filename = pic_file.filename
    ext = filename.split('.')[-1]
    new_filename = secrets.token_hex(8) + '.' + ext
    file_path = os.path.join(current_app.root_path, 'static/profile_pics/', new_filename)
    image = Image.open(pic_file)
    image.thumbnail((125, 125))
    image.save(file_path)
    return new_filename

@user_bp.route('/account', methods =['GET', 'POST'])
@login_required
def account():
    form=UpdateUser()
    if form.validate_on_submit():
        if form.profile_pic.data:
            current_user.profile_pic = add_profile_pic(form.profile_pic.data)
        if form.name.data:
            current_user.name = form.name.data
        if form.email.data:
            current_user.email = form.email.data
        else:
            form.email.data = current_user.email
        db.session.commit()
        flash('User info has been updated!!')
        return redirect(url_for('user.account'))
    profile_picture = url_for("static", filename="profile_pics/"+current_user.profile_pic)
    return render_template('account.html', profile_picture = profile_picture, form  = form)



        
