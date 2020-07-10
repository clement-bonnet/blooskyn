from flask import render_template, redirect, url_for, session
from flask_babel import _, get_locale
from app import app

@app.route("/")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html", config=app.config)

@app.route("/form")
def form():
    return render_template("form.html", config=app.config)

# handle 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", config=app.config), 404

# change language
@app.route("/language/<language>")
def set_language(language=None):
    session["language"] = language
    return redirect(url_for("gallery"))