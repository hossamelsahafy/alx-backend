#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Method that returns the best match
    """
    locale_param = request.args.get('locale')
    if locale_param in app.config['LANGUAGES']:
        return locale_param
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.locale_selector_func = get_locale


@app.route('/')
def index():
    """
    Method that returns the template
    """
    selected_locale = get_locale()
    return render_template('3-index.html',  selected_locale=selected_locale)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
