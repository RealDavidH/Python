from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Get all
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
            return users#^ assign var name and return that var

    #Get one by id
    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM users where id = %(id)s"
        results= connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user = cls(results[0])
            return user 
        return False

    #Get one by email
    @classmethod
    def get_one_email(cls, data):
        print(data, "DATA")
        query = "SELECT * FROM users where email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            user = cls(results[0])
            return user
        return False

    #Create
    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into users (first_name, last_name) values (%(first_name)s, %(last_name)s)"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id#^ assign var name and return that var


    @classmethod
    def add_friend(cls, data:dict) -> object:
        query = "insert into friendships (user_id, friend_id) values (%(user1)s, %(user2)s)"
        connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_friends(cls) -> object:
        query = "SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users as users2 ON users2.id = friendships.friend_id;"
        friends = connectToMySQL(DATABASE).query_db(query)
        if friends:
            return friends
        return False


    @classmethod
    def get_one_friend(cls, data:dict) -> object:
        query = "SELECT users.id, users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name, users2.id as friend_id FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users as users2 ON users2.id = friendships.friend_id where users.id = %(id)s"
        friends = connectToMySQL(DATABASE).query_db(query, data)
        if friends:
            return friends
        return False

    #Update one
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE users SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')

    #Delete one
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from users where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete user')



    #Validate
    @staticmethod
    def validate(form_data):
        friend =  User.get_one_friend({"id": form_data['user1'] })
        if not friend:
            return True
        for user in friend:
            if int(form_data['user2']) == user['friend_id']:
                flash("!!User already has friend added!!", "err_friend")
                return False
            if int(form_data['user1']) == user['id']:
                flash("!!User cannot friend themselves!!", "err_friend")
                return False
        return True