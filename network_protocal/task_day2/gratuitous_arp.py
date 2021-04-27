import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
import time


def gratuitous_arp(ip_address):  # 发送无故ARP请求并等待响应
    try:
        print("一直发送无故ARP，直到ctrl+c停止")
        while True:
            sendp(ARP(op=2, psrc=ip_address, pdst=ip_address), verbose=False)
            print('发送无故arp成功')
            time.sleep(1)
    except KeyboardInterrupt:
        print('退出程序成功')


if __name__ == '__main__':
    gratuitous_arp('192.168.0.107')
