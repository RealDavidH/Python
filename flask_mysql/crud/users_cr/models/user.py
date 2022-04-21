from config.mysqlconnection import connectToMySQL
DATABASE = 'users'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            users = []
            for user in results:
                users.append( cls(user) )
            print(users)
            return users

    @classmethod
    def create(cls, data:dict) -> object:
        print(data)
        query = "insert into users (first_name, last_name, email) values (%(first_name)s, %(last_name)s, %(email)s)"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id
    
    @classmethod
    def getinfo(cls, data:dict) -> object:
        print(data)
        query = "SELECT * FROM users where id = %(id)s"
        user_info = connectToMySQL(DATABASE).query_db(query, data)
        return user_info
    
    @classmethod 
    def delete_one (cls, data:dict) -> object:
        print(data)
        query = "delete from users where id = %(id)s"
        connectToMySQL(DATABASE).query_db(query, data)
        print('Delete user')
    
    @classmethod
    def update_one(cls, data:dict) -> object:
        print(data)
        query = "UPDATE users SET first_name= %(first_name)s, last_name= %(last_name)s, email= %(email)s WHERE id= %(id)s"
        connectToMySQL(DATABASE).query_db(query,data)
        print('Update')