import mysql.connector
from mysql.connector import Error
import csv

# config={}
# with open('config.txt','r') as f:
# 	config['host_name'] = f.readline().strip()
# 	config['user_name'] = f.readline().strip()
# 	config['user_password'] = f.readline().strip()
# config['database'] = ''

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

# connection = create_connection(**config)

def create_database(connection, db):
    query = 'CREATE SCHEMA IF NOT EXISTS {}'.format(db)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Database '{db}' created successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")

# db='sudoku'
# create_database(connection,db)
# config['database']=db
# connection = create_connection(**config)

def use_database(connection, db):
    query = 'USE {}'.format(db)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Using {db}")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")

# use_database(connection,db)

def execute_query(connection, query, action=''):

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query '{action}' executed successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")

# create_table = """
	# CREATE TABLE generator (
	# 	id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
	# 	puzzle CHAR(81),
	# 	solution CHAR(81),
	# 	PRIMARY KEY  (id)
	# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""

# execute_query(connection, create_table, action='create')


def execute_many_query(connection, query, args, action=''):

    cursor = connection.cursor()
    try:
        cursor.executemany(query, args)
        connection.commit()
        print(f"Query '{action}' executed successfully")
        cursor.close()
    except Error as e:
        print(f"The error '{e}' occurred")


# fill_table ="""
#   INSERT INTO generator (puzzle, solution)
#   VALUES (%s, %s)
# """

# with open('sudoku.csv', newline='') as csvfile:
#     print ('csv file opened') 
#     ins_vals=[]
#     reader = csv.DictReader(csvfile)
#     count = 0
#     step = 20000
#     stop = 1_000_000//step + 1
#     lin_space = [k*step for k in range(1,stop)]
#     while reader:
#         count +=1
#         try:
#             row = next(reader)
#         except:
#             break
#         ins_vals.append( (row['quizzes'], row['solutions']) )
#         if count in lin_space:
#             execute_many_query(connection, fill_table, ins_vals, action='insert into' )
#             ins_vals = []
#     print ('csv file closed')


def fetch_query(connection, one=False, many=0, all=False):
    cursor = connection.cursor()
    try:
        if one:
            # make raadnom selecton from id and system time
            cursor.execute("""SELECT puzzle from generator WHERE id = %s""", (one,))
            row = cursor.fetchone()[0]
            print(f"Query 'fetch one' executed successfully")
        elif many:
            cursor.execute("""SELECT puzzle from generator WHERE ...""")
            row = cursor.fetchmany(size=many)
            print(f"Query 'fetch many:(size{many})' executed successfully")
        elif all:
            cursor.execute("""SELECT puzzle from generator""")
            row = cursor.fetchall()
            print (f"Query 'fetch all' executed successfully")

        cursor.close()
        return row
    except Error as e:
        print(f"The error '{e}' occurred")


# connection.close()