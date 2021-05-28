from influxdb import InfluxDBClient

influx_host = '192.168.0.166'
router_ip = "192.168.0.66"
snmp_community = "tcpipro"

if __name__ == '__main__':
    # 使用系统管理员来查询信息
    client = InfluxDBClient(influx_host, 8086, 'admin', 'Cisc0123')

    # 查看数据库 
    print(client.get_list_database())
    # 创建数据库
    print(client.create_database('testdb'))
    print(client.get_list_database())
    # 删除数据库
    print(client.drop_database('testdb'))
    print(client.get_list_database())

    # 使用devdb
    client = InfluxDBClient(influx_host, 8086, 'devdbuser', 'Cisc0123', 'devdb')
    measurements_result = client.query('show measurements;')  # 显示数据库中的表
    print(f"Result: {format(measurements_result)}")

    retention_result = client.query('show retention policies on "devdb";')  # 显示数据库中的表
    print(f"Result: {format(retention_result)}")

