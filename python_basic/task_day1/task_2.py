import random

i = 1
ip = []

while i <= 4:
    section = random.randint(0, 255)
    ip.append(section)
    i += 1

print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]))