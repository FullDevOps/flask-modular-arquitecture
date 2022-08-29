from flask_login import UserMixin

from app.database import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(50), unique=True, nullable=False)
    password: str = db.Column(db.Text, nullable=False)


    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password


    def __repr__(self):
        return f'<User {self.username!r}>'