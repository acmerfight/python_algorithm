# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node_index = 2
        last_odd_node = head
        node = head.next
        first_even_node = last_even_node = head.next
        while node:
            if node_index % 2 == 1:
                last_odd_node.next = node
                last_odd_node = node
            elif node_index % 2 == 0 and node_index > 2:
                last_even_node.next = node
                last_even_node = node
            node_index += 1
            node = node.next
        if last_odd_node:
            last_odd_node.next = first_even_node
        if last_even_node:
            last_even_node.next = None
        return head


node = head = ListNode(1)
for i in xrange(2, 4):
    node.next = ListNode(i)
    node = node.next

Solution().oddEvenList(head)

while head:
    print head.val
    head = head.next
