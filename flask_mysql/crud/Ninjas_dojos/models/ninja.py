from config.mysqlconnection import connectToMySQL
DATABASE = 'dojo_and_ninjas'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            ninjas = []
            for ninja in results:
                ninjas.append( cls(ninja) )
            print(ninjas)
            return ninjas


    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into ninjas (first_name, last_name, age, dojos_id) values (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)"
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id


    @classmethod
    def getinfo(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM ninjas where id = %(id)s"
        ninja_info = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_info


    @classmethod
    def get_dojoinfo(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM ninjas where dojos_id = %(id)s"
        dojo_info = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_info



    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from ninjas where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete ninja')


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE ninjas SET first_name= %(first_name)s, last_name= %(last_name)s, age= %(age)s WHERE id= %(id)s"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')