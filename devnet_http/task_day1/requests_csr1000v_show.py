from requests.auth import HTTPBasicAuth

import requests


show_info = requests.get('http://192.168.0.66/level/15/exec/-/show/ip/interface/brief/CR',
                         auth=HTTPBasicAuth('admin', 'Cisc0123'))

print(show_info.text)
