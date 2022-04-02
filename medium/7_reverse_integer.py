class Solution:
	def reverse(self, x):
		sign = -1 if x < 0 else 1
		if x < 0:
			x = -x
		rev = 0
		while x != 0:
			rev = rev * 10 + x % 10
			x = x // 10
			return 0 if rev > 2**31 - 1
		return sign*rev

# x = (x//10)*10 + x%10
