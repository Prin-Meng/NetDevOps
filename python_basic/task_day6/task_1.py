import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n\
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for conn in asa_conn.split('\n'):
    re_result = re.match(
        'TCP\s+Student\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+Teacher\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5}).+bytes\s+(\d+),\s+flags\s+([A-Z]+)',
        conn).groups()
    asa_dict[(re_result[0], re_result[1], re_result[2], re_result[3])] = (re_result[4], re_result[5])
print("打印分析后的字典！")
print(asa_dict)

src_ip = 'src_ip'
src_port = 'src_port'
dst_ip = 'dst_ip'
dst_port = 'dst_port'
bytes_name = 'bytes'
flags = 'flags'
format_str1 = '{0:^10}:{1:^15}|{2:^10}:{3:^15}|{4:^10}:{5:^15}|{6:^10}:{7:^15}'
format_str2 = '{0:^10}:{1:^15}|{2:^10}:{3:^15}'

print("\n格式化打印输出\n")

for key, value in asa_dict.items():
    print(format_str1.format(src_ip, key[0], src_port, key[1], dst_ip, key[2], dst_port, key[3]))
    print(format_str2.format(bytes_name, value[0], flags, value[1]))
    length = len(format_str1.format(src_ip, key[0], src_port, key[1], dst_ip, key[2], dst_port, key[3]))
    print("=" * length)
