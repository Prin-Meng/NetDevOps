from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'qyt_title': '乾颐堂网络管理系统'})
