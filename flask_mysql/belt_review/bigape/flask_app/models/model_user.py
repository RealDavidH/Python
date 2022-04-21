from types import NoneType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash, session
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            users = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for user in results:
            #^ assign var name 
                users.append( cls(user) )
                #^ assign var name 
            return users #return that var you named on the list


    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM users where id = %(id)s"
        user = connectToMySQL(DATABASE).query_db(query, data)
        return user #^ assign var name and return that var


    @classmethod
    def get_one_email(cls, data):
        print(data, "DATA")
        query = "SELECT * FROM users where email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user = cls(results[0])
            return user
        return False


    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into users (first_name, last_name, email, password) values (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id#^ assign var name and return that var


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE users SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from users where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete user')


    @staticmethod
    def check_email(unchek_email):
        emails = User.get_all()
        print(emails)
        if isinstance(emails, NoneType):
            return True
        for email in emails:
            if unchek_email == email.email:
                return False
        return True


    @staticmethod
    def check_friends(form_data):
        friend =  User.get_one_friend({"id": form_data['user1'] })
        if form_data['user1'] == form_data['user2']:
                flash("!!User cannot friend themselves!!", "err_friend")
                return False
        if not friend:
            return True
        for user in friend:
            if int(form_data['user2']) == user['friend_id']:
                flash("!!User already has friend added!!", "err_friend")
                return False
        return True


    @staticmethod
    def validate(form_data:dict):
        print(form_data)
        fields = "One, or more of the required fields are blank."


        if len(form_data['first_name']) <= 0:
            flash(fields, "err_blank")
            return False


        if len(form_data['last_name']) <= 0:
            flash(fields, "err_blank")
            return False


        if len(form_data['email']) <= 0:
            flash(fields, "err_blank")
            return False


        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_email")
            return False


        if not User.check_email(form_data['email']):
            flash("Email already in use!", "err_email")
            return False

        if len(form_data['password']) < 8:
            flash('Password must be longer than 8 characters', 'err_paswrd')
            return False


        if  not True in [char.isalpha() for char in form_data['password']]:
            flash('Password must contain at least 1 letter and 1 number.', 'err_paswrd')
            print("no letter")
            return False



        if not True in [char.isdigit() for char in form_data['password']]:
            print("no number")
            flash('Password must contain at least 1 letter and 1 number.', 'err_paswrd')
            return False


        if form_data['password'] != form_data['chkr_password']:
            flash('Passwords must match!', 'err_paswrd')
            return False
        
        return True


    @staticmethod
    def validate_login(form_data):
        print(form_data)
        fields = "One, or more of the required fields are blank."


        if len(form_data['email']) <= 0:
            flash(fields, "err_blank_log")
            return False


        if  len(form_data['password']) <= 0:
            flash(fields, "err_blank_log")
            return False


        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email and/or password!", "err_invaild_log")
            return False


        if len(form_data['password']) < 8:
            flash('Invalid email and/or password!', 'err_invaild_log')
            return False
        else:
            poten_user = User.get_one_email({"email": form_data['email']})
            print(poten_user)
            if not bcrypt.check_password_hash(poten_user.password, form_data['password']):
                flash('Invalid email and/or password!', 'err_invaild_log')
                return False
            else:
                session['uuid'] = poten_user.id
        return True


