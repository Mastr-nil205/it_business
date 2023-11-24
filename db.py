from flask import current_app, g

from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def init_app(app):
    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://itbizuser:firstpath@192.168.1.121:5432/itbizdb'

    # Disable tracking modifications to suppress a warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the SQLAlchemy object to your Flask app
    db.init_app(app)

    app.teardown_appcontext(close_db)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if 'db' not in g:
        g.db = db.create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
    return g.db

def close_db(e=None):
    """Closes the database again at the end of the request."""
    db = g.pop('db', None)

    if db is not None:
        db.dispose()