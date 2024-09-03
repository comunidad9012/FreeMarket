import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('MYSQL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False