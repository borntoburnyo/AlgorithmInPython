class Solution:
	def kWeakestRows(self, mat, k):
		self.nums = [(sum(x),i) for i,x in enumerate(mat)]
		# utilize the built-in sort feature in Python
		self.nums.sort()
		return [x for i,x in self.nums[:k]]

	def kWeakestRows(self, mat, k):
		# utilize heap priority queue
		self.nums = [(sum(x),i) for i,x in enumerate(mat)]
		self.k = k
		heapq.heapify(self.nums)		
		idx = []
		while self.k > 0:
			strength, i = heapq.heappop(self.nums)
			idx.append(i)
			k -= 1
		
		return idx
