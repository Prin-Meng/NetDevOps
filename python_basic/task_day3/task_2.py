import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

record = re.match('([\w]+)\s(server)\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,5})\s(localserver)\s([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,5}),\s(idle)\s(\d+):(\d{2}):(\d{2}),\s(bytes)\s(\d+),\s(flags)\s([A-Z]+)',str1).groups()

str2 ='protocol'

line1 = f'{str2:15}: {record[0]}'
line2 = f'{record[1]:15}: {record[2]}'
line3 = f'{record[3]:15}: {record[4]}'
line4 = f'{record[5]:15}: {record[6]}小时 {record[7]}分钟 {record[8]}秒'
line5 = f'{record[9]:15}: {record[10]}'
line6 = f'{record[11]:15}: {record[12]}'

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)