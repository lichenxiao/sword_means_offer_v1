#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 4_replace_space.py
# @time: 2021/4/8 12:38 上午
# @desc: 将空格替换为%20，需要的O(n)时间复杂度
# 先遍历一遍字符串，将空格的数目算出来，再从后向前拷贝
# 用Python写的很别扭

def replace_space(origin_l, origin_len=7):
    space_count = 0
    for i in origin_l:
        if i == ' ':
            space_count += 1
    new_len = origin_len + 2 * space_count
    j = new_len-1
    for i in range(origin_len - 1, -1, -1):
        if origin_l[i] != ' ':
            origin_l[j] = origin_l[i]
            j -= 1
        else:
            origin_l[j] = '0'
            j -= 1
            origin_l[j] = '2'
            j -= 1
            origin_l[j] = '%'
            j -= 1
    return origin_l


res = list('123 4 5') + ['*'] * 10
print(replace_space(res))
