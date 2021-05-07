from ncclient import manager
from ncclient.operations import RPCError
import lxml.etree as ET


# 使用YANG XML配置
def csr_netconf_config(ip, username, password, payload_xml, port='830'):
    # 使用NETCONF客户端ncclient,连接网络设备
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            # 发送构建的XML数据,到网络设备,修改配置(edit_cofig)
            response = m.edit_config(target='running', config=payload_xml).xml
            # 从字符串数据转换到XML
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # 从XML数据,转换到字符串,并返回
        return ET.tostring(data).decode()


# 使用YANG XML获取设备信息, 例如:CPU
def csr_netconf_monitor(ip, username, password, payload_xml, port='830'):
    # 使用NETCONF客户端ncclient,连接网络设备
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            # 发送构建的XML数据,到网络设备,修改配置(edit_cofig)
            response = m.get(payload_xml).xml
            # 从字符串数据转换到XML
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # 从XML数据,转换到字符串,并返回
        return ET.tostring(data).decode()


if __name__ == '__main__':
    pass