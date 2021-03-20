import paramiko
import time


def qytang_ssh(ip, username, password, port=22, cmd='dis cu\n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    command = ssh.invoke_shell()
    # 保证dis cu能够一次将所有信息显示出来
    command.send('screen-length 0 temporary\n')
    command.send(cmd)
    time.sleep(2)
    output = command.recv(65535)
    x = output.decode('ascii')
    return x

if __name__ == '__main__':
    print(qytang_ssh('192.168.0.11', 'prin', 'Huawei@123'))
