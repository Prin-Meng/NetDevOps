import pg8000
import hashlib
import re
from compare_diff import diff_txt
from qytang_ssh import qytang_ssh


# 设备清单
device_ip = '192.168.0.66'
username = 'Prin'
password = 'Cisco123'
commands = ['terminal length 0\n', 'show run\n']


def get_config_md5(dev_ip, dev_username, dev_password, dev_commands):
    try:
        dev_config_raw = qytang_ssh(dev_ip, dev_username, dev_password, dev_commands, 'cisco')
        dev_config = re.findall('hostname[\s\S]+end', dev_config_raw)[0]
    except Exception as e:
        print(e)
        return

    # 获取配置的MD5值
    m = hashlib.md5()
    m.update(dev_config.encode())
    md5_value = m.hexdigest()

    return dev_config, md5_value


def write_config_md5_to_db(dbhost, dbuser, dbpass, dbname):
    # 连接对应数据库
    conn = pg8000.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
    cursor = conn.cursor()
    # 逐个迭代设备，写入数据库

    # 获取当前IP地址对应的配置和MD5值
    config_and_md5 = get_config_md5(device_ip, username, password, commands)
    if not config_and_md5:
        print('无法获取设备信息。')
        return None
    # 获取当前IP地址的md5值
    cursor.execute("select md5 from config_md5 where ip ='%s'" % device_ip)
    md5_value = cursor.fetchall()

    if not md5_value:
        # 如果设备对应的MD5值不存在，则直接写入信息
        cursor.execute("insert into config_md5(ip,config,md5) values ('%s','%s','%s')" % (
            device_ip, config_and_md5[0], config_and_md5[1]))
        conn.commit()
        print('设备信息不存在，已经写入信息。')
        return None
    else:
        # 如果计算得到的最新的MD5值与数据库中的存在的MD5值不匹配，返回配置的不同之处
        if config_and_md5[1] != md5_value[0][0]:
            cursor.execute("select config from config_md5 where ip ='%s'" % device_ip)
            config_info = cursor.fetchall()
            compare_info = diff_txt(config_info[0][0], config_and_md5[0])
            # 返回将数据库中的配置和MD5值进行更新
            cursor.execute("update config_md5 set config='%s', md5='%s'  where ip ='%s'" % (
                config_and_md5[0], config_and_md5[1], device_ip))
            conn.commit()
            return compare_info
        else:
            print('设备配置没有改变。')
            return None


if __name__ == '__main__':
    print(write_config_md5_to_db('192.168.0.109', 'prin', 'Cisc0123', 'dev_info'))
