from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash, session


class Recipe:
    db = "recipes"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


#Create
    @classmethod
    def create_new_recipe(cls,data):
        if not cls.validate_recipe_data(data):
            return False
        query = '''
        INSERT INTO recipes (name,description,instructions, date_made, under30)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under30)s)
        ;'''
        recipe_id = connectToMySQL(cls.db).query_db(query, data)
        return recipe_id

    @classmethod
    def get_recipe_by_id(cls,id):
        data = {
            'id': id
        }
        query = '''
        SELECT *
        FROM recipes
        WHERE id = %(id)s
        ;'''
        results = connectToMySQL(cls.db).query_db(query, data)
        if results:
            results = cls(results[0])
        return results

    @classmethod
    def update_recipe(cls,data):
        query = '''
        UPDATE recipes
        SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under30=%(under30)s
        WHERE id = %(id)s
        ;'''
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete_recipe_by_id(cls,id):
        data = {'id' : id}
        query = '''
        DELETE FROM recipes
        WHERE id = %(id)s
        ;'''

        connectToMySQL(cls.db).query_db(query,data)
        return

    @staticmethod
    def validate_recipe_data(data):
        is_valid = True
        if len(data['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False
        if len(data['description']) < 3:
            flash('Description must have at least 3 characters')
            is_valid = False
        if len(data['instructions']) < 3:
            flash('Instructions must have at least 3 characters')
            is_valid = False
        if data['date_made'] == "":
            flash('Please enter a date made')
            is_valid = False
        return is_valid