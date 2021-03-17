import os
import re
import time

x = False

while True:
    port_info = os.popen("netstat -tulnp").read()
    for line in port_info.split('\n'):
        if re.match('tcp.+0.0.0.0:80\s+.+LISTEN.+', line):
            print('HTTP(TCP/80)服务已经打开')
            x = True
            break
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1)
    if x:
        break



