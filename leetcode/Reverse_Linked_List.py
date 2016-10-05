# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_node = None
        cur_node = head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return pre_node

