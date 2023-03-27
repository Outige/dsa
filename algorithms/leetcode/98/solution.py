class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, None, None)
    
    def validate(self, root, upper, lower):
        if root is None:
            return True
        
        if upper is not None:
            if root.val >= upper:
                return False
        if lower is not None:
            if root.val <= lower:
                return False
        
        left = self.validate(root=root.left, upper=root.val, lower=lower)
        right = self.validate(root=root.right, upper=upper, lower=root.val)

        return left and right
