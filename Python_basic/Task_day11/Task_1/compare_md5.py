from qytang_ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Huawei@123'):
    try:
        dev_config_raw = qytang_ssh(ip, username, password)
        dev_config = re.findall('sysname[\s\S]+return', dev_config_raw)[0]
        return dev_config
    except Exception:
        return


def qytang_check_diff(ip, username='admin', password='Huawei@123'):
    m = hashlib.md5()
    m.update(qytang_get_config(ip, username).encode())
    before_md5 = m.hexdigest()
    while True:
        time.sleep(5)
        m = hashlib.md5()
        m.update(qytang_get_config(ip, username, password).encode())
        if before_md5 == m.hexdigest():
            print(before_md5)
        else:
            print(m.hexdigest())
            print('MD5 value changed！')
            break


if __name__ == '__main__':
    qytang_check_diff('192.168.0.11', 'prin')
