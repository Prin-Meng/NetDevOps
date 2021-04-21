import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from models import Devicetype, SNMPtype, DeviceSNMP, Devicedb

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
              }, ]
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
# snmp_info = snmpv2_get("192.168.0.66", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)
# for x in range(50):
#     device_cpu_router = Devicecpu(device=Devicedb.objects.get(name='网关路由器'), cpu_uasge=int(snmp_info[1]))
#     device_cpu_router.save()
#     sleep(1)
#
# cpu_info =
