import re

str1 = "Port-channel1.189    192.168.189.254 YES   CONFIG  up"

record = re.match("^([A-Z]+[\S]*\d)\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*(up|down)$",str1).groups()

line1 = "%-10s：%s" % ("接口", record[0])
line2 = "%-10s：%s" % ("IP地址", record[1])
line3 = "%-10s：%s" % ("状态", record[2])

print(line1)
print(line2)
print(line3)