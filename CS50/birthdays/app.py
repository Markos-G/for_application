import os
# import re


from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    message=''
    if request.method == "POST":
        TODO: Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            message = "NO NAME"
        birth = request.form.get("birth")
        match = re.match(r"^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])$",birth)
        if match:
            month,day = birth.split('/')
                db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?,?)", name, month, day)
        else
            message= "ERROR MONTH/DAY"

        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", message=message, birthdays=birthdays)

    else:

        TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", message=message, birthdays=birthdays)


