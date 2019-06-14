#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""买卖股票的最佳时机 III 最多进行两次交易"""

import sys


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        k = 2
        res = 0
        dp_states = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(k+1):
            if i == 0:
                dp_states[0][i][0], dp_states[0][i][1] = 0, -prices[0]
            else:
                dp_states[0][i][0], dp_states[0][i][1] = -sys.maxsize, -sys.maxsize
        for i in range(1, len(prices)):
            for j in range(0, k+1):
                if j > 0:
                    dp_states[i][j][0] = max(dp_states[i-1][j][0], dp_states[i-1][j-1][1] + prices[i])
                else:
                    dp_states[i][j][0] = dp_states[i-1][j][0]
                dp_states[i][j][1] = max(dp_states[i-1][j][1], dp_states[i-1][j][0] - prices[i])
                res = max(res, dp_states[i][j][0])
        return res


if __name__ == '__main__':
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
