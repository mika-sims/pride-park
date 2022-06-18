import bson
from flask import current_app, g, abort, make_response
from werkzeug.local import LocalProxy
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from flask import Flask, render_template, redirect, request, url_for, session, flash
from liveserver import LiveServer
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import os
from liveserver import LiveServer
from mimetypes import guess_extension
from werkzeug.utils import secure_filename


app = Flask(__name__)
ls = LiveServer(app)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'wav'])

app.config["MONGO_URI"] = 'mongodb+srv://amare:pridecoding@cluster0.0i04c.mongodb.net/prideDB'
app.secret_key = 'secretlyproud'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True
mongo = PyMongo(app)

user_collection = mongo.db.users


# Landing page
@app.route("/", methods=['GET', 'POST'])
def index():
   if(session.get('user')):
      user = user_collection.find_one({"username": session["user"]})
      return ls.render_template("index.html", user = user_collection.find_one({"username": session["user"]}))
   else:
      session["user"] = "guest"
      return ls.render_template("index.html", user = user_collection.find_one({"username": session["user"]}))


# About page
@app.route("/about", methods=['GET'])
def about():
   return render_template("about.html")

# Blog page
@app.route("/blog", methods=['GET'])
def blog():
   return render_template("blog.html")


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
   """
   Login function to let a user login if their username and email are in the database
   """
   if request.method == "POST":
      user_input = user_collection.find_one({"username": request.form.get("username")})
      if(user_input != None):
         user_name = request.form.get("username")
         if(user_input["password"] == request.form.get("password")):
            session["user"] = user_name
            flash(f'Welcome back {user_name}!')
            return redirect(url_for("index"))
         else:
            flash("Incorrect password")
            session["user"] = "guest"
            return render_template("login.html", user=user_collection.find_one({"username": session["user"]}))
      else:
         flash("No user account with this name exists")
         session["user"] = "guest"
         return render_template("login.html", user=user_collection.find_one({"username": session["user"]}))
   return render_template("login.html")


@app.route('/profile/<username>')
def profile(username):
   profile = user_collection.find_one({"username": session['user']})
   print(profile)
   if profile == 'guest':
      return redirect(url_for('login'))
   else:
      return render_template('profile.html')


# Record audio
@app.route('/record', methods=['GET', 'POST'])
def record():
   if request.method == "POST":
      user = session['user']
      user = user_collection.find_one({'username': user})
      f = request.files['audio_data']
      mongo.save_file(f'{user}_pod', f)
      with open(f'static/uploads/{user}'+ 'audio.wav', 'wb') as audio:
         f.save(audio)
      print('file uploaded successfully')

      return render_template('record.html', request="POST")
   else:
      return render_template("record.html")


@app.route('/episode/<episodename>')
def episode(episodename):
   return mongo.send_file(episodename)


# Contact page
@app.route("/podcasts", methods=['GET', 'POST'])
def podcast_list():
   if request.method == "POST":
      f = request.files['audio_data']
      with open('audio.wav', 'wb') as audio:
         f.save(audio)
      print('file uploaded successfully')

      return render_template('podcast_list.html', request="POST")
   else:
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