#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 11:56 PM
# @Author  : lichenxiao
# @File    : 27_BST_Dlist.py
# 将二叉排序树转化为双向链表


class BinaryTreeNode:
    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """
        测试基本功能，输出字符串
        :return:
        """
        return str(self.data)


class BinaryTree:
    """树类"""

    def __init__(self, node=None):
        if node:
            self.root = node
            self.myQueue = [node]  # 保存左右子节点未完整的列表
            self.all_node = [node]  # 所有节点的层序遍历的顺序
        else:
            self.root = BinaryTreeNode()
            self.myQueue = []
            self.all_node = []

    def __str__(self):
        """
        测试基本功能，输出字符串
        :return:
        """
        l = []
        for i in self.all_node:
            l.append(str(i.data))
        return ' '.join(l)

    def add(self, data):
        """为树添加节点"""
        node = BinaryTreeNode(data)
        if self.root.data == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
            self.all_node.append(node)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                self.all_node.append(node)
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.all_node.append(node)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print node.data,
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


def change(bst_root):
    if bst_root.left:
        p_head_l, p_last_l = change(bst_root.left)
        p_last_l.right = bst_root
        bst_root.left = p_last_l
    else:
        p_head_l = bst_root

    p_last_l = bst_root

    if bst_root.right:
        p_head_r, p_last_r = change(bst_root.right)
        p_last_l.right = p_head_r
        p_head_r.left = p_last_l
    else:
        p_last_r = bst_root
    return p_head_l, p_last_r


if __name__ == '__main__':
    """主函数"""
    # 生成十个数据作为树节点
    tree = BinaryTree()  # 新建一个树对象
    for data in [10, 6, 14, 4, 8, 12, 16]:
        tree.add(data)  # 逐个添加树的节点

    print '队列实现层次遍历:'
    print tree.level_queue(tree.root)
    print isinstance(tree.root, BinaryTreeNode)
    print isinstance(tree.root, BinaryTreeNode)
    a, b = change(tree.root)
    print a.data
    print b.data
