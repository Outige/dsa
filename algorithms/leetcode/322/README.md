So basically I create an array that is the length of the amount +1

```
amount = 11
coins = [1, 2, 5]
dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

With each index in DP indicating the min to create that amount of money.

The whole array initializes to None. After looping or during lookback if a None is in the array it means you can't make this value out of the coins

If the current index if present in coins (lookup in O(1) thanks to our hashmap) then the min is 1. Else what we do is try
        min(i - coin in coins + 1)

In english we do a look back i - some coin value for every coin value. And we get the min of this +1 (since it will take 1 more of those coins to get to our current position). If it's a None we just ignore this since its's impossible. 

Here is what the loop might look like:

```
Before i=0
    0     1     2     3     4     5     6     7     8     9    10    11
[None, None, None, None, None, None, None, None, None, None, None, None]


    0     1     2     3     4     5     6     7     8     9    10    11
[None, None, None, None, None, None, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1, None, None, None, None, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1, None, None, None, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2, None, None, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2, None, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1, None, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1,    2, None, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1,    2,    2, None, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1,    2,    2,    3, None, None, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1,    2,    2,    3,    3,    2, None]

    0     1     2     3     4     5     6     7     8     9    10    11
[None,    1,    1,    2,    2,    1,    2,    2,    3,    3,    2,    3]
```

Then just return dp[amount].

With some edge case handling around None and amount = 0
