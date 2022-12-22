from github import Github
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
# using username and password
#g = Github("user", "password")

# or using an access token
g = Github(access_token)
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)

""""
# To send data form-encoded data
response = requests.post(urlFakeData, headers=headers, data=data)

url = os.getenv("URL_HELLO")
urlFakeData = os.getenv("URL_FAKE_DATA")

data = {
    "firstName": "Edinson",
    "lastName": "Cavani",
    "checkbox": "false"
}

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
"""
