from napalm import get_network_driver
import json

driver = get_network_driver('huawei_vrp')
SW1 = driver('192.168.0.11', 'prin', 'Huawei@123')
SW1.open()

output = SW1.get_interfaces()

print(json.dumps(output, indent=2))
