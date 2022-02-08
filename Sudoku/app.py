import os

import mysql.connector
from mysql.connector import Error

from flask import Flask, flash, redirect, render_template, request

from random import randint

from db import create_connection ,fetch_query

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # app.config["TEMPLATES_AUTO_RELOAD"] = True
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def home():

        return render_template("home.html",n=0)

    @app.route('/newgame')
    def newgame():

        config={}
        with open('config.txt','r') as f:
            config['host_name'] = f.readline().strip()
            config['user_name'] = f.readline().strip()
            config['user_password'] = f.readline().strip()
            config['database'] = f.readline().strip()

        connection = create_connection(**config)

        puzzle = fetch_query(connection, one=randint(0, 1_000_000))
        print((puzzle))
        grid = [ [0 for i in range(9)] for j in range(9)]

        k = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if puzzle[k] == '0':
                    grid[i][j] = ''
                else:
                    grid[i][j] = puzzle[k]
                k += 1
        
        for row in grid:
            print(row,end='\n')
        connection.close()
        return render_template("newgame.html",n=grid)

    @app.route('/answer', methods=["POST"])
    def answer():

        return render_template("answer.html")




    return app