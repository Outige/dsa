# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursiveInvertTree(self, root):
        # Base:
        if root is None:
            return
        
        left = root.left
        root.left = root.right
        root.right = left

        self.recursiveInvertTree(root.left)
        self.recursiveInvertTree(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.recursiveInvertTree(root)
        return root
