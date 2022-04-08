'''reading pull requests from git repository'''
import yaml
import os
from github import Github

def get_repo_and_token(pathToYaml):
    '''reading the repo and access tokens from the yaml file'''
    repo_and_token = []
    repos = ""
    access_token = ""
    with open(pathToYaml) as file:
        yamlDict = yaml.load(file, Loader=yaml.FullLoader)
        repo_and_token.append(yamlDict['repo'])
        repo_and_token.append(yamlDict['accessToken'])
    return repo_and_token

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

def checkIfFileExists(path):
    '''check if file exists'''
    if not os.path.exists(path):
        return False
    return True

def trial():
    path = os.getcwd() + "\\conf\\repo.yaml"
    data = []
    if(checkIfFileExists(path)):
        repo_token = get_repo_and_token(path)
        data.append(repo_token[0])
        arr = get_pull_requests(repo_token[0], repo_token[1])
        for x in arr:
            data.append(x)
    else:
        data.append(("Yaml File doesn't exist at path: " + path))
    return data