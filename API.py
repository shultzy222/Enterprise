#!/usr/bin/env python3
import requests, json

api_url = "http://ipwho.is/8.8.4.4"
response = requests.get(api_url)
data = response.text
parse_json = json.loads(data)
print ("Response: ",(parse_json))
info = parse_json["postal"]
print ("Postal code: " + info)
