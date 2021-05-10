import time
import paramiko


def ssh_multicmd(ip, username, password, cmd_list, asy_id, wait_time=2, verbose=True):
    try:
        print('try ssh' + str(asy_id))
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5, compress=True)
        print("You have successfully connect to " + ip + '\n')
    except paramiko.ssh_exception.AuthenticationException:
        print("User authentication failed for " + ip + ".")
        return

    # 激活交互式shell
    command = ssh.invoke_shell()
    # 等待网络设备回应
    command.send("system\n")
    # 执行具体的命令
    for cmd in cmd_list:
        command.send(cmd)
    time.sleep(wait_time)
    # 获取路由器返回信息
    output = command.recv(65535)
    x = output.decode('ascii')
    # 关闭连接
    ssh.close()
    if verbose:
        print(x)
    return x


if __name__ == '__main__':
    # 执行命令，查看show version的值，和配置OSPF
    commands = ['ospf 1\n', 'area 0\n', 'network 192.168.56.0 0.0.0.255\n']
    return_results = ssh_multicmd('192.168.56.205', 'prin', 'Huawei@123', commands, 1)

