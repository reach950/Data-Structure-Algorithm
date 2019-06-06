#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""三角形最小路径和"""

import sys


class Solution:
    # 回溯算法 时间复杂度2的n次方
    def minimumTotal(self, triangle):
        self.size = len(triangle)
        self.res = sys.maxsize
        self._minimumTotal(triangle, 0, 0, 0)
        return self.res

    def _minimumTotal(self, triangle, i, j, total):
        if i == self.size:
            if total < self.res:
                self.res = total
            return
        total += triangle[i][j]
        self._minimumTotal(triangle, i+1, j, total)
        self._minimumTotal(triangle, i+1, j+1, total)

    # 动态规划递归
    def minimum_total(self, triangle):

        def _minimum_total(i, j):
            if i == 0 and j == 0:
                triangle_total[i][j] = triangle[0][0]
                return triangle_total[i][j]
            if triangle_total[i][j] > 0:
                return triangle_total[i][j]
            min_left = sys.maxsize
            if j-1 >= 0:
                min_left = _minimum_total(i-1, j-1)
            min_right = sys.maxsize
            if j <= i-1:
                min_right = _minimum_total(i-1, j)
            curr_min_total = min(min_left, min_right) + triangle[i][j]
            triangle_total[i][j] = curr_min_total
            return curr_min_total

        size = len(triangle)
        triangle_total = [[0 for _ in range(i)] for i in range(1, size+1)]
        for i in range(size):
            _minimum_total(size-1, i)
        res = sys.maxsize
        for i in range(size):
            if res > triangle_total[size-1][i]:
                res = triangle_total[size-1][i]
        return res

    # 动态规划非递归
    def minimum_total1(self, triangle):
        size = len(triangle)
        mem_res = [0 for _ in range(size)]
        mem_res[0] = triangle[0][0]
        for i in range(1, size):
            for j in reversed(range(i+1)):
                min_left = min_right = sys.maxsize
                if j > 0:
                    min_left = mem_res[j-1]
                if j < i:
                    min_right = mem_res[j]
                mem_res[j] = min(min_left, min_right) + triangle[i][j]
        res = sys.maxsize
        for i in mem_res:
            if res > i:
                res = i
        return res


if __name__ == '__main__':
    test_data = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimum_total1(test_data))
