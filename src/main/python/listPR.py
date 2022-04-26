'''reading pull requests from git repository'''
from dotenv import load_dotenv
import os
from github import Github

load_dotenv()

def get_pull_requests(repo_url, access_token):
    '''use the repo url and access token to get the pull requests from a repo'''
    pull_request_data = []
    git = Github(access_token)
    repo_url = repo_url[19:-4]
    repo_url.replace('https:', 'git:')
    repo = git.get_repo(repo_url)
    pulls = repo.get_pulls(state='open', sort='created', base='main')
    for pull in pulls:
        time_string = pull.created_at.strftime("%m/%d/%Y @ %H:%M:%S")
        pull_request_data.append([pull.number, pull.title, time_string, pull.html_url])
    return pull_request_data

def trial():
    data = []
    access = os.environ.get("ACCESS_TOKEN")
    repo = os.environ.get("REPO_URL")
    repo_token = [repo, access]
    data.append(repo_token[0])
    arr = get_pull_requests(repo_token[0], repo_token[1])
    for x in arr:
        data.append(x)
    return data