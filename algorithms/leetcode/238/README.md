So I basically just googled this one. Kind of shameful.

The idea is that you loop over nums and store the running product from the front. And in reverse. Then you loop over nums and return the product of pre[i-1] and post[i+1]. With i == 0 and i == len(nums) being edge cases

Performance:
- Time: O(n)
- Space: O(n)

# Resources

- [explanation](https://www.youtube.com/watch?v=bNvIQI2wAjk)
