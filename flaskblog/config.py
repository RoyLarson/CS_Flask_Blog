import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAILL_PW')
    SECRET_KEY = os.environ.get('WEBKEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_LOCATION')