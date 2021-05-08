from restconf_info import username, password, my_headers, client
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def conf_log(device_ip, username, password, hostip, serverity):
    json_data = {
        'logging': {
            "hostip": hostip,
            "trap": {
                "severity": serverity
            }
        }
    }
    url = 'https://' + device_ip + '/restconf/data/Cisco-IOS-XE-native:native/logging/'

    result = client.patch(url, headers=my_headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)

    if result.ok:
        return '提交成功'
    else:
        return result.json()


if __name__ == '__main__':
    # 监控最近五秒钟CPU利用率
    print(conf_log("192.168.0.88", username, password, "192.168.0.130", 7))
    print(conf_log("192.168.0.88", username, password, "192.168.0.120", 7))
