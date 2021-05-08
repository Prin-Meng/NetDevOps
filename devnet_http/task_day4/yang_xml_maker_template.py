from jinja2 import Template

tem_path = './jinja2/'


# 监控路由器CPU利用率
def netconf_monitor_cpu(monitor_type):
    with open(tem_path + 'monitor_cpu.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(monitor_type_use=monitor_type)
    return netconf_payload


def netconf_config_syslog(security_id, host):
    with open(tem_path + 'config_syslog.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(security_id=security_id, host_address=host)
    return netconf_payload


if __name__ == '__main__':
    print(netconf_monitor_cpu('5m'))
    print(netconf_config_syslog('7', '192.168.0.88'))
