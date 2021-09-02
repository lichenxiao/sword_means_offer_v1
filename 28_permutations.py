#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 28_permutations.py
# @time: 2021/4/13 4:27 下午
# @desc: 排列组合，元素不重复
import copy

def origin():
    """
    python的自带函数，实现排列组合
    """
    from itertools import combinations, permutations
    # 排列
    test_data = ('1', '2', '3')
    print('排列有：')
    for i, j in permutations(test_data, 2): print(i, j)

    # 组合
    print('组合有：')
    for i, j in combinations(test_data, 2): print(i, j)


def permutations(l):
    def _permutations(l, start):
        """
        排列
        """
        if start == len(l):
            print(''.join(l))
            return
        # 第一个元素与后面的依次交换，然后保持第一个不变，将后面的字符串看做整体，递归以上步骤
        for i in range(start, len(l)):
            l[start], l[i] = l[i], l[start]
            _permutations(l, start + 1)
            l[start], l[i] = l[i], l[start]
    if not l:
        return ''
    _permutations(l, 0)


def permutations2(s):
    str_set = []
    ret = []  # 最后的结果

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()

    permutation(s)
    return ret


def combination(l, m):
    """
    从l里选出m个元素
    """
    if not l:
        return False
    if m > len(l):
        return False
    choise_list = []

    def _combination(l, m, start, choise_list):
        """
        组合，这个写的不对
        """
        # 每个元素有两种选择,选与不选，然后通过之前的选择情况，决定后续的元素的选择情况
        if len(choise_list) == m:
            print(''.join(choise_list))
            return

        for i in range(start, len(l)):
            choise_list.append(l[i])
            start += 1
            _combination(l, m, start, choise_list)
            choise_list.pop()

            _combination(l, m, start, choise_list)

    _combination(l, m, 0, choise_list)


if __name__ == '__main__':
    # origin()
    # permutations(['1', '2', '4'])
    # print my_permutation('123')
    combination(['a', 'b', 'c', 'd'], 2)
