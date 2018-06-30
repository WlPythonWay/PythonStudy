#!/usr/bin/env python
# -*- coding: utf-8 -*-

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

product_index = {}
owner = {}
money = input('请输入您的总资产：')

if money.isdigit():
    money = int(money)
    while True:
        for index in range(len(goods)):
            product_index[index+1] = [goods[index]['name'], goods[index]['price']]
            print('%s.商品：%s 价格：%s' % (index + 1, goods[index]['name'], goods[index]['price']))
        num = input('请输入您想购买的商品序号：')
        if num.isdigit():
            num = int(num)
            if num in product_index.keys():
                product = product_index[num][0]
                price = product_index[num][1]
                if price < money:
                    money -= int(price)
                    owner[product] = int(owner.get(product, 0)) + 1
                    print('恭喜您购买[%s]成功，您当前的余额为%s, 您是否继续购买，确认请输入yes，否则输入quit退出购物车' % (product, money))
                    choice = input('>>>')
                    if choice == 'yes':
                        pass
                    elif choice == 'quit':
                        print('您的商品清单：')
                        for k, v in owner.items():
                            print(k, '%s件' % v)
                        print('购买结束，感谢您的光临')
                        break
                    else:
                        print('请输入正确yes or quit')
                else:
                    print('您的余额不足以购买该商品，请确认是否充值\n充值请输入yes,否则输入no')
                    choice = input('>>>')
                    if choice == 'yes':
                        recharge = input('请输入您需要充值的金额：')
                        if recharge.isdigit():
                            money += int(recharge)
                            print('充值成功，您当前的余额为%s' % money)
                        else:
                            print('输入类型错误，请输入正确的数字'.center(150, '-'))
                    else:
                        print('您的商品清单：')
                        for k, v in owner.items():
                            print(k, '%s件' % v)
                        print('购买结束，感谢您的光临')
                        break
            else:
                print('输入错误，请选择列表中存在的商品序号：'.center(150, '-'))
        else:
            print('输入类型错误，请输入正确的数字'.center(150, '-'))
else:
    print('输入错误，请输入正确的数字'.center(150, '-'))





