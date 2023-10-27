import requests

class Resource:
    def __init__(self):
        self._base_url = "http://stapi.co/api"

    def _build_url(self, path):
        return self._base_url + path

    def _get(self, path, payload=None):
        response = requests.get(self._build_url(path))

        return response