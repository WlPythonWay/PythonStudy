#!/usr/bin/env python
# -*- coding: utf-8 -*-

count = 1

while count < 101:
    result = count % 2
    if not result:
        print(count)
    count += 1
