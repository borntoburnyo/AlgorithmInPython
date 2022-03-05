class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            # Determines if it is worth to add previous element
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
