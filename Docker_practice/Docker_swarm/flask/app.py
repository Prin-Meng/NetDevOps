import os
import re
from flask import Flask

app = Flask(__name__)


def return_hostname():
    ifconfig_result = os.popen('ifconfig ' + 'eth0').read()
    # 正则表达式查找ip
    ipv4_add = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
    return ipv4_add


@app.route('/')
def hello():
    host = return_hostname()
    return f'Hello world version 2.0, I am {host}\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5080, debug=True)
