from NXOS_info import client, nxos1_url, my_headers, username, password
from requests.auth import HTTPBasicAuth
from pprint import pprint


def json_rpc_show_config(cmd):
    json_data = [
        {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": cmd,
                "version": 1
            },
            "id": 1
        },
    ]
    r = client.post(nxos1_url, headers=my_headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)
    return r.json()


if __name__ == '__main__':
    json_rpc_show_config('ip route 8.8.8.8 255.255.255.255 192.168.0.1')
    json_rpc_show_config('ip route 114.114.114.114 255.255.255.255 192.168.0.1')
    # pprint(json_rpc_show('show ip route static'))
    for dict in \
            json_rpc_show_config('show ip route static')['result']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf'][
                'ROW_addrf'][
                'TABLE_prefix']['ROW_prefix']:
        print(dict['ipprefix'], end=' ')
        print(dict['TABLE_path']['ROW_path']['ipnexthop'])
