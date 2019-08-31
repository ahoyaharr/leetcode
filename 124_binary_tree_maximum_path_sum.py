# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxPathSum(self, root):
        """
        Given some binary tree, computes the maximum path which exists in the tree if the edges were undirected.
               1
              / \
             2   3

        Output: 6

           -10
           / \
          9  20
            /  \
           15   7

        Output: 42
        :type root: TreeNode
        :rtype: int
        """
        node_walks = dict()  # From each node, memoize a NodePath - the best value walking to the left or to the right

        def path_lengths():
            """
            Once each node has been memoizes, generates the values of the paths from each node to find
            length of the best path from each node.
            """
            for node, (left, right) in node_walks.items():
                yield max(left, right, left + right - node.val)

        def search(node):
            if node is None:
                return 0
            elif node in node_walks:
                return max(node_walks[node])

            walk_left = node.val + max(0, search(node.left))
            walk_right = node.val + max(0, search(node.right))
            node_walks[node] = walk_left, walk_right
            return max(walk_left, walk_right)

        search(root)
        return max(path_lengths())
