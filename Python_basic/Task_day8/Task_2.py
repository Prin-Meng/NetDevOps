list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

print('方案一：')

for item1 in list1:
    if item1 in list2:
        print(str(item1) + ' in List1 and List2')
    else:
        print(str(item1) + ' only in List1')

print('\n方案二：')


def find_same(l1, l2):
    for item1 in list1:
        if item1 in list2:
            print(str(item1) + ' in List1 and List2')
        else:
            print(str(item1) + ' only in List1')


if __name__ == '__main__':
    find_same(list1, list2)
