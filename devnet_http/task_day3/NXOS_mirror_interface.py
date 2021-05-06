from cisco.interface import *
from nxos import *

# 产生接口实例
lo0 = Interface('loopback0')  # 判断接口是否Down

if lo0.show().admin_state == 'down ':
    # 如果接口处于down的状态,就重新打开接口,并且产生系统日志
    lo0.set_state(s="up")
    py_syslog(3, 'Interface state is down! , try to no shutdown! ')
else:
    # 如果接口处理up状态,依然产生正常的系统日志
    py_syslog(3, 'Interface state is up! ')
