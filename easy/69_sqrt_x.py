class Solution:
    def mySqrt(self, x):
        l, r = 1, x // 2 # Left and right number
        if x == 0:
            return 0

        # Binary search
        while l < r:
            if r ** 2 > x:
                r = ceil(x / 2) # Decrease right index
            else:
                l = r
                r += 1
        
        return l
