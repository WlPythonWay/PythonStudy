#!/usr/bin/env python
# -*- coding: utf-8 -*-

user_list = [
    {'username': 'alex', 'password': '123456'},
    {'username': 'eric', 'password': '112233'},
    {'username': 'tom', 'password': '113344'},
    {'username': 'jack', 'password': '332244'}
]

count = 0

while count < 3:
    flag = False
    username = input('please input username: ')
    password = input('please input password: ')
    for user_info in user_list:
        if username == user_info['username'] and password == user_info['password']:
            print('Login Success')
            flag = True
            break
    if not flag and count == 2:
        print('Exceed the number of login')
    elif not flag:
        print('Login Fail,Please Retry')
    else:
        break
    count += 1

