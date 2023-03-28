class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = collections.defaultdict(int)
        res = 0

        l = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
