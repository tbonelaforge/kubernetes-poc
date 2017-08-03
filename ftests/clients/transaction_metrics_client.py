import requests

from test_client import BASE_URL

class TransactionMetricsClient(object):

    def get(self, subscribe_key):
        url = BASE_URL + '/transaction_metrics/' + str(subscribe_key)
        get_request = requests.get(url)
        return get_request