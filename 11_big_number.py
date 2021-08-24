#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 11_big_number.py
# @time: 2021/4/8 11:25 上午
# @desc: 实现幂函数
# 需要考虑：1、底数是否为0，底数为0时指数分别为整数和负数
# 2、其他情况下，指数是否为负数


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    比较两个浮点数是否相等
    :param a:are the two values to be tested to relative closeness
    :param b:are the two values to be tested to relative closeness
    :param rel_tol: is the relative tolerance -- it is the amount of error allowed, relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, pass tol=0.05. The default tolerance is 1e-9, which assures that the two values are the same within about 9 decimal digits. rel_tol must be greater than 0.0
    :param abs_tol:is a minimum absolute tolerance level -- useful for comparisons near zero.
    :return:

    python3
    import math
    math.isclose(a, b, abs_tol=0.00003)
    """
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def power_with_unsigned_exponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    res = power_with_unsigned_exponent(base, exponent >> 1)
    res *= res
    if exponent & 0x1 == 1:
        res *= base
    return res


def power(base, exponent):
    flag = False
    if isclose(base, 0):
        if exponent >= 0:
            return 1
        else:
            return False
    if exponent <= 0:
        flag = True
        exponent *= -1
    res = power_with_unsigned_exponent(base, exponent)
    if flag:
        return float(1)/res
    return res


if __name__ == '__main__':
    print power(3, 3)
    print power(1.1, -2)
    print power(0, -1)
    print power(0, 4)
    print power(4, -2)
