from typing import List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Given k linked lists with sorted value, return a single linked list with all sorted values.
        :param lists:
        :return:
        """

        def merge_two_lists(first, second):
            if not first:
                return second
            if not second:
                return first

            if first.val < second.val:
                root = first
                first = first.next
            else:
                root = second
                second = second.next

            current = root
            while first and second:
                if first.val < second.val:
                    current.next = first
                    first = first.next
                else:
                    current.next = second
                    second = second.next
                current = current.next

            if first:
                current.next = first
            elif second:
                current.next = second

            return root

        if len(lists) == 0:
            return None

        queue = deque(lists)

        # Merge each pair of lists until there is only one. Because the merged lists are placed at the first of the
        # deque, and the pairs of lists are being popped off of the back, we get O(n * log(k)) runtime.
        # If we merge the lists and add them to the same size, then we get O(n * k) runtime, and that is bad.
        while len(queue) > 1:
            queue.appendleft(merge_two_lists(queue.pop(), queue.pop()))

        return queue.pop()
