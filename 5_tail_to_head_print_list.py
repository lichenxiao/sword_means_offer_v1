#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 7_list.py
# @time: 2021/4/5 6:28 下午
# @desc: 链表的基本操作：
# 5、从尾到头打印链表 递归
# 13、O(1)时间删除链表节点，入参：节点的指针
# 15、链表中倒数第k个节点
# 16、反转链表
# 17、合并两个排序链表


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        """
        测试基本功能，输出字符串
        :return:
        """
        return str(self.data)


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        """
        输入头节点，返回链表长度
        :return:
        """
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def __str__(self):
        data_list = []
        head = self.head
        while head:
            data_list.append(str(head.data))
            head = head.next
        return ' '.join(data_list)

    def print_reverse(self):
        """
        5
        用栈实现
        栈：先进后出
        :return:
        """
        l = []
        p = self.head
        while p:
            l.append(p.data)
            p = p.next
        while l:
            data = l.pop()
            print data

    def print_reverse_recursively(self):
        """
        5
        用递归实现
        :return:
        """

        def _print_reverse_recursively(head):
            if head:
                if head.next:
                    _print_reverse_recursively(head.next)
                print head.data

        _print_reverse_recursively(self.head)


if __name__ == '__main__':
    # test_merge()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    l = LinkedList(node1)
    print 'len', len(l)
    print 'list', l
    # l.append(10)
    # print 'list', l
    # l.remove_data(4)
    # print 'list', l
    l.print_reverse_recursively()
    l.print_reverse()
