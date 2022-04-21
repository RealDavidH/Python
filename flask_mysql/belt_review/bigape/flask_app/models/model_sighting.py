from flask_app.config.mysqlconnection import connectToMySQL
# change this to your database name in __init__ file
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re
#!!!!!!!!!!!!!!!!!!!!!!!!CHANGE MODEL FILE NAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.sighting_date = data['sighting_date']
        self.num_apes = data['num_apes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "select * from users left join skeptics on users.id = skeptics.users_id left join sightings on sightings.id = skeptics.sightings_id;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances
        if results:
            sightings = []
            # ^ assign var name and return that var
        # Iterate over the db results and create instances of friends with cls.
            for sighting in results:
                # ^ assign var name
                sightings.append(cls(sighting))
                # ^ assign var name
            return sightings  # return that var you named on the list
        return False

    @classmethod
    def get_one(cls, data: dict) -> object:
        print(data)
        query = "SELECT * FROM sightings where id = %(id)s"
        sighting = connectToMySQL(DATABASE).query_db(query, data)
        return sighting  # ^ assign var name and return that var

    @classmethod
    def join_sightings(cls):
        query = "select *, users.first_name, count(skeptics.id) as skeptic_tot from sightings left join users on users.id = sightings.user_id left join skeptics on skeptics.sightings_id = sightings.id;"
        sighting_joined = connectToMySQL(DATABASE).query_db(query)
        return sighting_joined
    
    @classmethod
    def join_sightings_one(cls, data:dict) -> object:
        query = "select *, count(skeptics.id) as skeptic_tot from sightings left join skeptics on skeptics.sightings_id = sightings.id where sightings.id = %(id)s;"
        sighting_joined = connectToMySQL(DATABASE).query_db(query, data)
        return sighting_joined

    @classmethod
    def create(cls, data: dict) -> object:
        print(data)
        query = "insert into sightings (location, description, sighting_date, num_apes, user_id) values (%(location)s, %(description)s, %(sighting_date)s, %(num_apes)s, %(user_id)s)"
        sighting_id = connectToMySQL(DATABASE).query_db(query, data)
        return sighting_id  # ^ assign var name and return that var

    @classmethod
    def update_one(cls, data: dict) -> object:
        print(data)
        query = "UPDATE sightings SET location = %(location)s, description = %(description)s, sighting_date = %(sighting_date)s, num_apes = %(num_apes)s where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Update')

    @classmethod
    def delete_one(cls, data: dict) -> object:
        print(data)
        query = "delete from sightings where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete sighting')

    @staticmethod
    def validate(form_data: dict):
        print(form_data)
        fields = "One, or more of the required fields are blank."
        if len(form_data['location']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['description']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['sighting_date']) <= 0:
            flash(fields, "err_blank")
            return False
        if len(form_data['num_apes']) <= 0:
            flash(fields, "err_blank")
            return False
        return True
