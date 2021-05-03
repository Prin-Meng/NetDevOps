from pprint import pprint

import requests

request_result = requests.get('http://192.168.0.188:8000/charts/ajax/chart2')
pprint(request_result.json())