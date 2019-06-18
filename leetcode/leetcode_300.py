#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""最长上升子序列"""


class Solution:
    # 动态规划 时间复杂度n的平方
    def lengthOfLIS(self, nums):
        size = len(nums)
        res = 0
        dp_status = [1 for _ in range(size)]
        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp_status[i] = max(dp_status[i], dp_status[j]+1)
            res = max(res, dp_status[i])
        return res

    # 非动态规划 时间复杂度nlogn
    def lengthOfLIS1(self, nums):
        res_list = []
        for num in nums:
            if not res_list or res_list[-1] < num:
                res_list.append(num)
            else:
                start = 0
                end = len(res_list)-1
                while start <= end:
                    mid = start + ((end - start) >> 1)
                    if res_list[mid] > num:
                        end = mid - 1
                    elif res_list[mid] < num:
                        start = mid + 1
                    else:
                        start = mid
                        break
                res_list[start] = num
        return len(res_list)


if __name__ == '__main__':
    nums = [4,10,4,3,8,9]
    print(Solution().lengthOfLIS1(nums))
