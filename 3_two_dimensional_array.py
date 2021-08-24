#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 3_two_dimensional_array.py
# @time: 2021/4/6 11:32 下午
# @desc: 二维数组，每行从左到右增大，从上到下增大，判断二维数组中是否含有某数字


def index(t_d_a, row, col, data):
    if not t_d_a:
        return -1, -1
    index_x = row - 1
    index_y = 0
    while index_x >= 0 and index_y <= col - 1:
        if data == t_d_a[index_x][index_y]:
            return index_x, index_y
        elif data > t_d_a[index_x][index_y]:
            index_y += 1
        else:
            index_x -= 1
    return -1, -1


t_d_a = [
    [1, 2, 5, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15]
]

print index(t_d_a, 4, 4, 7)
