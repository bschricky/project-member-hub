import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'Love4l!fe', #this is my individual password for MySQL!
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)

        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:

                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:

                    result = cursor.fetchall()
                    return result
                else:

                    self.connection.commit()
            except Exception as e:

                print("Something went wrong", e)
                return False
            finally:

                self.connection.close() 

def connectToMySQL(db):
    return MySQLConnection(db)