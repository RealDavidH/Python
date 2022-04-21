from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.var_name = data['var_name']
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
             = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for  in results:
            #^ assign var name 
                .append( cls(assign var name) )
                #^ assign var name 
            return #^ assign var name and return that var

    #Get one by id
    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM table_name where id = %(id)s"
        results= connectToMySQL(DATABASE).query_db(query, data)
        if results:
            !!!VAR_NAME!!! = cls(results[0])
            return !!!VAR_NAME!!! 
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
        query = "insert into table_name (column_name) values (%(var_name)s)"
         = connectToMySQL(DATABASE).query_db(query, data)
        return #^ assign var name and return that var

    #Update one
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE table_name SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')

    #Delete one
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from table_name where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete user')

    #Validate
    @staticmethod
    def validate(form_data:dict):
        if len(form_data['first_name']) <= 0:
            flash("First name is required", "err_user_first_name")
            return False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
            return False
        return True
