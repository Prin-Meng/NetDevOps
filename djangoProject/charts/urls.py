from django.urls import path
from charts.views.charts_view_multi_echarts import multi_echarts
from charts.views.charts_view_echarts_ajax import ajax_chart2, ajax_pie3, ajax_final_line_cpu, ajax_final_line_int
from charts.views.charts_view_cpu_final_line import echarts_final_line_cpu_usage
from charts.views.charts_view_int_fianl_line import echarts_final_line_if_speed

urlpatterns = [
    path('multi_echarts', multi_echarts),
    path('ajax/chart2', ajax_chart2),
    path('ajax/pie3', ajax_pie3),
    path('CPU_final_line', echarts_final_line_cpu_usage),
    path('ajax/final_line_cpu', ajax_final_line_cpu),
    path('int_final_line', echarts_final_line_if_speed),
    path('ajax/final_line_int', ajax_final_line_int),
]
