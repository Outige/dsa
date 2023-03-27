class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
         _        _        _
        [4, 5, 6, -1, 0, 1, 2]
        """
        def findM(start, mid, end):
            # Base: start is min. So return
            if nums[start] <= nums[end]:
                return nums[start]
            
            # Base: Minimal subcase. ie min is either start or end
            if end-start == 1:
                return min(nums[end], nums[start])

            # min is in the right subarray
            if nums[mid] > nums[end]:
                return findM(mid, mid+int((end-mid)/2), end)
            
            # min is in the left sub array
            if nums[start] > nums[mid]:
                return findM(start, start+int((mid-start)/2), mid)

        return findM(0, int((len(nums)-1)/2), len(nums)-1)
