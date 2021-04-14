from pysnmp.entity.rfc3413.oneliner import cmdgen
from network_protocal.task_day8.snmpv2_get import snmpv2_get
from pymongo import *
from pprint import pprint
import datetime
import time


def snmpv2_getnext(ip, community, oid, port=161):
    cmd_gen = cmdgen.CommandGenerator()

    error_indication, error_status, error_index, var_bind_table = cmd_gen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if error_indication:
        print(error_indication)
    elif error_status:
        print(error_status)

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for var_bind_table_row in var_bind_table:
        for item in var_bind_table_row:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


def write_info_to_db(dict_info):
    client = MongoClient('mongodb://prin:Cisc0123@192.168.0.109:27017/admin')
    db = client['admin']
    db.dev_info.insert_one(dict_info)
    print('*'*50+'写入信息:'+'*'*50)
    for obj in db.dev_info.find():
        pprint(obj, indent=4)


if __name__ == '__main__':
    print("收集路由器数据中,按ctrl+c退出")
    try:
        while True:
            # 获取接口名称信息
            if_name_raw = snmpv2_getnext("192.168.0.66", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161)
            if_name_list = [i[1] for i in if_name_raw]

            # 获取接口速率信息
            if_speed_raw = snmpv2_getnext("192.168.0.66", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161)
            if_speed_list = [i[1] for i in if_speed_raw]

            # 获取接口入字节数
            if_in_raw = snmpv2_getnext("192.168.0.66", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161)
            if_in_list = [i[1] for i in if_in_raw]

            # 获取接口出字节数
            if_out_raw = snmpv2_getnext("192.168.0.66", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161)
            if_out_list = [i[1] for i in if_out_raw]

            # 5秒内CPU利用率
            cpu_usage = snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)

            # 内存使用
            mem_usage = snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)

            # 内存空闲
            mem_free = snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)

            # 记录时间
            record_time = datetime.datetime.now()

            # 将其他参数写入一个字典
            other_info_dict = {'cpu_usage:': cpu_usage[1], 'mem_usage': mem_usage[1], 'mem_free': mem_free[1],
                               'record_time': record_time, 'ip': '192.168.0.66'}

            final_list = []
            for name, speed, in_bytes, out_bytes in zip(if_name_list, if_speed_list, if_in_list, if_out_list):
                final_list.append({'name': name, 'speed': speed, 'in_bytes': in_bytes, 'out_bytes': out_bytes})

            # pprint(final_list, indent=4)

            final_dict = {"int_info": final_list, 'other_info': other_info_dict}

            write_info_to_db(final_dict)
            time.sleep(10)
    except KeyboardInterrupt:  # 捕获Ctrl+C，打印信息并退出
            print("Crtl+C Pressed. Shutting down.")

