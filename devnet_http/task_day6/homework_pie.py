from matplotlib import pyplot as plt
from spider_python_homework import get_homework_info

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_pie(lable_values_dict, Theme):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.01, 0.01, 0.01, 0.01)

    name_list = [key for key in lable_values_dict.keys()]
    size_list = [values for values in lable_values_dict.values()]

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
    plt.title(Theme)  # 主题
    plt.legend()
    plt.show()


if __name__ == '__main__':
    list_info = get_homework_info('pye_menglp', '0Xk-Dwf')
    mat_pie(list_info[0], '课程作业分布图')
    mat_pie(list_info[1], '课程分数分布图')

