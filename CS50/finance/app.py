import os
import re
from datetime import datetime as dt

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database and create new table
db = SQL("sqlite:///finance.db")
create = "CREATE TABLE IF NOT EXISTS users" \
            "(id INTEGER, "\
            "username TEXT NOT NULL, "\
            "hash TEXT NOT NULL, "\
            "cash NUMERIC NOT NULL DEFAULT 10000.00, "\
            "PRIMARY KEY (id) )"
db.execute(create)
create = "CREATE TABLE IF NOT EXISTS transactions"\
            "(trans_id INTEGER, "\
            "user_id INTEGER, "\
            "type TEXT, "\
            "shares INTEGER, "\
            "company_shares INTEGER, "\
            "price FLOAT, "\
            "symbol TEXT, "\
            "company TEXT, "\
            "time datetime, "\
            "PRIMARY KEY (trans_id)" \
            "FOREIGN KEY (user_id) REFERENCES users(id) )"
db.execute(create)


# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    owned = "SELECT MAX(trans_id), symbol, company FROM transactions " \
                "WHERE user_id = ? " \
                "GROUP BY symbol " \
                "HAVING company_shares !=0"
    owned = db.execute(owned, user_id)
    n = len(owned)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash[0]["cash"]
    if not owned:
        return render_template("portfolio.html", n=0, smbl='', cmpn='', shrs='',
                                prc='', cost='', cash=round(cash, 4), total=round((cash), 4))
    else:
        symbols = []
        companies = []
        prc = []
        shrs = []
        cost = []
        total_cost = 0
        for i in range(n):
            symbols.append(owned[i]["symbol"])
            companies.append(owned[i]["company"])
            current_info = lookup(owned[i]["symbol"])
            prc.append(current_info["price"])
            company_shares = "SELECT company_shares FROM transactions " \
                                "WHERE user_id = ? AND symbol = ? " \
                                "ORDER BY trans_id desc " \
                                "LIMIT 1"
            company_shares = db.execute(company_shares, user_id, current_info["symbol"])
            shrs.append(company_shares[0]["company_shares"])
            total_cost += company_shares[0]["company_shares"] * current_info["price"]
            cost.append(company_shares[0]["company_shares"] * current_info["price"])

        return render_template("portfolio.html", n=n, smbl=symbols, cmpn=companies, shrs=shrs,
                                prc=prc, cost=cost, cash=round(cash, 4), total=round((cash+total_cost), 4))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("Enter stock to buy")
        if not shares:
            return apology("enter # of shares")

        stock = lookup(symbol.strip())
        if stock is None:
            return apology("No such stock exists")
        try:
            shares = int(shares.strip())
            user_id = session["user_id"]
            if shares > 0:
                cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
                cash = cash[0]["cash"]
                cost = shares * stock["price"]
                if cash >= cost:
                    cash -= cost
                    company_shares = "SELECT company_shares FROM transactions " \
                                        "WHERE user_id = ? AND company = ? " \
                                        "ORDER BY trans_id desc " \
                                        "LIMIT 1"
                    company_shares = db.execute(company_shares, user_id, stock["name"])
                    if not company_shares:
                        company_shares = shares
                    else:
                        company_shares = company_shares[0]["company_shares"] + shares

                    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

                    inserting = "INSERT INTO transactions(user_id, type, shares, company_shares, price, symbol, company, time)" \
                                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                    db.execute(inserting, user_id, "buy", shares, company_shares,
                                stock["price"], stock["symbol"], stock["name"], dt.now())
                    last_trans = "SELECT symbol, company, shares, price " \
                                    "FROM transactions WHERE user_id = ? AND type='buy' " \
                                    "ORDER BY trans_id desc " \
                                    "LIMIT 1"
                    last_trans = db.execute(last_trans, user_id)

                    return render_template("buy.html", smbl=last_trans[0]["symbol"], cmpn=last_trans[0]["company"], prc=last_trans[0]["price"],
                                            shrs=last_trans[0]["shares"], cost=round(cost, 4), cash=round(cash, 4))
                else:
                    return apology("Not enough cash")
            else:
                return apology("Enter a positive integer number")
        except ValueError:
            return apology("Enter a positive integer number")
    else:
        return render_template("buy.html", smbl='--', cmpn='--', prc='--', shrs='--', cost='--', cash='--')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    history = "SELECT type, symbol, company, price, shares, time from transactions " \
                "WHERE user_id = ?"
    history = db.execute(history, user_id)
    if not history:
        return apology("No transactions made yet")
    else:
        tp = []
        smbl = []
        cmpn = []
        prc = []
        shrs = []
        tm = []
        n=len(history)
        for i in range(n):
            tp.append(history[i]["type"])
            smbl.append(history[i]["symbol"])
            cmpn.append(history[i]["company"])
            prc.append(history[i]["price"])
            shrs.append(history[i]["shares"])
            tm.append(history[i]["time"])
        return render_template("history.html", n=n, tp=tp, smbl=smbl, cmpn=cmpn, shrs=shrs, prc=prc, tm=tm)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        symbol = request.form.get("symbol")
        """Get stock quote."""
        if not symbol:
            return apology("No stock to search")
        else:
            stock = lookup(symbol.strip())
            if stock is None:
                return apology("No such stock exists")
            else:
                return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("Name field left blank")
        exists = db.execute("SELECT username FROM users WHERE username = ?", username)
        if exists:
            return apology("User name already exists")

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if not password:
            return apology("Password field left blank")
        if not confirmation:
            return apology("Comfirmation field left blank")
        if password != confirmation:
            return apology("Passwords don't match")
        if not re.match(r"(?=.*[A-Za-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,})", password):
            return apology("password must have number, letter, symbol, >6-long")

        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, generate_password_hash(password, "sha256"))
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    user_id = session["user_id"]
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if symbol == "blank":
            return apology("Select stock to sell")
        if not shares:
            return apology("enter # of shares")

        stock = lookup(symbol.strip())
        if stock is None:
            return apology("No such stock exists")
        try:
            shares = int(shares.strip())
            if shares > 0:
                cost = shares * stock["price"]
                company_shares = "SELECT company_shares FROM transactions " \
                                    "WHERE user_id = ? AND company = ? " \
                                    "ORDER BY trans_id desc " \
                                    "LIMIT 1"
                company_shares = db.execute(company_shares, user_id, stock["name"])
                company_shares = company_shares[0]["company_shares"]
                if company_shares >= shares:
                    company_shares -= shares
                    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
                    cash = cash[0]["cash"] + shares * stock["price"]
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

                    inserting = "INSERT INTO transactions(user_id, type, shares, company_shares, price, symbol, company, time)" \
                                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                    db.execute(inserting, user_id, "sell", shares, company_shares,
                                stock["price"], stock["symbol"], stock["name"], dt.now())
                    last_trans = "SELECT symbol, company, shares, price " \
                                    "FROM transactions WHERE user_id = ? AND type='sell' " \
                                    "ORDER BY trans_id desc " \
                                    "LIMIT 1"
                    last_trans = db.execute(last_trans, user_id)

                    return render_template("sell.html", n=0, stcks='', smbl=last_trans[0]["symbol"], cmpn=last_trans[0]["company"], prc=last_trans[0]["price"],
                                            shrs=last_trans[0]["shares"], cost=round(cost, 4), cash=round(cash, 4))
                else:
                    return apology("Not enough shares")
            else:
                return apology("Enter a positive integer number")
        except ValueError:
            return apology("Enter a positive integer number")
    else:
        owned = "SELECT MAX(trans_id), symbol FROM transactions " \
                    "WHERE user_id = ? " \
                    "GROUP BY symbol " \
                    "HAVING company_shares !=0"
        owned = db.execute(owned, user_id)
        n = len(owned)
        if not owned:
            return apology("You dont own any stocks, go buy some")
        stcks = []
        for i in range(len(owned)):
            stcks.append(owned[i]["symbol"])
        return render_template("sell.html", n=n, stcks=stcks, smbl='--', cmpn='--', prc='--', shrs='--', cost='--', cash='--')


