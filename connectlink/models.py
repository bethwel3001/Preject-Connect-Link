

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# Initialize SQLAlchemy
db = SQLAlchemy()

# User Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'  # Explicitly naming the table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)  # Storing hashed passwords

    def __repr__(self):
        return f'<User {self.username}>'

# Additional Models Placeholder
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Service {self.name}>'

# Example association table for User-Service relationship (Optional)
user_services = db.Table('user_services',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('services.id'), primary_key=True)
)

# Example association table for User-Service relationship (Optional)