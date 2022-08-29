
def init_models():
    '''Initialize the database models'''
    from app.domain.auth.models import User
    from app.domain.blogs.models import Post


def install_extensions(app):
    '''Install flask extensions in the app'''

    # Flask-SQLAlchemy
    from app.database import init_db
    init_db(app)

    # TODO Flask-WTF

    # Flask-Login
    from app.domain.auth import init_auth_module
    init_auth_module(app)

    # TODO Flask-Principal

    # TODO Flask-Security

    # TODO Bcrypt

    # Flask-Mail

    # Flask-Bootstrap

    # Flask-Moment

    # Flask-Babel

    # Flask-Admin

    # Flask-Cache

    # Flask-Restless

    # Flask-Assets

    # Flask-Script

    # Flask-Migrate

    # Flask-DebugToolbar

    # Flask-Webpack

    # Flask-Themes


def register_blueprints_in_app(app, ip_addr: str = None, server_port: int = None):
    '''Register the routes of each module in the app'''
    from flask import render_template

    @app.get("/")
    def index():
        data: dict = dict(
            name="John Doe",
            ip_address = f'{ip_addr}:{server_port}',
        )
        return render_template('hello.html', data=data)


    @app.get("/about")
    def about():
        return "<p>About</p>"


    from .auth.controllers import auth_controller
    app.register_blueprint(auth_controller.bp)

    from app import printers
    app.register_blueprint(printers.bp)

    from .blogs.controllers import blogs_controller
    app.register_blueprint(blogs_controller.bp)

    return app


from urllib.parse import urlparse, urljoin
from flask import request

def is_safe_url(target):
    '''Validate the target url is safe to redirect to'''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc