#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用栈实现队列"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack, self.pop_stack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.pop_stack:
            for i in range(len(self.pop_stack)):
                self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.push_stack:
            for i in range(len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
        if self.pop_stack:
            return self.pop_stack.pop()
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        elif self.push_stack:
            for i in range(len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.push_stack and not self.pop_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
