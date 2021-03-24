from argparse import ArgumentParser
import paramiko


def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    usage = 'python simple_ssh_client -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-i", "--ipaddr", dest="ipaddr", help="SSH Server", default="192.168.0.106", type=str)
    parser.add_argument("-u", "--username", dest="username", help="SSH Username", default="root", type=str)
    parser.add_argument("-p", "--password", dest="password", help="SSH Password", default="root", type=str)
    parser.add_argument("-c", "--command", dest="command", help="Shell Command", default="ls", type=str)

    args = parser.parse_args()

    result = qytang_ssh(args.ipaddr, args.username, args.password, cmd=args.command)
    print(result)