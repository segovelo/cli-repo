import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
url = os.getenv("URL_HELLO")
urlFakeData = os.getenv("URL_FAKE_DATA")

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

data = {
    "firstName": "Edinson",
    "lastName": "Cavani",
    "checkbox": "false"
}

# To send data form-encoded data
#response = requests.post(urlFakeData, headers=headers, data=data)

# To send data json-encoded
response = requests.post(urlFakeData, headers=headers, json=data)
print("Headers: ", response.headers)
print("Status Code: ", response.status_code)
print("Body: ", response.json())

response = requests.get(urlFakeData, headers=headers)  # , json=data)
print("Headers: ", response.headers)
print("Status Code: ", response.status_code)
print("Body: ", response.json())
# Save response as JSON file
with open('output.json', 'w') as f:
    json.dump(response.json(), f)
