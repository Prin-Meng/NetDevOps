from yang_xml_maker_template import netconf_config_syslog
from netconf_request import csr_netconf_config


def conf_log(device_ip, username, password, security_id, host):
    csr_netconf_config(device_ip, username, password, netconf_config_syslog(security_id, host), port='830')


if __name__ == '__main__':
    conf_log('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.100')
    conf_log('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.88')
    conf_log('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.99')
    conf_log('192.168.0.88', 'Prin', 'Cisc0123', '7', '192.168.0.110')
