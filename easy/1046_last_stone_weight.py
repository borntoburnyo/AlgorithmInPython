class Solution:
	def lastStoneWeight(self, stones):
		self.heap = [-x for x in stones]
		heapq.heapify(self.heap)
		while len(self.heap) > 1 and self.heap[0] != 0:
			heapq.heappush(self.heap, heapq.heappop() - heapq.heappop())
		
		return -self.heap[0]

# negative to utilize the feature that heap[0] is the minimum
# utilize the feature that heappop will always pop the minimum and maintain heap invariant
