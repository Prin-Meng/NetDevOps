from matplotlib import pyplot as plt
from ssh_csr1000v import qytang_multicmd
import re

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
color_list = ['r', 'b', 'g', 'y']


def find_netflow_info(ip, username, password, cmd_list, enable):
    # 提取需要的信息
    result_raw = qytang_multicmd(ip, username, password, cmd_list, enable, verbose=False)
    netflow_info_raw = re.findall('APP NAME[\s\S]+', result_raw)[0]
    # 获取协议名称和字节数
    netflow_info = re.findall('\w+\s(\w+)\s+(\d+)', netflow_info_raw)
    return netflow_info


def mat_column(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=color_list)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=color_list)

    # 添加主题和注释
    plt.title('协议与所占字节数分布')
    plt.xlabel('协议')
    plt.ylabel('字节数(KB)')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


if __name__ == "__main__":

    counters = []
    protocols = []
    command = ['show flow monitor name qytang-monitor cache format table\n']
    netflow_info = find_netflow_info('192.168.0.66', 'Prin', 'Cisco123', command, 'cisco')
    for info in netflow_info:
        protocols.append(info[0]+'协议')
        counters.append(int(info[1])/1000)
    mat_column(counters, protocols)
