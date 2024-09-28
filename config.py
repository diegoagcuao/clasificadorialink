import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:passworduser@nombrednspostgres:puerto/basededatos'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@localhost/linkscribe'