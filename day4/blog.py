#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import time

status_dict = {'login': ''}


def register():
    """
    用户注册
    :return:
    """
    username = input('用户名：').strip()
    if not username:
        print('\033[32;0m用户不能为空\033[0m'.center(90, '-'))
        return
    with open(file='UserAccount', encoding='utf-8', mode='r') as f:
        account = f.read()
        if account == '':
            account = {}
        else:
            account = json.loads(account)
        error_count = 1
        for i in range(0, 2):
            if username in account:
                print('\033[32;0m用户名已注册，请输入新的用户名\033[0m'.center(90, '-'))
                username = input('用户名：').strip()
                username = input('用户名：').strip()
                if not username:
                    print('\033[32;0m用户不能为空\033[0m'.center(90, '-'))
                    return
                error_count += 1
    f.close()
    if error_count == 3:
        print('\033[32;0m用户名三次输入错误，注册失败\033[0m'.center(90, '-'))
        return
    password = input('密码：').strip()
    if not password:
        print('\033[32;0m密码不能为空\033[0m'.center(90, '-'))
        return
    twice = input('请再次输入密码：').strip()

    for i in range(0, 2):
        if twice == password:
            with open(file='UserAccount', encoding='utf-8', mode='w') as f:
                account[username] = password
                f.write(json.dumps(account))
            f.close()
            print('\033[32;0m%s 恭喜您，注册成功\033[0m'.center(90, '-') % username)
            print('\033[32;0m登录成功\033[0m'.center(90, '-'))
            status_dict['login'] = username
            return
        else:
            print('\033[32;0m两次密码不一致，请再次输入密码：\033[0m'.center(90, '-'))
            password = input('密码：').strip()
            if not password:
                print('\033[32;0m密码不能为空\033[0m'.center(90, '-'))
                return
            twice = input('请再次输入密码：').strip()

    print('\033[32;0m密码三次输入错误，用户注册失败\033[0m'.center(90, '-'))


def login():
    """
    用户登录
    :return:
    """
    username = input('用户名：')
    username = input('用户名：').strip()
    if not username:
        print('\033[32;0m用户不能为空\033[0m'.center(90, '-'))
        return
    with open(file='UserAccount', encoding='utf-8', mode='r') as f:
        account = f.read()
        if account == '':
            account = {}
        else:
            account = json.loads(account)

    if username not in account:
        print('\033[32;0m用户名不存在，请先注册\033[0m'.center(90, '-'))
        return

    password = input('密码：')
    if not password:
        print('\033[32;0m密码不能为空\033[0m'.center(90, '-'))
        return
    count = 0
    for i in range(0, 3):
        if count != 0:
            password = input('密码：')
            if not password:
                print('\033[32;0m密码不能为空\033[0m'.center(90, '-'))
                return
        if password == account[username]:
            print('\033[32;0m登录成功\033[0m'.center(90, '-'))
            status_dict['login'] = username
            return
        else:
            count += 1
            if count == 3:
                print('\033[32;0m三次输入错误，登录失败\033[0m'.center(90, '-'))
                return
            else:
                print('\033[32;0m密码输入错误，请重新输入\033[0m'.center(90, '-'))


def log(func):
    """
    保存日志装饰器
    :param func: 函数对象
    :return: 新函数对象
    """""

    def inner():
        if choice.strip() not in choice_list:
            print('\033[32;0m请输入正确选项\033[0m'.center(90, '-'))
            return

        func()

        if status_dict['login']:
            user = status_dict['login']
        else:
            user = 'guest'

        with open(file='blog.log', encoding='utf-8', mode='a') as log_file:
            log_file.write('[%s] %s用户访问%s\n'
                           % (time.strftime('%Y-%m-%d'), user, str(choice_list[choice.strip()].__name__)))

    return inner


def article():
    """
    文章页面
    :return:
    """
    print('\033[32;0m欢迎%s访问文章页面\033[0m'.center(90, '-') % status_dict['login'])


def diary():
    """
    日记页面
    :return:
    """
    print('\033[32;0m欢迎%s访问日记页面\033[0m'.center(90, '-') % status_dict['login'])


def comment():
    """
    评论页面
    :return:
    """
    print('\033[32;0m欢迎%s访问评论页面\033[0m'.center(90, '-') % status_dict['login'])


def collection():
    """
    收藏页面
    :return:
    """
    print('\033[32;0m欢迎%s访问收藏页面\033[0m'.center(90, '-') % status_dict['login'])


def cancellation():
    if status_dict['login']:
        status_dict['login'] = ''
        print('\033[32;0m用户已注销\033[0m'.center(90, '-'))
    else:
        print('\033[32;0m用户未登录，无法注销\033[0m'.center(90, '-'))


choice_list = {'1': register, '2': login, '3': article,
               '4': diary, '5': comment, '6': collection,
               '7': cancellation
               }

if not os.path.exists('UserAccount'):
    f = open(file='UserAccount', encoding='utf-8', mode='w')
    f.close()


@log
def menu():
    if choice in choice_list:
        if choice in ['1', '2', '7']:
            choice_list[choice.strip()]()
        else:
            if status_dict['login']:
                choice_list[choice.strip()]()
            else:
                print('\033[32;0m请登录后再访问\033[0m'.center(90, '-'))

    else:
        print('\033[32;0m请输入正确选项\033[0m'.center(90, '-'))


while True:
    print('''
    欢迎来到博客园首页
    1、注册
    2、登录
    3、文章页面
    4、日记页面
    5、评论页面
    6、收藏页面
    7、注销
    8、退出程序''')

    choice = input('请输入选项：').strip()
    if choice == '8':
        break

    menu()
