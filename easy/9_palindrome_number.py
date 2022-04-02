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

# Could reverse the number and compare

    def isPalindrome(self, x):
        l, r = 0, len(str(x))-1
        while l < r:
            if str(x)[l] == str(x)[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True
# Could use two pointers to loop through
