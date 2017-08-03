from chompt import Chompt

from clients.health_client import HealthClient
from clients.transaction_metrics_client import TransactionMetricsClient

class ApiTest(Chompt):
    def __init__(self):
        super(ApiTest, self).__init__()

        # Add all the endpoints
        self.incorporate(HealthClient(), 'health')
        self.incorporate(TransactionMetricsClient(), 'transaction_metrics')
