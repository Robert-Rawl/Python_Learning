
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, adventure

@app.route('/adventures/create', methods=['POST', 'GET'])
def create_adventures():
    if 'user_id' in session:
        if request.method == 'GET':
            return render_template('create_adventure.html')
        if adventure.Adventure.create_adventure(request.form):
            return redirect('/users/profile')
        else:
            return render_template('create_adventure.html')
    return redirect('/')
#READ Controllers
@app.route('/adventures/all')
def show_all_adventures():
    all_adventures = adventure.Adventure.get_all_adventures()
    return render_template('all_adventures.html', all_adventures=all_adventures)

@app.route('/adventures/info/<int:id>')
def show_adventure_details(id):
    this_adventure = adventure.Adventure.get_adventure_by_id(id)
    return render_template('info.html', this_adventure=this_adventure)


#Update Controllers
@app.route('/adventures/edit/<int:id>', methods=['POST', 'GET'])
def edit_adventure(id):
    if request.method == "GET":
        this_adventure = adventure.Adventure.get_adventure_by_id(id)
        return render_template('edit_adventure.html', this_adventure = this_adventure)

    if request.method == "POST":
        adventure.Adventure.update_adventure(request.form)
        return redirect('/users/profile')





        


#Delete Controllers
@app.route('/adventures/delete/<int:id>')
def delete_adventure(id):
    this_adventure = adventure.Adventure.get_adventure_by_id(id)
    if this_adventure.user_id == session['user_id']:
        adventure.Adventure.delete_adventure_by_id(id)
        return redirect('/users/profile')
    else:
        return render_template('bad_bad.html')

