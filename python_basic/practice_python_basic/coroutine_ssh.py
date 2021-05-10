from ssh_device import ssh_multicmd

import gevent
from gevent import monkey

monkey.patch_all()

commands = ['ospf 1\n', 'area 0\n', 'network 192.168.56.0 0.0.0.255\n']


def get_ssh_result(i):
    print("start", i)
    # 执行的任务函数
    result = ssh_multicmd('192.168.56.20' + str(i), 'prin', 'Huawei@123', commands, i, verbose=False)
    print("end", i)
    return result


# 同时执行5个任务，id为1-5
tasks = [gevent.spawn(get_ssh_result, i) for i in [1, 2, 3, 4, 5]]
all_result = gevent.joinall(tasks)

# 获取执行信息
for x in all_result:
    print(x.get())
