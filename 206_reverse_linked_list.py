# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        cycle_detector = set()

        repr_string = ''
        node = self
        while node.next:
            repr_string += '(' + str(node.val) + ')' + ' -> '
            if node in cycle_detector:
                return repr_string + ' *** Cycle Detected *** '
            else:
                cycle_detector.add(node)
            node = node.next
        repr_string += '(' + str(node.val) + ')' + ' -> ' + 'None'
        return repr_string

    @staticmethod
    def from_sequence(sequence):
        if len(sequence) == 0:
            return None
        head = ListNode(sequence[0])
        node = head
        for value in sequence[1:]:
            node.next = ListNode(value)
            node = node.next
        return head

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        >>> s = Solution()
        >>> ll = ListNode.from_sequence(range(10))
        >>> str(s.reverseList(ll)) == str(ListNode.from_sequence(range(10)[::-1]))
        True

        Reverse a linked list.
        :param head:
        :return:
        """
        if head.next is None:
            return head

        new_head = self.reverseList(head.next)
        # The node ahead of the current node should be set to point at the current node.
        head.next.next = head
        # If this node should have a next, it will be set in the next recursive call. Otherwise, it should be None.
        # Specifically handles the corner case of the original head becoming the tail. Without this case, there will
        # be a cycle between the original head and the node that it originally pointed to.
        head.next = None
        return new_head


print(str(ListNode.from_sequence(range(0, 10, -1))))