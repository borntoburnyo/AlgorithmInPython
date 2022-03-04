class Solution:
    def numberOfArithmeticSlices(self, nums):
        res = 0
        dp = [0]*len(nums)
        for i in range(len(nums)-2):
            if nums[i+2] - nums[i+1] == nums[i+1] - nums[i]:
                dp[i] = 1 + dp[i-1]
                res += dp[i]
        return res
