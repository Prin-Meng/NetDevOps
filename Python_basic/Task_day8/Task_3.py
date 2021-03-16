import logging
from kamene.layers.inet import IP, ICMP
from kamene.sendrecv import sr1

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 'ip 通！'
    else:
        return False

if __name__ == '__main__':
    result = qytang_ping('192.168.0.1')
    if result:
        print(result)
    else:
        print('此地址不通')



