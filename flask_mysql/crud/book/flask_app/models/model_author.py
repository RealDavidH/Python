from flask_app.config.mysqlconnection import connectToMySQL
# change this to your database name in __init__ file
from flask_app import DATABASE, bcrypt
from flask import flash
import re
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances
        if results:
            authors = []
            # ^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for author in results:
            # ^ assign var name 
                authors.append( cls(author) )
                # ^ assign var name 
            return authors #return that var you named on the list
        return False

    # Get one by id
    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM authors where id = %(id)s"
        author = connectToMySQL(DATABASE).query_db(query, data)
        return author

    # Create
    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into authors (name) values (%(name)s)"
        author_id = connectToMySQL(DATABASE).query_db(query, data)
        return author_id #^ assign var name and return that var

    # Update one
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE authors SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')

    # Delete one
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from authors where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete author')
