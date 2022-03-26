class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[(l+r)//2] < target:
                l = (l+r)//2 + 1
            elif nums[(l+r)//2] > target:
                r = (l+r)//2 - 1
            else:
                return (l+r)//2

        return -1
