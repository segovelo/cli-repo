import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os, sys
import git

def check_file(file_name, ext):
    file_name = file_name.translate({ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name = ".".join([file_name,ext])   
    return file_name


def save(data, save_file, ext):
    save_file = check_file(save_file, ext)
    with open(save_file, 'w') as f:
        f.write(data)
        f.close()

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

current_dir = os.getcwd().replace("/","\\")
# parent directory
parent_dir = os.path.dirname(current_dir)

git.Git(parent_dir).clone("https://github.com/{}/{}.git".format(username, repo_name))

os.chdir(os.path.join(parent_dir, repo_name))
print(os.getcwd())

readme_data = """
This a README.md test file 
"""
save(readme_data, "README", "md")

repo = git.Repo("test-repo")
repo.git.add('--all')
repo.git.commit('-m', 'commit message from python script', author='test_user@test.com')
origin = repo.remote(name="origin")
origin.push()


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
