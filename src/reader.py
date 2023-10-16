from urllib.request import urlopen

import requests

from src import API_URL
from src.gist import Gist


class Reader:
    def __init__(self, username: str):
        self.username = username
        self.pages = 1
        self.item_per_page = 10
        self.max_page = 1000

    def get_last_page_number(self):
        """Determines the last page number of list-gists-for-a-user
         Github API call for paginating the response
        """
        last_page = 1  # Default last page value
        gist_url = (f"https://api.github.com/users/{self.username}/gists?"
                    f"page={self.max_page}"
                    f"&per_page={self.item_per_page}")
        with urlopen(gist_url) as resp:
            link_header = resp.getheader('Link')
            if link_header:
                entries = link_header.split(",")
                for item in entries:
                    if "last" in item:
                        first_part = item.split(";")[0]
                        query_part = first_part.split("?")[1]
                        first_query = query_part.split("&")[0]
                        if 'page' in first_query:
                            last_page = int(first_query.split("=")[1])
            else:
                last_page = 1
            self.pages = last_page

    def getGists(self):
        # TODO: make this iterate over the pages.
        url = f'{API_URL}/users/{self.username}/gists'
        data = requests.get(url).json()
        return data
