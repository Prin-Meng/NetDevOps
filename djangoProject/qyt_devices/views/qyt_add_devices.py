from django.shortcuts import render
from qyt_devices.models import Devicedb, Devicetype
from qyt_devices.forms.qyt_add_devices_form import AddDeviceForm
from django.http import HttpResponseRedirect

def add_devices(request):
    if request.method == 'POST':
        # 没有登录
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login?next=/add_devices')
        # 登录但没有权限
        elif not request.session.get('device_add_permission') and request.user.is_authenticated:
            errormessage = '您无权访问此页面'
            return render(request, 'permission_deny.html', {'errormessage': errormessage})

        form = AddDeviceForm(request.POST)
        # 如果请求为POST，并且Form校验通过，把新添加的设备写入数据库
        if form.is_valid():
            devicedb_router = Devicedb(
                name=request.POST.get('name'),
                ip=request.POST.get('ip'),
                description=request.POST.get('description'),
                type=Devicetype.objects.get(id=request.POST.get('type')),
                snmp_ro_community=request.POST.get('snmp_ro_community'),
                snmp_rw_community=request.POST.get('snmp_rw_community'),
                ssh_username=request.POST.get('ssh_username'),
                ssh_password=request.POST.get('ssh_password'),
                enable_password=request.POST.get('enable_password')
            )

            devicedb_router.save()

            form = AddDeviceForm()
            return render(request, 'qyt_add_devices_form.html', {'form': form,
                                                                 'successmessage': '设备添加成功'})
        # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
        else:
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>IP地址已经存在</li></ul>
            return render(request, 'qyt_add_devices_form.html', {'form': form})

    # 如果不是POST，就是GET，表示初始访问，显示表达内容给客户
    else:
        # 没有登录
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/login?next=/add_devices')
        # 登录但没有权限
        elif not request.session.get('device_add_permission') and request.user.is_authenticated:
            errormessage = '您无权访问此页面'
            return render(request, 'permission_deny.html', {'errormessage': errormessage})

        form = AddDeviceForm()
        return render(request, 'qyt_add_devices_form.html', {'form': form})
