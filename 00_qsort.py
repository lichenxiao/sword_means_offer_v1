#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/17 2:04 PM
# @Author  : lichenxiao
# @File    : 00000.py
from typing import List


def quick_sort(nums: List[int], left: int, right: int) -> List[int]:
    if left >= right:
        return
    index = partition(nums, left, right)
    quick_sort(nums, left, index - 1)
    quick_sort(nums, index + 1, right)


def partition(nums: List[int], left: int, right: int) -> int:
    index = left
    pivot = nums[index]
    while left < right:
        # 这里就得没等于
        while left < right and nums[right] > pivot:
            right -= 1
        # 这里就得有等于
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    # 这里是交换
    nums[left], nums[index] = nums[index], nums[left]
    return left


if __name__ == '__main__':
    nums = [10, 7, 8, 5, 1, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
