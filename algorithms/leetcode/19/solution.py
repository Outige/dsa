# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def calculateListSize(self, head):
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        return size

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = self.calculateListSize(head)

        n = size-n

        # EC:
        if n == 0:
            return head.next
        
        i = 0
        node = head
        while i < n-1:
            i += 1
            node = node.next
        
        removeNode = node.next
        nextnext = node.next.next
        removeNode.next = None
        node.next = nextnext
        return head