@app.route("/balance", methods=["GET", "POST"])
@login_required
def balance():

    user_id = session["user_id"]
    oldcsh = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    oldcsh = oldcsh[0]["cash"]
    if request.method == "POST":
        cashtype= request.form.get("cashtype")
        if cashtype == "blank":
            return apology("Select field")
        if cashtype == "rmvall":
            db.execute("UPDATE users SET cash = ? WHERE id = ?", 0.0, user_id)
            return render_template("balance.html", oldcsh=oldcsh, newcsh=0.0)
        amount = request.form.get("amount")
        if not amount:
            return apology("Add amount")
        try:
            amount = float(amount.strip())
            if amount < 0:
                return apology("Enter positive number")
            if cashtype == "remove":
                if oldcsh < amount:
                    return apology("Not enough cash to remove")
                else:
                    newcsh = oldcsh - amount
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", newcsh, user_id)
            elif cashtype == "add":
                newcsh = oldcsh + amount
                db.execute("UPDATE users SET cash = ? WHERE id = ?", newcsh, user_id)
            return render_template("balance.html", oldcsh=oldcsh, newcsh=newcsh)
        except ValueError:
            return apology("Enter a positive number")

    else:
        return render_template("balance.html", oldcsh=oldcsh, newcsh='--')

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    user_id = session["user_id"]
    oldpassword = db.execute("SELECT hash FROM users WHERE id = ?", user_id)
    if request.method == "POST":
        action = request.form.get("action")
        if action == "blank":
            return apology("Select action")
        elif action == "changepass":
            newpassword = request.form.get("newpassword")
            if not newpassword:
                return apology("Enter new password")
            confirmation = request.form.get("confirmation")
            if not confirmation:
                return apology("Comfirm new password")
            if confirmation != newpassword:
                return apology("Passwords don't match")
            if not re.match(r"(?=.*[A-Za-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,})", newpassword):
                return apology("password must have number, letter, symbol, >6-long")
            elif check_password_hash(oldpassword[0]["hash"], newpassword):
                return apology("New password can't be the last one")
            else:
                db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(newpassword, "sha256"), user_id)
        elif action == "dltacc":
            db.execute("DELETE FROM transactions WHERE user_id = ?", user_id)
            db.execute("DELETE FROM users WHERE id = ?", user_id)
        session.clear()
        return redirect("/login")

    else:
        return render_template("settings.html")
