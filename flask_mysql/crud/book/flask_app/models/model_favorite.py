from types import NoneType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Favorite:
    def __init__( self , data ):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
    #Get all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM favorites;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            favorites = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for favorite in results:
            #^ assign var name 
                favorites.append( cls(favorite) )
                #^ assign var name 
            return favorites #return that var you named on the list

    #Get one by id
    @classmethod
    def get_one_author_id(cls, data:dict) -> object:
        print(data)
        query = "select * from authors left join favorites on authors.id = favorites.author_id left join books on books.id = favorites.book_id where author_id = %(id)s"
        results= connectToMySQL(DATABASE).query_db(query, data)
        
        if results:
            return results
        return False #^ assign var name and return that var


    @classmethod
    def get_one_book_id(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results= connectToMySQL(DATABASE).query_db(query, data)
        
        if results:
            return results
        return False #^ assign var name and return that var


    #Create
    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into favorites (author_id, book_id) values (%(author_id)s, %(book_id)s)"
        book_id = connectToMySQL(DATABASE).query_db(query, data)
        return book_id #^ assign var name and return that var

    #Update one
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE favorites SET column_name= %(var_name)s where id = %(id)s "
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')

    #Delete one
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from favorites where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete book')

    @staticmethod
    def check_book(unchek_book):
        favorites = Favorite.get_one_author_id({"id":unchek_book['author_id']})
        if not favorites:
            return True
        for favorite in favorites:
            if int(unchek_book['book_id']) == favorite['book_id']:
                return False
        return True




    @staticmethod
    def validate(form_data):
        if not Favorite.check_book(form_data):
            flash("!!Author already has book favorited!!", "err_favorite")
            return False
        return True