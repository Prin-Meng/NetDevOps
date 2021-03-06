"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from views.index import index
from qyt_devices.views.qyt_add_devices import add_devices
from qyt_devices.views.qyt_show_devices import show_devices
from qyt_devices.views.qyt_delete_devices import delete_devices
from views.qytang_login import qyt_login, qyt_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_devices', add_devices),
    path('show_devices', show_devices),
    path('delete_device/<int:device_id>', delete_devices),
    # 图表信息
    path('charts/', include(('charts.urls', 'charts'), namespace='charts')),
    # 登录、登出，固定URL不能改变
    path('accounts/login/', qyt_login),
    path('accounts/logout/', qyt_logout),
    # 文件管理
    path('file_mgmt/', include(('file_mgmt.urls', 'file_mgmt'), namespace='file_mgmt')),
]
