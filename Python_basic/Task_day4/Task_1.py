import re
import os

ifconfig_result = os.popen('ifconfig ' + 'ens33').read()

# 正则表达式查找ip，掩码，广播和MAC地址
ipv4_add = re.findall('inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
netmask = re.findall('netmask\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
broadcast = re.findall('broadcast\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ifconfig_result)[0]
mac_addr = re.findall('ether\s+([a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2})', ifconfig_result)[0]

# 格式化字符串
format_string = '{0:10}:{1}'

print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

# 产生网关的IP地址
net_addr_section = ipv4_add[0:10]
ipv4_gw = net_addr_section + '1'

# 打印网关的IP地址
print('\n我们假设网关IP地址的最后一位为1，因此网关IP地址为：' + ipv4_gw + '\n')

ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall('1\sreceived', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
