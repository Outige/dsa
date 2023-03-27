class Solution(object):
    def nSquaredSolution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_sum = -2**32
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                best_sum = max(current_sum, best_sum)
        return best_sum

    def nSolution(self, nums):
        best = -2**32
        current = 0
        for num in nums:
            if current < 0:
                current = num
            else:
                current += num
            best = max(current, best)
        return best
            

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.nSolution(nums)
