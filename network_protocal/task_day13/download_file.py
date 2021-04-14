from pysnmp.hlapi import *


def snmpv2_get(ip, community, oid, port=161):
    # varBinds���б��б��е�ÿ��Ԫ�ص�������ObjectType�������͵Ķ����ʾMIB variable��
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    # ������
    if error_indication:
        print(error_indication)
    elif error_index:
        print('%s at %s' % (
            error_status,
            error_index and var_binds[int(error_index) - 1][0] or '?'
        )
              )
        # ������ؽ���ֶ��У���Ҫƴ�Ӻ󷵻�
    result = ""

    for varBind in var_binds:
        # ���ؽ��
        result = result + varBind.prettyPrint()
        # ���ص�Ϊһ��Ԫ�飬OID���ַ������
        # print(result)
        return result.split("=")[0].strip(), result.split("=")[1].strip()


if __name__ == '__main__':
    # cpmCPUTotal5sec
    print(snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161))
