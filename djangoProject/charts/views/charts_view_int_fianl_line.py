from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def echarts_final_line_if_speed(request):
    return render(request, 'charts_int_final_line.html')