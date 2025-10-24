from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from datetime import datetime


app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to SQLite database named expenses.db
db = SQL("sqlite:///expenses.db")


@app.route("/")
@login_required
def index():
    # Grab the currently logged-in user's ID from the session
    user_id = session["user_id"]

    # Calculate the user's total spending from expenses table
    result = db.execute("SELECT SUM(amount) as total FROM expenses WHERE user_id = ?", user_id)
    total_spending = result[0]["total"] if result[0]["total"] is not None else 0

    # Fetch spending totals grouped by category, sorted by highest first
    categories = db.execute("""
        SELECT category, SUM(amount) as total
        FROM expenses
        WHERE user_id = ?
        GROUP BY category
        ORDER BY total DESC
    """, user_id)

    # Retrieve the 5 most recent expenses for the user, ordered by date
    recent = db.execute("""
        SELECT * FROM expenses
        WHERE user_id = ?
        ORDER BY date DESC, id DESC
        LIMIT 5
    """, user_id)

    # Render the homepage template with the compiled expense data
    return render_template("index.html",
                           total=round(total_spending, 2),
                           categories=categories,
                           recent=recent)


@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear any existing user session data before logging in
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure both username and password fields are filled
        if not username or not password:
            return render_template("error.html", message="Please provide username and password")

        # Check if user exists and verify password hash
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template("error.html", message="Invalid username or password")

        # Log user in by storing user_id in session
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    # Show login page for GET requests
    return render_template("login.html")


@app.route("/logout")
def logout():
    # Simply clear session data to log the user out
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate that all fields are provided
        if not username or not password or not confirmation:
            return render_template("error.html", message="All fields are required")

        # Check if passwords match
        if password != confirmation:
            return render_template("error.html", message="Passwords do not match")

        # Verify username isn't already taken
        existing = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing:
            return render_template("error.html", message="Username already exists")

        # Hash the password before storing in DB for security
        hash_password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_password)

        return redirect("/login")

    # Show registration page on GET requests
    return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        user_id = session["user_id"]
        description = request.form.get("description")
        amount = request.form.get("amount")
        category = request.form.get("category")
        date = request.form.get("date")

        # Ensure mandatory fields are filled out
        if not description or not amount or not category or not date:
            return render_template("error.html", message="All fields are required")

        # Validate amount is a positive number
        try:
            amount = float(amount)
        except:
            return render_template("error.html", message="Invalid amount")

        if amount <= 0:
            return render_template("error.html", message="Amount must be positive")

        # Insert the new expense record linked to user
        db.execute("""
            INSERT INTO expenses (user_id, description, amount, category, date)
            VALUES (?, ?, ?, ?, ?)
        """, user_id, description, amount, category, date)

        return redirect("/")

    # Serve the form for adding new expenses
    return render_template("add.html")


@app.route("/history")
@login_required
def history():
    # Fetch all expenses for logged-in user sorted by most recent
    user_id = session["user_id"]
    expenses = db.execute("""
        SELECT * FROM expenses
        WHERE user_id = ?
        ORDER BY date DESC, id DESC
    """, user_id)

    return render_template("history.html", expenses=expenses)


@app.route("/delete/<int:expense_id>", methods=["POST"])
@login_required
def delete(expense_id):
    # Allow user to delete their own expense by ID
    user_id = session["user_id"]
    db.execute("DELETE FROM expenses WHERE id = ? AND user_id = ?", expense_id, user_id)
    return redirect("/history")


if __name__ == "__main__":
    # Run the application in debug mode for development
    app.run(debug=True)
