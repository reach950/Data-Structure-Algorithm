#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用列表实现队列"""


class ArrayQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.n = capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.tail == self.n:
            return False
        self.items.append(item)
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return False
        res = self.items[self.head]
        self.head += 1
        return res
