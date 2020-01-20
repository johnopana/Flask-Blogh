from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    def __repr__(self):
        return f'User {self.username}'
    #method to save new user
class Blogpost(db.Model):
    __tablename__='blogpost'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255),index=True)
    content=db.Column(db.Text)
    comments=db.relationship('Comments',backref='blogpost',lazy='dynamic')
    #method to save a new blogpost
    def post_save(self):
        db.session.add(self)
        db.session.commit()
class Comments(db.Model):
    __tablename__='comment'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text,index=True)
    blogpost_id=db.Column(db.Integer,db.ForeignKey('blogpost.id'))
    #a method to save a new comments
    def comment_save(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()
    #a method to delete comments