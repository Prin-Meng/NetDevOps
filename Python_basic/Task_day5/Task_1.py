import re
import os

route_n_result = os.popen("route -n").read()
ip_gateway = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+UG",route_n_result)[0]

print('网关为:'+ip_gateway)
