#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 8_binary.py
# @time: 2021/4/7 11:59 下午
# @desc: 二进制中1的个数


def number_of_1(data):
    count = 0
    flag = 1
    if data < 0:
        data = data & 0xffffffff  # 这个是python里面的，python和别的语言存储负数的格式有点区别
    while data:
        if data & flag:
            count += 1
            data = data ^ flag
        flag = flag << 1
    return count


def number_of_1_other(data):
    """
    一个整数减去1以后再与原来的整数做与运算，会把这个整数的二进制表示中最右边的一个1变成0
    :param data:
    :return:
    """
    if data < 0:
        data = data & 0xffffffff  # 这个是python里面的，python和别的语言存储负数的格式有点区别
    count = 0
    while data:
        count += 1
        data = data & (data - 1)
    return count


if __name__ == '__main__':
    print number_of_1(5)
    print number_of_1(11)
    print number_of_1_other(11)
    print number_of_1_other(3)
    print number_of_1_other(-3)
