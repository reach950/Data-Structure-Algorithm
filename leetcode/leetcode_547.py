#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""朋友圈的数量"""


class Solution:
    def findCircleNum(self, M):
        pass


class UnionFind:

    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1


if __name__ == '__main__':
    m = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Solution().findCircleNum(m))
