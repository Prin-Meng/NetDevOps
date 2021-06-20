# paramiko需要通过pip下载
import paramiko
# import time的目的是为了保证不会因为输入命令或者回显内容过快而导致SSH终端速度跟不上，仅能显示部分命令，而netmiko已经自动解决了此问题
import time


def qytang_ssh(ip, username, password, port=22, cmd='dis cu\n'):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password, timeout=5, compress=True)
        print("You have successfully connect to " + ip + '\n')
        command = ssh.invoke_shell()
        command.send(cmd)
        time.sleep(2)
        output = command.recv(65535)
        x = output.decode('ascii')
        return x

    except paramiko.ssh_exception.AuthenticationException:
        print("User authentication failed for " + ip + ".")
        return


if __name__ == '__main__':
    # 创建三个变量，表示SW3的IP地址、SSH的用户名和密码
    ip = "192.168.56.11"
    username = "prin"
    password = "Huawei@123"

    qytang_ssh(ip, username, password,)
