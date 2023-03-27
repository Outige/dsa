# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# .
# 1 -> 2 -> 4
# .
# 1 -> 3 -> 4
class Solution(object):
    def isolateNodeFromList(self, l):
        isolatedNode = l
        l = l.next
        isolatedNode.next = None
        return (isolatedNode, l)

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list3 = None
        current = None
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                (node, list1) = self.isolateNodeFromList(list1)
            else:
                (node, list2) = self.isolateNodeFromList(list2)

            if current is None:
                list3 = node
                current = node
            else:
                current.next = node
                current = current.next
        
        # Cleanup
        if list1 is not None:
            if current is not None:
                current.next = list1
            else:
                list3 = list1
        elif list2 is not None:
            if current is not None:
                current.next = list2
            else:
                list3 = list2
        return list3
