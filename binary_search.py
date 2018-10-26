#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二分法查找"""


# 循环查找
def binary_search_loop(test_list, value):
    low = 0
    high = len(test_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if test_list[mid] == value:
            return mid
        elif test_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# 递归查找
def binary_search_recursive(test_list, value):

    def func(low, high):
        if low > high:
            return -1
        mid = low + ((high - low) >> 1)
        if test_list[mid] == value:
            return mid
        elif test_list[mid] > value:
            return func(low, mid - 1)
        else:
            return func(mid + 1, high)
    return func(0, len(test_list) - 1)


# 查找第一个值等给定值的元素
def binary_search_first(test_list, value):
    low = 0
    high = len(test_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if test_list[mid] < value:
            low = mid + 1
        elif test_list[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or test_list[mid-1] != value:
                return mid
            else:
                high = mid - 1
    return -1


# 查找最后一个值等给定值的元素
def binary_search_last(test_list, value):
    low = 0
    high = len(test_list) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if test_list[mid] < value:
            low = mid + 1
        elif test_list[mid] > value:
            high = mid - 1
        else:
            if mid == len(test_list) - 1 or test_list[mid+1] != value:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    test_list = [1, 3, 4, 9, 9, 10, 11]
    value = 9
    print(binary_search_last(test_list, value))
