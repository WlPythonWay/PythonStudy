#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import os
import re
import sys
import time
import random

# 常用模块
# collections 扩展的几个数据类型
# namedtuple 命名元组
# point = collections.namedtuple('point', ['x', 'y'])
# p = point(1, 2)
# print(p.x)
# print(p.y)

# deque 双端队列

# OrderedDict 有序字典

# defaultdict 默认字典
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# d = collections.defaultdict(list)
# for i in l:
#     if i > 5:
#         d['k1'].append(i)
#     else:
#         d['k2'].append(i)
#
# print(d)


# time 时间模块
# 时间的几种格式
# print(time.time())    时间戳(给计算机用的) float
# print(time.strftime('%Y-%m-%d-%H-%M-%S'))    格式化时间 年月日时分秒 str
# print(time.localtime())

# random 随机
# def verification_code():
#     l = []
#     for i in range(10):
#         l.append(i)
#
#     for i in range(65, 91):
#         l.append(chr(i))
#
#     for i in range(97, 123):
#         l.append(chr(i))
#
#     result = random.sample(l, 6)
#     print(''.join(result))
#
#
# verification_code()

# def verification_code():
#     code = ''
#     for i in range(6):
#         num = random.randint(0, 9)
#         x = chr(random.randint(65, 90))
#         y = chr(random.randint(97, 122))
#         r = random.choice([x, y, num])
#
#         code += str(r)
#     print(code)
#
#
# verification_code()
# sys 和python解释器相关的
# print('3.6' in sys.version) 系统版本
# print(sys.modules) 已导入的模块，包括内置
# print(sys.argv) 打印脚本后接的所有参数，返回列表  (可用于登录)
    # if len(sys.argv) > 1 and sys.argv[1] == 'wanliang' and sys.argv[2] == '123456':
    #     print('登录成功')
    # else:
    #     print('Usage：python file username password')

# os 和操作系统相关的
# print(os.getcwd()) 获取当前工作目录，执行代码的时候所在的目录
# os.chdir('d:') 切换目录
# print(__file__) 获取当前文件所在的绝对路径
    # os.chdir(os.path.dirname(__file__))   获取当前文件的所在目录
    # print(os.getcwd())
# os.rmdir() 删除一层空目录
# os.removedirs() 递归删除空目录
# print(os.stat(__file__)) 打印当前文件属性
# print(os.path.abspath(__file__)) 返回规范化的绝对路径
# print(os.path.join(os.path.dirname(__file__), os.path.basename(__file__))) 帮助你拼接路径
x = 'wawnwl'
r = re.findall('w.', x)
print(r)

