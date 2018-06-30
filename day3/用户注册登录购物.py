#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

login_status = False


def register():
    '''
    用户注册
    :return:
    '''
    username = input('用户名：')
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
                username = input('用户名：')
                error_count += 1
    f.close()
    if error_count == 3:
        print('\033[32;0m用户名三次输入错误，注册失败\033[0m'.center(90, '-'))
        return
    password = input('密码：')
    twice = input('请再次输入密码：')

    for i in range(0, 2):
        if twice == password:
            with open(file='UserAccount', encoding='utf-8', mode='w') as f:
                account[username] = password
                f.write(json.dumps(account))
            f.close()
            print('\033[32;0m%s 恭喜您，注册成功\033[0m'.center(90, '-') % username)
            return
        else:
            print('\033[32;0m两次密码不一致，请再次输入密码：\033[0m'.center(90, '-'))
            password = input('密码：')
            twice = input('请再次输入密码：')

    print('\033[32;0m密码三次输入错误，用户注册失败\033[0m'.center(90, '-'))


def login():
    '''
    用户登录
    :return:
    '''
    username = input('用户名：')
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
    count = 0
    for i in range(0, 3):
        if count != 0:
            password = input('密码：')
        if password == account[username]:
            print('\033[32;0m登录成功\033[0m'.center(90, '-'))
            global login_status
            login_status = True
            return
        else:
            count += 1
            if count == 3:
                print('\033[32;0m三次输入错误，登录失败\033[0m'.center(90, '-'))
                return
            else:
                print('\033[32;0m密码输入错误，请重新输入\033[0m'.center(90, '-'))


def shop():
    '''
    购物车
    :return:
    '''
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998}
    ]

    product_index = {}
    owner = {}
    money = input('请输入您的总资产：')

    count = 0
    for i in range(0, 3):
        if count != 0:
            money = input('请输入您的总资产：')
        if not money.isdigit():
            print('\033[32;0m输入错误，请重新输入正确的数字\033[0m'.center(90, '-'))
            count += 1

    if count == 3:
        print('\033[32;0m三次输入资产错误，购物失败\033[0m'.center(90, '-'))
        return

    money = int(money)
    while True:
        for index in range(len(goods)):
            product_index[index + 1] = [goods[index]['name'], goods[index]['price']]
            print('\033[32;0m%s.商品：%s 价格：%s\033[0m' % (index + 1, goods[index]['name'], goods[index]['price']))
        num = input('请输入您想购买的商品序号：')
        if num.isdigit():
            num = int(num)
            if num in product_index.keys():
                product = product_index[num][0]
                price = product_index[num][1]
                if price < money:
                    money -= int(price)
                    owner[product] = int(owner.get(product, 0)) + 1
                    print('\033[32;0m恭喜您购买[%s]成功，您当前的余额为%s, 您是否继续购买，确认请输入yes，否则输入quit退出购物车\033[0m'.center(90, '-') % (product, money))
                    choice = input('>>>')
                    if choice == 'yes':
                        pass
                    elif choice == 'quit':
                        print('\033[32;0m您的商品清单：\033[0m'.center(90, '-'))
                        for k, v in owner.items():
                            print('\033[32;0m%s %s件\033[0m' % (k, v))
                        print('\033[32;0m购买结束，感谢您的光临\033[0m'.center(90, '-'))
                        break
                    else:
                        print('\033[32;0m请输入正确yes or quit\033[0m'.center(90, '-'))
                else:
                    print('\033[32;0m您的余额不足以购买该商品，请确认是否充值\n充值请输入yes,否则输入no\033[0m'.center(90, '-'))
                    choice = input('>>>')
                    if choice == 'yes':
                        recharge = input('\033[32;0m请输入您需要充值的金额：\033[0m')
                        if recharge.isdigit():
                            money += int(recharge)
                            print('\033[32;0m充值成功，您当前的余额为%s\033[0m'.center(90, '-') % money)
                        else:
                            print('\033[32;0m输入类型错误，请输入正确的数字\033[0m'.center(90, '-'))
                    else:
                        print('\033[32;0m您的商品清单：\033[0m'.center(90, '-'))
                        for k, v in owner.items():
                            print('\033[32;0m%s %s件\033[0m' % (k, v))
                        print('\033[32;0m购买结束，感谢您的光临\033[0m'.center(90, '-'))
                        break
            else:
                print('\033[32;0m输入错误，请选择列表中存在的商品序号：\033[0m'.center(90, '-'))
        else:
            print('\033[32;0m输入类型错误，请输入正确的数字\033[0m'.center(90, '-'))

    goods_dict = {}
    for i in goods:
        goods_dict[i['name']] = i['price']
    with open(file='product_list', encoding='utf-8', mode='w') as f:
        for k, v in owner.items():
            f.write('商品：[%s] 数量：[%s] 单价：[%s]\n' % (k, v, goods_dict[k]))
    f.close()


def menu():
    '''
    运行菜单
    :return:
    '''
    if not os.path.exists('UserAccount'):
        f = open(file='UserAccount', encoding='utf-8', mode='w')
        f.close()
    while True:
        print('1，注册\n2，登录\n3，购物车\n4，退出')
        choice = input('请输入序号，选择对应的操作：')
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            if login_status:
                shop()
            else:
                print('\033[32;0m请先登录再购物\033[0m'.center(90, '-'))
        elif choice == '4':
            break
        else:
            print('\033[32;0m请输入正确的序号{1, 2, 3}\033[0m'.center(90, '-'))


menu()
