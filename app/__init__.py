from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
import pymysql

app = Flask(__name__, template_folder='template', static_folder='static')

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.TestingConfig")

pymysql.install_as_MySQLdb() #initialzie mySQL
db = SQLAlchemy(app) #initialize db
bootstrap = Bootstrap() #initialize boostrap
bootstrap.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager() #initialize login manager
login_manager.init_app(app)
login_manager.login_view = 'login'

from . import routes
from . import auth