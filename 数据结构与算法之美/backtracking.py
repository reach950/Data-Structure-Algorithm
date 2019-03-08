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


if __name__ == '__main__':
    # items = [7, 2, 4, 11, 9]
    # Backtracking.f(0, 0, items, len(items), 25)
    # print(Backtracking.maxw)
    print(Backtracking.solve_n_queens(4))
