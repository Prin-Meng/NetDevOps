import re
import ipaddress


def full_ipv6(ipv6):  # 转换为完整的IPv6地址
    return ipaddress.ip_address(ipv6).exploded


def solicited_node_multicast_address(ipv6):  # 拼接得到被请求节点组播地址
    return "FF02::1:FF" + full_ipv6(ipv6)[-7:]


def mac_to_ipv6_linklocal(mac):  # 得到linklocal地址
    # 移除多余的字符，并将16进制书转换到10进制数
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    # 注意第七位取反
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    high1 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff

    return 'fe80::{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)


def ipv6_to_mac(ipv6):  # 将通过EUI64生成的IPv6地址转换为Mac地址
    ipv6_address = full_ipv6(ipv6)
    last_4_sections = ipv6_address.split(":")[-4:]

    mac_1 = int(last_4_sections[0][:2], 16)
    mac_2 = int(last_4_sections[0][2:], 16)
    mac_3 = int(last_4_sections[1][:2], 16)
    mac_4 = int(last_4_sections[2][2:], 16)
    mac_5 = int(last_4_sections[3][:2], 16)
    mac_6 = int(last_4_sections[3][2:], 16)

    # 使用格式化打印,转换10进制位16进制,x为16进制字符串,并且使用02控制长度,并且补0
    return '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(mac_1, mac_2, mac_3, mac_4, mac_5, mac_6)


def mac_to_eui64(mac, prefix):  # 通过MAC地址和前缀，以EUI64的方式生成IPv6地址
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200
    high1 = mac_value >> 24 & 0xff
    low1 = mac_value >> 16 & 0xff
    low2 = mac_value & 0xffff
    host_id = '{:04x}:{:02x}ff:fe{:02x}:{:04x}'.format(high2, high1, low1, low2)

    net = prefix.split("/")[0]

    return net + host_id


if __name__ == '__main__':
    print(full_ipv6('2001::f107:94ac:2717:a736'))
    print(mac_to_eui64(mac='00:50:56:ab:4d:19', prefix='2001:db8:100::/64'))
    print(mac_to_ipv6_linklocal('00:50:56:ab:4d:19'))
    print(solicited_node_multicast_address('2001::f107:94ac:2717:a736'))
