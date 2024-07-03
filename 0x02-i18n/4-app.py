#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    """Define Congig Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
        Method that returns the best match
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel.locale_selector_func = get_locale


@app.route('/', strict_slashes=False)
def index() -> str:
    """
        Method that returns the template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
