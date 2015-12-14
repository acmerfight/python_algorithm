class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current_node = dummy
        while l1 and l2:
            if l1.val > l2.val:
                current_node.next = l2
                l2 = l2.next
            else:
                current_node.next = l1
                l1 = l1.next
            current_node = current_node.next
        if l1:
            current_node.next = l1
        else:
            current_node.next = l2
        return dummy.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cur = ListNode(None)
        head = cur
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        cur.next = l1 if l1 else l2
        return head.next
