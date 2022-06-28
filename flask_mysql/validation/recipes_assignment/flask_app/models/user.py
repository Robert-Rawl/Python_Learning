from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models import recipe
from flask import flash,session
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class User:
    db = "recipes"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []


# CREATE SQL
    @classmethod
    def create_user(cls,data):
        if not cls.validate_user_reg_data(data):# NEED VALIDATION METHOD
            return False
        data = cls.parse_registration_data(data) # NEED PARSE DATA METHOD
        query = '''
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        ;'''
        user_id = connectToMySQL(cls.db).query_db(query,data)
        session['user_id'] = user_id
        return user_id


# READ SQL
    @classmethod
    def get_user_by_email(cls,email):
        data = {
            'email' : email
        }
        query = '''
        SELECT * 
        FROM users
        WHERE email = %(email)s
        ;'''
        user = MySQLConnection(cls.db).query_db(query,data)
        if user:
            user = cls(user[0])
        return user

    @classmethod
    def get_user_by_id(cls,id):
        data = { 'id': id}
        query = '''
        SELECT *
        FROM users
        WHERE id = %(id)s
        ;'''
        user = MySQLConnection(cls.db).query_db(query, data)
        if user:
            user = cls(user[0])
        return user


# UPDATE SQL

#DELETE SQL

# VALIDATE SQL

    @staticmethod
    def validate_user_reg_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 2 :
            flash('Your first name must contain at least 3 characters')
            is_valid = False
        if len(data['last_name']) < 2 :
            flash('Your last name must contain at least 2 characters')
            is_valid = False
        if len(data['password']) < 8 :
            flash('Your password must contain at least 8 characters')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash('Please use a valid email address.')
            is_valid = False
        if User.get_user_by_email(data['email'].lower()):
            flash('That email is already in use.')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Your passwords do not match')
            is_valid = False
        return is_valid

    @staticmethod
    def parse_registration_data(data):
        parsed_data = {}
        parsed_data['first_name'] = data['first_name']
        parsed_data['last_name'] = data['last_name']
        parsed_data['email'] = data['email'].lower()
        parsed_data['password'] = bcrypt.generate_password_hash(data['password'])
        return parsed_data

    @staticmethod
    def login(data):
        this_user = User.get_user_by_email(data['email'].lower())
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                return True
        flash('Your login information is incorrect')
        return False
