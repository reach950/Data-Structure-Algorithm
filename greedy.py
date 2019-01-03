#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""贪心算法"""


# 在一个非负整数中，移除 k 个数字，让剩下的数最小
def greedy_test(num, k):
    num_list = [int(i) for i in str(num)]
    j = 0
    while k > 0 and j < len(num_list) - 1:
        if num_list[j] > num_list[j+1]:
            num_list.pop(j)
            k -= 1
            j -= 1
        else:
            j += 1
    if j == len(num_list) - 1:
        while k > 0:
            num_list.pop()
            k -= 1
    return num_list


if __name__ == '__main__':
    print(greedy_test(4556847594546, 5))
