import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = '12624208f9fa1814de122914363d1290be4321bcd1d7f938e304952c6bc46b2c'
    SECRET_KEY = '9e5685f304bc5d1ebee39b58b8d47f5111e0a2d824ba7d51c5322ef6d8eb0427'


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR, 'app.db')
