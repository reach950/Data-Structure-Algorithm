#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二分法查找"""


def binary_search(test_list, value):
    low = 0
    high = len(test_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if test_list[mid] == value:
            return mid
        elif test_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    test_list = [1, 3, 4, 9, 10, 11]
    value = 9
    print(binary_search(test_list, value))
