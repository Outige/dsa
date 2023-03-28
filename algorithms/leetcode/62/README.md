# DFS
So for the first solution I used dfs. I would recurse left and down until either oob or I hit the desired m,n index. If I hit the index I would inc and return. I then returned the global variable I was incrementing.

Unsure of complexity

# DP
FOr the dp problem it is somewhat explained in the code. But essentially the goal is the think of the problem as a matrix and at each index in the matrix, the value indicates how many unique combinations to get there. Then at any index the value will be the sum of the index above or to the left.

So the goal is to fill in the starting values/known values. I know I can fill in the top row and left col as 1 since you can only go right or down. Then the middle section of the matrix we can just use the algorithm of up + left.

Unsure of complexity
