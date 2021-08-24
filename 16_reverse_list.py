#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 10:10 PM
# @Author  : lichenxiao
# @File    : reverse_list.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(l_head):
    if not l_head:
        return None
    if not l_head.next:
        return l_head

    a = l_head
    b = a.next
    a.next = None
    if b.next:
        c = b.next
    else:
        c = None

    while True:
        b.next = a
        if not c:
            return b
        a = b
        b = c
        c = c.next


def print_list(head):
    h = head
    while h:
        print h.val
        h = h.next


def reverse_list_recur(head):
    """
    https://zhuanlan.zhihu.com/p/86745433
    """
    if not head or not head.nex:
        return head
    last = reverse_list_recur(head.next)
    head.next.next = head
    head.next = None
    return last


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

head = l1
# new_head = revese_list(head)
new_head = reverse_list_recur(head)
print_list(new_head)

