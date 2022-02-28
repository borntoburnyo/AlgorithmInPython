class Solution:
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            start = i
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start != i:
                res.append("{}->{}".format(nums[start], nums[i]))
            else:
                res.append("{}".format(nums[i])

            i += 1

        return res
