import os
class Config:
    SECRET_KEY=os.urandom(32)
    @staticmethod
    def init_app():
        pass

class DevelopmentConfigration(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfigration(Config):
    DEBUG= False
    # postgresql:://username:password@localhost:portnumber/dbname
    #SQLALCHEMY_DATABASE_URI = "postgresql://kemo:12345@localhost:5432/api"
    SQLALCHEMY_DATABASE_URI = "postgresql://kemoo:iti@localhost:5432/apinew"



projectConfig= {
    'dev': DevelopmentConfigration,
    'prod': ProductionConfigration
}



