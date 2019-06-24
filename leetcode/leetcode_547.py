#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""朋友圈的数量"""


class Solution:
    def findCircleNum(self, M):
        if not M or not M[0]:
            return 0
        uf = UnionFind(M)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                for d in directions:
                    new_i, new_j = i + d[0], j + d[1]
                    if 0 <= new_i < m and 0 <= new_j < n and M[new_i][new_j] == 1:
                        uf.union(i * n + j, new_i * n + new_j)
        return uf.count


class UnionFind:

    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


if __name__ == '__main__':
    m = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(Solution().findCircleNum(m))
