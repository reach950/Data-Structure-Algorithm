#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二叉树最大深度"""

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 深度优先
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1
        return max(depth_left, depth_right)

    # 广度优先
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = collections.deque([root])
        max_depth = 0
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth
