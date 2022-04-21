from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
DATABASE = 'friends_db'

class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        if results:
            friends = []
        # Iterate over the db results and create instances of friends with cls.
            for friend in results:
                friends.append( cls(friend) )
            return friends
        

#save || create
#get_all
#get_one
#update_one
#delete_one