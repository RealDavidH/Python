from types import NoneType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE #change this to your database name in __init__ file
import re
from flask import flash
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            emails = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for email in results:
            #^ assign var name 
                emails.append( cls(email) )
                #^ assign var name 
            return emails#return that var you named on the list


    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into emails (email) values (%(email)s)"
        email_id = connectToMySQL(DATABASE).query_db(query, data)
        return email_id#^ assign var name and return that var


    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM emails where id = %(id)s"
        one_email = connectToMySQL(DATABASE).query_db(query, data)
        return one_email#^ assign var name and return that var


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE table_name SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from emails where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete user')



    @staticmethod
    def check_email(unchek_email):
        emails = Email.get_all()
        print(emails)
        if isinstance(emails, NoneType):
            return True
        for email in emails:
            if unchek_email == email.email:
                return False
        return True


    @staticmethod
    def validate(form_data:dict):
        if len(form_data['email']) <= 0:
            flash("Please enter a email", "err_email")
            return False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", "err_email")
            return False
        if not Email.check_email(form_data['email']):
            flash("Email already in use!", "err_email")
            return False
        return True

