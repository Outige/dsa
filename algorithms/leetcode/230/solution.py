# Help from: https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/63829/python-easy-iterative-and-recursive-solution/?orderBy=most_votes
class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        return self.helper(root)
    
    def helper(self, root):
        if root is None:
            return None
        
        # Traverse left subtree, return if kth smallest found
        left = self.helper(root.left)
        if left is not None: return left

        # Current node is kth smallest
        self.k -= 1
        if self.k == 0:
            return root.val
        
        # Traverse left subtree, return if kth smallest found
        right = self.helper(root.right)
        if right is not None: return right
