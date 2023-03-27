class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.count = 0
        
        def dfs(i, j):
            # stop on oob
            if i >= len(grid) or i < 0:
                return
            if j >= (len(grid[0])) or j < 0:
                return
            
            # Case: Currently not an island
            if grid[i][j] == "0":
                return
            
            # Delete land mass and traverse in all directions
            grid[i][j] = "0"
            dfs(i+1, j+0)
            dfs(i+0, j+1)
            dfs(i-1, j+0)
            dfs(i+0, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.count += 1
                    dfs(i, j)
        return self.count
