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


# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
   return render_template("contact.html")