from flask import Flask, send_file
from flask import jsonify
from flask import render_template
from flask import request 
from common import yellow, cyan, log, green
import time
# import sqlite3
# from helpers.qr_code_maker import getQRCodeImage
# from io import BytesIO,StringIO
import base64
import json

# from helper import json_parse
#### Globals 
app = Flask(__name__)
stores = [] 



#### Endpoints
@app.route('/write', methods=['POST'])
def write():    
    content = request.json
    x = content['things']
    yellow("write")
    cyan(x)
    x = content['things']
    product = x['product']

    start = time.time()
    resultAsJson = write_product(x['network'], x['namespaceId'], x['groupId'], product)
    end = time.time()
    delta = end - start
    resultAsJson['walltime'] = delta
    resultAsJson = {"message":"this is a message "}
    return jsonify(resultAsJson)


@app.route('/read', methods=['POST'])
def read(): 
    content = request.json
    x = content['things']
    yellow("read")
    cyan(x)
    start = time.time()
    return jsonify(resultAsJson)

@app.route('/', methods=['GET'])
def main():

    cyan("main : /")

    message = { 
        "status":"status",
        "projectpath":"projectpath", 
        "kittycat":"kittycat"
    }
    return render_template('main.html', message=message)


@app.route('/healthcheck', methods=['GET'])
def test():
    cyan("healthcheck : ")
    message = { 
        "status":"good"
    }
    return jsonify(message)

@app.route('/doAction', methods=['POST', 'GET'])
def doAction():
    content = request.json
    cyan(content)

    message = { 
        "status":"post and get"
    }
    return jsonify(message)



if __name__ == '__main__':
    cyan("http://34.83.236.108:4040 with database at data/dispense.db")
    cyan("http://localhost:4040 with database at data/dispense.db")
    from waitress import serve
    serve(app, host="0.0.0.0", port=4040)