#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 11:51 PM
# @Author  : lichenxiao
# @File    : 24_post_order_BS_tree.py


def check_if_post_order_of_BStree(a, start, end):
    if start >= end:
        return True
    i = start
    root = a[end]
    while a[i] <= root:
        i += 1
    for index in range(i, end):
        if a[index] < root:
            return False
    return check_if_post_order_of_BStree(a, start, i - 1) & check_if_post_order_of_BStree(a, i, end - 1)


if __name__ == '__main__':
    a = [5, 7, 6, 9, 11, 10, 8]
    a = [7, 4, 6, 5]
    print check_if_post_order_of_BStree(a, 0, len(a) - 1)
