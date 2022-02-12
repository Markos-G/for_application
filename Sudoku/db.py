import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, database):

    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
            )
        print("Connection to MySQL DB {}".format(database))
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_database(connection, db):
    query = 'CREATE SCHEMA IF NOT EXISTS {}'.format(db)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Database '{db}' created successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")


def use_database(connection, db):
    query = 'USE {}'.format(db)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Using {db}")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")



def execute_query(connection, query, action=''):

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query '{action}' executed successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_many_query(connection, query, args, action=''):

    cursor = connection.cursor()
    try:
        cursor.executemany(query, args)
        connection.commit()
        print(f"Query '{action}' executed successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")



def fetch_query(connection, one=False):
    cursor = connection.cursor()
    try:
        if one:
            # make raadnom selecton from id and system time
            cursor.execute("""SELECT puzzle from generator WHERE id = %s""", (one,))
            row = cursor.fetchone()[0]
            print(f"Query 'fetch one' executed successfully")
        cursor.close()
        return row
    except Error as e:
        print(f"The error '{e}' occurred")
