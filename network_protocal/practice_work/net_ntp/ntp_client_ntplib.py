import ntplib
from time import ctime


def ntp_client(ntp_server):
    c = ntplib.NTPClient()
    response = c.request(ntp_server, version=3)
    # print(response.tx_time) # 1596243472.7740922
    # ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
    # Sat Aug  1 08:57:52 2020
    print('\t' + ctime(response.tx_time))


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    ntp_client('0.cn.pool.ntp.org')