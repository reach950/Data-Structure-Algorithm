#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""跳表"""

import random

MAX_LEVEL = 16


class SkipList:

    class Node:
        def __init__(self):
            self.data = -1
            self.forwords = [None] * MAX_LEVEL
            self.max_level = 0

        def __str__(self):
            return '{{data: {}; levels: {}}}'.format(self.data, self.max_level)

    level_count = 1
    head = Node()

    @classmethod
    def find(cls, value):
        p = cls.head
        for i in reversed(range(cls.level_count)):
            while p.forwords[i] is not None and p.forwords[i].data < value:
                p = p.forwords[i]
        if p.forwords[0] is not None and p.forwords[0].data == value:
            return p.forwords[0]
        else:
            return None

    @classmethod
    def insert(cls, value):
        level = cls.random_level()
        new_node = cls.Node()
        new_node.data = value
        new_node.max_level = level
        temp_list = []
        for i in range(level):
            temp_list.append(cls.head)
        p = cls.head
        for j in reversed(range(level)):
            while p.forwords[j] is not None and p.forwords[j].data < value:
                p = p.forwords[j]
            temp_list.append(p)
        for k in range(level):
            new_node.forwords[k] = temp_list[k].forwords[k]
            temp_list[k].forwords[k] = new_node
        if cls.level_count < level:
            cls.level_count = level

    @classmethod
    def delete(cls, value):
        p = cls.head
        temp_list = []
        for i in reversed(range(cls.level_count)):
            while p.forwords[i] is not None and p.forwords[i].data < value:
                p = p.forwords[i]
            temp_list.append(p)

        if p.forwords[0] is not None and p.forwords[0].data == value:
            for j in reversed(range(cls.level_count)):
                if temp_list[j].forwords[j] is not None and temp_list[j].forwords[j].data == value:
                    temp_list[j].forwords[j] = temp_list[j].forwords[j].forwords[j]

    @staticmethod
    def random_level():
        level = 1
        for i in range(1, MAX_LEVEL):
            if random.randint(1, 10) % 2 == 1:
                level += 1
        return level


if __name__ == '__main__':
    print(SkipList.Node())
