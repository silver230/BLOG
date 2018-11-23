import os

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1205@localhost/bloger'
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'sylveromondibloger'
    SENDER_EMAIL = 'sylveromondi@gmail.com'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True  

config_options={
'development':DevConfig,
'production':ProdConfig  
}      
