#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""乘积最大子序列"""


class Solution:
    # 回溯算法
    def maxProduct(self, nums):

        # n:考察到第几个数,product:乘积
        def _maxProduct(n, product):
            nonlocal max_product
            if n > 0 and max_product < product:
                max_product = product
            if n == len(nums)-1:
                return
            _maxProduct(n+1, nums[n+1])
            _maxProduct(n+1, product*nums[n+1])

        max_product = nums[0]
        _maxProduct(0, nums[0])
        return max_product

    # 动态规划
    def maxProduct1(self, nums):
        dp_states = [[0 for _ in range(2)] for _ in range(2)]
        dp_states[0][0], dp_states[0][1], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)-1):
            x, y = i % 2, (i-1) % 2
            dp_states[x][0] = max(dp_states[y][0] * nums[i], dp_states[y][1] * nums[i], nums[i])
            dp_states[x][1] = min(dp_states[y][0] * nums[i], dp_states[y][1] * nums[i], nums[i])
            res = max(dp_states[x][0], res)
        return res


if __name__ == '__main__':
    data = [2, 3, -2, 4]
    print(Solution().maxProduct1(data))
