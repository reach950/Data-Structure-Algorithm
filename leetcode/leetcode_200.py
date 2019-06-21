#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""岛屿的个数"""

from collections import deque


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        self.max_i = len(grid)
        self.max_j = len(grid[0])
        self.grid = grid
        return sum(self._dfs(i, j) for i in range(self.max_i) for j in range(self.max_j))

    def _dfs(self, i, j):
        if not self._is_valid(i, j):
            return 0
        self.grid[i][j] = '0'
        self._dfs(i - 1, j)
        self._dfs(i + 1, j)
        self._dfs(i, j - 1)
        self._dfs(i, j + 1)
        return 1

    def _bfs(self, i, j):
        if not self._is_valid(i, j):
            return 0
        queue = deque()
        self.grid[i][j] = '0'
        queue.append((i, j))
        while queue:
            cur_i, cur_j = queue.popleft()
            new_directions = [(cur_i - 1, cur_j), (cur_i + 1, cur_j), (cur_i, cur_j - 1), (cur_i, cur_j + 1)]
            for i, j in new_directions:
                if self._is_valid(i, j):
                    self.grid[i][j] = '0'
                    queue.append((i, j))
        return 1

    def _is_valid(self, i, j):
        if 0 <= i < self.max_i and 0 <= j < self.max_j and self.grid[i][j] == '1':
            return True
        else:
            return False


if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(grid))
