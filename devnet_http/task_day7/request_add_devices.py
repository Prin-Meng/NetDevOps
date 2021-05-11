import requests
import urllib3
from bs4 import BeautifulSoup

devices_info = [{'name': 'pythonAddDevice1',
                 'ip': '192.168.0.99',
                 'description': '乾颐堂网络实验室',
                 'snmp_ro_community': 'tcpipro',
                 'snmp_rw_community': 'tcpiprw',
                 'ssh_username': 'prin',
                 'ssh_password': 'Cisc0123',
                 'enable_password': 'cisco',
                 'type': '4'
                 },
                {'name': 'pythonAddDevice2',
                 'ip': '192.168.0.100',
                 'description': '乾颐堂网络实验室',
                 'snmp_ro_community': 'tcpipro',
                 'snmp_rw_community': 'tcpiprw',
                 'ssh_username': 'prin',
                 'ssh_password': 'Cisc0123',
                 'enable_password': 'cisco',
                 'type': '4'
                 }]


def config_device_info(username, password):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'http://192.168.0.188:8000/accounts/login/'
    username = str(username)
    password = str(password)

    # 建立并保持会话
    client = requests.session()
    # 获取登录页面的内容
    qytang_home = client.get(url, verify=False)

    qytang_soup = BeautifulSoup(qytang_home.text, 'lxml')
    # 找到csrf令牌的值
    csrftoken = qytang_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    # 构建用户名, 密码和csrf值的POST数据
    login_data = {'username': username, 'password': password, "csrfmiddlewaretoken": csrftoken}

    # POST提交数据到登录页面
    client.post(url, data=login_data, verify=False)

    r = client.get('http://192.168.0.188:8000/add_devices')
    device_soup = BeautifulSoup(r.text, 'lxml')

    # 找到csrf令牌的值
    csrftoken = device_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    # 构建用户名, 密码和csrf值的POST数据

    try:
        for device in devices_info:
            device.update({"csrfmiddlewaretoken": csrftoken})
            r = client.post('http://192.168.0.188:8000/add_devices', data=device, verify=False)
            BeautifulSoup(r.text, 'lxml')
            print('add device {0} successfully!'.format(device.get('name')))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    config_device_info('admin', 'Cisc0123')
