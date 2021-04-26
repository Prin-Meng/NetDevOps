from django.urls import path
from charts.views.charts_show_multi_echarts import multi_echarts

urlpatterns = [
    path('multi_echarts', multi_echarts),
]