from flask import Flask
from flask_cors import CORS
from gevent import pywsgi

from test import test as test_blueprint
from maze import maze as maze_blueprint
from gacha import gacha as gacha_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(test_blueprint, url_prefix='/test')
app.register_blueprint(maze_blueprint, url_prefix='/maze')
app.register_blueprint(gacha_blueprint, url_prefix='/gacha')
server = pywsgi.WSGIServer(('0.0.0.0', 8090), app)
server.serve_forever()
