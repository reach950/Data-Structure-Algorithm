#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""贪心算法"""


# 在一个非负整数中，移除 k 个数字，让剩下的数最小
def greedy_test(num, k):
    num_list = [int(i) for i in str(num)]
    stack = []
    for j in num_list:
        while stack and stack[len(stack)-1] > j and k > 0:
            stack.pop()
            k -= 1
        stack.append(j)
    while k > 0:
        stack.pop()
        k -= 1
    return stack


if __name__ == '__main__':
    print(greedy_test(123456789, 5))
