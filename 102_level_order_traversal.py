from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        traversal_queue = deque()
        traversal_queue.append((root, 1))

        values = []

        current_depth = 0
        while len(traversal_queue) > 0:
            current_node, depth = traversal_queue.popleft()

            # Reached a new level. Add another list to values.
            if depth > current_depth:
                current_depth = depth
                values.append(list())

            values[-1].append(current_node.val)

            if current_node.left:
                traversal_queue.append((current_node.left, depth + 1))
            if current_node.right:
                traversal_queue.append((current_node.right, depth + 1))

        return values