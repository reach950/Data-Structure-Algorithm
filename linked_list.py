#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""链表算法题"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    # 反转链表
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    # 两两反转
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        start = head.next
        while curr and curr.next:
            a = curr.next
            if prev is not None:
                prev.next = curr.next
                prev = prev.next
            else:
                prev = curr
            a.next, curr.next, curr = curr, a.next, curr.next.next
        return start
