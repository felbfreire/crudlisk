from flask_migrate import Migrate


def create_migrate(app, db):
    migrate = Migrate(app, db, render_as_batch=True)

    return migrate
