class Solution:
	def kWeakestRows(self, mat, k):
		self.nums = [(sum(x),i) for i,x in enumerate(mat)]
		# utilize the built-in sort feature in Python
		self.nums.sort()
		return [x for i,x in self.nums[:k]]
