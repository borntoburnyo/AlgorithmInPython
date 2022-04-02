class Solution:
    def romanToInt(self, s):
        hmap = dict(zip(['I','V','X','L','C','D';'M'], [1,5,10,50,100,500,1000]))
        res = 0
        for i in range(len(s)-1):
            if hmap[s[i+1]] > hmap[s[i]]:
                res -= hmap[s[i]]
            else:
                res += hmap[s[i]]

        return res + hmap[s[-1]]

# Pure math problem
