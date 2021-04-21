from django.contrib import admin

from qyt_devices.models import Devicecpu
from qyt_devices.models import Devicedb
from qyt_devices.models import Devicetype
from qyt_devices.models import DeviceSNMP
from qyt_devices.models import SNMPtype


admin.site.register(Devicedb)
admin.site.register(Devicetype)
admin.site.register(DeviceSNMP)
admin.site.register(Devicecpu)
admin.site.register(SNMPtype)