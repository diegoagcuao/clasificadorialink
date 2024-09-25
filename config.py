import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@localhost/linkscribe'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@35.184.238.185:5432/linkscribe'
