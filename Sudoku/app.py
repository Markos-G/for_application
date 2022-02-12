import os

import mysql.connector
from mysql.connector import Error

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from random import randint

from db import create_connection, fetch_query
from sudoku import fill_matrix, solve


# create and configure session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def home():
    return render_template("home.html",n=0)


@app.route('/newgame')
def newgame():

    # config.txt is a seperate file in directory where the credentials for the database are stored
    # env variables can be used instead
    config={}
    with open('config.txt','r') as f:
        config['host_name'] = f.readline().strip()
        config['user_name'] = f.readline().strip()
        config['user_password'] = f.readline().strip()
        config['database'] = f.readline().strip()
    connection = create_connection(**config)
    
    puzzle = fetch_query(connection, one=randint(0, 1_000_000))
    grid = [ [0 for i in range(9)] for j in range(9)]
    k = 0
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if puzzle[k] == '0':
                grid[i][j] = '_'
            else:
                grid[i][j] = puzzle[k]
            k += 1
    session['grid'] = grid

    ids = [x for x in range(81)]

    connection.close()
    return render_template("newgame.html",n=grid, ids=ids)
    

@app.route('/submit', methods=['post'])
def submit():

    grid = session['grid']
    grid = [[int(col) if col !='_' else 0 for col in row] for row in grid]

    X,Y = fill_matrix(grid)
    solution = solve(X, Y, sol=[])
    for sol in solution:
        grid[sol[0]][sol[1]] = sol[2]

    inpts={}
    for cell in range(81):
        number = request.form.get(str(cell))
        if number is not None:
            inpts[cell] = number
     
    user_grid = session['grid']
    for key,value in inpts.items():
        row,col = divmod(key,9)
        user_grid[row][col] = value

    err=[]
    for key,value in inpts.items():
        row,col = divmod(key,9)
        if value != str(grid[row][col]):
            err.append(key)

    ids = [x for x in range(81)]
    
    return render_template("submit.html", n=user_grid, ids=ids ,err=err)
