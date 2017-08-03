import requests

from test_client import BASE_URL

class HealthClient(object):

    def get(self):
        url = BASE_URL + '/health'
        get_request = requests.get(url)
        return get_request