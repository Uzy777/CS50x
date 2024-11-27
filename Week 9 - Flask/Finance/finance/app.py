import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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

    # Query for user's stocks
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
        user_id,
    )

    # Query for user's cash balance
    rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = rows[0]["cash"]

    # Prepare data for the template
    portfolio = []
    grand_total = cash

    for stock in stocks:
        stock_info = lookup(stock["symbol"])
        total = stock["shares"] * stock_info["price"]
        grand_total += total
        portfolio.append(
            {
                "symbol": stock["symbol"],
                "name": stock_info["name"],
                "shares": stock["shares"],
                "price": stock_info["price"],
                "total": total,
            }
        )

    return render_template(
        "index.html", stocks=portfolio, cash=cash, grand_total=grand_total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        shares = request.form.get("shares")

        if not stock:
            return apology("Invalid stock symbol", 400)

        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Input a positive number", 400)

        except ValueError:
            return apology("Input a valid number", 400)

        # Calculations for the purchase
        price = stock["price"]
        total_cost = shares * price

        # Query user's cash balance
        user_id = session["user_id"]
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = rows[0]["cash"]

        if cash < total_cost:
            return apology("You don't have enough cash", 400)

        # Check if the user already has shares of the stock
        existing_shares = db.execute(
            "SELECT shares FROM transactions WHERE user_id = ? AND symbol = ?",
            user_id,
            symbol,
        )

        if existing_shares:
            # Update the existing transaction
            db.execute(
                "UPDATE transactions SET shares = shares + ?, price = ? WHERE user_id = ? AND symbol = ?",
                shares,
                price,
                user_id,
                symbol,
            )
        else:
            # Insert a new transaction
            db.execute(
                "INSERT INTO transactions (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)",
                user_id,
                symbol,
                shares,
                price,
            )

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Query the updated cash balance
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = rows[0]["cash"]

        # Query for user's stocks
        stocks = db.execute(
            "SELECT symbol, SUM(shares) as shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )

        # Prepare data for the template
        portfolio = []
        grand_total = cash

        for stock in stocks:
            stock_info = lookup(stock["symbol"])
            total = stock["shares"] * stock_info["price"]
            grand_total += total
            portfolio.append(
                {
                    "symbol": stock["symbol"],
                    "name": stock_info["name"],
                    "shares": stock["shares"],
                    "price": stock_info["price"],
                    "total": total,
                }
            )

        return render_template(
            "index.html", stocks=portfolio, cash=cash, grand_total=grand_total
        )

    # Query the user's cash balance for GET request
    user_id = session["user_id"]
    rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = rows[0]["cash"]

    return render_template("buy.html", cash=cash)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # Query for all transactions of the user
    transactions = db.execute(
        "SELECT symbol, shares, price, transacted FROM transactions WHERE user_id = ? ORDER BY transacted DESC",
        user_id,
    )

    return render_template("history.html", transactions=transactions)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if stock:
            return render_template("quoted.html", stock=stock)
        else:
            return apology("Invalid stock symbol", 400)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if username or password or confirmation is blank
        if not username or not password or not confirmation:
            return apology("must provide username and password", 400)

        # Check if the password and confirmation match
        if not password == confirmation:
            return apology("password does not match", 400)

        # Hash the password
        hashed_password = generate_password_hash(
            password, method="scrypt", salt_length=16
        )

        # Try to insert the new user into the database
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                hashed_password,
            )
        except ValueError:
            return apology("username already exists", 400)

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Must select a stock", 400)

        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Must input a positive number", 400)
        except ValueError:
            return apology("Must input a valid number", 400)

        # Query for user's shares of the stock
        rows = db.execute(
            "SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?",
            user_id,
            symbol,
        )
        if len(rows) != 1 or rows[0]["total_shares"] < shares:
            return apology("Not enough shares", 400)

        # Calculate the total sale value
        stock = lookup(symbol)
        total_value = shares * stock["price"]

        # Update the transactions for the sale
        db.execute(
            "UPDATE transactions SET shares = shares - ?, price = ? WHERE user_id = ? AND symbol = ?",
            shares,
            stock["price"],
            user_id,
            symbol,
        )

        # Update the user's cash balance
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id
        )

        return redirect("/")

    else:
        # Query for user's owned stocks
        stocks = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0",
            user_id,
        )
        return render_template("sell.html", stocks=stocks)
