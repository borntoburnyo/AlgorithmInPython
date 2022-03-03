class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False
        res = 0
        for x in t:
            if res <= len(s) - 1:
                if s[res] == x:
                    res += 1
        return res == len(s)
