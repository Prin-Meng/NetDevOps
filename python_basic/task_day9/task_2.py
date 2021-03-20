from task_1 import *
import re


def ssh_get_route(ip, username, password, port=22, cmd='route -n'):
    result = qytang_ssh(ip, username, password, port, cmd)
    ip_gateway = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+0\.0\.0\.0\s+UG", result)[0]
    return ip_gateway


if __name__ == '__main__':
    print(qytang_ssh('192.168.0.106', 'prin', 'Cisc0123!'))
    print(qytang_ssh('192.168.0.106', 'prin', 'Cisc0123!', cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('192.168.0.106', 'prin', 'Cisc0123!'))
