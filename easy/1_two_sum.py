class Solution:
	def twoSum(self, nums, target):
		nums_d = {n:i for i,n in enumerate(nums)}
		for i in range(len(nums)):
			remn = target - nums[i]
			if remn in nums_d and nums_d[remn] != i:
				return [i, nums_d[remn]]
