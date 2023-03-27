I tried to do a two pointer solution like "most water" in problem which was wrong! Then thought a bit more about it and settled on the right approach

Time: O(n)
Space: O(n)

The solution involves keeping a dynamic memory of the best purchase prices at any give day.

```
  [7,1,5,3,6,4]
=>[7,1,1,1,1,1]
or
  [7,6,4,3,1]
=>[7,6,4,3,1]
```

Then you just loop over the original nums array and find the best diff between the dynamic memory we created earlier. This will catch the best case being 0 by default if all days are worse than previous days