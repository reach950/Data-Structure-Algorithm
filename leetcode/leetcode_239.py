#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""滑动窗口最大值"""

import heapq
import collections


class Solution:
    # heap实现
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt, heap, res = collections.Counter(), [], []
        for i, num in enumerate(nums):
            heapq.heappush(heap, -num)
            cnt[num] += 1
            while not cnt[-heap[0]]:
                heapq.heappop(heap)
            if i >= k - 1:
                res.append(-heap[0])
                cnt[nums[i - k + 1]] -= 1
        return res

    # deque实现
    def maxSlidingWindow_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        deque, res = collections.deque(), []
        for i, num in enumerate(nums):
            if i >= k and i-k >= deque[0]:
                deque.popleft()
            while deque and nums[deque[-1]] <= num:
                deque.pop()
            deque.append(i)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res
