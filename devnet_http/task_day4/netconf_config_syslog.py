from yang_xml_maker_template import netconf_config_syslog
from netconf_request import csr_netconf_config
from pprint import pprint


def csr_syslong_config(device_ip, username, password, security_id, host):
    result = csr_netconf_config(device_ip, username, password, netconf_config_syslog(security_id, host), port='830')
    print(result)
    # xmldict = xmltodict.parse(result_xml)
    # pprint(xmldict)
    # return xmldict['rpc-reply']['data']['cpu-usage']['cpu-utilization'][monitor_type_use]


if __name__ == '__main__':
    csr_syslong_config('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.88')
