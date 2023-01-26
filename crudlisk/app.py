from flask import Flask


from .ext.db import create_db
from .ext.migration import create_migrate

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "senha ultra secreta"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    db = create_db(app)
    migrate = create_migrate(app, db)

    with app.app_context():
        db.create_all()

    from .blueprints import home
    app.register_blueprint(home.bp)

    from . blueprints import register
    app.register_blueprint(register.bp)

    from . blueprints import login
    app.register_blueprint(login.bp)

    from . blueprints import logoff
    app.register_blueprint(logoff.bp)

    from . blueprints import unsign
    app.register_blueprint(unsign.bp)

    return app

