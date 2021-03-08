import re

str1 = "Port-channel1.189    192.168.189.254 YES   CONFIG  up"

record = re.match("^([A-Z]+[\S]*\d)\s+([0-2][0-9]{2}\.[0-2][0-9]{2}\.[0-2][0-9]{2}\.[0-2][0-9]{2}).*(up|down)$",str1).groups()

str1 = "%-10s：%s" % ("接口", record[0])
str2 = "%-10s：%s" % ("IP地址", record[1])
str3 = "%-10s：%s" % ("状态", record[2])

print(str1)
print(str2)
print(str3)