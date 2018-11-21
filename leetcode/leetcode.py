#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""leetcode算法题"""


class Solution:

    # 1. Two Sum
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

    # 20. Valid Parentheses 有效的括号
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

    # 242. Valid Anagram 有效的字母异位词
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list, t_list = [0]*26, [0]*26
        for i in s:
            s_list[ord(i) - ord('a')] += 1
        for j in t:
            t_list[ord(j) - ord('a')] += 1
        return s_list == t_list

    # 15. 3Sum 三数之和
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        result_list = set()
        for i, x in enumerate(nums[:-2]):
            if i >= 1 and x == nums[i-1]:
                continue
            temp_dict = dict()
            for j, y in enumerate(nums[i+1:]):
                if y not in temp_dict:
                    temp_dict[y] = j
                if -x-y in temp_dict and temp_dict[-x-y] != j:
                    result_list.add((x, -x-y, y))
        return map(list, result_list)
