from pymongo import *
import datetime
import numpy as np


def get_info_from_mongodb(ifname, direction, last_mins):
    client = MongoClient('mongodb://prin:Cisc0123@192.168.0.109:27017/admin')
    db = client['admin']

    if_bytes_list = []
    record_time_list = []

    # 循环表中的每一个元素，每个元素是一个字典
    for obj in db.dev_info.find():
        # 如果时间在我们所给的时间中，则进行后面的步骤
        if obj['other_info']['record_time'] > datetime.datetime.now() - datetime.timedelta(minutes=last_mins):
            # 将时间添加到列表里
            record_time_list.append(obj['other_info']['record_time'])
            # 循环每一个接口的字典
            for int_info in obj['int_info']:
                # 如果接口的名称和所给的名称相同
                if int_info['name'] == ifname:
                    # 将接口对应方向的值写入列表
                    if_bytes_list.append(int(int_info[direction + '_bytes']))
                    break


    # 计算两次获取字节数差值
    diff_if_bytes_list = list(np.diff(if_bytes_list))
    # 计算两次时间对象的秒数差值
    diff_record_list = [x.seconds for x in np.diff(record_time_list)]

    # 计算速率
    speed_list = list(
        map(lambda x: round((x[0] * 8 / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_list)))
    record_time_list = record_time_list[1:]

    return record_time_list, speed_list


if __name__ == '__main__':
    print(get_info_from_mongodb('GigabitEthernet1', 'out', 200))

