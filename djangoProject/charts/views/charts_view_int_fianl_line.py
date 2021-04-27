from django.shortcuts import render


def echarts_final_line_if_speed(request):
    return render(request, 'charts_int_final_line.html')