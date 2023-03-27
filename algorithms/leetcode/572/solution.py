# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findPossibleSubRoots(self, root, val, subRoots):
        # Base: Terminal node
        if root is None:
            return False
        
        if root.val == val:
            subRoots.append(root)
        
        self.findPossibleSubRoots(root.left, val, subRoots)
        self.findPossibleSubRoots(root.right, val, subRoots)
    
    def areRootsEqual(self, root1, root2):
        if root1 is None:
            if root2 is None:
                return True
            else:
                return False
        elif root2 is None:
            return False
        
        if root1.val != root2.val:
            return False
        
        return self.areRootsEqual(root1.left, root2.left) and self.areRootsEqual(root1.right, root2.right)

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            val = None
        else:
            val = subRoot.val

        subRoots = []
        self.findPossibleSubRoots(root, val, subRoots)
        for r in subRoots:
            if self.areRootsEqual(subRoot, r):
                return True
        return False
