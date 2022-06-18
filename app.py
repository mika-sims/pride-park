import bson
from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import Flask, render_template, redirect, request, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from liveserver import LiveServer
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import os
from datetime import datetime
from flask_moment import Moment
from liveserver import LiveServer


app = Flask(__name__)
ls = LiveServer(app)

ls = LiveServer(app)

app.config["MONGO_URI"] = 'mongodb+srv://amare:pridecoding@cluster0.0i04c.mongodb.net/prideDB'
app.secret_key = 'secretlyproud'

app.debug = True
mongo = PyMongo(app)
moment = Moment(app)

user_collection = mongo.db.users


@app.route("/home")
def home():
    """
    Renders home page when site is loaded.
    """
    return render_template('home.html')

# About page
@app.route("/about", methods=['GET'])
def about():
   return render_template("about.html")

# Blog page
@app.route("/blog", methods=['GET'])
def blog():
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    else:
      user = ""
    all_users = list(mongo.db.users.find())
    posts = list(mongo.db.posts.find())
    comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))
    likes = list(mongo.db.likes.find({'deleted': {"$ne": True}}))

    # print(comments)
    return render_template("blog.html",
                           posts=posts,
                           user=user,
                           all_users=all_users,
                           comments=comments,
                           liks=likes,
                           current_page="blog")


# create a register route function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        user_email = request.form.get('email')
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "user_email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": False
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful! please login")
        return redirect(url_for(
            "profile", username=session["user"], user_email=user_email))

    return render_template("register.html")

# login  route function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """
          Login user after checking if user is in the Database
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("You are logged in as: {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# create profile route function
@app.route("/profile/<username>")
def profile(username):
    # grab the session user's username from db , display user's blogs on thier profile
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    posts = list(mongo.db.posts.find(
        {"created_by": session["user"]}).sort("_id", -1))
    last_seen = datetime.utcnow()
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            posts=posts,
            last_seen=last_seen,
            current_time=datetime.utcnow())

    return redirect(url_for("login"))


# Contact page
@app.route("/podcasts", methods=['GET', 'POST'])
def podcast_list():
   return render_template("podcast_list.html")


# Contact page
@app.route("/podcast<podcastId>", methods=['GET', 'POST'])
def podcast_detail():
   return render_template("poscast_detail.html")


@app.route("/logout")
def logout():
    session.pop("user")
    session['user'] = "guest"
    return redirect(url_for("index"))


# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
   return render_template("contact.html")


#search functionality
@app.route("/blog/search", methods=["GET", "POST"])
def search():
    query = request.form.get("search")
    if query:
        comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))
        all_users = list(mongo.db.users.find())
        posts = list(
            mongo.db.posts.find({"$text": {"$search": query}}))
        flash("Search again to reset")
        return render_template("blog.html",
                               posts=posts,
                               all_users=all_users,
                               comments=comments,
                               current_page="blog")
    else:
        all_users = list(mongo.db.users.find())
        posts = list(mongo.db.posts.find())
        comments = list(mongo.db.comments.find({'deleted': {"$ne": True}}))
        return render_template("blog.html",
                               posts=posts,
                               all_users=all_users,
                               comments=comments,
                               current_page="blog")


@app.route("/blog/post/<post_id>", methods=['GET', 'POST'])
def single_post(post_id):
    if "user" in session:
        user = mongo.db.users.find_one({"_id": ObjectId(session["user"])})
    else:
        user = ""
    individual_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    comments = list(
        mongo.db.comments.find({"$and": [{"post": {'$eq': post_id}}]}))
    amount_of_comments = len(list(
        mongo.db.comments.find({"$and": [{"post": {'$eq': post_id}},
                                         {"deleted": {'$ne': True}}
                                         ]})))
    if len(comments) > 1:
        for i in range(len(comments)):
            comments[i]['username'] = mongo.db.users.find_one(
                {"_id": ObjectId(comments[i]['username'])})
            del comments[i]['username']['password']
    else:
        if comments:
            comments[0]['username'] = mongo.db.users.find_one(
                {"_id": ObjectId(comments[0]['username'])})
            del comments[0]['username']['password']
    return render_template("single_post.html", user=user,
                           single_post=individual_post,
                           comments=comments, current_page="single_post",
                           amount_of_comments=amount_of_comments)
