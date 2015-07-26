# Definition for singly-linked list.

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy_node = ListNode(0)
        dummy_node.next = head
        current_node = dummy_node
        while current_node and current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummy_node.next
