"""
1 1 1 1 1 1 1
1 2 3 4 5 6 7
1 3 _ _ _ _ _
1 _ _ _ _ _ .

m=3-1, n=3-1, i=0,j=0
m,i | 1 1 1
m,i | 1 2 2
m,i | 1 3 5 
"""
class Solution(object):
    def dfsSolution(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.paths = 0

        def dfs(m, n, i=0, j=0):
            # Base: OOB
            if i > m or j > n:
                return

            # Base: Correct end index
            if i == m and j == n:
                self.paths += 1

            # Take all paths
            dfs(m, n, i+1, j)
            dfs(m, n, i, j+1)
        
        dfs(m-1, n-1)
        return self.paths

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. Define empty m x n matrix
        matrix = [[0]*n]*m
        
        # 2.1 Populate top row = 1
        for j in range(n):
            matrix[0][j] = 1
        # 2.2 Populate left col = 1
        for i in range(m):
            matrix[i][0] = 1
        
        # 3. Populate middle of array
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        # 4. Return end index
        return matrix[m-1][n-1]

