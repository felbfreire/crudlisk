from flask import Blueprint, request, session, url_for, redirect


bp = Blueprint("home", __name__)



@bp.route("/")
def get_list():
    if 'username' in session:
        return f"you are logged in as {session['username']}"

    return "you have to be loged in"


@bp.route("/add")
def add_to_list():
    return "adding to list.."

@bp.route("/update")
def update_list():
    return "updating list.."

@bp.route("/delete")
def delete_from_list():
    return "deleting from list.."
