from flask import Flask, render_template

app = Flask(__name__)

# Landing page
@app.route("/", methods=['GET', 'POST'])
def index():
   return render_template("index.html")