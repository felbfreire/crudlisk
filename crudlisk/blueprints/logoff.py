from flask import Blueprint, session, request, redirect, url_for


bp = Blueprint('logoff', __name__)


@bp.route('/logoff', methods=['GET'])
def logoff():
    try:
        session.pop('username')
        session.pop('password')
        return "<p>You need to be logged in to use crudlisk."
    except KeyError:
        return "<p>You are not logged in"

        


