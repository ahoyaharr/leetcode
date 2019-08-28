from collections import deque
import ast

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    >>> root = TreeNode(1)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(3)
    >>> root.right.left = TreeNode(4)
    >>> root.right.right = TreeNode(5)
    >>> c = Codec()
    >>> serialized = c.serialize(root)
    >>> serialized
    '[1, 2, 3, None, None, 4, 5]'
    >>> deserialized = c.deserialize(serialized)
    >>> deserialized.val
    1
    >>> deserialized.left.val
    2
    >>> deserialized.right.val
    3
    >>> type(deserialized.left.left)
    <class 'NoneType'>
    >>> deserialized.right.left.val
    4
    >>> serialized == c.serialize(deserialized)
    True
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        example -
            1
           / \
          2   3
             / \
            4   5
        to [1,2,3,null,null,4,5]

        The left and right children of the ith node are serialized by storing their values at 2i and 2i+1 in
        a 1-indexed list of values.

        :type root: TreeNode
        :rtype: str
        """
        def traverse(node, index):
            if node is None:
                return 0

            node_values[index] = node.val

            return max(traverse(node.left, 2 * index),
                       traverse(node.right, 2 * index + 1),
                       index)

        node_values = dict()
        largest_index = traverse(root, 1)

        node_sequence = []
        for index in range(1, largest_index + 1):
            if index in node_values:
                node_sequence.append(node_values[index])
            else:
                node_sequence.append(None)

        return str(node_sequence)

        # 1 -> 2*1, 2*1 + 1
        # 2 -> 2*2, 2*2 + 1


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def construct_tree(index=1):
            # index assumes 1-indexing, but Python is 0-indexed
            if index - 1 >= len(node_values) or node_values[index - 1] is None:
                return

            node = TreeNode(node_values[index - 1])
            node.left, node.right = construct_tree(2 * index), construct_tree(2 * index + 1)

            return node

        node_values = ast.literal_eval(data)
        return construct_tree()
