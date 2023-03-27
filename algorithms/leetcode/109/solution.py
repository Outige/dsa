class Solution(object):
    def listNodeToArray(self, head):
        tree_list = []
        while head is not None:
            tree_list.append(head.val)
            head = head.next
        return tree_list

    def insert(self, val, node):
        # Base: Terminal node / equivilance case
        if node is None or node.val == val:
            return

        # Smaller case
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert(val, node.left)

        # Larger case
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insert(val, node.right)

    def calculate_median(self, l, r):
        if r-l >= 0:
            return l+int((r+1-l)/2)

        return -1

    def recursive_median_insert(self, tree, tree_list, l, r):
        median_index = self.calculate_median(l, r)

        if l == r:
            self.insert(tree_list[l], tree)
            return

        if median_index == -1:
            return

        self.insert(tree_list[median_index], tree)
        self.recursive_median_insert(tree, tree_list, l, median_index-1)
        self.recursive_median_insert(tree, tree_list, median_index+1, r)

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        tree_list = self.listNodeToArray(head)
        median_index = self.calculate_median(0, len(tree_list)-1)
        if median_index == -1:
            return None
        print(median_index, tree_list)
        tree = TreeNode(tree_list[median_index])
        self.recursive_median_insert(tree, tree_list, 0, len(tree_list)-1)
        return tree
