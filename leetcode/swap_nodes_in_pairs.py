class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_node = ListNode(0)
        dummy_node.next = head
        p = dummy_node
        while p.next and p.next.next:
            first_node = p.next
            second_node = p.next.next
            first_node.next = second_node.next
            second_node.next = first_node
            p.next = second_node
            p = p.next.next
        return dummy_node.next
