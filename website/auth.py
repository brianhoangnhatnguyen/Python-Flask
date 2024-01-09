from flask import Blueprint, render_template, request, flash
auth = Blueprint("auth", __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
    return render_template("login.html", name="Brian.", email="Enter your email: ")


@auth.route('/logout', methods=["GET", "POST"])
def logout():
    return "<h1>Logout page</h1>"


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        password_repeat = request.form.get("password_repeat")

        if len(first_name) <= 2:
            flash("First name needs to be more than 2 letters.", category="error")

        elif len(last_name) <= 2:
            flash("Last name needs to be more than 2 letters.", category="error")

        elif len(password) <= 12:
            flash("Password needs to have a minimum of 12 characters.", category="error")

        elif password_repeat != password:
            flash("Passwords do not match.", category="error")
        else:
            flash("Your account has been successfully created!", category="success")
    return render_template("signup.html")
