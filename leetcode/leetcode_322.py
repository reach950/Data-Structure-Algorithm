#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""零钱兑换"""


class Solution:
    def coinChange(self, coins, amount):
        dp_status = [amount+1 for _ in range(amount+1)]
        dp_status[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp_status[i] = min(dp_status[i], dp_status[i-coin]+1)
        if dp_status[amount] > amount:
            return -1
        else:
            return dp_status[amount]


if __name__ == '__main__':
    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount))
