from flask import Flask, make_response, render_template, send_from_directory, request, jsonify
from urllib.parse import urlparse
import os, jwt

app = Flask(__name__)

@app.route('/')
def index():
	resp = make_response(render_template('index.html'))
	return resp

@app.route('/msg', methods=['POST'])
def msg():
	try:
		host = jwt.decode(request.data, "deb8725dee324b814ee58a3bd454178f", algorithms="HS256")['host']
	except jwt.exceptions.InvalidSignatureError as e:
		return str(e)
	os.system('ping -c 1 ' + host + ' > tmp')
	with open('tmp') as f:
		res = f.read()
	return res

@app.route('/static/<path:path>')
def statics(path):
	return send_from_directory('static', path)

if __name__ == '__main__':
	app.run(port=8000)