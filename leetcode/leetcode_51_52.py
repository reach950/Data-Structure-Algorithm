#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""N皇后问题"""


class Solution(object):

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

    # 52. N-Queens II
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self._totalNQueens(n, 0, 0, 0, 0)
        return self.count

    def _totalNQueens(self, n, row, col, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(col | pie | na)) & ((1 << n) - 1)
        while bits > 0:
            p = bits & -bits
            self._totalNQueens(n, row+1, col | p, (pie | p) << 1, (na | p) >> 1)
            bits &= (bits - 1)


if __name__ == '__main__':
    print(Solution().totalNQueens(8))
