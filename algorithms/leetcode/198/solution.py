class Solution(object):
    def dfsRob(self, nums, i, bounty):
        # Base: OOB
        if i >= len(nums):
            return bounty
        
        one = self.dfsRob(nums, i+2, bounty + nums[i])
        two = self.dfsRob(nums, i+3, bounty + nums[i+1]) if i+1 < len(nums) else 0

        return max(one, two)
        
        """
        0
        _
        1 2 3 1
        """
        return 4

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
        


s = Solution()
assert s.rob([1,2,3,1]) == 4 == s.dfsRob([1,2,3,1], 0, 0)
assert s.rob([2,7,9,3,1]) == 12 == s.dfsRob([2,7,9,3,1], 0, 0)
assert s.rob([2,1,1,2]) == 4 == s.dfsRob([2,1,1,2], 0, 0)
