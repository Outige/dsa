class Solution(object):
    def numsToAbsoluteNums(self, nums):
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
    
    def squareNums(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
    
    def findFirstPostive(self, nums):
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i
        return len(nums)

    def findLastNegative(self, positive_pointer):
        return positive_pointer -1

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        positive_pointer = self.findFirstPostive(nums)
        negative_pointer = self.findLastNegative(positive_pointer)

        while negative_pointer >= 0 and positive_pointer < len(nums):
            # Case: Pick the next postive
            if nums[positive_pointer] ** 2 <= nums[negative_pointer] ** 2:
                result.append( nums[positive_pointer]**2 )
                positive_pointer += 1
            
            # Case: Pick the next negative
            else:
                result.append( nums[negative_pointer]**2 )
                negative_pointer -= 1

        while negative_pointer >= 0:
            result.append( nums[negative_pointer]**2 )
            negative_pointer -= 1

        while positive_pointer < len(nums):
            result.append( nums[positive_pointer]**2 )
            positive_pointer += 1

        return result
