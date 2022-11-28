#!/usr/bin/env python3

import os
import sys
from git import Repo

parent_dir = os.getcwd()
directory = sys.argv[1]
print("Current directory : ", parent_dir)
path = os.path.join(parent_dir, directory)
os.mkdir(path)

os.chdir(path)
repo_path = os.getcwd()
print("Repo path directory : ", repo_path)
repository = Repo.init(repo_path)
