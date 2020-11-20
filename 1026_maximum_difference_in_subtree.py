# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def traverse(root, minimum, maximum):
            if not root:
                return 0

            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)

            difference = abs(maximum - minimum)

            return max(
                difference,
                traverse(root.left, minimum, maximum) if root.left else 0,
                traverse(root.right, minimum, maximum) if root.right else 0
            )

        return traverse(root, root.val, root.val)