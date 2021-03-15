import os
import re

os.chdir('test')
file_dir_list = os.listdir(os.getcwd())

print('文件中包含“qytang”关键字的文件为：')
print('方案一：')

for file_or_dir in file_dir_list:
    if os.path.isfile(file_or_dir):
        test_file = open(file_or_dir)
        for lines in test_file.readlines():
            if re.findall('qytang', lines):
                print(file_or_dir)
                break

print("方案二：")

# topdown --可选，为True,则优先遍历top目录，否则优先遍历top的子目录(默认为开启)。如果topdown参数为 True，walk会遍历top文件夹，与top文件夹中每一个子目录。
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
        if name != '':
            test_file1 = open(name)
            for lines in test_file1.readlines():
                if re.findall('qytang', lines):
                    print(name)
                    break

# 清理创建测试文件的
os.chdir('..')

for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('test')
