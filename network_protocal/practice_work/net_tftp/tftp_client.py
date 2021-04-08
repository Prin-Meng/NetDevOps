from minimumTFTP import Client


def qyt_tftpclient(server, filedir, file, operation=1):
    tftp_client = Client(server, filedir, file)
    if operation == 1:
        tftp_client.get()
    if operation == 2:
        tftp_client.put()
    print()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径
    # /usr/local/lib/python3.6/site-packages/tools/minimumTFTP.py

    # qyt_tftpclient('10.1.1.100', '.', 'testupload.txt', operation=1)
    qyt_tftpclient('10.1.1.100', '.', 'testupload.txt', operation=2)