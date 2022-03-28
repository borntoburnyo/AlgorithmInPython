class Solution:
    def minDeletion(self, nums):
        i = 0
        n = len(nums)
        res = 0
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[i+1]:
                res += 1
                j += 1

            if j < n:
                i = j + 1
            else:
                res += 1
                return res
        
        return res

# Imagine 1 2 | 3 4 | 6 6 | 6 7 | .....
# The idea is to loop through the list make sure every pair is legal
# Straightforward coding
