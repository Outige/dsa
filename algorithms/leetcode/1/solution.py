class Solution(object):
    def cacheNums(self, nums):
        cache = {}
        for i in range(len(nums)):
            cache[nums[i]] = i
        return cache

    def isCacheHit(self, nums, target, i, cache):
        key = target - nums[i]
        if cache.get(key, None) is not None:
            return True
        
        return False
    
    def isDuplicateIndex(self, nums, target, i, cache):
        return cache[target-nums[i]] == i
    
    def mapIndexToResultArray(self, nums, target, i, cache):
        return [i, cache[target-nums[i]]]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = self.cacheNums(nums)

        for i in range(len(nums)):
            if self.isCacheHit(nums, target, i, cache):
                if not self.isDuplicateIndex(nums, target, i, cache):
                    return self.mapIndexToResultArray(nums, target, i, cache)
        
        return []
