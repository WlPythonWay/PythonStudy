#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Practice(object):
#     """
#     练习一：在终端输出如下信息
#
# 小明，10岁，男，%s上山去砍柴 小明
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
#     """
#     def __init__(self, name):
#         self.name = name
#         self.dict = {'小明': ['10岁', '男'], '老李': ['90岁', '男']}
#
#     def kancai(self):
#         print('%s, %s, %s, 砍柴' % (self.name, self.dict[self.name][0], self.dict[self.name][1]))
#
#     def driver(self):
#         print('%s, %s, %s, 开车' % (self.name, self.dict[self.name][0], self.dict[self.name][1]))
#
#     def baojian(self):
#         print('%s, %s, %s, 保健' % (self.name, self.dict[self.name][0], self.dict[self.name][1]))
#
#
# p1 = Practice('小明')
# p2 = Practice('老李')
#
# p1.kancai()
# p1.driver()
# p1.baojian()
#
# p2.kancai()
# p2.driver()
# p2.baojian()


# class Game_person:
#     def __init__(self,nickname,sex,hp,ad):
#         self.nickname = nickname
#         self.sex = sex
#         self.hp = hp
#         self.ad = ad
#     def attack(self,p):
#         p.hp -= self.ad
#         print('%s攻击了%s,%s还剩%s血量'%(self.nickname,p.nickname,p.nickname,p.hp))
#
#     def weapon_attack(self,武器):
#         self.武器 = 武器 #斧子对象
#
# class Weapon:
#     def __init__(self,name,ad):
#         self.name=name
#         self.ad=ad
#
#     def fight(self,p1,p2):
#         p2.hp -= self.ad
#         print('%s使用%s打了%s%s血,%s还剩%s滴血'\
#               %(p1.nickname,self.name,p2.nickname,self.ad,p2.nickname,p2.hp))
#
# ts = Game_person('泰森','男',200,50)
# barry = Game_person('太白','男',100,10)
# wea = Weapon('斧子',60)
# # wea.fight(barry,ts) 这样写不好，主体应该是人
# # ts.attack(barry)
# # barry.attack(ts)
# barry.weapon_attack(wea)
# # barry对象调用weapon_attack方法，
# # 方法执行的是将斧子对象wea封装到barry对象的属性中、
# # barry.武器 相当于 wea
# barry.武器.fight(barry,ts)


# class GamePerson(object):
#     """
#     游戏人物
#     """
#
#     def __init__(self, name, hp, ad):
#         """
#         初始化
#         """
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#
#     def attack(self, p):
#         p.hp = p.hp - self.ad
#         print('%s打了%s一拳,%s还剩%s血量' % (self.name, p.name, p.name, p.hp))
#
#     def weapon_attack(self, w, p):
#         w.flight(self, p)
#
#
# class Weapon(object):
#     """
#     武器
#     """
#
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#
#     def flight(self, p1, p2):
#         p2.hp = p2.hp - self.ad
#         print('%s用%s打了%s一%s，%s还剩%s血量'
#               % (p1.name, self.name, p2.name, self.name, p2.name, p2.hp))
#
#
# ts = GamePerson('泰森', 200, 50)
# tb = GamePerson('太白', 100, 10)
# w = Weapon('斧子', 60)
#
# ts.weapon_attack(w, tb)
# tb.attack(ts)
# tb.weapon_attack(w, ts)
# tb.weapon_attack(w, ts)
# tb.weapon_attack(w, ts)

# class Animal(object):
#
#     def eat(self):
#         print('eat')
#
#     def drink(self):
#         print('eat')
#
#     def la(self):
#         print('eat')
#
#     def sa(self):
#         print('eat')
#
#
# class Cat(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass
#
#
# cat = Cat()
# cat.eat()

# '''
# 1,alex,22,13651054608,IT
# 2,wusir,23,13304320533,Tearcher
# 3,taibai,18,1333235322,IT
#
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},......]'''
#
#
# list_obj = []
# with open('filename.txt') as f:
#     for i in f:
#         dict_obj = {}
#         line = i.strip().split(',')
#         id = line[0]
#         name = line[1]
#         age = line[2]
#         phone = line[3]
#         job = line[4]
#
#         dict_obj['id'] = id
#         dict_obj['name'] = name
#         dict_obj['age'] = age
#         dict_obj['phone'] = phone
#         dict_obj['job'] = job
#
#         list_obj.append(dict_obj)
#
# print(list_obj)

