class Solution(object):
    def numsToAbsoluteNums(self, nums):
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
    
    def squareNums(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.numsToAbsoluteNums(nums)
        nums.sort()
        self.squareNums(nums)
        
        return nums
