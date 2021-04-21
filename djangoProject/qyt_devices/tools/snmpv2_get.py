from pysnmp.hlapi import *


def snmpv2_get(ip, community, oid, port=161):
    # varBinds是列表，列表中的每个元素的类型是ObjectType（该类型的对象表示MIB variable）
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    # 错误处理
    if error_indication:
        print(error_indication)
    elif error_index:
        print('%s at %s' % (
            error_status,
            error_index and var_binds[int(error_index) - 1][0] or '?'
        )
              )
        # 如果返回结果又多行，需要拼接后返回
    result = ""

    for varBind in var_binds:
        # 返回结果
        result = result + varBind.prettyPrint()
        # 返回的为一个元组，OID与字符串结果
        # print(result)
        return result.split("=")[0].strip(), result.split("=")[1].strip()


if __name__ == '__main__':
    # cpmCPUTotal5sec
    print(snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161))
