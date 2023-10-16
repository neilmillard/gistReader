from unittest import TestCase
import json
import httpretty

from src import API_URL
from src.reader import Reader

GIST_RESPONSE = [
    {
        "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
        "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
        "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
        "id": "aa5a315d61ae9438b18d",
        "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
        "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
        "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
        "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
        "files": {
            "hello_world.rb": {
                "filename": "hello_world.rb",
                "type": "application/x-ruby",
                "language": "Ruby",
                "raw_url": "https://gist.githubusercontent.com/octocat/aa5a315d61ae9438b18d/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
                "size": 167
            }
        },
        "public": True,
        "created_at": "2010-04-14T02:15:15Z",
        "updated_at": "2011-06-20T11:34:15Z",
        "description": "Hello World Examples",
        "comments": 0,
        "user": None,
        "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
        "owner": {
            "login": "octocat",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": False
        },
        "truncated": False
    }
]

HEADERS = {
    "server": "GitHub.com",
    "content-type": "application/json; charset=utf-8"
}


class TestReader(TestCase):
    def setUp(self) -> None:
        httpretty.enable(False)

    def test_get_last_page_number(self):
        body = json.dumps(GIST_RESPONSE)
        status = 200
        httpretty.register_uri(
            httpretty.GET,
            f"{API_URL}/users/octocat/gists",
            status=status,
            body=body,
            adding_headers=HEADERS
        )
        reader = Reader('octocat')
        reader.get_last_page_number()
        self.assertEqual(1, reader.pages)

    def test_get_gists(self):
        body = json.dumps(GIST_RESPONSE)
        status = 200
        httpretty.register_uri(
            httpretty.GET,
            f"{API_URL}/users/octocat/gists",
            status=status,
            body=body,
        )
        reader = Reader('octocat')
        gists = reader.getGists()
        self.assertEqual("aa5a315d61ae9438b18d", gists[0]["id"])