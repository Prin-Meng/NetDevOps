import sqlite3

# Python字典对象，我们将把它写入SQLite数据库
homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

# 连接SQlite数据库
conn = sqlite3.connect('qytangdb.sqlite')
cursor = conn.cursor()

# 执行创建表的任务
cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int ,作业数 int)")

# 读取Python字典数据，并逐条写入SQLite数据库
for student in homework_dict:
    name = student['姓名']
    age = student['年龄']
    homework = student['作业数']
    cursor.execute(f"insert into qytang_homework_info(姓名,年龄,作业数) values( '{name}',{age},{homework})")

conn.commit()
