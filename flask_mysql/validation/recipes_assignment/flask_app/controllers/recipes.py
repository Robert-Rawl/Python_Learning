from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from flask_app.models.user import User


#Create Controller
@app.route('/recipes/create', methods=['POST', 'GET'])
def create_recipe():
    if 'user_id' in session:
        if request.method == 'GET':
            return render_template('create_recipe.html')
        if recipe.Recipe.create_new_recipe(request.form):
            return redirect('/users/profile')
        else:
            return render_template('create_recipe.html')
    return redirect('/')


#Read Controller

#Update Controller

#Delete Controller
