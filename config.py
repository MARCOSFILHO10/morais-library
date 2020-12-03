import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = "postgres://fgiqekumnpkxnh:f9f51ea276128cb30e95b63752662ed34c1c9fd96aa356d973e06e4b8c9ce0d1@ec2-3-216-89-250.compute-1.amazonaws.com:5432/d87k3h90a6t9bo"

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True