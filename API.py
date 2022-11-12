import requests
import json
api_url = "http://ipwho.is/8.8.4.4"
response = requests.get(api_url)
data = response.text
json.loads(data)
