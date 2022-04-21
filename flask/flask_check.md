# Pre-req

`One time thing

```
pip install pipenv
```

# Flask app Builder Checklist

1. Create folder for that project
2. cd to that folder
3. create our virtual env inside folder
    ```py
    pipenv install flask==2.0.3 pymysql(or whatever version you want)
    ```
4. Look for `pipfile` and `pipfile.lock`
   -if you don't see them fix it before cont
5. Enter into VE shell
    ```
    pipenv shell
    ```
6. folder structure
    - pipfile
    - pipfile.file
    - server.py
    - models
        - model_tablename.py
    - templates
        - index.html
    - controllers
        - controllers_tablename.py
    - config
        - mysqlconnection.py
    - static
        - css
            - style.css
        - js
            - script.js

7. create "__init__.py"
```py
from flask import Flask
from friend import Friend
app = Flask(__name__)

```

7. create server.py

    ```py
    from flask import redirect
    from __int__ import app
    from controllers import name_controller

    if __name__ == "__main__":
    app.run(debug=True)
    ```

8. connection to database
- create mysqlconnection.py in 'config'
ADD BELOW TO mysqlconnection.py
```py
    # a cursor is the object we use to interact with the database
    import pymysql.cursors


# this class will give us an instance of a connection to our database

    class MySQLConnection:
    def **init**(self, db): # change the user and password as needed
connection = pymysql.connect(host = 'localhost',
user = 'root',
password = 'root',
db = db,
charset = 'utf8mb4',
cursorclass = pymysql.cursors.DictCursor,
autocommit = True) # establish the connection to the database
self.connection = connection # the method to query the database
def query_db(self, query, data=None):
with self.connection.cursor() as cursor:
try:
query = cursor.mogrify(query, data)
print("Running Query:", query)

                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection

def connectToMySQL(db):
return MySQLConnection(db)
```

8. models.py file (name it as --> tablename_model.py)

```py
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
DATABASE = 'changeme_db'

class User:
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
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        if results:
            friends = []
        # Iterate over the db results and create instances of friends with cls.
            for friend in results:
                friends.append( cls(friend) )
            return friends
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




#save || create
#get_all
#get_one
#update_one
#delete_one
```

9. What the server.py would look like

```py

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```
