import heapq
class Solution:
	def maxProduct(self, nums):
		# utilize the python built-in heap priority queue class
		self.heap = nums
		heapq.heapify(self.heap)	
		res = []
		for i in heapq.nlargest(2, self.heap):
			res.append(i)

		return (res[0]-1)*(res[1]-1)

	def maxProduct2(self, nums):
		# utilize the heap priority queue to pop the max one at a time
		self.heap = [-x for x in nums]
		heapq.heapify(self.heap)
		
		return (-1*heapq.heappop(self.heap)-1) * (-1*heapq.heappop(self.heap)-1)
