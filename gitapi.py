import json
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import sys
import git


def check_file(file_name, ext):
    file_name = file_name.translate(
        {ord(i): None for i in '!#@{}[]<>=+£$%^&*()?|,;:/\\\'\"'})
    index = file_name.find(".")
    if index > 0:
        file_name = file_name[0:index]
    elif index == 0:
        file_name = file_name[1:]
    file_name = ".".join([file_name, ext])
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

gitUrl = "https://api.github.com/user/repos"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
data = {
    "name": repo_name,
    "private": "false"
}

#response = requests.get(gitUrl, auth=HTTPBasicAuth(username, access_token))
response = requests.post(gitUrl, auth=HTTPBasicAuth(
    username, access_token), headers=headers, json=data)
print("Headers: ", response.headers)
print("Status Code: ", response.status_code)
print("Response Json : ", response.json)

current_dir = os.getcwd().replace("/", "\\")
# parent directory
parent_dir = os.path.dirname(current_dir)

git.Git(current_dir).clone(
    "https://github.com/{}/{}.git".format(username, repo_name))

os.chdir(os.path.join(current_dir, repo_name))
print(os.getcwd())

readme_data = """
This a README.md test file 
"""
save(readme_data, "README", "md")

# Changing the CWD
os.chdir("../")
repo = git.Repo(repo_name)
repo.git.add('--all')
repo.git.commit("-m", "commit message from python script")
origin = repo.remote(name="origin")
origin.push()
