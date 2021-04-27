from django.http import JsonResponse
from charts.views.charts_get_data_from_db import return_data_from_db
from qyt_devices.models import Devicedb
from random import randint
from datetime import timedelta, datetime, date
import time


def ajax_chart2(request):
    all_data = return_data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'])
    print(all_data)
    return JsonResponse({'labelname': 'CPU利用率',
                         'legends': all_data[0],
                         'labels': all_data[1],
                         'datas': all_data[2]})


def ajax_pie3(request):
    pie3_label = '协议分布'
    pie3_protocol = ['HTTP', 'Telnet', 'SSH', 'ICMP']
    pie3_data = [{'value': randint(20, 100), 'name': p} for p in pie3_protocol]

    return JsonResponse({'labelname': pie3_label,
                         # 协议列表
                         'labels': pie3_protocol,
                         # 协议数据
                         'datas': pie3_data})


# 产生每一条线数据的函数
def line_data(name, time_data_list, color):
    return {
        'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示
        'symbol': 'circle',
        'name': name,
        'type': 'line',
        'smooth': True,
        'smoothMonotone': True,
        'data': time_data_list,
        'areaStyle': {
            'color': color
        },
        'markPoint': {
            'itemStyle': {
                'color': color
            },
            'data': [
                {'type': 'max', 'name': '最大值'},
                {'type': 'min', 'name': '最小值'}
            ]
        },
        'lineStyle': {
            'color': color
        },
        'itemStyle': {
            'color': color
        }
    }


def change_time(datetime_obj):
    return int(time.mktime(datetime_obj.timetuple())) * 1000


def ajax_final_line_cpu(request):
    cpu_time_list_1 = []
    cpu_time_list_2 = []
    now_time = datetime.now()
    # 产生时间和利用率对的列表
    for i in range(1000):
        cpu_time_list_1.append([change_time(now_time + timedelta(minutes=i)), randint(1, 100)])
        cpu_time_list_2.append([change_time(now_time + timedelta(minutes=i)), randint(1, 100)])
    # [[time, int], [time, int], [time, int], [time, int], [time, int], [time, int]]
    cpu_datas = [
        line_data('R1 CPU利用率', cpu_time_list_1, '#00BFFF'),
        line_data('R2 CPU利用率', cpu_time_list_2, '#FF3300'),
    ]

    return JsonResponse({'labelname': 'CPU利用率',
                         'legends': [x['name'] for x in cpu_datas],
                         'datas': cpu_datas,
                         'starttime': date.today().strftime('%Y-%m-%d')})


def ajax_final_line_int(request):
    # 产生随机数据
    g1_up_time_speed_list = []
    g1_down_time_speed_list = []
    now_time = datetime.now()
    for i in range(1000):
        # [[time, int], [time, int], [time, int], [time, int], [time, int], [time, int]]
        g1_up_time_speed_list.append(
            [change_time(now_time + timedelta(minutes=i * 30)),
             randint(40, 60)])
        g1_down_time_speed_list.append(
            [change_time(now_time + timedelta(minutes=i * 30)),
             randint(30, 70)])
        i += 1

    speed_datas = [line_data('G1 up流量', g1_up_time_speed_list, '#00BFFF'),
                   line_data('G1 down流量', g1_down_time_speed_list, '#FF3300')]

    return JsonResponse({'labelname': '接口速率',
                         'legends': [x['name'] for x in speed_datas],
                         'datas': speed_datas,
                         'starttime': date.today().strftime('%Y-%m-%d')})
