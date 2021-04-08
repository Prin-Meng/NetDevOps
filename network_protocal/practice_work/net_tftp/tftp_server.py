from minimumTFTP import Server


def qyt_tftpserver(tftp_dir):
    print("TFTP服务器准备就绪,根目录为", tftp_dir)
    tftp_serverr = Server(tftp_dir)
    tftp_serverr.run()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    # 正常安装有问题,需要把minimumTFTP.py文件放入如下的路径
    # /usr/local/lib/python3.6/site-packages/tools/minimumTFTP.py
    qyt_tftpserver('./tftp_dir')