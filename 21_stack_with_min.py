#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: stack_with_min.py
# @time: 2021/6/4 4:19 下午
# @desc:

class StackWithMin():
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.len = 0

    @property
    def min(self):
        if self.len:
            return self.min_stack[-1]
        else:
            return False

    def push(self, a):
        self.stack.append(a)

        if self.min == False or self.min > a:
            self.min_stack.append(a)
        else:
            self.min_stack.append(self.min)
        self.len += 1

    def pop(self):
        self.min_stack.pop()
        res = self.stack.pop()
        self.len -= 1
        return res


s = StackWithMin()
s.push(3)
s.push(4)
print s.min
s.push(-1)
s.push(6)
s.push(-2)
print s.min
s.pop()
print s.min
