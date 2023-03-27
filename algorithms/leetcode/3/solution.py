from collections import defaultdict

class Solution(object):
    def newDefaultDict(self):
        return defaultdict(bool)
    
    def sizeOfDict(self, d):
        return len(d.keys())

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. init default dict
        substring_dict = self.newDefaultDict()
        max_count = 0
        l = 0

        # 2. looop over s
        for i in range(len(s)):
            # Reset case and store result: Duplicate key or end of string
            if substring_dict[s[i]]:
                while True:
                    substring_dict.pop(s[l])
                    l += 1
                    if s[l-1] == s[i]:
                        break
            substring_dict[s[i]] = True
            max_count = max(max_count, self.sizeOfDict(substring_dict))

        return max_count
