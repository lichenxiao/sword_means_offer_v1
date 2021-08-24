#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 9_fibonacci.py
# @time: 2021/4/8 12:30 上午
# @desc:


def fibonacci(n):
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0, f1 = 0, 1
    for i in range(2, n + 1):
        f2 = f0 + f1
        f0, f1 = f1, f2
    return f2


print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
