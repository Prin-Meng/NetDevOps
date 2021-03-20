import re

str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
record = re.match('^([1-9][0-9]{0,3})\s([0-9a-z]{4}\.[0-9a-z]{4}\.[0-9a-z]{4})\s(DYNAMIC|STATIC)\s([A-Z][\S]+\d)$',
                  str1).groups()

line_tmp = '{0:15}: {1}'
list1 = ['VLAN ID', 'MAC', 'Type', 'Interface']

for i in range(4):
    new_line = line_tmp.format(list1[i], record[i])
    print(new_line)
