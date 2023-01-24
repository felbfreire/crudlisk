from flask import Blueprint, request
from .db import register_user


bp = Blueprint("register", __name__)

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        if request.form['username'] and request.form['email'] and request.form['password']:
            register_user(
                    username=request.form['username'],
                    email=request.form['email'],
                    password=request.form['password']
                    )

            return "Success!"

    return """<form method='post'>
            <p><input type=text name=username>
            <p><input type=text name=email>
            <p><input type=text name=password>
            <p><input type=submit>
            </form>
            """
