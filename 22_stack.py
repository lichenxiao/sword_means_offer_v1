#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: stack_with_min.py
# @time: 2021/6/4 4:19 下午
# @desc:

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        if not self.empty:
            return self.stack.pop()
        else:
            return None

    @property
    def top(self):
        if not self.empty:
            return self.stack[-1]
        else:
            return None

    @property
    def empty(self):
        if self.stack:
            return False
        return True


def check_if_pop_list(push_l, pop_l):
    if len(push_l) != len(pop_l):
        return False
    lenl = len(push_l)

    push_index = 0
    pop_index = 0
    s = Stack()
    while True:
        while push_index < lenl and s.top != pop_l[pop_index]:
            item = push_l[push_index]
            s.push(item)
            push_index += 1

        while pop_index < lenl and s.top == pop_l[pop_index]:
            a = s.pop()
            print a
            pop_index += 1

        if s.empty:
            return True

        if push_index >= lenl:
            return False


print check_if_pop_list('12345', '45321')
print check_if_pop_list('12345', '43512')
