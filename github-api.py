from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
# using username and password
#g = Github("user", "password")

# or using an access token
g = Github(access_token)
for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)