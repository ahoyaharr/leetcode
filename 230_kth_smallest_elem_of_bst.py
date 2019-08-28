# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def in_order(self, node):
        if node.left:
            self.in_order(node.left)

        print(node.val)

        if node.right:
            self.in_order(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root.left:
            self.in_order(root.left, k)

        print(root.val, k)

        if root.right:
            self.in_order(root.right, k)