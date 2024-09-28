import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:passworduser@nombrednspostgres:puerto/basededatos'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@localhost/linkscribe'
=======
    SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@localhost/linkscribe'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:password@35.184.238.185:5432/linkscribe'
>>>>>>> bea17413e07e1b0f4a193a8a83213fef4bdd08ac
