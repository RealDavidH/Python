from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash, session
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.intructions = data['instructions']
        self.under_30 = data['under_30']
        self.made = data['made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            recipes = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for recipe in results:
            #^ assign var name 
                recipes.append( cls(recipe) )
                #^ assign var name 
            return recipes #return that var you named on the list
        return False


    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM recipes where id = %(id)s"
        recipe = connectToMySQL(DATABASE).query_db(query, data)
        return recipe #^ assign var name and return that var


    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into recipes (name, description, instructions, made, under_30, user_id) values (%(name)s, %(description)s, %(instructions)s, %(made)s, %(under_30)s, %(user_id)s)"
        recipe_id = connectToMySQL(DATABASE).query_db(query, data)
        return recipe_id#^ assign var name and return that var


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, made = %(made)s"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from recipes where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete recipe')


    @staticmethod
    def validate(form_data:dict):
        print(form_data)
        fields = "One, or more of the required fields are blank."
        if len(form_data['name']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['description']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['instructions']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['made']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['under_30']) <= 0:
            flash(fields, "err_blank")
            return False
        return True



