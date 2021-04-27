from django.shortcuts import render
from qyt_devices.models import Devicedb
from charts.views.charts_get_data_from_db import return_data_from_db
from random import randint
import json


def multi_echarts(request):
    all_data = return_data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'], last_hours=1)

    pie2_label = '协议分布'
    pie2_protocol = ['HTTP', 'Telnet', 'SSH', 'ICMP']
    pie2_data = [{'value': randint(20, 100), 'name': p} for p in pie2_protocol]

    return render(request, 'charts_multi_echarts.html', {
        'chart2_label': 'CPU利用率',
        # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
        # 图标的列表
        'chart2_legends': json.dumps(all_data[0]),
        # X轴时间的列表
        'chart2_time': json.dumps(all_data[1]),
        # 多个设备(多线)的数据
        'chart2_data': json.dumps(all_data[2]),
        # 饼状图2 Django数据
        # 饼状图名称
        'pie2_label': json.dumps(pie2_label),
        # 协议列表
        'pie2_protocol': json.dumps(pie2_protocol),
        # 协议数据
        'pie2_data': json.dumps(pie2_data),
    })
