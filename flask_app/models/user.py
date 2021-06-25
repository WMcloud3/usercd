from flask_app.config.mysqlconnection import connectToMySQL

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
        results = connectToMySQL('usersCR').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('usersCR').query_db(query, data)
        print(results)
        return cls (results[0])

    @classmethod
    def save(cls, data):
        # ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() ) Has to mach the left side of data
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        results = connectToMySQL('usersCR').query_db(query, data)
        return results

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=NOW() WHERE id= %(id)s;"
        results = connectToMySQL('usersCR').query_db(query, data)
        return results


    @classmethod
    def del_user(cls, data):
        query = "DELETE FROM users WHERE id= %(id)s;"
        return