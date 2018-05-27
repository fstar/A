import os
import sys

if (len(sys.argv) > 1 and sys.argv[1] == "deploy") or os.environ.get("PROJECT_ENV") == "deploy":
    environment = "deploy"
else:
    environment = "test"

if environment == "test":
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_DB = "test"

    REDIS_HOST = "localhost"
    REDIS_PASSWORD = "test"
    REDIS_PORT = 6379
    REDIS_DATABASE = 5
    REDIS_URL = "redis://:{0}@{1}:{2}/{3}".format(REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DATABASE)

    db_host = "localhost"
    db_port = "5432"
    db_user = "test"
    db_password = "test"
    db_name = "A"
    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (
        db_user, db_password, db_host, db_port, db_name)

elif environment == "deploy":
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_DB = "test"

    REDIS_HOST = "localhost"
    REDIS_PASSWORD = "test"
    REDIS_PORT = 6379
    REDIS_DATABASE = 5
    REDIS_URL = "redis://:{0}@{1}:{2}/{3}".format(REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DATABASE)

    db_host = "localhost"
    db_port = "3307"
    db_user = "root"
    db_password = "test"
    db_name = "A"
    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (
        db_user, db_password, db_host, db_port, db_name)


class Config:
    SECRET_KEY = "A_web"
    MONGODB_HOST = MONGODB_HOST
    MONGODB_PORT = MONGODB_PORT
    MONGODB_DB = MONGODB_DB

    REDIS_URL = REDIS_URL

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

