from ssh_device import ssh_multicmd
from multiprocessing import cpu_count, Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support

results = []
commands = ['ospf 1\n', 'area 0\n', 'network 192.168.56.0 0.0.0.255\n']


# 多进程
def multi_process(ip_prefix, suffix, username, password, commands):
    freeze_support()
    cpus = cpu_count()  # 得到内核数的方法
    pool = ProcessPool(cpus)  # 有效控制并发进程或者线程数，默认为内核数(推荐)

    # 设置对应函数和传入的参数
    for i in suffix:
        result = pool.apply_async(ssh_multicmd, args=(ip_prefix + str(i), username, password, commands, i, 2, False))
        results.append(result)

    # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.close()
    pool.join()

    for info in results:
        print(info.get())


# 多线程
def multi_thread(ip_prefix, suffix, username, password, commands):
    pool = ThreadPool(100)
    # 设置对应函数和传入的参数
    for i in suffix:
        result = pool.apply_async(ssh_multicmd, args=(ip_prefix + str(i), username, password, commands, i, 2, False))
        results.append(result)

    # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.close()
    pool.join()

    for info in results:
        print(info.get())


if __name__ == '__main__':
    # 多线程
    # multi_thread('192.168.56.20', range(1, 6), 'prin', 'Huawei@123', commands)
    # 多进程
    multi_process('192.168.56.20', range(1, 6), 'prin', 'Huawei@123', commands)