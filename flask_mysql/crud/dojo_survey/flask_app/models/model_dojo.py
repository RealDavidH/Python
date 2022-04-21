from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE #change this to your database name in __init__ file
from flask import flash
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.var_name = data['var_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            dojos= []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for dojo in results:
            #^ assign var name 
                dojos.append( cls(dojo) )
                #^ assign var name 
            return dojos


    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        if 'comment' in data:
            query = "insert into dojos (name, location, language, comment) values (%(name)s, %(location)s, %(language)s, %(comment)s)"
        else:
            query = "insert into dojos (name, location, language, comment) values (%(name)s, %(location)s, %(language)s, (None))"
        created_dojo= connectToMySQL(DATABASE).query_db(query, data)
        return created_dojo


    @classmethod
    def getinfo(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM dojos where id = %(id)s"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from dojos where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete')


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE dojos SET name = %(name)s"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @staticmethod
    def validate(form_data:dict):
        print(form_data)
        is_valid = True
        
        if len(form_data['name']) <= 0:
            flash("Name is required", "err_dojo_name")
            is_valid = False
            return is_valid
        return is_valid

