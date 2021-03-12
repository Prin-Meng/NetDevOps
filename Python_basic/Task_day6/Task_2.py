import re

port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34',
             'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

port_num_list = []
final_list = []

for port_num in port_list:
    result = re.findall('(\d)/(\d\d\d)/(\d)/(\d+)', port_num)[0]
    port_num_list.append([int(result[2]), int(result[3])])

port_list_sorted = sorted(port_num_list, key=lambda x: (x[0], x[1]))

for list_num in port_list_sorted:
    L = [str(list_num[0]), str(list_num[1])]
    str1 = '/'.join(L)
    str2 = 'eth 1/101/' + str1
    final_list.append(str2)

print(final_list)
