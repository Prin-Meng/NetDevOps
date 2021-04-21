from django.contrib import admin

from qyt_device.models import Devicecpu
from qyt_device.models import Devicedb
from qyt_device.models import Devicetype
from qyt_device.models import DeviceSNMP
from qyt_device.models import SNMPtype


admin.site.register(Devicedb)
admin.site.register(Devicetype)
admin.site.register(DeviceSNMP)
admin.site.register(Devicecpu)
admin.site.register(SNMPtype)
