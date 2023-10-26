import requests
import json

class Resource:
    def __init__(self):
        self._url = "http://stapi.co/api"

    def _url(self):
        return getattr(self._url)

    def _build_url(self, path):
        return self._url + path

    def _get(self, path, payload=None):
        response = requests.get(self._build_url(path))

        return response.json()