from matplotlib import pyplot as plt
from influxdb_get_data import get_one_minutes_info
from influxdb_init_connect import influx_host, router_ip


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_line(mem_usage_time_info):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行，每行一图，第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate

    # 设置时间标签显示格式
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M:%S'))

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%3.2f%%'))
    ax.set_ylim(0, 100)  # 控制Y轴的取值范围

    # 把mem_usage_time_info的数据，拆分为x轴的时间，与y轴的利用率
    x = []
    y = []

    for time, mem in mem_usage_time_info:
        x.append(time)
        y.append(mem)

    # 添加主题和注释
    plt.title('路由器MEM利用率')
    plt.xlabel('采集时间')
    plt.ylabel('MEM利用率')

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
    # 获取数据库一分钟内的信息
    time_recode, mem_usage = get_one_minutes_info(influx_host, router_ip)
    mem_usage_time_info = list(zip(time_recode, mem_usage))
    # 绘图
    mat_line(mem_usage_time_info)
