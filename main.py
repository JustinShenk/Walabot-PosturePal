#!/usr/local/env python
import distance

from flask import Flask, jsonify, response

app = Flask(__name__)

distance = 0

@app.route('/set')
def set():
    global distance
    distance = request.args.get('distance')
    return jsonify(distance)

@app.route('/status')
def status():
    return jsonify(distance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, use_reloader=False)
