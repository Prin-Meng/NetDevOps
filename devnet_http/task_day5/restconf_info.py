import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = requests.session()

username = 'Prin'
password = 'Cisc0123'


my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
              'Accept': 'application/yang-data+json',
              'Content-type': 'application/yang-data+json'}
