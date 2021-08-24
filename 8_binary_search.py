#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 8_binary_search.py
# @time: 2021/4/8 12:37 上午
# @desc: 旋转数组 中的 最小的数字

"""
1234567
4567123
7123456
"""


def order(l, start, end):
    min_n = l[start]
    for i in range(start + 1, end):
        if l[i] < min_n:
            min_n = l[i]
    return min_n


def _min(l, start, end):
    if start + 1 == end:
        return l[end]
    mid = (start + end) / 2
    if l[mid] == l[start] and l[mid] == l[end]:
        return order(l, start, end)
    if l[mid] < l[end]:
        return _min(l, start, mid)
    elif l[mid] > l[start]:
        return _min(l, mid, end)


def min(l):
    i = 0
    j = len(l) - 1
    return _min(l, i, j)


print min([4, 5, 6, 7, 8, 2, 3])
print min([1, 0, 1, 1, 1])
