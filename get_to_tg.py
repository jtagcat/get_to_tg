"""
ENV VARIABLES REQUIRED:
 - GTT_BOT_TOKEN
"""
"""
Run in development env:
export FLASK_ENV=development
export FLASK_APP=get_to_tg.py
flask run
"""


### ENV Vars ###
from flask import Flask, Response, request # General flask, and the handle requests on the fly thing.
import os # for ENV arguments
import requests

api_url_base = 'https://api.telegram.org/bot{token}/sendMessage'.format
api_url = api_url_base(token=str(os.environ['GTT_BOT_TOKEN'])) # will raise if empty

### FLASK ###
app = Flask(__name__)


@app.route('/', methods=['GET'])
def parse_request():	# If somebody accesses us
	message = request.args.get('message')
	chat_id = request.args.get('chat_id')
	
	if not message:
		message = request.args.get('content') # Compatability with https://github.com/markusfisch/BinaryEye

	if not chat_id: # empty
		return Response('Missing chat_id.', mimetype='text/plain'), 400
	else:
		response = requests.post(url=api_url, json={
			'text': message,
			'chat_id': chat_id
		})
		return Response(response, mimetype='application/json')
