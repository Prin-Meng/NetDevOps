from napalm import get_network_driver
from datetime import datetime
import time

driver = get_network_driver('huawei_vrp')
device_ip = ['192.168.0.11', '192.168.0.22', '192.168.0.33', '192.168.0.44', '192.168.0.55']
active_devices = []

while True:
    # 找到能够连接的设备
    for ip in device_ip:
        try:
            SW = driver(ip, 'prin', 'Huawei@123')
            SW.open()
            # 如果没有异常，则将IP地址添加到active_devices列表中
            active_devices.append(ip)
        except Exception as e:
            print(ip + '连接失败')

    # 查看配置有无更改，如果有更改，记录更改设备的IP地址，更改时间，更改的内容到记事本中
    for ip in active_devices:
        SW = driver(ip, 'prin', 'Huawei@123')
        SW.open()
        SW.load_merge_candidate(filename='napalm_config_' + ip + '.cfg')
        # 对加载的配置文件和当前运行配置进行比较
        differences = SW.compare_config()
        if len(differences) > 0:
            # 打印出不同点
            print(ip + ':' + differences)
            # 获取当前时间的字符串
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # 将检查配置文件写入记事本中
            with open('change_config', 'a') as f:
                f.write(now + '\n\t' + ip + ':\n\t' + differences + '\n')
            # 如果配置了下面一条代码，则将设备恢复初始配置
            SW.commit_config()
        else:
            print(ip + ':' + '配置没有修改')
            SW.discard_config()
    # 每隔一小时运行一次脚本
    time.sleep(3600)
