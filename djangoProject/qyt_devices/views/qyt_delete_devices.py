from qyt_devices.views.qyt_show_devices import show_devices
from qyt_devices.models import Devicedb


def delete_devices(request, device_id):
    try:
        # 获取对应ID的设备的条目
        del_device = Devicedb.objects.get(id=device_id)
        # 从数据库中删除设备条目
        del_device.delete()
        return show_devices(request, successmessage="设备删除成功")
    except Devicedb.DoesNotExist:
        return show_devices(request, errormessage="设备未找到!或者已经被删除!")
