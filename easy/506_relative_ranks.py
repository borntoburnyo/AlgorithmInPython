class Solution:
	def findRelativeRanks(self, score):
		rank = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + [str(i) for i in range(4, len(score)+1)]
		score_sort = sorted(score, reverse=True)
		dct = dict(zip(score_sort, rank))

		return [dct[i] for i in score]
