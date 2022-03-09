from distutils.debug import DEBUG
import os
from pickle import FALSE, TRUE

class Development(object):
    DEBUG = TRUE
    TESTING = FALSE
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    DEBUG = FALSE
    TESTING = FALSE
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}