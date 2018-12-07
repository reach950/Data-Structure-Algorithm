#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二叉树最小深度"""

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 广度优先
    def minDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = collections.deque([root])
        min_depth = 0
        while queue:
            min_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left is None and node.right is None:
                    return min_depth

    # 深度优先
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.minDepth(root.left) + 1
        right = self.minDepth(root.right) + 1
        if left == 1:
            return right
        if right == 1:
            return left
        return min(left, right)
