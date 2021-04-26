from django.shortcuts import render
from qyt_devices.models import Devicedb
from charts.views.charts_get_data_from_db import return_data_from_db
import json



def multi_echarts(request):
    all_data = return_data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'], last_hours=1)
    return render(request, 'charts_multi_echarts.html', {
                                                             'chart2_label': 'CPU利用率',
                                                             # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                                             # 图标的列表
                                                             'chart2_legends': json.dumps(all_data[0]),
                                                             # X轴时间的列表
                                                             'chart2_time': json.dumps(all_data[1]),
                                                             # 多个设备(多线)的数据
                                                             'chart2_data': json.dumps(all_data[2]),
                                                             })
