import json
import unittest

from GitHub import get_github_repos_commits, print_user_repo_commits

class GitHubTests(unittest.TestCase):

    MY_REPO_ID = "richkempinski"
    def test_get_github_repos_commits(self):

        expected_repo_data = {'Mocks': 10, 'Project1': 2, 'hellogitworld': 30, 'helloworld': 6, 'threads-of-life': 1}
        repos = get_github_repos_commits(self.MY_REPO_ID)
        print_user_repo_commits(self.MY_REPO_ID)
        self.assertEqual(repos, expected_repo_data)
        

if __name__ == "__main__":
    unittest.main()