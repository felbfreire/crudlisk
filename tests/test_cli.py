from crudlisk.app import create_app

from flask import session
import pytest


app = create_app()
client = app.test_client()

def test_get_home(): 
    assert client.get(
            '/',
            ).status_code == 200


def test_login():
    assert client.post(
            '/login',
            data={'username': 'test', 'password': 'test'}
            ).status_code == 200


def test_logoff():
    assert client.get(
            '/logoff',
            ).status_code == 200
