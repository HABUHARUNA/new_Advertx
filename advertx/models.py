from datetime import datetime
from advertx import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(), nullable=False)
    posts= db.relationship('Post', backref='author', lazy=True)
    
    def set_password(self, password_entered):
        self.password = generate_password_hash(password_entered)

    def check_password_match(self, password_entered):
        return check_password_hash(self.password, password_entered)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    description = db.Column(db.Text, nullable= False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

