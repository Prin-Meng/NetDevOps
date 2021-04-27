from django.http import JsonResponse
from charts.views.charts_get_data_from_db import return_data_from_db
from qyt_devices.models import Devicedb
from random import randint


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

    return JsonResponse({'lablename': pie3_label,
                         # 协议列表
                         'labels': pie3_protocol,
                         # 协议数据
                         'datas': pie3_data,})
