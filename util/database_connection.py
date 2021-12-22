from psycopg import connect, OperationalError
import os

def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    # this exception will be raised if you can't connect to your database
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)
