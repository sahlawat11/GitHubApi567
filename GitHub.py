""" 
Author: Saransh Ahlawat
CWID: 10444938
Description: Homework 4a
"""

import requests
import json

def get_github_repos_commits(github_user_id):
    repositories = dict()
    
    user_repos = requests.get(f"https://api.github.com/users/{github_user_id}/repos")
    parsed_user_repos = json.loads(user_repos.text)

    for repo in parsed_user_repos:
        repo_name = repo["name"]

        repo_commits_raw = requests.get(f"https://api.github.com/repos/{github_user_id}/{repo_name}/commits")
        repo_commits = json.loads(repo_commits_raw.text)

        repositories[repo_name] = len(repo_commits)
    return repositories


def print_user_repo_commits(github_user_id):
    repo = get_github_repos_commits(github_user_id)
    for repo_name in repo:
        print(f"Repo: {repo_name} Number of commits: {repo.get(repo_name)}")


if __name__ == '__main__':
    print_user_repo_commits("sahlawat11")