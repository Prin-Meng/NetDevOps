import requests
from ASA_basic_info import url
from ASA_restapi_token import get_token

obj_info = {
    "kind": "object#NetworkObj",
    "name": "ASA_IP_INT",
    "host": {
        "kind": "IPv4Address",
        "value": "192.168.0.206"
    },
    "objectId": "ASA_IP_INT"
}

api_path = "/api/objects/networkobjects"
url_api = url + api_path


def restapi_obj():
    header = get_token()
    r = requests.post(url_api, headers=header, json=obj_info, verify=False)


if __name__ == '__main__':
    restapi_obj()
