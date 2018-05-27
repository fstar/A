from flask import Blueprint, request, jsonify
import base64
from bson.json_util import loads, dumps

from app.extension import mongodb, redis_store
from app.models.user_role import *


db_api_bp = Blueprint('db_api_bp', __name__, url_prefix="/db_api")


@db_api_bp.route("/insert/<collection>", methods=["POST"])
def insert_mongo(collection):
    data = request.form.to_dict()
    sorted_key = list(data.keys())
    sorted_key.sort()
    sorted_value = "_".join([data[key] for key in sorted_key])
    sorted_value_encode = base64.b64encode(sorted_value.encode("utf-8"))
    if redis_store._redis_client.sadd(collection, sorted_value_encode) == 1:
        collection_ = mongodb.db[collection]
        inserted_id = collection_.insert_one(data).inserted_id
        return jsonify({"code": 1, "inserted_id": str(inserted_id)})
    else:
        return jsonify({"code": 0, "inserted_id": "2"})


@db_api_bp.route("/get/<collection>", methods=["POST"])
@db_api_bp.route("/get/<collection>/<int:page>/<int:page_size>", methods=["POST"])
def get_mongo(collection, page=1, page_size=50):
    query = request.json
    result = list(mongodb.db[collection].find(query).skip((page-1)*page_size).limit(page_size))
    return dumps({"code": 1, "result": result})


@db_api_bp.route("/get/collectionlist", methods=["GET"])
def get_collectionlist():
    collection_names = mongodb.db.collection_names()
    return jsonify({"code": 1, "collection_names": collection_names})



