import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os, sys
import git

load_dotenv()

repo_name = sys.argv[1]
access_token = os.getenv("ACCESS_TOKEN")
username = os.getenv("USER_NAME")
url = os.getenv("URL_HELLO")
urlFakeData = os.getenv("URL_FAKE_DATA")
gitUrl = "https://api.github.com/user/repos"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
data = {
    "name": "test-repo",
    "private": "false"
}
""""
#response = requests.get(gitUrl, auth=HTTPBasicAuth(username, access_token))
response = requests.post(gitUrl, auth=HTTPBasicAuth(
    username, access_token), headers=headers, json=data)
print("Headers: ", response.headers)
print("Status Code: ", response.status_code)
print("Response Json : ", response.json)
"""

current_dir = os.getcwd()
# parent directory
parent_dir = os.path.dirname(current_dir)

git.Git(current_dir).clone("https://github.com/{}/{}.git".format(username, repo_name))

os.chdir(os.path.join(parent_dir, repo_name))
print(os.getcwd())
data1 = {
    "firstName": "Edinson",
    "lastName": "Cavani",
    "checkbox": "false"
}

# To send data form-encoded data
#response = requests.post(urlFakeData, headers=headers, data=data)
""""
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
