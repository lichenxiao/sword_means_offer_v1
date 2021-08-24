#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 14_move_odd_pre.py
# @time: 2021/5/10 4:35 下午
# @desc:调整数组顺序，使奇数位于偶数前面

def is_odd(n):
    return n & 1


def reorder(l, f):
    if not l:
        return
    i = 0
    j = len(l) - 1
    while i < j:
        while i < j and f(l[i]):  # i<j 这个条件别忘掉
            i += 1
        while i < j and not f(l[j]):
            j -= 1
        l[i], l[j] = l[j], l[i]


l = [5, 6, 3, 78, 1]
reorder(l=l, f=is_odd)
print l
