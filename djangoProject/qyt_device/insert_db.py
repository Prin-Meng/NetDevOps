from tools.snmpv2_get import snmpv2_get
from models import Devicetype, SNMPtype, DeviceSNMP, Devicedb, Devicecpu
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djghomework.settings')
django.setup()

device_type = ['CSR1000v']
device_type_router = 1

snmp_type = ['CPU Total 5Sec']

device_snmp = [{'oid': '1.3.6.1.4.9.9.109.1.1.1.3.7',
                'device_type_name': 'CSR1000v',
                'snmp_type_name': 'CPU Total 5Sec'
                }, ]

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


device_cpu = [ ]
