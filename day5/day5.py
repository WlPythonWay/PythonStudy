#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1 构建列表： 十以内的所有的元素的平方。
# print([i**2 for i in range(11)])

# 2, 30以内所有能被3整除的数的平方
# print([i**2 for i in range(1, 31) if i % 3 == 0])

# 3，[3,6,9] 组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# print([[n for n in range(i+1)][-3:] for i in [3, 6, 9]])

# 4,
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# x = [[n for n in i if n.count('e') == 2] for i in names]
# print(x)
# l = ['您好', '3.64',
# '请问您是刘晓宇同学的家长吗', '6.25',
# '是的有什么事情吗', '6.15',
# '您好我是学大教育的刘老师', '5.06',
# '这次给给您打电话主要是想了解一下孩子上学期的协议情况', '5.86',
# '针对于上学期的学习状况', '5.37',
# '我们学校邀请您和孩子周末过来听一下针对性的辅导课好吧好吧', '5.36',
# '可以我想问一下都有什么课程呢', '5.65',
# '呃主要是有英语和语文', '4.35',
#  '你看', '3.77',
#  '到时候咱们再联系好吧', '6.10',
#  '好的', '6.45',
#  '恩再见', '4.84']

# x = [[n for n in i] for i in names]

# 上面这个列表帮我转成下面这种格式
# [{"onebest":"您好", "speed":"6.060606"},
# {"onebest":"我这是中国电信的客户代表请问您是幺五幺幺零幺五六六六幺号码的长期使用者吗", "speed":"5.479452"},
# {"onebest":"是的", "speed":"5.405406"},
# {"onebest":"为啥谢谢您长期以来的支持",  "speed":"5.529954"},
# {"onebest":"交银退掉", "speed":"4.938272"},
# {"onebest":"考虑了解生活小贴士服务美元四月","speed":"4.672897"},
# {"onebest":"你们可以收到天气情况活动", "speed":"5.529954"},
# {"onebest":"我建议", "speed":"4.347826"},
# {"onebest":"生活中了就是周转现在开通后","speed":"4.024768"},
# {"onebest":"发到您的", "speed":"8.510638"},
# {"onebest":"都会","speed":"4.255319"},
# {"onebest":"现在","speed":"6.451613"},
# {"onebest":"可以享有就是看吗", "speed":"5.161290"},
# {"onebest":"可以","speed":"6.451613"},
# {"onebest":"改天先生那是的",  "speed":"4.046243"},
# {"onebest":"另外再见",  "speed":"5.479452"}
# ]


x = {
    'name': 'alex',
    'Values': [{'timestamp': 1517991992.94,
                'values': 100, },
               {'timestamp': 1517992000.94,
                'values': 200, },
               {'timestamp': 1517992014.94,
                'values': 300, },
               {'timestamp': 1517992744.94,
                'values': 350},
               {'timestamp': 1517992800.94,
                'values': 280}
               ], }
# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
# print([[i['timestamp'], i['values']] for i in x['Values']])


"""
# 内置函数
1、作用域相关
    globals()
    locals()

2、其他相关
    eval()  执行字符串中的代码，返回执行结果     ***
    exec()  执行字符串中的代码，不返回执行结果   ***
    print() 打印，sep参数设置分隔符；end参数设置结尾字符，默认为换行；file参数传入文件句柄，写入内容至文件 ***
    hash()  将不可变的数据类型转转为哈希值，数字的哈希值就是数字本身，True的是1，False是0
    id()    内存地址
    help()  查看对象所有信息
    open()  打开文件
    __import__() 函数加载动态类和函数
    callable()  检查对象是否可以调用  **
    dir()       检查对象中的所有方法和属性，并存储在列表中
    range()
    next    __next__

数字相关
    bool()
    int()   转换整数类型，取整 **
    float() 转换为浮点类型     *
    abs()   绝对值
    divmod()    print(divmod(100, 7)) ***
    round()     print(round(3.32434, 3))
    pow()
    sum()       求和
    min()
    max()
    reversed()  翻转
    repr()      原形毕露\r
    sorted()    排序
    map()
    filter()

# 匿名函数
l1 = [
    {'sales_volumn': 0},
    {'sales_volumn': 108},
    {'sales_volumn': 337},
    {'sales_volumn': 475},
    {'sales_volumn': 396},
    {'sales_volumn': 172},
    {'sales_volumn': 9},
    {'sales_volumn': 58},
    {'sales_volumn': 272},
    {'sales_volumn': 456},
    {'sales_volumn': 440},
    {'sales_volumn': 239}
]

print(sorted(l1, key=lambda i: i['sales_volumn']))
"""








