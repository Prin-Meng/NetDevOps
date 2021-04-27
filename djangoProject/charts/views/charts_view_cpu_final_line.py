from django.shortcuts import render


def echarts_final_line_cpu_usage(request):
    return render(request, 'charts_cpu_final_line.html')
