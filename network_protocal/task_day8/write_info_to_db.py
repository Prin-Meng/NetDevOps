import pg8000
from snmpv2_get import snmpv2_get
import datetime
import time


def write_cpu_info_db(ip, rocommunity, host, user, password, dbname, seconds):
    conn = pg8000.connect(host=host, user=user, password=password, database=dbname)
    cursor = conn.cursor()

    # 创建数据库
    cursor.execute("create table if not exists routerdb(id serial PRIMARY KEY, time timestamp, cpu int)")

    print("正在写入数据......")
    while seconds > 0:
        # cpmCPUTotal5sec
        cpu_info = snmpv2_get(ip, rocommunity, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1]
        # 记录当前时间
        time_info = datetime.datetime.now()
        # 把数据写入数据库
        cursor.execute("insert into routerdb (time, cpu) values ('%s', %d)" % (
            time_info, int(cpu_info)))
        # 每五秒采集一次数据
        time.sleep(5)
        seconds -= 5

    # 提交数据到数据库
    conn.commit()
    # 只查看最近一分钟内的信息
    cursor.execute("select * from routerdb")
    all_result = cursor.fetchall()

    # 打印时间和CPU利用率
    # for x in all_result:
    #     print(x[1], x[2])


if __name__ == '__main__':
    # 192.168.0.66是CSR1000v地址，192.168.0.105是数据库地址
    write_cpu_info_db("192.168.0.66", "tcpipro", '192.168.0.105', 'prin', 'Cisc0123', "dev_info", 60)
