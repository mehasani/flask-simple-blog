from app import app
from flask import render_template, redirect, flash
from app.administrator.models import Administrator
from app.administrator.forms import AdministratorLoginForm
from app.extensions import bcrypt
from flask_login import login_user, current_user, logout_user


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin')

    form = AdministratorLoginForm()
    if form.validate_on_submit():
        administrator = Administrator.query.filter_by(email=form.email.data).first()
        if administrator and bcrypt.check_password_hash(administrator.password, form.password.data):
            login_user(administrator)
            flash('you logged in successfully', 'success')
            return redirect('/admin')
        else:
            flash('email or password is wrong', 'danger')
    return render_template('administrator/login.html', form=form)


@app.route('/admin/logout')
def logout():
    logout_user()
    return redirect('/')
