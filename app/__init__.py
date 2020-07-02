from config import Config
from flask import Flask, request, session
from flask_babel import Babel, _

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

from app import routes

@babel.localeselector
def get_locale():
    language = session.get("language", None)
    if language is None:
        language = request.accept_languages.best_match(app.config["LANGUAGES"].keys())
        session["language"] = language
    return language
