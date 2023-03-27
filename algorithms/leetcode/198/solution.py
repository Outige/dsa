class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)

        robValues = [0]*len(nums)
        robValues[0] = nums[0]
        robValues[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            robValues[i] = max(nums[i] + robValues[i-2], robValues[i-1])
        return max(robValues)
