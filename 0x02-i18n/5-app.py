#!/usr/bin/env python3
"""
    Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(user_id)

@app.before_request
def before_request():
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        g.user = get_user(user_id)
    else:
        g.user = None

def get_locale():
    if g.user and g.user.get('locale'):
        return g.user['locale']
    return request.args.get('locale', Config.BABEL_DEFAULT_LOCALE)

babel.locale_selector_func = get_locale

@app.route('/')
def index():
    if g.user:
        return render_template('5-index.html', username=g.user['name'])
    else:
        return render_template('5-index.html', username=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
