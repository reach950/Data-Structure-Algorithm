#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""递归树"""


# 打印一组数据的所有排列
# k表示要处理的数据个数
def print_permutations(array_data, k):
    if k == 1:
        print(array_data)
    for i in range(k):
        array_data[i], array_data[k-1] = array_data[k-1], array_data[i]
        print_permutations(array_data, k-1)
        array_data[i], array_data[k-1] = array_data[k-1], array_data[i]


if __name__ == '__main__':
    print_permutations([1, 2, 3, 4], 4)
