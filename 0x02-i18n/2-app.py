#!/usr/bin/env python3
"""
    Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """
        Method that returns the best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
        Method that Return Template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
