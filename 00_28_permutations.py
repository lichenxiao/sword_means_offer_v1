#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 28_permutations.py
# @time: 2021/4/13 4:27 下午
# @desc: 排列组合，元素不重复


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


def permutations(l):
    if not l:
        return ''
    _permutations(l, 0)


def my_permutation(s):
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


def _combination(l, m, start, choise_set):
    """
    组合
    """
    # 每个元素有两种选择,选与不选，然后通过之前的选择情况，决定后续的元素的选择情况
    if m == 0:
        print(''.join(choise_set))
        return

    for i in range(start, len(l)):
        choise_set.append(l[start])
        _combination(l, m-1, start + 1, choise_set)

        choise_set.remove(l[start])
        _combination(l, m, start + 1, choise_set)


def combination(l, m):
    if not l:
        return False
    if m > l:
        return False
    choise_set = []
    _combination(l, m, 0, choise_set)





if __name__ == '__main__':
    permutations(['1', '2', '4', '3'])
    #combination(['1', '2', '3', '4'], 2)
    #print my_permutation('1234')