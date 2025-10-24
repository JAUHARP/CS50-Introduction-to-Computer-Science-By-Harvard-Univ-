# Expense-Tracker

#### Video Demo: https://youtu.be/MbDx-bfdbf4

#### Description:

This is my final project for [CS50x](https://cs50.harvard.edu/x/).

It is a web app created with Flask. Users can track their daily expenses and manage their personal finances. The application gives real-time insights into spending patterns by category. It helps users see where their money is going. Users can register, log in, and add, view, and delete their expenses whenever they choose. The app calculates total spending and breaks down expenses by category. This allows users to make informed financial choices.

## Features:

- `User Authentication`: Secure registration and login system with password hashing
- `Add Expenses`: Users can add expenses with a description, amount, category, and date
- `View Dashboard`: Shows total spending and a breakdown of expenses by category
- `Expense History`: Complete record of all expenses with sorting and filtering options
- `Delete Expenses`: Users can remove expenses if needed
-`Category Tracking`: Expenses are organized into 8 categories (Food, Transport, Entertainment, Shopping, Bills, Health, Education, Others)
- `Real-time Calculations`: Automatic calculation of total spending and category totals

## How to use:

Installation:

1. Clone or download this project
2. Install the required packages:
    "pip install -r requirements.txt"

3. Create the database:
    "sqlite3 expenses.db"

Then run the SQL commands from  Here or project documentation

4. Run the application:
    "python app.py"

5. Open your browser and go to: `http://127.0.0.1:5000/`

Using the App:

- `Register`: Click "Register" to create a new account with a username and password
- `Login`: Log in with your credentials
- `Dashboard`: View your total spending and recent expenses on the homepage
- `Add Expense`: Click "Add Expense" to log a new expense with a category and date
- `View History`: Click "History" to see all your expenses in a detailed table
-`View Category` Breakdown: The dashboard shows how much you spent in each category
- `Delete Expense`: Remove any expense from the history page if you need to

## How I made this:

This web app was made using the Python framework called [Flask](https://flask.palletsprojects.com/), which I learned about in Week 9 of CS50x. I chose Flask because it's lightweight, easy to learn, and great for building web applications. The frontend uses HTML, CSS, and Jinja2 templating for dynamic content rendering.

### Project Structure:

Root Directory Files:

- `app.py` - Main Flask application containing all routes, database operations, and business logic. This file manages user authentication, expense management, and calculations.
- `helpers.py` - Helper functions, including the `login_required` decorator for protecting routes that need user authentication.
- `expenses.db` - SQLite database that stores user credentials and all expense records securely.
- `requirements.txt` - Lists all external Python packages needed to run this project.

Static Folder (`/static`):

Contains all front-end styling and client-side logic:

- `styles.css` - Stylesheet for the entire application. It includes navbar styling, form layouts, table formatting, button styles, and responsive design for mobile devices.

Templates Folder (`/templates`):

Contains all HTML files for different pages:

- `layout.html` - Base Jinja2 template that all other pages inherit. It includes the navbar and footer.
- `index.html` - Homepage that displays the dashboard with total spending, category breakdown, and recent expenses.
- `login.html` - Login page for existing users to authenticate.
- `register.html` - Registration page for new users to create an account.
- `add.html` - Form page for adding new expenses with all required fields.
-`history.html` - Detailed table view of all expenses with delete functionality.
- `error.html` - Error page displayed when something goes wrong (invalid login, missing fields, etc.).

## Technical Details:

Database Schema:

The application uses two main tables:

1. users table:
- `id` (Primary Key)
- `username` (Unique)
- `hash` (Password hash using pbkdf2)

2. expenses table:
- `id` (Primary Key)
- `user_id` (Foreign Key to users)
- `description` (Expense description)
- `amount` (Expense amount in currency)
- `category` (Expense category)
- `date` (Date of expense)

Key Technologies:

- `Python` - Backend programming language
- `Flask` - Web framework
- `SQLite` - Database management
- `Jinja2` - Template engine for dynamic HTML
- `HTML/CSS` - Frontend markup and styling
- `Werkzeug` - For password hashing and security

## Security Features:

- Passwords are hashed using the `pbkdf2` algorithm before storage
- Session management keeps users logged in
- Login decorator protects sensitive routes
- SQL injection prevention using parameterized queries
- CSRF protection through Flask-Session

## Future Improvements:

- Add expense filtering by date range
- Generate visual charts and graphs for spending analysis
- Export expenses to CSV or PDF
- Set monthly budgets and alerts
- Enable recurring expenses functionality
- Support multiple currencies
- Offer a dark mode theme

## Challenges Faced:

- Implementing secure password hashing and session management
- Efficiently calculating category-wise totals
- Creating a responsive design for mobile and desktop
- Preventing SQL injection attacks in database queries

## Created By:
-Name: Muhammed Jauhar
-GitHub username: JAUHARP
-edX username : MUHAMMED-JAUHAR
-City,Country: Banglore, Karnataka

