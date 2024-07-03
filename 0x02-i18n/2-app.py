#!/usr/bin/env python3
"""
    Basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
        Define Config Class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


def get_locale():
    """
        Method that returns the best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.locale_selector_func = get_locale


@app.route('/')
def index() -> str:
    """
        Method that returns the template
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run
