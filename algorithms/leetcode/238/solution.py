class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # EdgeCase: size == 2
        if len(nums) == 2:
            return [nums[1], nums[0]]

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        result = [0] * len(nums)

        # Calculate prefix
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix[i] = product
        
        # Calculate postfix
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix[i] = product
        
        
        # Calculate result
        for i in range(len(nums)):
            # End case:
            if i+1 >= len(nums):
                post_product = 1
            else:
                post_product = postfix[i+1]
            
            # Start case:
            if i-1 < 0:
                pre_product = 1
            else:
                pre_product = prefix[i-1]
            
            result[i] = pre_product * post_product
        return result
