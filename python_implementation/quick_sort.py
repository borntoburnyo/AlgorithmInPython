class quick_sort:
	def __init__(self, nums):
		self.nums = nums
	
	def sort(self, p, r):
		if p < r:
			q = self.partition(p, r)
			self.sort(p, q-1)
			self.sort(q+1, r)
		
		return self.nums

	def partition(self, p, r):
		# using the last value of the list as pivot value
		x = self.nums[r-1]
		i = p - 1
		# find small values and keep them at the first half
		for j in range(p, r-1):
			if self.nums[j] <= x:
				i += 1
				self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
		self.nums[i+1], self.nums[r-1] = self.nums[r-1], self.nums[i+1]
		return i+1

qs = quick_sort([2,8,7,1,3,5,6,4])
print(qs.sort(0, 8))
