from yang_xml_maker_template import netconf_config_syslog
from netconf_request import csr_netconf_config
from pprint import pprint
import xmltodict


def conf_log(device_ip, username, password, security_id, host):
    result_xml = csr_netconf_config(device_ip, username, password, netconf_config_syslog(security_id, host), port='830')
    xmldict = xmltodict.parse(result_xml)
    pprint(xmldict)


if __name__ == '__main__':
    conf_log('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.100')

