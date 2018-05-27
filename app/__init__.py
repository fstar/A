from flask import Flask, request
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
print(app.config)

from app.extension import mongodb, redis_store, mysqldb
mongodb.init_app(app)
redis_store.init_app(app)
mysqldb.init_app(app)
print(mysqldb)


from app.db_api import db_api_bp
app.register_blueprint(db_api_bp)

from app.heart import heart_bp
app.register_blueprint(heart_bp)


def regist_blueprint(app):
    from app.db_api import db_api_bp
    app.register_blueprint(db_api_bp)


regist_blueprint(app)

@app.before_request
def before_request():
    print(request.headers)
    print(request.cookies)
mysqldb.create_all(app=app)