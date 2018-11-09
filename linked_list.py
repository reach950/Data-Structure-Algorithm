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
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        start = head.next
        while curr and curr.next:
            a = curr.next
            b = a.next
            if prev is not None:
                prev.next = curr.next
            prev = curr
            a.next, curr.next, curr = curr, b, b
        return start

    # 判断链表是否有环(用set实现，空间复杂度O(n))
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        hash_set = set()
        while curr:
            if curr in hash_set:
                return True
            hash_set.add(curr)
            curr = curr.next
        else:
            return False

    # 判断链表是否有环(用快慢指针实现，空间复杂度O(1))
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        else:
            return False