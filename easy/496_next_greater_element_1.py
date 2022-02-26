class Solution:
	def nextGreaterElement(self, nums1, nums2):
		hmap, stk = {}, []
		for x in nums2:
			if not stk or stk[-1] >= x:
				stk.append(x)
			else:
				while stk and stk[-1] < x:
					hmap[stk.pop()] = x
				stk.append(x)

		res = []
		for x in num1:
			if x in hmap:
				res.append(hmap[x])
			else:
				res.append(-1)
		
		return res
