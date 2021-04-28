from django.shortcuts import render
from djangoProject.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


def qyt_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # authenticate()函数, 接受用户名和密码, 如果认证通过返回一个User对象
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:  # is not None表示认证通过, user.is_active表示激活状态
            # login()函数的作用是, 使用Django的会话(session)框架, 把用户ID保存在该会话中(维护客户会话状态)
            login(request, user)
            # 设置会话变量, 名字是随意设计的, 数量也并没有限制
            request.session['fname'] = request.user.first_name
            # 如果属于employee组，就设置device_permission会话变量
            if Group.objects.get(name='employee') in user.groups.all():
                request.session['device_view_permission'] = True
            # 如果用户有'qyt_devices.view_devicedb'权限，就设置device_permission会话变量
            elif 'qyt_devices.view_devicedb' in request.user.get_all_permissions():
                request.session['device_view_permission'] = True
            # 如果用户有'qyt_devices.add_devicedb'权限，就设置device_permission会话变量
            if 'qyt_devices.add_devicedb' in request.user.get_all_permissions():
                request.session['device_add_permission'] = True
            # 如果用户有'qyt_devices.delete_devicedb'权限，就设置device_permission会话变量
            if 'qyt_devices.delete_devicedb' in request.user.get_all_permissions():
                request.session['device_delete_permission'] = True
            # 重定向回触发重定向的初始页面
            next_url = request.GET.get('next', '/')
            return HttpResponseRedirect(next_url)

        else:
            return render(request, 'registration/login.html', {'form': form, 'error': '用户名或密码错误'})
    else:
        # 如果用户处于认证状态! 还访问登录页面! 直接重定向到首页
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        else:  # 未认证用户, 给他返回登录页面
            form = UserForm()
            return render(request, 'registration/login.html', {'form': form})


def qyt_logout(request):
    logout(request)  # 注销并取消维护的用户会话
    return HttpResponseRedirect('/accounts/login')  # 重定向到登录页面