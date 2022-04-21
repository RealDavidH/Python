from config.mysqlconnection import connectToMySQL
DATABASE = 'dojo_and_ninjas'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            dojos = []
            for dojo in results:
                dojos.append( cls(dojo) )
            print(dojos)
            return dojos

    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into dojos (name) values (%(name)s)"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        
        return dojo_id


    @classmethod
    def getinfo(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM dojos where id = %(id)s"
        dojo_info = connectToMySQL(DATABASE).query_db(query, data)
        
        return dojo_info


    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from dojos where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete dojo')


    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE dojos SET name= %(name)s WHERE id= %(id)s"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')


    @classmethod
    def join_tables(cls, data:dict) -> object:
        print(data)
        query = "select * from ninjas join dojos on dojos.id = ninjas.dojos_id;"
        joinedinfo = connectToMySQL(DATABASE).query_db(query,data)
        
        return joinedinfo