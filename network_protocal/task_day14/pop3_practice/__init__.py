import re

receiver_mail = re.findall('<(.+@.+)>', '<772062725@qq.com>')[0]
print(receiver_mail)