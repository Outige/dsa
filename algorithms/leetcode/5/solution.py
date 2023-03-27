class Solution(object):
    def longestPFromLToR(self, s, l, r):
        best = [1, 0] # negative distance
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                # aba
                best = [l, r]
            else:
                break
            l -= 1
            r += 1
        return best

    def cmp(self, a, b):
        a_distance = a[1] - a[0]
        b_distance = b[1] - b[0]
        if a_distance > b_distance:
            return 1
        elif a_distance == b_distance:
            return 0
        elif a_distance < b_distance:
            return -1
    
    def longestPalindromeFromCurrentPostion(self, s, i):
        # odd case
        odd_best = self.longestPFromLToR(s, i, i)
        
        # even case
        even_best = self.longestPFromLToR(s, i, i+1)

        if even_best and self.cmp(even_best, odd_best) >= 0:
            return even_best
        
        return odd_best

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = [0, 0]
        for i in range(len(s)):
            current = self.longestPalindromeFromCurrentPostion(s, i)
            if self.cmp(current, best) >= 0:
                best = current
                
        return s[best[0]:best[1]+1]
