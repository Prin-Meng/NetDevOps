from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return render(request, 'index.html', {'qyt_title': '乾颐堂网络管理系统'})
