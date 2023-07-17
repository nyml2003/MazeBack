import json
from random import randint
from flask import Blueprint, make_response, jsonify

gacha = Blueprint('gacha', __name__)


@gacha.route('/')
def getGacha():
    # 从本地 JSON 文件中读取 pool 列表
    json_file = 'pool.json'
    with open(json_file, 'r') as f:
        pool = json.load(f)
    return make_response(
        jsonify({
            'message': 'gacha',
            'result': pool[randint(0, len(pool) - 1)]
        }),
        200
    )
