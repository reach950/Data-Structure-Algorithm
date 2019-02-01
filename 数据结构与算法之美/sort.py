#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 冒泡排序
def bubble_sort(target_list):
    for i in range(len(target_list)):
        flag = False
        for j in range(len(target_list)-i-1):
            if target_list[j] > target_list[j+1]:
                target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
                flag = True
        if not flag:
            break
    return target_list


# 插入排序
def insert_sort(target_list):
    for i in range(1, len(target_list)):
        temp = target_list[i]
        j = i - 1
        while temp < target_list[j]:
            target_list[j+1] = target_list[j]
            j -= 1
            if j < 0:
                break
        target_list[j+1] = temp
    return target_list


# 选择排序
def selection_sort(target_list):
    for i in range(len(target_list)-1):
        index = i
        for j in range(i+1, len(target_list)):
            if target_list[j] < target_list[index]:
                index = j
        target_list[i], target_list[index] = target_list[index], target_list[i]
    return target_list


# 归并排序
def merge_sort(target_list):

    def merge(a_list, b_list):
        temp_list = []
        i = 0
        j = 0
        while i < len(a_list) and j < len(b_list):
            if a_list[i] <= b_list[j]:
                temp_list.append(a_list[i])
                i += 1
            else:
                temp_list.append(b_list[j])
                j += 1
        if i == len(a_list):
            for k in b_list[j:]:
                temp_list.append(k)
        else:
            for k in a_list[i:]:
                temp_list.append(k)
        return temp_list

    if len(target_list) <= 1:
        return target_list
    sep = len(target_list) // 2
    return merge(merge_sort(target_list[:sep]), merge_sort(target_list[sep:]))


# 快速排序
def quick_sort(target_list):

    def seprate(start, end):
        pivot = target_list[end]
        i = j = start
        while j < end:
            if target_list[j] < pivot:
                target_list[i], target_list[j] = target_list[j], target_list[i]
                i += 1
            j += 1
        target_list[end], target_list[i] = target_list[i], target_list[end]
        return i

    def quick_sort_recursive(start, end):
        if start >= end:
            return
        seprate_index = seprate(start, end)
        quick_sort_recursive(start, seprate_index-1)
        quick_sort_recursive(seprate_index+1, end)

    quick_sort_recursive(0, len(target_list)-1)
    return target_list


# 计数排序
def count_sort(target_list):
    max = target_list[0]
    for i in target_list:
        if max < i:
            max = i
    count_list = [0] * (max + 1)
    for i in target_list:
        count_list[i] += 1
    for i in range(1, max+1):
        count_list[i] = count_list[i-1] + count_list[i]
    temp_list = target_list.copy()
    for i in reversed(target_list):
        index = count_list[i] - 1
        temp_list[index] = i
        count_list[i] -= 1
    target_list = temp_list
    return target_list


# 求解无序数组中第K大元素
def find_index(target_list, k):

    def seprate(start, end):
        pivot = target_list[end]
        i = j = start
        while j < end:
            if target_list[j] < pivot:
                target_list[i], target_list[j] = target_list[j], target_list[i]
                i += 1
            j += 1
        target_list[end], target_list[i] = target_list[i], target_list[end]
        return i

    def find_index_recursive(start, end):
        if start >= end:
            return
        index = seprate(start, end)
        if index+1 == k:
            return
        elif index+1 > k:
            find_index_recursive(start, index-1)
        else:
            find_index_recursive(index+1, end)

    find_index_recursive(0, len(target_list)-1)
    return target_list[k-1]


if __name__ == '__main__':
    test_list = [6, 8, 17, 11, 9, 3, 32, 23, 5, 25]
    print(merge_sort(test_list))
