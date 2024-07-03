#!/usr/bin/env python3
"""
    Mock logging in
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Union, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError


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


# @babel.localeselector
def get_locale() -> str:
    """
        Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    user = g.get('user')
    if user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.locale_selector_func = get_locale


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
        Returns a user dictionary or None if
        the ID cannot be found or if login_as was not passed.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


def get_timezone() -> str:
    """
    Determines the best match for supported
    time zones based on the following priority:
        1. Time zone from URL parameters
        2. Time zone from user settings
        3. Default to UTC
    """
    timezone = request.args.get('timezone', '').strip()
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    user = g.get('user')
    if user:
        user_timezone = user.get('timezone', None)
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass

    return 'UTC'


babel.timezone_selector_func = get_timezone


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
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
