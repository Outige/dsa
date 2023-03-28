from typing import (
    List,
)

from collections import defaultdict

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        edgeLookup = {}
        for i in range(n):
            edgeLookup[i] = defaultdict(bool)
        visited = set()

        # 1. Construct dict(dict) edge lookup
        for a, b in edges:
            edgeLookup[a][b] = True
            edgeLookup[b][a] = True
        
        def dfs(i):
            if i in visited:
                return False
            
            visited.add(i)
            
            if True not in edgeLookup[i].values():
                return True
            

            for k in edgeLookup[i]:
                if edgeLookup[i][k] == True:
                    edgeLookup[i][k] = False
                    edgeLookup[k][i] = False
                    if not dfs(k):
                        return False
            return True
        


        # Run dfs on any element
        if not dfs(0):
            return False

        # Make sure graph is connected
        for i in range(n):
            if i not in visited:
                return False
        
        return True

s = Solution()
assert True == s.valid_tree(n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]])
assert False == s.valid_tree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
