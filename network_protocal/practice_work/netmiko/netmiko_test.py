# netmiko需要通过pip下载
from netmiko import ConnectHandler

# 设备类型为huawei，除此之外，还支持绝大多数主流厂商的设备，这也是netmiko的优势；其余上参数分别为SW2的IP，SSH的用户名和密码
SW1 = {
    'device_type': 'huawei',
    'ip': '192.168.56.11',
    'username': 'prin',
    'password': 'Huawei@123',
}

print("正在连接设备..........")
# 调用ConnectHandler（）函数，用上一步创建的字典进行SSH连接，并且将返回值赋予connect变量，注意**不可以省略
connect = ConnectHandler(**SW1)

print("Successfully connected to " + SW1['ip'])

# 设置一个列表，其中为配置的命令，这里可以省略'sys'和'return'，因为netmiko会自动加上
config_commands = ['int l0', 'ip address 2.2.2.2 255.255.255.255']

# 调用connect的send_config_set（）函数，发送配置命令，并打印出来
output = connect.send_config_set(config_commands)
print(output)
save = connect.save_config()
print(save)

# 调用connect的send_command（）函数，发送配置命令，并打印
# 注意connect.send_command（）仅能发送一个命令，而send_config_set（）函数则可以一次性发送多个命令
