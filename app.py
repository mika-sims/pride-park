import bson
from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import os


app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb+srv://amare:pridecoding@cluster0.0i04c.mongodb.net/prideDB'
app.secret_key = 'secretlyproud'

app.debug = True
mongo = PyMongo(app)

user_collection = mongo.db.users


# Landing page
@app.route("/", methods=['GET', 'POST'])
def index():
   return render_template("index.html")


# About page
@app.route("/about", methods=['GET'])
def about():
   return render_template("about.html")


# Signup page
@app.route("/signup", methods=['GET', 'POST'])
def signup():
   """
   User registration
   """
   if request.method == 'POST':
      user_exists = user_collection.find_one({'username': request.form.get('username').lower()})
      email_exists = user_collection.find_one({'email': request.form.get('email')})
      if user_exists:
         flash('Username already taken')
         return redirect(url_for('signup'))
      elif email_exists:
         flash('Email already in use!')
         return redirect(url_for('signup'))
      else:
         new_user = {
               'username': request.form.get('username'),
               'email': request.form.get('email'),
               'password': request.form.get('password'),
         }
         user_collection.insert_one(new_user)
         # Add user to session cookies
         session['user'] = request.form.get('username')
         flash(
               f'Account created {request.form.get("username")}. Welcome to Pride Park!')
         return redirect(url_for('index'))
   return render_template("signup.html")


# Signin page
@app.route("/login", methods=['GET', 'POST'])
def login():
   return render_template("login.html")


# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
   return render_template("contact.html")