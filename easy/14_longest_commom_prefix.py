class Solution:
    def longestCommonPrefix(self, strs):
        # Sort the list of strings
        strs.sort()
        smallest = strs[0]
        biggest = strs[len(strs)-1]
        for i, char in enumerate(smallest):
            # If the character in ith place from the smallest string does not match with the biggest string
            if char != biggest[i]:
                return smallest[:i]

        # If it loops through the entire smallest string
        return smallest
