import json
import unittest
from unittest.mock import patch, Mock
import os 
from GitHub import get_git_repos, get_git_repo_commits

class GitHubTests(unittest.TestCase):

    MY_REPO_ID = "richkempinski"

    def test_request_response_with_patcher(self):
        """Mocking using a patcher"""
        mock_get_git_repos_patcher = patch('GitHub.get_git_repos')
        mock_get_git_repos = mock_get_git_repos_patcher.start()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/repo-data.json") as file:
            mock_get_git_repos.return_value = json.load(file)
        mock_get_git_repos_patcher.stop()
        repos = mock_get_git_repos()

        self.assertEqual(repos[0].get("node_id"), "MDEwOlJlcG9zaXRvcnkyODc2NTc5MQ==")

        mock_get_git_repos_commits_patcher = patch('GitHub.get_git_repo_commits')
        mock_get_git_repos_commits = mock_get_git_repos_commits_patcher.start()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/repo-commits-data.json") as file:
            mock_get_git_repos_commits.return_value = json.load(file)
        mock_get_git_repos_commits_patcher.stop()
        repo_commits = mock_get_git_repos_commits()

        self.assertEqual(len(repo_commits), 30)
        self.assertEqual(repo_commits[1].get("node_id"), "MDY6Q29tbWl0Mjg3NjU3OTE6M2E5MDc5MDFhZGQ5YTBkMzhlNmExOTkyNTFkZDNkZjBiMTczZWY2Zg==")


if __name__ == "__main__":
    unittest.main()
