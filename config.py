class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'dwai2j31opj52op165kjo21pkp'

    MYSQL_HOST = 'sql7.freemysqlhosting.net'
    MYSQL_DB = 'sql7357583'
    MYSQL_USER = 'sql7357583'
    MYSQL_PASSWORD = 'vHFIwAMjttRr1!KF'
    MYSQL_CURSORCLASS = 'DictCursor'

    UPLOADS = '/home/username/app/app/static/images/uploads' #path on our server

    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/codex'
    SQLALCHEMY_ECHO = False

    SESSION_COOKIE_SECURE = False #works on https server


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    MYSQL_HOST = 'localhost' 
    MYSQL_DB = 'User'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'vHFIwAMjttRr1!KF'
    MYSQL_CURSORCLASS = 'DictCursor'

    UPLOADS = '/home/username/flask_development/app/app/static/images/uploads'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/codex'
    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'User'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'vHFIwAMjttRr1!KF'
    MYSQL_CURSORCLASS = 'DictCursor'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://MYSQL_USER:MYSQL_PASSWORD@MYSQL_HOST/MYSQL_DB'

    UPLOADS = '/home/username/flask_test/app/app/static/images/uploads'
    SQLALCHEMY_ECHO = True

    SESSION_COOKIE_SECURE = False