#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
from datetime import datetime, time
import requests, json, re

api_url = "http://ipwho.is/8.8.4.4"
response = requests.get(api_url)
data = response.text
parse_json = json.loads(data)
info = parse_json["postal"]

@app.route("/", methods=['GET'])
def hello_world():
    today = datetime.today()
    return "<p>Hello World!</p>" + today.strftime('%Y/%m/%d %I:%M:%S') + "<p>Postal code is " + info

app.run()
