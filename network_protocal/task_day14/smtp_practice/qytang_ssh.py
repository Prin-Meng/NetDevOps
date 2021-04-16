import paramiko
import time


def qytang_ssh(ip, username, password, cmd_list, enable='', wait_time=2, verbose=False):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, password, timeout=5, compress=True)
    print("You have successfully connect to " + ip + '\n')
    # 激活交互式shell
    command = ssh.invoke_shell()
    # 等待网络设备回应
    time.sleep(wait_time)
    # 进入特权模式
    command.send('enable\n')
    command.send(enable + '\n')
    # 执行具体的命令
    for cmd in cmd_list:
        command.send(cmd)
    time.sleep(wait_time)
    # 获取路由器返回信息
    output = command.recv(65535)
    x = output.decode('ascii')
    if verbose:
        print(x)
    return x


if __name__ == '__main__':
    # 执行命令，查看show version的值，和配置OSPF
    commands = ['terminal length 0\n', 'show version\n', 'conf t\n', 'router ospf 1\n',
                'network 192.168.0.0 0.0.0.255 area 0\n']
    return_results = qytang_ssh('192.168.0.66', 'Prin', 'Cisco123', commands, 'cisco', verbose=True)
