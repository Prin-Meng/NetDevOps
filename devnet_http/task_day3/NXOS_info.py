import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = requests.session()

username = 'admin'
password = 'Cisc0123'

nxos1_ip = '192.168.0.199'

nxos1_url = 'https://' + nxos1_ip + '/ins'

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
              'Accept': 'application/json',
              'Content-type': 'application/json-rpc'}
