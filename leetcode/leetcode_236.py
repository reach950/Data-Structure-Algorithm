#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""二叉树的最近公共祖先"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 普通二叉树
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

    # 搜索二叉树,循环解决
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        while True:
            if p.val >= root.val >= q.val or p.val <= root.val <= q.val:
                return root
            elif p.val > root.val < q.val:
                root = root.right
            else:
                root = root.left

    # 搜索二叉树，递归解决
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val >= root.val >= q.val or p.val <= root.val <= q.val:
            return root
        elif p.val > root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        else:
            return self.lowestCommonAncestor2(root.left, p, q)
