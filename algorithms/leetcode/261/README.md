# DFS solution
Case:
```
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output: true.
```

The actual problem you want to solve is 1) The graph must be acyclic 2) The graph must be connected

To achieve this I will use 2 tools. 1) An adjacency lookup 2) A visited set


```
adjacencyLookup = {
    0: {1: True, 2: True, 3: True},
    1: {0: True, 4: True},
    2: {0: True},
    3: {0: True},
    4: {1: True}
}

visited = ()
```

Then what I do is run dfs on the 0 element (it could be any valid element).

I first check if this node has been visited. If it has then we found a cycle.
```
            if i in visited:
                return False
```

Then I visit the node
```
            visited.add(i)
```

Then I check if this node has no more edges. If it doesn't then I return.
```
            if True not in edgeLookup[i].values():
                return True
```

Then what I do is I loop through the current nodes edges. I delete it from both the source and destination node and then I dfs on that destination node.
If any of this comes back as False I know at some point down the call stack a loop was discovered and so I can return False.
```
            for k in edgeLookup[i]:
                if edgeLookup[i][k] == True:
                    edgeLookup[i][k] = False
                    edgeLookup[k][i] = False
                    if not dfs(k):
                        return False
```

### Trace
```
dfs(0)
adjacencyLookup = {
    0: {1: True->False, 2: True, 3: True},
    1: {0: True->False, 4: True},
    2: {0: True},
    3: {0: True},
    4: {1: True}
}, visited(0)
dfs(1)
adjacencyLookup = {
    0: {1: False, 2: True, 3: True},
    1: {0: False, 4: True->False},
    2: {0: True},
    3: {0: True},
    4: {1: True->False}
}, visited(0, 1)
dfs(4)
adjacencyLookup = {
    0: {1: False, 2: True, 3: True},
    1: {0: False, 4: False},
    2: {0: True},
    3: {0: True},
    4: {1: False}
}, visited(0, 1, 4)
# no more edges for 4, so return true and return back to dfs(1) call
# no more edges for 1, so return true and return back to dfs(0) call
dfs(2)
adjacencyLookup = {
    0: {1: False, 2: True->False, 3: True},
    1: {0: False, 4: False},
    2: {0: True->False},
    3: {0: True},
    4: {1: False}
}, visited(0, 1, 4, 2)
# no more edges for 2, so return true and return back to dfs(0) call
dfs(3)
adjacencyLookup = {
    0: {1: False, 2: False, 3: True->False},
    1: {0: False, 4: False},
    2: {0: False},
    3: {0: True->False},
    4: {1: False}
}, visited(0, 1, 4, 2, 3)
# no more edges for 3, so return true and return back to dfs(0) call
# no more edges for 0, so return true and return True
adjacencyLookup = {
    0: {1: False, 2: False, 3: False},
    1: {0: False, 4: False},
    2: {0: False},
    3: {0: False},
    4: {1: False}
}, visited(0, 1, 4, 2, 3)

```
