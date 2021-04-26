import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()
import time
from qyt_devices.tools.snmpv2_get import snmpv2_get
from qyt_devices.models import Devicetype, SNMPtype, DeviceSNMP, Devicedb, Devicecpu



# 删除现有的数据
# Devicecpu.objects.all().delete()
Devicedb.objects.all().delete()
Devicetype.objects.all().delete()
DeviceSNMP.objects.all().delete()
SNMPtype.objects.all().delete()

# --------------------------设备类型------------------------------
device_type = ['CSR1000v']
for name in device_type:
    device_type_router = Devicetype(name=name)
    device_type_router.save()
# --------------------------设备snmp类型---------------------------
snmp_type = ['CPU Total 5Sec']
for name in snmp_type:
    snmp_type_router = SNMPtype(name=name)
    snmp_type_router.save()
# --------------------------设备snmp-----------------------------
device_snmp = [{'oid': '1.3.6.1.4.9.9.109.1.1.1.3.7',
                'device_type_name': 'CSR1000v',
                'snmp_type_name': 'CPU Total 5Sec'
                }, ]
for dict_info in device_snmp:
    device_snmp_router = DeviceSNMP(
        oid=dict_info['oid'],
        device_type=Devicetype.objects.get(name=dict_info['device_type_name']),
        snmp_type=SNMPtype.objects.get(name=dict_info['snmp_type_name'])
    )
    device_snmp_router.save()
# --------------------------设备信息------------------------------
device_db = [{'device_name': '网关路由器',
              'device_ip': '192.168.0.66',
              'description': '乾颐堂网络实验室',
              'snmp_ro_community': 'tcpipro',
              'snmp_rw_community': 'tcpiprw',
              'ssh_username': 'prin',
              'ssh_password': 'Cisc0123',
              'enable_password': 'cisco',
              'device_type_name': 'CSR1000v'
              },
             {'device_name': '核心路由器',
              'device_ip': '192.168.0.88',
              'description': '乾颐堂网络实验室',
              'snmp_ro_community': 'tcpipro',
              'snmp_rw_community': 'tcpiprw',
              'ssh_username': 'prin',
              'ssh_password': 'Cisc0123',
              'enable_password': 'cisco',
              'device_type_name': 'CSR1000v'
              }]

for dict_info in device_db:
    device_db_router = Devicedb(
        name=dict_info['device_name'],
        ip=dict_info['device_ip'],
        description=dict_info['description'],
        snmp_ro_community=dict_info['snmp_ro_community'],
        snmp_rw_community=dict_info['snmp_rw_community'],
        ssh_username=dict_info['ssh_username'],
        ssh_password=dict_info['ssh_password'],
        enable_password=dict_info['enable_password'],
        type=Devicetype.objects.get(name=dict_info['device_type_name'])
    )
    device_db_router.save()
# --------------------------设备CPU信息----------------------------
print('收集信息中......')

for x in range(50):
    snmpv2_info = snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)
    device_cpu_router = Devicecpu(device=Devicedb.objects.get(name='网关路由器'), cpu_usage=snmpv2_info[1])

    device_cpu_router.save()

    snmpv2_info = snmpv2_get("192.168.0.88", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)
    device_cpu_router = Devicecpu(device=Devicedb.objects.get(name='核心路由器'), cpu_usage=snmpv2_info[1])

    device_cpu_router.save()

    time.sleep(1)

gw = Devicedb.objects.get(name='网关路由器')
print(gw)

# 进行外键搜素
snmp_info = gw.type.devicesnmp.all()

for snmp in snmp_info:
    print(f"SNMP类型:{snmp.snmp_type.name:<20}| OID:{snmp.oid}")

cpu_info = gw.cpu_usage.all()
for cpu in cpu_info:
    print(f"CPU利用率:{cpu.cpu_usage:<5}| 记录时间:{cpu.record_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
