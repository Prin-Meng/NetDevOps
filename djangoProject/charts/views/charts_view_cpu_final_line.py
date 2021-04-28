from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def echarts_final_line_cpu_usage(request):
    return render(request, 'charts_cpu_final_line.html')
