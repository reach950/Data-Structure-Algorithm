#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""编辑距离"""

import sys


class Solution:
    # 回溯算法 时间复杂度2的n次方 edist指当前的编辑距离
    def minDistance(self, word1: str, word2: str) -> int:

        def _minDistance(i, j, edist):
            if i == m or j == n:
                if i < m:
                    edist += m - i
                if j < n:
                    edist += n - j
                if edist < self.res:
                    self.res = edist
                return
            if word1[i] == word2[j]:
                _minDistance(i + 1, j + 1, edist)
            else:
                _minDistance(i + 1, j, edist + 1)
                _minDistance(i, j + 1, edist + 1)
                _minDistance(i + 1, j + 1, edist + 1)

        m = len(word1)
        n = len(word2)
        self.res = sys.maxsize
        _minDistance(0, 0, 0)
        return self.res

    # 动态规划 时间复杂度m*n
    def minDistance1(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return m or n
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if word1[i] == word2[0]:
                dp[i][0] = i
            elif i != 0:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = 1
        for j in range(n):
            if word2[j] == word1[0]:
                dp[0][j] = j
            elif j != 0:
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[m - 1][n - 1]

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1), dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)
        return dp[m][n]


if __name__ == '__main__':
    word1 = 'intention'
    word2 = 'execution'
    print(Solution().minDistance2(word1, word2))
