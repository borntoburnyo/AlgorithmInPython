class Solution:
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            tryOne = s[l+1 : r+1]
            tryTwo = s[l : r]
            return tryOne == iryOne[::-1] or tryTwo == tryTwo[::-1]
        l += 1
        r -= 1

        return True

# Once find no match, compare if worth going forward
# If not, return False directly
