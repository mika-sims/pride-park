from flask import Flask, render_template

app = Flask(__name__)

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
   return render_template("signup.html")


# Signin page
@app.route("/login", methods=['GET', 'POST'])
def login():
   return render_template("login.html")


# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
   return render_template("contact.html")