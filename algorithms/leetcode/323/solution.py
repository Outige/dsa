from typing import (
    List,
)
"""
Array 0 to n-1, each index is a set of neighbors

Once you dfs on a node you add it to visited.
Loop over the nodes neighbor. dfs and remove from set. If a node is visited remove from set. Return once no more
0: {_}
1: {0,2}
2: {1}

3:{4}
4:{3}

Loop over the n and if not visited visited and add component count

visited = {}
components = 1
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Create adjacency sets
        neighbors = [None] * n
        for i in range(n):
            neighbors[i] = set()
        
        for a,b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a) # If I just get rid of this I think we get to the same solution

        visited = set()

        def dfs(i):
            visited.add(i)
            while len(neighbors[i]) > 0:
                neighbor = neighbors[i].pop()
                if i in neighbors[neighbor] and neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count

s = Solution()
"""
0-1     3
  |     |
  2     4
"""
assert s.countComponents(n=5, edges=[[0,1],[1,2],[3,4]]) == 2

"""
0 1 2 3 4
"""
assert s.countComponents(n=5, edges=[]) == 5

"""
0-1-2
|  /
3-4
"""
assert s.countComponents(n=5, edges=[ [0,1], [1,2], [2,4], [4,3], [3,0] ]) == 1

"""
-----
|   |
0-1-2

3-4

5
"""
assert s.countComponents(n=6, edges=[ [0,1], [1,2], [2,0], [3,4] ]) == 3
