#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 12:07 AM
# @Author  : lichenxiao
# @File    : 26_complex_list_clone.py


class Node():
    def __init__(self, v, next=None, sibling=None):
        self.value = v
        self.next = next
        self.sibling = sibling


class ComplexList():

    def __init__(self, head=None):
        self.head = head

    def copy(self):
        node = self.head
        while node:
            new_node = Node(v=node.value, next=node.next, sibling=None)
            node.next = new_node
            node = node.next.next

        node = self.head
        new_node = node.next
        while new_node.next:
            if node.sibling:
                new_node.sibling = node.sibling.next
            node = node.next.next
            new_node = new_node.next.next

        node = self.head
        new_node = node.next
        new_head = new_node
        while new_node.next:
            node.next = new_node.next
            new_node.next = new_node.next.next
            node = node.next
            new_node = new_node.next

        return ComplexList(new_head)

    def __str__(self):
        l = []
        l_sibling = []
        n = self.head
        while n:
            l.append(n.value)
            if n.sibling:
                l_sibling.append(n.sibling.value)
            else:
                l_sibling.append('')
            n = n.next

        return ' '.join([str(i) for i in l]) + '\n' + ' '.join([str(i) for i in l_sibling])


if __name__ == '__main__':
    a = Node(v=1)
    b = Node(v=2)
    c = Node(v=3)
    d = Node(v=4)
    e = Node(v=5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    a.sibling = e
    c.sibling = e
    l = ComplexList(a)

    print l

    l_new = l.copy()
    print l_new