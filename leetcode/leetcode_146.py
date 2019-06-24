#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""LRU Cache"""

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.od = collections.OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        v = self.od.pop(key)
        self.od[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.pop(key)
        elif len(self.od) == self.size:
            self.od.popitem(last=False)
        self.od[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
