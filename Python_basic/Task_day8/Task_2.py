list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print('方案一：')

for item1 in list1:
    for item2 in list2:
        if item2 == item1:
            print(str(item1) + ' only in list1 and list2')

print('方案二：')
