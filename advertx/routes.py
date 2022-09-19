from flask import Flask, render_template, redirect, url_for, request , flash
import secrets
from advertx.__init__ import main, db
from advertx.forms import RegistrationForm, LoginForm, PostForm
from advertx.models import User, Post

@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")

@main.route("/services")
def services():
    return render_template("services.html")


@main.route("/about")
def about_us():
    return render_template("about_us.html")


@main.route("/contact")
def contact_us():
    return render_template("contact_us.html")


@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            phone = form.phone.data
        )
        
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()
        
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for('login'))
    return render_template("signup.html", form=form)


@main.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()

    return render_template("login.html", form=form)