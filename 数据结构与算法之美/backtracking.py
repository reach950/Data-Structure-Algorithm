#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""回溯算法"""


class Backtracking:

    maxw = 0

    # 0,1背包问题
    # i表示考察到哪个物品了,cw表示当前装进去的重量和,w表示背包重量,n表示物品总个数
    @classmethod
    def f(cls, i, cw, items, n, w):
        if cw == w or i == n:
            if cw > cls.maxw:
                cls.maxw = cw
            return
        cls.f(i + 1, cw, items, n, w)
        if cw + items[i] <= w:
            cls.f(i + 1, cw + items[i], items, n, w)

    # 0,1背包问题优化算法
    @classmethod
    def f_opt(cls, items, n, w):
        cls.state_list = [[False for _ in range(w + 1)] for _ in range(n)]
        cls.f_opt_helper(0, 0, items, n, w)

    @classmethod
    def f_opt_helper(cls, i, cw, items, n, w):
        if cw == w or i == n:
            if cw > cls.maxw:
                cls.maxw = cw
            return
        if cls.state_list[i][cw]:
            return
        cls.state_list[i][cw] = True
        cls.f_opt_helper(i + 1, cw, items, n, w)
        if cw + items[i] <= w:
            cls.f_opt_helper(i + 1, cw + items[i], items, n, w)

    # n皇后问题
    @classmethod
    def solve_n_queens(cls, n):
        cls.result = []
        cls.helper(0, n, [])
        return cls.result

    @classmethod
    def helper(cls, row, n, col_list):
        if row == n:
            cls.result.append(col_list)
            return
        for col in range(n):
            if cls.is_valid(n, row, col, col_list):
                cls.helper(row + 1, n, col_list + [col])

    @classmethod
    def is_valid(cls, n, row, col, col_list):
        left_up = col - 1
        right_up = col + 1
        for i in reversed(range(row)):
            if col_list[i] == col:
                return False
            if left_up >= 0:
                if col_list[i] == left_up:
                    return False
            if right_up < n:
                if col_list[i] == right_up:
                    return False
            left_up -= 1
            right_up += 1
        return True

    # 数读问题
    @classmethod
    def solve_shudu(cls, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    for i in range(1, 10):
                        if cls.is_ok(board, row, col, i):
                            board[row][col] = str(i)
                            if cls.solve_shudu(board):
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return True

    @classmethod
    def is_ok(cls, board, row, col, num):
        num_str = str(num)
        for i in range(9):
            if board[row][i] == num_str:
                return False
            if board[i][col] == num_str:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num_str:
                return False
        return True

    # 硬币找零问题 coin_list:已有的硬币价格 price:总价
    def find_min_coins(self, coin_list, price):
        self.count = price
        self.find_min_coins_helper(coin_list, price, 0, 0)
        return self.count

    def find_min_coins_helper(self, coin_list, price, n, price_sum):
        if price_sum == price:
            if n < self.count:
                self.count = n
            return
        for coin in coin_list:
            if coin <= price - price_sum:
                self.find_min_coins_helper(coin_list, price, n+1, price_sum+coin)


if __name__ == '__main__':
    # print(Backtracking.solve_n_queens(4))
    # board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    #          ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    #          ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    #          ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    #          ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    #          ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    #          ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    #          ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    #          ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    #          ]
    # Backtracking.solve_shudu(board)
    # for i in board:
    #     print(i)
    print(Backtracking().find_min_coins([1, 3, 5], 9))
