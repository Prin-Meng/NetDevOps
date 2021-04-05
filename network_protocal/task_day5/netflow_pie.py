from matplotlib import pyplot as plt
import re
import ssh_csr1000v



def find_netflow_info(ip, username, password, cmd_list, enable):
    # 提取需要的信息
    result_raw = ssh_csr1000v.qytang_multicmd(ip, username, password, cmd_list, enable, verbose=False)
    netflow_info_raw = re.findall('APP NAME[\s\S]+', result_raw)[0]
    netflow_info = re.findall('port\s(\w+)\s+(\d+)',netflow_info_raw)
    return netflow_info


def mat_bing(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.01, 0.01, 0.01, 0.01)

    patches, label_text, percent_text = plt.pie(size_list,
                                                # explode=explode,
                                                labels=name_list,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    # 改变文本的大小,方法是把每一个text遍历。调用set_size方法设置它的属性
    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


if __name__ == "__main__":

    counters = []
    protocols = []
    command = ['show flow monitor name qytang-monitor cache format table\n']
    netflow_info = find_netflow_info('192.168.0.66', 'Prin', 'Cisco123', command, 'cisco')
    for info in netflow_info:
        protocols.append(info[0])
        counters.append(int(info[1]))
    mat_bing(counters, protocols)
