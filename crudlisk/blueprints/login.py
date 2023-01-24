from flask import Blueprint, request, session, url_for
from .db import get_users


bp = Blueprint('login', __name__)



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            users = get_users()
            if (request.form['username'], request.form['password']) in [(user[1], user[2]) for user in users]:

                session['username'] = request.form['username']
                session['password'] = request.form['password']

                return f"You are logged in as {session['username']}"

    return """<form method='post'>
            <p><input type=text name=username>
            <p><input type=text name=password>
            <P><input type=submit>
            """


