from restconf_info import username, password, my_headers, client
from requests.auth import HTTPBasicAuth


def get_cpu(device_ip, username, password, monitor_type='5s'):
    if monitor_type == '1m':
        monitor_type_use = 'one-minute'
    elif monitor_type == '5m':
        monitor_type_use = 'five-minutes'
    else:
        monitor_type_use = 'five-seconds'

    url = 'https://' + device_ip + '/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/' + monitor_type_use

    result = client.get(url, headers=my_headers, auth=HTTPBasicAuth(username, password), verify=False)

    if result.ok:
        return result.json().get('Cisco-IOS-XE-process-cpu-oper:{0}'.format(monitor_type_use))
    else:
        return '出现故障'


if __name__ == '__main__':
    # 监控最近五秒钟CPU利用率
    print(get_cpu('192.168.0.88', username, password, '5s'))
