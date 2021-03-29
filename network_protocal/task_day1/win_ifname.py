import netifaces as ni
# import winreg as wr


def get_connection_name_from_guid(iface_guids):  # 将windows下的接口的名称和唯一ID一一对应存入字典并返回
    wr = __import__('winreg', globals(), locals(), ['wr'])
    iface_dict = {}
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')

    for i in iface_guids:
        try:
            reg_subkey = wr.OpenKey(reg_key, i + r'\Connection')
            iface_dict[wr.QueryValueEx(reg_subkey, 'Name')[0]] = i
        except FileNotFoundError:
            pass
    return iface_dict


def win_from_name_get_id(ifname):  # 根据输入的接口名称，返回唯一ID
    x = ni.interfaces()
    return get_connection_name_from_guid(x).get(ifname)


if __name__ == '__main__':
    import platform

    if platform.system() == "Windows":
        print(win_from_name_get_id("WLAN"))
