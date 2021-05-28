import time
import datetime
from snmpv2_get import snmpv2_get
from influxdb import InfluxDBClient
from influxdb_init_connect import router_ip, snmp_community, influx_host


client = InfluxDBClient(influx_host, 8086, 'devdbuser', 'Cisc0123', 'devdb')

while True:
    # ----------------------写入内存数据------------------------

    # cpmCPUMemoryUsed
    mem_usage = snmpv2_get(router_ip, snmp_community, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)
    # cpmCPUMemoryFree
    mem_free = snmpv2_get(router_ip, snmp_community, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)

    current_time = datetime.datetime.utcnow().isoformat("T")

    # 组织数据信息
    cpu_mem_body = [
        {
            "measurement": "router_monitor",
            "time": current_time,
            "tags": {
                "device_ip": router_ip,
                "device_type": "IOS-XE"
            },
            "fields": {
                "mem_usage": int(mem_usage[1]),
                "mem_free": int(mem_free[1]),
            },
        }
    ]

    # 每个五秒收集数据信息，写入到infldb中
    client.write_points(cpu_mem_body)
    time.sleep(5)
