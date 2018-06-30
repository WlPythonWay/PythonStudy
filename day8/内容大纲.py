#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

# 常用模块

point = collections.namedtuple('point', ['x', 'y'])
p = point(1, 2)
print(p.x)
print(p.y)
