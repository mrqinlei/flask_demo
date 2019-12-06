import flask
import datetime


from flask import Flask, request, Response, jsonify
from flask_cors import *
import gevent.pywsgi # 导入相关的包
import gevent.monkey
import time
gevent.monkey.patch_all()  # 可选内容，是否加载猴子补丁


class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False


app = Flask(__name__)
CORS(app, supports_credentials=True)
# 从配置对象来加载配置
app.config.from_object(Config)

@app.route('/gevent/time',methods=['get'])
def get_time1():
    time.sleep(10)
    return 'Hello World!'


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run('0.0.0.0',port=8889,debug=True)