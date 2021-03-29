import ipaddress

ip_list = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23',
           ]


def sort_ip(ips):
    return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))


if __name__ == "__main__":
    print(sort_ip(ip_list))
