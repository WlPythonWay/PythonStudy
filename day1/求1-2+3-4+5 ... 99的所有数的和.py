#!/usr/bin/env python
# -*- coding: utf-8 -*-

end = 0
count = 1
while count < 101:
    result = count % 2
    if result:      # 奇数
        end += count
    else:           # 偶数
        end -= count
    count += 1

print(end)
