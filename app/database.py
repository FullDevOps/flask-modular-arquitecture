import os
from flask_sqlalchemy import SQLAlchemy


db = None

def init_db(app):
    '''Initialize the database'''
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.instance_path, app.config.get('DATABASE_FILENAME'))
    db = SQLAlchemy(app)

    from app.domain import init_models
    init_models()
    db.create_all()
        
