from django.urls import path
from charts.views.charts_view_multi_echarts import multi_echarts
from charts.views.charts_view_echarts_ajax import ajax_chart2

urlpatterns = [
    path('multi_echarts', multi_echarts),
    path('ajax/chart2', ajax_chart2)
]
