import os
import sys
msg = """
    1:查询
    2:添加
    3:删除
    4:修改
    5:退出
    """
msg_dict = {1: 'fetch', 2: 'add', 3: 'remove', 4: 'change', 5: 'exit'}
while True:
    print(msg)
    choice = input("输入序号>>:")
    if len(choice) == 0 or choice not in msg_dict:
        continue
    elif choice == 5:
        exit(5)
    else:
        msg_dict[choice]()

# 查询员工信息
def fetch():
    # 查询方式一：select * from staff_table where age >= 22
    # 查询方式二：select * from staff_table where dept = IT
    # 查询方式三：select * from staff_table where enroll_date like "2013"
    data = input('输入您的查询信息：')
    data = data.split(' ')
    con = data[7]
    asp = data[5]
    count = 0
    with open('员工信息.txt', 'r', encoding='utf-8') as f:
        if asp == 'age':
            for line in f:
                if int(line.split(',')[2]) >= int(con):
                    print(line)
                    count += 1
        elif asp == 'dept':
            for line in f:
                if line.split(',')[4] in con:
                    print(line)
                    count += 1
        else:
            for line in f:
                if line.split(',')[5].split('-')[0] in con:
                    print(line)
                    count += 1
        print('查询结束，共查到符合条件的信息 %d 条 ' % count)
# 按要求添加信息
def add():

    # 添加语法： name,age,phone,dept,enroll-date
    data = input('输入您要添加的员工信息：')
    list_data = data.strip().split(',')
    list_all = []
    f = open('员工信息.txt', 'r+')
    for line in f:
        list_all.append(line.strip().split(',')[3])
    if list_data[2] in list_all:
        print("该用户已经存在")
        f.close()
    else:
        for line in f:
            f.write(line)
        staff_id = str(len(list_all)+1)
        list_data.insert(0, str(staff_id))
        f.write('\n')
        f.write("','.join(list_data)")
        f.close()
        print('添加成功')
# 按要求删除信息
def remove():
    # 删除语法：delete from staff_table where staff_id = 12
    staff_id = input("输入您要删除员工的Staff_id:")
    staff_id = staff_id.strip().split(' ')[6]
    f = open('员工信息.txt', 'r')
    f1 = open('新版信息表.txt', 'w')
    for line in f:
        in_list = line.split(',')
        if in_list[0] < staff_id:
            f1.write(line)
        elif in_list[0] > staff_id:
            in_list[0] = str(int(in_list[0])-1)
            f1.write("','.join(in_list)")
        else:
            continue
    f.close()
    f1.close()
    os.remove('员工信息.txt')
    os.rename('新版信息表.txt', '员工信息.txt')
    print('删除成功')
# 按要求修改信息
def change():
    # 修改请输入（注意空格和没有引号）：UPDATE staff_table SET dept = IT where dept = 运维
    data = input("请输入您要修改的信息：")
    old = data.split(' ')[5]
    new = data.split(' ')[9]
    f = open('员工信息.txt', 'r', encoding='utf-8')
    f1 = open('新版信息表.txt', 'w', encoding="utf-8")
    for line in f:
        if old in line:
            line = line.replace(old, new)
        f1.write(line)
    f.close()
    f1.close()
    os.remove('员工信息.txt')
    os.rename('新版信息表.txt', '员工信息.txt')
    print('修改成功')
