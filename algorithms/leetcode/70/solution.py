class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n < setup
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # setup
        stairs = [0]*n
        stairs[0] = 1
        stairs[1] = 2
        
        # main algorithm
        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n-1]
