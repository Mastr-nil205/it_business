import os

from flask import Flask, render_template

from . import db

def create_app(test_config=None):
    """
    Create and configure the app.

    Parameters:
        test_config (dict, optional): A dictionary containing the test configuration. Defaults to None.

    Returns:
        Flask: An instance of the Flask application.
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'itcloudpath.postgres'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/home')
    def home():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    # Initialize the SQLAlchemy object
    db.init_app(app)

    from . import services
    app.register_blueprint(services.bp, url_prefix='/services')

    return app


