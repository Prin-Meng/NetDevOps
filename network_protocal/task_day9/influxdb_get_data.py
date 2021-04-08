import datetime
from influxdb import InfluxDBClient
from influxdb_init_connect import influx_host, router_ip


def get_one_minutes_info(influx_host, router_ip):
    client = InfluxDBClient(influx_host, 8086, 'qytdbuser', 'Cisc0123', 'mem_info')
    # 记录时间和CPU利用率
    time_recode = []
    mem_usage = []

    # 将datetime对象转换为字符串，方便过滤
    now = datetime.datetime.now()
    one_minute_age = now - datetime.timedelta(minutes=1)
    string_time = one_minute_age.strftime('%Y-%m-%d %H:%M:%S')

    # 找到一分钟内的数据信息
    router_monitor_result = client.query(f"select * from router_monitor where time > '{string_time}'")
    for x in router_monitor_result.get_points('router_monitor',  # 表measurement
                                              {
                                                  'device_ip': router_ip,  # tag
                                                  'device_type': 'IOS-XE'  # tag
                                              }):
        # print(x)
        # 转换为datetime对象
        final_time = datetime.datetime.strptime('{0}'.format(x.get('time')), '%Y-%m-%dT%H:%M:%S.%fZ')
        # 返回datetime对象和CPU利用率
        time_recode.append(final_time)
        mem_usage.append(round(int(x.get('mem_usage')) / (int(x.get('mem_usage')) + int(x.get('mem_free'))) * 100, 2))

    return time_recode, mem_usage


if __name__ == '__main__':
    time_recode, mem_usage = get_one_minutes_info(influx_host, router_ip)
    print(time_recode)
    print(mem_usage)
