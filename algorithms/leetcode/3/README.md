# Explanation of solution

Loop over word.

Have a concept of a left pointer l and a right pointer i. Along the way add the visited letters to a visited dictionary.

If the current letter at pointer i has previously been visited then you need to put the l pointer in first position that will create a substring that doesn't have the letter at i.

So in l and pop out the letters saved from the string at l.

Then at the end of each iteration save the max between the current max and the size of the dict.

Alternatively we could just use i-l instead of dict size.


# Issues faced

My initial solution contained many elements of my final solution but it didn't solve the whole problem. Only a special case.

Initially there was no way to move the left pointer to remove the substring. I would just nuke the whole substring and start again. This worked in a case like:
```
abcda => 3
```

But not in the case
```
dvdf => 2
```

My solution also made use of defaultdict which I had to google.

My solution also made use of dict.pop() which I had to google and I was even unsure of it's performance.


## Take away

1. Learn default dict import
1. Think about your solution carefully in the beginning. It doesn't pay dividends to solve the wrong problem quickly



# Performance

The problem can at best be solved in O(n) time since every node needs to be visited.

- Space: O(n)
- Time: Loop over tree_array * insert = O(n) * O(log(n)) = O(nlogn)
