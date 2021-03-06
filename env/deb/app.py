from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)



@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    