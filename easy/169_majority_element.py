class Solution:
	def majorityElement(self, nums):
		majority, count = nums[0], 0
		for x in nums:
			if x == majority:
				count += 1
			elif count == 0:
				majority, count = x, 1
			else:
				count -= 1
		return majority
