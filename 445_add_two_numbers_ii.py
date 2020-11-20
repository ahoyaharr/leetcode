# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1.prev = l2.prev = None
        while l1.next:
            l1.next.prev = l1
            l1 = l1.next
        while l2.next:
            l2.next.prev = l2
            l2 = l2.next

        current_node = None
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            current_node = ListNode(val=v1 + v2, next=current_node)
            if current_node.next and current_node.next.val >= 10:
                current_node.next.val -= 10
                current_node.val += 1

            if l1:
                l1 = l1.prev
            if l2:
                l2 = l2.prev

        if current_node.val >= 10:
            current_node.val -= 10
            current_node = ListNode(val=1, next=current_node)

        return current_node