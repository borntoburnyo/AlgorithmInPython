class Solution:
	def threeSum(self, nums):
		nums = sorted(nums)
		R = []
		for i in range(len(nums)-2):
			if nums[i] > 0:
				break
			j,k = i+1, len(nums)-1
			while j < k:
				if nums[i] + nums[j] + nums[k] > 0:
					k -= 1
				elif nums[i] + nums[j] + nums[k] < 0:
					j += 1
				else:
					R.append([nums[i], nums[i], nums[k]])
				while j < k and nums[j] == nums[j+1]:
					j += 1
				while j < k and nums[k] == nums[k-1]:
					k -= 1
				j += 1
				k -= 1
		return R
