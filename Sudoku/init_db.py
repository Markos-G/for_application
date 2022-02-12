from db import create_connection, create_database,use_database, execute_query, execute_many_query
import csv


config={}
with open('config.txt','r') as f:
  config['host_name'] = f.readline().strip()
  config['user_name'] = f.readline().strip()
  config['user_password'] = f.readline().strip()
config['database'] = ''


connection = create_connection(**config)

db='sudoku'
create_database(connection,db)
config['database']=db
use_database(connection,db)

create_table = """
    CREATE TABLE generator (
      id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
      puzzle CHAR(81),
      solution CHAR(81),
      PRIMARY KEY  (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
execute_query(connection, create_table, action='create')


fill_table ="""
  INSERT INTO generator (puzzle, solution)
  VALUES (%s, %s)
"""
with open('sudoku.csv', newline='') as csvfile:
    print ('csv file opened') 
    ins_vals=[]
    reader = csv.DictReader(csvfile)
    count = 0
    step = 20000
    stop = 1_000_000//step + 1
    lin_space = [k*step for k in range(1,stop)]
    while reader:
        count +=1
        try:
            row = next(reader)
        except:
            break
        ins_vals.append( (row['quizzes'], row['solutions']) )
        if count in lin_space:
            execute_many_query(connection, fill_table, ins_vals, action='insert into' )
            ins_vals = []
    print ('csv file closed')


connection.close()