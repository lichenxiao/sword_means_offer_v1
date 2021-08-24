#!/usr/bin/env python
# encoding: utf-8
# @author: lichenxiao
# @file: 7_stack_queue.py
# @time: 2021/4/7 12:01 上午
# @desc: 栈模拟队列。 队列模拟栈


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, data):
        self.stack1.append(data)

    def delete_head(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


class Stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        if not self.queue1 and not self.queue2:
            self.queue1.append(data)
            return
        if self.queue1:
            self.queue1.append(data)
            return
        if self.queue2:
            self.queue2.append(data)
            return

    def pop(self):
        if self.queue1:
            queue1 = self.queue1
            queue2 = self.queue2
        elif self.queue2:
            queue1 = self.queue2
            queue2 = self.queue1
        else:
            return None

        while len(queue1) > 1:
            queue2.append(queue1[0])
            del queue1[0]
        data = queue1[0]
        del queue1[0]
        return data


if __name__ == '__main__':
    # q = Queue()
    # q.append_tail(1)
    # q.append_tail(2)
    # print q.delete_head()
    # q.append_tail(3)
    # q.append_tail(4)
    # print q.delete_head()
    # print q.delete_head()
    # print q.delete_head()
    # print q.delete_head()

    s = Stack()
    s.push(1)
    s.push(2)
    print s.pop()
    s.push(3)
    s.push(4)
    print s.pop()


