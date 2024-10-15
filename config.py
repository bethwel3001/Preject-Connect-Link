
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', ' f"mysql+mysqlconnector://root:''@localhost/connectlink"')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
