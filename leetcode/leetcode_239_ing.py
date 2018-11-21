#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""滑动窗口最大值"""

import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result_list = []
        max_heap = []
        if not nums and not k:
            return result_list
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(max_heap, nums[i] * -1)
            else:
                result_list.append(max_heap[0] * -1)
                if nums[i-k] == max_heap[0] * -1:
                    heapq.heapreplace(max_heap, nums[i] * -1)
                else:
                    heapq.heappush(max_heap, nums[i] * -1)
        result_list.append(max_heap[0] * -1)
        return result_list
