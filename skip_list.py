#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""跳表"""


class SkipList:

    class Node:
        def __init__(self):
            self._data = -1
            self._forwords = []
            self._max_level = 0

        def __str__(self):
            return '{{data: {}; levels: {}}}'.format(self._data, self._max_level)


if __name__ == '__main__':
    print(SkipList().Node())
