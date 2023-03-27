# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeToList(self, tree, tree_list):
        # base case: Terminal node
        if tree is None:
            tree_list.append(None)
            return
        
        tree_list.append(tree.val)
        self.treeToList(tree.left, tree_list)
        self.treeToList(tree.right, tree_list)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_list = []
        self.treeToList(p, p_list)
        q_list = []
        self.treeToList(q, q_list)

        # Edge: Lists don't match in size; Think
        if len(p_list) != len(q_list):
            return False
        
        for i in range(len(p_list)):
            if p_list[i] != q_list[i]:
                return False
        
        return True
