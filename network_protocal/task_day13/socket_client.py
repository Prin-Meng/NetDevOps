import json
from socket import *
import base64


def client_json(ip, port, obj):
    # 创建TCP Socket并连接
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((ip, port))

    if 'exec_cmd' in obj.keys():
        send_obj = obj
    elif 'upload_file' in obj.keys():
        with open('{0}'.format(obj['upload_file']), 'rb') as f:
            read_data = f.read()
            bytes_b64code = base64.b64encode(read_data)
            send_obj = {'upload_file': obj['upload_file'], 'file_bit': bytes_b64code.decode()}
    elif 'download_file' in obj.keys():
        send_obj = obj

    # 把obj转换为JSON字节字符串
    send_message = json.dumps(send_obj).encode()
    # 读取1024字节长度数据, 准备发送数据分片
    send_message_fragment = send_message[:1024]
    # 剩余部分数据
    send_message = send_message[1024:]

    while send_message_fragment:
        sockobj.send(send_message_fragment)  # 发送数据分片（如果分片的话）
        send_message_fragment = send_message[:1024]  # 读取1024字节长度数据
        send_message = send_message[1024:]  # 剩余部分数据

    recieved_message = b''  # 预先定义接收信息变量
    recieved_message_fragment = sockobj.recv(1024)  # 读取接收到的信息，写入到接收到信息分片

    while recieved_message_fragment:
        recieved_message = recieved_message + recieved_message_fragment  # 把所有接收到信息分片重组装
        recieved_message_fragment = sockobj.recv(1024)

    return_data = json.loads(recieved_message.decode())

    if 'download_file' not in return_data.keys():
        print('收到确认数据:', return_data)
    else:
        print('收到确认数据:', return_data)
        # 应该考虑写入下载的文件名！但是由于使用了相同的目录测试！所以使用了’download_file.py‘
        with open('download_file.py', 'w+') as f:
            b4code_back = bytes(return_data['file_bit'], 'GBK')
            file_info = base64.b64decode(b4code_back)
            f.write(file_info.decode())
        print('下载文件{0}保存成功！'.format((obj.get('download_file'))))
    sockobj.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    port = 6666

    # 执行命令
    exec_cmd = {'exec_cmd': 'pwd'}
    client_json('192.168.0.188', port, exec_cmd)

    # 上传文件
    upload_file = {'upload_file': 'snmpv2_get_file.py'}
    client_json('192.168.0.188', port, upload_file)

    # 下载文件
    download_file = {'download_file': 'snmpv2_get_file.py'}
    client_json('192.168.0.188', port, download_file)
