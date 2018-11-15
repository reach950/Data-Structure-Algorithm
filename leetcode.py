#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""leetcode算法题"""


class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for i, x in enumerate(nums):
            if (target - x) in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i

    # 验证括号是否合法
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_stack = []
        characters_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in characters_dict.values():
                temp_stack.append(i)
            elif not temp_stack or characters_dict[i] != temp_stack.pop():
                return False
        if temp_stack:
            return False
        return True
