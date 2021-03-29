import netifaces
import platform
import pprint

pp = pprint.PrettyPrinter(indent=4)


def get_mac_address(ifname):
    if platform.system() == "Linux":
        try:
            return netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0]['addr']
        except ValueError:
            return None
    elif platform.system() == "Windows":
        from win_ifname import win_from_name_get_id
        if_id = win_from_name_get_id(ifname)
        if not if_id:
            return None
        else:
            return netifaces.ifaddresses(if_id)[netifaces.AF_LINK][0]['addr']
    else:
        print('操作系统不支持,本脚本只能工作在Windows或者Linux环境!')


if __name__ == '__main__':
    import platform

    if platform.system() == "Linux":
        print(get_mac_address('ens33'))
    elif platform.system() == "Windows":
        print(get_mac_address('WLAN'))
