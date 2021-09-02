#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 6_tree.py
# @time: 2021/4/5 8:13 下午
# @desc: 二叉树，先中后层序遍历，
# 红黑树，树中的节点定义为红黑两种颜色，通过规则确保，从根节点到叶节点最长的路径的长度不超过最短路径的两倍
# c++ STl中set multiset map multimap都是通过红黑树实现
# 最大堆，最小堆 快速找到最大值或者最小值的问题可以用堆来实现
# 6、重建二叉树，通过前序和中序遍历的结果，重建二叉树
# 18、判断b树是不是a树的子树
# 23、从上到下打印二叉树 -》层序遍历


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
            self.myQueue = [node]
            self.all_node = [node]
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

    def preorder_recursively(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print root.data,
        self.preorder_recursively(root.left)
        self.preorder_recursively(root.right)

    def in_order_recursively(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.in_order_recursively(root.left)
        print root.data,
        self.in_order_recursively(root.right)

    def post_order_recursively(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.post_order_recursively(root.left)
        self.post_order_recursively(root.right)
        print root.data,

    def preorder_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print node.data,
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right  # 开始查看它的右子树

    def in_order_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print node.data,
            node = node.right  # 开始查看它的右子树

    def post_order_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print myStack2.pop().data,

    def level_queue(self, root):
        """
        23
        利用队列实现树的层次遍历
        """
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

    def level_queue_with_newline(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        myQueue.append('\n')
        while myQueue:
            node = myQueue.pop(0)
            if node != '\n':
                print node.data,
                if node.left != None:
                    myQueue.append(node.left)
                if node.right != None:
                    myQueue.append(node.right)
            else:
                print node
                myQueue.append('\n')

    def construct_tree(self, preorder, inorder):
        """
        6
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


if __name__ == '__main__':
    """主函数"""
    datas = range(1, 10)  # 生成十个数据作为树节点
    tree = BinaryTree()  # 新建一个树对象
    for data in datas:
        tree.add(data)  # 逐个添加树的节点

    print '队列实现层次遍历:'
    tree.level_queue(tree.root)

    print '\n\n递归实现先序遍历:'
    tree.preorder_recursively(tree.root)
    print '\n递归实现中序遍历:'
    tree.in_order_recursively(tree.root)
    print '\n递归实现后序遍历:'
    tree.post_order_recursively(tree.root)

    print '\n\n堆栈实现先序遍历:'
    tree.preorder_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.in_order_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.post_order_stack(tree.root)
