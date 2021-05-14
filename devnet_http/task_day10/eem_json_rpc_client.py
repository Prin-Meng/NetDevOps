import requests

from cli import *

r = requests.post('http://192.168.0.104:8080/eem',
                  json={'event': 'ospf', 'event_detail': 'ospf', 'interface': 'gig1'})

result_cmd = r.json().get('cmd')

output = configure(result_cmd)

print(output)
