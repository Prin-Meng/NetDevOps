import socket
import pickle
import struct
import hashlib


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1

    for x in data_list:
        # 获取发送的数据
        send_data = pickle.dumps(x)
        # 计算发送数据的MD5值
        m = hashlib.md5()
        m.update(send_data)
        md5_value = m.hexdigest()
        # 构建报头
        msg_head = struct.pack('>hhii', version, pkt_type, seq_id, len(send_data))
        # 组合成packet
        packet = msg_head + send_data + md5_value.encode()
        # 发送信息到指定地址
        s.sendto(packet, address)

        seq_id += 1
    s.close()


if __name__ == "__main__":
    user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}]
    udp_send_data('192.168.1.2', 6666, user_data)
