#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 6_tree.py
# @time: 2021/4/5 8:13 下午
# @desc: 二叉树，先中后层序遍历，
# 红黑树，树中的节点定义为红黑两种颜色，通过规则确保，从根节点到叶节点最长的路径的长度不超过最短路径的两倍
# c++ STl中set multiset map multimap都是通过红黑树实现
# 最大堆，最小堆 快速找到最大值或者最小值的问题可以用堆来实现
# 19、树的景象


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

    def construct_tree(self, preorder, inorder):
        """
        通过先序和中序构建二叉树
        :return:
        """

        def construct(preorder_start, preorder_end, inorder_start, inorder_end):
            root_data = preorder[preorder_start]
            root = BinaryTreeNode(root_data)
            if preorder_start == preorder_end:
                if preorder[preorder_start, preorder_end] == inorder[inorder_start, inorder_end]:
                    return root
                else:
                    raise ValueError('cannot construct tree')
            try:
                root_index = inorder[inorder_start, inorder_end].index(root_data)
            except:
                raise ValueError('cannot construct tree')
            left_length = root_index
            left_end = preorder_start + root_index
            right_length = preorder_end - left_end
            if left_length:
                root.left = construct(preorder_start + 1, left_end, inorder_start,
                                      root_index + inorder_start)
            if right_length:
                root.right = construct(left_end + 1, preorder_end, inorder_start + 1, inorder_end)
            return root

        if not preorder and not inorder:
            return None
        return construct(0, len(preorder), 0, len(inorder))


def mirror_tree(tree_root):
    """
    树的的镜像树，对与每个节点都是交换左右孩子，可以使用前序遍历方式
    """
    if not tree_root:
        return
    if not tree_root.left and tree_root.right:
        return

    tree_root.left, tree_root.right = tree_root.right, tree_root.left
    mirror_tree(tree_root.left)
    mirror_tree(tree_root.right)
    return tree_root


if __name__ == '__main__':
    """主函数"""
    datas = range(1, 10)  # 生成十个数据作为树节点
    tree = BinaryTree()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个添加树的节点

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)
