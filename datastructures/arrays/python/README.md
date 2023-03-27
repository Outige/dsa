This README tries to discuss the implementation of the python array (List)

# Performance

| Operation             | Average Case  | Amortized Worst Case  |
|-----------------------|---------------|-----------------------|
|  Copy                 | O(n)          | O(n)                  |
|  Append[1]            | O(1)          | O(1)                  |
|  Pop last             | O(1)          | O(1)                  |
|  Pop intermediate[2]  | O(n)          | O(n)                  |
|  Insert               | O(n)          | O(n)                  |
|  Get Item             | O(1)          | O(1)                  |
|  Set Item             | O(1)          | O(1)                  |
|  Delete Item          | O(n)          | O(n)                  |
|  Iteration            | O(n)          | O(n)                  |
|  Get Slice            | O(k)          | O(k)                  |
|  Del Slice            | O(n)          | O(n)                  |
|  Set Slice            | O(k+n)        | O(k+n)                |
|  Extend[1]            | O(k)          | O(k)                  |
|  Sort                 | O(n log n)    | O(n log n)            |
|  Multiply             | O(nk)         | O(nk)                 |
|  x in s               | O(n)          |                       |
|  min(s), max(s)       | O(n)          |                       |
|  Get Length           | O(1)          | O(1)                  |



# Sources

- [Python time complexity wiki](https://wiki.python.org/moin/TimeComplexity)
