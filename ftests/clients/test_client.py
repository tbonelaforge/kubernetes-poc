
from testconfig import config

BASE_URL = 'http://localhost:5000'
if 'service_host' in config:
    BASE_URL = config['service_host']
