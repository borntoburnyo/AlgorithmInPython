class Solution:
    def lenghOfLongestSubstring(self, s):
        # hash map to store visited character index
        hmap = {}

        # left index to start with
        left = 0

        res = 0

        for i, char in enumerate(s):
            if char in hmap and hmap[x] >= left:
                left = hmap[char] + 1 # Update the left index rolling forward
            else:
                res = max(res, i - left + 1) # O/W update the return value

            hmap[x] = i # Update hash map

        return res