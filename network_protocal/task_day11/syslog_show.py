import sqlite3
from matplotlib import pyplot as plt
from syslog_server_to_db import severity_level_dict


def syslog_show_error_level_pie(dbname):
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 提取安全级别和数量信息
    cursor.execute("select severity_level as level,COUNT(*) as count from syslogdb group by severity_level")
    yourresults = cursor.fetchall()

    level_list = []
    count_list = []

    # 把结果写入leve_list和count_list的列表
    for level_info in yourresults:
        level_list.append(severity_level_dict[level_info[0]])
        count_list.append(level_info[1])

    print(level_list)
    print([float(count) for count in count_list])

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 使用count_list的比例来绘制饼图
    # 使用level_list作为注释
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=level_list,
                                      labeldistance=1.1,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title('SYSLOG严重级别分布图')  # 主题
    plt.legend()
    plt.show()


def syslog_show_source_pie(dbname):
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 提取log源与其对应的数量
    cursor.execute("select log_source,COUNT(*) as count from syslogdb group by log_source")
    yourresults = cursor.fetchall()

    source_list = []
    count_list = []

    # 将数据库的信息，依次写入两个列表
    for source_info in yourresults:
        source_list.append(source_info[0])
        count_list.append(source_info[1])

    print(source_list)
    print([float(count) for count in count_list])

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 使用count_list的比例来绘制饼图
    # 使用level_list作为注释
    patches, l_text, p_text = plt.pie(count_list,
                                      labels=source_list,
                                      labeldistance=1.1,
                                      autopct='%3.1f%%',
                                      shadow=False,
                                      startangle=90,
                                      pctdistance=0.6)

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = 30
    for t in p_text:
        t.set_size = 20
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title('日志源分布图')  # 主题
    plt.legend()
    plt.show()


if __name__ == '__main__':
    syslog_show_error_level_pie("syslog.sqlite")
    syslog_show_source_pie("syslog.sqlite")
