# this is to test updating code via git
import difflib

# imports
import requests
import json
import datetime
from git import Repo

updated_version = "1.0"

current_version = "1.0"

# function to check if its updated
def update_version():
    if current_version == updated_version:
        print("Version is update to date")
    else:
        print("Version is NOT update to date")


# code using subproccess and git diff
def compare_code():
    repo = Repo(".")  # "." indicates the current directory is a Git repository

    diff = repo.git.diff("prod_code.py", "update_prod_code.py")
    print(diff)

