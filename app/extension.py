from flask_pymongo import PyMongo
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

mongodb = PyMongo()
redis_store = FlaskRedis()
mysqldb = SQLAlchemy()

