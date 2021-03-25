import sqlite3

conn = sqlite3.connect('qytangdb.sqlite')
cursor = conn.cursor()

user_notify = """
请输入查询选项:
输入1 : 查询整个数据库
输入2 : 基于姓名查询
输入3 : 基于年龄查询
输入4 : 基于作业数查询
输入0 : 退出
"""

while True:
    print(user_notify)
    user_input = input('请选择:')
    if user_input == '0':
        print('已退出数据库！')
        break
    elif user_input == '1':
        cursor.execute("select * from qytang_homework_info")
        results = cursor.fetchall()
        for inform in results:
            print('学员姓名:{0:<5}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(inform[0], inform[1], inform[2]))

    elif user_input == '2':
        students_name = input('请输入学员姓名:')
        if not students_name:
            print('姓名不能为空！')
            continue
        cursor.execute("select * from qytang_homework_info where 姓名 = '{0}'".format(students_name))
        results = cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        else:
            for inform in results:
                print('学员姓名:{0:<5}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(inform[0], inform[1], inform[2]))

    elif user_input == '3':
        students_age = input('搜索大于输入年龄的学员，请输入学员年龄:')
        if not students_age.isdigit():
            print('年龄输入错误！')
            continue
        cursor.execute("select * from qytang_homework_info where 年龄 > {0}".format(students_age))
        results = cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        else:
            for inform in results:
                print('学员姓名:{0:<5}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(inform[0], inform[1], inform[2]))

    elif user_input == '4':
        homework_num = input('搜索大于输入作业数的学员，请输入作业数量:')
        if not homework_num.isdigit():
            print('作业数量输入错误！')
            continue
        cursor.execute("select * from qytang_homework_info where 作业数 > {0}".format(homework_num))
        results = cursor.fetchall()
        if not results:
            print('学员信息未找到！')
        else:
            for inform in results:
                print('学员姓名:{0:<5}  学员年龄:{1:<3}  学员作业数:{2:<3}'.format(inform[0], inform[1], inform[2]))

    else:
        print('输入错误！请重试！')
