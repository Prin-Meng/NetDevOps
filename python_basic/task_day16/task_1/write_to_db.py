import pg8000
import hashlib
import re
from qytang_ssh import qytang_ssh

# 设备清单
device_list = ['192.168.0.66']
username = 'Prin'
password = 'Cisco123'
commands = ['terminal length 0\n', 'show run\n']


def get_config_md5(ip, username, password, commands):
    try:
        dev_config_raw = qytang_ssh(ip, username, password, commands, 'cisco')
        dev_config = re.findall('hostname[\s\S]+end', dev_config_raw)[0]
    except Exception:
        return

    # 获取配置的MD5值
    m = hashlib.md5()
    m.update(dev_config.encode())
    md5_value = m.hexdigest()

    return dev_config, md5_value


def write_config_md5_to_db():
    # 连接对应数据库
    conn = pg8000.connect(host='192.168.0.106', user='prin', password='Cisc0123', database='dev_info')
    cursor = conn.cursor()
    # 逐个迭代设备，写入数据库
    for device_ip in device_list:
        # 获取当前IP地址对应的配置和MD5值
        config_and_md5 = get_config_md5(device_ip, username, password, commands)
        # 如果获取的结果为None，则直接进入下一个循环
        if not config_and_md5:
            continue
        # 获取当前IP地址的md5值
        cursor.execute("select md5 from config_md5 where ip ='%s'" % device_ip)
        md5_value = cursor.fetchall()

        if not md5_value:
            # 如果设备对应的MD5值不存在，则直接写入信息
            cursor.execute("insert into config_md5(ip,config,md5) values ('%s','%s','%s')" % (
                device_ip, config_and_md5[0], config_and_md5[1]))
        else:
            # 如果计算得到的最新的MD5值与数据库中的存在的MD5值不匹配，将数据库中的配置和MD5值进行更新
            if config_and_md5[1] != md5_value:
                cursor.execute("update config_md5 set config='%s', md5='%s'  where ip ='%s'" % (
                    config_and_md5[0], config_and_md5[1], device_ip))
            else:
                continue

    cursor.execute("select * from config_md5")
    all_result = cursor.fetchall()
    # 打印查看IP和MD5值
    for x in all_result:
        print(x[0], x[2])

    conn.commit()


if __name__ == '__main__':
    # print(get_config_md5('192.168.0.66', username, password, commands))
    write_config_md5_to_db()
