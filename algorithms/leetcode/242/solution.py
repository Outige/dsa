from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_key_count = defaultdict(int)
        t_key_count = defaultdict(int)
        
        for x in s:
            s_key_count[x] += 1
        for x in t:
            t_key_count[x] += 1
        
        for k in s_key_count.keys():
            if s_key_count[k] != t_key_count[k]:
                return False
        
        for k in t_key_count.keys():
            if s_key_count[k] != t_key_count[k]:
                return False

        return True
