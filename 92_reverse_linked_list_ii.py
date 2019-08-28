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
    """
    TODO: Finish
    """
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            stop = left == right or right.next == left


            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        if not head:
            return None

        left, right = head, head
        stop = False


        recurseAndReverse(right, m, n)
        return head

s = Solution()
ll = ListNode.from_sequence(range(10))
print(ll)
r = s.reverseBetween(ll, 2, 4)
print(r)
