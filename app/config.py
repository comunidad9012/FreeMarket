import os

class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://admin:admin@mysql:3306/freemarket'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='123456789'