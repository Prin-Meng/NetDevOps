from yang_xml_maker_template import netconf_monitor_cpu
from netconf_request import csr_netconf_monitor
import xmltodict
from pprint import pprint


def get_cpu(device_ip, username, password, monitor_type='5s'):
    if monitor_type == '1m':
        monitor_type_use = 'one-minute'
    elif monitor_type == '5m':
        monitor_type_use = 'five-minutes'
    else:
        monitor_type_use = 'five-seconds'
    result_xml = csr_netconf_monitor(device_ip, username, password, netconf_monitor_cpu(monitor_type_use), port='830')
    xmldict = xmltodict.parse(result_xml)
    # pprint(xmldict)
    return xmldict['rpc-reply']['data']['cpu-usage']['cpu-utilization'][monitor_type_use]


if __name__ == '__main__':
    # 监控最近五秒钟CPU利用率
    print(get_cpu('192.168.0.88', 'Prin', 'Cisc0123', '5s'))
