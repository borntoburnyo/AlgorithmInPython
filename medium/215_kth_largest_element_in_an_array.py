class Solution:
	# Utilize the heap priority queue
	def findKthLargest(self, nums, k):
		self.heap = nums
		self.k = k
		heapq.heapify(self.heap)
		return heapq.nlargest(self.k, self.heap)[-1]
