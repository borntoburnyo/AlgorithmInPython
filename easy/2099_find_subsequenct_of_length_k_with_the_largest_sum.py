class Solution:
	def maxSubsequence(self, nums, k):
		# utilize the heapq.nlargest function
		# use the sorted function with key option
		self.heap = nums
		self.k = k
		heapq.heapify(self.heap)
		klargest = sorted(heapq.nlargest(self.k, self.heap), key=lambda x: x[-1])
		
		return [i for i,x in klargest]
