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

    def append(self, data):
        """
        在链表结尾增加一个节点
        :param data:
        :return:
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = new_node

    def remove_data(self, data):
        """
        删除data = data的节点
        :param data:
        :return:
        """
        if not self.head:
            return
        delete_node = None
        if self.head.data == data:  # 头结点
            self.head = self.head.next
            delete_node = self.head
        else:  # 非头结点
            p = self.head.next
            p_pre = self.head
            while p:
                if p.data == data:
                    delete_node = p
                    p_pre.next = p.next
                    break
                p = p.next
                p_pre = p_pre.next
        if delete_node:
            del delete_node

    def remove_node(self, delete_node):
        """
        13
        使用O(1)的时间复杂度，删除node指向的节点
        无法保证节点是否在链表中
        """
        if not self.head:
            return
        if delete_node == self.head:  # 头结点
            self.head = self.head.next
        else:  # 非头结点
            if delete_node.next:  # 非尾结点
                p = delete_node.next
                delete_node.data = p.data
                delete_node.next = p.next
                delete_node = p
            else:  # 尾节点
                p_pre = self.head
                p = p_pre.next
                while p != delete_node:
                    p = p.next
                    p_pre = p_pre.next
                p_pre.next = None
        if delete_node:
            del delete_node

    def print_reverse(self):
        """
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
        用递归实现
        :return:
        """

        def _print_reverse_recursively(head):
            if head:
                if head.next:
                    _print_reverse_recursively(head.next)
                print head.data

    def the_last_k_node(self, k):
        """
        15、链表中倒数第k个节点
        """
        if k <= 0:
            return False
        if not self.head:
            return None
        pre = self.head
        for i in range(0, k):
            if pre.next:
                pre = pre.next
            else:
                return False
        p = self.head
        while pre.next:
            pre = pre.next
            p = p.next
        return p


def merge_to_sorted_list(l1, l2):
    """
    17、合并两个排序链表
    """
    if not l1.head:
        return l2.head
    if not l2.head:
        return l1.head

    p1 = l1.head
    p2 = l2.head
    p_head = None
    p3 = Node()

    while p1 and p2:
        if p1.data <= p2.data:
            if not p_head:
                p_head = p1
            p3.next = p1
            p1 = p1.next
        else:
            if not p_head:
                p_head = p2
            p3.next = p2
            p2 = p2.next
        p3 = p3.next

    if p1:
        p3.next = p1
    elif p2:
        p3.next = p2
    return p_head


def merge_to_sorted_list_v2(l1, l2):
    """
    17、合并两个排序链表
    """
    if not l1.head:
        return l2.head
    if not l2.head:
        return l1.head

    p1 = l1.head
    p2 = l2.head

    if p1.data <= p2.data:
        p_head = p1
        p3 = p1
        p1 = p1.next
    else:
        p_head = p2
        p3 = p2
        p2 = p2.next

    while p1 and p2:
        if p1.data <= p2.data:
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next
        p3 = p3.next

    if p1:
        p3.next = p1
    elif p2:
        p3.next = p2
    return p_head


def test_merge():
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
    l.append(10)
    # print 'list', l
    # l.remove_data(4)
    # print 'list', l
    # l.print_reverse()

    node21 = Node(1)
    node22 = Node(2)
    node23 = Node(3)

    node21.next = node22
    node22.next = node23

    l2 = LinkedList(node21)
    print 'len', len(l2)
    print 'list', l2

    head = merge_to_sorted_list_v2(l, l2)
    data_list = []
    while head:
        data_list.append(str(head.data))
        head = head.next
    print ' '.join(data_list)


def get_list():
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
    l.append(10)
    res = l.the_last_k_node(5)
    print res.data


if __name__ == '__main__':
    test_merge()
