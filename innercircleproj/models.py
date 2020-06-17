import datetime as dt
from innercircleproj import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from innercircleproj import login_manager

class User(db.Model, UserMixin):
    __tablename__="User"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, index = True)
    email = db.Column(db.String, unique = True, index = True)
    password = db.Column(db.String, unique = True, index = True)
    profile_pic = db.Column(db.String, nullable = False, default = "default.jpg")
    posts = db.relationship("Post", backref="author", lazy = True)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        
    def check_password(self, pw):
        return check_password_hash(self.password, pw)
    
    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, email:{self.email}'
    
class Post(db.Model, UserMixin):
    __tablename__="Post"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    
    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id
        
    def __repr__(self):
        return f'{self.title}'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)