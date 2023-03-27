# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visted = {}
        while head is not None:
            if visted.get(head, False):
                return head
            visted[head] = True
            head = head.next
        return None
