import os

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1205@localhost/blog'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True  

config_options={
'development':DevConfig,
'production':ProdConfig  
}      
