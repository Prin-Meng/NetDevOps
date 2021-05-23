from netmiko import ConnectHandler
import json

CSR1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.66',
    'username': 'prin',
    'password': 'Cisc0123',
}

CSR2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.77',
    'username': 'prin',
    'password': 'Cisc0123',
}

CSR_Group = [CSR1, CSR2]

for device in CSR_Group:
    # 避免有连接不上的设备，使用异常处理机制
    try:
        # 依次连接每一个设备
        connect = ConnectHandler(**device)
        print('*' * 50, f"{device['ip']}状态为UP的接口", '*' * 50)
        # 通过textfsm模板对接口信息进行分析
        interfaces = connect.send_command('show ip int brief', use_textfsm=True)
        # print(json.dumps(interfaces, indent=2))

        # 根据打印出的json格式信息，输出状态是UP的接口
        for interface in interfaces:
            if interface["status"] == 'up':
                print(f'{interface["intf"]} is up!  IP address: {interface["ipaddr"]}')

        # 通过textfsm模板对路由条目进行分析
        print('*' * 50, f"{device['ip']}OSPF的路由信息", '*' * 50)
        route = connect.send_command('show ip route', use_textfsm=True)
        # print(json.dumps(route, indent=2))

        # 根据打印出的json格式信息，输出是OSPF的路由信息
        for ospf_route in route:
            if ospf_route['protocol'] == ('O' or 'IA' or 'N1' or 'N1' or 'N2' or 'E1' or 'E2'):
                print(
                    f"OSPF路由:network {ospf_route['network']}/mask {ospf_route['mask']} nexthop_ip {ospf_route['nexthop_ip']}")
    except Exception as e:
        print(e)
