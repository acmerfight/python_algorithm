#Given a linked list, determine if it has a cycle in it.
#
#Follow up:
#    Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        p1 = p2 = head
        while p2 is not None and p2.next is not None:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                return True
        return False
