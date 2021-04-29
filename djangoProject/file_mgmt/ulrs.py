from django.urls import path
from charts.views.charts_view_multi_echarts import multi_echarts
from charts.views.charts_view_echarts_ajax import ajax_chart2, ajax_pie3, ajax_final_line_cpu, ajax_final_line_int
from charts.views.charts_view_cpu_final_line import echarts_final_line_cpu_usage
from charts.views.charts_view_int_fianl_line import echarts_final_line_if_speed

urlpatterns = [
    path('upload_files',)
]
