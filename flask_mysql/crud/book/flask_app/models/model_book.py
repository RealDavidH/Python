from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            books = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for book in results:
            #^ assign var name 
                books.append( cls(book) )
                #^ assign var name 
            return books #return that var you named on the list

    #Get one by id
    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM books where id = %(id)s"
        results= connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return results
        return False #^ assign var name and return that var

    #Create
    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into books (title, num_of_pages) values (%(title)s, %(num_of_pages)s)"
        book_id = connectToMySQL(DATABASE).query_db(query, data)
        return book_id #^ assign var name and return that var

    #Update one
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE books SET column_name= %(var_name)s where id = %(id)s "
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')

    #Delete one
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from books where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete book')

