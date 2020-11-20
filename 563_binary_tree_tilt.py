# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        The tilt of a binary tree is given by abs( sum(left_subtree) + sum(right_subtree) ).
        findTilt returns the sum of the tilts of every node in a binary tree.
        :param root:
        :return:
        """
        tilts = [0]

        def traverse(node):
            if node.left:
                left_sum = traverse(node.left)
            else:
                left_sum = 0

            if node.right:
                right_sum = traverse(node.right)
            else:
                right_sum = 0

            tilts.append(abs(left_sum - right_sum))
            return left_sum + right_sum + node.val

        if root:
            traverse(root)
        return sum(tilts)