# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        link_list_index = 1
        pre_node = None
        cur_node = head
        m_pre_node = m_node = None
        while cur_node:
            next_node = cur_node.next
            if link_list_index == m:
                m_pre_node = pre_node
                m_node = cur_node
            elif m < link_list_index <= n:
                cur_node.next = pre_node
                if link_list_index == n:
                    if m_pre_node:
                        m_pre_node.next = cur_node
                    m_node.next = next_node
                    if m == 1:
                        head = cur_node
                    return head
            pre_node = cur_node
            cur_node = next_node
            link_list_index += 1
        return head
