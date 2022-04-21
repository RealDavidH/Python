from types import NoneType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt #change this to your database name in __init__ file
from flask import flash, session
import re	
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Skeptic:
    def __init__( self , data ):
        self.id = data['id']
        self.sightings_id = data['sightings_id']
        self.skeptics_id = data['skeptics_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM skeptics;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances 
        if results:
            skeptics = []
            #^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for skeptic in results:
            #^ assign var name 
                skeptics.append( cls(skeptic) )
                #^ assign var name 
            return skeptics #return that var you named on the list


    @classmethod
    def get_one(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM skeptics where id = %(id)s"
        skeptic = connectToMySQL(DATABASE).query_db(query, data)
        return skeptic #^ assign var name and return that var


    @classmethod
    def get_skep_name(cls, data:dict) -> object:
        print(data)
        query = "select users.first_name, users.last_name, skeptics.users_id from users left join skeptics on users.id = skeptics.users_id where sightings_id = %(id)s"
        tot_skeptic = connectToMySQL(DATABASE).query_db(query, data)
        return tot_skeptic #^ assign var name and return that var

    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into skeptics (sightings_id, users_id) values (%(sightings_id)s, %(users_id)s )"
        skeptic_id = connectToMySQL(DATABASE).query_db(query, data)
        return skeptic_id#^ assign var name and return that var


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE skeptics SET column_name = %(var_name)"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from skeptics where users_id = %(user_id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete skeptic')





    # @staticmethod
    # def validate(form_data:dict):



