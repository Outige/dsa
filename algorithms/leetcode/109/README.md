# Explanation of solution
Time take: 90 mins

The first step was to implement a standard `insert` function for the BST.

The second step is to turn the LinkedList(LL) into an array via `listNodeToArray`.

```
0 -> 1 -> 2 -> 3 -> 4 -> 5 ==> [0, 1, 2, 3, 4, 5]
```

The next step is to initialize our tree with a valid median. Making use of `calculate_median` which behaves like (the output is the index):
```
[0, 1, 2, 3] => 2
[0, 1, 2] => 1
[0, 1] => 0
```
So in our case:
```
[0, 1, 2, 3, 4, 5] => 3
So our tree is
 3
/ \
```

Then we recursively call a function that will shrink our pointers and find the median in this shrunken space. Note that our original median will be attempted to be inserted again. Our insert function will just ignore this.

The stack trace looks like:
``` 
    l              m         r
[   0,   1,   2,   3,   4,   5   ] => 3

    l    m    r
[   0,   1,   2,   3,   4,   5   ] => 1

    lmr
[   0,   1,   2,   3,   4,   5   ] => 0

              lmr
[   0,   1,   2,   3,   4,   5   ] => 2

                        l    mr
[   0,   1,   2,   3,   4,   5   ] => 5

                        lmr
[   0,   1,   2,   3,   4,   5   ] => 4
```


# Issues faced

1. At first I simply inserted the median and then looped over the array to insert
1. My next move was to loop from the median to the beginning and then from the median to the end.

Both were incorrect since I needed to be inserting the median at every step.

Next I faced issues for not considering the base case where l == r. I knew that the median would be added and it would be l == m == r. But I should also terminate here. So that there isn't an endless loop by unnecessarily calling the left and right recursion.

Finally I forgot to map the median pointer back to the original array. By doing m = l + m.

## Take away

BST balancing doesn't just depend on the root. It is insert order dependent.

I believe this subdivision of an array is a common solution pattern. So the learning of mapping the median correctly as well as the len=1 base case is a good thing to remember.



# Performance

The problem can at best be solved in O(n) time since every node needs to be visited.

- Space: O(n)
- Time: Loop over tree_array * insert = O(n) * O(log(n)) = O(nlogn)
