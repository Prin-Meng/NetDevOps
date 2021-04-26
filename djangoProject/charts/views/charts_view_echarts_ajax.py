from django.http import JsonResponse
from charts.views.charts_get_data_from_db import return_data_from_db
from qyt_devices.models import Devicedb


def ajax_chart2(request):
    all_data = return_data_from_db(Devicedb.objects.all(), ['#00BFFF', '#FF3300'], ['line', 'bar'])
    print(all_data)
    return JsonResponse({'labelname': 'CPU利用率',
                         'legends': all_data[0],
                         'labels': all_data[1],
                         'datas': all_data[2]})
