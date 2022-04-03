class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums) - 1
        # Find the first number that is not in ascedning order from right to left
        while i > 0:
            if nums[i] > nums[i-1]:
                break
            else:
                i -= 1
        if i == 0:
            nums.reverse()
        # Find the smallest number that is greater than the pivot number we just find and swap them
        while j >= i:
            if nums[j] > nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
                break
            else:
                j -= 1
        # Sort the numbers after the pivot number in ascending order
        l, r = i, len(nums) - 1
        while l < r:
            nums[l],nums[r] = nums[r], nums[l] 
            l += 1
            r -= 1
            
