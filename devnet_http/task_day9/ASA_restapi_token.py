import requests
from requests.auth import HTTPBasicAuth
from ASA_basic_info import http_headers, username, password, url
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_path = "/api/tokenservices"
auth_url = url + api_path


def get_token():
    try:
        r = requests.post(auth_url, auth=HTTPBasicAuth(username, password), verify=False)

        final_header = http_headers.copy()
        final_header['X-Auth-Token'] = r.headers['X-Auth-Token']
        # 返回插入了'X-Auth-Token'头部的字典
        return final_header
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    pprint(get_token())
