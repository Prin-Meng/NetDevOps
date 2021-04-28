from django.shortcuts import render
from qyt_devices.models import Devicedb
from django.http import HttpResponseRedirect


def show_devices(request, successmessage=None, errormessage=None):
    # 没有登录
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login?next=/show_devices')
    # 登录但没有权限
    elif not request.session.get('device_view_permission') and request.user.is_authenticated:
        errormessage = '您无权访问此页面'
        return render(request, 'permission_deny.html', {'errormessage': errormessage})

    # 查询整个数据库的信息 object.all()
    result = Devicedb.objects.all()
    # 最终得到设备清单devices_list，清单内部是每一个设备信息的字典
    devices_list = []
    for x in result:
        # 产生学员信息的字典
        devices_dict = {'id_delete': "/delete_device/" + str(x.id),
                        'id': x.id,
                        'name': x.name,
                        'ip': x.ip,
                        'snmp_ro_community': x.snmp_ro_community,
                        'snmp_rw_community': x.snmp_rw_community,
                        'ssh_username': x.ssh_username,
                        'ssh_password': x.ssh_password,
                        'enable_password': x.enable_password,
                        'type': x.type.name,
                        'create_datetime': x.create_datetime,
                        }

        # 提取学员详细信息，并写入字典
        devices_list.append(devices_dict)

    return render(request, 'qyt_show_devices_info.html', {'devices_list': devices_list,
                                                          'successmessage': successmessage,
                                                          'errormessage': errormessage})
