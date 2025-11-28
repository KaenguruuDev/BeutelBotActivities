import os
import requests
from github import Github
from github import Auth
from dotenv import load_dotenv

load_dotenv()

PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
REPO_USER = "KaenguruuDev"
REPO_NAME = "RTOSharp"

auth = Auth.Token(PAT_TOKEN)
gh = Github(auth=auth)

repository = gh.get_repo(f"{REPO_USER}/{REPO_NAME}")
commits = repository.get_commits().totalCount

with open("dynamic/COMMITCOUNT", "w") as f:
    f.write(str(commits) + " Commits")
