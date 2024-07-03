#!/usr/bin/env python3
"""
Mock logging in
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext
from typing import Union, Dict, Optional


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """
        Define Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

def get_locale() -> str:
    """
    Determines the best match for supported languages
    based on the following priority:
        1. Locale from URL parameters
        2. Locale from user settings
        3. Locale from request header
        4. Default locale
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    user = g.get('user')
    if user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.locale_selector_func = get_locale

def get_user() -> Optional[Dict[str, Optional[str]]]:
    """
        Returns a user dictionary or None if the ID
        cannot be found or if login_as was not passed.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request():
    """
        Executes before each request
    """
    g.user = get_user()

@app.route('/', strict_slashes=False)
def index() -> str:
    """
        Renders a basic html template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
