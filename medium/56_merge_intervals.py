class Solution:
	def merge(self, intervals):
		R = []
		for lst in sorted(intervals):
			if R and R[-1][1] >= lst[0]:
				R[-1][1] = max(lst[1], R[-1][1])
			else:
				R.append(lst)	
	return R
