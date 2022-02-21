class Solution:
	# Use two pointer than traverse in different speed
	def removeElement(self, nums):
		i = 0
		for x in nums:
			if x != val:
				nums[i] = x
				i += 1
		return i
