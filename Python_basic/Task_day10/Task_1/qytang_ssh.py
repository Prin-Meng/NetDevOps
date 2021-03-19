import paramiko
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
