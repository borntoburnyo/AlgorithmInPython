class Solution:
    def lenghOfLongestSubstring(self, s):
        # hash map to store visited character index
        hmap = {}

        # left index to start with
        left = 0

        res = 0

        for i, char in enumerate(s):
            if char in hmap and hmap[char] >= left:
                left = hmap[char] + 1 # Update the left index rolling forward
            else:
                res = max(res, i - left + 1) # O/W update the return value

            hmap[char] = i # Update hash map

        return res

# Need to memorize the seen characters, use hash map / dictionary
# Then get the desired output based on logic
