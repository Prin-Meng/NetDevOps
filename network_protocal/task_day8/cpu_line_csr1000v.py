from matplotlib import pyplot as plt
from read_info_from_db import get_info_from_db
from write_info_to_db import write_cpu_info_db


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_line(cpu_usage_list):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行，每行一图，第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate

    # 设置时间标签显示格式
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))
    ax.set_ylim(0, 100)  # 控制Y轴的取值范围

    # 把cpu_usage_list的数据，拆分为x轴的时间，与y轴的利用率
    x = []
    y = []

    for time, cpu in cpu_usage_list:
        x.append(time)
        y.append(cpu)

    # 添加主题和注释
    plt.title('路由器CPU利用率')
    plt.xlabel('采集时间')
    plt.ylabel('CPU利用率')

    # 当x轴太拥挤的时候可以让他自适应
    fig.autofmt_xdate()

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果你有两套数据，完全可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R1')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 绘制图形
    plt.show()


if __name__ == '__main__':
    # 192.168.0.66是CSR1000v地址，192.168.0.105是数据库地址，向数据库中写入信息
    write_cpu_info_db("192.168.0.66", "tcpipro", '192.168.0.105', 'prin', 'Cisc0123', "dev_info", 60)
    # 获取数据库一分钟内的信息
    time_recode, cpu_usage = get_info_from_db('192.168.0.105', 'prin', 'Cisc0123', 'dev_info')
    cpu_time_info = list(zip(time_recode, cpu_usage))
    # 绘图
    mat_line(cpu_time_info)
