# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0

        cumulative_value = root.val if L <= root.val <= R else 0
        if root.val > L:
            cumulative_value += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            cumulative_value += self.rangeSumBST(root.right, L, R)
        return cumulative_value
