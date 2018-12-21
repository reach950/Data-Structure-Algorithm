#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""leetcode算法题"""


class Solution:

    # 1. Two Sum 两数之和
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

    # 50. Pow(x, n)
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x * x, n // 2)

    # 169. Majority Element 求众数
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_dict = dict()
        for i in nums:
            temp_dict[i] = temp_dict.get(i, 0) + 1
            if temp_dict[i] > len(nums) / 2:
                return i

    # 122. Best Time to Buy and Sell Stock II 买卖股票的最佳时机 II
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) < 2:
            return profit
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit

    # 22. Generate Parentheses 括号生成
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left+1, right, n, result+'(')
        if right < left:
            self._gen(left, right+1, n, result+')')

    # 51. N-Queens N皇后
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.select_column = set()
        self.forward_slash = set()
        self.back_slash = set()
        self.result = []
        self._solveNQueens(n, 0, [])
        return self.result

    def _solveNQueens(self, n, row, curr_list):
        if row >= n:
            self.result.append(curr_list)
            return
        for i in range(n):
            if i not in self.select_column and row+i not in self.forward_slash and row-i not in self.back_slash:
                self.select_column.add(i)
                self.forward_slash.add(row+i)
                self.back_slash.add(row-i)

                self._solveNQueens(n, row+1, curr_list+[i])

                self.select_column.remove(i)
                self.forward_slash.remove(row+i)
                self.back_slash.remove(row-i)

    # 69. Sqrt(x) x 的平方根
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid == x / mid:
                return mid
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return right

    # 69 修改版，返回精度小数
    def my_sqrt(self, x, precision):
        left, right = 0, x
        while right - left >= 1 / (10 ** precision):
            mid = left + (right - left) / 2
            if mid > x / mid:
                right = mid
            else:
                left = mid
        return left


if __name__ == '__main__':
    print(Solution().my_sqrt(2, 2))
