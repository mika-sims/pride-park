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
from datetime import datetime
from flask_moment import Moment
from liveserver import LiveServer
from mimetypes import guess_extension
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
import env

app = Flask(__name__)
ls = LiveServer(app)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'wav'])
app.config["MONGO_URI"] = 'mongodb+srv://amare:pridecoding@cluster0.0i04c.mongodb.net/prideDB'
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
# app.secret_key = 'secretlyproud'
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
# @app.route('/profile/<username>')
# def profile(username):
#    profile = user_collection.find_one({"username": session['user']})
#    print(profile)
#    if profile == 'guest':
#       return redirect(url_for('login'))
#    else:
#       return render_template('profile.html')
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
# search route function
@app.route("/search", methods=["GET", "POST"])
def search():
    """ Passes querys from  the form then
    searches the Database index forany matching criteria
    """
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("blogs.html", posts=posts)

@app.route("/")
# route function to render the explore page
@app.route("/posts")
# all the blogs written by users
def posts():
    posts = list(mongo.db.posts.find())
    return render_template("blogs.html", posts=posts)

# Podcast page
@app.route("/podcast", methods=['GET'])
def podcast():
   return render_template("podcast.html")


# Create a post
# add / create blogs
@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        post = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "published_date": request.form.get("published_date"),
            "tags": request.form.get("tags"),
            "read_time": request.form.get("read_time"),
            "created_by": session['user']
        }
        mongo.db.posts.insert_one(post)
        flash('Post Successfully Added')
        return redirect(url_for("posts"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('add_post.html', categories=categories)


# edit/update post function
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "content": request.form.get("content"),
            "published_date": request.form.get("published_date"),
            "tags": request.form.get("tags"),
            "read_time": request.form.get("read_time"),
            "created_by": session['user']
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash('Post Successfully Updated')

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template('edit_post.html', post=post, categories=categories)


# delete blog function
@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash('Post has been Successfully deleted!')
    return redirect(url_for("post"))


# create blog categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# add blog categories
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit/update category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category SuccessfullY Updated")
        return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete category route
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))

if __name__ == "__main__":
      app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

