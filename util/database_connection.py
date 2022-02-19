from psycopg2 import connect, OperationalError
import os


def create_connection():
    try:
        conn = connect(
            host=os.getenv("HOST"),
            dbname=os.getenv("DBNAME"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT"),
        )
        return conn
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)
