from django.shortcuts import render


def multi_echarts(request):
    return render(request, 'charts_multi_echarts.html')