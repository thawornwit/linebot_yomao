#!/usr/bin/env python

import flask
import logging
import requests
import configparser
import pixiv

config = configparser.ConfigParser()
config.sections()
config.read('linebot_yomao.conf')

WEBHOOK_PORT = int(config['Default']['webhook_port'])
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_PATH = config['Default']['webhook_path']

pixiv.pixiv_username = config['Default']['pixiv_username']
pixiv.pixiv_password = config['Default']['pixiv_password']

LINE_ENDPOINT = "https://trialbot-api.line.me"

HEADERS = {
    "X-Line-ChannelID": config['Default']['channel_id'],
    "X-Line-ChannelSecret": config['Default']['channel_secret'],
    "X-Line-Trusted-User-With-ACL": config['Default']['mid']
}

app = flask.Flask(__name__)
app.config.from_object(__name__)
app.logger.setLevel(logging.DEBUG)

def send_text(to, text):
	content = {
		"contentType": 1,
		"toType": 1,
		"text": text
	}
	events(to, content)

def send_picture(to, img):
	content = {
		"contentType": 2,
		"toType": 1,
		"originalContentUrl": img["origin"],
		"previewImageUrl": img["thumb"]
	}
	events(to, content)

def events(to, content):
	app.logger.info(content)
	data = {
		"to": to,
		"toChannel": "1383378250",
		"eventType": "138311608800106203",
		"content": content
	}
	r = requests.post(LINE_ENDPOINT + "/v1/events", json=data, headers=HEADERS)
	app.logger.info(r.text)


@app.route('/')
def index():
	return ''

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
	json_string = flask.request.json
	app.logger.info(json_string)
	app.logger.info(flask.request.headers)
	update = json_string['result'][0]
	text = update['content']['text']
	print(text)
	send_text([update['content']['from']], text)
	return ''

app.run(host=WEBHOOK_LISTEN, port=WEBHOOK_PORT, debug=True)
