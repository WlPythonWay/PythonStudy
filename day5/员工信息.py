#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

field_index = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}
field_name = ['id', 'name', 'age', 'phone', 'job']
condition_list = ['>', "<", '=', 'like']


def get_id():
    with open(file='user_list', encoding='utf-8', mode='r') as f:
        line = f.readlines()[-1]
        uid = line.split()[0]
        if uid == 'id':
            uid = 1
        else:
            uid = int(uid) + 1
        return uid


def insert():
    uid = get_id()
    name = input('请输入员工姓名: ').strip()
    age = input('请输入员工年龄: ').strip()
    if not age.isdigit():
        print('年龄必须是数字')
        return
    phone = input('请输入员工电话: ').strip()
    if not phone.isdigit():
        print('电话必须是数字')
        return
    job = input('请输入员工职位: ').strip()
    with open(file='user_list', encoding='utf-8', mode='a') as f:
        f.write('%s    %s    %s    %s    %s\n' % (uid, name, age, phone, job))
    f.close()


def select():
    global info
    info = []
    sql = input('请输入查询语句：')
    if 'select' not in sql or 'where' not in sql:
        print('语法错误')
        return
    field = sql.split('where')[0].split()[1:]
    field_list = []
    for i in field:
        if i == '*':
            field_list = field_name
            break
        for n in i.split(','):
            if n:
                field_list.append(n)

    condition = sql.split('where')[1]

    for i in condition_list:
        if i in condition:
            k = condition.split(i)[0].strip()
            v = condition.split(i)[1].strip()

            for n in field_name:
                if n == k:
                    if i == '>':
                        with open('user_list') as f_read:
                            for l in f_read:
                                if 'id' in l:
                                    continue
                                v_index = field_index[k]
                                f_v = l.split()[v_index]
                                if f_v > v:
                                    info.clear()
                                    for f in field_list:
                                        info.append('%s: [%s]' % (f, l.split()[field_index[f]]))
                                    print(info)
                        f_read.close()
                    elif i == '<':
                        with open('user_list') as f_read:
                            for l in f_read:
                                if 'id' in l:
                                    continue
                                v_index = field_index[k]
                                f_v = l.split()[v_index]
                                if f_v < v:
                                    info.clear()
                                    for f in field_list:
                                        info.append('%s: [%s]' % (f, l.split()[field_index[f]]))
                                    print(info)
                        f_read.close()
                    elif i == '=':
                        with open('user_list') as f_read:
                            for l in f_read:
                                if 'id' in l:
                                    continue
                                v_index = field_index[k]
                                f_v = l.split()[v_index]
                                if f_v == v:
                                    info.clear()
                                    for f in field_list:
                                        info.append('%s: [%s]' % (f, l.split()[field_index[f]]))
                                    print(info)
                        f_read.close()
                    elif i == 'like':
                        with open('user_list') as f_read:
                            for l in f_read:
                                if 'id' in l:
                                    continue
                                v_index = field_index[k]
                                f_v = l.split()[v_index]
                                if v in f_v:
                                    info.clear()
                                    for f in field_list:
                                        info.append('%s: [%s]' % (f, l.split()[field_index[f]]))
                                    print(info)
                        f_read.close()
                    else:
                        print('语法错误')
                        return


def update():
    pass


def delete():
    flag = True
    uid = input('请输入需要删除的员工id: ')
    f_read = open('user_list')
    f_write = open('user_list_swap', 'w')
    for i in f_read:
        if uid == i.split()[0]:
            flag = False
            continue
        f_write.write(i)

    f_write.close()
    f_read.close()
    if flag:
        print('该用户id不存在')
        return
    os.remove('user_list')
    os.rename('user_list_swap.', 'user_list')


func_list = {'1': insert, '2': select, '3': delete, '4': update}

if not os.path.exists('user_list'):
    f = open(file='user_list', encoding='utf-8', mode='w')
    f.write('id    name    age    phone    job\n')
    f.close()

while True:
    print('''
    1、插入员工信息
    2、查询员工信息
    3、删除员工信息
    4、修改员工信息
    5、退出
    ''')
    choice = input('>>>').strip()
    if choice == '5':
        break

    if choice in func_list:
        func_list[choice]()
    else:
        print('请输入正确的选项')
