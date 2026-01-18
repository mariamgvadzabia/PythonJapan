from ext import db, app, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.String(20))

    role = db.Column(db.String(20), default="guest")

    def __repr__(self):
        return f'< Username: {self.username}, Birthday: {self.birthday}, Password: {self.password}>'

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    img= db.Column(db.String(100), nullable=False, default="default_img.jpg")
    category = db.Column(db.String(50))
    subtitle = db.Column(db.String(300))

    def __repr__(self):
        return f'<Product {self.name}>'