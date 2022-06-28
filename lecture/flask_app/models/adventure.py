

from unittest import result
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.controllers.adventures import edit_adventure
from flask_app.models import user
from flask import flash, session


class Adventure:
    db = "users_adventures"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.place = data['place']
        self.date = data['date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.adventurer = None

    #CREATE adventure SQL
    @classmethod
    def create_adventure(cls,data):
        if not cls.validate_adventure_data(data):# NEED VALIDATION METHOD
            return False
        query = '''
        INSERT INTO adventures (title, place, date, description, user_id)
        VALUES (%(title)s,%(place)s,%(date)s,%(description)s,%(user_id)s)
        ;'''
        adventure_id = connectToMySQL(cls.db).query_db(query,data)

        return adventure_id

    #READ adventure SQL
    @classmethod
    def get_adventure_by_id(cls,id):
        data = {'id' : id}
        query = '''
        SELECT *
        FROM adventures
        WHERE id = %(id)s
        ;'''
        results = connectToMySQL(cls.db).query_db(query,data)
        if results:
            results = cls(results[0])
        return results

    @classmethod 
    def get_all_adventures(cls):
        query = '''
        SELECT *
        FROM adventures
        JOIN users
        ON adventures.user_id = users.id
        ;'''
        result = connectToMySQL(cls.db).query_db(query)
        all_adventures = []
        if not result:
            return result
        for this_adventure in result:
            new_adventure = cls(this_adventure)
            this_adventurer = {
                'id' : this_adventure['users.id'],
                'first_name' : this_adventure['first_name'],
                'last_name' : this_adventure['last_name'],
                'email' : this_adventure['email'],
                'password' : this_adventure['password'],
                'created_at' : this_adventure['users.created_at'],
                'updated_at' : this_adventure['users.updated_at']
            }
            new_adventure.adventurer = user.User(this_adventurer)
            all_adventures.append(new_adventure)
        return all_adventures


    #UPDATE adventure SQL
    @classmethod
    def update_adventure(cls, data):
        query = '''
        UPDATE adventures
        SET title=%(title)s, place=%(place)s, date=%(date)s, description=%(description)s
        WHERE id =%(id)s
        ;'''

        result = connectToMySQL(cls.db).query_db(query,data)
        return result


    #DELETE adventure SQL
    @classmethod
    def delete_adventure_by_id(cls, id):
        data = {'id' : id}
        query = '''
        DELETE FROM adventures
        WHERE id = %(id)s
        ;'''
        connectToMySQL(cls.db).query_db(query, data)
        return

    #VALIDATION adventure SQL
    @staticmethod
    def validate_adventure_data(data):
        is_valid = True
        if len(data['title']) < 3:
            flash('Title must be at least 3 characters')
            is_valid = False
        if len(data['place']) < 3:
            flash('Place must have at least 3 characters')
            is_valid = False
        if len(data['date']) < 3:
            flash('Must have a date')
            is_valid = False
        if len(data['description']) < 10:
            flash('description must be at least 10 characters')
            is_valid = False
        if data['user_id'] != data['user_id']:
            flash( 'Not the right user')
            is_valid = False
        return is_valid



@app.route('/shows/edit/<int:id>', methods= ['POST','GET'])
def edit_show(id):
    if request.method == 'GET':
        this_show = show.Show.get_show_by_id(id)
        return render_template('edit_show.html', this_show=this_show)
    if request.method == 'POST':
        show.Show.update_show(request.form)
        return redirect('/user/dashboard')