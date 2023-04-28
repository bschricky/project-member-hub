from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    db = "posts"
    def __init__(self,data):
        self.id = data['id']
        self.employer= data['employer']
        self.program_type= data['program_type']
        self.start_date= data['start_date']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (employer, program_type, start_date, comment, user_id) VALUES (%(employer)s, %(program_type)s, %(start_date)s, %(comment)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        results =  connectToMySQL(cls.db).query_db(query)
        
        posts = []
        for post in results:

            posts.append(cls(post))

        return posts
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM posts WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET employer=%(employer)s, program_type=%(program_type)s, start_date=%(start_date)s, comment=%(comment)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post['employer']) < 3:
            is_valid = False
            flash("Employer must be at least 3 characters","post")
        if post['start_date'] == "": #this is the ENUM/select so may try removing
            is_valid = False
            flash("Please select a program type","post")
        if post['start_date'] == "":
            is_valid = False
            flash("Please enter a start date","post")
        if len(post['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters","post")
        return is_valid