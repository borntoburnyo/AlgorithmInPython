class Solution:
    def partitionLabels(self, s):
        last = {} # Store the last index of each letter
        res = []
        # Find the last index of each letter
        for i in range(len(s)):
            last[s[i]] = i

        l, r = 0, 0
        for i, letter in enumerate(s):
            # Update the rightmost index
            r = max(r, last[letter])

            # If find the rightmost index for a complete fraction
            res.append(r - l + 1)
            l = i + 1 # Update left index

        return res
