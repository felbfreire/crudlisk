from flask import Blueprint, request

from .db import get_users, unsign_user


bp = Blueprint('unsign', __name__)


@bp.route("/unsign", methods=["GET", "POST"])
def unsign():

    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            users = get_users()
            if (request.form['username'], request.form['password']) in [(user[1], user[2]) for user in users]:

                username = request.form['username']

                unsign_user(username=username)
                return 'have a nice day :)'

    return """<form method='post'>
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit>
            </form>
            """
