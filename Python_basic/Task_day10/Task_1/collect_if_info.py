from qytang_ssh import qytang_ssh
from qytang_ping import qytang_ping
import re
import pprint


def qytang_get_if(*ips, username='admin', password='Huawei@123'):
    device_if_dict = {}
    for ip in ips:
        result = qytang_ping(ip)
        if '不通' not in result:
            if_str = qytang_ssh(ip, username, password, 22, 'display ip interface brief\n')
            if_info = re.findall('([A-Z].+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})', if_str)
            if_dict = dict(if_info)
        else:
            if_dict = {}
        new_dict = {ip: if_dict}
        device_if_dict.update(new_dict)

    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.0.11', '192.168.0.22', username='prin', password='Huawei@123'))
