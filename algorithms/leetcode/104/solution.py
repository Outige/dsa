# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursiveMaxDepth(self, root, depth):
        # base case: terminal node
        if root is None:
            return depth-1
        
        # Std case: return max(depth, root.left, root.right)
        max_depth = max(depth, self.recursiveMaxDepth(root.left, depth+1))
        max_depth = max(max_depth, self.recursiveMaxDepth(root.right, depth+1))
        return max_depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursiveMaxDepth(root, 1)
