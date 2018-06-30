#!/usr/bin/env python
# -*- coding: utf-8 -*-
field_index = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}
field_name = ['id', 'name', 'age', 'phone', 'job']
condition_list = ['>', "<", '=', 'like']

x = 'select * where age>22'
field = x.split('where')[0].split()[1:]
field_list = []
for i in field:
    for n in i.split(','):
        if n:
            field_list.append(n)

condition = x.split('where')[1]

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
                                for f in field_list:
                                    print('%s: [%s]' % (f, l.split()[field_index[f]]))
                    f_read.close()
                elif i == '<':
                    with open('user_list') as f_read:
                        for l in f_read:
                            if 'id' in l:
                                continue
                            v_index = field_index[k]
                            f_v = l.split()[v_index]
                            if f_v < v:
                                for f in field_list:
                                    print('%s: [%s]' % (f, l.split()[field_index[f]]))
                    f_read.close()
                elif i == '=':
                    with open('user_list') as f_read:
                        for l in f_read:
                            if 'id' in l:
                                continue
                            v_index = field_index[k]
                            f_v = l.split()[v_index]
                            if f_v == v:
                                for f in field_list:
                                    print('%s: [%s]' % (f, l.split()[field_index[f]]))
                    f_read.close()
                elif i == 'like':
                    with open('user_list') as f_read:
                        for l in f_read:
                            if 'id' in l:
                                continue
                            v_index = field_index[k]
                            f_v = l.split()[v_index]
                            if v in f_v:
                                for f in field_list:
                                    print('%s: [%s]' % (f, l.split()[field_index[f]]))
                    f_read.close()
                else:
                    print('input error')



# with open('user_list') as f_read:
#     for l in f_read:
#         if 'id' in l:
#             continue
#         age = int(l.split()[2])


