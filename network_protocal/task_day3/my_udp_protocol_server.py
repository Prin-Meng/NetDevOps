import socket
import sys
import pickle
import struct
import hashlib

address = ("0.0.0.0", 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服务器就绪！等待客户端数据！')

while True:
    try:
        # 最大获取长度不超过2048个字节
        recv_source_data = s.recvfrom(2048)
        raw_values, addr = recv_source_data
        # 获取头部信息（前12bytes）
        head_values = struct.unpack('>hhii', raw_values[:12])
        seq_id = head_values[2]
        length = head_values[3]
        # 获取数据信息 ()
        data = raw_values[12:(12+length)]
        # 获取MD5信息()
        md5_recv = raw_values[(12 + length):]
        # 计算新的MD5信息()
        m = hashlib.md5()
        m.update(data)
        md5_value = m.hexdigest()

        if md5_recv == md5_value.encode():
            print('=' * 80)
            print("{0:30}:{1:<30}".format("数据来源于", str(addr)))
            print("{0:30}:{1:<30}".format("数据序号为", seq_id))
            print("{0:30}:{1:<30}".format("数据长度为", length))
            print("{0:30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))
        else:
            print("MD5值不匹配")

    except KeyboardInterrupt:
        sys.exit()

s.close()
