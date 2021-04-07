import pg8000
import datetime


def get_info_from_db(host, user, password, dbname):
    # 连接数据库
    conn = pg8000.connect(host=host, user=user, password=password, database=dbname)
    cursor = conn.cursor()

    # 查看一分钟内写入的信息
    now = datetime.datetime.now()
    one_minute_age = now - datetime.timedelta(minutes=1)
    string_time = one_minute_age.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("select * from routerdb where time > '%s'" % string_time)
    all_result = cursor.fetchall()

    # 记录时间和CPU利用率
    time_recode = []
    cpu_usage = []

    # 得到时间和CPU利用率
    for x in all_result:
        print(x[1], x[2])
        time_recode.append(x[1])
        cpu_usage.append(x[2])
    return time_recode, cpu_usage


if __name__ == '__main__':
    time_recode, cpu_usage = get_info_from_db('192.168.0.105', 'prin', 'Cisc0123', 'dev_info')

