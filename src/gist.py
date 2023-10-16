import requests

from src import API_URL


class Gist(object):
    def __init__(self, url):
        self.gistUrl = url
        self.gistId = url.split('/')[-1]

    def __repr__(self):
        return f'<Gist Object at {self.gistUrl}>'

    def getRawJSON(self):
        return requests.get(f'{API_URL}/gists/{self.gistId}').json()

    def getFileContent(self):
        files = self.getRawJSON()['files']
        return dict([(key, files[key]['content']) for key in files.keys()])
