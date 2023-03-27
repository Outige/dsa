from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = defaultdict(bool)

        for x in nums:
            if visited[x] == True:
                return True
            visited[x] = True
        return False
