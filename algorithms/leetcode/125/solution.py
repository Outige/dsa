class Solution(object):
    def formatString(self, s):
        result = []
        for x in s:
            lower_x = x.lower()
            if lower_x.isalnum():
                result.append(lower_x)
        return ''.join(result)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = self.formatString(s)

        l = 0
        r = len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
