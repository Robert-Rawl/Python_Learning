from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe

# CREATE CONTROLLER

@app.route('/users/create', methods = ['POST'])
def create_user():
    created_user =user.User.create_user(request.form)
    if created_user:
        return redirect('/users/profile')
    return redirect('/')

# READ CONTROLLER
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/profile')
def user_profile():
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('profile.html', this_user = this_user)

@app.route('/users/login', methods = ['POST'])
def login():
    if user.User.login(request.form):
        return redirect('/users/profile')
    return redirect('/')

@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')

# UPDATE CONTROLLER

# DELETE CONTROLLER