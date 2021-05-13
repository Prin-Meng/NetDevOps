import requests
from ASA_basic_info import url
from ASA_restapi_token import get_token


def config_int(interface, name, security_level, ip_addr, mask):
    obj_info = {
        "kind": "object#GigabitInterface",
        "hardwareID": interface,
        "interfaceDesc": name,
        "channelGroupID": "",
        "channelGroupMode": "active",
        "duplex": "auto",
        "lacpPriority": -1,
        "managementOnly": False,
        "mtu": 1500,
        "name": name,
        "securityLevel": security_level,
        "shutdown": True,
        "speed": "auto",
        "flowcontrolOn": False,
        "flowcontrolHigh": -1,
        "flowcontrolLow": -1,
        "flowcontrolPeriod": -1,
        "forwardTrafficCX": False,
        "forwardTrafficSFR": False,
        "ipAddress": {
            "kind": "StaticIP",
            "ip": {
                "kind": "IPv4Address",
                "value": ip_addr
            },
            "netMask": {
                "kind": "IPv4NetMask",
                "value": mask
            }
        }
    }

    api_path = "/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"
    url_api = url + api_path

    header = get_token()
    r = requests.put(url_api, headers=header, json=obj_info, verify=False)

    if r.ok:
        return f'配置接口{interface}成功'
    else:
        return '配置出错'


def config_route(dest_network, out_int, next_hop):
    obj_info = {
        "kind": "object#IPv4Route",
        "gateway": {
            "kind": "IPv4Address",
            "value": next_hop
        },
        "distanceMetric": 1,
        "network": {
            "kind": "IPv4Network",
            "value": dest_network
        },
        "tracked": False,
        "tunneled": False,
        "interface": {
            "kind": "objectRef#Interface",
            "name": out_int
        }
    }

    api_path = "/api/routing/static"
    url_api = url + api_path

    header = get_token()
    r = requests.post(url_api, headers=header, json=obj_info, verify=False)

    if r.ok:
        return f'配置路由{dest_network} {next_hop}成功'
    else:
        return '配置出错'


if __name__ == '__main__':
    # 配置IP地址
    print(config_int('GigabitEthernet0/0', 'Outside', 0, '202.100.1.254', '255.255.255.0'))
    print(config_int('GigabitEthernet0/1', 'Inside', 100, '10.1.1.254', '255.255.255.0'))
    print(config_int('GigabitEthernet0/2', 'DMZ', 50, '172.16.1.254', '255.255.255.0'))

    # 配置路由
    print(config_route('1.1.1.0/24', 'Outside', '202.100.1.1'))
    print(config_route('2.2.2.0/24', 'Inside', '10.1.1.1'))
    print(config_route('3.3.3.0/24', 'DMZ', '172.16.1.1'))
