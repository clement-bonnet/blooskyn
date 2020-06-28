from flask import render_template, redirect, url_for
from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

# handle 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404