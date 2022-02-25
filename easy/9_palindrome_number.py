class Solution:
	def isPalindrome(self, x):
		if x < 0:
			return False
		else:
			x_cp = x
			rev = 0
			while x > 0:
				rev = rev*10 + x%10
				x = x // 10
		return rev == x_cp
